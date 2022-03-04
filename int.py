from tkinter import *
from bs4 import BeautifulSoup 
from tkinter import ttk
from lxml import etree

root = Tk()
root.title('atelier 1')
root.geometry("400x600")


# Create Update function to update a record
def update():
	pass

# Create Edit function to update a record
def edit():
	pass
	


# Create Function to Delete A Record
def delete():
	pass


# Create Submit Function For database
def submit():

    #get last id
    with open('schema.xml', 'r') as f: 
        data = f.read() 
    
    Bs_data = BeautifulSoup(data, "xml") 
    
    b_unique = Bs_data.find_all('livre')
    ids = list()
    for livre in b_unique:
        ids.append(livre['id'])

    #gettin data from form and adding to xml file
    root = etree.parse("schema.xml").getroot()
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
    tree.write('schema.xml', pretty_print=True, xml_declaration=True, encoding="utf-8")

    #Clear the boxes
    genre.current(0)
    auteur.delete(0,END)
    titre.delete(0,END)

    #calling query to update the shows
    query()

# Create Query Function
def query():
    #extract data
    with open('schema.xml', 'r') as f: 
        data = f.read() 
    
    Bs_data = BeautifulSoup(data, "xml") 
    
    b_unique = Bs_data.find_all('livre') 
    print_records = ''
    for livre in b_unique:
        print_records += livre['genre'] + " " + "\t" + livre.titre.text + " " + "\t" + livre.auteur.text + "\n"
    	  
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


# Create Text Boxes
genre = ttk.Combobox(root,values=["fiction", "drame","aventure","policier"])
genre.grid(row=0, column=1, padx=20, pady=(10, 0))
genre.current(0)
titre = Entry(root, width=30)
titre.grid(row=1, column=1)
auteur = Entry(root, width=30)
auteur.grid(row=2, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create Text Box Labels
genre_label = Label(root, text="Genre")
genre_label.grid(row=0, column=0, pady=(10, 0))
titre_label = Label(root, text="Titre")
titre_label.grid(row=1, column=0)
auteur_label = Label(root, text="Auteur")
auteur_label.grid(row=2, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create A Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

query()

root.mainloop()