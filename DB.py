
from neo4j import GraphDatabase
graphdb=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Naamais12"))
session=graphdb.session()
q1="MATCH (x) return (x)"
nodes=session.run(q1)
'''
for node in nodes:
    print(node)
'''
def searchNodes():
    session=graphdb.session()
    q1="MATCH (x) return (x)"
    nodes=session.run(q1)
    for node in nodes:
        print(node)
#searchNodes()
def CreatPersonNode(p):
    session = graphdb.session()
    q1 = "CREATE (N:person {name:'"+p.name+"',age:'"+p.age+"', gender:'"+p.gender+"'})"
    session.run(q1)
    q2="MATCH(x:person) return (x)"
    nodes = session.run(q2)
    for node in nodes:
        print(node)
def CreatApartmentNode(a):
    session = graphdb.session()
    q1 = "CREATE (N:Apartment {number:'" + a.number + "'})"
    session.run(q1)
    q2 = "MATCH(x:Apartment) return (x)"
    nodes = session.run(q2)
    for node in nodes:
        print(node)
class Person:
    def __init__(self, name, age,gender):
        self.name = name
        self.age = age
        self.gender = gender
class Apartment:
    def __init__(self,number):
        self.number=number


Names=['Emma','Rechel','Monica','Chandler','Joey','Phoebe','Ross']
Ages=['1','32','32','32','32','31','34']
Genders=['Female','Female','Female','Male','Male','Female','Male']
'''
for i in range(len(Names)):
    CreatPersonNode(Person(Names[i],Ages[i],Genders[i]))
Number_Apartments=['19','20','Nan','Nan']
for i in range(len(Number_Apartments)):
    CreatApartmentNode(Apartment(Number_Apartments[i]))
'''
def  marriedRelationship(a_name,b_name):
     session = graphdb.session()
     q2="MATCH(a:person{'"+a_name+"'}),(a:person{'"+b_name+"'})"
     session.run(q2)
     q3 = "MERGE(" + q1 + ")-[m1:married_to]->(" + q2 + ")"
     nodes = session.run(q3)
     for node in nodes:
         print(node)


def create_friendship(a_name, b_name):
    session = graphdb.session()
    q1 = "MERGE(MATCH(a:person{'" + a_name + "'}),(a:person{'" + b_name + "'})) return a,b"
    nodes = session.run(q1)
    for node in nodes:
        print(node)

create_friendship("Monica","Chandler")

'''
def Live_inRelationship:
    "ff"
def ParentRelationship:

def SiblingRelationship:
'''