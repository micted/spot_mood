provider "aws" {
    region = "${var.region}"
    access_key = var.TF_VAR_ACCESS_KEY
    secret_key = var.TF_VAR_SECRET_KEY
}

terraform {
  backend "s3" {
    bucket         = "my-bucket-for-layer-spoot-mood"
    key            = "terrastate/terraform.tfstate"
    region         = "us-east-1" 
    encrypt        = false 
  }
}
