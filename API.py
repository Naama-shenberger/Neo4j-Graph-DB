from flask import Flask,jsonify
from neo4j import GraphDatabase

driver = GraphDatabase.driver(uri="bolt://54.236.55.139:7687", auth=("neo4j","wingnuts-ringing-ponds" ))
session = driver.session()
api = Flask(__name__)


@api.route("/reviewed")
def reviewedMoives():
    """A function that returns the nodes where there is a reviewed connection """
    try:
        results = session.run("MATCH (p:Person)-[r:REVIEWED]-(m:Movie) return p,r,m")
        data = results.data()
        return jsonify(data)

    except Exception as e:
        return str(e)


@api.route("/movie name/<string:movie_name>", methods=["GET", "POST"])
def actor(movie_name):
    """A function gets a movie name and returns the actors who played in the movie (in a alphabet order)"""
    try:
        results = session.run("""MATCH(m: Movie {title:$movie_name}) < -[: ACTED_IN]-(actor) RETURN  actor.name order by 
        actor.name """, movie_name=movie_name)
        data = results.data()
        return jsonify(data)
    except Exception as e:
        return str(e)


@api.route("/MATCH/<string:name>&<string:movie>", methods=["GET", "POST"])
def relationshipType(name, movie):
    """A function that receives a movie name and name and returns the type of connection between the nodes"""
    try:
        results = session.run("""MATCH (p:Person{name:$name})-[r]->(m:Movie{title:$movie}) RETURN type(r)""", name=name,
                              movie=movie)
        data = results.data()
        return jsonify(data)
    except Exception as e:
        return str(e)


@api.route("/Place birth/<string:place_birth>", methods=["GET", "POST"])
def placeBirth(place_birth):
    try:
        """A function that gets a place birth and returns the names of people who were born in that place (using an indexer)"""
        session.run("""CREATE INDEX ON :Person(place_birth)""", place_birth=place_birth)
        results = session.run("""MATCH (n:Person)
       USING INDEX n:Person(place_birth)
       WHERE n.place_birth = $place_birth
       RETURN n.name
        """, place_birth=place_birth)
        data = results.data()
        return jsonify(data)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    api.run(debug=True)


