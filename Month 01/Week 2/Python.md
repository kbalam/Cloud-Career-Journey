# 🐍 Python Practice – Week 2

---

## 📌 Topics Covered

- Setting up Python virtual environment in project folder
- Installing boto3 within venv and confirming installation with pip freeze
- Understanding AWS credentials on local system (from AWS CLI config)
- Using boto3.client() to connect to AWS S3
- Uploading a file to S3 bucket using upload_file() method
- Handling upload logs using Python logging
- Writing logs to a text file
- Handling FileNotFoundError and UnicodeEncodeError in Windows
- Testing script with different files
- Understanding object overwrite behavior when the same key is uploaded again
- Basic directory management with os.makedirs()

---

## 🧪 Hands-On Practice

### ✅ Virtual Environment Setup

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Install boto3 inside venv
pip install boto3

# Confirm installation
pip freeze

```

### ✅ AWS Credentials Setup
AWS credentials were already configured via AWS CLI:

```bash
aws configure
On Windows, boto3 auto-detects credentials from this path:

makefile
C:\Users\<username>\.aws\credentials
```

## ✅ Upload Script (Python)

### 🧠 Logic Covered:

Create boto3 S3 client:

```Python
#Create boto3 S3 client:
s3 = boto3.client('s3')

#Upload file to S3:
s3.upload_file(local_file, bucket_name, object_key)

#Create logs directory and write upload messages:
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
with open(LOG_FILE, "a") as log:
    log.write(message + "\n")
```
✅ Used upload_file() method
✅ Tested with different files and keys

## ✅ Error Handling & Debugging

🛠️ UnicodeEncodeError
- Occurred due to emoji and Windows cp1252 encoding
- Fixed by removing emoji from log messages

🛠️ FileNotFoundError
- Happened when the test file did not exist
- Resolved by creating sample_file.txt

📦 Re-upload Behavior
- Same object key resulted in overwrite (expected behavior in S3)


## ✅ Execution

```bash
# Run Python script
python "Month 01/Week 2/script/s3_upload.py"

📥 File uploaded to:
s3://my-practise-bucket-01/uploads/sample_file.txt
```

## 💡 Reflections
- Learned how AWS SDK for Python (boto3) interacts with S3
- Understood the importance of directory structure and encoding between Windows/Linux
- Noted that S3 overwrites existing objects when uploaded with the same key
- Gained more confidence using virtual environments and writing reusable cloud automation scripts

## 📚 Resources

- [Boto3 Official Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS CLI Configure Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
- [Python os.makedirs() Docs](https://docs.python.org/3/library/os.html#os.makedirs)

## Files

- 📜 Python Script: [`S3_Upload.py`](./script/s3_upload.py)
- 📄 Output File: [`Upload Logs.txt`](./output/upload_logs.txt)

