pipeline {
    agent any

    environment{
        IMAGE_VERSION = '2.3'
        IMAGE_NAME = 'wog_world'
        DOCKER_USERNAME = "${env.DOCKER_USERNAME ?: ''}"
        DOCKER_IMAGE_PREFIX = "${env.DOCKER_USERNAME ? env.DOCKER_USERNAME +'/': 'null'}"
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
                script {
                    if (DOCKER_USERNAME?.trim()) {
                        echo "Pushing latest version to docker hub"
                        bat "docker tag ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_VERSION} ${DOCKER_USERNAME}/${IMAGE_NAME}:latest"
                        bat "docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_VERSION}"
                    }
                    else{
                        echo "DOCKER_USERNAME is not set, skipping Docker push."
                    }
                }
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
