import cherrypy
import json

class HelloWorld2(object):
    #@cherrypy.expose
    exposed = True

    def GET(self, *uri, **params):
        finalValue = 0.0
        if params["originalUnit"] == 'C':
            if params["targetUnit"] == 'K':
                finalValue = float(params["value"]) + 273.15
            elif params ["targetUnit"] == 'F':
                finalValue = (float(params["value"])*9/5)+32
        elif params["originalUnit"] == 'K':
            if params["targetUnit"] == 'C':
                finalValue = float(params["value"]) - 273.15
            elif params ["targetUnit"] == 'F':
                finalValue = (float(params["value"]-273.15)*9/5)+32
        elif params["originalUnit"] == 'F':
            if params["targetUnit"] == 'C':
                finalValue = ((float(params["value"]) - 32) * 5 / 9)
            elif params["targetUnit"] == 'K':
                #(5 °F - 32) × 5/9 + 273,15
                finalValue = ((float(params["value"]) - 32) * 5 / 9) + 273.15

        dict = {"value": "{}".format(round(finalValue, 2)),
                "originalUnit": str(params["originalUnit"]),
                "finalUnit": str(params["targetUnit"])}

        return json.dumps(dict)


if __name__ == "__main__":
    # standard configuration to serve the url "localhost:8080"

    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        }
    }

    cherrypy.tree.mount(HelloWorld2(), '/converter', conf)
    cherrypy.config.update({'server.socket_host': '127.0.0.1'})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    input()
    cherrypy.engine.stop()

    #    cherrypy.quickstart(HelloWorld2(),'/',conf)


