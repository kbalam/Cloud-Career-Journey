# Week 06 – Cloud Learning Track

---

This week focuses on practical troubleshooting tasks for common AWS services (S3, EC2) aligned with real-world support issues. Each day simulates a support ticket with CLI-based debugging, step-by-step fixes, and reflection.

---

## ✅ Topics Covered

| Day | Service | Focus Area |
|-----|---------|------------|
| 1   | S3      | Access issues, permission models, 403/404 debugging |
| 2   | EC2     | SSH access, security groups, key pair recovery      |

---

## 🧪 Hands-On Summary

### 🟦 **Day 1: S3 Access Troubleshooting**

**Simulated Errors:**
- `403 AccessDenied`: Missing or blocked permission
- `404 Not Found`: Wrong object or bucket
- `400 Bad Request`: Invalid URL syntax

**Key Tasks:**
- Created S3 bucket via CLI/Console
- Uploaded test object
- Created IAM user with limited access
- Simulated and fixed permission errors using IAM and bucket policies
- Used `--debug` flag to trace CLI-level access issues

---

### 🟩 **Day 2: EC2 Boot & SSH Access Troubleshooting**

**Simulated Errors:**
- Timeout on SSH (port 22 blocked)
- Key pair not attached
- Wrong SSH user
- Console logs missing

**Key Tasks:**
- Launched EC2 without key pair + blocked port 22
- Attempted SSH from local Ubuntu VM
- Debugged using:
  - `describe-instances`
  - `get-console-output`
- Fixed by:
  - Opening port 22 in SG
  - Relaunching EC2 with valid key pair
  - Using correct SSH user (`ubuntu`)
  - Rebooting instance and checking logs

---

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

---

## Policies

- [IAM Policy](./Scripts/policy.json)
- [Bucket Policy](./Scripts/S3ReadOnlyPolicy.json)

## 🧠 Reflections

- 🔐 **S3:** Realized how access to objects depends on IAM + bucket policy + block public access. `403` errors are not always straightforward.
- 💻 **EC2:** Gained hands-on experience with SSH troubleshooting: SG misconfig, key mismatch, wrong username — just like real-world escalations.
- 🛠️ CLI tools like `--debug`, `describe-instances`, and `get-console-output` are critical in support triage workflows.

---

## 🔗 Resources

- [S3 Bucket Policy Examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html)
- [EC2 Key Pair Troubleshooting](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)
- [SSH Troubleshooting for EC2](https://repost.aws/knowledge-center/ec2-linux-resolve-ssh-connection-errors)
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/index.html)
