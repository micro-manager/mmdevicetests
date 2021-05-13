import setuptools
import setuptools.command.build_py

mmdevice_extension = setuptools.Extension(
    'mmdevicetests._mmdevice',
    sources=[
        'mmdevicetests/mmdevice.i',
        'mmCoreAndDevices/MMDevice/MMDevice.cpp',
    ],
    swig_opts=[
        '-c++',
        '-py3',
    ],
)

# Make build_py depend on build_ext, so that mmdevice.py exists


class build_py(setuptools.command.build_py.build_py):
    def run(self):
        self.run_command('build_ext')
        return super().run()


setuptools.setup(
    cmdclass={'build_py': build_py},
    packages=['mmdevicetests'],
    ext_modules=[mmdevice_extension],
    python_requires='>=3.6',
)
