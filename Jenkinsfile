pipeline {
    agent any

    environment {
        // node
        NVM_DIR = "${env.HOME}/.nvm"
        PATH = "${env.PATH}:${env.NVM_DIR}/versions/node/v20.15.1/bin"

        SSH_KEY = credentials('ba741c35-78de-4755-a515-fe3db6a01987') // Use credential ID instead of full key
        DB_HOST = 'localhost:5432'
        DB_USER = 'root'
        DB_PASSWORD = '_Root_!123^StrongP$$wd'
        DB_NAME = 'thefuteur_db'
        DATABASE_URL='postgresql://root:_Root_!123^StrongP$$wd@localhost:5432/thefuteur_db?schema=public'
        
        // Equifax environment variables
        EFX_CHANNEL_ID_NUMBER = 3
        EFX_CHANNEL_NAME = 'ISTS'
        EFX_CUSTOMER_NUMBER = '999ZB18001'
        EFX_PERMISSIBLE_PURPOSE = 24
        EFX_PROD_COMMERCIAL_CREDIT_REPORT_URL = 'https://commercial-ppe.equifax.com/sbeppe/jsonservices/DecisionService/OrderCreditReport'
        EFX_PRODUCT_CODE_1_CODE = '0036'
        EFX_PRODUCT_CODE_1_NAME = 'RPT'
        EFX_PRODUCT_CODE_1_VALUE = 'RPT0036'
        EFX_PRODUCT_CODE_2_CODE = '0126'
        EFX_PRODUCT_CODE_2_NAME = 'SCR'
        EFX_PRODUCT_CODE_2_VALUE = 'SCR0126'
        EFX_SECURITY_CODE = 'X38'
        EFX_SERVICE_CODE = 'SB1'
        EFX_TRAN_ID = 'XSOF'
        EFX_UAT_COMMERCIAL_CREDIT_REPORT_URL = 'https://commercial-ppe-uat.equifax.com/sbeppe/jsonservices/DecisionService/OrderCreditReport'
        EFX_VERSION = '5.0'
        JWT_EXPIRE_IN = '7d'
        JWT_SECRET = '443934_jlkjdsfkladsjf209439434394394kafkadsjklfadsJASKLJKLJF'
        CREDIT_SAFE_UAT_CREDIT_REPORT_URL = 'https://connect.sandbox.creditsafe.com/v1'
        CREDIT_SAFE_PROD_CREDIT_REPORT_URL = 'https://connect.creditsafe.com/v1'
        CREDIT_SAFE_AUTH_TOKEN = ''
        // Recurly
        RECURLY_ACCOUNT_URL="https://v3.recurly.com/accounts"
        RECURLY_SUBSCRIPTIONS_URL="https://v3.recurly.com/subscriptions"
        RECURLY_AUTHORIZATION="OWJiZmRlZjhhOTYwNGE5OGFiNmE4YWZhYjZmZjU2MDY6"
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
                        git branch: 'main', credentialsId: 'ba741c35-78de-4755-a515-fe3db6a01987', url: 'git@github.com:TheFuteur/futeur-api.git'
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

