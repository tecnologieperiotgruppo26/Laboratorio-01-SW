import cherrypy

class StringGeneratorWebService(object):
    cherrypy.exposed = True
    def GET (self, *uri, ** params):
        return ("URI: %s; Parameters %s" % (str (uri), str(params)))
    
if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount (StringGeneratorWebService(), '/string', conf)
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8080})
    
    cherrypy.engine.start()
    cherrypy.engine.block()