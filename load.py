import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:12345678@localhost/sql_course"
)

df = pd.read_csv("/Users/meetshah/Downloads/all_folders/csv_files/skills_job_dim.csv")
df.to_sql("skills_job_dim", engine, if_exists="append", index=False)
