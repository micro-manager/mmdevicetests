import mmdevicetests.mmdevice as mmdevice


def test_constants():
    assert mmdevice.DEVICE_OK == 0
    assert mmdevice.DEVICE_ERR == 1
