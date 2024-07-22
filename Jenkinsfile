pipeline {
    agent any

    stages {
        stage('BUILD') {
            steps {
                bat 'docker build -t my-jtest:1.4 .'    
            }
        }
        stage('RUN') {
            steps {
                bat 'winpty docker run -it my-jtest:1.4'
            }
        }
    }
}
