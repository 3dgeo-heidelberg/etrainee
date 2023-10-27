# Welcome to the E-TRAINEE course repository!

[![DOI](https://zenodo.org/badge/643862021.svg)](https://zenodo.org/badge/latestdoi/643862021)

This repository hosts the **E-TRAINEE course on Time Series Analysis in Remote Sensing for Understanding Human-Environment Interactions**, which is an open e-learning course containing four main modules. The first one provides a general overview of methods for remote sensing (RS) time series analysis, and the other three focus on specific processing steps connected to different types of data:

* Module 1: Methods of Time Series Analysis in RS
* Module 2: Satellite Multispectral Images Time Series Analysis
* Module 3: 3D/4D Geographic Point Cloud Time Series Analysis
* Module 4: Airborne Imaging Spectroscopy Time Series Analysis

Each module consists of several themes with a theoretical part, a self-evaluation quiz, as well as practical tutorials and exercises. Moreover, modules 2-4 include two or three case studies with a deeper look into selected research problems. In addition, there is Module 0 summarising the course prerequisites in terms of knowledge in RS, statistics, and programming necessary to follow the course; links to available learning materials are provided there.

**Disclaimer:** This is a pre-release of the course. The course is still under development and revision within the ongoing research project [E-TRAINEE](https://web.natur.cuni.cz/gis/etrainee/). This means that not all contents are completely finished and you may encounter possible improvements or required corrections.

## Intended audience

The course is primarily developed for MSc students of geoinformatics and geography who specialize in remote sensing for monitoring Earth surface dynamics and changes. It may also be of interest and use to MSc and PhD students in fields related to environmental studies, ecology, geology, and other potential users dealing with remote sensing applications, such as practitioners of national environmental and conservation agencies.

## Datasets

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10003575.svg)](https://doi.org/10.5281/zenodo.10003575) 

[Datasets](https://doi.org/10.5281/zenodo.10003574) used in the exercises, case studies, and practical tutorials are hosted on Zenodo and can be downloaded separately for each Module.

## Course website

The course site is hosted on GitHub Pages and can be accessed at [https://3dgeo-heidelberg.github.io/etrainee/](https://3dgeo-heidelberg.github.io/etrainee/). It is automatically built from the source files in this repository (contained in `/course`).

### Downloading the course website documents

The automatically compiled website can be downloaded from the *gh-pages* branch of this repository.

### Building the course documents with mkdocs

The course site is built using the [mkdocs](https://www.mkdocs.org/) site generator, which is configured with a single YAML configuration file (`mkdocs/mkdocs.yml`). This procedure can be run locally. You may need to install mkdocs and any required packages using conda and pip or other Python package managers (see `/mkdocs/requirements_mkdocs.txt`).

To build the course site, change into the `/mkdocs` directory and run mkdocs:

`python -m mkdocs build`

The full course website is then generated in a directory called `site`.

## Usage and development of the course

* The latest version of the course is always available in the **main branch** of this repository. Updates to the course are made in **feature branches** or forks (see below) and merged into the main branch when ready. Therefore, the main branch may be ahead of the latest release version.
* When using the course, i.e., when teaching or training with it, we recommend to **fork the repository** into your GitHub account/organization and use the latest version of the main branch. This ensures that the course content is stable while updates may be merged in this repository. If you want to integrate updates from this repository into your fork, you can do so by **creating a pull request** from this repository to your forked repository, or use the syncing offered by GitHub. 
* Updates or corrections of the course material in this repository can be made by **creating a pull request** from your forked repository to this repository. The pull request will be reviewed and merged into the main branch if accepted.
* **Reviewing and releases** of the course are performed by the E-TRAINEE team. The latest release version of the course is tagged in the repository.

## Acknowledgements

This course was developed in the frame of the strategic partnership project [E-TRAINEE](https://web.natur.cuni.cz/gis/etrainee/index.html) funded by the [Erasmus+ Programme](https://www.erasmusplus.de/) of the European Union (ID 2020-1-CZ01-KA203-078308).
Acquisition of data for this course was supported by the mini grant "Towards sustainable development of natural environments based on continuous remote sensing monitoring" funded by the [4EU+ European University Alliance](https://4eualliance.eu/).

## Citation
Please cite E-TRAINEE when using it in your teaching or training, and reference the appropriate release version. All releases of E-TRAINEE are listed on Zenodo where you will find the citation information including DOI.

E-TRAINEE Development Team. E-TRAINEE - E-learning course on Time Series Analysis in Remote Sensing for Understanding Human-Environment Interactions [Computer software]. https://github.com/3dgeo-heidelberg/etrainee

The course has also been showcased in these publications:



## License
Except when explicitly stated otherwise, the course is licensed under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license, associated code is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.

## Team members (version A)
The development team has been led by Dr. Markéta Potůčková and it consists of experts from 4 universities:

### [Charles University, Faculty of Science](https://www.natur.cuni.cz/eng?set_language=en)
| [Dept. of Applied Geoinformatics and Cartography](https://www.natur.cuni.cz/geography/department-of-applied-geoinformatics-and-cartography?set_language=en)  |   |   |
|:---|:---:|:---:|
| Dr. Markéta Potůčková  | [web](https://www.natur.cuni.cz/geografie/geoinformatika-kartografie/mpot)  | [ORCID](https://orcid.org/0000-0002-8760-790X)  |
| Dr. Lucie Kupková      | [web](https://www.natur.cuni.cz/geografie/geoinformatika-kartografie/lkupkova)  | [ORCID](https://orcid.org/0000-0002-0270-0516)  |
| Dr. Lucie Červená      | [web](https://www.natur.cuni.cz/geografie/geoinformatika-kartografie/cervl7an)  | [ORCID](https://orcid.org/0000-0001-5246-1106)  |
| Alex Šrollerů          |   |   |
| Jakub Dvořák           |   | [ORCID](https://orcid.org/0000-0001-7845-7738)  |
| Adéla Šedová           |   |   |
|   |   |   |
| [**Dept. of Experimental Plant Biology**](https://www.natur.cuni.cz/biology/plant-biology)  |   |   |
| Prof. Jana Albrechtová | [web](http://kfrserver.natur.cuni.cz/lide/albrecht)  | [ORCID](https://orcid.org/0000-0001-6912-1992) |
| Dr. Zuzana Lhotáková   |   | [ORCID](https://orcid.org/0000-0003-3060-641X)  |
| Dr. Lena Hunt          |   | [ORCID](https://orcid.org/0000-0002-7605-1379)  |
| Dr. Eva Neuwirthová    |   | [ORCID](https://orcid.org/0000-0001-5613-847X)  |

### [Heidelberg University, Institute of Geography](https://www.geog.uni-heidelberg.de/index_en.html)
| [3D Geospatial Data Processing Group](https://www.geog.uni-heidelberg.de/3dgeo/index_en.html)  |   |   |
|---|:---:|:---:|
| Prof. Bernhard Höfle   | [web](https://www.geog.uni-heidelberg.de/gis/hoefle.html)  | [ORCID](https://orcid.org/0000-0001-5849-1461)  |
| Dr. Katharina Anders   | [web](https://www.geog.uni-heidelberg.de/gis/anders.html)  | [ORCID](https://orcid.org/0000-0001-5698-7041)  |
| Sina Antonia Zumstein  |   |   |

### [University of Innsbruck, Institute for Geography](https://www.uibk.ac.at/geographie/)
| [Remote Sensing & Topographic LiDAR Research Group](https://www.uibk.ac.at/geographie/lidar)  |   |   |
|---|:---:|:---:|
| Dr. Martin Rutzinger   | [web](https://www.uibk.ac.at/geographie/personal/rutzinger)  | [ORCID](https://orcid.org/0000-0001-6628-4681)  |
| Dr. Andreas Mayr       | [web](https://www.uibk.ac.at/geographie/personal/mayr)  | [ORCID](https://orcid.org/0000-0001-8305-4765)  |

### [University of Warsaw, Faculty of Geography and Regional Studies](http://wgsr.uw.edu.pl/wgsr/index.php/en/home-page-2)
| [Dept. of Geoinformatics, Cartography and Remote Sensing](http://geoinformatics.uw.edu.pl/)  |   |   |
|---|:---:|:---:|
| Dr. Adriana Marcinkowska-Ochtyra | [web](http://geoinformatics.uw.edu.pl/adriana-marcinkowska-ochtyra)  | [ORCID](https://orcid.org/0000-0002-9080-3899)  |
| Dr. Adrian Ochtyra               | [web](http://geoinformatics.uw.edu.pl/adrian-ochtyra)  | [ORCID](https://orcid.org/0000-0003-4799-8093)  |
| Krzysztof Gryguc                 |   | [ORCID](https://orcid.org/0000-0002-8107-6837)  |


## Team members (version B)
The development team has been led by Dr. Markéta Potůčková and it consists of experts from 4 universities:

<details>
<summary>Charles University, Faculty of Science</summary>

| [Dept. of Applied Geoinformatics and Cartography](https://www.natur.cuni.cz/geography/department-of-applied-geoinformatics-and-cartography?set_language=en)  |   |   |
|:---|:---:|:---:|
| Dr. Markéta Potůčková  | [web](https://www.natur.cuni.cz/geografie/geoinformatika-kartografie/mpot)  | [ORCID](https://orcid.org/0000-0002-8760-790X)  |
| Dr. Lucie Kupková      | [web](https://www.natur.cuni.cz/geografie/geoinformatika-kartografie/lkupkova)  | [ORCID](https://orcid.org/0000-0002-0270-0516)  |
| Dr. Lucie Červená      | [web](https://www.natur.cuni.cz/geografie/geoinformatika-kartografie/cervl7an)  | [ORCID](https://orcid.org/0000-0001-5246-1106)  |
| Alex Šrollerů          |   |   |
| Jakub Dvořák           |   | [ORCID](https://orcid.org/0000-0001-7845-7738)  |
| Adéla Šedová           |   |   |
|   |   |   |
| [**Dept. of Experimental Plant Biology**](https://www.natur.cuni.cz/biology/plant-biology)  |   |   |
| Prof. Jana Albrechtová | [web](http://kfrserver.natur.cuni.cz/lide/albrecht)  | [ORCID](https://orcid.org/0000-0001-6912-1992) |
| Dr. Zuzana Lhotáková   |   | [ORCID](https://orcid.org/0000-0003-3060-641X)  |
| Dr. Lena Hunt          |   | [ORCID](https://orcid.org/0000-0002-7605-1379)  |
| Dr. Eva Neuwirthová    |   | [ORCID](https://orcid.org/0000-0001-5613-847X)  |
</details>

<details>
<summary>Heidelberg University, Institute of Geography</summary>

| [3D Geospatial Data Processing Group](https://www.geog.uni-heidelberg.de/3dgeo/index_en.html)  |   |   |
|---|:---:|:---:|
| Prof. Bernhard Höfle   | [web](https://www.geog.uni-heidelberg.de/gis/hoefle.html)  | [ORCID](https://orcid.org/0000-0001-5849-1461)  |
| Dr. Katharina Anders   | [web](https://www.geog.uni-heidelberg.de/gis/anders.html)  | [ORCID](https://orcid.org/0000-0001-5698-7041)  |
| Sina Antonia Zumstein  |   |   |
</details>

<details>
<summary>University of Innsbruck, Institute for Geography</summary>

| [Remote Sensing & Topographic LiDAR Research Group](https://www.uibk.ac.at/geographie/lidar)  |   |   |
|---|:---:|:---:|
| Dr. Martin Rutzinger   | [web](https://www.uibk.ac.at/geographie/personal/rutzinger)  | [ORCID](https://orcid.org/0000-0001-6628-4681)  |
| Dr. Andreas Mayr       | [web](https://www.uibk.ac.at/geographie/personal/mayr)  | [ORCID](https://orcid.org/0000-0001-8305-4765)  |
</details>

<details>
<summary>University of Warsaw, Faculty of Geography and Regional Studies</summary>

| [Dept. of Geoinformatics, Cartography and Remote Sensing](http://geoinformatics.uw.edu.pl/)  |   |   |
|---|:---:|:---:|
| Dr. Adriana Marcinkowska-Ochtyra | [web](http://geoinformatics.uw.edu.pl/adriana-marcinkowska-ochtyra)  | [ORCID](https://orcid.org/0000-0002-9080-3899)  |
| Dr. Adrian Ochtyra               | [web](http://geoinformatics.uw.edu.pl/adrian-ochtyra)  | [ORCID](https://orcid.org/0000-0003-4799-8093)  |
| Krzysztof Gryguc                 |   | [ORCID](https://orcid.org/0000-0002-8107-6837)  |
</details>
