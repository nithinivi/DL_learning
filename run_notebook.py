#!/usr/bin/env python

import nbformat, fire
from nbconvert.preprocessors import ExecutePreprocessor


def run_notebook(path):
    nb = nb.format.read(open(path), as_version=nbformat.NO_CONVERT)
    ExecutePreprocessor(timeout=600).preprocess(nb, {})
    print("done")


if __name__ == '__main__':
    fire.Fire(run_notebook)
