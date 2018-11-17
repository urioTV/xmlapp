import os
import xml.etree.ElementTree as et


base_path = os.path.dirname(os.path.realpath(__file__))

xml_file = os.path.join(base_path, "data\\product_listing.xml")

tree = et.parse(xml_file)

root = tree.getroot()

#for child in root:
#    print(child.tag, child.attrib)

#for child in root:
#    for element in child:
#        print(element.tag, ":", element.text)



new_product = et.SubElement(root, "product", attrib={"id": "4"})

new_prod_name = et.SubElement(new_product, "name")
new_pod_desc = et.SubElement(new_product, "description")
new_prod_cost = et.SubElement(new_product, "cost")
new_prod_ship = et.SubElement(new_product, "shipping")

new_prod_name.text = "Python pants"
new_pod_desc.text = "Pants and done"
new_prod_cost.text = "199.82"
new_prod_ship.text = "201.93"

tree.write(xml_file)


