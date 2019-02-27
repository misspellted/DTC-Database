import xml.etree.ElementTree
import json

def xmlRoot(xmlFilePath):
    return xml.etree.ElementTree.parse(xmlFilePath).getroot()

def xmlToJsonCodesFile(xmlCodesRoot, jsonFilePath):
    jsonCodes = {xmlCodesRoot.tag: [{"code": xmlCode.attrib["code"], "text": xmlCode.text.strip()} for xmlCode in xmlCodesRoot]}

    with open(jsonFilePath, "w") as jsonCodesFile:
        json.dump(jsonCodes, jsonCodesFile, separators=(",",": "), indent=4)

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
