# ERUDIT-BACKEND
This project is the backend service for Erudit. It provides APIs and handles data processing for the Erudit application.

## Getting started
Follow the steps below to set up and run the speech-service using Docker.
   
### ⚙️ Configure Environment Variables

Copy the example environment file and fill in the necessary values:

```bash
cp .env.example .env
```

Edit the `.env` file to set your environment variables. You can use the default values or customize them as needed.

### 🐳 Build and Run the Docker Container

Start the Docker container with the following command:

```bash
docker compose up --build -d
```

This command will build the Docker image and start the container.
