import json

class Convert(object):
    def __init__(self, data):
        self.data = data

    def convert(self):
        return

class XmlConvert(Convert):
    def convert(self):
        try:
            return json.dumps(self.data)
        except:
            print('xml data conversion error')

class CsvConvert(Convert):
    def convert(self):
        try:
            return self.data.to_json()
        except:
            print('csv data conversion error')