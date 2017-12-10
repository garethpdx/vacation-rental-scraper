AirBNB Property Parser

Extract property details from  AirBNB URLs.

Getting Started

Fetch property information by passing URLs to main.py as stdin, one per line:

$ python main.py < tests/urls.txt

Installation:

This project has only been tested with python3.

Install requirements before using

$ pip3 install -r requirements.txt

Run tests

$ PYTHONPATH=. python tests/tests.py

Only airbnb is supported at the moment. Support for additional vendors could be added by implementing another in scraper/vendors. At a minimum, this would consist of adding a preprocessor and selectors to handle the new vendor's page model. See scraper/vendors/airbnb.py for an example. After implementing a new vendor, register it in scraper/vendors/__init__.py

If it becomes necessary handle more than 3 properties at a time, requests should be parallelized. The most time consuming part of this process is I/O wait while we're downloading the page from airbnb servers. It'd be a lot faster to fetch them in parellel, maybe with async or a scraper library like scrapy.
