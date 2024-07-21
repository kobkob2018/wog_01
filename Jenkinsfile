pipeline {
    agent any

    stages {
        stage('BUILD') {
            steps {
                script {
                    bat 'docker build -t my-jtest:1.3 .'
                }
            }
        }
    }
}
