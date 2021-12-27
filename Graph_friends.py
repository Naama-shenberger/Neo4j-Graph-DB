
#https://neo4j.com/developer/cypher/querying/
from Person import Person
from Apartment import Apartment
from Person import CreatPersonNode
from Apartment import CreatApartmentNode
from neo4j import GraphDatabase
graphdb=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Naamais12"))

#Data
Apartment_numbers=['19','20','Nan','Nan']
Names=['Emma','Rechel','Monica','Chandler','Joey','Phebe','Ross']
Last_names=['Green','Green','Geller','Bing','Tribbiani','Buffay','Geller']
Ages=['1','32','32','32','32','31','34']
Genders=['Female','Female','Female','Male','Male','Female','Male']

def marriedRelationship(a_key,b_key):
    '''A function that receives two nodes keys and connects the two nodes in a married relationship'''
    session = graphdb.session()
    session.run("MATCH ("+a_key+":person {key:'"+a_key+"'}), ("+b_key+":person {key:'"+b_key+"'})"
                "MERGE ("+a_key+")-[:married_to]->("+b_key+")")

def livingRelationship(a_key,b_key):
    '''A function that receives two nodes keys and connects the two nodes in a Living together relationship'''
    session = graphdb.session()
    session.run("MATCH ("+a_key+":person {key:'"+a_key+"'}), ("+b_key+":Apartment {key:'"+b_key+"'})"
                "MERGE ("+a_key+")-[:Lives_in]->("+b_key+")")
def siblingRelationship(a_key,b_key):
    '''A function that receives two nodes keys and connects the two nodes in a sibling relationship'''
    session = graphdb.session()
    session.run("MATCH (" + a_key + ":person {key:'" + a_key + "'}), (" + b_key + ":person {key:'" + b_key + "'})"
                "MERGE (" + a_key + ")-[:Sibling]->(" + b_key + ")")
def parentRelationship(a_key,b_key):
    '''A function that receives two nodes keys and connects the two nodes in a parent relationship'''
    session = graphdb.session()
    session.run("MATCH (" + a_key + ":person {key:'" + a_key + "'}), (" + b_key + ":person {key:'" + b_key + "'})"
                "MERGE (" + a_key + ")-[:Parent_of]->(" + b_key + ")")
def reset_db():
    "Remove all nodes and relationships from the database"
    session=graphdb.session()
    session.run('MATCH (n) DETACH DELETE n')

reset_db()
object_list=[]#A list of all objects so that they are easy to access
for i in range(len(Names)):
    p=Person(Names[i],Last_names[i],Ages[i],Genders[i])#Build an object person type
    p.key="_"+str(id(p))#A unique number is assigned to a key field
    object_list.append(p)
    CreatPersonNode(p)#Creat Node type Person

for i in range(len(Apartment_numbers)):
    a=Apartment(Apartment_numbers[i])#Build an object Apartment type
    a.key="_"+str(id(a))#A unique number is assigned to a key field
    object_list.append(a)
    CreatApartmentNode(a)#Creat Node type Apartment

'''Calling functions'''
marriedRelationship(object_list[2].key,object_list[3].key)
marriedRelationship(object_list[3].key,object_list[2].key)

livingRelationship(object_list[1].key,object_list[8].key)
livingRelationship(object_list[5].key,object_list[10].key)
livingRelationship(object_list[6].key,object_list[9].key)
livingRelationship(object_list[2].key,object_list[8].key)
livingRelationship(object_list[3].key,object_list[7].key)
livingRelationship(object_list[4].key,object_list[7].key)

siblingRelationship(object_list[6].key,object_list[2].key)
siblingRelationship(object_list[2].key,object_list[6].key)

parentRelationship(object_list[6].key,object_list[0].key)
parentRelationship(object_list[1].key,object_list[0].key)
