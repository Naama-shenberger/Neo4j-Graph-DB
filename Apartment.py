'''Connection to database neo4j'''
from neo4j import GraphDatabase
graphdb=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Naamais12"))

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
