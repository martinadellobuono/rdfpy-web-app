# RDFpy web app template

**RDFpy web app template** is a [Python 3](https://www.python.org/downloads/) web application built in [Flask](https://flask.palletsprojects.com/en/2.3.x/).

## Quick start

Clone this repository using the URL https://github.com/rdfpy-web-app-template.git
or download the folder.

The project works with this **requirement**:

- [**Python**](https://www.python.org/downloads/) v3.6.3

Packages can be installed by running **setup.sh**:
```
sh setup.sh
```

If your data are on [**Blazegraph**](https://blazegraph.com/):

after installing the required packages, install [**Blazegraph**](https://blazegraph.com/) locally:

- Download [**blazegraph.jar**](https://github.com/blazegraph/database/releases/tag/BLAZEGRAPH_2_1_6_RC)
- Create a new **folder** and rename it **data**
- Put **blazegraph.jar in data** folder
- From the terminal enter data and **run blazegraph.jar**:
```
cd data
java -server -Xmx4g -jar blazegraph.jar
```

If your data are on [**Wikidata**](https://www.wikidata.org/wiki/Wikidata:Main_Page) or other knowledge base:

change the endpoint and the query in **views.py**

Finally run the application:
- Run **app.py**
```
python3 app.py
```
- Open the application in your browser: **http://localhost:8000/**

The data are visualized in the frontend in [**Jinjia2**](https://pypi.org/project/Jinja2/).

Frontend toolkit: [**Bootstrap v5.2**](https://getbootstrap.com/docs/5.2/getting-started/introduction/).

