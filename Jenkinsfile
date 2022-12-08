pipeline {
  agent any    
  stages {
    stage('QA Sanity Test') {
      steps {
         sh 'python3 reflect_run.py'
      }
    }
  }
}
