import xml.etree.ElementTree
import json

def xmlRoot(xmlFilePath):
    return xml.etree.ElementTree.parse(xmlFilePath).getroot()

def xmlToJson_namedArray_verbose(xmlCodesRoot):
    return {xmlCodesRoot.tag: [{"code": xmlCode.attrib["code"], "text": xmlCode.text.strip()} for xmlCode in xmlCodesRoot]}

def xmlToJson_namedArray_compressed(xmlCodesRoot):
    return {xmlCodesRoot.tag: [{xmlCode.attrib["code"]: xmlCode.text.strip()} for xmlCode in xmlCodesRoot]}

def xmlToJson_unnamedArray_verbose(xmlCodesRoot):
    return [{"code": xmlCode.attrib["code"], "text": xmlCode.text.strip()} for xmlCode in xmlCodesRoot]

def xmlToJson_unnamedArray_compressed(xmlCodesRoot):
    return [{xmlCode.attrib["code"]: xmlCode.text.strip()} for xmlCode in xmlCodesRoot]

def xmlToJson_allTheFields(xmlCodesRoot):
    fields = dict()

    for xmlCode in xmlCodesRoot:
        fields[xmlCode.attrib["code"]] = xmlCode.text.strip()

    return fields

def xmlToJsonCodesFile(xmlCodesRoot, jsonFilePath):
#    xmlToJson = xmlToJson_namedArray_verbose
#    xmlToJson = xmlToJson_namedArray_compressed
    xmlToJson = xmlToJson_unnamedArray_verbose
#    xmlToJson = xmlToJson_unnamedArray_compressed
#    xmlToJson = xmlToJson_allTheFields

    with open(jsonFilePath, "w") as jsonCodesFile:
        json.dump(xmlToJson(xmlCodesRoot), jsonCodesFile, separators=(",",": "), indent=4)

def main():
    xmlToJsonCodesFile(xmlRoot("codes.xml"), "codes.json")

if __name__ == "__main__":
    main()

def test():
    xmlToJsonCodesFile(xmlRoot("codes.xml"), "codes.json")

    jsonCodes = None

    with open("codes.json", "r") as jsonCodesFile:
        jsonCodes = json.load(jsonCodesFile)

    if jsonCodes:
        print(jsonCodes)
