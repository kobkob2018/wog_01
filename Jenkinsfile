pipeline {
    agent any

    stages {
        stage('BUILD') {
            steps {
                sh 'docker build -t my-jtest:1.42 .'    
            }
        }
        stage('RUN') {
            steps {
                sh 'winpty docker run -it my-jtest:1.42'
            }
        }
    }
}
