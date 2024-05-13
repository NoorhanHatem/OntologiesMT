from rdflib import Graph, URIRef, RDF

g = Graph()
g.parse("movie5.owl", format='ttl')

print("Persons:")
for s, p, o in g.triples((None, RDF.type, None)):
    if o.endswith("actor") or o.endswith("director") or o.endswith("writer"):
        print(s)