This project demonstrates how to integrate the Neo4j Graph Database with Python for creating, managing, and querying graph-based data. The example showcases how to represent real-world entities such as people and cities as nodes, and relationships such as "lives in" and "connected by roads" using Cypher queries.

Features
Node Creation: Add entities like people and cities as nodes in the Neo4j graph database.
Relationship Management: Define relationships between nodes, such as where people live and how cities are connected.
Cypher Queries: Query the data for insights, including listing people living in specific cities and city connections.
Python Integration: Use Python scripts to automate graph creation and querying via the Neo4j Python driver.
Project Overview
The project creates a simple graph structure:

People Nodes: Representing individuals (e.g., Alice, Bob, Charlie).
City Nodes: Representing cities (e.g., New York, Los Angeles, Chicago).
Relationships:
LIVES_IN: Connecting people to the cities they reside in.
ROAD: Connecting cities that are linked by roads.
The data is visualized and queried in the Neo4j Browser for verification.

Technologies Used
Neo4j: A powerful graph database for managing relationships between entities.
Python: For connecting to Neo4j and executing Cypher queries.
Cypher: A query language used to interact with Neo4j.
