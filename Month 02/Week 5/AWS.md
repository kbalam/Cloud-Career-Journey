# Week 5 – AWS Progress

---

### ✅ Topics Covered
- Introduction to Infrastructure as Code (IaC) using Terraform
- Installing and configuring Terraform CLI on Ubuntu Linux
- Writing `provider`, `resource`, `variable` blocks
- Provisioning and destroying S3 buckets and EC2 instances
- Creating IAM users, policies, and roles with trust relationships
- Parameterizing configs using `variables.tf` and `terraform.tfvars`
- Extracting values using `outputs.tf` for dynamic automation
- Modularizing infrastructure using reusable Terraform modules

---

### 🧪 Hands-On
- Installed Terraform CLI inside Ubuntu VirtualBox lab
- Configured AWS provider with CLI IAM credentials
- Created and destroyed an S3 bucket using Terraform
- Launched and SSH’ed into an EC2 instance (`t2.micro`)
- Added Security Group for SSH (port 22)
- Created IAM user using Terraform and role with attached AWS managed policies
- Used `terraform.tfvars` to input dynamic values
- Refactored EC2 and IAM configs into reusable module structure

---

### 📁 Outputs
- [EC2 Creation with SG](.\/Outputs/EC2%20SG%20creation.png)
- [IAM User Creation](./Outputs/IAM_user.png)
- [IAM Role Creation](./Outputs/IAM_role.png)
- [S3 Creation](./Outputs/S3%20creation.png)
---

### 📸 Screenshots
- [CLI – EC2 Instance with SG attached](./Screenshots/ec2_creation.png)
- [CLI – New user from Terraform](./Screenshots/iam_user.png)
- [CLI – New role from Terraform](./Screenshots/iam_role.png)
- [CLI - Crating Module structure (EC2 + IAM)](./Screenshots/CLI_terraform.png)

---

### 🧠 Reflections
- Gained confidence in using Terraform for real AWS provisioning
- Understood stateful resource tracking and declarative config
- Variables and outputs made configs reusable and scalable
- Modules simplified reuse and showed how teams manage infrastructure
- Learned how Terraform fits into real DevOps and automation workflows

---

### 🔗 Resources
- [Terraform Official Docs](https://developer.hashicorp.com/terraform)
- [AWS Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest)
- [Terraform EC2 Resource](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance)
- [Terraform IAM Resources](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_user)
- [Terraform Modules Guide](https://developer.hashicorp.com/terraform/language/modules)
