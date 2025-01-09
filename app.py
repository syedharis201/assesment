from neo4j import GraphDatabase

# Create a connection to the Neo4j database
uri = "bolt://localhost:7687"
user = "neo4j"
password = "11111111"

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self):
        self.driver.close()

# Instantiate the connection
conn = Neo4jConnection(uri=uri, user=user, password=password)

# Function to create new sample data (people and cities)
def create_new_sample_data(conn):
    session = conn.driver.session()

    # Create nodes for People and Cities
    session.run("CREATE (p:Person {name: 'Alice', age: 28})")
    session.run("CREATE (p:Person {name: 'Bob', age: 32})")
    session.run("CREATE (p:Person {name: 'Charlie', age: 25})")
    
    session.run("CREATE (c:City {name: 'New York'})")
    session.run("CREATE (c:City {name: 'Los Angeles'})")
    session.run("CREATE (c:City {name: 'Chicago'})")

    # Create relationships between People and Cities
    session.run("""
        MATCH (p:Person {name: 'Alice'}), (c:City {name: 'New York'})
        CREATE (p)-[:LIVES_IN]->(c)
    """)
    
    session.run("""
        MATCH (p:Person {name: 'Bob'}), (c:City {name: 'Los Angeles'})
        CREATE (p)-[:LIVES_IN]->(c)
    """)
    
    session.run("""
        MATCH (p:Person {name: 'Charlie'}), (c:City {name: 'Chicago'})
        CREATE (p)-[:LIVES_IN]->(c)
    """)

    # Create ROAD relationships between cities
    session.run("""
        MATCH (c1:City {name: 'New York'}), (c2:City {name: 'Los Angeles'})
        CREATE (c1)-[:ROAD]->(c2)
    """)
    
    session.run("""
        MATCH (c1:City {name: 'Los Angeles'}), (c2:City {name: 'Chicago'})
        CREATE (c1)-[:ROAD]->(c2)
    """)

    session.run("""
        MATCH (c1:City {name: 'Chicago'}), (c2:City {name: 'New York'})
        CREATE (c1)-[:ROAD]->(c2)
    """)

    session.close()

# Function to query new data (people and cities)
def query_new_data(conn):
    session = conn.driver.session()

    # Query all people and the cities they live in
    result = session.run("""
        MATCH (p:Person)-[:LIVES_IN]->(c:City)
        RETURN p.name AS person, c.name AS city
    """)

    print("People and their Cities:")
    for record in result:
        print(f"{record['person']} lives in {record['city']}")

    # Query the cities connected by roads
    result = session.run("""
        MATCH (c1:City)-[:ROAD]->(c2:City)
        RETURN c1.name AS city1, c2.name AS city2
    """)

    print("\nCities connected by roads:")
    for record in result:
        print(f"{record['city1']} is connected to {record['city2']}")

    session.close()

# Call the function to create new data
create_new_sample_data(conn)

# Query and print new results
query_new_data(conn)

# Close the connection
conn.close()
