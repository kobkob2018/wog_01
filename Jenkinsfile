pipeline {
    agent any

    stages {
        stage('BUILD') {
            steps {
                script {
                    sh 'docker build -t my-jtest:1.3 .'
                }
            }
        }
    }
}
