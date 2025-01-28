# Backend Developer Test

A simple test application for Catch Design Backend developers test.

## How to run the app

### Environment Requirements

0. git
1. Pythen 3.12 
2. Pip

### Local Set up
0. Go to root folder `CATCHDESIGN-DEV-TEST`
1. Run `pip install pipenv` to install virtual environments.
2. Run `pipenv install` to install all the required framework and packages.
3. Run `pipenv shell` to actiave the virtual environment.
4. Go to directory `test-project` and run `python manage.py migrate` to set up local DB.
5. Run `python manage.py import_customer` to load data to local DB.
6. Run `python manage.py runserver` to host the local server

### Presents
1. Visit `http://127.0.0.1:8000/test_app/api/customers/?page=2&gender=Male&page_size=5` to see the API customer data in JSON foramt that suitable for web and mobile client.
    * URL parameter __page__ can filter by page number.
    * URL parameter __page_size__ can filter by number of item per page.
    * URL parameter __gender__ can filter by options: 'Male', 'Female' and 'Other'
    * URL parameters also can have __city__ and __company__
    * Result ordering can sort by __id__, __last_name__ or __email__
2. Visit `http://127.0.0.1:8000/test_app/customers/` see web page asynchronously loads the customer data from API.
