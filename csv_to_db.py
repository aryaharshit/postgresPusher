import pandas as pd 
import json
from sqlalchemy import create_engine
import sys

user = sys.argv[1]
password = sys.argv[2]
host = sys.argv[3]
port = sys.argv[4]
dbname = sys.argv[5]

src_base_dir = "C:/Study/Data Eng/postgresPusher/DATA/retail_db"
file_json = open(f"{src_base_dir}/schemas.json")
schema = json.load(file_json)


def get_column_name(schema, ds_name):
    column_details = schema[ds_name]
    column_names = list(map(lambda x: x.get('column_name'), column_details))
    return(column_names)


def csv_to_df(ds_name):
    columns = get_column_name(schema, ds_name)
    df = pd.read_csv(f"{src_base_dir}/{ds_name}/part-00000",
                     names=columns,
                     index_col=columns[1])
    return df


def dev_engine(user, password, host, port, dbname):
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
    return engine


def to_db(ds_names  = None):
    engine = dev_engine(user, password, host, port, dbname)
    if not ds_names:
        ds_names = schema.keys()
    for ds_name in ds_names:
        df = csv_to_df(ds_name)
        df.to_sql(ds_name, con=engine, if_exists='replace') 

to_db()