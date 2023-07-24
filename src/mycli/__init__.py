import os
import pathlib
from .mycli import patched_main

__here__ = pathlib.Path(__file__)
__version__ = "0.0.1"

_data_path = []
_data_path.append(__here__ / "data")

if __name__ == '__main__':
    patched_main()
