from setuptools import setup, find_packages

#https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
setup(
    name='sphinx_demo',
    version='0.1.0',
    author='William E. Chapman',
    author_email='wchapman@ucar.edu',
    description='A package to demo a sphinx website',
    license='GNU General Public License v2',
    packages=find_packages(include='sphinx_demo*'),
    install_requires=[
        'pyyaml',
        'pandas',
        'numpy',
        'matplotlib',
        'xarray',
        'datetime',
        'netCDF4'
    ],
    extras_require={
        'full_func': ['jupyter','dask'],
        'dev': ['build', 'pytest', 'pytest-pep8', 'tox', 'sphinx==1.7.1', 'Jinja2<3.1' , 'm2r2', 'sphinx_rtd_theme', 'twine','bluepy'],
      },
    package_data={'sphinx_demo': ['*/*.nc']},
)
