# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:12:43 2017

@author: cognsrj
"""

import pymssql
conn = pymssql.connect(server='10.101.13.14', user='fasttrack', password='P@ssw0rdP@ssw0rd', database='test_db')
cursor = conn.cursor()
query1 = """DROP TABLE IF EXISTS phone_records
create table phone_records(
Cust_ID int NOT NULL PRIMARY KEY,
Cust_Name VARCHAR(100) NOT NULL,
Phone_Record VARCHAR(max)
CONSTRAINT [Phone_Record must be formatted as JSON array]
CHECK ( ISJSON(Phone_Record)>0 )
)"""
cursor.execute(query1)
cursor.executemany(
"INSERT INTO phone_records VALUES (%d, %s, %s)",
[(1, 'John Smith', '
{"phone_number": "+45 55 66 77 88", "duration": "107"}
'),
(2, 'Jane Doe', '
{"phone_number": "+45 55 66 77 95", "duration": "87"}
'),
(3, 'Mike T.', '
{"phone_number": "+45 55 66 77 64", "duration": "110"}
')])
conn.commit()
conn.close()