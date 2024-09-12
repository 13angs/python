#!/bin/bash

# Build the Docker image and push the image to Docker Hub
docker build -t 13angs/flask-liveness-readiness:latest . && \
    docker push 13angs/flask-liveness-readiness:latest