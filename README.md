# URL Shortener

This is a project about making a URL shortener using Django.

## Installation & Usage

* Clone the repo or download the repo files and `cd` into the root of the project
* Run `pipenv shell` to enter a virtual environment
* Run `pipenv install` to install the necessary packages
* `cd` into the *URLshortener* directory and run `python manage.py runserver`
* You can view the result at http://localhost:8000 

## Run *runserver --insecure* if you can't see a styled site or getting any error?

To handle errors we turned Debug mode off to be able to display our owns html files for differents errors.
With debug turned off Django won't handle static files for you any more. Your production web server should take care of that.
Using *--insecure* django is able to find static files locally and also handle errors.


## How it looks...

![Homepage](https://i.ibb.co/Gfwdp9Z/2022-05-05-1.png)


![Homepage With New Url](https://i.ibb.co/qR9vW4N/2022-05-05.png)
