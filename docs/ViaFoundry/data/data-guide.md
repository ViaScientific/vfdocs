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

## Upload from your computer

!!! tip

    When uploading data from your local machine to the cloud, it's crucial to organize your data effectively. This will make it much easier to locate your files when you need them.

### Prerequisites

#### Contact Support

Before you begin, contact Via Scientific support at `support@viascientific.com` to obtain:  

* **Bucket Name/Path** You'll need this to know where to upload data.
* **AWS Credentials** (AWS Access Key and Secret Key) for AWS data transfers.
* **Project ID** Unique identifier for the Google Cloud project for Google CLoud

### Using CLI with `gsutil`

Before you can upload files, make sure you have these things ready:

* ***Google Cloud SDK Installed**  The Google Cloud SDK contains `gsutil`, the tool you’ll use to upload files. Follow the official [installation guide](https://cloud.google.com/sdk/docs/install) to set it up on your computer.
* **Google Cloud Project**  You must have access to a Google Cloud project with permission to use Cloud Storage.
* **Google Cloud Storage Bucket** You need a bucket where your files will be stored. If you're unsure what your bucket name is, **reach out to Via Scientific Support**.
* **Login Credentials** Make sure you can log in to Google Cloud and access your project. You’ll use your Google account, again **reach out to Via Scientific Support** if there are issues here.

#### GCP Step-by-Step

1. Authenticate with Google Cloud

    First, open your terminal (on Mac/Linux) or command prompt (on Windows) and log in to your Google account by typing:

    ```bash
    gcloud auth login
    ```

    This will open a browser window asking you to log in. Once you’ve logged in, close the browser and return to the terminal.

2. Confirm Your Google Cloud Project

    To make sure you're working in the right project, run the following command to check which project is currently active:

    ```bash
    gcloud config list project
    ```

    If you need to change the project, use this command:

    ```bash
    gcloud config set project YOUR_PROJECT_ID
    ```

    (Replace `YOUR_PROJECT_ID` with the ID of your project. If you don't know your project ID, reach out to support.)

3. Upload a File Using `gsutil`

    Now that you're logged in and working in the correct project, you can upload your file to Google Cloud Storage. Use the following command to upload a file:

    ```bash
    gsutil cp /path/to/your/file gs://YOUR-BUCKET-NAME/
    ```

    - Replace `/path/to/your/file` with the actual location of the file on your computer.
    - Replace `YOUR-BUCKET-NAME` with the name of your Google Cloud Storage bucket. If you're unsure, **contact your IT support team** for this information.

    For example, if you want to upload a file called `data.csv` from your desktop, you would use a command like this:

    ```bash
    gsutil cp ~/Desktop/data.csv gs://my-research-bucket/
    ```

4. Upload Multiple Files or a Whole Folder

    To upload multiple files or an entire folder, use the `-r` option (for recursive). For example, to upload a folder named `experiment_data` from your desktop, type:

    ```bash
    gsutil cp -r ~/Desktop/experiment_data gs://YOUR-BUCKET-NAME/
    ```

    This will upload all the files in the folder and any subfolders inside it.

5. Check Your Upload

    After uploading, you can verify the files were uploaded by listing the files in your bucket. Use this command:

    ```bash
    gsutil ls gs://YOUR-BUCKET-NAME/
    ```

    This will display all the files currently stored in the bucket.


??? note "Troubleshooting Google Cloud data uploads"

    If you encounter any issues, like not knowing your bucket name or needing access to a project, **reach out to your VIA Scientific Support**. You may need help with:

    - **Project ID**: The specific project where your data is stored.
    - **Bucket Name**: The location where your files need to be uploaded.
    - **Permissions**: Ensuring you have the right access to upload files.

### Using CLI using `aws cli`

* Install AWS CLI following the instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

#### Step-by-Step

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

You'll need the Bucket Path and Google Cloud Platform Project ID you received from support. Download Cyberduck for your platform. Follow the instructions [here](https://cyberduck.io/download/)

!!! Danger "Add video on the data transfer"

    Add video on the data transfer

1. Create a new Bookmark, this will take you to the Bookmark configuration window
2. Enter `Project ID` you received from Via Scientific Support
3. Enter the `Path` you received from Via Scientific Support
4. Close the Bookmark configuration window
5. Open the newly create Google Storage Bookmark
6. Organize data as you want (Create folders, move files, etc...)
7. Right click or Drag and drop files to upload

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
