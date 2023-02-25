provider "aws" {
    region = "${var.region}"
    access_key = var.aws_access_key
    secret_key = var.aws_secret_key
}

terraform {
  backend "s3" {
    bucket         = "my-bucket-for-layer-spoot-mood"
    key            = "terrastate/terraform.tfstate"
    region         = "us-east-1" 
    encrypt        = false 
  }
}
