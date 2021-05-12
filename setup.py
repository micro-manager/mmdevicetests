import setuptools
import setuptools.command.build_py

mmdevice_extension = setuptools.Extension(
    'pymmdevice._mmdevice',
    sources=[
        'pymmdevice/mmdevice.i',
        'mmCoreAndDevices/MMDevice/MMDevice.cpp',
    ],
    swig_opts=[
        '-c++',
        '-py3',
        '-builtin',
    ],
)

# Make build_py depend on build_ext, so that mmdevice.py exists
class build_py(setuptools.command.build_py.build_py):
    def run(self):
        self.run_command('build_ext')
        return super().run()

setuptools.setup(
        cmdclass={'build_py': build_py},
        packages=['pymmdevice'],
        ext_modules=[mmdevice_extension],
        python_requires='>=3.6',
)
