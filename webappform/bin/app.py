import web
import json
import sql_wrapper as sql



urls = ('/ibResponse.json', 'Index')


app = web.application(urls, globals())

class Index(object):
    def GET(self):
        form = web.input(name="Nobody")
        web.header('Content-Type', 'application/json')
        
        if form.name == "version":
            greeting = sql.getSQLiteVersion()
        elif form.name == "ib_sites":
            return json.dumps(sql.getInstallBaseCust())
        elif form.name == "ib_vnx":
        	return json.dumps(sql.getInstallBaseVNX())
        else:
            return json.dumps({"text": "invalid parameter"})

if __name__ == "__main__":
    app.run()



