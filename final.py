import xml.etree.ElementTree as ET
from sys import argv
import os

List_storage=[]
List_processing=[]
def parsing(processing,storage):

    tree_process = ET.parse(processing)
    root_process = tree_process.getroot()

    tree_storage = ET.parse(storage)
    root_storage =tree_storage.getroot()

    id_storage = root_storage.get("analyzerId")
    name_storage = root_storage.get("id")
    version_storage = root_storage.get("schema_version") 

# To get List of storage side
    for key in root_storage.findall("./Columns/Column/Property/[@value='Key']..."):
        k_name = key.attrib['name']
        List_storage.append(k_name)
    for metric in root_storage.findall("./Columns/Column/Property/[@value='Metric']..."):
        m_name = metric.attrib['name']
        List_storage.append(m_name)     

# To get List of processing side
    process_name = root_process.findall("./[@id ='%s']/reports/report/[@name = '%s']/[@version = '%s']" %(id_storage,name_storage ,version_storage) )
    def extract (node):
        if node.tag == 'key':
            name = iter(node)
            for key_name in name:
                kname = key_name.text
                List_processing.append(kname) 
                  
        if node.tag == 'metrics':
            name = iter(node)
            for metric_name in name:
                mname = metric_name.get('name')
                List_processing.append(mname)    
        else:
            for child in iter(node):
                extract(child)
        return(List_processing)

    for prop in process_name:
        extract (prop)

# Comparing both the lists        
parsing(argv[1], argv[2] )
if List_storage==List_processing:
    print("Valid")
else:
    print("Invalid")

