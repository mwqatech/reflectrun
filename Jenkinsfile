pipeline {
  agent any    
  stages {
    stage('Man Matters Sanity') {
      steps {
         sh 'python3 reflect_run.py'
      }
    }
  }
  post {
        always {
          emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
                attachLog: true, recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                to: 'hitesh.burla@mosaicwellness.in','pranay@mosaicwellness.in','vitthal.daund@mosaicwellness.in','shouvik@mosaicwellness.in','minal.jain@mosaicwellness.in','arun.ramesh@mosaicwellness.in, abhay.kaintura@mosaicwellness.in, tejaswini.gowda@mosaicwellness.in',
                subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}"
            }
    }
}
