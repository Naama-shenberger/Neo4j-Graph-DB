'''Connection to database neo4j'''
#https://github.com/neo4j/neo4j-python-driver/issues/509
from neo4j import GraphDatabase
#https://github.com/neo4j/neo4j-python-driver/issues/509
#uri = "bolt://localhost:7687"
from uri import graphdb

class Apartment:
    '''class Apartment'''
    def __init__(self,number,key=-1):
        '''A constructor that gets a number and key unique to each object (Initialized with zero)'''
        self.key=key
        self.number=number

def CreatApartmentNode(a):
    '''A function that accepts a Apartment-type object and builds a node with properties'''
    if(type(a)==Apartment):
      session = graphdb.session()
      q1 = "CREATE (N:Apartment {number:'" + a.number + "',key:'"+a.key+"'})"
      session.run(q1)
    else:
        print("The parameter you submitted is not Apartment-type object")
'''
  def _find_and_return_person(tx, person_name):
        query = (
            "MATCH (p:Person) "
            "WHERE p.name = $person_name "
            "RETURN p.name AS name"
        )
        result = tx.run(query, person_name=person_name)
        return [row["name"] for row in result]

'''
