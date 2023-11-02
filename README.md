Rmath4-python
============

This is a standalone Rmath library based on R version 4 for Python. It is based on the Rmath-julia and original Rmath-python package from Nick Tessore (https://github.com/ntessore/Rmath-python).

This package was created in order to call statistical functions in numba generated code in non-python mode. 


Installation
------------

The package is available for pip installation:

    pip install Rmath4

Alternatively, you can clone or download this repository, and install from
there in the usual way.

In either case, a functional build system is required, but there are no
dependencies.


Updating the Library
--------------------

To update to the latest version of R, bump the `RVERSION` file, and run `make
update`. Some additional manual changes to the headers may be necessary: these
should go in `include/Rconfig.h`. Additional manual updates for the `nmath.h` patches for the warning messages may be required.


[Rmath]: https://cran.r-project.org/doc/manuals/r-release/R-admin.html#The-standalone-Rmath-library
[Rmath-julia]: https://github.com/JuliaStats/Rmath-julia
[Rmath-python]: https://github.com/ntessore/Rmath-python
