pipeline {
	agent { label 'py-app' }
	stages {
		stage('Compile') {
			sh "python3 calculator.py 2 2"
		}
		stage('Run unit test') {
			sh "python3 test_calculator.py"
		}
	}
}