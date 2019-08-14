pipeline {
	agent { label 'py-app' }
	triggers {
		pollSCM('* * * * *')
	}
	stages {
		stage('Compile') {
			steps {
				sh "python3 calculator.py 2 2"
			}
		}
		stage('Run unit test') {
			steps {
				sh "python3 test_calculator.py"
			}
		}
	}
}
