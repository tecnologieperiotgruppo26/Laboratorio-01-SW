import os, os.path 
import random 
import string 
import cherrypy

class StringGenerator(object): 
  @cherrypy.expose

  def index(self):
    return open('./freeboard/index.html')

if __name__ == '__main__': 
  conf = {
    '/': {
      'tools.sessions.on': True,
      'tools.staticdir.root': os.path.abspath(os.getcwd()) 
    },
    '/freeboard': {
      'tools.staticdir.on': True,
      'tools.staticdir.dir': './freeboard' 
    },
    '/static': {
      'tools.staticdir.on': True,
      'tools.staticdir.dir': './freeboard/static'
    }
  }
  cherrypy.tree.mount(StringGenerator(), '/', conf) 
  cherrypy.engine.start()
  cherrypy.engine.block()