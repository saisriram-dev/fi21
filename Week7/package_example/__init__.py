# This file tells python that the directory should be treated as a package.
# It can also be used to import specific modules or functions
# This file runs whenever we import the package, so we can use it to set up any
# necessary initialization code or to define what is available when the package is imported.

# Importing modules from the package
# This allows us to import the modules directly from the package without having to specify the submodules.

# This is known as relative imports
# If we didn't use relative imports, we would have to import the modules using absolute imports:
# from package_example.config import APP_NAME, VERSION, DEBUG
# from package_example.utils import add, subtract, multiply, divide, power

from .config import APP_NAME, VERSION, DEBUG
from .utils import add, subtract, multiply, divide, power
