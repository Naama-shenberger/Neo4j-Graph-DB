# Link to files
from Person import Person
from Person import createPersonNode
from Apartment import Apartment
from Apartment import createApartmentNode
from neo4j import GraphDatabase

# Connection to neo4j driver connection
from driver_connection import graphdb

# Data
Apartment_numbers = ['19', '20', 'Nan', 'Nan']
Names = ['Emma', 'Rechel', 'Monica', 'Chandler', 'Joey', 'Phebe', 'Ross']
Last_names = ['Green', 'Green', 'Geller', 'Bing', 'Tribbiani', 'Buffay', 'Geller']
Ages = ['1', '32', '32', '32', '32', '31', '34']
Genders = ['Female', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male']


def marriedRelationship(a_key, b_key):
    """A function that receives two nodes keys and connects the two nodes in a married relationship"""
    session = graphdb.session()
    session.run("MATCH (a:person {key: $a_key}), (b:person {key: $b_key})"
                "MERGE (a)-[:married_to]->(b)", a_key=a_key, b_key=b_key)


def livingRelationship(a_key, b_key):
    """A function that receives two nodes keys and connects the two nodes in a Living together relationship"""
    session = graphdb.session()
    session.run("MATCH (a:person {key: $a_key}), (b:Apartment {key: $b_key})"
                "MERGE (a)-[:Lives_in]->(b)", a_key=a_key, b_key=b_key)


def siblingRelationship(a_key, b_key):
    """A function that receives two nodes keys and connects the two nodes in a sibling relationship"""
    session = graphdb.session()
    session.run("MATCH (a:person {key: $a_key}), (b:person {key: $b_key})"
                "MERGE (a)-[:Sibling]->(b)", a_key=a_key, b_key=b_key)


def parentRelationship(a_key, b_key):
    """A function that receives two nodes keys and connects the two nodes in a parent relationship"""
    session = graphdb.session()
    session.run("MATCH (a:person {key: $a_key}), (b:person {key: $b_key})"
                "MERGE (a)-[:Parent_of]->(b)", a_key=a_key, b_key=b_key)


def reset_db():
    """Remove all nodes and relationships from the database"""
    session = graphdb.session()
    session.run('MATCH (n) DETACH DELETE n')


reset_db()  # reset data base
object_list = []  # A list of all objects so that they are easy to access
for i in range(len(Names)):
    p = Person(Names[i], Last_names[i], Ages[i], Genders[i])  # Build an object person type
    p.key = "_" + str(id(p))  # A unique number is assigned to a key field
    object_list.append(p)
    createPersonNode(p)  # Create Node type Person

for i in range(len(Apartment_numbers)):
    a = Apartment(Apartment_numbers[i])  # Build an object Apartment type
    a.key = "_" + str(id(a))  # A unique number is assigned to a key field
    object_list.append(a)
    createApartmentNode(a)  # Create Node type Apartment

'''Createing a relationship'''
print("marriedRelationship")
marriedRelationship(object_list[2].key, object_list[3].key)
marriedRelationship(object_list[3].key, object_list[2].key)

print("living Relationship")
livingRelationship(object_list[1].key, object_list[8].key)
livingRelationship(object_list[5].key, object_list[10].key)
livingRelationship(object_list[6].key, object_list[9].key)
livingRelationship(object_list[2].key, object_list[8].key)
livingRelationship(object_list[3].key, object_list[7].key)
livingRelationship(object_list[4].key, object_list[7].key)

print("sibling Relationship")
siblingRelationship(object_list[6].key, object_list[2].key)
siblingRelationship(object_list[2].key, object_list[6].key)

print("parent of Relationship")
parentRelationship(object_list[6].key, object_list[0].key)
parentRelationship(object_list[1].key, object_list[0].key)
graphdb.close()  # close the driver connection