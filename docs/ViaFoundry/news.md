# Foundry News

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