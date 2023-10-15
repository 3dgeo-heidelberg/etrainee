# Python

Python is a powerful scripting/programming language widely used in scientific processing and analysis: [https://www.python.org/](https://www.python.org/)

## Download and installation

There are many ways to install Python. We recommend using the [Anaconda distribution](https://www.anaconda.com/products/individual), which provides a safe and flexible way for installing Python with different packages and all their dependencies. Instructions for installation on various platforms are available in the [Anaconda documentation](https://docs.anaconda.com/anaconda/).
Using Conda, a Python environment containing all required packages (modules) can be created, see suggested procedure [below](#creating-the-etrainee-python-environment-with-conda).

### Required packages (modules)
Different Python packages (modules) are required for in different modules/themes of this course. Find the list of required packages in the `.yml` files. You can download the yaml files for the respective modules here:  
Module 1: <a href=../assets/python_envs/etrainee_m1.yml download>etrainee_m1.yml</a>    
Module 3: <a href=../assets/python_envs/etrainee_m3.yml download>etrainee_m3.yml</a>    
Module 4: <a href=../assets/python_envs/etrainee_m4.yml download>etrainee_m4.yml</a>    

### Creating the etrainee Python environment with Conda
A recommended practice to set up Python for this course, is to create a [Conda environment](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) with all required modules (packages). If you are using Conda, you may use the following procedure to create an `etrainee_mX` Python environment for each module:

```
conda env create -f etrainee_m1.yml
conda env create -f etrainee_m2.yml
conda env create -f etrainee_m3.yml
```


## Getting started 
Basic knowledge of programming and Python are required in this course. If you are new to Python, check the resources given in the [pre-module](../module0/module0.md#programming-in-python).
