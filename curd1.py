from tkinter import*
from tkinter import messagebox
import sqlite3
root=Tk()
root.title("User")
co=sqlite3.connect("Facebook.db")
c=co.cursor()
# c.execute("""CREATE TABLE User(
#     FirstName text,
#     LastName text,
#     age text,
#     address text,
#     city text,
#     zipcode integer,
#     password text,
#     gender)""")
# print("Table created successfully")

#create text box
def add():
    co=sqlite3.connect("Facebook.db")
    c=co.cursor()
    c.execute("INSERT INTO User VALUES(:f_name, :l_name, :age, :address, :city, :zipcode, :password, :gender)",{ 
       "f_name":f_name.get(),
       "l_name":l_name.get(),
        "age":age.get(),
        "address":address.get(),
        "city":city.get(),
        "zipcode":zipcode.get(),
        "password":password.get(),
        "gender":gender.get()
    })
    messagebox.showinfo("user","Inserted Successfully")
    f_name.delete(0,END)
    l_name.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)
    password.delete(0,END)
    gender.delete(0,END)
    co.commit()
    co.close()

def show():
    co=sqlite3.connect("Facebook.db")
    c=co.cursor()
    c.execute("SELECT *, oid FROM User")
    records=c.fetchall()
    print_records=""
    for record in records:
        print_records+=str(record[0]) + " " +str(record[1]) + "" + "\t" + str(record[8]) + "\n"
    show_label=Label(root,text=print_records)
    show_label.grid(row=10,column=0,columnspan=2)
    co.commit()
    co.close()

def delete():
    co=sqlite3.connect("Facebook.db")
    c=co.cursor()
    c.execute("Delete from User WHERE oid=" + delete_box.get())
    # print("Deleted successfully")
    delete_box.delete(0,END)
    messagebox.showinfo("user","Deleted Successfully")
    co.commit()
    co.close()
def update():
    co=sqlite3.connect("Facebook.db")
    c=co.cursor()
    record_id=delete_box.get()
    
    c.execute(""" UPDATE User SET
    FirstName=:first,
    LastName=:last,
    age=:age,
    address=:address,
    city=:city,
    zipcode=:zipcode,
    password=:password,
    gender=:gender
    WHERE oid=:oid""",
    {"first":f_name_editor.get(),
    "last":l_name_editor.get(),
    "age":age_editor.get(),
    "address":address_editor.get(),
    "city":city_editor.get(),
    "zipcode":zipcode_editor.get(),
    "password":password_editor.get(),
    "gender":gender_editor.get(),
    "oid":record_id
    }
    )
    messagebox.showinfo("user","Upadted Successfully")
    co.commit()
    co.close()
    editor.destroy()

def edit():
    global editor 
    editor=Toplevel()
    editor.title("Update Data")
    editor.geometry("300x400")

    conn=sqlite3.connect("Facebook.db")
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute("SELECT * FROM User WHERE oid=" + record_id)
    records=c.fetchall()
    global f_name_editor
    global l_name_editor
    global age_editor
    global address_editor
    global city_editor
    global zipcode_editor  
    global password_editor
    global gender_editor


    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1)

    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)

    age_editor=Entry(editor,width=30)
    age_editor.grid(row=2,column=1)

    address_editor=Entry(editor,width=30)
    address_editor.grid(row=3,column=1)

    city_editor=Entry(editor,width=30)
    city_editor.grid(row=4,column=1)

    zipcode_editor=Entry(editor,width=30)
    zipcode_editor.grid(row=5,column=1)

    password_editor=Entry(editor,width=30)
    password_editor.grid(row=6,column=1)

    gender_editor=Entry(editor,width=30)
    gender_editor.grid(row=7,column=1)

    f_name_label=Label(editor,text="First Name")
    f_name_label.grid(row=0,column=0)

    l_name_label=Label(editor,text="Last Name")
    l_name_label.grid(row=1,column=0)

    age_label=Label(editor,text="age")
    age_label.grid(row=2,column=0)

    address_label=Label(editor,text="Address")
    address_label.grid(row=3,column=0)

    city_label=Label(editor,text="City")
    city_label.grid(row=4,column=0)

    zipcode_label=Label(editor,text="zipcode")
    zipcode_label.grid(row=5,column=0)

    password_label=Label(editor,text="password")
    password_label.grid(row=6,column=0)

    gender_label=Label(editor,text="gender")
    gender_label.grid(row=7,column=0)

    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        age_editor.insert(0,record[2])
        address_editor.insert(0,record[3])
        city_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])
        password_editor.insert(0,record[6])
        gender_editor.insert(0,record[7])

    edit_btn=Button(editor,text="Save",command=update)
    edit_btn.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=110)



f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0)

l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)

age_label=Label(root,text="age")
age_label.grid(row=2,column=0)

address_label=Label(root,text="address")
address_label.grid(row=3,column=0)

city_label=Label(root,text="city")
city_label.grid(row=4,column=0)

zipcode_label=Label(root,text="zipcode")
zipcode_label.grid(row=5,column=0)

password_label=Label(root,text="password")
password_label.grid(row=6,column=0)

gender_label=Label(root,text="Gender")
gender_label.grid(row=7,column=0)

delete_label=Label(root,text="Delete Id")
delete_label.grid(row=11,column=0)

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)

age=Entry(root,width=30)
age.grid(row=2,column=1)

address=Entry(root,width=30)
address.grid(row=3,column=1)

city=Entry(root,width=30)
city.grid(row=4,column=1)

zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)

password=Entry(root,width=30)
password.grid(row=6,column=1)

gender=Entry(root,width=30)
gender.grid(row=7,column=1)

delete_box=Entry(root,width=30)
delete_box.grid(row=11,column=1,pady=5)

add_btn=Button(root,text="Add Record",command=add)
add_btn.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

show_btn=Button(root,text="Show Record",command=show)
show_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

delete_btn=Button(root,text="Delete button",command=delete)
delete_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

edit_btn=Button(root,text="Update",command=edit)
edit_btn.grid(row=13,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

co.commit()
co.close()

root.mainloop()
