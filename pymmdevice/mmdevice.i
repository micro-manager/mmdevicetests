%module(package="pymmdevice", directors="1") mmdevice

%{
#include "../mmCoreAndDevices/MMDevice/MMDeviceConstants.h"
#include "../mmCoreAndDevices/MMDevice/MMDevice.h"
%}

%feature("director") MM::Core;

%include "../mmCoreAndDevices/MMDevice/MMDeviceConstants.h"
%include "../mmCoreAndDevices/MMDevice/MMDevice.h"


/*
 * We wrap the device classes here with SWIG, but use ctypes to access the
 * ModuleInterface functions, so need a way to wrap device pointers obtained
 * there using the SWIG wrappers. The following trivial functions do this.
 *
 * Note that the SWIG proxy objects do not own the pointer (TODO: Check this by
 * printing something in the destructor). Pointer ownership can be controlled
 * using the acquire() and disown() methods, and queried with own().
 */

%{
    MM::Generic* wrap_ctypes_generic_pointer(unsigned long long ptr) {
        return (MM::Generic*)ptr;
    }

    MM::Camera* wrap_ctypes_camera_pointer(unsigned long long ptr) {
        return (MM::Camera*)ptr;
    }

    MM::Shutter* wrap_ctypes_shutter_pointer(unsigned long long ptr) {
        return (MM::Shutter*)ptr;
    }

    MM::Stage* wrap_ctypes_stage_pointer(unsigned long long ptr) {
        return (MM::Stage*)ptr;
    }

    MM::XYStage* wrap_ctypes_xystage_pointer(unsigned long long ptr) {
        return (MM::XYStage*)ptr;
    }

    MM::State* wrap_ctypes_state_pointer(unsigned long long ptr) {
        return (MM::State*)ptr;
    }

    MM::Serial* wrap_ctypes_serial_pointer(unsigned long long ptr) {
        return (MM::Serial*)ptr;
    }

    MM::AutoFocus* wrap_ctypes_autofocus_pointer(unsigned long long ptr) {
        return (MM::AutoFocus*)ptr;
    }

    MM::ImageProcessor* wrap_ctypes_imageprocessor_pointer(unsigned long long ptr) {
        return (MM::ImageProcessor*)ptr;
    }

    MM::SignalIO* wrap_ctypes_signalio_pointer(unsigned long long ptr) {
        return (MM::SignalIO*)ptr;
    }

    MM::Magnifier* wrap_ctypes_magnifier_pointer(unsigned long long ptr) {
        return (MM::Magnifier*)ptr;
    }

    MM::SLM* wrap_ctypes_slm_pointer(unsigned long long ptr) {
        return (MM::SLM*)ptr;
    }

    MM::Galvo* wrap_ctypes_galvo_pointer(unsigned long long ptr) {
        return (MM::Galvo*)ptr;
    }

    MM::Hub* wrap_ctypes_hub_pointer(unsigned long long ptr) {
        return (MM::Hub*)ptr;
    }
%}

MM::Generic* wrap_ctypes_generic_pointer(unsigned long long ptr);
MM::Camera* wrap_ctypes_camera_pointer(unsigned long long ptr);
MM::Shutter* wrap_ctypes_shutter_pointer(unsigned long long ptr);
MM::Stage* wrap_ctypes_stage_pointer(unsigned long long ptr);
MM::XYStage* wrap_ctypes_xystage_pointer(unsigned long long ptr);
MM::State* wrap_ctypes_state_pointer(unsigned long long ptr);
MM::Serial* wrap_ctypes_serial_pointer(unsigned long long ptr);
MM::AutoFocus* wrap_ctypes_autofocus_pointer(unsigned long long ptr);
MM::ImageProcessor* wrap_ctypes_imageprocessor_pointer(unsigned long long ptr);
MM::SignalIO* wrap_ctypes_signalio_pointer(unsigned long long ptr);
MM::Magnifier* wrap_ctypes_magnifier_pointer(unsigned long long ptr);
MM::SLM* wrap_ctypes_slm_pointer(unsigned long long ptr);
MM::Galvo* wrap_ctypes_galvo_pointer(unsigned long long ptr);
MM::Hub* wrap_ctypes_hub_pointer(unsigned long long ptr);