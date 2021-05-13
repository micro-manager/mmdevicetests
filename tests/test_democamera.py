import os
import mmdevicetests.mmdevice
import mmdevicetests.module_interface
import pytest


democam_envvar = 'MMDEVICETESTS_TEST_DEMOCAMERA_PATH'


@pytest.fixture
def democam_path():
    path = os.environ.get(democam_envvar)
    # We require absolute path because tests run in their own directory
    if not path or not os.path.isabs(path):
        pytest.skip("{} not set to an absolute path".format(democam_envvar))
    return path


def load_democam(democam_path):
    return mmdevicetests.module_interface.DeviceAdapterModule(democam_path)


def test_load_democam(democam_path):
    assert load_democam(democam_path)


@pytest.fixture
def democam_module(democam_path):
    try:
        return load_democam(democam_path)
    except:
        pytest.skip("The DemoCamera module failed to load")


@pytest.mark.dependency()
def test_democam_version(democam_module):
    democam_module.InitializeModuleData()
    assert democam_module.GetModuleVersion() == mmdevicetests.module_interface.MODULE_INTERFACE_VERSION
    assert democam_module.GetDeviceInterfaceVersion() == mmdevicetests.mmdevice.DEVICE_INTERFACE_VERSION


@pytest.mark.dependency(depends=['test_democam_version'])
def test_democam_enumerate(democam_module):
    democam_module.InitializeModuleData()
    assert democam_module.GetNumberOfDevices() > 0
