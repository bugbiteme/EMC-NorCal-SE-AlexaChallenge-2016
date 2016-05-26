import sqlite3 as lite
import sys

##############################################################
# This just gives you the version of sqlite
##############################################################

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
			
##############################################################			
# this will give you a list of customers from your install base
##############################################################
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
			
##############################################################
# this will give you the install base for a particular customer
##############################################################
def getInstallBaseVNX():
	# type: () -> object
	try:
		con = lite.connect('installbase.db')
	
		cur = con.cursor()
		cur.execute('select CS_CUSTOMER_NAME, PRODUCT_GROUP, ITEM_SERIAL_NUMBER from tbl_installbase where PRODUCT_GROUP like \'VNX%\'')
	
		rows = cur.fetchall()
	
		result = ""
		result = "You have " + str(len(rows)) + " VNX systems in your install base:\n"
		for row in rows:
			result += "location: " + row[0] + ".\n"
			result += "model: " + row[1] + ".\n"
			result += "serial number: " + row[2] + ".\n"
			
		return result
	
	except lite.Error, e:

		print "Error %s:" % e.args[0]
		sys.exit(1)
	
	finally:
		if con:
			con.close()

# ############################################################ #
# ################## END OF FUNCTION DEFS #################### #
# ############################################################ #
