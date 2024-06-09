#Load Libraries
import pandas as pd
import xml.etree.ElementTree as ET

def convert_csv_to_ead(csv_file):
    df = pd.read_csv(csv_file)
    
    ead = ET.Element('ead')
    eadheader = ET.SubElement(ead, 'eadheader')
    
    eadid = ET.SubElement(eadheader, 'eadid')
    eadid.text = 'converted-id'
    
    filedesc = ET.SubElement(eadheader, 'filedesc')
    titlestmt = ET.SubElement(filedesc, 'titlestmt')
    titleproper = ET.SubElement(titlestmt, 'titleproper')
    titleproper.text = 'Converted Collection'
    
    archdesc = ET.SubElement(ead, 'archdesc', level='collection')
    did = ET.SubElement(archdesc, 'did')
    
    unittitle = ET.SubElement(did, 'unittitle')
    unittitle.text = 'Converted Archival Unit'
    
    unitdate = ET.SubElement(did, 'unitdate')
    unitdate.text = '2024'
    
    physdesc = ET.SubElement(did, 'physdesc')
    extent = ET.SubElement(physdesc, 'extent')
    extent.text = 'Variable Linear Feet'
    
    dsc = ET.SubElement(archdesc, 'dsc')
    for _, row in df.iterrows():
        c01 = ET.SubElement(dsc, 'c01', level='file')
        did = ET.SubElement(c01, 'did')
        unittitle = ET.SubElement(did, 'unittitle')
        unittitle.text = row['Title']
        unitdate = ET.SubElement(did, 'unitdate')
        unitdate.text = row['Date']
    
    tree = ET.ElementTree(ead)
    tree.write('converted_ead.xml', encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    csv_file = 'legacy_finding_aid.csv'  # Replace with your CSV file path
    convert_csv_to_ead(csv_file)
