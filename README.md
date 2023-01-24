# do-python-dockerized-api

## :wave: Welcome

This Python API project is designed to provide secure password authentication by salting and hashing user passwords.

## 💻 Description

Rhe project includes a secure method for storing and verifying user passwords, an API that allows users to create new accounts and authenticate existing accounts using the salted and hashed passwords, and test cases to ensure the functionality is working as expected. The project is containerized using Docker, making it easy to set up and run in different environments and providing a consistent and reproducible way to handle password authentication in web applications.

## :gear: Packages & Requirements

-  described in requirements.txt file

## :bookmark_tabs: To run the app

1. go to {root}/python
2. run `docker-compose build`
3. run `docker-compose up`
4. to run test `docker exec -ti pythonapi python -m unittest tests-login.py`


