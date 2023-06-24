# App Guide

## Basics


In the top navigation bar, you will find the "App" button. Clicking on this button allows you to access all the shared or public apps available. If you have a specific app in mind that you would like to create, we are here to assist you. Simply contact us at <support@viascientific.com> for guidance and support.

![image](../images/apps.png)


## -   **Shiny App - DEBrowser**

DEBrowser is an R library which provides an easy way to perform and
visualize DE (Differential Expression) analysis. This module takes count
matrices as input and allows interactive exploration of the resulting
data. You can find their documentation
[here](https://bioconductor.org/packages/release/bioc/vignettes/debrowser/inst/doc/DEBrowser.html).

![image](../images/rnaseq_debrowser.png)


## -   **R-Studio - R-Markdown**

The R-Studio launcher facilitates interactive analysis of the data generated from a run. We have prepared a set of R-Markdown reports that provide access to your report in HTML or PDF format immediately after the run is completed.

For instance, the code below performs differential expression analysis for each comparison listed in the compare file. It generates volcano and MA plots for differentially expressed genes in each comparison:

![image](../images/rstudio-app.png)

## -   **Jupyter Notebook**

The Jupyter Notebook app, due to its interactive and flexible nature, allows bioinformatics researchers to combine code, visualizations, and explanatory text in a single document. Bioinformaticians can write and execute code snippets in real-time, visualize data using various plotting libraries, and document their analyses step-by-step.

![image](../images/jupyter-app.png)

## -   **Shiny App - GSEA Explorer**

GSEA Explorer is an R library that offers a convenient method for conducting and visualizing Gene Set Enrichment Analysis (GSEA). GSEA aims to assess whether a specific gene set or pathway is enriched in gene expression data, indicating its potential biological significance in the studied condition. The GSEA Explorer application can be accessed after executing Foundry's complete RNA-sequencing pipeline or the standalone Differential Expression module. By leveraging GSEA Explorer, researchers can gain valuable insights into the functional implications of gene sets and pathways, aiding in the interpretation of RNA-seq results and facilitating a deeper understanding of biological mechanisms.

![image](../images/gsea_explorer.png)

## -   **Shiny App - Network Explorer**

The Network Explorer allows bioinformaticians to explore and analyze these complex networks, helping them uncover hidden patterns, identify key players, and understand the underlying biological mechanisms. The Network Explorer application can be launched after running Foundry's full RNA-sequencing pipeline or the stand-alone Differential Expression module.

![image](../images/network_explorer.png)

## Recommended Practices for App Development

The following section contains guidelines to help you develop your own apps. Although nothing in this section is required, we find these guideline to help create applications that are both reproducibile and easy to maintain.

### Directory Structure

A directory structure similar to below can be tracked on Github and Dockerhub for easy version control and containerization.

```

|-- parent-directory/
	|-- README.md
	|-- Dockerfile
	|-- app-directory/
		|-- app.R
		|-- R/
			|-- # additional scripts sourced by app
			|--
			|--
		|-- www/
			|-- # CSS files
			|--
			|--
		|-- data/
			|-- # Data files used for app
			|--
			|--
```

### Dockerfile

Docker is an open-source platform that allows developers to automate the deployment and management of applications within lightweight, isolated containers. It provides an additional layer of abstraction and standardization, enabling software to be packaged with all its dependencies and run consistently over time across different environments.

When building a docker, it is best to aim for a minimalistic approach - only including the necessary components and dependencies required for your application.

```
FROM rocker/shiny:4.3.0
LABEL author="zach@viascientific.com" description="Docker image containing all requirements for the Via Scientific GSEA explorer App"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Install System libraries
RUN apt-get update --fix-missing && \
    apt-get install -y gcc unzip curl make zlib1g-dev libglpk-dev libgmp3-dev libxml2-dev pandoc libicu-dev vim

# Install required R packages
RUN R -e 'install.packages(c("shiny", "BiocManager", "dplyr", "DT", "ggplot2", "shinydashboard", "shinydashboardPlus", "shinycssloaders", "igraph", "shinyjs"), \
    repos="https://packagemanager.posit.co/cran/__linux__/focal/2023-06-01")'
RUN R -e "BiocManager::install(version = '3.17')"
RUN R -e "BiocManager::install(c('fgsea', 'clusterProfiler', 'org.Hs.eg.db', 'org.Mm.eg.db'))"

# Copy app directory onto image
ADD gsea-explorer /gsea-explorer/

# Run the app when the container is started
CMD ["R", "-e", "shiny::runApp('/gsea-explorer')"]
```

In the above example, a minimal base image (rocker/shiny:4.3.0) was selected that supports shiny applications. Only the necessary system libraries and R packages are installed. The entire app directory (gsea-explorer) is copied onto the image. Finally, the app is automatically started when the app is run.

[Posit's Package Manager](https://packagemanager.posit.co/client/#/repos/2/packages/A3) is a useful tool in determining which system libraries are necessary for each R package. Navegate to the cran or bioconductor package of interest and look for the "Install System Prerequisities" section. Select the distribution that matches your base image.

Additionally, when using `install.packages()`, setting the `repos` argument to use posit's package manager allows you to both download pre-built binariers (significantly speeding up docker build time) as well as freezing the version of each library to a specific date in time.

### Port Selection

The shiny app file should set the host to `0.0.0.0` and specify the port. An example skeleton is below:

```
ui = dashboardPage(

	# UI Code

)

server = function(input, output, session) {

	# Sever Code

}

options(shiny.host = "0.0.0.0", shiny.port = 8789)
shinyApp(ui = ui, server = server)
```

### Host App on Foundry

To host the app on Foundry, navigate to the `Apps` page and select the `My Apps` tab and then click `Create App`

![image](../images/create_app.png)

#### App Definition File

In the app definition file, set the following values:

![image](../images/app_definition.png)
![image](../images/app_definition_2.png)

1. Set the name of the app
2. If the docker image is hosted on Dockerhub, provide the path
3. Select the container
4. Set status to active
5. The command to run when the container is activated. This can be left blank if the run command was set in the dockerfile. (as above `CMD ["R", "-e", "shiny::runApp('/gsea-explorer')"]`)
6. Set the port number. This should match the port that is set in the app.R file.

	```
	options(shiny.host = "0.0.0.0", shiny.port = 8789)
	```

7. Set Websocket-reconnection-mode to None (default)
8. Set the Container Environment to
	```
	DISABLE_AUTH: true
	WWW_ROOT_PATH: "/api/route/#{proxy.getRuntimeValue('SHINYPROXY_PROXY_ID')}/"
	```

## Support

For any questions or help, please reach out to
<support@viascientific.com> with your name and question.
