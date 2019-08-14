pipeline {
	agent { label 'py-app' }
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