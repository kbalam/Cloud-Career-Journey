# Week 06 – Cloud Learning Track

---

## ✅ Topics Covered – Day 1

- S3 architecture and permission models
- Types of access errors (403, 404, etc.)
- IAM policies vs bucket policies vs ACLs
- Block public access settings
- Using AWS CLI to simulate and debug S3 access issues

---

## 🧪 Hands-On

- Created an S3 bucket using the AWS CLI and Console
- Uploaded test object (Sample.txt) via CLI
- Created IAM user with restricted S3 access
- Simulated the following S3 errors:
  - `403 AccessDenied`: No permission or blocked by policy
  - `404 Not Found`: Object missing or wrong bucket
  - `400 Bad Request`: Invalid bucket/object URL
- Used the `--debug` flag to trace CLI permission failures
- Fixed permission issues step-by-step:
  - Updated IAM policy to allow `s3:GetObject`
  - Removed explicit deny from bucket policy

---

## 📁 Outputs

- [S3 bucket name: `my-debugger-bucket`](./Outputs/S3%20creation.png)
- [S3 Object creation: `Samle.txt`](./Outputs/S3OjectUploaded.png)
- [IAM user: `brokenUser`](./Outputs/IAM%20user.png)
- [CLI test results (403)](./Screenshots/CLI%20-%20%20S3%20Error%20Message.png)

---

## 📸 Screenshots

- [CLI - S3 bucket created](./Screenshots/CLI%20-S3.png)
- [CLI - Object uploaded](./Screenshots/CLI%20-%20Uploading_file.png)
- [CLI - Attaching Bucket Policy](./Screenshots/CLI%20-%20Attaching%20Bucket%20Policy.png)
- [CLI - Attaching IAM Policy](./Screenshots/CLI%20-%20Attaching%20Iam%20Policy.png)
- [CLI - Debbugging S3](./Screenshots/CLI%20-%20Debugging%20S3.png)
- [Permission error (403) on CLI](./Screenshots/CLI%20-%20BucketPolicyRestriction.png)

---

## Scripts

- [IAM Policy](./Scripts/policy.json)
- [Bucket Policy](./Scripts/S3ReadOnlyPolicy.json)

## 🧠 Reflections

- Learned how S3 permissions are layered: IAM + bucket policy + block public access
- `403` can mean multiple root causes — not just lack of permission
- `404` happens even with permission if the object path is wrong
- CLI `--debug` flag is extremely helpful for root cause tracing
- This mirrors how real customer S3 issues come in at L1 support level

---

## 🔗 Resources

- [S3 Bucket Policy Examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html)
- [Understanding Amazon S3 Access Permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html)
- [AWS CLI S3 Commands](https://docs.aws.amazon.com/cli/latest/reference/s3/)
