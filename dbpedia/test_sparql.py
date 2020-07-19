from rdflib import Graph
from rdflib.plugins.stores.sparqlstore import SPARQLStore
import pandas as pd

data_graph = Graph(SPARQLStore("http://dbpedia.org/sparql", context_aware=False))
results = data_graph.query("""
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpo: <http://dbpedia.org//>
select distinct ?Page where {?Page rdf:type dbo:Activity}
""")

counter=0
pages = []
for row in results:
    print(row)
    counter+=1

print(counter)