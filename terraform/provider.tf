provider "aws" {
    region = "${var.region}"
    
}

terraform {
  backend "s3" {
    bucket         = "my-bucket-for-layer-spoot-mood"
    key            = "terrastate/terraform.tfstate"
    region         = "us-east-1" 
    encrypt        = false 
  }
}
