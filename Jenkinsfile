pipeline {
    agent any

    environment {
        VENV = "venv"
        PORT = "5000"
    }

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/santoshbaba1/flask_Practice_Copy.git'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    $VENV/bin/pip install --upgrade pip
                    $VENV/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    pkill -f app.py || true
                    nohup venv/bin/python3 app.py > app.log 2>&1 &
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    sleep 5
                    curl -f http://192.168.1.9:$PORT || exit 1
                '''
            }
        }
    }

    post {
        success {
            emailext (
                to: 'santoshpvt08@gmail.com',
                subject: "SUCCESS: Build ${BUILD_NUMBER}",
                body: "Build succeeded! Check: ${BUILD_URL}",
                smtpHost: 'smtp.gmail.com',
                smtpPort: '587'
            )
        }
        failure {
            emailext (
                to: 'santoshpvt08@gmail.com',
                subject: "FAILED: Build ${BUILD_NUMBER}",
                body: "Build failed! Check: ${BUILD_URL}",
                smtpHost: 'smtp.gmail.com',
                smtpPort: '587'
            )
        }
    }
}
