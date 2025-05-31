# 🪣 AWS S3 Practice – Week 2

## 📌 Topics Covered

- What is S3 and how it stores objects
- Creating buckets via Console and CLI
- S3 bucket naming rules and region selection (Mumbai used)
- Blocking public access and its implications
- Understanding and enabling bucket versioning
- What is a bucket policy (with JSON structure)
- Exploring `Version` in bucket policy
- Installing and configuring AWS CLI
- Checking current CLI region and changing it
- Uploading files to S3 using CLI (`aws s3 cp`)
- Downloading files from S3 using CLI
- Using `aws s3 ls`, `mv`, `rm`, and `sync`
- Creating folder structure in S3 (e.g., `docs/`, `uploads/`)
- Deleting specific files and entire folders (`--recursive`)
- Cleaning up buckets via CLI and Console
- Identifying sensitive info for GitHub screenshots

---

## 🧪 Hands-On Practice

### ✅ Bucket Operations via Console
- Created `my-practise-bucket-01` in **ap-south-1 (Mumbai)** region
- Blocked public access
- Enabled versioning (understood how versions are tracked)

### ✅ Permissions
- Explored JSON-based bucket policy
- Understood `"Version"` tag (policy language version)
- Differentiated between public and private access settings

### ✅ CLI Practice

```bash
# Check all buckets
aws s3 ls

# Create a bucket
aws s3 mb s3://my-practise-bucket-01 --region ap-south-1

# Upload file to S3
aws s3 cp sample_file.txt s3://my-practise-bucket-01/uploads/

# Download file from S3
aws s3 cp s3://my-practise-bucket-01/uploads/sample_file.txt ./downloaded_file.txt

# List bucket contents
aws s3 ls s3://my-practise-bucket-01/
aws s3 ls s3://my-practise-bucket-01/uploads/ --recursive

# Move file within bucket
aws s3 mv s3://my-practise-bucket-01/uploads/sample_file.txt s3://my-practise-bucket-01/docs/sample_file.txt

# Remove file or folder
aws s3 rm s3://my-practise-bucket-01/uploads/sample_file.txt
aws s3 rm s3://my-practise-bucket-01/docs/ --recursive

# Sync local folder with S3
aws s3 sync ./local-folder/ s3://my-practise-bucket-01/sync-test/

# View ACL
aws s3api get-bucket-acl --bucket my-practise-bucket-01

# Remove bucket (after cleanup)
aws s3 rb s3://my-practise-bucket-01

```

## 📸 Screenshot
Screenshots saved under:
📂 /Week-2/screenshots/

- [AWS Hands On](./screenshots/AWS%20console/)
- [Terminal Practise](./screenshots/Terminal%20Screenshots/)
- [Bucket Policy File](./script/Bucket%20policy.txt)

## 🧠 Reflections
- S3 folders are logical prefixes, not real directories
- You must use --recursive to remove nested files/folders
- Bucket policies must use "Version": "2012-10-17" to work correctly
- Always verify and clean up after practice to avoid Free Tier limits
- Region matters — CLI uses config's default, Console can override it

## 📚 Resources 
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/s3/)
- [Amazon Free Tier](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)


