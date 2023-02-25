pipeline {
    agent any

    stages {
        withCredentials([
            [
                credentialsId: 'my-aws-creds',
                accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
            ]
        ])
        
        stage('Terraform init') {
            steps {
                sh 'terraform init -backend-config="bucket=my-bucket-for-layer-spoot-mood" -backend-config="key=terrastate/terraform.tfstate"'
            }
        }
        
        stage('Terraform apply') {
            when {
                branch 'main'
            }
            steps {
                sh 'terraform apply -auto-approve'
            }
        }
        
        stage('Deploy to Lambda') {
            when {
                branch 'main'
            }
            steps {
                withEnv(['AWS_DEFAULT_REGION=us-east-1']) {
                    sh 'cd lambda && zip -r function.zip ./*'
                    sh 'aws lambda update-function-code --function-name my-lambda-function --zip-file fileb://lambda/function.zip'
                }
            }
        }
    }
}
