country-randomizr
=================

A very simple Python web app to randomly pick a country and show a Google Map.

How's it work?
--------------

This is created using the GoogleAppEngine and is written in Python. It is the code behind: http://james.thebatefamily.com/

Point the GoogleAppEngineLauncher at your folder and start up the server. 
Navigate to the root URL and a country will be randomly chosen. It will show the capital city and continent along with a full screen Google Map.

Database
--------

The app uses the GoogleAppEngine Datastore. Either manually create a new index or use the `add` option described below.

Options
-------

The web app does take a couple of URL parameters so you can get fancy:

* __c__ - force a particular country to be retrieved (e.g. `?country=brazil`)
* __add__ - when adding a new country append `add=true` and the relevant form will appea
* __country__ - when adding a country append a `country` name to pre-populate the country box in the form
* __capital__ - when adding a country append a `capital` name to pre-populate the capital box in the form
* __continent__ - when adding a country append a `continent` name to pre-populate the continent box in the form
