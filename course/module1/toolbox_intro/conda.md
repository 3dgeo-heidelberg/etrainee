---
title: "Conda"
description: "This quick guide to package management with Conda is part of the introduction to the E-TRAINEE course which sets the prerequisites for starting with Module 1."
dateCreated: 2023-11-06
authors: Andreas Mayr
contributors: TBA
estimatedTime: 30 minutes
---

# Conda

To install the general-purpose programming language Python and to manage its versions along with all packages extending it (make it useful for our specific purposes) we use the package management system [Conda](https://conda.io/). Conda quickly installs, runs, and updates packages and their dependencies. Conda easily creates, saves, loads, and switches between environments on your local computer. It was created for Python programs but it can package and distribute software for any language.

<p align="center">
    <img src="toolbox_media/snakes_v01.png" title="Figure created partly with DALL-E 3 / CC BY 4.0" width="300">
</p>

## Conda distributions

*Anaconda* is a popular distribution of Conda, which has lots of software and extensions preinstalled (e.g., Python with numerous packages, ...). While this may sound nice you will probably not need all this software and, instead, you might want to install other packages or specific versions.

*Miniconda* is a free minimal installer that includes only conda, Python, the packages they both depend on, and a small number of other useful packages. More packages can be installed from thousands of packages available by default in Anaconda’s public repo, or from other channels, like conda-forge or bioconda.

*Miniforge* is comparable to Miniconda but it has [conda-forge](https://conda-forge.org/) as the default channel to install packages from and it has Mamba installed in the base environment (more on this later).

## Should I install Miniforge?

* If you have anaconda or miniconda or miniforge already installed and it works for you: Just keep your installation.
* If you encounter problems with an existing installation, uninstall and install Miniforge as described below.
* If you do not yet have a Conda distribution installed, we recommend Miniforge.

## Miniforge installation

Go to the [Miniforge download website](https://github.com/conda-forge/miniforge#miniforge3) and download the installer fitting your operating system (Windows, Linux, Mac OS and) and architecture (most probably `x86_64` is the right one).

* On **Windows** just download and execute the installer manually (double-click the `.exe` file), follow the instructions on the screen and accept the default settings (recommendations). Avoid installing in a directory with special characters and spaces in the name.
* If you are on **Linux or Mac Os**, follow the procedure described [here](https://github.com/conda-forge/miniforge#unix-like-platforms-mac-os--linux).


## Manage packages and environments

Open the Miniforge prompt (in Windows type "miniforge prompt" into the search bar, then add this app to the task bar for convenience). You will see a black window with a command line where you can use the standard commands for your system (e.g. [Windows](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)) plus the [commands for Conda](https://docs.conda.io/projects/conda/en/stable/commands/index.html) (and Mamba if you installed Miniforge).

To see all your Python installations, type ``where Python`` and hit enter. Now you are probably shown multiple paths where Python is installed and this can easily cause confusion about which Python is actually used to run code or to install extensions (packages) for. Conda is made exactly to avoid this confusion and to easily maintain control over your Python installations and packages.

*What are Python packages?* - 
A Python package is a collection of modules, which, in turn, are essentially Python or C scripts that contain published functionality. There are Python packages for data input, data analysis, data visualization, etc. Each package offers a unique toolset and may have its own unique syntax. The [Python Standard Library](https://docs.python.org/3/library/) contains a general-purpose set of packages shipped with every Python installation. Many additional ('third-party' or 'external') packages have been published and can be installed as needed.

Package management is useful because you may want to update a package for one of your projects, but keep it at the same version in other projects to ensure that they continue to run as expected. With Conda, we can manage packages in different *environments*, as an installation happens only in the currently active environment (indicated in brackets at the beginning of the prompt and indicated by an asterisk (*) when you list all environemnts whith ``conda env list``). We can switch between environments with ``conda activate <your_env_name>`` Initially, there is only the 'base' environment but we can create others. When you install packages (or another Python version) for a specific project, it is recommended that you do this in a fresh environment (not in the base environment).

When one of your environments becomes “broken” or obsolete, you can simply delete it with ``conda remove -n <your_env_name> --all``. This will delete the corresponding folder and all packages in it (Yes, an environment is just a folder on your system!).

### Mamba

Solving the dependencies for complex environments with many different packages can take a long time (and sometimes fail) with conda. [Mamba](https://mamba.readthedocs.io/en/latest/index.html) was developed to improve this. Mamba is a drop-in replacement and uses the same commands and configuration options as Conda, i.e., you can swap almost all commands between Conda and Mamba (see below).

Miniforge has Mamba pre-installed in the base environment<!--(since release 23.3.1-0, thus being identical to Mambaforge now (except for installation paths))-->.

If you have a Conda installed with another distribution (e.g. Anaconda), you can

    conda install mamba -n base -c conda-forge

and then use mamba to install other packages.

### Basic use

Let's try this! Create a new environment called 'geopython' which contains an installation of Python 3.10.

    mamba create --name geopython python=3.10

Activate this 'geopython' environment.

    mamba activate geopython

Check which packages and versions are installed in this environment.

    mamba list

Now install some packages to this active environment. Note that we only specify some packages but many others (such as *pandas*, *numpy* and *scipy*) are also installed automatically because they are required for the specified ones to work properly.

    mamba install ipykernel geopandas rasterio xarray rioxarray

Check which environments we have. The active one is marked by an asterisk (*).

    mamba env list

Just for testing, we could create another environment called 'geopython_v2' which is identical to the 'geopython' environment.

    mamba create -n geopython_v2 --clone geopython

Delete the 'geopython_v2' environment and all packages in it.

    mamba remove -n geopython_v2 --all

See also this [Conda cheat sheet](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html) for a list of useful commands. Read more about Conda, packages and environments in the [conda documentation](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-environments).

Unfortunately, not all packages are available from a conda channel (such as conda-forge). In this case (and only in this case) you should install the package either from the Python Package Index ([PyPi](https://pypi.org/)) via [``pip``](https://pip.pypa.io/en/stable/) within a Conda environment (see also the recommendations [here](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html#pip-in-env)). More on the differences between Conda and pip and why Conda is the recommended way is explained [here](https://www.anaconda.com/blog/understanding-conda-and-pip).

### Set up the E-TRAINEE course environment

To set up an environment with Python and the packages required for the course, there are two options:

**Option 1:** Use the YAML requirements file provided for the course. This file defines the environment with all required packages (versions fixed, builds not fixed for cross-platform compatibility). Just download the Module 1 [requirements file](https://3dgeo-heidelberg.github.io/etrainee/assets/python_envs/etrainee_m1.yml) from the E-TRAINEE GitHub, save it in your working directory and run this command:

```
conda env create -f etrainee_m1.yml --name etrainee_m1
```

You can also open the YAML file in a text editor and have a look at its content. [Here](https://3dgeo-heidelberg.github.io/etrainee/assets/python_envs/), you find also requirements files for the other E-TRAINEE modules and one for the entire course.

**Option 2:** Run the following commands (in the Conda/Miniforge prompt or in a VSCode terminal with Conda recognized):

```
mamba create -n etrainee_m1 python=3.10
mamba activate etrainee_m1
mamba install ipykernel earthengine-api eemont geemap pygis wxee scikit-learn stackstac xarrayutils hvplot datashader xmovie laspy vaex seaborn
```

*Note*: This will install >480 packages, with a total download volume of >780 MB.

If you need to install additional packages, you can usually do this with `mamba install <package_name>`. If a specific package is not available on the Conda channels (e.g., conda-forge), you might have to use `pip install <package_name>` or install from source.

### Conda and Python in VSCode

#### Conda environments in VSCode

You can also use Conda in a terminal (prompt) in Visual Studio Code (instead of the Miniforge prompt) to manage packages and environments. 
And, importantly, you will be able to select one of your environments as a 'kernel' which is used to run Python code. 

If Conda is not recognized in VSCode, open VSCode by entering ``code` in the Miniforge prompt. For other solutions see e.g. [this article](https://medium.com/analytics-vidhya/efficient-way-to-activate-conda-in-vscode-ef21c4c231f2).

#### Creating and running a Python script

In the upper left menu of VScode, go to *File - New File ...* to create a new Python file (*.py) and save it in your working directory ('my_script.py'). Alternatively, use the shortcut *CTRL + Shift + P" to show and run commands for VSCode at the top of your screen and then type/select "Python: New Python File". Write a very simple script that prints "Hello world!".

You have at least two options to control the environment/kernel used to run the script:

* In the VSCode terminal, activate the environment you want to use. Type the file name of the script into the terminal and hit enter (make sure you are in the same folder as this script or type also the path to the script).
* `CTRL + Shift + P` and type `Python: Select Interpreter`. Run the script via the play button in the upper right. This opens an interactive window, where you can also choose the `kernel' among your Python installations (for the next run).

Actually, the environment doesn't matter now for this simple script but as we are going to do more specific things we will need an environment with the right packages installed. More on Python and VSCode is explained [here](https://code.visualstudio.com/docs/languages/python).

### Next: Jupyter Notebooks

Continue with *Jupyter Notebooks* for interactive computing and workflow documentation [here](./jupyter.ipynb).
