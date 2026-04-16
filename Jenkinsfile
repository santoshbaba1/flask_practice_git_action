pipeline {
    agent any

    environment {
        VENV = "venv"
        PORT = "5000"
        APP_NAME = "flask-app"
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/santoshbaba1/flask_Practice_Copy.git'
            }
        }

        stage('Build & Install Dependencies') {
            steps {
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt

                # Production server
                pip install gunicorn
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . $VENV/bin/activate
                pytest --maxfail=1 --disable-warnings
                '''
            }
        }

        stage('Stop Previous App') {
            steps {
                sh '''
                pkill -f "gunicorn" || true
                pkill -f "app.py" || true
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                . $VENV/bin/activate

                nohup gunicorn -b 0.0.0.0:$PORT app:app > app.log 2>&1 &
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                sleep 5
                curl -f http://localhost:$PORT || exit 1
                '''
            }
        }
    }

    post {
        success {
            mail to: 'santoshbaba1@rediffmail.com',
                 subject: "SUCCESS: Build #${BUILD_NUMBER}",
                 body: "Flask app deployed successfully on port ${PORT}"
        }
        failure {
            mail to: 'santoshbaba1@rediffmail.com',
                 subject: "FAILED: Build #${BUILD_NUMBER}",
                 body: "Build failed. Check Jenkins console output."
        }
    }
}
