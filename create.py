from lxml import etree
root = etree.parse("data.xml").getroot()

users = etree.Element("users")

users_data = [
("101", "Zorro", "Danseur"),
("102", "Hulk", "Footballeur"),
("103", "Zidane", "Star"),
("104", "Beans", "Epicier"),
("105", "Batman", "Veterinaire"),
("106", "Spiderman", "Veterinaire"),
]

for user_data in users_data:
    user = etree.SubElement(users, "user")
    user.set("data-id", user_data[0])
    nom = etree.SubElement(user, "nom")
    nom.text = user_data[1]
    metier = etree.SubElement(user, "metier")
    metier.text = user_data[2]
    root.insert(1,user)

tree = etree.ElementTree(root)
tree.write('data.xml', pretty_print=True, xml_declaration=True,   encoding="utf-8")
