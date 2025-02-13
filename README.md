# django_api_admin Demo

This repository provides a quick way to launch a demo environment for `django_api_admin` using Docker Compose.

## Prerequisites

Ensure you have the following installed on your machine:
- [Docker](https://docs.docker.com/get-docker/)

## Getting Started

1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/api-admin-demo.git
   cd api-admin-demo
   git checkout -b nocelery origin/nocelery
   ```

2. **Build the Demo**
   ```sh
   docker build -t api-admin-node -f Dockerfile
   ```
   This will build the image.

3. **Launch the demo**
     ```
     docker run --name api-admin-demo --env-file .env -p 8000:8000 api-admin-demo
     ```
     This will create and run the container.


## Configuration

- Default admin credentials (if applicable):
  ```
  Username: admin
  Password: password
  ```


## License
This project is licensed under the MIT License.

