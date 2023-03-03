# aws_api_gateway_rest_api.StartExecutionAPI:
resource "aws_api_gateway_rest_api" "StartExecutionAPI" {
    api_key_source               = "HEADER"
    arn                          = "arn:aws:apigateway:us-east-1::/restapis/9bneg9jui6"
    binary_media_types           = []
    created_date                 = "2023-02-20T07:23:13Z"
    description                  = "invoke step function"
    disable_execute_api_endpoint = false
    execution_arn                = "arn:aws:execute-api:us-east-1:858879043794:9bneg9jui6"
    id                           = "9bneg9jui6"
    minimum_compression_size     = -1
    name                         = "StartExecutionAPI"
    put_rest_api_mode            = "overwrite"
    root_resource_id             = "kdlvs810xi"
    tags                         = {}
    tags_all                     = {}

    endpoint_configuration {
        types            = [
            "REGIONAL",
        ]
        vpc_endpoint_ids = []
    }
}



# aws_api_gateway_rest_api.step-login:
resource "aws_api_gateway_rest_api" "step-login" {
    api_key_source               = "HEADER"
    arn                          = "arn:aws:apigateway:us-east-1::/restapis/q2f76phkj4"
    binary_media_types           = []
    created_date                 = "2023-02-19T18:57:18Z"
    disable_execute_api_endpoint = false
    execution_arn                = "arn:aws:execute-api:us-east-1:858879043794:q2f76phkj4"
    id                           = "q2f76phkj4"
    minimum_compression_size     = -1
    name                         = "step-login"
    put_rest_api_mode            = "overwrite"
    root_resource_id             = "kbmxmqylbg"
    tags                         = {}
    tags_all                     = {}

    endpoint_configuration {
        types            = [
            "REGIONAL",
        ]
        vpc_endpoint_ids = []
    }
}