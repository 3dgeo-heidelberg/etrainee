# R language

R is a scripting/programming language suitable for statistical computing. It offers a wide range of
tools for statistical data analysis, including graphics:
  
[https://www.r-project.org/](https://www.r-project.org/)

It is a free software developed released under the GNU General Public License.

## Download and installation

R can be extended by RStudio, an integrated development environment (IDE) which makes working in R significantly easier.

Firstly, install the core R package from the Comprehensive R Archive Network (CRAN) website:

[https://cran.r-project.org](https://cran.r-project.org)

The installation and administration guidelines are available on the R-project homepage:  

[https://cran.r-project.org/doc/manuals/r-release/R-admin.html](https://cran.r-project.org/doc/manuals/r-release/R-admin.html)

After installing R, RStudio can be downloaded and installed from:

[https://posit.co/download/rstudio-desktop/](https://posit.co/download/rstudio-desktop/)

### Module 2 environment
Contents of Module 2 of this course uses R version 4.3.0 "Already Tomorrow", which you can download from this website: [https://cran.r-project.org/bin/windows/base/old/4.3.0](https://cran.r-project.org/bin/windows/base/old/4.3.0).

A recommended way to setup working environment in RStudio is to use [renv package](https://github.com/rstudio/renv):  

1. Create a New Project
2. Install `renv` using `install.packages("renv")` command
3. Use `renv::init()` to initialize `renv` within a project created in step 1
4. Replace the default `renv.lock` file inside the project folder with the downloaded one: <a href=../assets/r_envs/renv.lock download>download renv.lock</a>
5. Use `renv::restore()` to install the specific package versions recorded in the lockfile

By following these steps you ensure that you will work on the most up-to-date environment that the contents of Module 2 use.


***Note: To ensure compatibility and consistent results across exercises, please adhere to the following specified versions of R and packages. Running exercises on different versions may lead to unexpected results and potential inconsistencies and errors.***

## Getting started / external material

If you are new to R / programming, consider going through one or more of these tutorials first:

Introduction to the R language and statistical analysis:  
[https://cran.r-project.org/doc/manuals/r-release/R-intro.html](https://cran.r-project.org/doc/manuals/r-release/R-intro.html)

Instructions on how to import and export data using R and respective packages:  
[https://cran.r-project.org/doc/manuals/r-release/R-data.html](https://cran.r-project.org/doc/manuals/r-release/R-data.html)
