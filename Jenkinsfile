pipeline {
    agent any

    environment {
        APP_DIR = '/opt/learnhub'
        APP_PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v
                '''
            }
        }

                stage('Deploy') {
            steps {
                sh '''
                    set -e

                    echo "Deploying LearnHub..."

                    mkdir -p "$APP_DIR"

                    rm -rf "$APP_DIR/app"
                    cp -r app "$APP_DIR/"
                    cp requirements.txt "$APP_DIR/"

                    python3 -m venv "$APP_DIR/venv"
                    "$APP_DIR/venv/bin/pip" install -r "$APP_DIR/requirements.txt"

                    sudo systemctl daemon-reload
                    sudo systemctl enable learnhub
                    sudo systemctl restart learnhub

                    for i in $(seq 1 10); do
                        if curl -fsS http://127.0.0.1:$APP_PORT/health; then
                            echo "LearnHub deployment successful."
                            exit 0
                        fi
                        sleep 2
                    done

                    echo "Application health check failed"
                    exit 1
                '''
            }
        }
[Unit]
Description=LearnHub Flask Application
After=network.target

[Service]
Type=simple
WorkingDirectory=$APP_DIR
ExecStart=$APP_DIR/venv/bin/gunicorn --bind 0.0.0.0:$APP_PORT app:app
Restart=on-failure
User=ubuntu

[Install]
WantedBy=multi-user.target
SERVICE

                    sudo systemctl daemon-reload
                    sudo systemctl enable learnhub
                    sudo systemctl restart learnhub

                    for i in $(seq 1 10); do
                        if curl -fsS http://127.0.0.1:$APP_PORT/health; then
                            exit 0
                        fi
                        sleep 2
                    done

                    echo "Application health check failed"
                    exit 1
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully.'
        }
        failure {
            echo 'CI/CD pipeline failed. Check the stage logs.'
        }
    }
}
