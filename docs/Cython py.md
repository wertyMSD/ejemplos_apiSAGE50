---
Alias: null
Creado fecha: 2023-04-14 08:13
Modificado date: viernes 14º abril 2023 08:14:14
Tags: null
---
   
# URL   
[Source Files and Compilation — Cython 0.29.34 documentation](https://cython.readthedocs.io/en/stable/src/userguide/source_files_and_compilation.html#compilation)   
   
   
# ejemplo   
For the time being, it is just a warning that you can ignore.   
   
If you need to specify compiler options, libraries to link with or other linker options you will need to create `Extension` instances manually (note that glob syntax can still be used to specify multiple extensions in one line):   
   
from distutils.core import setup   
from distutils.extension import Extension   
from Cython.Build import cythonize   
   
extensions = [   
    Extension("primes", ["primes.pyx"],   
        include_dirs=[...],   
        libraries=[...],   
        library_dirs=[...]),   
# Everything but primes.pyx is included here.   
    Extension("*", ["*.pyx"],   
        include_dirs=[...],   
        libraries=[...],   
        library_dirs=[...]),   
]   
setup(   
    name="My hello app",   
    ext_modules=cythonize(extensions),   
)   
   
Note that when using setuptools, you should import it before Cython as setuptools may replace the `Extension` class in distutils. Otherwise, both might disagree about the class to use here.