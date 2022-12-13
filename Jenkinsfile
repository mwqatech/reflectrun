pipeline {
  agent any
  stages {
    stage('QA Sanity'){
     parallel{
        stage('Man Matters Sanity') {
          steps {
            sh 'python3 reflect_run_mm.py'
          }
        }
        stage('BE Bodywise Sanity') {
          steps {
            sh 'python3 reflect_run_bw.py'
          }
        }
    }
  }
  }   
  post {
        always {
          emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
                attachLog: true, recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                to: 'arun.ramesh@mosaicwellness.in, abhay.kaintura@mosaicwellness.in, tejaswini.gowda@mosaicwellness.in, basanagouda.b@mosaicwellness.in', 
                subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}"
          create_newjira_issue()
            }
    }  
}
void create_newjira_issue() {
    node {
      stage('JIRA') {
        def NewJiraIssue = [fields: [project: [key: 'MWQA'],
            summary: 'Build Failed : Summary.',
            description: 'Description of JIRA ticket ',
            issuetype: [id: '10108']]]

    response = jiraNewIssue issue: NewJiraIssue, site: 'https://mosaicwellness.atlassian.net/'

    echo response.successful.toString()
    echo response.data.toString()
    }
  }
}
