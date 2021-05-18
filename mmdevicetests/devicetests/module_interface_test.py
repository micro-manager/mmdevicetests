import logging

from .. import mmdevice
from ..module_interface import DeviceAdapterModule


# TODO This should go in a central location
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)


# Design note: for now the tests are simple, plain code. Better structuring
# (perhaps a proper framework for progressive testing, which may or may not be
# best constructed based on a unit testing framework) will be needed as we gain
# more tests, and the appropriate structure needs to be informed by what the
# tests look like.


def test_module_metadata(path):
    logging.info("{}: Loading".format(path))
    mod = DeviceAdapterModule(path)
    assert mod  # Unlikely (would have already raised exception)

    logging.info("{}: Checking device interface version".format(path))
    dev_if_ver = mod.GetDeviceInterfaceVersion()
    assert dev_if_ver == mmdevice.DEVICE_INTERFACE_VERSION, \
        "Device adapter {} has device interface version {}; " + \
        "this test is for version {}".format(path, dev_if_ver,
                                             mmdevice.DEVICE_INTERFACE_VERSION)

    logging.info("{}: Initializing module".format(path))
    mod.InitializeModuleData()

    logging.info("{}: Getting device count".format(path))
    num_devs = mod.GetNumberOfDevices()
    logging.info("{}: Number of devices = {}".format(path, num_devs))

    logging.info("{}: Getting device names, types, and descriptions".
                 format(path))
    for i in range(num_devs):
        name = mod.GetDeviceName(i)
        assert name, "Device name must not be empty"
        # TODO We should also test for unallowed characters in device name
        logging.info("{}: Device {}: name = \"{}\"".
                     format(path, i, name.decode()))
        typ = mod.GetDeviceType(name)
        logging.info("{}: Device {}: type = {}".
                     format(path, name.decode(), typ))
        check_real_device_type(typ)
        desc = mod.GetDeviceDescription(name)
        assert desc is not None, "Device description must exist even if empty"
        logging.info("{}: Device {}: description = \"{}\"".
                     format(path, name.decode(), desc.decode()))

    logging.info("{}: Testing out-of-range cases of getting device information".
                 format(path))
    assert mod.GetDeviceName(num_devs) is None, \
        "GetDeviceName must return false when argument out of range"
    assert mod.GetDeviceType("") is None, \
        "GetDeviceType must return false when argument not a device name"
    assert mod.GetDeviceDescription("") is None, \
        "GetDeviceDescription must return false when argument not a device name"

    for i in range(num_devs):
        name = mod.GetDeviceName(i)
        logging.info("{}: Device {}: Creating".format(path, name.decode()))
        dev = mod.CreateDevice(name)
        assert dev is not None, \
            "CreateDevice must not return NULL for valid device name"
        logging.info("{}: Device {}: Deleting".format(path, name.decode()))
        mod.DeleteDevice(dev)

    # TODO Creating the same device multiple times needs to be tested. Also,
    # failure to create a registered device is not always a bug - in non-Hub
    # adapters, it just means the device is not available.

    # Note that CreateDevice may accept device names other than the ones
    # enumerated above. But we can still test with empty string, which is not
    # a valid device name.
    assert mod.CreateDevice("") is None, \
        "CreateDevice must return NULL when argument not a device name"


def check_real_device_type(typ):
    assert typ >= 0, "Device type must not be negative"
    assert typ != mmdevice.UnknownType, "Device type must not be UnknownType"
    assert typ != mmdevice.AnyType, "Device type must not be AnyType"

    # Currently (device i/f ver 70), GalvoDevice is the greatest enum item
    assert typ <= mmdevice.GalvoDevice, "Device type must be a known type"
