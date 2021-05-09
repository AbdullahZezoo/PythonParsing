import pandas as pd
import xmltodict

class File(object):

    def __init__(self, input, output):
        self.input = input
        self.output = output

    def readFile(self):
        return

    def writeJson(self, data):
        try:
            with open(self.output, 'a') as outfile:
                outfile.write(data)
                outfile.write(",")
                outfile.close()
        except:
            print('write to json file error')

class XmlFile(File):
    def readFile(self):
        try:
            with open(self.input) as xml_file:
                data_dict = xmltodict.parse(xml_file.read())
                xml_file.close()
                return data_dict
        except:
            print('read xml file error')

class CsvFile(File):
    def readFile(self):
        try:
            data = pd.read_csv(self.input)
            return data
        except:
            print('read csv file error')
