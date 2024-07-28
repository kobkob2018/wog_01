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
                    bat "docker-compose down -v --rmi all"
            }
        }
    }
}
