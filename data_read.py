from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://user:pass@localhost/db_name')
df = pd.read_csv('../fant_o_players.csv')
df.to_sql('pandas_db', engine)