import cherrypy
import json

class Converter():
    #cherrypy.\
    exposed = True
    
    def PUT(self, *uri):
        # Lettura del body e decodifica da json a dizionario
        str_json = cherrypy.request.body.read()
        input_dict = json.loads(str_json)
        output_dict = {
            "originalValues": input_dict["values"],
            "convertedValues": ""
        }
        conv = []
        # Ciclo sui valori da convertire
        for num in output_dict["originalValues"]:
            value = self.convert(num, input_dict["originalUnit"], input_dict["targetUnit"])
            conv.append(value)
        output_dict["convertedValues"] = conv
        return json.dumps(output_dict)
    
    def convert(self, num: float, originalUnit: str, targetUnit: str) -> float:
        finalValue = 0
        if originalUnit == 'C':
            if targetUnit == 'K':
                finalValue = float(num) + 273.15
            elif targetUnit == 'F':
                finalValue = (float(num)*9/5)+32
        elif originalUnit == 'K':
            if targetUnit == 'C':
                finalValue = float(num) - 273.15
            elif targetUnit == 'F':
                finalValue = (float(num-273.15)*9/5)+32
        elif originalUnit == 'F':
            if targetUnit == 'C':
                finalValue = ((float(num) - 32) * 5 / 9)
            elif targetUnit == 'K':
                #(5 °F - 32) × 5/9 + 273,15
                finalValue = ((float(num) - 32) * 5 / 9) + 273.15

        return round(finalValue, 2)
    
if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
        }
    }
    cherrypy.tree.mount (Converter(), '/', conf)
    cherrypy.config.update({'server.socket_port': 8080})
    
    cherrypy.engine.start()
    cherrypy.engine.block()