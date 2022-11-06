# Simple Dashboard in Flask

This is a very simple dashboard in flask. Basically, the content seen by an anonymous user is contained by bootstrap's class `container`. However, upon authentication, the content is not contained and a functional sidebar is provided. 

![Flask Dashboard](/app/static/images/flask_dashboard.gif)

Check out the other sample dashboards:

- [x] [Custom dashboard](https://github.com/GitauHarrison/simple-dashboard-in-flask)  (this repo) &#10004;
- [x] [Scrollable sidebar dashboard](https://github.com/GitauHarrison/scrollable-sidebar-dashboard) &#10004;
- [x] [Fixed sidebar dashboard](https://github.com/GitauHarrison/fixed-sidebar-dashboard) &#10004;
- [x] [Overlay fixed sidebar dashboard](https://github.com/GitauHarrison/overlay-fixed-sidebar-dashboard)  &#10004;
- [x] [Partially collapsible sidebar dashboard](https://github.com/GitauHarrison/partially-collapsible-sidebar-dashboard) &#10004;

## Features

- User authentication

## Tools Used

* Flask
* Python
* Flask SQLAlchemy
* Flask Bootstrap
* Flask Migrate
* Flask-Login
* Flask-WTF

## Testing the Application Locally

* Clone this repository:
    ```python
    git clone git@github.com:GitauHarrison/simple-dashboard-in-flask.git
    ```
* Move into the directory:
    ```python
    cd simple-dashboard-in-flask
    ```
* Create and activate a virtual environment:
    ```python
    $ virtualenv venv
    $ source venv/bin/activate

    # or (if you prefer using virtualenvwrapper)
    # $ mkvirtualenv venv
    ```
* Install dependencies within the virtual environment:
    ```python
    (venv)$ pip3 install -r requirements.txt
    ```
* Needed environment variables:
  * Create a file called `.env` in the root directory of the project.
    ```python
    (venv)$ touch .env
    ```
  * Add the following lines to the file:
    ```python
    SECRET_KEY=<your secret key>
    ```
    * Best to create the value of `SECRET_KEY` by running ```python -c "import os; print(os.urandom(24))"``` in your terminal.
* Start the flask server:
    ```python
    (venv)$ flask run
    ```
* Access the application on your browser using the link http://localhost:5000

<hr>
Cheers!