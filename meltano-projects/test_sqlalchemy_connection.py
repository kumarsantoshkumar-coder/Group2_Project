from sqlalchemy import create_engine

# Use your Meltano connection string
engine = create_engine("postgresql://pgadm2:Santa666@localhost:5432/bbb")

# Test the connection and print table names
with engine.connect() as connection:
    result = connection.execute("SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema NOT IN ('pg_catalog', 'information_schema');")
    for row in result:
        print(row)
