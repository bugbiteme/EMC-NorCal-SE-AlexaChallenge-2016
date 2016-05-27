# webappform
This is the structure for the web api which will accept url parameters.
It is using the web.py framework

#prereqs

You will need the following in order to make this work:
 - pip from http://pypi.python.org/pypi/pip
 - distribute from http://pypi.python.org/pypi/distribute
 - nose from http://pypi.python.org/pypi/nose/
 - virtualenv from http://pypi.python.org/pypi/virtualenv
 - lpthw.web - sudo pip install lpthw.web

$pip install [distribute|nose|virtualenv]

#To Run
$ python bin/app.py 

point your browser to localhost:8080/hello?name=<input parameters>

supported parameters:
 - version (version of sqlite)
 - ib_sites (all sites in db)
 - ib_vnx (all vnx system in db)
