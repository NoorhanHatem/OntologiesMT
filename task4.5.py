from rdflib import Graph, URIRef

g = Graph()
g.parse("movie5.owl", format="turtle")

query = """
    SELECT DISTINCT ?ActorDirector
    WHERE {

        {?ActorDirector a :actor .}
        
        {?ActorDirector a :director .}
    }
"""

results = g.query(query)

print("ActorDirector:")
for row in results:
    ActorDirector = row["ActorDirector"]
    print(ActorDirector)
