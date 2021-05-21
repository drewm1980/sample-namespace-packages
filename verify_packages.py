from normal_package_deep_in_subdirectories import a

from example_native_pkg import a
from example_native_pkg import b

from example_resources_pkg import a
from example_resources_pkg import b

from example_pkg import a
from example_pkg import b

# A deeply nested directory structure ending in a module that uses a local import.
from e.f.g import bar
from e.f.g import Bar
from e.f.g.h import baz
from e.f.g.h.baz import baz

