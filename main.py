import sqlite3 as lite
import sys

con = None

def getSQLiteVersion():
	try:
		con = lite.connect('installbase.db')
	
		cur = con.cursor()
		cur.execute('SELECT SQLITE_VERSION()')
	
		data = cur.fetchone()
	
		return "SQLite version: " + str(data)
	
	except lite.Error, e:

		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:

		if con:
			con.close()

def getInstallBaseCust():
	try:
		result = "Here are all of your customers:\n"
		con = lite.connect('installbase.db')
	
		cur = con.cursor()
		cur.execute('select distinct CS_CUSTOMER_NAME from tbl_installbase')
	
		rows = cur.fetchall()
	
		for row in rows:
			result += str(row[0]) + "\n"
	
		return result
		
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
	
		result = "Here are all of your VNX systems:\n"
		for row in rows:
			result += row[0] + "\n"
			result += row[1] + "\n"
			result += row[2] + "\n"
			
		return result
	
	except lite.Error, e:

		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:

		if con:
			con.close()

def getInstallBaseISILON():
	try:
		con = lite.connect('installbase.db')
	
		cur = con.cursor()
		cur.execute('select CS_CUSTOMER_NAME, PRODUCT_GROUP, ITEM_SERIAL_NUMBER from tbl_installbase where PRODUCT_GROUP like \'Isilon%\'')
	
		rows = cur.fetchall()
	
		result = "Here are all of your Isilon systems:\n"
		for row in rows:
			result += row[0] + "\n"
			result += row[1] + "\n"
			result += row[2] + "\n"
			
		return result
	
	except lite.Error, e:

		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:

		if con:
			con.close()
						

print getSQLiteVersion()
print getInstallBaseCust()
print getInstallBaseVNX()
print getInstallBaseISILON()
