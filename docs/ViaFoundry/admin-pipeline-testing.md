# Pipeline Testing

## Configuration of Run Environment

Once logged in, click on the profile tab in the top right of the screen. You'll notice several tabs to explore in profile page.

- **Run environments:** This is your main segment for creating connection profiles for users.
- **SSH Keys:** where you can create new or enter existing SSH key pairs to establish connection to any kind of host.
  Before creating run environment, SSH Keys needed to be created in SSH Keys tab. For more details to define the cluster please check the [documentation](../profile)

## Executing Test Run

To test a pipeline, you can follow these steps:

1. Visit the following link: [RNA-Seq pipeline](https://www.viafoundry.com/pipeline/219).

2. On the webpage, locate the "download pipeline" button and click on it. This will initiate the download of a zip file.

3. Once the zip file is downloaded, extract its contents. Inside the extracted folder, you will find a file named `main.dn`. This file contains the pipeline definition and can be used for importing the pipeline.

4. Now, go to the "pipelines" tab on the ViaFoundry website.

5. Look for the "Create Pipeline" button and click on it. This will open the pipeline creation interface.

6. In the pipeline creation interface, you will find an option to import a pipeline. Drag and drop the `main.dn` file that you extracted earlier into the designated area.

7. The pipeline will be imported, and you can proceed with further customization or execution as needed.

To enable the necessary inputs for each selected genome in the RNA-Seq pipeline:

- Enable `run_Download_Genomic_Sources` step.
- For Sequential mapping, enable `download_build_sequential_mapping_indexes`.
- For STAR, enable `build_STAR_index`.
- For RSEM, enable `build_RSEM_index`.
- For HISAT2, enable `build_Hisat2_index`.
- For Tophat, enable `build_Bowtie2_index`.
- For Kallisto, enable `build_Kallisto_index`.

Enabling these options ensures that the required indexes for each selected genome are built and utilized in the RNA-Seq pipeline.
