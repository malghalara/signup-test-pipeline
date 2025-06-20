pipeline {
    agent any

    stages {
        stage('Clone App Repo') {
            steps {
                git url: 'https://github.com/malghalara/signup.git', changelog: false, poll: false
            }
        }

        stage('Build and Run Selenium Tests') {
            steps {
                script {
                    // Move into the test repo directory if needed
                    sh 'docker build -t signup-tests https://github.com/malghalara/signup-test-pipeline.git#master'
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
