# Scrollable Sidebar Dashboard

This sample dashboard shows a static collapsible sidebar menu that **vertically scrolls along the page**.

![Sample Dashboard 2](app/static/images/sample_dashboard2.2.gif)

Check out the other sample dashboards:

- [x] [Custom dashboard](https://github.com/GitauHarrison/simple-dashboard-in-flask) &#10004;
- [x] [Scrollable sidebar dashboard](https://github.com/GitauHarrison/scrollable-sidebar-dashboard) (this repo) &#10004;
- [x] [Fixed sidebar dashboard](https://github.com/GitauHarrison/fixed-sidebar-dashboard) &#10004;
- [x] [Overlay fixed sidebar dashboard](https://github.com/GitauHarrison/overlay-fixed-sidebar-dashboard) (this repo) &#10004;
- [x] [Partially collapsible sidebar dashboard](https://github.com/GitauHarrison/partially-collapsible-sidebar-dashboard) &#10004;

## Technologies Used

- Flask
- Flask Bootstrap 
- Media queries
- Font Awesome
- Flask Login
- Flask Migrate
- Flask SQLAlchemy
- Flask WTF

## Features 

- Basic user authentication

## Testing Locally

- Clone this repo:
    ```python
    $ git clone git@github.com:GitauHarrison/scrollable-sidebar-dashboard.git
    ```

- Move into cloned directory:
    ```python
    cd scrollable-sidebar-dashboard
    ```

- Create and activate a virtual environment:
    ```python
    $ mkvirtualenv venv # I am using virtualenvwrapper
    ```

- Install project dependancies:
    ```python
    (venv)$ pip3 install -r requirements.txt
    ```

- Copy the contents of `.env-template` to `.env` file:
    ```python
    (venv)$ cp .env-template .env
    ```

- Update the values in `.env` (we have only the `SECRET_KEY`) py pasting the output of the command below:
    ```python
    (venv)$ python3 -c 'import secrets; print(secrets.token_hex(12))'
    ```

- Run the application:
    ```python
    (venv)$ flask run
    ```

- Check the application in your favourite browser by pasting the URL http://127.0.0.1:5000/

- [Register](http://127.0.0.1:5000/register) a user then [log them in](http://127.0.0.1:5000/login). You should be able to access the sample dashboard.

Reference: [Bootstrapicious](https://bootstrapious.com/p/bootstrap-sidebar)&#9996;.