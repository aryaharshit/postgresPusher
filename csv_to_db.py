import pandas as pd 
import json
from sqlalchemy import create_engine
from dotenv.main import load_dotenv
import os

load_dotenv()
user = os.environ['DB_USER']
password =os.environ['DB_PASSWORD']
host = os.environ['DB_HOST']
port = os.environ['DB_PORT']
dbname = os.environ['DB_NAME']
src_base_dir = os.environ['DIRECTORY']

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