pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Code checked out by Jenkins automatically ...'
                sh 'pwd && ls -la'
            }
        }
        stage('System Info') {
            steps {
                echo 'Gathering System Information...'
                sh 'whoami && id && git --version && docker --version && uname -a && df -h && free -m'
            }
        }
        stage('Security Scan') {
            steps{
                echo 'Running Trivy security scan...'
                sh 'trivy fs --scanners secret,misconfig --exit-code 0 .'
            }
        }
        stage('Verify Structure') {
            steps {
                echo 'Checking devops-lab structure...'
                sh 'find . -not -path "./.git/*" -type f | sort'
            }
        }
    }
    post {
        success {
            echo 'Pipeline passed all the stages including security scan!'
        }
        failure {
            echo 'Pipeline failed — check the logs above'
        }
    }
}