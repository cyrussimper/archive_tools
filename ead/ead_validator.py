from lxml import etree

def validate_ead(xml_file, schema_file):
    with open(schema_file, 'rb') as f:
        schema_root = etree.XML(f.read())
        schema = etree.XMLSchema(schema_root)
    
    parser = etree.XMLParser(schema=schema)
    
    try:
        with open(xml_file, 'rb') as f:
            etree.fromstring(f.read(), parser)
        print("EAD XML file is valid.")
    except etree.XMLSyntaxError as e:
        print("EAD XML file is invalid.")
        print(e)

if __name__ == "__main__":
    xml_file = 'ead_output.xml'  # Replace with your EAD XML file path
    schema_file = 'ead.xsd'     # Replace with the EAD schema file path
    validate_ead(xml_file, schema_file)
