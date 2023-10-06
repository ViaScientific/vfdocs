# Foundry News

## 14.10.2023
### Foundry Version 1.6.4 Released
#### Features:
- Google Cloud Batch support has been implemented.
- An import pipeline feature is now accessible to all users.
- Foundry pipelines now generate Nextflow DSL2 workflows.
- Metadata Tracker feature added to projects.
- The Metadata tab on the run page now allows bulk file insertion and submitting runs with selected files.
- Introduced a retry feature for SSH queries when submitting a job.
#### Bug Fixes:
- Fixed the Download Pipeline button for nf-core/nextflow pipelines.
- Emails updating on run status now include a link to the Foundry platform.
- Addressed a bug affecting the initial runs for triple and quadruple samples.
- Resolved issues with downloading the same report files multiple times in apps.

### Pipeline Releases:
- TE Transcripts Pipeline is now available.

### App Releases:
- IGV Browser is now released.
- TCGA App is now released.


## 14.07.2023

### Foundry Version 1.6.3 Released

#### Features:
- Updated the Pipeline files section to improve the overall user experience.
- Introduced the pipeline revision feature, allowing users to track and manage revisions effectively.

#### Bug Fixes:
- Fixed a bug related to module name changes on module revision update.
- Resolved the issue with the run duration column for initial runs, displaying accurate information.
- Fixed the broken symlinks error during NF-core/Nextflow run creation.

### Pipeline Releases:
- DE Analysis Module is now available.
- LimmaVoom module is now available.
- Fastqc module is now available.

### App Releases:
- Network Explorer is now released.
- PCA Explorer is now released.

## 18.06.2023

### Foundry Version 1.6.2 Released

#### Features:
- Implemented security updates for file accesses to enhance system protection.
- Admin users can now view all groups within the system.
- Added unique group name validation to prevent duplicate group names.
- Introduced the process revision feature, allowing users to track and manage revisions effectively.
- When importing pipelines, users now have the option to either overwrite existing pipelines or create a new revision.
- Pipeline files can now be viewed in a tree structure for improved organization and navigation.
- A new Run Report tab has been added to the pipeline page, providing users example reports related to the pipeline.
- The paramsFile feature has been upgraded, enhancing its functionality and usability.
- Added support for downloading single files from Amazon S3 storage.
- Multiple app selection support added. Run page app section upgraded.

#### Bug Fixes:
- Disabled the spreadsheet mode for S3 files, ensuring compatibility and consistent file handling.
- Fixed CSV parse error in the spreadsheet viewer for seamless data handling.
- Users in the same host environment can now perform single file downloads.

### Pipeline Releases:
- Cell Ranger Multi Pipeline is now available.

### App Releases:
- GSEA Explorer is now released.

## 21.05.2023

### Foundry Version 1.6.1 Released

#### Features:
- NF-core custom param file upload feature added.
- New editor added for run, report, and pipeline pages with image support.
- Import from Bitbucket support added.
- Custom Nextflow pipeline support initiated.
- Core pipeline and use paramsfiles features added.

#### Bug Fixes:
- The upload tab is hidden for AWS batch environments.
- Loading spinner added for the reports tab.
- Reports page loading upgraded.
- Optional channel support added.

### Pipeline Releases:
- scRNA Analysis Module is now available.

### App Releases:
- ISEE App is now released.
- scViewer is now released.

## 05.05.2023

### Foundry Version 1.6.0 Released

#### Features:
- NF-Core pipeline support added.
- Regex support upgraded for S3 file searches.
- Directory tree support was added to the Report page.

#### Bug Fixes:
- Parentheses bug fixed for single file imports.

### Pipeline Releases:
- ATAC-Seq Pipeline is now available.
- CHIP-Seq Pipeline is now available.

### App Releases:
- Jupyter Notebook Lab is now released.
- Cellxgene App is now released.
- DEBrowser App is now released.
- Rstudio App is now released.