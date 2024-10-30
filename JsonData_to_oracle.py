import cx_Oracle
import pandas as pd


# Oracle connection
ora_connection = cx_Oracle.connect("", "", "")
ora_cursor = ora_connection.cursor()
print("OracleDB connection ok")
print()


document_list = [{"name": "pantea", "last_name": "tourang", "age": "18", "gender": "f", "city": "shirza"},
                 {"name": "yahya", "last_name": "maleki", "age": "19", "gender": "m", "city": "abadan"},
                 {"name": "ali", "last_name": "shirazi", "age": "23", "gender": "m"},
                 {"name": "lale", "last_name": "sarabi", "age": "99", "city": "ghom"},
                 {"name": "shirin", "last_name": "panahi", "gender": "f", "city": "langerood"},
                 ]
df = pd.DataFrame(document_list)
print(df)
print()

# initiate empty data frame
mydf = pd.DataFrame()

for i, r in df.iterrows():
    name = '' if "name" not in df.keys() or str(r["name"]) == "nan" else str(r["name"])
    last_name = '' if "last_name" not in df.keys() or str(r["last_name"]) == "nan" else str(r["last_name"])
    age = None if "age" not in df.keys() or str(r["age"]) == "nan" else r["age"]
    gender = '' if "gender" not in df.keys() or str(r["gender"]) == "nan" else str(r["gender"])
    city = '' if 'city' not in df.keys() or str(r["city"]) == "nan" else str(r["city"])


    t = {'a': name, 'b': last_name, 'c': age, 'd': gender, 'e': city}

    t_df = pd.DataFrame([t])
    mydf = pd.concat([mydf, t_df], ignore_index=True)


print(mydf)
oracle_query = 'insert into jasondata_to_oracle values (:1, :2, :3, :4, :5)'
ora_cursor.executemany(oracle_query, mydf.values.tolist())
ora_connection.commit()
