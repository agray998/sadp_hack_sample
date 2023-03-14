pipeline {
    agent any
    environment {
        DOCKER_CREDS = credentials('DOCKER_CREDS')
        MYSQL_ROOT_PASSWORD = credentials('MYSQL_ROOT_PASSWORD')
    }
    stages {
        stage('Build and push images') {
            steps {
                sh "cp models.py drivers/application/models.py"
                sh "cp models.py packages/application/models.py"
                sh "docker login -u ${DOCKER_CREDS_USR} -p ${DOCKER_CREDS_PSW}"
                sh "docker-compose build --parallel"
                sh "docker-compose push"
                sh "docker image prune"
            }
        }
    }

}