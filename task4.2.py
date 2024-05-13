from rdflib import Graph, URIRef

g = Graph()
g.parse("movie5.owl", format="turtle")

query = """
    SELECT DISTINCT ?individual
    WHERE {
        {?individual a :writer .}
        UNION
        {?individual a :actor .}
        UNION
        {?individual a :director .}
    }
"""

results = g.query(query)

print("Persons")
for row in results:
    individual = row["individual"]
    print(individual)
