import xml.etree.ElementTree as ET
key_count=0
metric_count=0
tree = ET.parse('storage_5454.xml')
root = tree.getroot()
properties = root.findall("./Columns/Column")
for prop in properties:
    children = prop.getchildren()
    for child in children:
        if child.attrib['value'] =='Key':
            print("Name of the key:",prop.attrib['name'])
            key_count+=1
    for child in children:
        if child.attrib['value'] =='Metric':
            print("Name of the metric:",prop.attrib['name'])
            print("Dtype:",prop.attrib['dtype'])
            metric_count+=1
print("Total no. of keys are:",key_count)
print("Total no. of metric are:",metric_count)







    
        


