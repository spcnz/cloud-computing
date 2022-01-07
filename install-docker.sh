#!/bin/bash
if [ -x "$(command -v docker)" ];
then 
    echo "Docker is already installed!"
    exit
else
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
fi