from rdflib import Graph
from rdflib.plugins.stores.sparqlstore import SPARQLStore
import pandas as pd

data_graph = Graph(SPARQLStore("http://dbpedia.org/sparql", context_aware=False))
counter = 0

pages2 = []
results6 = data_graph.query("""
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpo: <http://dbpedia.org//>
select distinct ?Page where {?Page rdf:type yago:WikicatArtificialNeuralNetworks}
""")

for row in results6:
    str_r = str(row)
    if '(rdflib.term.URIRef("' in str_r:
        str_rq = str_r.split('"')
        pages2.append(str_rq[1])
    else:
        str_rq = str_r.split("'")
        pages2.append(str_rq[1])
    counter+=1

print(counter)

results7 = data_graph.query("""
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpo: <http://dbpedia.org//>
select distinct ?Page where {?Page rdf:type yago:RainForest108439126}
LIMIT 1400
""")

for row in results7:
    str_r = str(row)
    if '(rdflib.term.URIRef("' in str_r:
        str_rq = str_r.split('"')
        pages2.append(str_rq[1])
    else:
        str_rq = str_r.split("'")
        pages2.append(str_rq[1])
    counter+=1

print(counter)

results8 = data_graph.query("""
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpo: <http://dbpedia.org//>
select distinct ?Page where {?Page rdf:type dbo:Food}
LIMIT 300
""")

for row in results8:
    str_r = str(row)
    if '(rdflib.term.URIRef("' in str_r:
        str_rq = str_r.split('"')
        pages2.append(str_rq[1])
    else:
        str_rq = str_r.split("'")
        pages2.append(str_rq[1])
    counter+=1

print(counter)

results9 = data_graph.query("""
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpo: <http://dbpedia.org//>
select distinct ?Page where {?Page rdf:type dbo:Activity}
LIMIT 150
""")

for row in results9:
    str_r = str(row)
    if '(rdflib.term.URIRef("' in str_r:
        str_rq = str_r.split('"')
        pages2.append(str_rq[1])
    else:
        str_rq = str_r.split("'")
        pages2.append(str_rq[1])
    counter+=1

print(counter)

abstract2 = []
titles2 = []
target2 = []
for p in pages2:
    abstrac1 = data_graph.query("""
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dbpo: <http://dbpedia.org//>
    SELECT ?label 
    WHERE {
        <"""+p+"""> dbo:abstract ?label . 
        FILTER (lang(?label) = 'en') .
    }
    """)

    for row in abstrac1:
        str_r = str(row)
        str_r = str_r.replace('(rdflib.term.Literal(', '')
        str_r = str_r.replace("lang='en'", "")
        str_r = str_r.replace('),)"]', '')
        str_r = str_r.replace("'", "")
        str_r = str_r.replace('"', "")
        str_r = str_r.replace(',', '')
        str_r = str_r.replace('[', '')
        str_r = str_r.replace('(', '')
        str_r = str_r.replace(')', '')
        abstract2.append(str_r)
        titles2.append(p)
        target2.append(0)
        print(str_r)

non_hist_df = pd.DataFrame(list(zip(titles2, abstract2, target2)), columns=['Name', 'Abstract', 'Target'])
non_hist_df.to_pickle("non_hist_test.pkl")