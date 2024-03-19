# Market
The web application was coded in Python language using Flask as the framework. The styling framework is Bootstrap, and the frontend was created using HTML and CSS.
For user authentication the app uses Flask-Login, this is an extension of Flask that provides user management and authentication features. 
This app uses PostGreSQL as a database hosted in Render.com.
The web app is hosted in a GitHub repository and uses GitHub Actions for the pipeline to deploy on a server hosted on Render.com.

## What is the application about?

The application that I develop it’s a very simplified version of an e-commerce website.

## Installation

Use the package manager pip:
```bash
pip install flask
```
Install the database (for a web app running locally):
```bash
pip install flask-sqlalchemy
```
Install also email validation for flask:
```bash
pip install email_validator
```
```bash
pip install Flask-Seeder
```


## Getting started to run it locally, first run the command to populate the seed into the app and then run the app.

```bash
flask seed run
```

```bash
flask run
```
