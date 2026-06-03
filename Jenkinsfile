pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Code checked out by Jenkins automatically ...'
                sh 'pwd'
                sh 'ls -la'
            }
        }
        stage('System Info') {
            steps {
                echo 'Gathering System Information...'
                sh 'whoami'
                sh 'git --version'
                sh 'docker --version'
                sh 'uname -a'
                sh 'df -h'
                sh 'free -m'
            }
        }
        stage('Verify Structure') {
            steps {
                echo 'Checking devops-lab structure...'
                sh 'find . -type f | sort'
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed — check the logs above'
        }
    }
}