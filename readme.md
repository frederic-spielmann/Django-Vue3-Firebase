<div align="center">
  <h1 align="center">Django Rest API - Vue 3 - MySQL - Firebase</h1>
</div>

<!-- TABLE OF CONTENTS -->
### Table of Contents
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#authentication">Authentication</a></li>
      </ul>
    </li>
  </ol>

<!-- ABOUT THE PROJECT -->
## About The Project
Web Application with a simple CRUD example (Movie) and Firebase Authentication.
### Features :
* Firebase
  * Create / Delete a User account (Firebase + local DB MySQL)
  * Login / Logout
  * Reset a password
  * Update a User Profile (Display Name, Email, Password, Avatar)
* CRUD
  * Create / Update / Delete a Movie
  * List all Movies
  * Movie details

### Example :
<img src="https://raw.githubusercontent.com/frederic-spielmann/Django-Vue3-Firebase/main/screenshots/login.png" width="45%"></img> 
<img src="https://raw.githubusercontent.com/frederic-spielmann/Django-Vue3-Firebase/main/screenshots/update_profile.png" width="45%"></img> 
<img src="https://raw.githubusercontent.com/frederic-spielmann/Django-Vue3-Firebase/main/screenshots/home.png" width="45%"></img> 
<img src="https://raw.githubusercontent.com/frederic-spielmann/Django-Vue3-Firebase/main/screenshots/crud.png" width="45%"></img> 


### Built With
This section list all the major frameworks/libraries used in this project.

* Frontend
  * [Vue 3](https://vuejs.org/)
  * [Vue-Router](https://router.vuejs.org/)
  * [Pinia](https://pinia.vuejs.org/)
  * [Bootstrap 4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
  * [Firebase](https://firebase.google.com/docs/auth)
* Backend
  * [Python 3.11](https://www.python.org/)
  * [Poetry](https://python-poetry.org/)
  * [Django 4.1](https://www.djangoproject.com/)
  * [Django REST Framework 3.14](https://www.django-rest-framework.org/)
  * [Firebase Admin Python SDK](https://firebase.google.com/docs/reference/admin/python)
* Database
  * [MySQL 8.0](https://www.mysql.com/)
* Others
  * [Docker](https://www.docker.com/)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Docker and Docker-compose will be required for this project.

* [Get Docker](https://docs.docker.com/get-docker/)
* [Docker-Compose](https://docs.docker.com/compose/compose-file/)
* Having a [Firebase Project](https://firebase.google.com) setup with "Email/Password" as a Sign-in providers


### Installation
#### 1. Frontend :
* Firebase - In your Firebase Account, go to `Project Settings -> General`, and copy the JS configuration of your application. Paste the configuration in `frontend/src/.config`

<img src="https://raw.githubusercontent.com/frederic-spielmann/Django-Vue3-Firebase/main/screenshots/firebase.png"></img>

* In the `frontend` folder, create a `.env` file to configure your frontend and backend URLs.

Here is an example of the default configuration :
```
VITE_FRONTEND_URL="http://localhost:8080/"
VITE_BACKEND_URL="http://localhost:8000/api/"
```

#### 2. Database
* In the root folder (where there is `backend` and `frontend` folder), create a `.env` file, and provide your Domain and MySQL configuration.

Example:
```
DOMAIN=localhost

# MySQL
DB_DATABASE=myDatabase
DB_USERNAME=myUser
DB_PASSWORD=myPassword
```


#### 3. Backend :
* Firebase - In your Firebase Account, go to `Project Settings -> Service Accounts`.
In "Admin SDK configuration snippet" select "Python" and click on "Generate new private key".
It will download a `JSON` configuration file. Rename the file as `firebase.json` and add it to the `backend` folder

* Database - Open `backend/backend/settings.py` and update the MySQL credentials (as provided previously in the `.env`)


#### 4. Let's start
Open a Terminal / Command Prompt and type :

To create the migrations files
```
docker-compose run --rm backend python manage.py makemigrations
```

Start the Web App
```
docker-compose up -d --build
```

Migrate
```
docker-compose run --rm backend python manage.py migrate
```

Make sure all the containers started
```
docker container ls --all
docker container logs <containerID>
```

You can now access the website `http://localhost:8080` and the Django API with `http://localhost:3000/api/`

### Authentication

The following image shows the steps to authenticate a user with Firebase

<img src="https://raw.githubusercontent.com/frederic-spielmann/Django-Vue3-Firebase/main/screenshots/auth_diagram.png"></img>
