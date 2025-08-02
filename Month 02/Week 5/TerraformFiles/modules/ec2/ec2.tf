
resource "aws_instance" "my_server" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = var.key
  vpc_security_group_ids = [aws_security_group.ssh_access.id]

  tags = {
    Name = "Terraform-practise-ec2"
  }
}

