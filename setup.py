from distutils.core import setup, Extension
import numpy

module1 = Extension('_dpcore_py',
                    sources = ['dpcore_py.c'],
                   include_dirs = [numpy.get_include()])

setup (name = '_dpcore_py',
       version = '0.0',
       description = 'Dynamic programming core routine',
       ext_modules = [module1])
