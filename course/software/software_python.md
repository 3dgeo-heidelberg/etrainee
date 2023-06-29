# Python

Python is a powerful scripting/programming language widely used in scientific processing and analysis: [https://www.python.org/](https://www.python.org/)

## Download and installation

There are many ways to install Python. We recommend using the [Anaconda distribution](https://www.anaconda.com/products/individual), which provides a safe and flexible way for installing Python with different packages and all their dependencies. Instructions for installation on various platforms are available in the [Anaconda documentation](https://docs.anaconda.com/anaconda/).
Using Conda, a Python environment containing all required packages (modules) can be created, see suggested procedure [below](#creating-the-etrainee-python-environment-with-conda).

### Required packages (modules)
Different Python packages (modules) are required for in different modules/themes of this course. Find the list of required packages in the `etrainee.yml`. You can download the yaml file here: <a href=../assets/python_envs/etrainee.yml download>etrainee.yml</a>.

### Creating the etrainee Python environment with Conda
A recommended practice to set up Python for this course, is to create a [Conda environment](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) with all required modules (packages). If you are using Conda, you may use the following procedure to create the Python environment `etrainee`:

```
conda create -f etrainee.yml
```


## Getting started 
Basic knowledge of programming and Python are required in this course. If you are new to Python, check the resources given in the [pre-module](../module0/module0.md#programming-in-python).