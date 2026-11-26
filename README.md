
# Flask Calculator API

## Project Overview

This is a simple Calculator API built using Python and Flask.

The API performs four mathematical operations:
- Addition
- Subtraction
- Multiplication
- Division

I built this project to practise DevOps tools and understand how an application is tested, packaged into a Docker image, and deployed automatically using CI/CD.

## Technologies Used

- **Python:** Used to write the application.
- **Flask:** Used to create the API and its endpoints.
- **Pytest:** Used to test the API automatically.
- **Docker:** Used to package the application into a container.
- **Docker Compose:** Used to build and run the application locally.
- **Gunicorn:** Used as the production server for Flask.
- **Git and GitHub:** Used for version control and storing the project.
- **GitHub Actions:** Used to automate testing, building and deployment.
- **Docker Hub:** Used to store and publish Docker images.
- **Self-hosted GitHub Runner:** Used to deploy the application on my MacBook.

## API Endpoints

The API supports the following operations:

| Endpoint | Description |
|---|---|
| `/add?a=10&b=20` | Adds two numbers |
| `/subtract?a=20&b=10` | Subtracts two numbers |
| `/multiply?a=10&b=5` | Multiplies two numbers |
| `/divide?a=20&b=5` | Divides two numbers |
| `/environment` | Shows the application environment |

The API also handles invalid input, missing values and division by zero.

## Project Structure

```text
proj2/
│
├── app.py
├── test_app.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── compose.yaml
├── .gitignore
└── .github/
    └── workflows/
        └── ci.yml
```

### Important Files

- **app.py:** Contains the Flask application and API endpoints.
- **test_app.py:** Contains automated tests for the API.
- **requirements.txt:** Contains the application dependencies.
- **requirements-dev.txt:** Contains the dependencies needed for development and testing.
- **Dockerfile:** Contains instructions to build the Docker image.
- **compose.yaml:** Defines how to build and run the application using Docker Compose.
- **ci.yml:** Defines the GitHub Actions CI/CD pipeline.
- **.gitignore:** Prevents unnecessary files, such as the Python virtual environment, from being committed.

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/hussainayubplymuni-ui/flask-app-proj2.git
cd flask-app-proj2
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements-dev.txt
```

### 4. Run the tests

```bash
pytest -v
```

### 5. Start the application

```bash
python3 app.py
```

The API will be available at:

```text
http://localhost:5000
```

## Running with Docker Compose

Make sure Docker Desktop is running.

Build and start the application:

```bash
docker compose up -d --build
```

The API will be available at:

```text
http://localhost:5001
```

To stop the application:

```bash
docker compose down
```

## CI/CD Pipeline

I created a GitHub Actions workflow to automate the project deployment.

The pipeline has three main jobs:

### 1. Test

- Runs on a GitHub-hosted Ubuntu runner.
- Installs Python and the required dependencies.
- Runs automated tests using Pytest.
- Checks that the application is working correctly.

### 2. Build and Push

- Runs after the tests pass.
- Builds a Docker image using the Dockerfile.
- Builds images for AMD64 and ARM64 platforms.
- Logs in to Docker Hub using GitHub Secrets.
- Pushes the Docker image to Docker Hub.

### 3. Deploy

- Runs after the Docker image is successfully published.
- Uses a self-hosted GitHub Actions runner on my MacBook.
- Pulls the latest Docker image from Docker Hub.
- Stops and removes the previous deployed container.
- Starts the updated container using Docker.

The deployed application is available locally at:

```text
http://localhost:5002
```

## Docker Hub

Docker image:

```text
hussainayub/flask-calculator-api
```

## What I Learned

Through this project, I gained practical experience with:

- Creating a REST API using Flask.
- Writing automated tests using Pytest.
- Understanding Docker images and containers.
- Writing Dockerfiles and using Docker Compose.
- Using Gunicorn to run a Flask application.
- Creating CI/CD pipelines with GitHub Actions.
- Managing GitHub Secrets.
- Building and publishing multi-platform Docker images.
- Setting up a self-hosted GitHub Actions runner.
- Automating application deployment.

## Author

Hussain Ayub

