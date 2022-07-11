#!/bin/bash
# Simple script to run CLI tool inside the docker container

DOCKER=`which docker`
VERSION="latest"
NAME="nornir_example"

# UID and GID of current user.
# Files created by the script running inside the container
# will be owned by current user and not root.
USER="--user $(id -u):$(id -g)"

# Mount host user info and current directory
VOLUMES="-v /etc/passwd:/etc/passwd:ro \
         -v /etc/shadow:/etc/shadow:ro \
         -v /etc/group:/etc/group:ro \
         -v $(pwd):/opt/${NAME}"

# Image to use
IMAGE="${NAME}:${VERSION}"

$DOCKER run $USER $VOLUMES $IMAGE $@