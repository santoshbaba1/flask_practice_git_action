pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/santoshbaba1/flask_Practice_Copy.git'
                    ]]
                ])
            }
        }

        stage('Build') {
            steps {
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install -r requirements.txt
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
                nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }
}
