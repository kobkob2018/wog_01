pipeline {
    agent any

    environment{
        IMAGE_VERSION = '1.5'
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
                    echo "This will be the finalize stage, only if l goes well"
                    bat "docker tag kobkobdock/wog_world:${IMAGE_VERSION} kobkobdock/wog_world:latest"
                    bat "docker push kobkobdock/wog_world:${IMAGE_VERSION}"
            }
        }
    }
    post {

        always {
                echo 'Cleaning up...'
                // This stage will run regardless of the pipeline result
                //bat "docker-compose down -v --rmi all"
                bat "docker-compose down"
        }
    }
}
