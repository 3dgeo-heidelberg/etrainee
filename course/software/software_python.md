# Python

Python is a powerful scripting/programming language widely used in scientific processing and analysis: [https://www.python.org/](https://www.python.org/)

## Download and installation

There are many ways to install Python. We recommend using the fast cross-platform package manager [Mamba](https://github.com/mamba-org/mamba) from the [Miniforge distribution](https://github.com/conda-forge/miniforge), which provides a safe, flexible and fast way for installing Python with different packages and all their dependencies. Instructions for installation on various platforms are available in the [Mamba installation guide](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html).
Using `mamba`, a Python environment containing all required packages (modules) can be created, see suggested procedure [below](#creating-the-etrainee-python-environment-with-mamba). 
`mamba` is a reimplementation of the `conda` package manager in C++ and is generally faster and better at respolving dependencies. It is a drop-in replacement and uses the same commands and configuration options as `conda`.

### Required packages (modules)
Different Python packages (modules) are required for in different modules/themes of this course. Find the list of required packages in the `.yml` files. You can download the yaml files for the respective modules here:  
Module 1: <a href=../assets/python_envs/etrainee_m1.yml download>etrainee_m1.yml</a>    
Module 3: <a href=../assets/python_envs/etrainee_m3.yml download>etrainee_m3.yml</a>    
Module 4: <a href=../assets/python_envs/etrainee_m4.yml download>etrainee_m4.yml</a>    

### Creating the etrainee Python environment with Mamba
A recommended practice to set up Python for this course, is to create a [Mamba environment](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) with all required modules (packages). If you are using Conda/Mamba, you may use the following procedure to create an `etrainee_mX` Python environment for each module:

```
mamba env create -f etrainee_m1.yml
mamba env create -f etrainee_m2.yml
mamba env create -f etrainee_m3.yml
```


## Getting started

Basic knowledge of programming and Python are required in this course. If you are new to Python, check the resources given in the [pre-module](../module0/module0.md#programming-in-python). If you are already familiar with some Python basics but not with Conda/Mamba and environments, with Jupyter Notebooks, and with geodata processing in Python then we recommend to go through the [Toolbox intro](../module1/toolbox_intro/ETRAINEE_intro_overview.md) at the beginning of Module 1.
