# Playwright Python Test the https://www.coffe-soft.com/

Example project for different features of the **Playwright** Python technology.

Many of the examples are working with the **OpenProject** site, so you should install it on your local 
machine before running them

Installation instruction for **OpenProject** can be found in [this](https://www.openproject.org/docs/installation-and-operations/installation/docker/#quick-start-1) link

## Prerequisite

Other than the **Open Project** site, you should have the following installed:

* Python 3.9 and up
* Pipenv
* Pytest

Create venv and install all dependencies by use requirements.txt:

```
> python -m venv venv
> source venv/bin/activate # On Windows, use venv\Scripts\activate
> pip freeze > requirements.txt
> pip install -r requirements.txt
```

[Or Not use the step above] Create venv and install all dependencies by use requirements.txt and pipenv:

```
> pip freeze > requirements.txt
install pipenv:
> pip install pipenv
active virtual environment:
> pipenv shell
And install it will create also Pipfile and Pipfle.lock:
> pipenv install
```


You will also need the Playwright installed.
While it is part of the projects dependencies and will be installed by Pipenv, it is best that you will follow the 
following command for installation of the different browsers rendering engines. 

```
> pip install playwright
> playwright install
```

## Running the project

You can run the tests using your favourite IDE or from the command line. For example:

```
> pytest .\tests\coffe_soft\test_home.py
```

## Running the project in parallel - using pytest pytest-xdist

You can run the tests using your favourite IDE or from the command line using parameter -n [number of workers].
For example using 10 workers:

```
> pytest .\tests\coffe_soft\test_home.py -n 10
```


