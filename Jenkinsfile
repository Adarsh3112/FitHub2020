pipeline {
    agent any
    environment {
        appRegistry = 'nikhil2611/fithub' 
    }
    stages{
        stage("Try"){
            steps{
                echo"Trying to build Jenkins pipeline"
            }
        }
        stage("Build image"){
            script{
                dockerImage = docker.build( appRegistry + ":$BUILD_NUMBER", "./Docker-files/app/multistage/" ) 
            }
        }
    }
}