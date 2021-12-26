'''Connection to database neo4j'''
from neo4j import GraphDatabase
graphdb=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Naamais12"))

class Person:
    '''class person'''
    def __init__(self, name, age,gender,key=-1):
        '''A constructor that gets a name, age, gender, and key unique to each object (Initialized with zero)'''
        self.name = name
        self.age = age
        self.gender = gender
        self.key=key
def CreatPersonNode(p):
    '''A function that accepts a person-type object and builds a node with properties'''
    if(type(p)==Person):
     session = graphdb.session()
     q1 = "CREATE (N:person {name:'"+p.name+"',age:'"+p.age+"', gender:'"+p.gender+"',key:'"+p.key+"'})"
     session.run(q1)
    else:
        print("The parameter you submitted is not person-type object")
