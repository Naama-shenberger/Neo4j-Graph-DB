from flask import Flask, jsonify
from neo4j import GraphDatabase

# neo4j driver connection
driver = GraphDatabase.driver(uri="bolt://54.236.55.139:7687", auth=("neo4j", "wingnuts-ringing-ponds"))
session = driver.session()
api = Flask(__name__)


@api.route("/reviewed", methods=["GET"])
def reviewedMoives():
    """A function that returns all nodes that have reviewed connection """
    try:
        results = session.run("MATCH (p:Person)-[r:REVIEWED]-(m:Movie) return p,r,m")
        data = results.data()
        return jsonify(data)

    except Exception as e:
        return str(e)


@api.route("/movie_name/<string:movie_name>", methods=["GET"])
def actor(movie_name):
    """A function that receive a movie name and returns the actors who played in the movie (in a alphabet order)"""
    try:
        results = session.run("""MATCH(m: Movie {title:$movie_name}) < -[: ACTED_IN]-(actor) RETURN  actor.name order by 
        actor.name """, movie_name=movie_name)
        data = results.data()
        return jsonify(data)
    except Exception as e:
        return str(e)


@api.route("/MATCH/<string:name>&<string:movie>", methods=["GET"])
def relationshipType(name, movie):
    """A function that receives a movie name and name and returns the type of connection between the nodes"""
    try:
        results = session.run("""MATCH (p:Person{name:$name})-[r]->(m:Movie{title:$movie}) RETURN type(r)""", name=name,
                              movie=movie)
        data = results.data()
        return jsonify(data)
    except Exception as e:
        return str(e)


@api.route("/born/<int:born>", methods=["GET"])
def born_year(born):
    try:
        """A function that gets a born year and returns the names of People born that year (using an indexer)
        There is an index used but in principle it is used when there are different property nodes
        """
        session.run("""CREATE INDEX myIndex IF NOT EXISTS FOR (p:Person) ON (p.born)""",born=born)
        results = session.run("""MATCH (n:Person)
       USING INDEX n:Person(born)
       WHERE n.born = $born
       RETURN n.name
        """, born=born)
        data = results.data()
        return jsonify(data)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    api.run(debug=True)
