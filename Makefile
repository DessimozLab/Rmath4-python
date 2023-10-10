RVERSION := $(shell cat RVERSION)


.PHONY: all update

all:
	@echo 'use Python to build'
	@echo 'use "make update" to update Rmath version'

update: R-$(RVERSION).tar.gz
	tar -xzvf $< --strip-components 3 -C src --include '*/src/nmath/*.[ch]' \
		--exclude '*/src/nmath/standalone/test.c'
	find include/R_ext -name '*.h' | xargs -I {} tar -xzvf $< --strip-components 2 '*/src/{}'
	tar -xzvf $< --strip-components 2 '*/src/include/Rmath.h0.in'
	mv -f include/Rmath.h0.in include/Rmath.h
	python fix_nmath.py src/nmath.h > src/nmath.h.tmp
	mv src/nmath.h.tmp src/nmath.h

R-$(RVERSION).tar.gz:
	curl -OL https://cran.r-project.org/src/base/R-4/$@
