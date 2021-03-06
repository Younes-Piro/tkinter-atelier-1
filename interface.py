from tkinter import *
from tkinter import ttk
from lxml import etree
import xml.etree.cElementTree as ET
import lxml.etree

root = Tk()
root.title('atelier 1')
root.geometry("400x600")

def validate():
    xml_file = lxml.etree.parse("biblio.xml")
    xml_validator = lxml.etree.DTD(file="bibliotheque.dtd")
    is_valid = xml_validator.validate(xml_file)
    print(is_valid)

# Create Update function to update a record
def update():
    ntree = ET.parse('biblio.xml')
    root_xml = ntree.getroot()
    id = int(my_data.focus())+1
    
    for livre in root_xml.findall('livre'):
        if int(livre.get('id')) == id:
            livre.set('genre', genre_editor.get())
            livre.find('auteur').text = auteur_editor.get()
            livre.find('titre').text = titre_editor.get()
             #save the update
            ntree.write("biblio.xml") 
            
    editor.destroy()
    root.deiconify()
    query()
# Create Edit function to update a record
def edit():
    root.withdraw()
    global editor
    editor = Tk()
    editor.title('Update Records')
    editor.geometry("400x300")

    #Create Global Variables for text box names
    global genre_editor
    global titre_editor
    global auteur_editor

    genres = ["fiction", "drame","aventure","policier"]
    # Create Text Boxes
    genre_editor = ttk.Combobox(editor,values=genres)
    genre_editor.grid(row=0, column=1, padx=20, pady=(10,0))
    genre_editor.current(0)
    titre_editor = Entry(editor,width=30)
    titre_editor.grid(row=1,column=1)
    auteur_editor = Entry(editor,width=30)
    auteur_editor.grid(row=2, column=1)

    # Create Text Box Labels
    genre_label = Label(editor, text="Genre")
    genre_label.grid(row=0, column=0, pady=(10, 0))
    titre_label = Label(editor, text="Titre")
    titre_label.grid(row=1, column=0)
    auteur_label = Label(editor, text="Auteur")
    auteur_label.grid(row=2, column=0)

    ntree = ET.parse('biblio.xml')
    root_xml = ntree.getroot()
    # Loop over our xml file and get the propre values
    id = int(my_data.focus())+1
    for livre in root_xml.findall('livre'):
        if int(livre.get('id')) == id:
            for idx,genre in enumerate(genres):
                if genre == livre.get('genre'):
                    genre_editor.current(idx)
            titre_editor.insert(0,livre.find('titre').text)
            auteur_editor.insert(0,livre.find('auteur').text)

    # Create a Save Button To Save edited record
    edit_btn = Button(editor, text="Edit Record", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=145)
	
# Create Function to Delete A Record
def delete():

    ntree = ET.parse('biblio.xml')
    root_xml = ntree.getroot()

    for livre in root_xml.findall('livre'):
        #get the email of the current record, 
        ids = livre.get('id')
        #check is this the email we are looking for?
        id = int(my_data.focus())+1
        for single_id in ids:
            if int(single_id) == id:
                root_xml.remove(livre)            
                #finally save the update
                ntree.write("biblio.xml") 
            
    #calling query to update the shows
    query()


# Create Submit Function For database
def submit():

    #get last id
    ntree = ET.parse('biblio.xml')
    root_xml = ntree.getroot()
    
    ids = list()
    for livre in root_xml.findall('livre'):
        ids.append(livre.get('id'))

    #gettin data from form and adding to xml file
    root = etree.parse("biblio.xml").getroot()
    biblio = etree.Element("bibliotheque")
    livre = etree.SubElement(biblio, "livre")
    livre.set("genre", genre.get())
    livre.set("id", str((int(ids[-1])+1)))
    nom = etree.SubElement(livre, "titre")
    nom.text = titre.get()
    metier = etree.SubElement(livre, "auteur")
    metier.text = auteur.get()
    root.append(livre)
    tree = etree.ElementTree(root)
    tree.write('biblio.xml', pretty_print=True, xml_declaration=True, encoding="utf-8")

    #Clear the boxes
    genre.current(0)
    auteur.delete(0,END)
    titre.delete(0,END)

    #calling query to update the shows
    query()

# Create Query Function
def query():
    ntree = ET.parse('biblio.xml')
    root_xml = ntree.getroot()
    #delete rows 
    for row in my_data.get_children():
        my_data.delete(row)

    for livre in root_xml.findall('livre'):
         my_data.insert(parent='',index='end',iid=(int(livre.get('id'))-1),text='',values=(livre.get('id'),livre.get('genre'),livre.find('titre').text,livre.find('auteur').text)) 
       

# Create Text Boxes
genre = ttk.Combobox(root,values=["fiction", "drame","aventure","policier"])
genre.grid(row=0, column=1, padx=20, pady=(10, 0))
genre.current(0)
titre = Entry(root, width=30)
titre.grid(row=1, column=1)
auteur = Entry(root, width=30)
auteur.grid(row=2, column=1)
# delete_box = Entry(root, width=30)
# delete_box.grid(row=9, column=1, pady=5)

# Create Text Box Labels
genre_label = Label(root, text="Genre")
genre_label.grid(row=0, column=0, pady=(10, 0))
titre_label = Label(root, text="Titre")
titre_label.grid(row=1, column=0)
auteur_label = Label(root, text="Auteur")
auteur_label.grid(row=2, column=0)
# delete_box_label = Label(root, text="Select ID")
# delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# # Create a Query Button
# query_btn = Button(root, text="Show Records", command=query)
# query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create A Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

data_frame = Frame(root)
data_frame.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

my_data = ttk.Treeview(data_frame)

#define our column
 
my_data['columns'] = ('livre', 'genre', 'titre', 'auteur')

# format our column
my_data.column("#0", width=0,  stretch=NO)
my_data.column("livre",anchor=CENTER, width=80)
my_data.column("genre",anchor=CENTER,width=80)
my_data.column("titre",anchor=CENTER,width=80)
my_data.column("auteur",anchor=CENTER,width=80)

#Create Headings 
my_data.heading("#0",text="",anchor=CENTER)
my_data.heading("livre",text="livre",anchor=CENTER)
my_data.heading("genre",text="genre",anchor=CENTER)
my_data.heading("titre",text="titre",anchor=CENTER)
my_data.heading("auteur",text="auteur",anchor=CENTER)

my_data.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

if validate:
    query()
else:
    print("XML FILE IS INVALID")

root.mainloop()