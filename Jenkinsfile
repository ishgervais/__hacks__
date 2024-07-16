pipeline {
    agent any

    environment {
        // node
        NVM_DIR = "${env.HOME}/.nvm"
        PATH = "${env.PATH}:${env.NVM_DIR}/versions/node/v20.15.1/bin"

        SSH_KEY = credentials('') // Use credential ID instead of full key
        DB_HOST = 'localhost:5432'
        DB_USER = ''
        DB_PASSWORD = ''
        DB_NAME = ''
        DATABASE_URL='postgresql://<user>:<password>@localhost:5432/<db_name>?schema=public'
    }

    stages {

        stage('Cleanup') {
            steps {
                cleanWs()
            }
        }
        stage('Clone Repository') {
            steps {
                script {
                    node {
                        git branch: 'main', credentialsId: '', url: 'git@github.com:username/repo'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    node {
                        sh 'npm i -g pnpm && npm i -g pm2 &&  pnpm install --no-frozen-lockfile'
                    }
                }
            }
        }

          stage('Generate Prisma Client') {
            steps {
                script {
                    node {
                        sh 'npx prisma generate'
                    }
                }
            }
        }

        stage('Run Migrations') {
            steps {
                script {
                    node {
                        sh 'npx prisma migrate dev'
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    node {
                        sh 'pnpm run build'
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                if (getContext(hudson.FilePath)) {
                    deleteDir()
                }
            }
        }
    }
}

