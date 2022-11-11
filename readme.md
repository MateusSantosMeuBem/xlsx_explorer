# XLSX EXPLORER

Simple project to rows from a xlsx file using flask.

## Set up the configurations
Copy the file env.
```sh
cp app/example.env app/.env
```
And fill its fields for your goal.

## Install dependencies
All commands should be run into [git bash](https://git-scm.com/downloads)


### Python
Install python, just [click here](https://www.python.org/downloads/).

### Create and active a virtual enviroment
To run the project into a controlled enviroment, let's create a virtual enviroement using a native python module.

**Create the enviroment** 
```sh
python -m venv venv
```
**Active the enviroment**
```sh
. venv/Script/activate
```

### Install packages
```sh
pip install -r requirements.txt
```

## Run app
Just execute the program using yout python interpreter.
```sh
python app
```
To get the json, access the follow url:
```txt
http://127.0.0.1:5000/row/{row_index}
```