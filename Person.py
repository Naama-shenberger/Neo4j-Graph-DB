# neo4j driver connection
from driver_connection import graphdb

session = graphdb.session()


class Person:
    """class person"""

    def __init__(self, name, last_name, age, gender, key=-1):
        """A constructor that gets a name,last name,age, gender, and a unique key to each object (Initialized with zero)"""
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.key = key


def createPersonNode(p):
    """A function that accepts a person-type object and builds a node with properties"""
    if type(p) == Person:
        name, last_name, age, gender, key = p.name, p.last_name, p.age, p.gender, p.key
        session.run("CREATE (N:person {name:$name, last_name:$last_name, age:$age, gender:$gender, key:$key})",
                    name=name, last_name=last_name, age=age, gender=gender, key=key)
    else:
        print("The parameter you submitted is not person-type object")
