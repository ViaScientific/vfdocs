# Uploading Files to Via Foundry

- [Uploading Files to Via Foundry](#uploading-files-to-via-foundry)
  - [Configure xCloud](#configure-xcloud)
  - [Upload to our bucket using `aws cli`](#upload-to-our-bucket-using-aws-cli)
    - [Prerequisites:](#prerequisites)
    - [Step-by-Step Instructions:](#step-by-step-instructions)
    - [Example:](#example)

---

## Configure xCloud

[xCloud](https://www.viascientific.com/products/)

## Upload to our bucket using `aws cli`

### Prerequisites:

Ensure you have the AWS CLI installed. If not, follow the instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

### Step-by-Step Instructions:

1. **Contact Support**:
   - Before you begin, contact Via Scientific support at `support@viascientific.com` to obtain:
     - **Bucket Name**
     - **AWS Credentials** (Access Key and Secret Key)

2. **Configure AWS CLI**:
   - Open your terminal or command prompt.
   - Run the following command to configure your AWS CLI with the credentials provided by support:
     ```bash
     aws configure
     ```
   - Enter the Access Key ID, Secret Access Key, and region when prompted.
     - Set `us-east-1` as the region
     - Leave the default output format as `json`.

3. **Prepare Your Data**:
   - Ensure your data files are ready for upload. Organize them in a directory on your local machine.

4. **Upload Data to S3 Bucket**:
   - Use the `aws s3 cp` command to upload your data. Replace `<bucket-name>` with the bucket name provided by support and `<file-path>` with the path to your data file or directory.
   - For a single file:
     ```bash
     aws s3 cp <file-path> s3://<bucket-name>/
     ```
   - For a directory (uploads all files within the directory):
     ```bash
     aws s3 cp <directory-path> s3://<bucket-name>/ --recursive
     ```

5. **Verify Upload**:
   - List the contents of your S3 bucket to verify that your files have been uploaded successfully:
     ```bash
     aws s3 ls s3://<bucket-name>/
     ```

### Example:
If you have a file `data.csv` and a bucket name `via-foundry-bucket`, your commands will look like this:
```bash
aws s3 cp data.csv s3://via-foundry-bucket/
aws s3 ls s3://via-foundry-bucket/
```

By following these steps, you can efficiently upload your data to Via Foundry using the AWS CLI. If you encounter any issues, please reach out to Via Scientific support at `support@viascientific.com`.
