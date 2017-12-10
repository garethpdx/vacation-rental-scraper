# Vacation Rental Scraper

Extract property details from short-term rental listing by downloading and processing a listing, then running predefined extractors against the parsed property information. When run from the command line, scraped details are printed as JSON objects.

Initially, only Airbnb is supported. To retrieve Airbnb property information, this project takes advantage of the fact that Airbnb's use of redux, react[1], and hypernova[2] means that a full representation of a property can be found in JSON embedded within the listing.

[1] https://github.com/airbnb/hypernova-react
[2] https://github.com/airbnb/hypernova

## Getting Started

Fetch property information by passing URLs to main.py as stdin, one per line:

> $ python main.py < tests/urls.txt

## Installation:

Clone this repo from GitHub, then install requirements:

> $ pip3 install -r requirements.txt

This project has only been tested with python3. 

## Run tests

> $ PYTHONPATH=. python tests/tests.py

## Vacation Rental Scraper

While only Airbnb is supported at the moment, support for additional vendors could be added by implementing another in scraper/vendors/. At a minimum, this would consist of adding a preprocessor and selectors to handle the new vendor's page model. See scraper/vendors/airbnb.py for an example. After implementing a new vendor, register it in scraper/vendors/__init__.py

If it becomes necessary handle more than 3 properties at a time, requests should be parallelized. The most time consuming part of this process is I/O wait while we're downloading the page from Airbnb servers. It'd be a lot faster to fetch them in parellel, maybe with async or a scraper library like scrapy.
