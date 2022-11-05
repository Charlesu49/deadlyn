# Backend

## Getting up and running
- Python version 3.10.7 (you can use pyenv to manage multiple pyhon versions)
- cd to the `/backend` directory
- set up and activate a virtual environment
- go to config.py and update `SQLALCHEMY_DATABASE_URI` to your database.
- run `source start.sh` to activate the venv andd set environmental variables or view the file and do that manually.
- For non sqlite databases, run the below to create the database in youur command line
    - open terminal
    - run `flask shell`
    - in the interactive window that comes up run;
    - `from app import db` 
    - `db.creat_all()`
    - exit the interactive shell with `exit()`
- run `flask run` to start the application
- test the register endpoint with the following body you can use a consistent password of '11111111'
    ```
    {
        "username": "uche",
        "password": "11111111",
        "email": "uche@dev.com
    }
    ```
- test the `/api/v1/login` endpoint with the following body and the response should bear a token
    ```
    {
    "req_username": "charlie",
    "req_password": "11111111"
    }
    ```

- Request to everyother endpoint will require a token e.g request to `/api/v1/user` requires a token which is validated before a response carrrying the information of the user is returned. so ensure there is a bearer token in the authorization header for that request.