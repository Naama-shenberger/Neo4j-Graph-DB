# neo4j driver connection
from driver_connection import graphdb

session = graphdb.session()


class Apartment:
    """class Apartment"""

    def __init__(self, number, key=-1):
        """A constructor that receive a number and a unique key to each object (Initialized with zero)"""
        self.key = key
        self.number = number


def createApartmentNode(a):
    """A function that accepts a Apartment-type object and builds a node with properties"""
    if type(a) == Apartment:
        key, number = a.key, a.number
        session.run("CREATE (N:Apartment {number:$number,key:$key})", number=number, key=key)
    else:
        print("The parameter you submitted is not Apartment-type object")
