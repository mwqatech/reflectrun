pipeline {
  agent any    
  stages {
    stage('Man Matters Sanity') {
      steps {
         sh 'python3 reflect_run_mm.py'
         env.mamatters_stage = env.STAGE_NAME
      }
    }
  }
  post {
        always {
          emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} Stage ${env.mamatters_stage} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
                attachLog: true, recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                to: 'arun.ramesh@mosaicwellness.in, abhay.kaintura@mosaicwellness.in, tejaswini.gowda@mosaicwellness.in',
                subject: "Jenkins Build ${currentBuild.currentResult}: Stage ${env.mamatters_stage}"
            }
    }
}
