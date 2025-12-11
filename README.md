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

2. **Launch the demo**
     ```
     docker compose up --build
     ```
     This will create and run the container.

3. **Migrate the database changes**

     First run bash inside the running container
     ```
     docker exec -it <container-id> /bin/bash
     ```
     
     Now run manage.py migrate
     
     ```
     uv run manage.py migrate
     ```
     

## Configuration

- Default admin credentials (if applicable):
  ```
  Username: admin
  Password: password
  ```

## License
This project is licensed under the MIT License.
