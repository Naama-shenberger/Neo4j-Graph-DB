'''Connection to database neo4j'''
from neo4j import GraphDatabase
#uri = "bolt://localhost:7687"
uri = "neo4j+s://1d0a616c.databases.neo4j.io"
#graphdb=GraphDatabase.driver(uri,auth=("neo4j","gmnnjaal3rzkRdOuAD8QHN1EAwwyzhNMiid85MTIN0c"))
from uri import graphdb
class Person:
    '''class person'''
    def __init__(self, name,last_name ,age,gender,key=-1):
        '''A constructor that gets a name,last name,age, gender, and key unique to each object (Initialized with zero)'''
        self.name = name
        self.last_name=last_name
        self.age = age
        self.gender = gender
        self.key=key
def CreatPersonNode(p):
    '''A function that accepts a person-type object and builds a node with properties'''
    if(type(p)==Person):
     session = graphdb.session()
     q1 = "CREATE (N:person {name:'"+p.name+"',last_name:'"+p.last_name+"',age:'"+p.age+"', gender:'"+p.gender+"',key:'"+p.key+"'})"
     session.run(q1)
    else:
        print("The parameter you submitted is not person-type object")
#graphdb.close()