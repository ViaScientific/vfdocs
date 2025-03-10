# Data Guide

The Data Guide is your go-to resource for learning how to efficiently connect and manage your data with Via Foundry. Whether you're integrating data from external sources or uploading local datasets, Via Foundry has you covered. In this section, we'll walk you through the various features and methods Via Foundry offers for seamless data integration.

## Access your Data in the Cloud

!!! tip

    Foundry readily integrate with Cloud Infrastructure. We recommend using [xCloud](https://www.viascientific.com/products/) to take full advantage of Foundry in your environment.

### Integrate your Cloud with Foundry xCloud

With Foundry [xCloud](https://www.viascientific.com/products/), deploying Via Foundry in your AWS or GCP account has never been easier. Leveraging xCloud, you can set up Via Foundry in your existing cloud environment. This setup allows you to maintain your cloud infrastructure in AWS and Google Cloud while taking advantage of the the robust, feature-rich Via Foundry experience .

Want to get started with Foundry xCloud? Reach out to our support team at <support@viascientific.com>, and we'll get you started.

### Connect your Cloud with Foundry vCloud

For users who want to use Via Foundry public cloud, but want a greater control of data we allow you connect your private S3 or Google bucket to Via Foundry [vCloud](https://www.viascientific.com/products/) product. Reach out to support to get started, `support@viascientific.com`.


### Accessing Your Google Cloud Storage Bucket via Web

You can easily manage your Google Cloud Storage bucket through a web interface by accessing a URL in your browser. This allows you to view, upload, and manage the contents of your bucket without needing to use the command line.

To access your bucket, use the following URL format, replacing `<bucket name>` with the name of your bucket:

```
https://storage.cloud.google.com/<bucket name>/
```

For example, if your bucket is named `viafoundry-clt-demo-bucket`, you can access it by navigating to:

```
https://storage.cloud.google.com/viafoundry-clt-demo-bucket/
```

Once there, you'll have full access to the contents of your bucket and can manage your data directly through the Google Cloud Storage web interface:

<figure markdown="span">
    ![image](../../images/gcp-bucket-web.png){ width="650" }
    <figcaption>Google Cloud Storage web interface</figcaption>
</figure>

## Upload from your computer

!!! tip

    When uploading data from your local machine to the cloud, it's crucial to organize your data effectively. This will make it much easier to locate your files when you need them.

!!! Warning "Avoid invalid paths"

    Certain characters are allowed locally, i.e. `/` in Windows, but are problematic in cloud environments. Avoid: `/`. white-spaces, `:`, `"`, `<`, `>`, or `|`, Cloud platform documentation for characters to avoid:

    * [Google Cloud Storage objects](https://cloud.google.com/storage/docs/objects#naming) in paths
    * [Amazon S3 object naming](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html)

### Prerequisites

#### Contact Support

Before you begin, contact Via Scientific support at `support@viascientific.com` to obtain:  

* **Bucket Name/Path** You'll need this to know where to upload data.
* **AWS Credentials** (AWS Access Key and Secret Key) for AWS data transfers.

### Google Cloud CLI Step-by-Step

Install the : Download and install the Google Cloud SDK (`gcloud`) by following the instructions [here](https://cloud.google.com/sdk/docs/install).

1. **Authenticate with Google Cloud**:
     * After installation, authenticate with your Google account:
     ```bash
     gcloud auth login
     ```
2. **Storage bucket**:
     * [Contact support](mailto:support@viascientific.com) for the bucket path

3. **Uploading a Single File**:

      * To upload a single file to Google Cloud Storage, use the following command:

      ```bash
      gcloud storage cp /local/path/to/your/file.txt gs://<your-bucket-name>/
      ```

      * Example:
      ```bash
      gcloud storage cp /home/user/data/myfile.txt gs://my-storage-bucket/
      ```

      This command uploads the `myfile.txt` from your local system to the Google Cloud Storage bucket named `my-storage-bucket`.

4. **Uploading a Folder**:

      * To upload a folder (including all files and subdirectories within it), use the `-r` flag for a recursive upload:
      ```bash
      gcloud storage cp -r /local/path/to/your/folder gs://<your-bucket-name>/
      ```

      * Example:
      ```bash
      gcloud storage cp -r /home/user/data/myfolder gs://my-storage-bucket/
      ```

      This command uploads the entire contents of the `myfolder` directory (including all files and subdirectories) to the Google Cloud Storage bucket `my-storage-bucket`.

### AWS cli Step-by-Step

Install AWS CLI following the instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

1. **Configure AWS CLI**:
     * Open your terminal or command prompt.
     * Run the following command to configure your AWS CLI with the credentials provided by support:
     ```bash
     aws configure
     ```
     * Enter the Access Key ID, Secret Access Key, and region when prompted.
     * Set `us-east-1` as the region
     * Example configuration:
        ```
        AWS Access Key ID [None]: <ACCESS KEY>
        AWS Secret Access Key [None]: <SECRET ACCESS KEY>
        Default region name [None]: us-east-1
        Default output format [None]:
        ```

2. **Prepare Your Data**:
    * Organize them in a directories on your local machine.
    * The organization on your local machine will match the organization on AWS

3. **Upload Data to S3 Bucket**:
     * Use the `aws s3 cp` command to upload a single file. Replace `<bucket-name>` with the bucket name provided by support and `<file-path>` with the path to your data file or directory.
     * For a single file:
     ```bash
     aws s3 cp <file-path> s3://<bucket-name>/
     ```
     * Use the `aws s3 sync` command to upload all files within the directory, retaining the directory structure starting with `<directory-path>`:
     ```bash
     aws s3 sync <directory-path> s3://<bucket-name>/ --recursive
     ```

4. **Verify Upload**:
     * List the contents of your S3 bucket to verify that your files have been uploaded successfully:
     ```bash
     aws s3 ls s3://<bucket-name>/
     aws s3 ls s3://<bucket-name>/<directory-path>
     ```

### Using Cyberduck

!!! warning

    Cyberduck is a 3rd party tool. Via Scientific doesn't own, control, support, or distribute this tool. It's one of many UI friendly ways to upload data to the Cloud

Cyberduck is an open-source file transfer client for Mac and Windows that supports various protocols, including FTP, SFTP, WebDAV, and cloud storage services such as Amazon S3, Google Drive, Dropbox, and Microsoft OneDrive. It is known for its user-friendly interface, which allows users to connect to and manage files on remote servers or cloud storage accounts easily.

You can use Cyberduck to upload data to Via Foundry. This walkthrough assumes a Mac installation, but similar steps apply to Windows installation.

#### Google Cloud Storage Step-by-Step

You'll need the Bucket Path you received from support. Download Cyberduck for your platform. Follow the instructions [here](https://cyberduck.io/download/)

<iframe width="560" height="315" src="https://www.youtube.com/embed/NQsFhw_-2QU?si=yAJFXTvW0W50oa6W" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

1. Create a new Bookmark, this will take you to the Bookmark configuration window
2. Enter the `Path` you received from Via Scientific Support
3. Close the Bookmark configuration window
4. Open the newly create Google Storage Bookmark
5. Organize data as you want (Create folders, move files, etc...)
6. Right click or Drag and drop files to upload

#### AWS Step-by-Step

You'll need the **Bucket Name** and **AWS Credentials** (Access Key and Secret Key) you received from support. Download Cyberduck for your platform. Follow the instructions [here](https://cyberduck.io/download/)

<figure markdown="span">
    ![image](../../images/data/cyber-1-duck-launch.png){ width="600" }
    <figcaption>Launch Cyberduck and add a new bookmark</figcaption>
</figure>

<figure markdown="span">
    ![image](../../images/data/cyber-2-select-S3.png){ width="600" }
    <figcaption>Select S3 Bookmark</figcaption>
</figure>


<figure markdown="span">
    ![image](../../images/data/cyber-3-set-params.png){ width="600" }
    <figcaption>Enter Bucket name, AWS access key, and Secret access key</figcaption>
</figure>

<figure markdown="span">
    ![image](../../images/data/cyber-4-select-bookmark.png){ width="600" }
    <figcaption>Select newly created bookmark</figcaption>
</figure>

<figure markdown="span">
    ![image](../../images/data/cyber-5-select-upload.png){ width="350" }
    <figcaption>Select "Upload..." from the menu and select a file from your local machine</figcaption>
</figure>
