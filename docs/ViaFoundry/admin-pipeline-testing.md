# Pipeline Testing

## Downloading Genome files

```
# Set localdownload directory
genomedata="/opt/viafoundry/run_data"

## Main Genomes
wget https://web.dolphinnext.com/umw_biocore/dnext_data/genome_data/human/hg38/ -P ${genomedata}/genome_data/human/hg38/ -l inf -nc -nH --cut-dirs=4 -r --no-parent -R "index.html*"
wget https://web.dolphinnext.com/umw_biocore/dnext_data/genome_data/mouse/mm10/ -P ${genomedata}/genome_data/mouse/mm10/ -l inf -nc -nH --cut-dirs=4 -r --no-parent -R "index.html*"
wget https://web.dolphinnext.com/umw_biocore/dnext_data/genome_data/mousetest/mm10/ -P ${genomedata}/genome_data/mousetest/mm10/ -l inf -nc -nH --cut-dirs=4 -r --no-parent -R "index.html*"


## Optional Genomes
wget https://web.dolphinnext.com/umw_biocore/dnext_data/genome_data/human/hg19/ -P ${genomedata}/genome_data/human/hg19/ -l inf -nc -nH --cut-dirs=4 -r --no-parent -R "index.html*"
wget https://web.dolphinnext.com/umw_biocore/dnext_data/genome_data/rat/rn6/ -P ${genomedata}/genome_data/rat/rn6/ -l inf -nc -nH --cut-dirs=4 -r --no-parent -R "index.html*"
wget https://web.dolphinnext.com/umw_biocore/dnext_data/genome_data/c_elegans/ce11/ -P ${genomedata}/genome_data/c_elegans/ce11/ -l inf -nc -nH --cut-dirs=4 -r --no-parent -R "index.html*"
wget https://web.dolphinnext.com/umw_biocore/dnext_data/genome_data/d_melanogaster/BDGP6_32/ -P ${genomedata}/genome_data/d_melanogaster/BDGP6_32/ -l inf -nc -nH --cut-dirs=4 -r --no-parent -R "index.html*"
wget https://web.dolphinnext.com/umw_biocore/dnext_data/genome_data/dog/canFam3/ -P ${genomedata}/genome_data/dog/canFam3/ -l inf -nc -nH --cut-dirs=4 -r --no-parent -R "index.html*"
wget https://web.dolphinnext.com/umw_biocore/dnext_data/genome_data/e_coli/ASM584v2_NC_000913_3/ -P ${genomedata}/genome_data/e_coli/ASM584v2_NC_000913_3/ -l inf -nc -nH --cut-dirs=4 -r --no-parent -R "index.html*"
wget https://web.dolphinnext.com/umw_biocore/dnext_data/genome_data/n_vectensis/jaNemVect1_1/ -P ${genomedata}/genome_data/n_vectensis/jaNemVect1_1/ -l inf -nc -nH --cut-dirs=4 -r --no-parent -R "index.html*"
wget https://web.dolphinnext.com/umw_biocore/dnext_data/genome_data/s_cerevisiae/sacCer3/ -P ${genomedata}/genome_data/s_cerevisiae/sacCer3/ -l inf -nc -nH --cut-dirs=4 -r --no-parent -R "index.html*"
wget https://web.dolphinnext.com/umw_biocore/dnext_data/genome_data/s_pombe/ASM294v2/ -P ${genomedata}/genome_data/s_pombe/ASM294v2/ -l inf -nc -nH --cut-dirs=4 -r --no-parent -R "index.html*"
wget https://web.dolphinnext.com/umw_biocore/dnext_data/genome_data/zebrafish/GRCz11/ -P ${genomedata}/genome_data/zebrafish/GRCz11/ -l inf -nc -nH --cut-dirs=4 -r --no-parent -R "index.html*"


# If you're using AWS Cloud, Sync data with S3 bucket
aws s3 sync -r ${genomedata} s3://DEST_BUCKET/viafoundry/run_data/genome_data
# Remove the local data after syncing with AWS S3
rm -rf ${genomedata}

# If you're using Google Cloud, Sync data with Google Cloud Storage bucket
gsutil rsync -r ${genomedata} gs://DEST_BUCKET/viafoundry/run_data/genome_data
# Remove the local data after syncing with Google Cloud Storage
rm -rf ${genomedata}

```

## Configuration of Run Environment

Once logged in, click on the profile tab in the top right of the screen. You'll notice several tabs to explore in profile page.

- **SSH Keys:** Needs to be configured to setup a [connection](../profile/#ssh-keys)
- **Run environments:** This is your main segment for creating connection profiles for users.

  - **Run environments:** -> **Profile Variables** : Set the following directory for DOWNDIR:

    ```
    ## A. For Google Cloud:
    ## if genome_data located at gs://DEST_BUCKET/viafoundry/run_data/genome_data
    params.DOWNDIR = "gs://DEST_BUCKET/viafoundry/run_data"

    ## B. For AWS Cloud:
    ## if genome_data located at s3://DEST_BUCKET/viafoundry/run_data/genome_data
    params.DOWNDIR = "s3://DEST_BUCKET/viafoundry/run_data"

    ## C. For Local Execution (eg. clusters):
    ## if genome_data located at /opt/viafoundry/run_data/genome_data
    params.DOWNDIR = "/opt/viafoundry/run_data"
    ```

  - **Run environments:** -> **Default Working Directory** : Set the following directory for runs:
  ```
  /opt/runs
  ```

  - **Run environments:** -> **Default Bucket Location for Publishing** : Set the following directory for cloud environmets:
    ```
    s3://DEST_BUCKET/viafoundry/runs
    or
    gs://DEST_BUCKET/viafoundry/runs
    ```


## Executing Test Run

To test a pipeline, you can follow these steps:

1. Visit the following link: [RNA-Seq pipeline](https://www.viafoundry.com/pipeline/219).

2. On the webpage, locate the "download pipeline" button and click on it. This will initiate the download of a zip file.

3. Once the zip file is downloaded, extract its contents. Inside the extracted folder, you will find a file named `main.dn`. This file contains the pipeline definition and can be used for importing the pipeline.

4. Now, go to the "pipelines" tab on the ViaFoundry website.

5. Look for the "Create Pipeline" button and click on it. This will open the pipeline creation interface.

6. In the pipeline creation interface, you will find an option to import a pipeline. Drag and drop the `main.dn` file that you extracted earlier into the designated area.

7. The pipeline will be imported, and you can proceed with further customization and execution.

