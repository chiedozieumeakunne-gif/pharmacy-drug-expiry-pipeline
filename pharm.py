#imports
import pandas as pd
from datetime import datetime
from toolkit import mysqlconnector
from toolkit import createsqlengine

#SQL addresses
engine = createsqlengine()
connection = mysqlconnector()


#processing
query = "SELECT * FROM drug"    
df = pd.read_sql(query, connection)
today = pd.Timestamp.today()
df["Expiry_Date"] = pd.to_datetime(df["Expiry_Date"])
difference = df["Expiry_Date"] - today
df["Days_Left"] = difference.dt.days

#conversion of python result to sql
df.to_sql(
    "drug_processed",
    engine,
    if_exists="replace",
    index=False)
print(df)

connection.close()