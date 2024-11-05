from pathlib import Path
from textwrap import dedent

from cffi import FFI

parent_dir = Path(__file__).parent.resolve()
rel_parent_dir = parent_dir.relative_to(Path.cwd())

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
    sources=[str(rel_parent_dir.joinpath('approx_pi.cpp'))],
    source_extension=".cpp",
    include_dirs=[str(parent_dir)])
    # library_dirs=[str(parent_dir)],
    # extra_link_args=[f"-Wl,-rpath,{str(parent_dir)}"],
    # libraries=["approx_pi"])


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
