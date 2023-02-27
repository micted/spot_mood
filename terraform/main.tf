resource "aws_lambda_layer_version" "mypackage_layer_moodanalysis" {
    filename   = "../mypackage.zip"
    layer_name = "mypackage_layer_moodanalysis"
    compatible_runtimes =["python3.9"]
}

resource "aws_lambda_function" "mood_analysis" {
  filename      = "../function.zip"
  function_name = "mood_analysis"
  role          = "arn:aws:iam::858879043794:role/lambda"
  handler       = "main.lambda_handler"
  runtime       = "python3.9"

  layers = [aws_lambda_layer_version.mypackage_layer_moodanalysis.arn]
  
  environment {
    variables = {
      SPOTIFY_USERNAME      = var.TF_VAR_SPOTIFY_USERNAME
      SPOTIPY_CLIENT_ID     = var.TF_VAR_SPOTIPY_CLIENT_ID
      SPOTIPY_CLIENT_SECRET = var.TF_VAR_SPOTIPY_CLIENT_SECRET
      SPOTIFY_REDIRECT_URI  = var.TF_VAR_SPOTIFY_REDIRECT_URI
      FLASK_SECRET_KEY      = var.TF_VAR_FLASK_SECRET_KEY
      OPENAI_API_KEY        = var.TF_VAR_OPENAI_KEY
    }
  }
}
