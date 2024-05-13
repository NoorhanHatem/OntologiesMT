from rdflib import Graph, Namespace, RDF
from owlrl import DeductiveClosure, OWLRL_Semantics

# Load the RDF data
def load_data(file_path):
    g = Graph()
    g.parse(file_path, format="ttl")
    return g

# Apply OWL inference
def apply_inference(graph):
    DeductiveClosure(OWLRL_Semantics).expand(graph)
    return graph

# Search films based on criteria using SPARQL
def search_films_sparql(graph, included_actors=None, excluded_actors=None, included_directors=None, 
                        excluded_directors=None, included_genres=None, excluded_genres=None):
    # Define namespaces
    ns = Namespace("http://www.semanticweb.org/noorh/ontologies/2024/4/untitled-ontology-6/")
    
    # Build the SPARQL query string
    query = """
PREFIX ns: <http://www.semanticweb.org/noorh/ontologies/2024/4/untitled-ontology-6/>

SELECT DISTINCT ?title ?year ?country ?genre ?actorName ?directorName
WHERE {
    ?movie a ns:movie ;
           ns:movie_title ?title ;
           ns:movie_year ?year ;
           ns:movie_country ?country .
    OPTIONAL { ?movie ns:movie_genre ?genre . }
    OPTIONAL { 
        ?movie ns:hasActor ?actor .
        ?actor ns:person_name ?actorName .
    }
    OPTIONAL {
        ?movie ns:hasDirector ?director .
        ?director ns:person_name ?directorName . }
        
    %s
    %s
    %s
    %s
    %s
    %s
}

    """ % (
        f"FILTER (?actor IN ({', '.join(map(lambda a: f'<{ns[a]}>', included_actors))}))" if included_actors else "",
        f"FILTER (?actor NOT IN ({', '.join(map(lambda a: f'<{ns[a]}>', excluded_actors))}))" if excluded_actors else "",
        f"FILTER (?director IN ({', '.join(map(lambda d: f'<{ns[d]}>', included_directors))}))" if included_directors else "",
        f"FILTER (?director NOT IN ({', '.join(map(lambda d: f'<{ns[d]}>', excluded_directors))}))" if excluded_directors else "",
        f"FILTER (?genre IN ({', '.join(map(lambda g: f'<{ns[g]}>', included_genres))}))" if included_genres else "",
        f"FILTER (?genre NOT IN ({', '.join(map(lambda g: f'<{ns[g]}>', excluded_genres))}))" if excluded_genres else ""
    )
    
    print("SPARQL Query:")
    print(query)

    # Execute the SPARQL query
    results = graph.query(query)
    
    # Convert the query results into a list of dictionaries
    films = []
    for row in results:
        film = {
            "title": row.title,
            "year": row.year,
            "country": row.country,
            "genre": row.genre,
            "actor": row.actorName,
            "director": row.directorName
        }
        films.append(film)
    
    return films

# Display list of films
def display_films(films):
    if films:
        print("Matching Films:")
        for idx, film in enumerate(films, start=1):
            print(f"{idx}. {film['title']} ({film['year']}) - {film['country']}")
            print("   Genre:", film['genre'])
            print("   Actor:", film['actor'])
            print("   Director:", film['director'])
            print()
    else:
        print("No matching films found.")

if __name__ == "__main__":
    file_path = "movie5.owl"
    graph = load_data(file_path)
    
    # Apply OWL inference
    graph = apply_inference(graph)
    
    # Take input from the user for included and excluded fields
    included_actors = input("Enter included actors (comma-separated, leave blank for any): ").split(",") if input else None
    excluded_actors = input("Enter excluded actors (comma-separated, leave blank for none): ").split(",") if input else []
    included_directors = input("Enter included directors (comma-separated, leave blank for any): ").split(",") if input else None
    excluded_directors = input("Enter excluded directors (comma-separated, leave blank for none): ").split(",") if input else []
    included_genres = input("Enter included genres (comma-separated, leave blank for any): ").split(",") if input else None
    excluded_genres = input("Enter excluded genres (comma-separated, leave blank for none): ").split(",") if input else []
    
    # Search films using SPARQL
    films = search_films_sparql(graph, included_actors, excluded_actors, included_directors, 
                                excluded_directors, included_genres, excluded_genres)
    
    # Display results
    display_films(films)
