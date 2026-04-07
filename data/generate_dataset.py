import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

rows = 500001

products = ["Laptop","Phone","Tablet","Headphones","Camera"]
regions = ["Texas","California","New York","Florida","Illinois"]

start_date = datetime(2023,1,1)

data = []

for i in range(rows):

    date = start_date + timedelta(days=random.randint(0,365))

    product = random.choice(products)

    region = random.choice(regions)

    quantity = random.randint(1,5)

    price = random.randint(50,1500)

    revenue = quantity * price

    data.append([i,date,product,region,quantity,price,revenue])


df = pd.DataFrame(data,columns=[
    "transaction_id",
    "date",
    "product",
    "region",
    "quantity",
    "price",
    "revenue"
])

df.to_csv("data/transactions_raw.csv",index=False)

print("Dataset generated successfully")