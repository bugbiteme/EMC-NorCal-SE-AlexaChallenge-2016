import web
import sql_wrapper as sql



urls = ('/hello', 'Index')


app = web.application(urls, globals())

render = web.template.render('templates/')


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
            greeting = "Hello, %s" % form.name

        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()



