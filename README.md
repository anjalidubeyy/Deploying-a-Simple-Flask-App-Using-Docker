# Dockerized Flask Web Application

## Overview
This project demonstrates how to containerize a simple Flask web application using Docker. By encapsulating the application in a Docker container, we ensure consistency across environments, simplify deployment, and eliminate dependency conflicts.

## Prerequisites
- Docker installed on your system
- Python 3.9 or later

## Project Structure
```
.
├── app.py              # Flask application script
├── requirements.txt    # Dependencies
├── Dockerfile          # Docker configuration file
└── README.md           # Project documentation
```

## Installation & Setup

### 1. Clone the Repository
```sh
git clone <repository_url>
cd <repository_name>
```

### 2. Create a Virtual Environment (Optional)
```sh
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

## Running the Application Locally (Without Docker)
```sh
python app.py
```
Access the app at: `http://localhost:5000`

## Dockerizing the Application

### 1. Build the Docker Image
```sh
docker build -t flask-app .
```

### 2. Run the Docker Container
```sh
docker run -p 5000:5000 flask-app
```

### 3. Access the Application
Open your browser and go to:
```
http://localhost:5000
```

## Debugging & Logs
- Check running containers:
  ```sh
  docker ps
  ```
- View logs:
  ```sh
  docker logs <container_id>
  ```
- Stop a running container:
  ```sh
  docker stop <container_id>
  ```

## Conclusion
This project successfully demonstrates how to Dockerize a Flask web application, making it portable and easy to deploy across different environments.

## Future Enhancements
- Implement Docker Compose for multi-container applications.
- Deploy the containerized app on cloud services like AWS, Azure, or Google Cloud.
- Automate deployment using CI/CD pipelines.

## Author
- **Anjali Dubey**
