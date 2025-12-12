import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://pgadm2:Santa666@localhost:5432/bbb")

orders = pd.read_sql("SELECT order_id, order_purchase_timestamp FROM raw.olist_orders_dataset", engine)
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'], errors='coerce')
orders['order_month'] = orders['order_purchase_timestamp'].dt.to_period('M')
monthly_sales = orders.groupby('order_month').size().reset_index(name='num_orders')

print("\nMonthly Sales Trends:")
print(monthly_sales)


