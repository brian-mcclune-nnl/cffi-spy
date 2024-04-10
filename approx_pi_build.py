from pathlib import Path
from textwrap import dedent

from cffi import FFI

parent_dir = str(Path(__file__).parent.resolve())

ffibuilder = FFI()
ffibuilder.cdef(dedent("""\
    double leibniz(int n);
    double wallis(int n);
"""))
ffibuilder.set_source(
    "_approx_pi",
    dedent("""\
        #include "approx_pi.h"
    """),
    sources=['approx_pi.cpp'],
    source_extension=".cpp",
    include_dirs=[parent_dir])
    # library_dirs=[parent_dir],
    # extra_link_args=[f"-Wl,-rpath,{parent_dir}"],
    # libraries=["approx_pi"])


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
