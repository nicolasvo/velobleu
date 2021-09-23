# velobleu

This project fetches the velobleu bike stations name, coordinates, number of available bikes (ab), number of available parking slots (ap). It is deployed using Terraform, AWS Lambda and AWS ECR.

## Steps

1. Export `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
2. `cd terraform`
3. `terraform init`
4. `terraform plan`
5. `terraform apply`

## TODO

- At the moment, AWS API Gateway trigger is manually added. It needs to be declared in Terraform.
