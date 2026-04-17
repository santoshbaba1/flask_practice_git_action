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
                # Create virtual environment
                python3 -m venv $VENV
                . venv/bin/activate
                # Install dependencies using full path (IMPORTANT FIX)
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
    }
}
