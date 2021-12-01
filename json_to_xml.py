import json
import sys

BASE_OUTPUT_FOLDER=""


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


def gen_xml(source: str, lang_flag: str):
    result = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n" \
             "<resources>\n"
    content = json.loads(IOUtils.read(source))
    for key in json.loads(IOUtils.read(source)):
        value = (content[key])[lang_flag]
        result += "    <string name=\"" + key + "\">" + value + "</string>\n"
    result += "</resources>\n"
    output = "strings_" + lang_flag.replace("-", "_") + ".xml"
    IOUtils.gen_file_w(output, result)


if __name__ == "__main__":
    index = 0
    file = sys.argv[1]
    for arg in sys.argv:
        if index < 2:
            index += 1
            continue
        gen_xml(file, arg)
        index += 1


