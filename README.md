# Pi Data Strategy & Consulting - Python Challenge (Backend)
![pi_data_strategy_&_consulting_logo](pi_logo.png)

Welcome, `3.14` reviewer!

In this repository, you will find my solution for `Pi Data Strategy & Consulting` - `Python Backend` challenge.

If you don't have the challenge itself, don't worry, I will attach it in this file: [Click here](https://github.com/AugustoCarloPareja/pi_python_challenge/blob/master/ChallengePython-Interview.pdf)

This app was created using FastAPI (I really love `pydantic`!).

Also, it offers flexibility for deployment, allowing for local deployment or containerization using the provided Dockerfile.

## Local Deployment
To deploy the application locally, follow these steps:
1. Clone the repository to your local machine.
2. Create a local enviroment (it is a good practice to isolate enviroments) and activate it.
```
python -m venv venv
```
```
venv\Scripts\activate
```
3. Install the required dependencies listed in requirements.txt.
```
pip install -r requirements.txt
```
4. Run the FastAPI server using the provided command.
```
uvicorn api.main:app --reload
```

**Side note**:
- When the app was being created, it was used a virtual enviroment named venv, but for clean code purposes, it was ignored by default by the .`gitignore` file.

## Containerized Deployment
Alternatively, you can deploy the application as a container using Docker. 

Follow these steps:
1. Ensure Docker is installed on your system.
2. Build the Docker image using the provided Dockerfile.
  ```
docker build -t pi_python_challenge .
  ```
3. Run the Docker container (port 8000 by default).
  ```
docker run -d -p 8000:8000 pi_python_challenge
  ```

## Documentation / Swagger Docs
Curious to learn more about the API endpoints and their functionalities? FastAPI automatically generates interactive API documentation (Swagger Docs) for you!

Follow these steps to check out the API documentation:
1. Ensure that the API server is up and running locally. If not, follow the instructions provided in the "Local Deployment" or "Containerized Deployment" section above.
1. Open your web browser and navigate to http://localhost:8000/docs.
1. Explore the interactive API documentation to view details about each endpoint, including request parameters, response formats, and example requests/responses.
1. Use the interactive interface to test out different endpoints and see live responses.

The Swagger Docs provide a user-friendly interface for understanding and interacting with the API, making it easy to explore its capabilities.

## API Testing
Excited to try out the API? Let's get started!

### Using Postman Collection
1. Download the Postman Collection from [here](https://github.com/AugustoCarloPareja/pi_python_challenge/blob/master/docs/PI%20DS%20%26%20Consulting-%20Python%20Challenge.postman_collection.json).
1. Import the collection into your Postman application.
1. Start exploring and testing the API endpoints right away!

### Local Testing
Prefer testing locally? No problem!

1. Ensure that the API server is up and running locally. If not, follow the instructions provided in the "Local Deployment" or "Containerized Deployment" section above.
1. Open your preferred API testing tool (e.g., Postman, cURL).
1. Send requests to the API endpoints using the base URL http://localhost:8000 (or the appropriate URL if you've configured a different port).

Get ready to interact with the API and witness its functionality firsthand!

## Final notes
It was a pleasure working on this project, and I'm excited to share my solution with you. I hope you enjoy exploring the code and functionalities as much as I enjoyed developing them.

Happy reviewing, and thank you for taking the time to assess my work! 😎