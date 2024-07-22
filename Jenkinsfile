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
                bat 'docker run --rm -p 8777:5000 --name wog_flask  -v C:/Users/yacov/work/school/dockersftuff/scoremount.txt:/app/datafiles/score.txt -it my-jtest:1.4'
            }
        }
        stage('E2E') {
            steps {
                    bat "python e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                dir('World-Of-Games') {
                    bat "docker stop wog_flask"
                }
            }
        }
    }
}
