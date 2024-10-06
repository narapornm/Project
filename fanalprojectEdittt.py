import sqlite3
import time 

conn=sqlite3.connect("bookbookbutpoohedit.db")
c=conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id_product INTEGER PRIMARY KEY NOT NULL,
        date varchar(50) NOT NULL,
        time varchar(50) NOT NULL,
        product CHAR(20) NOT NULL,
        price INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        picture BLOB NOT NULL
    )
    ''')


c.execute('''CREATE TABLE IF NOT EXISTS cart (
        
        cart_id integer PRIMARY KEY NOT NULL,
        cart_code CHAR(20) NOT NULL,
        Name_product CHAR(20) NOT NULL,
        Price INTEGER NOT NULL
        
        
    )
    ''')
#c.execute ('''ALTER TABLE cart ADD quantity INTEGER''')
#c.execute('''ALTER TABLE usermember DROP COLUMN password;''')

c.execute('''CREATE TABLE IF NOT EXISTS admin(
                id integer PRIMARY KEY AUTOINCREMENT,
                Date varchar(50) NOT NULL,
                Time varchar(50) NOT NULL,
                Username varchar(100) NOT NULL)''')
    
c.execute('''
        CREATE TABLE IF NOT EXISTS usermember (
        id INTEGER PRIMARY KEY NOT NULL,
        username CHAR(20) NOT NULL,
        Tel CHAR(10) NOT NULL
        
    )
    ''')


c.execute('''
        CREATE TABLE IF NOT EXISTS Daily_income (
        list CHAR(20) NOT NULL,
        pice INTEGER ,
        date DATE , 
        month DATE 
              
    )
    ''')



conn.commit()


import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter.colorchooser import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as tkFont
from io import BytesIO  #แปลงอักษรจากตารางsqlite เป็นภาพ
from tkinter import simpledialog
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
import subprocess
from reportlab.lib import colors  # Add this import line
from fpdf import FPDF
import subprocess
#import tkinter as toplevel
#import random

# Provide the full path to the "TH Sarabun New" font file
font_path = r"C:\Users\User\Desktop\python\projact.py\pj\THSarabunNew.ttf"
# Register the "TH Sarabun New" font
pdfmetrics.registerFont(TTFont('THSarabunNew', font_path))

def convert_to_number(text):    #ฟังก์ชั่นแปลงข้อมูลข้อความเป็นตัวเลข
        try:
            return int(text)  # แปลงข้อความเป็นตัวเลข
        except ValueError:
            return None  # หากไม่สามารถแปลงได้ให้คืนค่า None


# ฟังก์ชั่นสำหรับแอดมิน
def open_login_admin():
    global login_image  # ประกาศตัวแปรเป็น global 
    mainwindow.withdraw()  # ซ่อนหน้าต่างหลัก  withdraw คือการซ่อน
    # สร้างหน้าต่างเสริมสำหรับการล็อกอิน  สร้างหน้าต่างที่ 2 ######################################################################################
    login_window = tk.Toplevel(mainwindow)
    login_window.title("เข้าสู่ระบบ")
    login_window.geometry("500x300+460+200")

    #พื้นหลังเป็นรูปภาพ
    login_image = tk.PhotoImage(file="bg_login.png")  # เปลี่ยน "background.png" เป็นชื่อไฟล์รูปของคุณ

    # สร้าง Label แสดงรูปภาพพื้นหลัง
    bglogin_label = tk.Label(login_window, image=login_image)
    bglogin_label.place(relwidth=1, relheight=1)

    
    #login_window.withdraw()  # ซ่อนหน้าต่างล็อกอินไว้ก่อน

    # สร้างปุ่มเปิดหน้าต่างเสริมสำหรับการล็อกอิน 
    #login_window.deiconify()  # เปิดหน้าต่างล็อกอิน


    # สร้างช่องใส่ username และ password
    username_label = tk.Label(login_window, text="Username:", fg="#591404",bg="#FFF0E3",font=10)
    username_label.place(x=70,y=100)
    username_entry = tk.Entry(login_window)
    username_entry.place(x=185,y=103)

    password_label = tk.Label(login_window, text="Password:",fg="#591404",bg="#FFF0E3",font=10)
    password_label.place(x=70,y=150)
    password_entry = tk.Entry(login_window)  # เราใส่ show="*" เพื่อซ่อนรหัสผ่าน
    password_entry.place(x=185,y=153)



    def check_login():
        username = username_entry.get()
        password = password_entry.get()
        
        
        if username =="" and password == "" :
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกชื่อผู้ใช้และรหัสผ่าน")
        elif password == "" :
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกรหัสผ่าน")
        elif username =="" :
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกชื่อผู้ใช้")
        elif password == "000":   
            
            username_value = username_entry.get()      #คือการดึงสิ่งที่ admin พิมพ์ในช่อง entry มาไว้ในตัวแปร username_value
                    
            named_tuple = time.localtime() # get struct_time
            date_string = time.strftime("%d/%m/%Y", named_tuple)
            time_string = time.strftime("%H:%M",named_tuple)
            print("วันที่ : ",date_string)
            print("เวลา : ",time_string)


    #****************************************************************************************************************************************************
            #การดึงค่าใส่ sql ของหน้า ล็อกอินแอดมิน

            # ดึงค่า username และ password จาก Entry widgets
   

            # ใช้ค่าที่ดึงมาในคำสั่ง SQL

            c.execute("INSERT INTO admin (Date, Time, Username) VALUES (?,?,?)", (date_string, time_string,username_value))
            conn.commit()

            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
        #*********************************************************************************************************************************************  
            login_window.withdraw()  # ซ่อนหน้าต่าง เมนูแอดมิน ไว้ก่อน
            open_menu_admin()

        else:
            messagebox.showerror("ข้อผิดพลาด", "รหัสผ่านไม่ถูกต้อง")

    #ฟังก์ชั่นปิดหน้าต่างล็อกอินแล้วหน้าต่งหลักขึ้นมา
    def close_login_admin():
        login_window.withdraw()  # ซ่อนหน้าต่างล็อกอิน
        mainwindow.deiconify()  # เปิดหน้าต่างหลัก

    # กำหนดเหตุการณ์เมื่อหน้าต่างล็อกอินถูกปิด
    login_window.protocol("WM_DELETE_WINDOW", close_login_admin)

     # สร้างปุ่ม Login ในหน้าล็อกอิน
    login_button = tk.Button(login_window, text="Login",fg="#591404",font="12",bg="#E4CAB5", command=check_login)
    login_button.place(x=210,y=185)

#ฟังก์ชั่นเปิดหน้าจัดการสินค้า
def open_menu_admin ():
    menu_admin = tk.Toplevel(mainwindow)
    menu_admin.title("เมนูสำหรับแอดมิน")
    menu_admin.geometry("700x500+300+80")
    

    def add_stock():    #เพิ่มสินค้าใน stock
        id_product = id_entry.get()
        product = product_entry.get()   #โค้ดนี้เรียก get() บน product_entry เพื่อรับข้อมูลที่ผู้ใช้ป้อนในช่องป้อนข้อมูลชื่อสินค้า (product) และเก็บข้อมูลในตัวแปร product
        price = price_entry.get()
        quantity = quantity_entry.get()

        named_tuple = time.localtime() # get struct_time
        date_string = time.strftime("%d/%m/%Y", named_tuple)
        time_string = time.strftime("%H:%M",named_tuple)

        
        if id_product.isdigit() :
            if product.strip() :
                if price.isdigit() :
                    if quantity.isdigit() :
                        file_ = filedialog.askopenfilename()      #เปิดหน้าต่างไฟล์เพื่อเลือกไฟล์รูปภาพและเก็บที่อยู่ของไฟล์ที่เลือกในตัวแปร file_
                        if file_:                                 #นี่คือเงื่อนไขที่ตรวจสอบว่าผู้ใช้ได้เลือกไฟล์รูปภาพหรือไม่.
                            with open(file_, 'rb')as file:
                                picture = file.read()
                        if picture:
                            # บันทึกข้อมูลลงในตาราง SQLite
                            c.execute("INSERT INTO products (id_product,date,time, product, price, quantity,picture) VALUES (?,?,?,?,?, ?, ?)",
                                        (id_product,date_string,time_string, product, price, quantity,picture))
                            conn.commit()
                            
                            # ล้างข้อมูลใน Entry Widgets  ล้างข้อมูลที่กรอก
                            id_entry.delete(0, tk.END)
                            product_entry.delete(0, tk.END)
                            price_entry.delete(0, tk.END)
                            quantity_entry.delete(0, tk.END)  

                            show_products_in_store()
                        else:
                            messagebox.showerror("ข้อผิดพลาด", "ไม่มีรูปภาพ")
                    else:
                        messagebox.showerror("ข้อผิดพลาด", "จำนวนไม่ถูกต้อง")
                else:   
                    messagebox.showerror("ข้อผิดพลาด", "ราคาไม่ถูกต้อง")         
            else:   
                messagebox.showerror("ข้อผิดพลาด", "ชื่อสินค้าไม่ถูกต้อง")            
        else:
            messagebox.showerror("ข้อผิดพลาด", "ID สินค้าไม่ถูกต้อง")
            

    z=[]
    def show_products_in_store():  #โชว์สินค้าใน listbox ในร้านค้าหน้าแอดมิน
        frame2_listbox.delete(0, tk.END)   

        c.execute('''SELECT * FROM products''')                        #ดึงข้อมูลสินค้าจากฐานข้อมูลและแสดงข้อมูลเหล่านั้นใน Listbox
        result = c.fetchall()
        i = 1
        z.clear()

        for x in result:
            frame2_listbox.insert(x[0]," ID:  {}    {}    ราคา:  {} จำนวน: {}".format(i,x[3],x[4],x[5]))
            z.append(x[0])
            i+=1
        
            
    def delete_product_from_store():  #ลบสินค้าออกจากร้าน
            try:
                product_idd = frame2_listbox.curselection()     
                
                if not product_idd:
                    messagebox.showinfo(title=None,message="โปรดเลือกสินค้าก่อนลบ")
                    return
                for index in product_idd:
                    if index <0 or index >=len(z):
                    
                        messagebox.showerror(title=None,message=f"Invalid index: {index}")
                        return
                    product_id = z[index] 
                    sure=messagebox.askyesno(title=None,message=f"ยืนยันที่จะลบสินค้าชิ้นที่ {product_id} หรือไม่")
                    if sure == True :
                
                        c.execute("DELETE FROM products WHERE id_product=?", (product_id,))
                        conn.commit()

                        show_products_in_store()
                        messagebox.showinfo(title=None,message=f"ลบสินค้ารหัส {product_id} แล้ว")       
            except sqlite3.Error as e:
                messagebox.showerror(title=None,message=f"sqlite {e}")
    
    def clearentry():
        id_entry.delete(0,tk.END)
        product_entry.delete(0,tk.END)
        price_entry.delete(0,tk.END)
        quantity_entry.delete(0,tk.END)  

    def select_update(event):
        id_entry.delete(0,tk.END)
        product_entry.delete(0,tk.END)
        price_entry.delete(0,tk.END)
        quantity_entry.delete(0,tk.END)   
        update_listbox =[]  
        product_idd = frame2_listbox.curselection()  
        print(product_idd)
        for index in product_idd:
            if index <0 or index >=len(z):
            
                messagebox.showerror(title=None,message=f"Invalid index: {index}")
                return
            product_id = z[index]
            print(product_id)
            c.execute('SELECT product, price, quantity FROM products WHERE id_product = ?',(product_id,))
            results = c.fetchone()
            print(results)
            for i in results:
                update_listbox.append(i)
            print(update_listbox) 
            id_entry.insert(0,product_id)
            product_entry.insert(0,update_listbox[0])
            price_entry.insert(0,update_listbox[1])
            quantity_entry.insert(0,update_listbox[2])

    def update_product(): #อัปเดตสินค้า

            try:

                product_id = id_entry.get()
                new_product = product_entry.get()
                new_price = price_entry.get()
                new_quantity = quantity_entry.get()

                # แปลงค่าให้เป็นตัวเลข
                id_product = convert_to_number(product_id)
                price = convert_to_number(new_price)
                quantity = convert_to_number(new_quantity)
                
                if id_product =="" or new_product == "" or price=="" or quantity=="":
                    messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลสินค้า")            
                else :
                    
                    c.execute("UPDATE products SET product=?, price=?, quantity=? WHERE id_product=?", (new_product, price, quantity, id_product))
                    conn.commit()

                    id_entry.delete(0,tk.END)
                    product_entry.delete(0,tk.END)
                    price_entry.delete(0,tk.END)
                    quantity_entry.delete(0,tk.END)                     
                    messagebox.showinfo(title=None,message=f"อัปเดตสินค้ารหัส {id_product} เรียบร้อยแล้ว")
                    
                    # โชว์ที่อัปเดตไป
                    show_products_in_store()
                
            except sqlite3.Error as e:
                messagebox.showerror(title=None,message=f"sqlite error {e}")

    def new_member ():  # เพิ่มสมาชิก
        tempuser =[]
        def show_member():   # ฟังก์ชั่นโชว์รายชื่อลูกค้า
            
            frame2_member_listbox.delete(0, tk.END)
            c.execute('''SELECT * FROM usermember''')                        #ดึงข้อมูลสินค้าจากฐานข้อมูลและแสดงข้อมูลเหล่านั้นใน Listbox
            result = c.fetchall()
            i = 1
            tempuser.clear()

            for x in result:
                frame2_member_listbox.insert(x[0]," ID:  {}    Usernam: {}   Tel:  {} ".format(i,x[1],x[2],))
                tempuser.append(x[0])
                i+=1
    
        
        def add_user():
            
            #รับค่าเบอร์โทร
            name = username_entry.get()
            
            number = tel_entry.get()           
            print(number)
                
            if number.startswith("0"):
                #messagebox.showinfo("สถานะ", "เบอร์โทรถูกต้อง")
            
                
                code = convert_to_number(number)
                

                # วนลูปผ่านรายการสินค้าและเพิ่มลงใน Listbox

                error_massages=[]
                if not number.isdigit():
                    error_massages.append("เบอร์โทรต้องเป็นตัวเลขเท่านั้น!!!")
            
                if len(number) > 10 :    # len คือขนาดของสิ่งที่อยู่ในวงเล็บ
                    error_massages.append("เบอร์โทรต้องมี 10 หลัก!!!")

                if len(number) < 10 :    # len คือขนาดของสิ่งที่อยู่ในวงเล็บ
                    error_massages.append("เบอร์โทรต้องมี 10 หลัก!!!")
    

                if not error_massages :
                    pass_code = str(code)
                    number = ("0"+ pass_code)
                    c.execute("INSERT INTO usermember (username, Tel) VALUES ( ?, ?)",
                                (name, number))
                    conn.commit()
                
                    tempuser.append(pass_code)
                    
                    username_entry.delete(0,tk.END)
                
                    tel_entry.delete(0,tk.END)  

                    show_member()  #โชว์รายชื่อสมาชิกลูกค้า
                else :
                    # แสดงข้อความข้อผิดพลาด
                    error_message = "\n".join(error_massages)
                    messagebox.showerror("Error", error_message)   

                    # ลบข้อมูลที่กรอกลงในช่อง entry
                    username_entry.delete(0,tk.END)
                    
                    tel_entry.delete(0,tk.END)  
            else:
                messagebox.showerror("ข้อผิดพลาด", "เบอร์โทรไม่ขึ้นต้นด้วย 0")
                # ลบข้อมูลที่กรอกลงในช่อง entry
                username_entry.delete(0,tk.END)
                
                tel_entry.delete(0,tk.END)

            
        def delete_user():

            try:
                user_id = frame2_member_listbox.curselection()
                if not user_id:
                    messagebox.showinfo(title=None,message="โปรดเลือกผู้ใช้ก่อนลบ")
                    return
                for index in user_id:
                    if index <0 or index >=len(tempuser):
                        messagebox.showerror(title=None,message=f"Invalid index: {index}")
                        return
                    user_id = tempuser[index]  


                c.execute("DELETE FROM usermember WHERE id=?", (user_id,))
                conn.commit()

                show_member()

                messagebox.showinfo(title=None,message=f"ลบผู้ใช้ที่ : {user_id} แล้ว")
            except sqlite3.Error as e:
                messagebox.showerror(title=None,message=f"sqlite {e}")

        def back_member():
            menu_admin.withdraw()
            mainwindow.deiconify()
            
        #********* หน้าบริหารลูกค้า ************************************************************************************************************
        frame1_member = tk.Frame(add_member)  # กำหนดสีพื้นหลังของเฟรมแรกเป็นสีน้ำเงิน
        frame1_member.pack(side="left", padx=0, pady=10, fill="both", expand=True) #ใช้ fill="both" และ expand=True เพื่อทำให้เฟรมเต็มขนาดหน้าต่างและขยายเมื่อปรับขนาดหน้าต่าง GUI.
        

        global member_image  #เรียกใช้รูปภาพ
        #พื้นหลังเป็นรูปภาพ
        member_image = tk.PhotoImage(file="bg_member1.png")  # เปลี่ยน "background.png" เป็นชื่อไฟล์รูปของคุณ
        # สร้าง Label แสดงรูปภาพพื้นหลัง
        bgmember_label = tk.Label(frame1_member, image=member_image)
        bgmember_label.place(relwidth=1, relheight=1) 


        username_label = tk.Label(add_member, text="Username:", fg="#FFEFE0",bg="#A73B24",font=10)
        username_label.place(x=19,y=105)
        username_entry = tk.Entry(add_member)
        username_entry.place(x=135,y=110,width=180,height=25)

        tel_label = tk.Label(add_member, text="Tel:",fg="#FFEFE0",bg="#A73B24",font=20)
        tel_label.place(x=50,y=180)
        tel_entry = tk.Entry(add_member)  
        tel_entry.place(x=135,y=180,width=180,height=25)

        #ปุ่มย้อนกลับ
        global pt1_back
        pt1_back = PhotoImage(file="back1.png")
        bt1_back = tk.Button(add_member,image=pt1_back,borderwidth=0,command=back_member)
        bt1_back.place(x=20,y=400)

#------------------------------------------------------------------------------------------------------------------------------------------------
        frame2_member = tk.Frame(add_member, bg="#915A44")  # กำหนดสีพื้นหลังของเฟรมที่สองเป็นสีเขียว
        frame2_member.pack(side="right", padx=0, pady=10, fill="both", expand=True) #ใช้ fill="both" และ expand=True เพื่อทำให้เฟรมเต็มขนาดหน้าต่างและขยายเมื่อปรับขนาดหน้าต่าง GUI.

        global memberf2_image  #เรียกใช้รูปภาพ
        #พื้นหลังเป็นรูปภาพf2_member.png
        memberf2_image = tk.PhotoImage(file="f2_member.png")  # เปลี่ยน "background.png" เป็นชื่อไฟล์รูปของคุณ
        # สร้าง Label แสดงรูปภาพพื้นหลัง
        bgmemberf2_label = tk.Label(frame2_member, image=memberf2_image)
        bgmemberf2_label.place(relwidth=1, relheight=1) 

        frame2_member_listbox=Listbox(frame2_member,width=50,height=20)           
        frame2_member_listbox.place(x=20,y=5) 
        show_member()
       
        
        save_member = tk.Button(frame1_member,text="บันทึก",borderwidth=0,fg="white",bg="#D67968",font=3,command= add_user)
        save_member.place(x=145,y=300)

        delete_member = tk.Button(frame2_member,text="ลบ",borderwidth=0,fg="white",bg="#D67968",font=1,command= delete_user)
        delete_member.place(x=155,y=380) 

    #ฟังก์ชั่นปิดหน้าต่างล็อกอินแล้วหน้าต่งหลักขึ้นมา
    def close_login_admin():
        menu_admin.withdraw()  # ซ่อนหน้าต่างล็อกอิน
        mainwindow.deiconify()  # เปิดหน้าต่างหลัก

    # กำหนดเหตุการณ์เมื่อหน้าต่างล็อกอินถูกปิด
    menu_admin.protocol("WM_DELETE_WINDOW", close_login_admin)
   

    def open_daily():    #ส่วนหน้าของการตรวจสอบรายได้ร้านค้า
        
        # สร้างหน้าต่างในแท็บแรก
        label1 = tk.Frame(watch_daily)
        label1.pack()
        
        global bg_daily
       #พื้นหลังเป็นรูปภาพ
        bg_daily = tk.PhotoImage(file="bg_daily.png")  # เปลี่ยน "background.png" เป็นชื่อไฟล์รูปของคุณ
        # สร้าง Label แสดงรูปภาพพื้นหลัง
        daily_label = tk.Label(watch_daily, image=bg_daily)
        daily_label.place(relwidth=1, relheight=1)

        #สร้างตัวแปรเพื่อเก็บวันที่
        selected_date = tk.StringVar()

        #แสดงประวัติคำสั่งซื้อรายวัน
        def show_daily_orders():
            date = selected_date.get() #ดึงวันที่จากตัวแปร selected_date
            #ดึงข้อมูลจากฐานข้อมูลและคำนวณยอดขายรายวัน
            daily_sales = calculate_daily(date)
           
            #แสดงผลลัพธ์บน Label
            daily_sales_label.config(text=f"ยอดขายวันที่ {date}: {daily_sales}  บาท",bg="#E4CAB5",font=0)
            daily_sales_label.place(x=50, y=95)
           

        #คำนวณยอดขายรายวัน
        def calculate_daily(date):
            c.execute("SELECT SUM(pice) FROM Daily_income WHERE date = ?", (date,)) #วิธีกรอก 12/09/2023
            result = c.fetchone() #fetchone คือการดึงข้อมูล
            return result[0] if result[0] else 0

        #สร้างตัวแปรเพื่อเก็บรายเดือน
        selected_month = tk.StringVar()

        #แสดงประวัติคำสั่งซื้อรายเดือน
        def show_monthly_orders():
            month = selected_month.get()  #ดึงเดือนจากตัวแปร selected_month
            #ดึงข้อมูลจากฐานข้อมูลและคำนวณยอดขายรายเดือน
            monthly_sales = calculate_monthly(month)
            #แสดงผลลัพธ์บน Label
            monthly_sales_label.config(text=f"ยอดขายเดือน {month}: {monthly_sales}   บาท",bg="#E4CAB5",font=0)
            monthly_sales_label.place(x=50, y=220)

        #คำนวณยอดขายรายเดือน
        def calculate_monthly(month):

            c.execute("SELECT SUM(pice) FROM Daily_income WHERE (month) = ?", (month,))  #วิธีกรอก 09/2023
            print(month)
            result = c.fetchone() #fetchone คือการดึงข้อมูล
            print(result)
            return result[0] if result[0] else 0 #ถ้าไม่มีข้อมูลจะขึ้น 0

        def back_daily():
            menu_admin.withdraw()
            mainwindow.deiconify()


        #แสดงผลลัพธ์ของยอดขายรายวัน
        daily_sales_label = tk.Label(watch_daily, text="", font=12)
        daily_sales_label.place(x=785, y=80)

        #สร้างเมนูเลือกวันที่ในแท็บรายวัน
        date_entry = tk.Entry(watch_daily, textvariable=selected_date, font=18,justify="center")
        date_entry.place(x=100, y=120,width=200,height=30)
        #กดรูปภาพเพื่อใช้ฟังก์ชั่นต่อไป
        global sh_day
        sh_day = PhotoImage(file="showday.png")
        day_button = tk.Button(watch_daily,image=sh_day,borderwidth=0,command=show_daily_orders)
        day_button.place(x=120, y=155)

        #แสดงผลลัพธ์ของยอดขายรายเดือน
        monthly_sales_label = tk.Label(watch_daily, text="", font=12)
        monthly_sales_label.pack()

        #สร้างเมนูเลือกเดือนในแท็บรายเดือน 
        month_entry = tk.Entry(watch_daily, textvariable=selected_month, font=18,width=15,justify="center")
        month_entry.place(x=100, y=245,width=200,height=30)
        global sh_month
        sh_month = PhotoImage(file="showmonth.png")
        month_button = tk.Button(watch_daily,image=sh_month,borderwidth=0,command=show_monthly_orders)
        month_button.place(x=110, y=285)
        

        #ปุ่มย้อนกลับ
        global photo_back
        photo_back = PhotoImage(file="back.png")
        back_button = tk.Button(watch_daily,image=photo_back,borderwidth=0,command=back_daily)
        back_button.place(x=30,y=400)

# ---------- การสร้าง แท็ป -------------------------------------------------------------------------------------------------------------------
    
    def back_add_product():
        menu_admin.withdraw()
        mainwindow.deiconify()
   
    global menu_image  # ประกาศตัวแปรเป็น global
    notebook = ttk.Notebook (menu_admin)

    add_product = Frame(notebook)
    add_member = Frame(notebook)
    watch_daily = Frame(notebook)
    
    notebook.add(add_product,text="บริหารสินค้าในร้าน")  
    notebook.add(add_member,text="บริหารรายชื่อลูกค้า")
    notebook.add(watch_daily,text="ตรวจสอบรายได้")
    notebook.pack(expand=True,fill="both")


    #************** เพิ่มสินค้าลงในร้านค้า **********************************************************************************************************
    
    frame1 = tk.Frame(add_product,width=300,height=500,bg="#FFEDDC")  # กำหนดสีพื้นหลังของเฟรมแรกเป็นสีน้ำเงิน
    frame1.pack(side="left", padx=0, pady=10) #ใช้ fill="both" และ expand=True เพื่อทำให้เฟรมเต็มขนาดหน้าต่างและขยายเมื่อปรับขนาดหน้าต่าง GUI.

    #พื้นหลังเป็นรูปภาพ
    menu_image = tk.PhotoImage(file="bgframe1.png")  # เปลี่ยน "background.png" เป็นชื่อไฟล์รูปของคุณ
    # สร้าง Label แสดงรูปภาพพื้นหลัง
    bgmenu_label = tk.Label(frame1, image=menu_image)
    bgmenu_label.place(relwidth=1, relheight=1)


    id_label = tk.Label(add_product,text="รหัสสินค้า", fg="#FFEFE0",bg= "#D67968",font=1)
    id_label.place(x=25,y=85)
    id_entry = tk.Entry(frame1)
    id_entry.place(x=125,y=80)

    product_label = tk.Label(add_product, text="ชื่อสินค้า", fg="#FFEFE0",bg= "#D67968",font=1)
    product_label.place(x=28,y=130)
    product_entry = tk.Entry(frame1)
    product_entry.place(x=120,y=125)

    price_label = tk.Label(add_product, text="ราคาสินค้า", fg="#FFEFE0",bg= "#D67968",font=1)
    price_label.place(x=18,y=180)
    price_entry = tk.Entry(frame1)
    price_entry.place(x=125,y=175)

    quantity_label = tk.Label(add_product, text="จำนวนสินค้า", fg="#FFEFE0",bg= "#D67968",font=1)
    quantity_label.place(x=15,y=225)
    quantity_entry = tk.Entry(frame1)
    quantity_entry.place(x=125,y=220)

    saveadd = Button(frame1,text="เพิ่ม",borderwidth=0,fg="black",bg="#F4B18F",font=1,command=add_stock)
    saveadd.place(x=70,y=300)

    #ปุ่มย้อนกลับ
    global pt_back
    pt_back = PhotoImage(file="back1.png")
    bt_back = tk.Button(add_product,image=pt_back,borderwidth=0,command=back_add_product)
    bt_back.place(x=20,y=400)
    

    # สร้างเฟรมที่ 2 ------------------------------------------------------------------------------------------------------------------------
    global f2_image  # ประกาศตัวแปรเป็น global

    frame2 = tk.Frame(add_product,bg="#C3714B")  # กำหนดสีพื้นหลังของเฟรมที่สองเป็นสีเขียว
    frame2.pack(side="right", padx=0, pady=10, fill="both", expand=True) #ใช้ fill="both" และ expand=True เพื่อทำให้เฟรมเต็มขนาดหน้าต่างและขยายเมื่อปรับขนาดหน้าต่าง GUI.
    #พื้นหลังเป็นรูปภาพ
    f2_image = tk.PhotoImage(file="bgframe2.png")  # เปลี่ยน "background.png" เป็นชื่อไฟล์รูปของคุณ
    # สร้าง Label แสดงรูปภาพพื้นหลัง
    bgf2_label = tk.Label(frame2, image=f2_image)
    bgf2_label.place(relwidth=1, relheight=1)

    frame2_listbox=Listbox(frame2,width=60,height=20)           
    frame2_listbox.place(x=15,y=15) 
    frame2_listbox.bind('<Double-Button>',select_update)

    delete = tk.Button(frame2,text="ลบ",borderwidth=0,fg="white",bg="#AD5545",font=1,command = delete_product_from_store)
    delete.place(x=180,y=355)  
    show_products_in_store()

    #********** อัปเดตสินค้า *************************************************************************************************************
    save_update = tk.Button(frame1,text="อัปเดต",borderwidth=0,fg="black",bg="#F4B18F",font=1,command = update_product)
    save_update.place(x=190,y=300) 
    
    #****** ลบช่องที่กรอกข้อมูล *************************************************************************************************************************
    clear = tk.Button(frame1,text="เคลียร์",borderwidth=0,fg="black",bg="#F4B18F",font=1,command = clearentry)
    clear.place(x=130,y=345) 

    #******** เพิ่มสมาชิกลูกค้า **********************************************************************************************************
    new_member()

    #********* ตรวจสอบรายได้ *************************************************************************************************************
    open_daily()


########### ระบบร้านค้า #######################################################################################################################################

order_items = []        #เก็บรายการสินค้า
cart_product =[]        #รายการสินค้าที่ถูกเพิ่มลงในตะกร้า
total_price = 0         #เก็บยอดรวม
tempproduct=[]          #เพื่อเก็บข้อมูลชั่วคราวก่อนที่จะถูกเพิ่มใน cart_product


# ฟังก์ชันแสดงรายการหนังสือและเพิ่มสินค้า
def open_books():
    
    def on_mousewheel(event):      #ฟังก์ชั่นการเลื่อนล้อเมาส์
        canvas.yview_scroll(int(-1*(event.delta/120)), "units") #คำสั่งเลื่อนเนื้อหา

    book_window = tk.Toplevel(mainwindow)
    book_window.title("รายการหนังสือ")
    # กำหนดขนาดความกว้างและความยาวของหน้าต่างรายการหนังสือ
    book_window.geometry("1300x700+200+65")
    screenwidth = book_window.winfo_screenwidth()
    screenheight = book_window.winfo_screenheight()
    book_window.resizable(False, False)


    deletecart() #ฟังก์ชั่นใช้ในการลบสินค้า
     
    canvas = tk.Canvas(book_window, bg="#FFDEC0", scrollregion=(0, 0, 700, 5000))  #กล่องตรงกลาง
    canvas.place(x=450,y=0, width=850, height=700)
    product = tk.Frame(canvas, bg="#FFDEC0") 
    canvas.create_window((0, 0), window=product, anchor='nw')

    book_window.bind("<MouseWheel>", on_mousewheel)     # ทำให้เป็นกล่องข้อมูลที่สามารถเลื่อนได้  

    f1 = tk.Frame(book_window)  # กำหนดสีพื้นหลังของเฟรมที่สองเป็นสีเขียว
    f1.place(width=453,height=1000)

    global f1_image
    #พื้นหลังเป็นรูปภาพ
    f1_image = tk.PhotoImage(file="bg_shhhhh.png")  # เปลี่ยน "background.png" เป็นชื่อไฟล์รูปของคุณ
    # สร้าง Label แสดงรูปภาพพื้นหลัง
    bgf1_label = tk.Label(f1, image=f1_image)
    bgf1_label.place(width=453,height=700)


    mainwindow.withdraw() #ซ่อนหน้าต่่าง root


    def show_cart():                               #เเสดงสินค้าในตะกร้า
        global product_name,quantity_now           #สร้างตัวเเปร
        show_listbox.delete(0,tk.END)              #ลบรายการในลิสบ๊อก
        c.execute("SELECT  cart_id,Name_product, Price,quantity FROM cart ")
        product_incart = c.fetchall()              #การดึงข้อมูลSQLเเล้วมาเก็บไว้
        for x in product_incart:                   #วนลูปผ่านรายการสินค้าในตะกร้าที่ได้จากฐานข้อมูล
            
            id_product,product_name, price,quantity_now = x         #เพื่อเก็บค่า
            tempproduct.append(id_product)            
            item_text = f"{product_name} ราคา: {price} บาท จำนวน: {quantity_now}"     #ชื่อสินค้า ราคา จำนวน
            show_listbox.insert(tk.END, item_text) #tk.END เพื่อให้ข้อมูลถูกเพิ่มไปด้านล่างของ Listbox.        
                 
    def delete_cart():  #ลบของในตะกร้า
        try:
                cart_idd = show_listbox.curselection()      #รับรายการสินค้า
                print(cart_idd)
                if not cart_idd: 
                    messagebox.showinfo(title=None,message="โปรดเลือกสินค้าก่อนลบ")
                    return
                for index in cart_idd:                     
                    print(tempproduct)     
                    id_cart = tempproduct[index]            
                    print(id_cart)


                    c.execute("SELECT  quantity FROM products WHERE product=?",(product_name,))   #เพิ่มเข้าตาราง
                    quantity_instore = c.fetchall()         #ดึงจำนวนสินค้ามาไว้ใน
                    print(quantity_instore[0][0])   
                    new_quantity = quantity_now+quantity_instore[0][0]
                    print(new_quantity)
                    c.execute("UPDATE products SET quantity=? WHERE product=?", (new_quantity, product_name,))
                    c.execute("DELETE FROM cart WHERE cart_id=?", (id_cart,))
                    conn.commit()
                    
                    # ลบรายการที่เลือกจาก Listbox
                    show_listbox.delete(index) 
                    tempproduct.clear()      #ลบรายการในลิส
                    
                    order_show_product()  #อัปเดตรายการที่จากลบไปเเล้ว
                
                    show_cart()

                #messagebox.showinfo(title=None,message=f"ลบสินค้ารหัส {id_cart} แล้ว")
        except sqlite3.Error as e:
                messagebox.showerror(title=None,message=f"sqlite {e}")


        
    def order_show_product():
            c = conn.cursor()
            c.execute("SELECT id_product, product, price, quantity, picture FROM products ")
            conn.commit()  
            pictures = c.fetchall()
            
            
            def addtocart(item): #ฟังก์ชันที่รับข้อมูลรายการเพื่อเเสดงข้อมูลหรือภาพของสินค้า
                
                def add():      #เพิ่มสินค้าลงในตะกร้า
                    
                    quantityincart=simpledialog.askinteger("Input", "กรอกข้อความ:")  #เเสดงข้อความให้ผู้ใช้กรอก
                    selected_product=item[0]     #เก็บรหัสสินค้า
                    print(item[0])
                    available_quantity = item[3]    #เก็บสินค้าที่เหลือในสต็อก
                    print(item[3])
                    if quantityincart <= available_quantity:   #ตรวจสอบจำนวนสินค้า
                        new_quantity = available_quantity - quantityincart   
                        c.execute("UPDATE products SET quantity=? WHERE id_product=?", (new_quantity, selected_product))
                    
                        c.execute("INSERT INTO cart (Name_product,Price,quantity) VALUES (?, ?,?)", (item[1], item[2],quantityincart))
                        conn.commit() 
                        order_show_product()
                        add_cart()    
                        show_cart()
                    else:
                        messagebox.showerror(title=None,message=f"สินค้าไม่เพียงพอ")
                return add

            for i, x in enumerate(pictures):    #แปลงภาพ
                image = Image.open(BytesIO(x[4]))
                target_width, target_height = 200, 300  #ปรับความกว้างและความยาวของ product
                image = image.resize((target_width, target_height))   #ปรับขนาดรูปภาพให้ตรงกับขนาดเป้าหมาย
                image = ImageTk.PhotoImage(image)    #แปลงรูปภาพ Pillow เป็น ImageTk.PhotoImage

                custom3_font = tkFont.Font(size=11) 
                label = Button(product, image=image, text=" {} \n{} บาท จำนวน:{} ".format(x[1], x[2],x[3]), compound="top", command=addtocart(x),  fg="#EFE9CE",bg="#A6744C",font=custom3_font, width=250, height=358)  #ปรับขนาดปุ่ม
                label.image = image
                label.grid(row=i // 3, column=i % 3, padx=10, pady=10)

    #การเลื่อนล้อเมาส์ขึ้นหรือลง, canvas.yview_scroll จะถูกเรียกเพื่อเลื่อน Canvas ตามทิศทางและปริมาณที่เลื่อนมา.
    

    order_show_product()


    #แสดงสินค้าที่เพิ่มจากแอดมิน
    for item in order_items:
        item_label = Label(book_window, text=f"{item['name']} - {item['price']} บาท", font=('arial', 12), bg='#E6E6E6')
        item_label.place(x=400)

    
    # ฟังก์ชันสำหรับเปิด messagebox ที่ให้กรอกข้อความ
    '''def open_input_dialog(x):
        result = simpledialog.askinteger("Input", "กรอกข้อความ:")
        if result:
            print("ข้อความที่คุณกรอกคือ:", result)
        else:
            print("คุณยกเลิกหรือไม่กรอกข้อความ") '''
    update_listboxf1 =[] 
    def select_updatecart(event): #ฟังก์ชั่นดับเบิ้ลคลิ๊ก
        global upproduct_id
         
        product_quantity = show_listbox.curselection()  
        print(1234567)
        print(product_quantity)
        for index in product_quantity:
            if index <0 or index >=len(tempproduct):
            
    
                messagebox.showerror(title=None,message=f"Invalid index: {index}")
                return
            print(tempproduct)
            print(index)
            upproduct_id = tempproduct[index]
            print(upproduct_id)
            c.execute('SELECT Name_product,quantity FROM cart WHERE cart_id = ?',(upproduct_id,))
            results = c.fetchone()
            print(results)
            for i in results:
                update_listboxf1.append(i)
            print(update_listboxf1) 
           
            quantitycart_entry.insert(0,update_listboxf1[1])  #แสดงค่าใน entry
            

        def updatecartplus():
            try:
                new_quantitycart = quantitycart_entry.get()
                new_quantity = convert_to_number(new_quantitycart)
                if update_listboxf1[1] <new_quantity:
                    quantity=new_quantity-update_listboxf1[1]

                    print(quantity)
                    c.execute("UPDATE cart SET quantity=? WHERE cart_id=?", ((update_listboxf1[1]+quantity), upproduct_id,))

                    c.execute("SELECT  quantity FROM products WHERE product=?",(update_listboxf1[0],))   #เพิ่มเข้าตาราง
                    quantity_instore = c.fetchall()         #ดึงจำนวนสินค้ามาไว้ใน
                    print(quantity_instore[0][0])   
                    new_quantity = quantity_instore[0][0]-(quantity)
                    print(new_quantity)
                    c.execute("UPDATE products SET quantity=? WHERE product=?", (new_quantity, update_listboxf1[0],))

                    quantitycart_entry.delete(0,tk.END)                     
                    #messagebox.showinfo(title=None,message=f"อัปเดต0eo;o {id_product} เรียบร้อยแล้ว")
                    tempproduct.clear()
                    update_listboxf1.clear()
                    # โชว์ที่อัปเดตไป
                    show_cart()
                    order_show_product()

                elif update_listboxf1[1] >new_quantity: 
                    quantity=new_quantity-update_listboxf1[1]

                    print(quantity)
                    c.execute("UPDATE cart SET quantity=? WHERE cart_id=?", ((update_listboxf1[1]+quantity), upproduct_id,))

                    c.execute("SELECT  quantity FROM products WHERE product=?",(update_listboxf1[0],))   #เพิ่มเข้าตาราง
                    quantity_instore = c.fetchall()         #ดึงจำนวนสินค้ามาไว้ใน
                    print(quantity_instore[0][0])   
                    new_quantity = quantity_instore[0][0]-(quantity)
                    print(new_quantity)
                    c.execute("UPDATE products SET quantity=? WHERE product=?", (new_quantity, update_listboxf1[0],))

                    quantitycart_entry.delete(0,tk.END)                     
                    #messagebox.showinfo(title=None,message=f"อัปเดต0eo;o {id_product} เรียบร้อยแล้ว")
                    tempproduct.clear()
                    update_listboxf1.clear()
                    # โชว์ที่อัปเดตไป
                    show_cart()
                    order_show_product()

            except sqlite3.Error as e:
                    messagebox.showerror(title=None,message=f"sqlite error {e}")

            
        global edit1  #เพิ่มจำนวนสินค้า
        edit1 = PhotoImage(file="edit.png")
        edit1_button = tk.Button(f1,image=edit1,highlightthickness=0,border=0,borderwidth=0,command=updatecartplus)
        edit1_button.place(x=195,y=420)



    def add_cart():  #เพิ่มสินค้าลงตะกร้า

        global total_price
        
        cart_product.clear()
        c.execute("SELECT * FROM cart ")
        order = c.fetchall()
        print(order)
        item_name=order[0][1]
        print(item_name)
        item_price=order[0][2]
        print(item_price)

        for item_name in order:
    
            cart_product.append((item_name,item_price))
          
    
    def calculater():  #เมนูคิดบิลลูกค้า
    
        total_window = tk.Toplevel(mainwindow)
        total_window.title("ชำระเงิน")
        total_window.geometry("600x700+480+50")
        
        #book_window.withdraw() #ซ่อนหน้าต่่าง 

        global receipt_image  # ประกาศตัวแปรเป็น global
    #พื้นหลังเป็นรูปภาพ
        receipt_image = tk.PhotoImage(file="bg.ชำระเงิน.png")  # เปลี่ยน "background.png" เป็นชื่อไฟล์รูปของคุณ

        # สร้าง Label แสดงรูปภาพพื้นหลัง
        bglogin_label = tk.Label(total_window, image=receipt_image)
        bglogin_label.place(relwidth=1, relheight=1)
        
        


        def total_product():
            named_tuple = time.localtime() # get struct_time
            date_string = time.strftime("%d/%m/%Y", named_tuple)
            month_string = time.strftime("%m/%Y",named_tuple)
            time_string = time.strftime ("%H:%M",named_tuple)
            print("วันที่ : ",date_string)
            print("เดือน : ",month_string)

            c.execute("SELECT Name_product,Price,quantity FROM cart ")
            result=c.fetchall()
            total_price = 0

           

            receipt = f"รายการทั้งหมด\n\n"
            print(result)  
            for item, price,quantity in result:
                allprice = price*quantity           #คำนวณราคา
                receipt += f"{item}           {allprice:.2f} บาท\n"     
                allprice = convert_to_number(allprice)
                total_price = total_price + allprice

            tatol_final=total_price-discout
            receipt += f"\n\n\nยอด               {total_price:.2f}  บาท\n"
            receipt+= f"\nส่วนลดสมาชิก             {discout:.2f}     บาท\n"
            receipt+= f"\n\nยอดรวม                {tatol_final:.2f} บาท\n"
            receipt += f"\nวันที่: {date_string}        {time_string}"

            receipt_label = Label(total_window, text=receipt, font=("Arial", 12),bg="#FFFBF7",anchor='n')
            receipt_label.place(x=100,y=20,width=400,height=500)


            def clear_listbox():  #เคลียร์ listbox
                for product_name,price_product,quantity_product in result:
                    c.execute("SELECT  SUM(quantity) FROM cart WHERE Name_product=?",(product_name,))
                    quantity_incart = c.fetchall()                
                    c.execute("SELECT  quantity FROM products WHERE product=?",(product_name,))
                    quantity_instore = c.fetchall()
                    print(quantity_instore[0][0])
                    new_quantity = quantity_incart[0][0]+quantity_instore[0][0]
                    print(new_quantity)
                    c.execute("UPDATE products SET quantity=? WHERE product=?", (new_quantity, product_name,))
                c.execute("DELETE FROM cart" )
                conn.commit()
                order_show_product()
                show_cart()
                total_window.withdraw()
                    # ฟังก์ชันสำหรับลบสินค้าออกจากตะกร้า

            def submit():   #เเสดงใบเสร็จเมื่อกดเสร็จสิ้น
                
                total_window.withdraw()
                c.execute("INSERT INTO Daily_income (list,pice,date,month) VALUES (?,?,?,?)", (receipt,tatol_final,date_string,month_string))
                conn.commit() 
                order_show_product()
                show_cart()
                show_listbox.delete(0, tk.END)
                #total_window.withdraw()  # ปิดหน้าต่างbill 

                def receipt_sh():  #ใบเสร็จ
                    receipt_window = tk.Toplevel(mainwindow)
                    receipt_window.title("ชำระเงิน")
                    receipt_window.geometry("400x500+480+50")
                        
                    named_tuple = time.localtime() # get struct_time
                    date_string = time.strftime("%d/%m/%Y", named_tuple)
                    month_string = time.strftime("%m/%Y",named_tuple)
                    time_string = time.strftime ("%H:%M",named_tuple)
                    print("วันที่ : ",date_string)
                    print("เดือน : ",month_string)

                    c.execute("SELECT Name_product,Price,quantity FROM cart ")
                    result=c.fetchall()
                    total_price = 0

                    

                    receipt = f"ใบเสร็จ\n\n"
                    print(result)  
                    for item, price,quantity in result:
                        allprice = price*quantity
                        receipt += f"{item}           {allprice:.2f} บาท\n"     
                        allprice = convert_to_number(allprice)
                        total_price = total_price + allprice

                    tatol_final=total_price-discout
                    receipt += f"\n\n\nยอด               {total_price:.2f}  บาท\n"
                    receipt+= f"\nส่วนลดสมาชิก             {discout:.2f}     บาท\n"
                    receipt+= f"\n\nยอดรวม                {tatol_final:.2f} บาท\n"
                    receipt += f"\nวันที่: {date_string}        {time_string}"

                    receipt_label = Label(receipt_window,text=receipt, font=("Arial", 12),bg="#FFFBF7",anchor='n')
                    receipt_label.place(x=0,y=0,width=400,height=500)

                    c.execute("DELETE FROM cart")
                    conn.commit()


                receipt_sh()
                    
                    
            
            finish = tk.Button(total_window,text="เสร็จสิ้น",borderwidth=0,fg="white",bg="#AD5545",font=1,command=submit)
            finish.place(x=350,y=380)   

            cancel = tk.Button(total_window,text="ยกเลิก",borderwidth=0,fg="white",bg="#AD5545",font=1,command=clear_listbox)
            cancel.place(x=180,y=380)
        total_product()


    #ฟังก์ชั่นปิดหน้าต่างล็อกอินแล้วหน้าต่งหลักขึ้นมา
    def close_menu_admin():
        book_window.withdraw()  # ซ่อนหน้าต่างล็อกอิน
        mainwindow.deiconify()  # เปิดหน้าต่างหลัก  

    # กำหนดเหตุการณ์เมื่อหน้าต่างล็อกอินถูกปิด
    #book_window.protocol("WM_DELETE_WINDOW", close_login_admin)

    def check_cal():
        global discout
        check_discourt=simpledialog.askstring("Input", "กรอกเบอร์โทร:")       
        if not check_discourt :     #กรณีไม่กรอกเบอร์โทร
            discout = 0
            calculater()

        elif check_discourt:      #ในกรณีที่กรอกเบอร์โทร
            print("00000000")
            c.execute("SELECT * FROM usermember WHERE Tel = ?",(check_discourt,))
            conn.commit()  
            tel_user = c.fetchall()
            discout = 0
            if tel_user:   #ตรวจสอบว่ามีเบอร์ผู้ใช้
                discout = 50  
                calculater()

            else:
                messagebox.showerror("ข้อผิดพลาด", "ไม่พบสมาชิก")   


    def back_tocart():
        book_window.withdraw()
        mainwindow.deiconify()

    quantitycart_entry = tk.Entry(f1)  
    quantitycart_entry.place(x=110,y=378,width=180,height=28)

    show_listbox=Listbox(f1,width=68,height=20)           
    show_listbox.place(x=20,y=30)
    show_listbox.bind('<Double-Button>',select_updatecart)
    
    global delete_tocart  #ลบสินค้าในตะกร้า
    delete_tocart = PhotoImage(file="dl_sh.png")
    exit_button = tk.Button(f1,image=delete_tocart,highlightthickness=0,border=0,borderwidth=0,command=delete_cart)
    exit_button.place(x=180,y=480)


    global pay  #ชำระเงิน
    pay = PhotoImage(file="receipt_sh.png")
    pay_button = tk.Button(f1,image=pay,highlightthickness=0,border=0,borderwidth=0,command=check_cal)
    pay_button.place(x=180,y=545)


    
    #ปุ่มย้อนกลับ
    global ct_back
    ct_back = PhotoImage(file="back1.png")
    ct_back_bt = tk.Button(f1,image=ct_back,borderwidth=0,command=back_tocart)
    ct_back_bt.place(x=20,y=600)

def open_developer():   #หน้าผู้พัฒนา
    
    developer = tk.Toplevel(mainwindow) 
    developer.title("ผู้พัฒนาโปรแกรม")
    developer.geometry("700x500+350+80")

    mainwindow.withdraw() #ปิดหน้าหลักลง

    #พื้นหลังเป็นรูปภาพ
    global im_developer
    im_developer = tk.PhotoImage(file="bg.ผู้พัฒนา.png")  # เปลี่ยน "background.png" เป็นชื่อไฟล์รูปของคุณ

    # สร้าง Label แสดงรูปภาพพื้นหลัง
    developer_label = tk.Label(developer, image=im_developer)
    developer_label.place(relwidth=1, relheight=1)

    #ฟังก์ชั่นปิดหน้าต่างล็อกอินแล้วหน้าต่งหลักขึ้นมา
    def close_developer():
        developer.withdraw()  # ซ่อนหน้าต่างล็อกอิน
        mainwindow.deiconify()  # เปิดหน้าต่างหลัก

    # กำหนดเหตุการณ์เมื่อหน้าต่างล็อกอินถูกปิด
    developer.protocol("WM_DELETE_WINDOW", close_developer)

   
def close_root():
    #หน้ายืนยันการออกจากโปรแกรม
    confirm = messagebox.askquestion("ยืนยัน", "+ ?")
    if confirm == "yes":
        #root.destroy()
        mainwindow.deiconify()

def delete_daily ():  #ลบสินค้าในตะกร้าที่จะใช้นำมาทำรายได้รายวัน รายเดือน
    c.execute("DELETE FROM Daily_income")
    conn.commit()

def deletecart ():  
    c.execute("DELETE  FROM cart")
    conn.commit()

def delete_admin ():  #ลบสินค้าในตะกร้าที่จะใช้นำมาทำรายได้รายวัน รายเดือน
    c.execute("DELETE FROM admin")
    conn.commit()

#หน้ายืนยันการออกจากโปรแกรม
def exitall():
    confirm = messagebox.askquestion("ยืนยัน", "คุณต้องการปิดโปรแกรมหรือไม่ ?")
    if confirm == "yes":
        mainwindow.destroy()

#delete_daily()
#deletecart()
#delete_admin()

# สร้างหน้าต่างหลัก
mainwindow=tk.Tk()
mainwindow.title("READ HEAL")

#การกำหนดขนาดหน้าจอ
mainwindow.geometry("800x500+280+100")   #ปรับแนวตั้งคือ กXย=800x500  ปรับแนวนอนคือ +280+100 แกน x แกน y

#พื้นหลังเป็นรูปภาพ
bg_image = tk.PhotoImage(file="สำเนาของ bg1.png")  # เปลี่ยน "background.png" เป็นชื่อไฟล์รูปของคุณ

# สร้าง Label แสดงรูปภาพพื้นหลัง
background_label = tk.Label(mainwindow, image=bg_image)
background_label.place(relwidth=1, relheight=1)

#กดรูปภาพเพื่อใช้ฟังก์ชั่นต่อไปในหน้าหลัก
global shop_img   #ร้านค้า
shop_img = PhotoImage(file="shopbutton.png")
shop_button = tk.Button(mainwindow,image=shop_img,bg="#915A44",highlightthickness=0,border=0,borderwidth=0,command=open_books)
shop_button.place(x=10,y=2)

global admin_img  #แอดมิน
admin_img = PhotoImage(file="adminbutton.png")
bt_admin = tk.Button(mainwindow,image=admin_img,bg="#915A44",highlightthickness=0,border=0,borderwidth=0,command=open_login_admin)
bt_admin.place(x=200,y=5)

#ปุ่มผู้พัฒนาโปรแกรม
global ph_developer                  #เรียกใช้รูปภาพ
ph_developer = tk.PhotoImage(file="Developerbutton.png")  # เปลี่ยน "background.png" เป็นชื่อไฟล์รูปของคุณ
# สร้าง Label แสดงรูปภาพพื้นหลัง
developer_button = tk.Button(mainwindow, image=ph_developer,highlightthickness=0,borderwidth=0,command=open_developer)
developer_button.place(x=400,y=3)

global exit  #ออกจากโปรแกรม
exit = PhotoImage(file="logout.png")
exit_button = tk.Button(mainwindow,image=exit,bg="#915A44",highlightthickness=0,border=0,borderwidth=0,command=exitall)
exit_button.place(x=600,y=3.5)

#-----------------------------------------------------------------------------------------------------------------------------------------------

mainwindow.mainloop()

