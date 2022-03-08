from tkinter import *
from tkinter import ttk
from lxml import etree
import xml.etree.cElementTree as ET

root = Tk()
root.title('atelier 1')
root.geometry("600x600")


# Create Update function to update a record
def update():
    pass
# Create Edit function to update a record
def edit():
    pass
# Create Function to Delete A Record
def delete():
    ntree = ET.parse('schema2.xml')
    root_xml = ntree.getroot()

    for galerie in root_xml.findall('galerie'):
        #get the email of the current record, 
        ids = galerie.get('id')
        #check is this the email we are looking for?
        id = int(my_data.focus())+1
        for single_id in ids:
            if int(single_id) == id:
                root_xml.remove(galerie)            
                #finally save the update
                ntree.write("schema2.xml") 
            
    #calling query to update the shows
    query()
# Create Submit Function For database
def submit():
    mytree= ET.parse('schema2.xml')
    myroot= mytree.getroot() 

    ids = list()

    if not myroot.findall('galerie'):
        ids.append(1)
    else:
        for galerie in myroot.findall('galerie'):
            ids.append(galerie.get('id'))


    nextId=int(ids[-1]) + 1 
    newrecord = ET.SubElement(myroot, "galerie",id=str(nextId) , address= address.get())  
    ET.SubElement(newrecord, "gerant", ).text = gerant.get()  
    contenu = ET.SubElement(newrecord, "contenu") 
    ET.SubElement(contenu, "type").text = type.get()  
    ET.SubElement(contenu, "auteur").text = auteur.get()  
    ET.SubElement(contenu, "titre").text = titre.get()
    ET.SubElement(contenu, "prix").text = prix.get()

    mytree.write("schema2.xml")    

    address.delete(0,END)
    gerant.delete(0,END)
    type.delete(0,END)
    auteur.delete(0,END)
    titre.delete(0,END)
    prix.delete(0,END)
    query()

# Create Query Function
def query():
    ntree = ET.parse('schema2.xml')
    root_xml = ntree.getroot()
    #delete rows 
    for row in my_data.get_children():
        my_data.delete(row)
    for galerie in root_xml.findall('galerie'):
        for contenu in galerie.findall('contenu'):
             my_data.insert(parent='',index='end',iid=(int(galerie.get('id'))-1),text='',values=(galerie.get('id'),galerie.get('address'),galerie.find('gerant').text,contenu.find('type').text,contenu.find('auteur').text,contenu.find('titre').text,contenu.find('prix').text))
          

# Create Text Boxes
address = Entry(root, width=30)
address.grid(row=0, column=1, padx=20, pady=(10, 0))
gerant = Entry(root, width=30)
gerant.grid(row=1, column=1)
type = Entry(root, width=30)
type.grid(row=2, column=1)
auteur = Entry(root,width=30)
auteur.grid(row=3,column=1)
titre = Entry(root,width=30)
titre.grid(row=4,column=1)
prix = Entry(root,width=30)
prix.grid(row=5,column=1)
# delete_box = Entry(root, width=30)
# delete_box.grid(row=9, column=1, pady=5)

# Create Text Box Labels
address_label = Label(root, text="address")
address_label.grid(row=0, column=0, pady=(10, 0))
gerant_label = Label(root, text="gerant")
gerant_label.grid(row=1, column=0)
type_label = Label(root, text="type")
type_label.grid(row=2, column=0)
auteur_label = Label(root, text="auteur")
auteur_label.grid(row=3, column=0)
titre_label = Label(root, text="titre")
titre_label.grid(row=4, column=0)
prix_label = Label(root, text="prix ")
prix_label.grid(row=5, column=0)
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
 
my_data['columns'] = ('id','address', 'gerant', 'type', 'auteur', 'titre','prix')

# format our column
my_data.column("#0", width=0,  stretch=NO)
my_data.column("id",anchor=CENTER, width=80)
my_data.column("address",anchor=CENTER, width=80)
my_data.column("gerant",anchor=CENTER,width=80)
my_data.column("type",anchor=CENTER,width=80)
my_data.column("auteur",anchor=CENTER,width=80)
my_data.column("titre",anchor=CENTER,width=80)
my_data.column("prix",anchor=CENTER,width=80)


#Create Headings 
my_data.heading("#0",text="",anchor=CENTER)
my_data.heading("id",text="id",anchor=CENTER)
my_data.heading("address",text="address",anchor=CENTER)
my_data.heading("gerant",text="gerant",anchor=CENTER)
my_data.heading("type",text="type",anchor=CENTER)
my_data.heading("auteur",text="auteur",anchor=CENTER)
my_data.heading("titre",text="titre",anchor=CENTER)
my_data.heading("prix",text="prix",anchor=CENTER)


my_data.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

query()

root.mainloop()