pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'digensclub/devops-lab-webapp'
        DOCKER_TAG = 'v${BUILD_NUMBER}'
    }

    stages {
        stage ('Checkout') {
            steps {
                echo 'Building commit: ${GIT_COMMIT}'
                sh 'hostname && whoami && pwd && ls -la'
            }
        }

        stage ('Security Scan') {
            steps {
                echo 'Running Trivy Security Scan...'
                sh 'trivy fs --scanners secret,misconfig --exit-code 0 .'
            }
        }

        stage ('Build Docker Image') {
            steps {
                echo 'Building image: ${DOCKER_IMAGE}:${DOCKER_TAG}'
                sh 'docker build --tag ${DOCKER_IMAGE}:${DOCKER_TAG} phase2-devsecops/docker/webapp/'
                sh 'docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest'
            }
        }

        stage ('Push to Docker Hub') {
            steps {
                withCredentials(
                    [
                        usernamePassword(
                            credentialsId: 'dockerhub-credentials',
                            usernameVariable: 'DOCKER_USER',
                            passwordVariable: 'DOCKER_PASS'
                        )
                    ]
                )
                {
                    sh 'echo $DOCKER_PASS | docker login --username $DOCKER_USER --password-stdin'
                    sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
                    sh 'docker push ${DOCKER_IMAGE}:latest'
                    sh 'docker logout'
                }
            }

        }
        stage ('Verify') {
            steps {
                echo 'Image Pushed successfully: ${DOCKER_IMAGE}:${DOCKER_TAG}'
                sh 'docker images | grep devops-lab-webapp'
            }

        }
    }
    post {
        success {
            echo 'Pipeline complete! Image available at: docker.io/${DOCKER_IMAGE}:${DOCKER_TAG}'
        }
        failure {
            echo 'Pipeline failed - check logs above'
            sh 'docker logout || true'
        }
    }
}

