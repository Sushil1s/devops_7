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
                // Updated with your actual Docker Hub username
                sh 'docker build -t sushilchavan02/devops_7:latest .'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Starting Test Container and Running UI Tests...'
                sh '''
                    # Clean up old containers
                    docker rm -f devops7_test || true
                    
                    # Run the app temporarily for testing
                    docker run -d -p 5000:5000 --name devops7_test sushilchavan02/devops_7:latest
                    
                    # Wait for Flask to boot
                    sleep 5
                    
                    # Setup Virtual Environment and install Selenium
                    python3 -m venv test_env
                    . test_env/bin/activate
                    pip install selenium
                    
                    # Run the tests
                    touch tests/__init__.py
                    python3 -m unittest discover tests
                '''
            }
            post {
                always {
                    // Destroy the temporary container whether tests pass or fail
                    echo 'Tearing down test container...'
                    sh 'docker rm -f devops7_test || true'
                }
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
