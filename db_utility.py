import sqlite3
import logging
import pandas as pd


def get_db_connection():
	conn = ''
	try:
		conn = sqlite3.connect('test.db')
	except Exception as e:
		logging.error(f"DB connection Error: {e}")
	return conn

def create_table():
	try:
		conn = sqlite3.connect('test.db')
		conn.execute('''CREATE TABLE IF NOT EXISTS REPORTS
			(ID INTEGER PRIMARY KEY AUTOINCREMENT,
			REQUESTED_BY	TEXT    NOT NULL,
			KPI		CHAR(100)     NOT NULL,
			TYPE	CHAR(100)     NOT NULL,
			PRIORITY	CHAR(50))''')
		logging.debug("Table created")
	except Exception as e:
		logging.error(f"DB Table creation Error: {e}")
	finally:
		conn.close()

def add_report(requested_by, kpi, type, priority):
	conn = get_db_connection()
	if conn:
		conn.execute("INSERT INTO REPORTS (REQUESTED_BY,KPI,TYPE,PRIORITY) \
	      VALUES (?, ?, ?, ?)", (requested_by,kpi, type, priority));
		print("Report request added")
		conn.commit()
		conn.close()

def get_records():
	conn = get_db_connection()
	if conn:
		cursor = conn.execute("SELECT * from REPORTS")
		#print(len(cursor.fetchall()))
		count = len(cursor.fetchall())
		conn.close()
	return count

def all_records():
	conn = get_db_connection()
	if conn:
		df = pd.read_sql_query("SELECT REQUESTED_BY,KPI, TYPE, PRIORITY FROM REPORTS", conn)
		#print(df)
		conn.close()
		return df, df.shape[0]


if __name__ == '__main__':
	#create_table()
	#add_report("Akash", "Uptime", "Raw", "Low")
	#add_report("Kumar", "Uptime", "Raw", "Low")
	get_records()
	all_records()