pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                script {
                    def currentDir = pwd()
                    echo "Current working directory: ${currentDir}"
                }
            }
        }
    }
}
