resource "aws_dynamodb_table" "token_store" {
  name         = "token_store"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "access_token"
  range_key    = "timestamp"

  attribute {
    name = "access_token"
    type = "S"
  }

  attribute {
    name = "timestamp"
    type = "N"
  }

  ttl {
    attribute_name = "expiration_time"
    enabled        = true
  }

  tags = {
    Name = "token_store"
  }
}
