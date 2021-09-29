pipeline {
   agent any
   stages {
       stage('docker-compose') {
           steps {
              sh "docker-compose build"
              sh "docker-compose up -d"
           }
       }
   }
   post {
      success {
         slackSend color: '#00FF00', message: 'python-flask-docker-job Success'
      }
	  failure {
		 slackSend color: '#FF000', message: 'python-flask-docker-job Failed'
	  }
   }   
}
