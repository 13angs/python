# Managing S3 Folders Using `s3cmd`

This document provides step-by-step instructions on how to manage folders in Amazon S3 (or compatible object storage like Linode) using `s3cmd`. The guide covers installation, configuration, making a folder public, generating public URLs for files, and deleting all files in a folder.

## 1. Install `s3cmd`

If you haven't installed `s3cmd` yet, you can do so using `pip`:

```bash
pip install s3cmd
```

This command installs `s3cmd`, a command-line tool for managing Amazon S3 and S3-compatible object storage services.

## 2. Configure `s3cmd`

After installing `s3cmd`, you need to configure it with your AWS credentials (or credentials for another S3-compatible service like Linode Object Storage). Run the following command:

```bash
s3cmd --configure
```

This command will prompt you to enter your access key, secret key, and other configuration settings.

> **Note**: If you are using Linode Object Storage, refer to [this guide](https://techdocs.akamai.com/cloud-computing/docs/using-s3cmd-with-object-storage#configure-s3cmd) for detailed configuration instructions.

## 3. Make an Entire Folder Public

To make all the files in a specific folder (and the folder itself) publicly accessible, use the `s3cmd setacl` command:

```bash
s3cmd setacl s3://your-bucket-name/your-folder-name/ --acl-public --recursive
```

- Replace `your-bucket-name` with the name of your S3 bucket.
- Replace `your-folder-name` with the name of the folder you want to make public.

### Explanation:
- The `--acl-public` flag sets the Access Control List (ACL) to public, making the files accessible to anyone.
- The `--recursive` flag ensures that the command applies to all files and subfolders within the specified folder.

## 4. Verify the Public Access

After making the folder public, you can verify that the files are publicly accessible by listing the ACLs of the files:

```bash
s3cmd info s3://your-bucket-name/your-folder-name/filename
```

Replace `filename` with the actual file name. The output should indicate that the file is public.

## 5. Generate Public URLs for All Files

To generate the public URLs for all the files in a folder, you can use the following command:

```bash
s3cmd ls s3://your-bucket-name/your-folder-name/ | awk '{sub("s3://your-bucket-name", ""); print "https://your-bucket-name.ap-south-1.linodeobjects.com" $4}' > s3_links.txt
```

### Explanation:
- This command lists all files in the specified folder.
- The `awk` command processes each line, removing the `s3://your-bucket-name` prefix from the file paths and appending them to the base URL (`https://your-bucket-name.ap-south-1.linodeobjects.com`).
- The result is saved in the `s3_links.txt` file, which contains the public URLs of all files.

## 6. Delete All Files in a Specific Folder

To delete all the files in a specific folder in your S3 bucket, use the following command:

```bash
s3cmd del s3://your-bucket-name/your-folder-name/ --recursive
```

### Explanation:
- The `s3cmd del` command deletes the specified files.
- The `--recursive` flag ensures that all files and subfolders within the specified folder are deleted.