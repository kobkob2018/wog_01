pipeline {
    agent any

    stages {
        stage('BUILD') {
            steps {
                bat 'docker build -t world-wog:1.1 .'    
            }
        }
        stage('RUN') {
            steps {
                bat 'docker run -d --rm -p 8777:5000 --name wog_flask  -v ./work/school/dockersftuff/scoremount.txt:/app/datafiles/score.txt my-wog:v1.1'
            }
        }
        stage('E2E') {
            steps {
                    bat "python app/tests/e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                    bat "docker stop wog_flask"
            }
        }
    }
}
