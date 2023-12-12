#!/bin/bash

read -p "Enter new db username: " username
read -p "Enter new db password: " password

echo "DB_USER=$username" > .env
echo "DB_PASSWORD=$password" >> .env

docker compose up