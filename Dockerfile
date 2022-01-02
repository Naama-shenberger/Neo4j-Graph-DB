FROM python:3.7

ADD driver_connection.py .
ADD Graph_friends.py .
ADD Person.py .
ADD Apartment.py .

RUN pip install neo4j

CMD ["python","./GraphFriends.py"]