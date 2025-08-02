variable "region"{
	type = string
	default = "ap-south-1"
}

variable "instance_type"{
	type = string
	default= "t2.micro"
}

variable "ami"{
	type  = string
}

variable "key"{
	type = string
}

variable "bucket_name"{
	type = string
}

variable "user_name"{
	type = string
}

variable "iam_user_policy_arn"{
	type = string
}

variable "role_name"{
	type = string
}

variable "iam_role_policy_arn"{
	type = string

}
