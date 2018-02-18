texoptions = \
  -lualatex \
  -output-directory=build \
  -interaction=nonstopmode \
  -halt-on-error

texenv = \
  max_print_line=2500 \
  TEXINPUTS=images:build:build/plots:


all: build/fact_open_data.pdf

build/plots/%.pdf: scripts/plot_%.py matplotlibrc_half header-matplotlib.tex | build/plots
	MATPLOTLIBRC=matplotlibrc_half TEXINPUTS=$(shell pwd): python $<


plots: build/plots/drs_calib.pdf build/plots/spikes.pdf build/plots/phs.pdf

build/plots/phs.pdf: build/phs.jsonl.gz

build/plots/zenith.pdf: build/runs.csv

plots: build/plots/theta2.pdf build/plots/zenith.pdf

build/plots/theta2.pdf: 
	MATPLOTLIBRC=matplotlibrc_full \
	TEXINPUTS=$(shell pwd): \
	fact_plot_theta_squared crab_gammas_dl3.hdf5 --theta2-cut=0.025 -o build/plots/theta2.pdf


build/phs.jsonl.gz:
	curl -o build/phs.jsonl.gz https://ihp-pc41.ethz.ch/public/phs/public/20131101_185.phs.jsonl.gz 


build/runs.csv:
	curl -o build/runs.csv https://www.fact-project.org/data/open_crab_sample_runs.csv


build/fact_open_data.pdf: FORCE plots build/plots/drs_calib.pdf | build
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
