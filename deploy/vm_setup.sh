#!/bin/bash

# Update and install required packages
sudo apt update -y
sudo apt install -y python3-pip

# Install required Python packages
pip3 install -r requirements.txt

# Set up environment variables
echo "export AMADEUS_API_KEY='your_api_key'" >> ~/.bashrc
echo "export AMADEUS_API_SECRET='your_api_secret'" >> ~/.bashrc
source ~/.bashrc

