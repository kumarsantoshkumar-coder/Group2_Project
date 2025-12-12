import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://pgadm2:Santa666@localhost:5432/bbb")

orders = pd.read_sql("SELECT customer_id, order_id FROM raw.olist_orders_dataset", engine)
customer_order_counts = orders.groupby('customer_id').size().reset_index(name='num_orders')

def segment(n):
    if n == 1:
        return 'New'
    elif n <= 4:
        return 'Returning'
    else:
        return 'Loyal'

customer_order_counts['segment'] = customer_order_counts['num_orders'].apply(segment)

print("\nCustomer Segmentation by Purchase Behavior:")
print(customer_order_counts['segment'].value_counts())
