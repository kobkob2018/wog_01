pipeline {
    agent any

    environment{
        IMAGE_VERSION = '1.9'
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
                    bat "docker tag ${DOCKER_USERNAME}/wog_world:${IMAGE_VERSION} kobkobdock/wog_world:latest"
                    bat "docker push ${DOCKER_USERNAME}/kobkobdock/wog_world:${IMAGE_VERSION}"
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
