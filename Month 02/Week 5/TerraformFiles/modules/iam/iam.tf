
resource "aws_iam_user" "test_user"{
	name = var.user_name
}

resource "aws_iam_user_policy_attachment" "ec2_policy"{
	user = aws_iam_user.test_user.name
	policy_arn = var.iam_user_policy_arn
}


# IAM role

resource "aws_iam_role" "ec2-role"{
	name = var.role_name

	assume_role_policy = jsonencode({
		Version = "2012-10-17",
		Statement = [
			{
			Effect = "Allow",
			Principal = {
				Service = "ec2.amazonaws.com"
			},
			Action = "sts:AssumeRole",
			}
		]
})			
}

resource "aws_iam_role_policy_attachment" "ec2_policy"{
	role = aws_iam_role.ec2-role.name
	policy_arn = var.iam_role_policy_arn
}
