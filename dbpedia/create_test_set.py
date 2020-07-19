from rdflib import Graph
from rdflib.plugins.stores.sparqlstore import SPARQLStore
import pandas as pd

data_graph = Graph(SPARQLStore("http://dbpedia.org/sparql", context_aware=False))
counter = 0
pages = []

results1 = data_graph.query("""
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpo: <http://dbpedia.org//>
select distinct ?Page where {?Page rdf:type yago:WikicatUprisingsDuringWorldWarII}
""")

for row in results1:
    str_r = str(row)
    if '(rdflib.term.URIRef("' in str_r:
        str_rq = str_r.split('"')
        pages.append(str_rq[1])
    else:
        str_rq = str_r.split("'")
        pages.append(str_rq[1])
    counter+=1

print(counter)

results2 = data_graph.query("""
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpo: <http://dbpedia.org//>
select distinct ?Page where {?Page rdf:type yago:WikicatNaziWarCrimes}
""")

for row in results2:
    str_r = str(row)
    if '(rdflib.term.URIRef("' in str_r:
        str_rq = str_r.split('"')
        pages.append(str_rq[1])
    else:
        str_rq = str_r.split("'")
        pages.append(str_rq[1])
    counter+=1

print(counter)

results3 = data_graph.query("""
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpo: <http://dbpedia.org//>
select distinct ?Page where {?Page rdf:type yago:WikicatTreatiesAndDeclarationsOfTheEuropeanUnion}
""")

for row in results3:
    str_r = str(row)
    if '(rdflib.term.URIRef("' in str_r:
        str_rq = str_r.split('"')
        pages.append(str_rq[1])
    else:
        str_rq = str_r.split("'")
        pages.append(str_rq[1])
    counter+=1

results4 = data_graph.query("""
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpo: <http://dbpedia.org//>
select distinct ?Page where {?Page rdf:type yago:Revolution107424109}
""")

for row in results4:
    str_r = str(row)
    if '(rdflib.term.URIRef("' in str_r:
        str_rq = str_r.split('"')
        pages.append(str_rq[1])
    else:
        str_rq = str_r.split("'")
        pages.append(str_rq[1])
    counter+=1

results5 = data_graph.query("""
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpo: <http://dbpedia.org//>
select distinct ?Page where {?Page rdf:type umbel-rc:OlympicGames}
""")

for row in results5:
    str_r = str(row)
    if '(rdflib.term.URIRef("' in str_r:
        str_rq = str_r.split('"')
        pages.append(str_rq[1])
    else:
        str_rq = str_r.split("'")
        pages.append(str_rq[1])
    counter+=1


print(counter)
print(pages[0])

abstract = []
titles = []
target = []
for p in pages:
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
        abstract.append(str_r)
        titles.append(p)
        target.append(1)
        print(str_r)

print(abstract[0])
hist_df = pd.DataFrame(list(zip(titles, abstract, target)), columns=['Name', 'Abstract', 'Target'])
hist_df.to_pickle("hist_test.pkl")






