pipeline {
    agent any

    stages {
        stage('Clone Test Repo') {
            steps {
                git 'https://github.com/malghalara/signup-test-pipeline.git'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    // Assuming Dockerfile is in root of cloned repo
                    sh 'docker build -t signup-tests .'
                    sh 'docker run --rm signup-tests'
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
