import sqlite3
from sqlite3 import OperationalError

conn = sqlite3.connect('us_cities.db')
c = conn.cursor()

sql_command = """SELECT US_CITIES.ID, US_STATES.STATE_CODE, US_STATES.STATE_NAME, US_CITIES.CITY, US_CITIES.COUNTY FROM US_STATES INNER JOIN US_CITIES ON US_STATES.ID = US_CITIES.ID_STATE ORDER BY US_CITIES.ID ASC INTO OUTFILE 'US_CITIES.csv' FIELDS TERMINATED BY ';' ECNLOSED BY '' LINES TERMINATED BY '\n';"""

c.execute(sql_command)

#fd = open('us_cities.sql')
#sqlFile = fd.read()
#fd.close()



#sqlCommands = sqlFile.split(',')


#for command in sqlCommands:
#    try:
#        c.execute(command)
#    except OperationalError, msg:
#        print("command skipped: ", msg)
