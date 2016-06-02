import web
import json
import sql_wrapper as sql



urls = ('/ibResponse.json', 'Index')


app = web.application(urls, globals())

class Index(object):
    def GET(self):
        form = web.input(name="Nobody")
        
        if form.name == "version":
            greeting = sql.getSQLiteVersion()
        elif form.name == "ib_sites":
            greeting = sql.getInstallBaseCust()
        elif form.name == "ib_vnx":
        	greeting = sql.getInstallBaseVNX()
        else:
            greeting = "{\"text\": \"invalid parameter\"}"

        return greeting

if __name__ == "__main__":
    app.run()



