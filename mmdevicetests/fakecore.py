from . import mmdevice
import ctypes
import math
import time


class FakeCore(mmdevice.Core):
    def __init__(self):
        super().__init__()

    # Method parameters have type hints copied from the SWIG-generated
    # superclass. These are for humans only.

    def LogMessage(self, caller: "Device", msg: "char const *", debugOnly: "bool") -> "int":
        return mmdevice.DEVICE_OK

    def GetDevice(self, caller: "Device", label: "char const *") -> "MM::Device *":
        return None

    def GetDeviceProperty(self, deviceName: "char const *", propName: "char const *") -> "int":
        return mmdevice.DEVICE_ERR, ""

    def SetDeviceProperty(self, deviceName: "char const *", propName: "char const *", value: "char const *") -> "int":
        return mmdevice.DEVICE_ERR

    def GetLoadedDeviceOfType(self, caller: "Device", devType: "MM::DeviceType", deviceIterator: "unsigned int const") -> "void":
        return ""

    def SetSerialProperties(self, portName: "char const *", answerTimeout: "char const *", baudRate: "char const *", delayBetweenCharsMs: "char const *", handshaking: "char const *", parity: "char const *", stopBits: "char const *") -> "int":
        return mmdevice.DEVICE_ERR

    def SetSerialCommand(self, caller: "Device", portName: "char const *", command: "char const *", term: "char const *") -> "int":
        return mmdevice.DEVICE_ERR

    def GetSerialAnswer(self, caller: "Device", portName: "char const *", ansLength: "unsigned long", answer: "char *", term: "char const *") -> "int":
        return mmdevice.DEVICE_ERR

    def WriteToSerial(self, caller: "Device", port: "char const *", buf: "unsigned char const *", length: "unsigned long") -> "int":
        return mmdevice.DEVICE_ERR

    def ReadFromSerial(self, caller: "Device", port: "char const *", buf: "unsigned char *", length: "unsigned long", read: "unsigned long &") -> "int":
        # TODO output parameters need SWIG wrapper fix
        return mmdevice.DEVICE_ERR

    def PurgeSerial(self, caller: "Device", portName: "char const *") -> "int":
        return mmdevice.DEVICE_ERR

    def GetSerialPortType(self, portName: "char const *") -> "MM::PortType":
        return mmdevice.InvalidPort

    def OnPropertiesChanged(self, caller: "Device") -> "int":
        return mmdevice.DEVICE_OK

    def OnPropertyChanged(self, caller: "Device", propName: "char const *", propValue: "char const *") -> "int":
        return mmdevice.DEVICE_OK

    def OnStagePositionChanged(self, caller: "Device", pos: "double") -> "int":
        return mmdevice.DEVICE_OK

    def OnXYStagePositionChanged(self, caller: "Device", xPos: "double", yPos: "double") -> "int":
        return mmdevice.DEVICE_OK

    def OnExposureChanged(self, caller: "Device", newExposure: "double") -> "int":
        return mmdevice.DEVICE_OK

    def OnSLMExposureChanged(self, caller: "Device", newExposure: "double") -> "int":
        return mmdevice.DEVICE_OK

    def OnMagnifierChanged(self, caller: "Device") -> "int":
        return mmdevice.DEVICE_OK

    def GetClockTicksUs(self, caller: "Device") -> "unsigned long":
        # The return value of this function on 32-bit or LLP64 systems rolls
        # over in about 71 minutes, so is dangerous to use in delay
        # computations.
        microseconds = time.time() * 1e3
        ulong_max = ctypes.c_ulong(-1).value
        return int(math.floor(microseconds)) % ulong_max

    # MMCore uses the microseconds since 2000-01-01 00:00:00 local time.
    _mm_epoch_ms = time.mktime((2000, 1, 1, 0, 0, 0, 5, 1, 0))

    def GetCurrentMMTime(self) -> "MM::MMTime":
        microseconds = (time.time() - self._mm_epoch_ms) * 1e3
        return mmdevice.MMTime(microseconds)

    def AcqFinished(self, caller: "Device", statusCode: "int") -> "int":
        return mmdevice.DEVICE_OK

    def PrepareForAcq(self, caller: "Device") -> "int":
        return mmdevice.DEVICE_OK

    def InsertImage(self, *args) -> "int":
        return mmdevice.DEVICE_OK

    def ClearImageBuffer(self, caller: "Device") -> "void":
        pass

    def InitializeImageBuffer(self, channels: "unsigned int", slices: "unsigned int", w: "unsigned int", h: "unsigned int", pixDepth: "unsigned int") -> "bool":
        return mmdevice.DEVICE_OK

    def InsertMultiChannel(self, caller: "Device", buf: "unsigned char const *", numChannels: "unsigned int", width: "unsigned int", height: "unsigned int", byteDepth: "unsigned int", md: "Metadata *") -> "int":
        return mmdevice.DEVICE_OK

    def GetImage(self) -> "char const *":
        return None

    def GetImageDimensions(self, width: "int &", height: "int &", depth: "int &") -> "int":
        return mmdevice.DEVICE_ERR

    def GetFocusPosition(self, pos: "double &") -> "int":
        return mmdevice.DEVICE_ERR

    def SetFocusPosition(self, pos: "double") -> "int":
        return mmdevice.DEVICE_ERR

    def MoveFocus(self, velocity: "double") -> "int":
        return mmdevice.DEVICE_ERR

    def SetXYPosition(self, x: "double", y: "double") -> "int":
        return mmdevice.DEVICE_ERR

    def GetXYPosition(self, x: "double &", y: "double &") -> "int":
        return mmdevice.DEVICE_ERR

    def MoveXYStage(self, vX: "double", vY: "double") -> "int":
        return mmdevice.DEVICE_ERR

    def SetExposure(self, expMs: "double") -> "int":
        return mmdevice.DEVICE_ERR

    def GetExposure(self, expMs: "double &") -> "int":
        return mmdevice.DEVICE_ERR

    def SetConfig(self, group: "char const *", name: "char const *") -> "int":
        return mmdevice.DEVICE_ERR

    def GetCurrentConfig(self, group: "char const *", bufLen: "int", name: "char *") -> "int":
        return mmdevice.DEVICE_ERR

    def GetChannelConfig(self, channelConfigName: "char *", channelConfigIterator: "unsigned int const") -> "int":
        return mmdevice.DEVICE_ERR

    def GetImageProcessor(self, caller: "Device") -> "MM::ImageProcessor *":
        return None

    def GetAutoFocus(self, caller: "Device") -> "MM::AutoFocus *":
        return None

    def GetParentHub(self, caller: "Device") -> "MM::Hub *":
        return None

    def GetStateDevice(self, caller: "Device", deviceName: "char const *") -> "MM::State *":
        return None

    def GetSignalIODevice(self, caller: "Device", deviceName: "char const *") -> "MM::SignalIO *":
        return None

    def NextPostedError(self, arg0: "int &", arg1: "char *", arg2: "int", arg3: "int &") -> "void":
        pass

    def PostError(self, arg0: "int const", arg1: "char const *") -> "void":
        pass

    def ClearPostedErrors(self) -> "void":
        pass
