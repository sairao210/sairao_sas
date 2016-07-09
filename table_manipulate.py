import sqlite3
import datetime
conn = sqlite3.connect("./DataBase/attendance.db")
c = conn.cursor()
now = datetime.datetime.now()
date = str(now.date())
# num = '13EE10027'
# c.execute("UPDATE example SET "+'['+date+']'+"=(1) WHERE roll=?",(num,) )
# conn.commit()
#########################
#delete coloumn
#############
# c.execute('BEGIN TRANSACTION;')
# c.execute('CREATE TABLE t1_backup(roll)')
# c.execute('INSERT INTO t1_backup SELECT roll FROM example')
# c.execute('DROP TABLE example')
# c.execute('ALTER TABLE t1_backup RENAME TO example')

# c.execute("INSERT INTO example (roll) VALUES ('13EE10027')")
# conn.commit()
# st = ''
# for row in c.execute("SELECT roll FROM example WHERE "+'['+date+']'+"=?", (1,)):
#     for item in row:
#         st+=str(item)+'\t'
#     st+='\n'
# print st



###########################################
for row in c.execute("SELECT * FROM example"):
    print row
