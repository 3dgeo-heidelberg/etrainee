---
title: "E-TRAINEE Toolbox overview"
description: "This is an overview for the E-TRAINEE Module 1 toolbox introduction (software guide)."
dateCreated: 2023-11-06
authors: Andreas Mayr
contributors: TBA
estimatedTime: 5.0 hrs (for the entire toolbox intro)
---

# Toolbox overview

Before starting the course let's "unpack our toolbox" to ensure that we have the necessary digital working environment ready. This means we introduce the different **software components used in E-TRAINEE Module 1** (and partly also in other Modules). Thereby, we cover installation and some basic methods of

* [Visual Studio Code](./vscode.md) (code editor)
* [Conda](./conda.md) (package management system)
* [Jupyter Notebooks](./jupyter.ipynb) (interactive computing), with some Python fundamentals (programming language)
* GeoPython - A quickstart to geographic data handling in Python: Vector data with [GeoPandas](./geopandas.ipynb), raster data with [rasterio](./rasterio.ipynb), and multidimensional raster data with [xarray](./xarray.ipynb).

## Background and objective
<!--*SHORTEN OR SKIP THIS!*-->

The **objective** of this introduction to the E-TRAINEE course is to provide you with the software knowledge and skills needed to start with the practical parts of E-TRAINEE Module 1. For working on these practical parts, there are often a couple of similar software tools and varieties that may be suitable for a specific task, e.g. (our choice in bold):

* Program code can be run by executing either "normal" scripts (e.g. ```*.py``` files) or code cells within interactive **Jupyter Notebooks** (```*.ipynb```) with text explanations as well as graphics and other output in between.
* Jupyter Notebook documents can be edited and run in various web-based or desktop applications, such as [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/), [JupyterHub](https://jupyterhub.readthedocs.io/en/latest), [Jupyter Desktop](https://github.com/jupyterlab/jupyterlab-desktop), or **Visual Studio Code**, etc..
* Data can be processed with a variety of graphical user interface software or command line tools or by scripting in a programming language such as R, **Python**, JavaScript, or Julia.
* GeoPython: For handling geographic data in Python, we focus on the packages **GeoPandas**, **rasterio** and **xarray**. There are other packages available but some of them introduce unnecessary complexity, are no longer well-maintained, or are tailored to rather specific tasks.

Out of this variety, we *selected a set of tools* that makes up a tested and proven *digital working environment*. We hope that, by using a such a recommended, uniform environment for all course participants, you will (i) encounter less software-related problems, (ii) get more helpful, more specific instructions, (iii) learn an approach that enables you to set up and customize your working environment also for follow-up tasks (such as your MSc thesis, where you may need to install additional or different packages). A concise, step-by-step guide will show you how to make the components of this environment interact, so you don't need to search the endless resources of the web, and you have a condensed resource to look things up in case you forget something.

In addition to setting up such a working environment, you will learn some of the most useful methods of geodata handling and visualization in Python. This will be helpful when working on the practical parts of E-TRAINEE Module 1, where many of the more advanced workflows build upon these tools and methods.

### Next: VSCode

Get started with the *Visual Studio Code* source-code editor [here](./vscode.md)