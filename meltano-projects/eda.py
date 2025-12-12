import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Connect to your database
engine = create_engine("postgresql://pgadm2:Santa666@localhost:5432/bbb")

# Load data into a DataFrame
df = pd.read_sql("SELECT * FROM raw.olist_customers_dataset", engine)

# Plot customer counts by state
state_counts = df['customer_state'].value_counts()
state_counts.plot(kind='bar', figsize=(10,5), title='Customers by State')
plt.xlabel('State')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()