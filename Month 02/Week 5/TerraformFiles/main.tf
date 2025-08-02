provider "aws"{
	region = var.region
}

# EC2
module "ec2_instance"{
	source = "./modules/ec2"
	instance_type = var.instance_type
	key = var.key
	ami = var.ami
}

#S3
module "s3_bucket"{
	source = "./modules/s3"
	bucket_name = var.bucket_name
}

#IAM
module "iam"{
	source = "./modules/iam"
	user_name = var.user_name
	iam_user_policy_arn = var.iam_user_policy_arn
	role_name = var.role_name
	iam_role_policy_arn  = var.iam_role_policy_arn
}


