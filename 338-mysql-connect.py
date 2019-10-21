# Connecting to a MySQL server
import mysql.connector
# first do "pip3 install mysql.connector"

connect = mysql.connector.connect(
    host = 'ensembldb.ensembl.org',
    # public server
    user = 'anonymous',
    passwd = ''
)

cursor = connect.cursor()
cursor.execute('select now()')
# get current time from a server

print(cursor.fetchall()) # list of tuples
