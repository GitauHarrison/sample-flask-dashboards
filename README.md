# Sample Dashboards

Below are samples of dashboards usable in flask applications. You can click on the links to navigate to individual projects. Alternatively, you can open each folder in the repository to interact with them. All folders are complete projects with individual README files.

- [x] [Custom dashboard](https://github.com/GitauHarrison/all-dashboards/tree/main/simple_flask_dashboard) &#10004;
- [x] [Scrollable sidebar dashboard](https://github.com/GitauHarrison/all-dashboards/tree/main/scrollable_sidebar_dashboard) &#10004;
- [x] [Fixed sidebar dashboard](https://github.com/GitauHarrison/all-dashboards/tree/main/fixed_sidebar_dashboard) &#10004;
- [x] [Overlay fixed sidebar dashboard](https://github.com/GitauHarrison/all-dashboards/tree/main/overlay_sidebar_dashboard) &#10004;
- [x] [Partially collapsible sidebar dashboard](https://github.com/GitauHarrison/all-dashboards/tree/main/partially_collapsible_sidebar_dashboard) &#10004;


## Testing The Projects

- Clone this repository
    ```python
    $ git clone git@github.com:GitauHarrison/sample-flask-dashboards.git
    ```

- Open the project you would want in your favourite text editor:
    ```python
    $ code sample-flask-dashboards/fixed_sidebar_dashboard # I am using VS Code
    ```

[From Your Editor's Terminal]

- Create and activate your virtual environment from your editor's terminal
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

- Update the values in `.env` (we have only the `SECRET_KEY`) by pasting the output of the command below:
    ```python
    (venv)$ python3 -c 'import secrets; print(secrets.token_hex(12))'
    ```

- Run the application:
    ```python
    (venv)$ flask run
    ```

- Check the application in your favourite browser by pasting the URL http://127.0.0.1:5000/

- [Register](http://127.0.0.1:5000/register) a user then [log them in](http://127.0.0.1:5000/login). You should be able to access the sample dashboard.

Reference: [Bootstrapicious](https://bootstrapious.com/p/bootstrap-sidebar) &#9996;.