#!/usr/bin/env python

import os
import argparse

parser = argparse.ArgumentParser(
  description="Compiles latex and bibtex from source. The output is created in the parent directory of the source, in the 'pdf' directory, which is created if it does not exist.")
parser.add_argument("-s", "--source", dest="source",
                    help="Source latex document. Default is 'latex/main.tex'.", type=str, default="latex/main.tex")
args = parser.parse_args()

source_path = os.path.realpath(args.source)

if not os.path.isfile(source_path):
  raise FileNotFoundError("Source file %s not found" % source_path)

source_dir = os.path.dirname(source_path)
source_base = os.path.basename(source_path)
os.chdir(source_dir)
pdf_dir = os.path.join(os.pardir, "pdf")


def compile_latex():
  if os.system(
          "pdflatex -halt-on-error -output-directory %s %s" % (pdf_dir, source_base)):
    exit(-1)


def compile_bibtex():
  if os.system("bibtex %s" % (source_base.split(".")[0])):
    exit(-1)


if not os.path.exists(pdf_dir):
  os.makedirs(pdf_dir)

compile_latex()
os.chdir(pdf_dir)
compile_bibtex()
os.chdir(source_dir)
for i in range(2):
  compile_latex()

print("DONE.\nCompiled files can be found in %s" % os.path.realpath(pdf_dir))
exit(0)
