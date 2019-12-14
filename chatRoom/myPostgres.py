import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(user='postgres', password='48235015', host='localhost', port=5432)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
curs = conn.cursor()

curs.execute('CREATE DATABASE myMapsa')

conn.commit()