from flask import Flask, jsonify
from neo4j import GraphDatabase

# neo4j driver connection
driver = GraphDatabase.driver(uri="bolt://54.236.55.139:7687", auth=("neo4j", "wingnuts-ringing-ponds"))
session = driver.session()
api = Flask(__name__)


@api.route("/reviewed", methods=["GET", "POST"])
def reviewedMoives():
    """A function that returns all nodes that have reviewed connection """
    try:
        results = session.run("MATCH (p:Person)-[r:REVIEWED]-(m:Movie) return p,r,m")
        data = results.data()
        return jsonify(data)

    except Exception as e:
        return str(e)


@api.route("/movie name/<string:movie_name>", methods=["GET", "POST"])
def actor(movie_name):
    """A function that receive a movie name and returns the actors who played in the movie (in a alphabet order)"""
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


@api.route("/birth place/<string:birth_place>", methods=["GET", "POST"])
def placeBirth(birth_place):
    try:
        """A function that gets a birth place and returns the names of people who were born in that place (using an indexer)"""
        session.run("""CREATE (p:Person {name: 'Alan Ruck',born:'1956',birth_place:'USA'})"""
                    """MATCH (p:Person), (m:Movie)
                       WHERE p.name = "Alan Ruck" and m.title = "Twister"
                       CREATE (p)-[a:ACTED_IN]->(m)"""
                    """CREATE INDEX ON :Person(birth_place)""", birth_place=birth_place)
        results = session.run("""MATCH (n:Person)
       USING INDEX n:Person(birth_place)
       WHERE n.place_birth = $birth_place
       RETURN n.name
        """, birth_place=birth_place)
        data = results.data()
        return jsonify(data)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    api.run(debug=True)
