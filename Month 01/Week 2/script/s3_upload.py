#!/usr/bin/env python3
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from boto3.exceptions import S3UploadFailedError
import os
from datetime import datetime

# === CONFIGURATION ===
BUCKET_NAME = "my-practise-bucket-01"     ## Tested with wrong bucket name
FILE_PATH = "sample_file.txt"         ## Tested with file that is not exist.
OBJECT_NAME = "uploads/sample_file.txt"  
LOG_FILE = "../output/upload_logs.txt"  

# === Checking if Bucket exist Logic ===
def check_bucket_exists(bucket_name):
    s3 = boto3.client("s3")
    try:
        s3.head_bucket(Bucket=bucket_name)
        return True
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            error = f"[{datetime.now()}] ❌ Bucket '{bucket_name}' does not exist."
        elif error_code == 403:
            error = f"[{datetime.now()}] ❌ Access denied to bucket '{bucket_name}'."
        else:
            error = f"[{datetime.now()}] ❌ Error checking bucket: {e}"
        print(error)
        log_to_file(error)
        return False


# === Upload Logic ===
def upload_to_s3(file_path, bucket, object_name):

    if not check_bucket_exists(bucket):
        return
    
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket, object_name)
        log_msg = f"[{datetime.now()}] ✅ Uploaded '{file_path}' to 's3://{bucket}/{object_name}'"
        print(log_msg)
        log_to_file(log_msg)
    except FileNotFoundError:
        error = f"[{datetime.now()}] ❌ File not found: {file_path}"
        print(error)
        log_to_file(error)
    except NoCredentialsError:
        error = f"[{datetime.now()}] ❌ AWS credentials not found"
        print(error)
        log_to_file(error)
    except ClientError as e:
        error = f"[{datetime.now()}] ❌ AWS Error: {e}"
        print(error)
        log_to_file(error)
    except S3UploadFailedError as e:
        error = f"[{datetime.now()}] ❌ Upload failed: {e}"
        print(error)
        log_to_file(error)


# === Logger ===
def log_to_file(message):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(message + "\n")

# === Entry Point ===
if __name__ == "__main__":
    upload_to_s3(FILE_PATH, BUCKET_NAME, OBJECT_NAME)
