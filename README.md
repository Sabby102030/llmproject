LLM App


This repository contains the code for a Language Model (LLM) application deployed on Google Kubernetes Engine (GKE). The application leverages the HuggingFaceTB/SmolLM-360M model to provide advanced language processing capabilities through a Flask web interface.
## Features

- LLM Integration: Utilizes the HuggingFaceTB/SmolLM-360M model for language understanding and generation
- Flask Web App: A user-friendly web interface built with Flask to interact with the language model.
- Containerized Deployment: Dockerized application for consistent and reproducible deployments.
- Kubernetes Orchestration: Deployed on a GKE cluster, ensuring scalability and reliability.
- Secure API Access: Integrated with OpenAI's API for additional language model support.


## Architecture

- Docker: The application is containerized using Docker. The Docker image is tagged as chatapp:latest.
- Google Kubernetes Engine (GKE): Deployed on a GKE cluster with e2-medium instances to ensure efficient resource utilization.
- Kubernetes Configuration: Number of nodes 2 Includes all necessary Kubernetes manifests (Deployment, Service, Ingress) for deploying the application.
## Prerequisites

- Google Cloud Platform (GCP) Account: Set up a GCP account and create a Kubernetes cluster

- Docker: Install Docker to build and manage container images.

- Kubectl: Install kubectl to manage Kubernetes clusters.

- Minikube: Install Minikube for local Kubernetes cluster setup.

- Hugging face: Obtain an API key from Hugging face for additional language model capabilities.
## Setup Instructions

Deploying on Google Kubernetes Engine (GKE)

1. Clone the Repository:
```bash
git clone https://github.com/sabby102030/llm-app.git
cd llm-app
```
2. Build the Docker Image:
```bash
docker build -t chatapp:latest .
```

3. Push the Image to Google Container Registry:
```bash
docker tag chatapp:latest gcr.io/your-gcp-project-id/chatapp:latest
docker push gcr.io/your-gcp-project-id/chatapp:latest
```
4. Deploy to GKE:
- Deploy to GKE:
- Apply the Kubernetes manifests:
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
Deploying on Local Machine Using Minikube
1. Start Minikube
```bash
Minikube start
```
2. Clone the Repository:
```bash
git clone https://github.com/sabby102030/llm-app.git
cd llm-app
```
3. Build the Docker Image in Minikube:
```bash
eval $(minikube docker-env)
docker build -t chatapp:latest .
```
4. Deploy to Minikube:
- Ensure your Kubernetes manifests are configured for local deployment.
- Apply the Kubernetes manifests:
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

5.Access the Application:
- Get the Minikube IP and the service port:
```bash
minikube service chatapp-service --url
```
- Open the displayed URL in your web browser to access the application.

## Usage/Examples
I have already deployed to my GKE account from here you can acces:
- link: http://34.134.245.247:80
- You'll get the same url if you follow the same step
Usage
Once deployed, the application will be accessible through the GKE cluster's external IP or the configured Ingress.

Access the Web Interface: Open your browser and navigate to the application's URL.
Interact with the LLM: Use the web interface to input text and receive generated responses from the HuggingFaceTB/SmolLM-360M model.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.
## License

This project is licensed under the MIT License.