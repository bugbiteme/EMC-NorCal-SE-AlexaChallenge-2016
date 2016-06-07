import web
import json
import sql_wrapper as sql
from datetime import datetime


urls = ('/ibResponse.json', 'Index')


app = web.application(urls, globals())

class Index(object):
    def GET(self):
        form = web.input(name="Nobody")
        web.header('Content-Type', 'application/json')

        
        i = datetime.now()
        
        print "[" + i.strftime('%d/%m/%Y %H:%M:%S') + "] - - Requesting: " + form.name
        
        if form.name == "version":
            greeting = sql.getSQLiteVersion()
        elif form.name == "sites":
            return json.dumps(sql.getInstallBaseCust())
        elif form.name == "vnx":
        	return json.dumps(sql.getInstallBaseVNX())
        elif form.name == "isilon":
        	return json.dumps(sql.getInstallBaseISILON())
        else:
            return json.dumps({"text": "nobody has a " + form.name })

if __name__ == "__main__":
    app.run()



