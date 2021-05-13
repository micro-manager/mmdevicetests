import ctypes
from . import mmdevice

MODULE_INTERFACE_VERSION = 10

_ptr_wrap_func = {
    mmdevice.GenericDevice: mmdevice.wrap_ctypes_generic_pointer,
    mmdevice.CameraDevice: mmdevice.wrap_ctypes_camera_pointer,
    mmdevice.ShutterDevice: mmdevice.wrap_ctypes_shutter_pointer,
    mmdevice.StageDevice: mmdevice.wrap_ctypes_stage_pointer,
    mmdevice.XYStageDevice: mmdevice.wrap_ctypes_xystage_pointer,
    mmdevice.StateDevice: mmdevice.wrap_ctypes_state_pointer,
    mmdevice.SerialDevice: mmdevice.wrap_ctypes_serial_pointer,
    mmdevice.AutoFocusDevice: mmdevice.wrap_ctypes_autofocus_pointer,
    mmdevice.ImageProcessorDevice: mmdevice.wrap_ctypes_imageprocessor_pointer,
    mmdevice.SignalIODevice: mmdevice.wrap_ctypes_signalio_pointer,
    mmdevice.MagnifierDevice: mmdevice.wrap_ctypes_magnifier_pointer,
    mmdevice.SLMDevice: mmdevice.wrap_ctypes_slm_pointer,
    mmdevice.GalvoDevice: mmdevice.wrap_ctypes_galvo_pointer,
    mmdevice.HubDevice: mmdevice.wrap_ctypes_hub_pointer,
}


class DeviceAdapterModule:
    def __init__(self, path):
        self.dll = ctypes.CDLL(path)

        self.dll.InitializeModuleData.restype = None
        self.dll.InitializeModuleData.argtypes = []
        self.dll.CreateDevice.restype = ctypes.c_void_p  # MM::Device*
        self.dll.CreateDevice.argtypes = [ctypes.c_char_p]
        self.dll.DeleteDevice.restype = None
        self.dll.DeleteDevice.argtypes = [ctypes.c_void_p]  # MM::Device*
        self.dll.GetModuleVersion.restype = ctypes.c_long
        self.dll.GetModuleVersion.argtypes = []
        self.dll.GetDeviceInterfaceVersion.restype = ctypes.c_long
        self.dll.GetDeviceInterfaceVersion.argtypes = []
        self.dll.GetNumberOfDevices.restype = ctypes.c_uint
        self.dll.GetNumberOfDevices.argtypes = []
        self.dll.GetDeviceName.restype = ctypes.c_bool
        self.dll.GetDeviceName.argtypes = [
            ctypes.c_uint,
            ctypes.c_char_p,
            ctypes.c_uint,
        ]
        self.dll.GetDeviceType.restype = ctypes.c_bool
        self.dll.GetDeviceType.argtypes = [
            ctypes.c_char_p,
            ctypes.POINTER(ctypes.c_int),
        ]
        self.dll.GetDeviceDescription.restype = ctypes.c_bool
        self.dll.GetDeviceDescription.argtypes = [
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_uint,
        ]

        mv = self.GetModuleVersion()
        if mv != MODULE_INTERFACE_VERSION:
            raise RuntimeError(
                "Device adapter module {} has module interface version {} (expected {})".format(
                    path, mv, MODULE_INTERFACE_VERSION))

    def InitializeModuleData(self):
        self.dll.InitializeModuleData()

    def CreateDevice(self, name):
        if not isinstance(name, bytes):
            name = name.encode()
        ptr = self.dll.CreateDevice(name)
        if not ptr:
            return None
        type = self.GetDeviceType(name)
        try:
            wrap_func = _ptr_wrap_func[type]
        except KeyError:
            self.dll.DeleteDevice(ptr)
            raise
        ret = wrap_func(ptr)
        ret._ctypes_address = ptr  # Save for DeleteDevice()
        return ret

    def DeleteDevice(self, device):
        self.dll.DeleteDevice(device._ctypes_address)

    def GetModuleVersion(self):
        return int(self.dll.GetModuleVersion())

    def GetDeviceInterfaceVersion(self):
        return int(self.dll.GetDeviceInterfaceVersion())

    def GetNumberOfDevices(self):
        return int(self.dll.GetNumberOfDevices())

    def GetDeviceName(self, index):
        name = ctypes.create_string_buffer(mmdevice.MaxStrLength)
        ok = self.dll.GetDeviceName(index, name, len(name))
        return name.value if ok else None

    def GetDeviceType(self, name):
        if not isinstance(name, bytes):
            name = name.encode()
        type = ctypes.c_int()
        ok = self.dll.GetDeviceType(name, ctypes.byref(type))
        return type.value if ok else None

    def GetDeviceDescription(self, name):
        if not isinstance(name, bytes):
            name = name.encode()
        desc = ctypes.create_string_buffer(mmdevice.MaxStrLength)
        ok = self.dll.GetDeviceDescription(name, desc, len(desc))
        return desc.value if ok else None
