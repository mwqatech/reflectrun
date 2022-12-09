pipeline {
  agent any
  stages {
    stage('Man Matters Sanity') {
      steps {
         sh 'python3 reflect_run_mm.py'
      }
    }
  }
  post {
        always {
          emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
                attachLog: true, recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                to: 'vitthal.daund@mosaicwellness.in, pranay@mosaicwellness.in, minal.jain@mosaicwellness.in, shouvik@mosaicwellness.in, hitesh.burla@mosaicwellness.in, arun.ramesh@mosaicwellness.in, abhay.kaintura@mosaicwellness.in, tejaswini.gowda@mosaicwellness.in',
                subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}"
            }
    }
}
