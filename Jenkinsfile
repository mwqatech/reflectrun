pipeline {
  agent any    
  stages {
    stage('QA Sanity Test') {
      steps {
         sh 'python3 reflect_run.py'
      }
    }
  }
  post {
        always {
          emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
                subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}"
            }
    }
}
