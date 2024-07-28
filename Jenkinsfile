pipeline {
    agent any

    stages {
        stage('DOCKER') {
            steps {
                bat 'docker-compose up --build -d'    
            }
        }
        stage('E2E') {
            steps {
                    bat "python app/tests/e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                    echo "This will be the finalize stage, only if l goes well"
            }
        }
    }
    post {
        always {
            stage('Cleanup') {
                echo 'Cleaning up...'
                // This stage will run regardless of the pipeline result
                bat "docker-compose down -v --rmi all"
            }
        }
    }
}
