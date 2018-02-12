texoptions = \
  -lualatex \
  -output-directory=build \
  -interaction=nonstopmode \
  -halt-on-error

texenv = \
  max_print_line=2500 \
  TEXINPUTS=images:build:build/plots:


all: build/fact_open_data.pdf

build/fact_open_data.pdf: FORCE | build
	$(texenv) latexmk $(texoptions) fact_open_data.tex

preview: FORCE | build
	$(texenv) latexmk $(texoptions) -pvc fact_open_data.tex

FORCE:

build:
	mkdir -p build

build/plots:
	mkdir -p build/plots

clean:
	rm -rf build

.PHONY: FORCE clean plots
