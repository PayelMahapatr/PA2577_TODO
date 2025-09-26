# PA2577_TODO
Masters in Software Engineering - Blekinge Institute of Technology
This is a to-do application created for submission of assignment PA2577: Cloud Computing and Big Data.
It includes atleast 2 microservices called accounts and todo having their own postgres database with REST apis integrated.

The technology stack that has been used are as follows:
• The frontend is developed using HTML and Javascript.
• The backend is written in Python programming language
using Python Django Framework.
• Django Rest Framework(DRF) with Jason Web To-
ken(JWT) authentication has been used to develop REST-
ful endpoints in the microservices.
• Postgres databases have been used to connect to the
microservices for data storage.
• Docker and Docker Desktop were used to containerize
the microservices by creating docker images which were
pushed to Docker Hub. Two images were created which
are available publicly to be pulled.
– payelmahapatra/todo:latest
– payelmahapatra/accounts:latest
• docker-compose was used for local testing of the appli-
cation.
• minikube and kubectl was used to deploy the services in
kubernetes cluster.
