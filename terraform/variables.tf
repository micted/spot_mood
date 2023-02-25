variable "TF_VAR_SPOTIFY_USERNAME" {
  type = string
  default = "31lsfo3boeszgingsyq4jvcr3pyy"
}

variable "TF_VAR_SPOTIFY_REDIRECT_URI" {
  type = string
  default = "https://4mgy710c5k.execute-api.us-east-1.amazonaws.com/prod/callback/"
}

variable "TF_VAR_SPOTIPY_CLIENT_ID" {
    type = string
    default = "3cda7feffdfb4d0c95e0fa480314fde2"
}

variable "TF_VAR_SPOTIPY_CLIENT_SECRET" {
    type = string
    default = "4d072df39ed84029be1ce0415caa3532"
}

variable "TF_VAR_OPENAI_KEY" { 
    type = string
    default = "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"
}

variable "TF_VAR_MUSIXMATCH_API_KEY" {

    type = string
    default = "e19acacfc7e6e698dec58594a7f59262"
  
}


variable "TF_VAR_FLASK_SECRET_KEY" {
    type  = string
    default = "development"
}

variable "TF_VAR_ACCESS_KEY" {
  type = string
     
}

variable "TF_VAR_SECRET_KEY" {
  type = string
  
}

variable "region" {
  default = "us-east-1"
}

variable "account_id" {
  default = "858879043794"
}



