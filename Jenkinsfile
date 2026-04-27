pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building Docker Image...'
                // Replace 'yourusername' with your actual Docker Hub username
                sh 'docker build -t yourusername/devops_7:latest .'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Selenium UI Tests...'
                // This command runs your python test script
                sh 'python3 -m unittest tests/test_ui.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to Kubernetes...'
                sh 'kubectl apply -f k8s.yaml'
            }
        }
    }
}
