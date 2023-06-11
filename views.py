from flask import Blueprint, render_template
from SPARQLWrapper import SPARQLWrapper, JSON
import uuid

""" blueprint """
views = Blueprint(__name__, "views")

""" endpoint """
endpoint = "https://query.wikidata.org/sparql"
sparql = SPARQLWrapper(endpoint)

""" query """
query = """
    PREFIX bd: <http://www.bigdata.com/rdf#>
    PREFIX p: <http://www.wikidata.org/prop/>
    PREFIX psn: <http://www.wikidata.org/prop/statement/value-normalized/>
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX wikibase: <http://wikiba.se/ontology#>
    SELECT ?island ?islandLabel ?islandImage
    WITH {
        SELECT DISTINCT *
        WHERE {
            ?island (wdt:P31/wdt:P279*) wd:Q23442.
            OPTIONAL { ?island wdt:P18 ?islandImage. }
            ?island p:P2046/psn:P2046/wikibase:quantityAmount ?islandArea.
        }
        ORDER BY DESC(?islandArea)
        LIMIT 100
    } AS %i
    WHERE {
        INCLUDE %i
        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" . }
    }
    ORDER BY DESC(?islandArea) 
"""

""" home """
@views.route("/")
def index():
    return render_template("index.html")

""" data """
@views.route("/data")
def altro():
    """ convert data into JSON """
    sparql = SPARQLWrapper(endpoint)
    sparql.setTimeout(55)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    queryResults =  sparql.query().convert()

    """ list of items """
    items = []
    for result in queryResults["results"]["bindings"]:
        items.append(result["islandLabel"]["value"])
    
    """ dict of items """
    itemsDict = {}
    for i in items:
        for result in queryResults["results"]["bindings"]:
            if i == result["islandLabel"]["value"]:
                itemsDict[i] = result["island"]["value"]
    
    return render_template("data.html", itemsDict = itemsDict)