# sphinx_demo


Installation
------------
It can be installed using, 
e.g., pip.
    
    pip3 install .

The following optional dependency sets can additionaly be installed by adding ["set_name"] behind the above commands:
  * *full_func*: Install these packages to be sure that all options are really available. This might 
    require a higher Python version than for the core functionality alone. RMM may still be computed without these
    additional packages, but the number of alternative approaches is limited.
  * *dev*: packages that are needed for the further development, documentation and testing of sphinx_demo.

Examples: 

    pip3 install -e .[full_func]

or

    pip3 install -e .[dev]