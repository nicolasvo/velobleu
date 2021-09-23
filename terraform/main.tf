provider "aws" {
  region = "eu-central-1"

  # Make it faster by skipping something
  skip_get_ec2_platforms      = true
  skip_metadata_api_check     = true
  skip_region_validation      = true
  skip_credentials_validation = true
  skip_requesting_account_id  = true
}

module "lambda_function_from_container_image" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "velobleu-lambda-from-container-image"
  description   = "My awesome lambda function from container image"

  create_package = false

  ##################
  # Container Image
  ##################
  image_uri    = module.docker_image.image_uri
  package_type = "Image"
  timeout      = 20
}

module "docker_image" {
  source = "terraform-aws-modules/lambda/aws//modules/docker-build"

  create_ecr_repo = true
  ecr_repo        = "velobleu"
  image_tag       = "2.1"
  source_path     = ".."
}
