import xml.etree.ElementTree
import json

CODE = "code"
TEXT = "text"

def xmlRoot(xmlFilePath):
    """Parses an XML file and returns the root element."""
    return xml.etree.ElementTree.parse(xmlFilePath).getroot()

def xmlToTuple(xmlCode):
    """Extracts the attribute and contents of a <code> element as a tuple."""
    return (xmlCode.attrib[CODE], xmlCode.text.strip())

def xmlToJsonObject(xmlCodesRoot):
    """Generates an unnamed fields dictionary in preparation for json.dump().

    Using the dictionary in the json.dump() call will produce the following
    structure in the codes.json file:

    {
        "P1000": "Example code",
        ...
    }
    """
    object = dict()

    for xmlCode in xmlCodesRoot:
        field, value = xmlToTuple(xmlCode)
        object[field] = value

    return object

def xmlToNamedJsonObject(xmlCodesRoot):
    """Generates a named fields dictionary in preparation for json.dump().

    Using the dictionary in the json.dump() call will produce the following
    structure in the codes.json file:

    {
        "codes":
        {
            "P1000": "Example code",
            ...
        }
    }
    """
    return {xmlCodesRoot.tag: xmlToJsonObject(xmlCodesRoot)}

def xmlToVerboseJsonArray(xmlCodesRoot):
    """Generates an unnamed fields list in preparation for json.dump().

    Using the list in the json.dump() call will produce the following structure
    in the codes.json file:

    [
        {
            "code": "P1000",
            "text": "Example code"
        },
        ...
    ]
    """
    array = list()

    for xmlCode in xmlCodesRoot:
        field, value = xmlToTuple(xmlCode)
        array.append({CODE: field, TEXT: value})

    return array

def xmlToNamedVerboseJsonArray(xmlCodesRoot):
    """Generates a named fields list in preparation for json.dump().

    Using the list in the json.dump() call will produce the following structure
    in the codes.json file:

    {
        "codes":
        [
            {
                "code": "P1000",
                "text": "Example code"
            },
            ...
        ]
    }
    """
    return {xmlCodesRoot.tag: xmlToVerboseJsonArray(xmlCodesRoot)}

def xmlToCompressedJsonArray(xmlCodesRoot):
    """Generates an unnamed fields list in preparation for json.dump().

    Using the list in the json.dump() call will produce the following structure
    in the codes.json file:

    [
        {
            "P1000": "Example code"
        },
        ...
    ]
    """
    array = list()

    for xmlCode in xmlCodesRoot:
        field, value = xmlToTuple(xmlCode)
        array.append({field: value})

    return array

def xmlToNamedCompressedJsonArray(xmlCodesRoot):
    """Generates a named fields list in preparation for json.dump().

    Using the list in the json.dump() call will produce the following structure
    in the codes.json file:

    {
        "codes":
        [
            {
                "P1000": "Example code"
            },
            ...
        ]
    }
    """
    return {xmlCodesRoot.tag: xmlToCompressedJsonArray(xmlCodesRoot)}

def xmlToJsonCodesFile(xmlCodesRoot, jsonFilePath):
#    xmlToJson = xmlToJsonObject
    xmlToJson = xmlToNamedJsonObject
#    xmlToJson = xmlToVerboseJsonArray
#    xmlToJson = xmlToNamedVerboseJsonArray
#    xmlToJson = xmlToCompressedJsonArray
#    xmlToJson = xmlToNamedCompressedJsonArray

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
