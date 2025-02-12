# django_api_admin Demo

This repository provides a quick way to launch a demo environment for `django_api_admin` using Docker Compose.

## Prerequisites

Ensure you have the following installed on your machine:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/api-admin-demo.git
   cd api-admin-demo
   ```

2. **Launch the Demo**
   ```sh
   docker compose up --build
   ```
   This will build and start the necessary containers.

3. **Access the Application**
   - The API admin interface should be available at:
     ```
     http://localhost:8000/admin/
     ```

4. **Stop the Demo**
   To stop and remove containers, use:
   ```sh
   docker compose down
   ```

## Configuration

- Default admin credentials (if applicable):
  ```
  Username: admin
  Password: password
  ```
- To customize environment variables, update the `.env` file before running `docker compose up`.

## Troubleshooting

- If ports are already in use, change the mapped ports in `docker-compose.yml`.
- Run logs can be checked with:
  ```sh
  docker compose logs -f
  ```

## License
This project is licensed under the MIT License.

