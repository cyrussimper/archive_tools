import xml.etree.ElementTree as ET

def create_ead(data):
    ead = ET.Element('ead')
    eadheader = ET.SubElement(ead, 'eadheader')
    
    # Add metadata about the EAD document
    eadid = ET.SubElement(eadheader, 'eadid')
    eadid.text = data.get('eadid', 'unique-id')
    
    filedesc = ET.SubElement(eadheader, 'filedesc')
    titlestmt = ET.SubElement(filedesc, 'titlestmt')
    titleproper = ET.SubElement(titlestmt, 'titleproper')
    titleproper.text = data.get('titleproper', 'Title of the Collection')
    
    archdesc = ET.SubElement(ead, 'archdesc', level='collection')
    did = ET.SubElement(archdesc, 'did')
    
    # Add essential information about the archival unit
    unittitle = ET.SubElement(did, 'unittitle')
    unittitle.text = data.get('unittitle', 'Title of the Archival Unit')
    
    unitdate = ET.SubElement(did, 'unitdate')
    unitdate.text = data.get('unitdate', '2024')
    
    physdesc = ET.SubElement(did, 'physdesc')
    extent = ET.SubElement(physdesc, 'extent')
    extent.text = data.get('extent', '1 Linear Feet')
    
    # Add hierarchical structure if available
    if 'components' in data:
        dsc = ET.SubElement(archdesc, 'dsc')
        for component in data['components']:
            c01 = ET.SubElement(dsc, 'c01', level=component.get('level', 'file'))
            did = ET.SubElement(c01, 'did')
            unittitle = ET.SubElement(did, 'unittitle')
            unittitle.text = component.get('unittitle', 'Untitled')
            unitdate = ET.SubElement(did, 'unitdate')
            unitdate.text = component.get('unitdate', '2024')
    
    tree = ET.ElementTree(ead)
    tree.write('ead_output.xml', encoding='utf-8', xml_declaration=True)

# Example data
data = {
    'eadid': '12345',
    'titleproper': 'Sample Collection Title',
    'unittitle': 'Sample Archival Unit',
    'unitdate': '2024',
    'extent': '2 Linear Feet',
    'components': [
        {'level': 'series', 'unittitle': 'Series 1', 'unitdate': '2024'},
        {'level': 'file', 'unittitle': 'File 1', 'unitdate': '2024'}
    ]
}

if __name__ == "__main__":
    create_ead(data)
