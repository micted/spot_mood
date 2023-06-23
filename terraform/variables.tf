variable "TF_VAR_SPOTIFY_USERNAME" {
  type = string
  default = ""
}

variable "TF_VAR_SPOTIFY_REDIRECT_URI" {
  type = string
  default = "https://4mgy710c5k.execute-api.us-east-1.amazonaws.com/prod/callback/"
}

variable "TF_VAR_SPOTIPY_CLIENT_ID" {
    type = string
    default = ""
}

variable "TF_VAR_SPOTIPY_CLIENT_SECRET" {
    type = string
    default = ""
}

variable "TF_VAR_OPENAI_KEY" { 
    type = string
    default = ""
}

variable "TF_VAR_MUSIXMATCH_API_KEY" {

    type = string
    default = ""
  
}


variable "TF_VAR_FLASK_SECRET_KEY" {
    type  = string
    default = "development"
}

variable "aws_access_key" {}

variable "aws_secret_key" {}

variable "region" {
  default = "us-east-1"
}

variable "account_id" {
  default = ""
}



