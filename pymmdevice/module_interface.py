import ctypes
from . import mmdevice

# Wrapper for module interface version 10

class DeviceAdapterModule:
    def __init__(self, path):
        self.dll = ctypes.CDLL(path)

        self.dll.InitializeModuleData.restype = None
        self.dll.InitializeModuleData.argtypes = []
        self.dll.CreateDevice.restype = ctypes.c_void_p # MM::Device*
        self.dll.CreateDevice.argtypes = [ctypes.c_char_p]
        self.dll.DeleteDevice.restype = None
        self.dll.DeleteDevice.argtypes = [ctypes.c_void_p] # MM::Device*
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

    def InitializeModuleData(self):
        self.dll.InitializeModuleData()

    def CreateDevice(self, name):
        if not isinstance(name, bytes):
            name = name.encode()
        # TODO Wrap using SWIG-generated interface
        return self.dll.CreateDevice(name)

    def DeleteDevice(self, device):
        # TODO Unwrap if device is SWIG-generated type
        self.dll.DeleteDevice(device)

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