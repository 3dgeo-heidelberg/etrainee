---
title: "VSCode"
description: "This quick guide to Visual Studio Code is part of the introduction to the E-TRAINEE course which sets the prerequisites for starting with Module 1."
dateCreated: 2023-11-06
authors: Andreas Mayr
contributors: TBA
estimatedTime: 15 minutes
---

# Visual Studio Code

To write, modify and execute Python code, we use [*Visual Studio Code*](https://code.visualstudio.com/) (VSCode).

## What is it?

VSCode is a popular source-code editor by Microsoft. It is available for Windows, Linux and macOS and comes with the following features (and more):

* Support for many popular programming and markup languages: C++, Fortran, JavaScript, Python, Julia, Markdown, HTML, ... (built-in or via extensions)
* Syntax highlighting, bracket matching, code folding
* Intelligent code completion (auto-completion popups while typing)
* Support for debugging
* Version control (needs link to a version control system such as Git)
* Possibilities to change the theme, keyboard shortcuts, preferences, and install extensions that add functionality
* Telemetry: Collects usage data and sends it to Microsoft (can be disabled)

*Is it open-source?*

The [source code](https://github.com/Microsoft/vscode) for VSCode is fully open-source (and released under a MIT license), but the binaries that you [download from Microsoft](https://code.visualstudio.com/Download) are not.
With [VSCodium](https://vscodium.com/) you could also download a truly open-source binary distribution of VSCode, which is freely licensed and has telemetry disabled. This is basically the same as but more convenient than [building from source](https://github.com/Microsoft/vscode/wiki/How-to-Contribute#build-and-run) by yourself.


## Installation

Download and execute the installer for VSCode from [here](https://code.visualstudio.com/).

Open VSCode and install the Python and Jupyter extensions for VSCode, see [here](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

## Command line essentials

In VSCode, there is a command line ("terminal", "prompt", "shell"), usually at the bottom. This can be a Windows *PowerShell* or the "classic" *cmd* command prompt or "Bash" (Unix shell). For a comprehensive overview of commands see the [Windows Commands Reference](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd) or the [Guide to Unix commands](https://en.wikibooks.org/wiki/Guide_to_Unix/Commands). Some commands related to navigation in your directory (folder) structure will be useful (here for Windows; Unix commands in *italic* if they differ):

| Command | Operation |
| ------- | --------- |
| dir (*Unix: ls*) | List files and subdirectories in the current directory. |
| tree | Displays the directory structure of a path or of the disk. |
| cd FOLDER_NAME | "Change directory": Move to a folder within your current folder. |
| cd PATH_TO_YOUR_FOLDER_AND_NAME | Move to a folder at any path. |
| cd .. | Move to parent directory (i.e. one level up). |

Use these commands to move to your working directory, where you save your scripts (*Hint*: Try the 'Tab' key to auto-complete folder or file names).

Some other useful commands are related to file handling:

| Command | Operation |
| ------- | --------- |
| mkdir DIRECTORY | Creates a directory or subdirectory |
| rd DIRECTORY /s | Deletes a directory including all its files. |
| copy FILE FOLDER | Copies one or more files from one location to another. |
| rename SRC DES | Renames files or directories. |
| del FILE (*Unix: rm FILE*) | Delete one or more files. |

### Next: Conda

Continue with Python installation and package management using *Conda* [here](./conda.md).