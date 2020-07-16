import cherrypy
import json

class WebServer(object):
    exposed = True

    def GET(self, *uri, **params):
        token = uri
        finalValue = 0.0
        if token[1] == 'C':
            if token[2] == 'K':
                finalValue = float(token[0]) + 273.15
            elif params ["targetUnit"] == 'F':
                finalValue = (float(token[0])*9/5)+32
            else:
                raise cherrypy.HTTPError(404, 'Si è utilizzato un comando non valido!')
        elif token[1] == 'K':
            if token[2] == 'C':
                finalValue = float(token[0]) - 273.15
            elif params ["targetUnit"] == 'F':
                finalValue = (float(token[0]-273.15)*9/5)+32
            else:
                raise cherrypy.HTTPError(404, 'Si è utilizzato un comando non valido!')
        elif token[1] == 'F':
            if token[2] == 'C':
                finalValue = ((float(token[0]) - 32) * 5 / 9)
            elif token[2] == 'K':
                #(5 °F - 32) × 5/9 + 273,15
                finalValue = ((float(token[0]) - 32) * 5 / 9) + 273.15
            else:
                raise cherrypy.HTTPError(404, 'Si è utilizzato un comando non valido!')
        else:
            raise cherrypy.HTTPError(404, 'Si è utilizzato un comando non valido!')

        dict = {"value": "{}".format(round(finalValue, 2)),
                "originalUnit": str(token[1]),
                "finalUnit": str(token[2])}

        return json.dumps(dict)


if __name__ == "__main__":
    # standard configuration to serve the url "localhost:8080"

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        }
    }

    cherrypy.tree.mount(WebServer(), '/converter', conf)
    cherrypy.config.update({'server.socket_host': '127.0.0.1'})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    input()
    cherrypy.engine.stop()