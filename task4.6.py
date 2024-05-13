from rdflib import Graph, URIRef

g = Graph()
g.parse("movie5.owl", format="turtle")

# Query for movies made in america
query1 = """
    SELECT DISTINCT ?Movies
    WHERE {
        {?Movies a :movie .}
        
        {?Movies :movie_country "USA" .}
    }
"""
# Query for Action movies

query2 = """
    SELECT DISTINCT ?Movies
    WHERE {
        {?Movies a :movie .}

        {?Movies :movie_genre "Action" .}
    }
"""
# Query for movies involving quentin tarantino

query3 = """
    SELECT DISTINCT ?Movies
    WHERE {
        {?Movies a :movie .}
        {?Movies :hasActor :Quentin_Tarantino .}
        UNION
        {?Movies :hasDirector :Quentin_Tarantino .}
        UNION
        {?Movies :hasWriter :Quentin_Tarantino}
    }
"""

results1 = g.query(query1)
results2 = g.query(query2)
results3 = g.query(query3)

print("Movies made in America")
for row in results1:
    movie = row["Movies"]
    print(movie)

print("Action movies")
for row in results2:
    movie = row["Movies"]
    print(movie)
    
print("Movies involving Quentin Tarantino")
for row in results3:
    movie = row["Movies"]
    print(movie)