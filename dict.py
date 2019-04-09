import xmltodict
 
def convert(xml_file, xml_attribs=True):
    with open(second, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return d