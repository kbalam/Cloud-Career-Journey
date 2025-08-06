# Week 06 – Cloud Learning

This week simulates common real-world AWS support issues using CLI, debugging flags, and IAM policy evaluation. Each task mirrors actual L1/L2 support tickets handled in production environments.

---

## ✅ Topics Covered

| Day | Service | Focus Area                                      |
|-----|---------|--------------------------------------------------|
| 1   | S3      | Access issues, permission models, 403/404 errors |
| 2   | EC2     | SSH access, key pair & security group issues     |
| 3   | IAM     | AccessDenied errors & policy troubleshooting     |

---

## 🧪 Hands-On Summary

---

### 🟦 **Day 1: S3 Access Troubleshooting**

**Simulated Errors:**
- `403 AccessDenied` – IAM or bucket policy restriction
- `404 NotFound` – Missing object or wrong path
- `400 BadRequest` – Malformed URL

**Actions Taken:**
- Created S3 bucket via Console & CLI  
- Uploaded object using CLI  
- Created IAM user with limited permissions  
- Simulated access errors by removing `s3:GetObject`  
- Added inline policy, removed explicit deny  
- Used `--debug` CLI flag for tracing errors  

---

### 🟩 **Day 2: EC2 SSH & Boot Debugging**

**Simulated Issues:**
- SSH timeout → Port 22 blocked  
- Permission denied → Wrong user  
- Missing key pair → Unable to connect  
- Instance boot errors → No system logs

**Actions Taken:**
- Launched EC2 with no SSH access + wrong user  
- SSH from local Ubuntu VM failed  
- Used:
  - `aws ec2 describe-instances`
  - `aws ec2 get-console-output`
- Fixed by:
  - Adding port 22 in SG  
  - Relaunching with proper key pair  
  - Using correct username (`ec2_user`)  
  - Rebooting instance and checking logs  

---

### 🟨 **Day 3: IAM AccessDenied Debugging**

**Simulated Case:**
IAM user running CLI commands fails with:

 `An error occurred (AccessDenied) when calling the DescribeInstances operation: User is not authorized to perform: ec2:DescribeInstances`


**Root Causes Simulated:**
- No policy attached for EC2 access  
- Explicit deny (optional test)  
- Policy allows only specific resources or regions  
- Wrong CLI profile

**Steps Taken:**
1. Created IAM user `brokenIAMUser` with S3 read-only access  
2. Configured CLI profile:
    `aws configure --profile brokenIAMUser`

```bash
aws s3 ls --profile brokenIAMUser                          # ✅ Success
aws ec2 describe-instances --profile brokenIAMUser         # ❌ AccessDenied
aws ec2 describe-instances --debug --profile brokenIAMUser # 🔍 Traced
```

Fixed by attaching:

`AmazonEC2ReadOnlyAccess`

or inline custom policy allowing `ec2:DescribeInstances`

Re-tested and validated access

---

## 📁 Outputs

- [S3 bucket name: `my-debugger-bucket`](./Outputs/S3%20creation.png)
- [S3 Object creation: `Sample.txt`](./Outputs/S3OjectUploaded.png)
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

- [EC2 Issue Simulation](./Screenshots/Simulating%20EC2%20issue.png)
- [Debugged KeyPair issue](./Screenshots/Debugged%20Keypair%20issue.png)
- [Debugged SSH issue](./Screenshots/Dubugging%20SSH.png)

- [IAM User with limited access](./Screenshots/IAM%20with%20limited%20access.png)
- [Debugging IAM access issue](./Screenshots/Dubbging%20IAM%20issue.png)
- [IAM Explicit Deny Policy](./Screenshots/IAM%20inline%20Deny%20policy.png)

---

## Policies

- [IAM Policy](./Policies/policy.json)
- [Bucket Policy](./Policies/S3ReadOnlyPolicy.json)
- [Inline IAM Policy](./Policies/inline_policy.json)

---

### 🔐 Fix Steps Summary

| Issue                    | Root Cause                             | Fix Applied                                      |
|--------------------------|----------------------------------------|--------------------------------------------------|
| S3 AccessDenied          | No permission or explicit deny         | Updated IAM and bucket policies                  |
| EC2 SSH timeout          | Port 22 not open                       | Added inbound rule in SG                         |
| EC2 Permission denied    | Key pair missing or wrong user         | Used valid key + default username                |
| IAM AccessDenied on EC2  | Missing `ec2:DescribeInstances`        | Attached EC2 read-only policy                    |
| Wrong CLI profile        | Wrong key or region in config          | Switched to correct profile                      |


## 🧠 Reflections

- S3 access issues often result from multi-layered policies (IAM + bucket + block public access).
- EC2 SSH failures mimic real-world panic cases — knowing how to read console logs is crucial.
- IAM permission debugging using --debug and understanding evaluation flow is a core support skill.
- CLI profile separation is great for testing policies in isolation — just like support engineers do.

## 🔗 Resources

- [IAM Policy Evaluation Logic](./https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [S3 Permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-actions)
- [EC2 SSH Troubleshooting](https://repost.aws/knowledge-center/ec2-linux-resolve-ssh-connection-errors)
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/)