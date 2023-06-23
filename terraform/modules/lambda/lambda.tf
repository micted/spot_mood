# aws_lambda_function.login:
resource "aws_lambda_function" "login" {
    architectures                  = [
        "x86_64",
    ]
    arn                            = "arn:aws:lambda:us-east-1:858879043794:function:login"
    function_name                  = "login"
    handler                        = "login.lambda_handler"
    id                             = "login"
    invoke_arn                     = "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:858879043794:function:login/invocations"
    last_modified                  = "2023-02-21T07:50:18.000+0000"
    layers                         = [
        "arn:aws:lambda:us-east-1:858879043794:layer:mypackage_layer:1",
    ]
    memory_size                    = 128
    package_type                   = "Zip"
    qualified_arn                  = "arn:aws:lambda:us-east-1:858879043794:function:login:$LATEST"
    qualified_invoke_arn           = "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:858879043794:function:login:$LATEST/invocations"
    reserved_concurrent_executions = -1
    role                           = "arn:aws:iam::858879043794:role/lambda"
    runtime                        = "python3.9"
    source_code_hash               = "ULi4TwRAjOh9nh5YGWEGj99qmd27FJCGp7CBIxLjBjA="
    source_code_size               = 10612
    tags                           = {}
    tags_all                       = {}
    timeout                        = 60
    version                        = "$LATEST"

    environment {
        variables = {
            "DYNAMODB_TABLE_NAME"   = "token_store"
            "FLASK_SECRET_KEY"      = "development"
            "SPOTIFY_REDIRECT_URI"  = "https://q2f76phkj4.execute-api.us-east-1.amazonaws.com/prod/redirect"
            "SPOTIFY_USERNAME"      = ""
            "SPOTIPY_CLIENT_ID"     = ""
            "SPOTIPY_CLIENT_SECRET" = ""
        }
    }

    ephemeral_storage {
        size = 512
    }

    timeouts {}

    tracing_config {
        mode = "PassThrough"
    }
}




# aws_lambda_function.callback:
resource "aws_lambda_function" "callback" {
    architectures                  = [
        "x86_64",
    ]
    arn                            = "arn:aws:lambda:us-east-1:858879043794:function:callback"
    function_name                  = "callback"
    handler                        = "callback.lambda_handler"
    id                             = "callback"
    invoke_arn                     = "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:858879043794:function:callback/invocations"
    last_modified                  = "2023-02-20T13:07:26.000+0000"
    layers                         = [
        "arn:aws:lambda:us-east-1:858879043794:layer:mypackage_layer:1",
    ]
    memory_size                    = 128
    package_type                   = "Zip"
    qualified_arn                  = "arn:aws:lambda:us-east-1:858879043794:function:callback:$LATEST"
    qualified_invoke_arn           = "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:858879043794:function:callback:$LATEST/invocations"
    reserved_concurrent_executions = -1
    role                           = "arn:aws:iam::858879043794:role/lambda"
    runtime                        = "python3.9"
    source_code_hash               = "1zaM1lTXSmerzke2RAhc9Pmg+Y1pgqUHS7qiKQ6vihA="
    source_code_size               = 10871
    tags                           = {}
    tags_all                       = {}
    timeout                        = 300
    version                        = "$LATEST"

    environment {
        variables = {
            "DYNAMODB_TABLE_NAME"   = "token_store"
            "FLASK_SECRET_KEY"      = "development"
            "SPOTIFY_REDIRECT_URI"  = "https://q2f76phkj4.execute-api.us-east-1.amazonaws.com/prod/redirect"
            "SPOTIFY_USERNAME"      = "31lsfo3boeszgingsyq4jvcr3pyy"
            "SPOTIPY_CLIENT_ID"     = "3cda7feffdfb4d0c95e0fa480314fde2"
            "SPOTIPY_CLIENT_SECRET" = "4d072df39ed84029be1ce0415caa3532"
        }
    }

    ephemeral_storage {
        size = 512
    }

    timeouts {}

    tracing_config {
        mode = "PassThrough"
    }
}




# aws_lambda_function.recently_played:
resource "aws_lambda_function" "recently_played" {
    architectures                  = [
        "x86_64",
    ]
    arn                            = "arn:aws:lambda:us-east-1:858879043794:function:recently_played"
    function_name                  = "recently_played"
    handler                        = "recently_played.lambda_handler"
    id                             = "recently_played"
    invoke_arn                     = "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:858879043794:function:recently_played/invocations"
    last_modified                  = "2023-02-20T11:57:41.000+0000"
    layers                         = [
        "arn:aws:lambda:us-east-1:858879043794:layer:mypackage_layer:1",
    ]
    memory_size                    = 128
    package_type                   = "Zip"
    qualified_arn                  = "arn:aws:lambda:us-east-1:858879043794:function:recently_played:$LATEST"
    qualified_invoke_arn           = "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:858879043794:function:recently_played:$LATEST/invocations"
    reserved_concurrent_executions = -1
    role                           = "arn:aws:iam::858879043794:role/lambda"
    runtime                        = "python3.9"
    source_code_hash               = "15hM5o0vri0FYtxO1bPjKjq0xLEGgNp6i5VnPRBI+cA="
    source_code_size               = 11400
    tags                           = {}
    tags_all                       = {}
    timeout                        = 300
    version                        = "$LATEST"

    environment {
        variables = {
            "DYNAMODB_TABLE_NAME"   = "token_store"
            "FLASK_SECRET_KEY"      = "development"
            "SPOTIFY_REDIRECT_URI"  = "https://q2f76phkj4.execute-api.us-east-1.amazonaws.com/prod/redirect"
            "SPOTIFY_USERNAME"      = "31lsfo3boeszgingsyq4jvcr3pyy"
            "SPOTIPY_CLIENT_ID"     = "3cda7feffdfb4d0c95e0fa480314fde2"
            "SPOTIPY_CLIENT_SECRET" = "4d072df39ed84029be1ce0415caa3532"
        }
    }

    ephemeral_storage {
        size = 512
    }

    timeouts {}

    tracing_config {
        mode = "PassThrough"
    }
}
