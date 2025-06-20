pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/malghalara/signup.git'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                dir('test-pipeline') {
                    script {
                        sh 'docker build -t signup-tests .'
                        sh 'docker run --rm signup-tests'
                    }
                }
            }
        }
    }

    post {
        always {
            echo '📦 Selenium test pipeline complete.'
        }
    }
}
