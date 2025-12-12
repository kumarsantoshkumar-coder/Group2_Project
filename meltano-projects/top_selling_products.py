import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://pgadm2:Santa666@localhost:5432/bbb")

order_items = pd.read_sql("SELECT product_id FROM raw.olist_order_items_dataset", engine)
top_products = order_items['product_id'].value_counts().head(10)

print("\nTop-Selling Products (by number of items sold):")
print(top_products)
