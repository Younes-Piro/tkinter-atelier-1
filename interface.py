from tkinter import *
from  tkinter import ttk
from lxml import etree
from bs4 import BeautifulSoup 

root  = Tk()
root.title('Crud bibliotheque with xml')
root.geometry('500x500')
root['bg'] = '#AC99F2'

game_frame = Frame(root)
game_frame.pack()

#scrollbar
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

game_scroll = Scrollbar(game_frame,orient='horizontal')
game_scroll.pack(side= BOTTOM,fill=X)

my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)


my_game.pack()

game_scroll.config(command=my_game.yview)
game_scroll.config(command=my_game.xview)

#define our column
 
my_game['columns'] = ('livre', 'genre', 'titre', 'auteur')

# format our column
my_game.column("#0", width=0,  stretch=NO)
my_game.column("livre",anchor=CENTER, width=80)
my_game.column("genre",anchor=CENTER,width=80)
my_game.column("titre",anchor=CENTER,width=80)
my_game.column("auteur",anchor=CENTER,width=80)

#Create Headings 
my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("livre",text="livre",anchor=CENTER)
my_game.heading("genre",text="genre",anchor=CENTER)
my_game.heading("titre",text="titre",anchor=CENTER)
my_game.heading("auteur",text="auteur",anchor=CENTER)

#extract data
with open('schema.xml', 'r') as f: 
    data = f.read() 
  
Bs_data = BeautifulSoup(data, "xml") 
  
b_unique = Bs_data.find_all('livre') 

def insert():
    for idx, livre in enumerate(b_unique):
        my_game.insert(parent='',index='end',text='',
        values=((idx+1),livre['genre'],livre.titre.text,livre.auteur.text))
insert()
# Create Submit Function For database
def submit():
	

	# Clear The Text Boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
my_game.pack()

# Create Text Boxes
f_name_label = Label(root, text="First Name")
f_name_label.pack(side=LEFT)
f_name = Entry(root, width=30)
f_name.pack(side=RIGHT)
l_name = Entry(root, width=30)
l_name.pack(side=LEFT)
address = Entry(root, width=30)
address.pack(side=RIGHT)
city = Entry(root, width=30)
city.pack()
state = Entry(root, width=30)
state.pack()
zipcode = Entry(root, width=30)
zipcode.pack()
delete_box = Entry(root, width=30)
delete_box.pack()


# Create Text Box Labels

l_name_label = Label(root, text="Last Name")
l_name_label.pack()
address_label = Label(root, text="Address")
address_label.pack()
city_label = Label(root, text="City")
city_label.pack()
state_label = Label(root, text="State")
state_label.pack()
zipcode_label = Label(root, text="Zipcode")
zipcode_label.pack()
delete_box_label = Label(root, text="Select ID")
delete_box_label.pack()

# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.pack()

root.mainloop()