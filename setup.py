import setuptools
import setuptools.command.build_py

py_mod_name = 'mmdevice'
ext_mod_name = '_' + py_mod_name

mmdevice_extension = setuptools.Extension(
    ext_mod_name,
    sources=[
        'mmdevice.i',
        'mmCoreAndDevices/MMDevice/MMDevice.cpp',
    ],
    swig_opts=[
        '-c++',
        '-py3',
        '-builtin',
        '-module', py_mod_name,
    ],
)

# Make build_py depend on build_ext, so that mmdevice.py exists
class build_py(setuptools.command.build_py.build_py):
    def run(self):
        self.run_command('build_ext')
        return super().run()

setuptools.setup(
        cmdclass={'build_py': build_py},
        py_modules=[py_mod_name],
        ext_modules=[mmdevice_extension],
        python_requires='>=3.6',
)
