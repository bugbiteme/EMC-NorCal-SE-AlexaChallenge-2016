import sqlite3 as lite
import sys

con = None

def getSQLiteVersion():
	try:
		con = lite.connect('installbase.db')
	
		cur = con.cursor()
		cur.execute('SELECT SQLITE_VERSION()')
	
		data = cur.fetchone()
	
		print "SQLite version: %s" % data
	
	except lite.Error, e:

		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:

		if con:
			con.close()

def getInstallBaseCust():
	try:
		con = lite.connect('installbase.db')
	
		cur = con.cursor()
		cur.execute('select distinct CS_CUSTOMER_NAME from tbl_installbase')
	
		rows = cur.fetchall()
	
		print "Here are all of your customers:"
		for row in rows:
			print row[0]
	
	except lite.Error, e:

		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:

		if con:
			con.close()

def getInstallBaseVNX():
	try:
		con = lite.connect('installbase.db')
	
		cur = con.cursor()
		cur.execute('select CS_CUSTOMER_NAME, PRODUCT_GROUP, ITEM_SERIAL_NUMBER from tbl_installbase where PRODUCT_GROUP like \'VNX%\'')
	
		rows = cur.fetchall()
	
		print "Here are all of your customers:"
		for row in rows:
			print row[0]
			print row[1]
			print row[2]
	
	except lite.Error, e:

		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:

		if con:
			con.close()
						

getSQLiteVersion()
getInstallBaseCust()
getInstallBaseVNX()
