# Basic Information

```bash
# Check Docker version
docker --version

# Show system-wide information
docker info
```

# Container Management

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Run an image
docker run image_name

# Run image in interactive mode (terminal access)
docker run -it image_name

# Run image in background (detached mode)
docker run -d image_name

# Run container and give it a custom name
docker run -d --name my_container image_name

# Map ports (host:container)
docker run -d -p 8080:80 image_name

# Run with environment variables
docker run -d -e KEY=value image_name

# Stop a running container
docker stop container_id

# Start a stopped container
docker start container_id

# Restart a container
docker restart container_id

# Remove a stopped container
docker rm container_id

# Stop all running containers
docker stop $(docker ps -q)

# Remove all stopped containers
docker container prune
```

# Inspecting & Debugging

```bash
# Detailed info of a container
docker inspect container_name_or_id

# View logs of a container
docker logs container_name_or_id

# Follow (stream) container logs
docker logs -f container_name_or_id

# Execute a command inside a running container
docker exec -it container_name_or_id bash

# View live resource usage (CPU, RAM, etc.)
docker stats

# Check container port mappings
docker port container_name_or_id
```

# Image Management

```bash
# List all images
docker images

# Build image from Dockerfile
docker build -t image_name .

# Remove specific image
docker rmi image_id

# Remove all images
docker rmi $(docker images -q)

# Remove dangling (unused) images
docker image prune

# Remove all unused images (not used by any container)
docker image prune -a
```

# Volumes & Networks

```bash
# List all volumes
docker volume ls

# Remove all unused volumes
docker volume prune

# List all networks
docker network ls

# Remove all unused networks
docker network prune
```

# Cleanup & System Maintenance

```bash
# Remove stopped containers, unused networks, and build cache
docker system prune

# Remove everything (containers, images, networks, volumes)
docker system prune -a --volumes
```

# Pro Tips

```bash
# Run container with auto-restart policy
docker run -d --restart unless-stopped image_name

# Copy file from host to container
docker cp ./file.txt container_name:/path/in/container

# Copy file from container to host
docker cp container_name:/path/in/container ./file.txt

# Rename a container
docker rename old_name new_name

# Check logs for specific time range or last lines
docker logs --since 1h container_name
docker logs --tail 100 container_name
```

# Docker Compose

```bash
# Start all services defined in docker-compose.yml
docker compose up -d

# Stop all running services
docker compose down

# View logs for all services
docker compose logs -f

# Rebuild services
docker compose up --build
```
