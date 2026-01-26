# Single Cell RNA-seq Analysis on Via Foundry

## Introduction

This document provides a walkthrough for researchers with wet-lab experience who wish to conduct single-cell RNA sequencing (scRNA-seq) analyses using the Via Foundry platform. The goal is to guide users through the computational steps necessary to process scRNA-seq data, from raw inputs to analyzed results, in an intuitive and streamlined manner.

## Getting Started on Foundry

### Logging into the Via Foundry Platform
To begin using Via Foundry, access the platform via the official website and enter your credentials to log in. If you do not have an account, you will need to register and verify your email address.

### Navigating the Interface
Via Foundry features a user-friendly drag-and-drop interface designed to facilitate easy navigation and project setup. Main components such as 'Projects', 'Pipelines', and 'Datasets' are prominently displayed, making them easy to access and use.

### Accessing and Selecting the Single Cell RNA-sequencing Pipeline
Choose the Single Cell RNA-sequencing pipeline from the list of available pipelines. This selection is designed specifically for processing and analyzing scRNA-seq data.

## Setting Up Your Project and Attaching the Pipeline
Creating a New Project
Start by creating a new project. Name your project and provide a brief description. Organize your workspace by creating folders as needed.

### Attaching the Cell Ranger Pipeline to the Project
Attach the Cell Ranger pipeline, which is commonly used for scRNA-seq data processing. It includes steps like barcode recognition and gene expression counting.

### Preparing for the First Run
Configure your project settings, ensuring all necessary data and files are uploaded and correctly linked to your new project.

## Input Files and Reference Genome

### Requirements for Input Files
Ensure your input files are in FASTQ format, which is required for the subsequent steps of the Cell Ranger pipeline.

### Reference Genome Selection
Select a reference genome for mapping the RNA reads. Users can either upload their custom reference genomes or choose from prebuilt options provided on the platform.

### Setting Input Parameters for the Analysis
Focus on setting parameters in the run_scRNA_Analysis module. Proper parameter setting ensures accurate read alignment, barcode assignment, and gene-cell matrix generation.

## Running the Pipeline

### Starting the Run
Initiate the pipeline run. The computational steps are fully automated, requiring minimal user intervention once the run has started.

### Monitoring Run and Analyzing Logs
Regularly check the progress of your run and review logs to ensure that the process is proceeding without errors.

### Overview of Quality Control Metrics
Upon completion, the pipeline generates several quality control metrics essential for assessing the validity and quality of the output data.

## Common Mistakes to Avoid

### Ensuring Correct Parameter Settings
Verify all input parameters to avoid common errors that could affect the results.

### Importance of Ambient RNA Removal and Doublet Filtering
Implement steps for ambient RNA removal and doublet filtering to improve data quality.

### Adjusting QC Settings
Adjust quality control settings based on the quality of the input data to optimize the output.

## Visualizing Your Results

### Tools for Post-Run Data Visualization
Utilize tools like DEBrowser, Network Explorer, GSEA Explorer, and R Markdown to visualize and analyze the processed data. These tools support a range of analyses including differential expression, network analysis, and gene set enrichment.

### Uploading Gene-Cell Matrix
Post-analysis, upload your gene-cell matrix to these tools and apply visualization techniques such as PCA or t-SNE to explore your data further.

## Conclusion

Via Foundry simplifies the scRNA-seq process, enabling researchers to focus more on their scientific questions and less on computational complexities. Remember to utilize the quality control and visualization tools provided, and do not hesitate to contact support for assistance with any issues that emerge during your analysis.