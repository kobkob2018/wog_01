pipeline {
    agent any

    environment{
        IMAGE_VERSION = '2.1'
        IMAGE_NAME = 'wog_world'
        DOCKER_USERNAME = "${env.DOCKER_USERNAME}"
    }
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
                    echo "Pushing latest version to docker hub"
                    bat "docker tag ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_VERSION} ${DOCKER_USERNAME}/${IMAGE_NAME}:latest"
                    bat "docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_VERSION}"
            }
        }
    }
    post {

        always {
                echo 'Cleaning up...'
                // This stage will run regardless of the pipeline result
                bat "docker-compose down -v --rmi all"
        }
    }
}
