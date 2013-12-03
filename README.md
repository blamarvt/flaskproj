## flaskproj

This is a seriously basic but hopefully (eventually) complete app to get started quickly with Flask.

### Create Your Virtual Environment
    make venv

Although this command will run automatically before any other command, feel free to run it explicitly. This command will create a Python virtual environment (http://www.virtualenv.org/en/latest/) and update all dependencies in requirements.txt and test-requirements.txt. 


### Test Your Code
    make test

Currently there are no tests, but this will run `nosetests` regardless!


### Initialize The Datastore
    make db (Not Yet Implemented)
    
Creates tables, indicies, and any other datastructures necessary to run this project using the configured database. Ideally, this will also run any database migrations you might have as well!


### Create Documentation
    make docs (Not Yet Implemented)
    
Generate documentation and ideally publish it locally or remotely (depending on configuration settings).


### Install Permanently
    make install (Not Yet Implemented)
    
Use Puppet (http://puppetlabs.com/) to install and configure this app based on configuration options.
