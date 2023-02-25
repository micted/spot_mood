pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
    }

    stages {
        stage('Terraform init') {
            steps {
                sh 'terraform init -backend-config="bucket=my-bucket-for-layer-spoot-mood" -backend-config="key=terrastate/terraform.tfstate"'
            }
        }

        
        stage('Terraform apply') {
            when {
                branch 'master'
            }
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'my-aws-creds',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    dir('/terraform/') {
                    sh 'terraform apply -auto-approve'
                    }
                }
            }
        }

        stage('Deploy to Lambda') {
            when {
                branch 'master'
            }
            steps {
                sh 'cd lambda && zip -r function.zip ./*'
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'my-aws-creds',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    sh 'aws lambda update-function-code --function-name my-lambda-function --zip-file fileb://lambda/function.zip'
                }
            }
        }
    }
}
