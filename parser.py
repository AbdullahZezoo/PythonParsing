from file import *
from convert import *
import sys

class Parser(object):
    def __init__(self, type, files):
        self.type = type
        self.files = files
        self.types = ['csv', 'xml']

    def parse(self):
        self.typeHandle()
        for file in self.files:

            file_obj = globals()[type.capitalize()+'File'](file, 'parsing_result/smaple.json')
            file_data = file_obj.readFile()

            convert_obj = globals()[type.capitalize()+'Convert'](file_data)
            converted_data = convert_obj.convert()

            file_obj.writeJson(converted_data)

    def typeHandle(self):
        if self.type not in self.types:
            sys.exit(self.type + " file type not supported")

if __name__ == '__main__':

    _len = len(sys.argv)
    if _len < 3:
        sys.exit("program takes <file_type> <file_path>\nexample > parser.py csv csv/customers.csv")

    type = str(sys.argv[1])
    files = sys.argv[2:_len]
    obj = Parser(type, files=files)
    obj.parse()