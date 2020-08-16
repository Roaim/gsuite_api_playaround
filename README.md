# Access GSuite APIs using Python Flask

A sample project to playaround with **GSuite APIs** i.e. Doc, Sheet, etc. using **Python Flask**.

### Demo

Demo is hosted at: 

https://gsapi.roaim.app/sheets

### Documentation: 
Replace `{{host}}` with the following value:

    "host": "https://gsapi.roaim.app"

**DOC:** [sheet.http](http/sheet.http)

## Environment Setup

Create project directory

    mkdir gsapi
    cd gsapi
    
#### Requirements
* **Python 3.7+**

Run the following commands to create and activate a virtual environment named `venv` (different name can be used)

    python3 -m venv venv
    . venv/vin/activate

## Build and Install
Set flask app by running following command:
#### Windows
    
    set FLASK_APP=app

#### Linux / Mac

    export FLASK_APP=app

### Build Distribution Package
If wheel is not installed run the follwoing command to install it:

    pip install wheel

To build distribution package run the following command:

    python setup.py bdist_wheel

    
## Create database
For the first time, run the following commands to create database schemas:

    flask db init
    flask db migrate
    flask db upgrade

### Install Distribution Package
Replace **x.x.x** with the actual version name

    pip install app-x.x.x-py3-none-any.whl

## Run
If **`waitress`** is not installed run the following command to install it:

    pip install waitress

If **`waitress`** is already installed run the following command to run the application:

    waitress-serve --call app:create_app

## Setup Google Service Account
Follow the [Using OAuth 2.0 for Server to Server Applications](https://developers.google.com/identity/protocols/oauth2/service-account#python) documentation to [create a service account](https://developers.google.com/identity/protocols/oauth2/service-account#creatinganaccount).

Download your **Google Service Account JSON** file from google console and rename it to 

    gsapipa-1597559125165-8c2be94eb0b8.json 

and copy it to 

    venv/var/app-instance/
