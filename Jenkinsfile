pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
    }

    stages {
        stage('Terraform init') {
            steps {
                dir('terraform'){
                    withCredentials([
                        [
                            $class: 'AmazonWebServicesCredentialsBinding',
                            credentialsId: 'my-aws-creds',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                        ]
                    ]) {
                        sh 'terraform init -backend-config="bucket=my-bucket-for-layer-spoot-mood" -backend-config="key=terrastate/terraform.tfstate"'
                    }
                }
            }
        }

        
        stage('Terraform apply') {
            
            steps {
                dir('terraform') {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'my-aws-creds',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    
                    sh "terraform apply -auto-approve -var 'aws_access_key=${AWS_ACCESS_KEY_ID}' -var 'aws_secret_key=${AWS_SECRET_ACCESS_KEY}'"
                    
                }
                }
            }
        }

        stage('Deploy to Lambda') {
            
            steps {
                sh 'cd lambda && zip -r function.zip ./* '
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'my-aws-creds',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                ]]) {
                    sh 'aws lambda update-function-code --function-name mood_analysis --zip-file fileb://lambda/function.zip'
                }
            }
        }
    }
}
