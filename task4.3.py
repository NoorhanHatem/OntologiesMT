from rdflib import Graph, RDF
from owlrl import DeductiveClosure, OWLRL_Semantics

g = Graph()
g.parse("movie5.owl", format='ttl')

DeductiveClosure(OWLRL_Semantics).expand(g)

print("Persons:")
for s, p, o in g.triples((None, RDF.type, None)):
    if o.endswith("actor"):
        print(s)