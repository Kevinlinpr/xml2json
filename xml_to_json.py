import json
import sys
from langdetect import detect
from langdetect import DetectorFactory

DetectorFactory.seed = 0

BASE_OUTPUT_FOLDER = ""


class IOUtils:
    @staticmethod
    def gen_file_w(name: str, stream: str):
        path = BASE_OUTPUT_FOLDER + name
        file = open(path, "w")
        file.write(stream)
        file.close()

    @staticmethod
    def read(filename: str):
        file = open(filename)
        content = file.read()
        return content

    @staticmethod
    def parse(filename: str):
        file = open(filename)
        while file.readable():
            line = file.readline()
            if not line:
                break
            if line == "\n":
                continue


class XML:
    content: str
    filename: str
    dic: dict

    def __init__(self, filename: str):
        self.filename = filename
        self.content = IOUtils.read(filename)
        self.dic = {}

    def parse(self):
        file = open(self.filename)
        while file.readable():
            line = file.readline()
            if not line:
                break
            if line == "\n":
                continue
            if (not XML.filter(line)) and XML.string_flag(line):
                self.key_value(line)

    @staticmethod
    def filter(line: str):
        return line.startswith("<?xml") or line.startswith("<resources>") or line.startswith("<!--") or line.startswith("</resources>")

    @staticmethod
    def string_flag(line: str):
        return line.endswith("</string>\n")

    def key_value(self, line: str):
        key = line.split(">")[0].split("=")[1].replace("\"", "")
        value = line.split(">")[1].split("<")[0]
        self.dic[key] = value

    def json(self, lang_flag: str):
        result = "{\n"
        if lang_flag == "UNKNOWN":
            for key in self.dic:
                try:
                    value = self.dic[key]
                    if lang_flag == detect(value):
                        result += "  " + "\"" + key + "\": \"" + self.dic[key] + "\"\n"
                except:
                    result += "  " + "\"" + key + "\": \"" + self.dic[key] + "\"\n"
        else:
            for key in self.dic:
                try:
                    value = self.dic[key]
                    if lang_flag == detect(value):
                        result += "  " + "\"" + key + "\": \"" + self.dic[key] + "\",\n"
                except:
                    print("This row throws and error:", key)
        result += "}"
        return result

    @staticmethod
    def convert(source: str, lang_flag: str):
        xml = XML(source)
        xml.parse()
        output = "strings_" + lang_flag.replace("-", "_") + ".json"
        IOUtils.gen_file_w(output, xml.json(lang_flag))


if __name__ == '__main__':
    XML.convert(sys.argv[1], sys.argv[2])

