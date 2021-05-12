%module(directors="1") mmdevice

%{
#include "mmCoreAndDevices/MMDevice/MMDeviceConstants.h"
#include "mmCoreAndDevices/MMDevice/MMDevice.h"
%}

%feature("director") MM::Core;

%include "mmCoreAndDevices/MMDevice/MMDeviceConstants.h"
%include "mmCoreAndDevices/MMDevice/MMDevice.h"