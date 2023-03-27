pipeline {
    agent any
    stages{
        stage("Try"){
            steps{
                echo"Trying to build Jenkins pipeline"
            }
        }
        stage("Build image"){
            steps{
                sh"docker build -t fithub:latest ."
            }
        }
    }
}