from hashlib import sha256
from os import remove,path,chdir
from time import sleep
from threading import Thread
from tkinter import filedialog,messagebox
from PIL import Image,ImageTk
import ttkbootstrap as ttk
from random import randrange
running=[False,]
config=["_lock","Texte",False]
mode=["_bah_je_sais_pas_encore_Mr_l_'_utilisateur_","pareil_oh_mon_cerveau_est_vide","..."]
def Translate():
    if config[2]:
        texte_0="Text"
        texte_1="Image"
        texte_2="Audio"
        texte_3="Video"
        texte_4="Choisir"
        texte_5="Mot de passe"
        texte_6="Analyse"
        texte_7="Protéger"
        texte_8="Verrouiller"
        texte_9="Deverrouiller"
        texte_10="Ouvrir"
        texte_11="Selectionner un fichier "+config[1]
        texte_12="En cours"
    else:
        texte_0="Text"
        texte_1="Image"
        texte_2="Audio"
        texte_3="Video"
        texte_4="Choice"
        texte_5="Password"
        texte_6="Analyse"
        texte_7="Secure"
        texte_8="Lock"
        texte_9="Unlock"
        texte_10="Open"
        texte_11="Select an "+config[1]+" file"
        texte_12="Process"
    
    Trans=[texte_0,texte_1,texte_2,texte_3,texte_4,texte_5,texte_6,texte_7,texte_8,texte_9,texte_10,texte_11,texte_12]
    return Trans
chdir("ressources")

def estim_unit(size):
    a=0
    if 1024<size:
        unit="Ko"
        size_=size/1024
        a=1
    if(1024*1024)<size:
        unit="Mo"
        size_=size/(1024*1024)

    if (1024*1024*1024)<size:
        unit="Go"
        size_=size/(1024*1024*1024)
        a=1
    if size< 1024:
        unit="octet"
        size_=size
    estimation= str(round(size_,2))+" "+unit
    return estimation



def update_monitor(origin,child,level):
    bar['value']=level
    lab9.config(text=str((estim_unit(child))+"/"+(estim_unit(origin))+" ||"+str(level)+"%"))

def about_Fred():
    text_1="Secure a été developper par Achméle@Fred Tout Droits Reservés"
    text_2="Merci d'utiliser 'Secure'"
    red="red"
    yellow="yellow"
    bg="black"
    bg=bg
    fred=ttk.Window(title="About Secure",resizable=(False,False))
    label=ttk.Label(fred,text="",font=("Bold",10),foreground=red,background=bg)
    label.config(text=text_1)
    label.place(x=10,y=10)
    fred.config(background=bg)
    label2=ttk.Label(fred,text="",font=("Bold",20),foreground=yellow,background=bg)
    label2.config(text=text_2)
    label2.place(x=60,y=100)
    fred.geometry("700x200")
    fred.after(10000,fred.destroy)
    fred.mainloop()

def monitor(fst,scd):
    while running[0]:
        sleep(.300)
        try:
            origin=path.getsize(fst)
            child=path.getsize(scd)
            if origin== 0 and child ==0:
                pass
            else:
                centper=int((child/origin)*100)
                config.append(centper)
                print(str(round((child/(1024*1024)),2))+"Mo/"+str(round((origin/(1024*1024)),2))+"Mo -- "+str(centper)+"% ")
                update_monitor(origin,child,centper)
        except:exit




def alert(message):
    messagebox.showerror("Secure",message)
def resize_img(file,height,width):
        image=Image.open(file)
        image=image.resize((height,width))
        return ImageTk.PhotoImage(image)
    


def encrypt(key,file_in,file_out,run_monitor=False):
    off((but5,but6,but7,but1,but2,but3,but8))
    bar["value"]=0
    keys=sha256((key).encode("UTF-8")).digest()
    with open (file_in,"rb") as src:
        running[0]=True
        with open(file_out,"wb") as out:
            a=0
            if run_monitor :
                    run_thread(monitor,(file_in,file_out),"4")
                    but5.config(text="",command=que_dalle,state="disabled")
                    lab9.place(x=285,y=320)
                    bar.place(x=240,y=300)
                    run_thread(txt_add,("En cours",but5,.100,False),"5")
            while src.peek():
                b=ord(src.read(1))
                c=a%len(keys)
                d=bytes([b^keys[c]])
                out.write(d)
                a=a+1
            running[0]=False

    on((but5,but6,but7,but3,but2,but1,but8))
    if run_monitor:
        sleep(1)
        but5.config(text="Terminer",command=clean_all)
    
    if mode[0]=="_lock":
        but5.config(image=img_lock,compound="right")
    if mode[0]=="un_lock":
        but5.config(image=img_unlock,compound="right")
            




def convert_to_txt(file,out):
    with open (file,"rb") as document:
        content=document.read() 
    with open (out+".txt","wb") as document:
        document.write(content)



def convert_to_mp4(file,out,ext):
    with open (file,"rb") as document:
        content=document.read() 
    with open (out+"."+ext,"wb") as document:
        document.write(content)



def extrat_content(file):
    with open(file,"rb") as doc:
        return doc.read()



def extrat_info(file,mode):
    with open(file,mode) as doc:
        info=[]
        for elts in doc.readlines()[0].split("Midnight"):
            info.append(elts)
        return info


def  extrat_password_S(file,mode):
    with open(file,mode) as doc:
        return doc.readlines()[0]



def clean(targets):
    for target in targets:
        remove(target)



def add_password(file,password):
    with open(file,"rb") as doc:
        content=doc.read()
    with open(file,'wb') as doc:
        print(password)
        doc.write(password+b'\n'+content)
        


def delete_password(file):
    but5.config(text="Analyse")
    with open(file,'rb') as doc:
        content=doc.readlines()
    with open (file,"wb") as doc:
        doc.writelines(content[1:])


def creat_file(file,content,mode):
    with open( file,mode) as doc:
        doc.write(content)


def lock_vid(file,password):
    garbage=[]
    password=str(password)
    print("convertion..")
    convert_to_txt(file,"extrat")
    print("locking")
    encrypt(password,"extrat.txt",file.split(".")[0],True)
    creat_file("pass",password+" Midnight "+ file.split(".")[-1],"w")
    
    encrypt(password,"pass","word")
    password=extrat_password_S("word","rb")
    garbage.append("word")
    garbage.append("pass")
    add_password(file.split(".")[0],password)
    garbage.append("extrat.txt")
    garbage.append(file)
    print("locking done")
    clean(garbage)



def unlock_vid(file,password):
    garbage=[]
    password=str(password)
    secret_code=extrat_password_S(file,"rb")
    
    creat_file("word",secret_code,"wb")
    encrypt(password,"word","password")
    
    info=extrat_info("password","r")
    
    secret_code=info[0]
    print("1")
    garbage=[]
    if secret_code[:-1]!= password:
        print("not the same password")
        alert("Une erreur est survenue lors de l'analyse du mot de passe")
        put.delete(0,ttk.END)
    else:
        print("1")
        
        delete_password(file)
        
        print("okay")
        print(secret_code,":::",password)
        print("unlocking")
        print("ok")
        encrypt(password,file,"decrypt.txt",True)
        print("convertion..")
        convert_to_mp4("decrypt.txt",file.split(".")[0],info[1][1:][:-1])
        garbage.append("decrypt.txt")  
        print("unlocking done.")    
        # sleep(.200)
        garbage.append(file)
    garbage.append("password")
    garbage.append("word")
    clean(garbage)



def lock_img(file,password):
    garbage=[]
    creat_file("pass",password+" Midnight "+file.split(".")[-1],"w")
    encrypt(password,"pass","word")
    info=extrat_password_S("word","rb")
    encrypt(password,file,file.split(".")[0],True)
    add_password(file.split(".")[0],info)
    
    garbage.append("pass")
    garbage.append(file)
    garbage.append("word")
    clean(garbage)


def unlock_img(file,password):
    
    
    garbage=[]
    
    info=extrat_password_S(file,"rb")
    
    creat_file("pass",info,"wb")
    
    encrypt(password,"pass","word")
    info=extrat_info("word","r")
    secret_code=info[0]
    print(info)
    print(password==secret_code[:-1])
    garbage=[]
    
    if password==secret_code[:-1]:
        delete_password(file)
        encrypt(secret_code[:-1],file,"decrypt.txt",True)
        convert_to_mp4("decrypt.txt",file,info[1][:-1][1:])
        garbage.append(file)
        garbage.append("decrypt.txt")
    else:
        print("Not the same password")
        alert("Une erreur est survenue lors de l'analyse du mot de passe")

        put.delete(0,ttk.END)

        
    garbage.append("pass")
    garbage.append("word")
    # garbage.append("password")
    clean(garbage)
    




def txt_add(txt,widget,time,change_color,color_origin="pas de changement bordel"):
    stle=("bold","courier","times","italic")
    font_size=(13,14,15,16)
    txt_=""
    for word in txt:
        txt_=txt_+word
        widget.config(text=txt_)
        sleep(time)
        if change_color:
            widget.config(font=(stle[randrange(3)],font_size[randrange(3)]))
    if change_color:
        widget.config(foreground=color_origin,font=font1)



def run_thread(fonction,arguments,name):
    Thread(target=fonction,args=arguments,name=name).start()

#end traitement
#-----------replace--------------


def next_1():
    lab3.place(x=220,y=85)
    but4.place(x=580,y=85)



def clean_next_1():
    lab3.place(x=220,y=1000)
    but4.place(x=580,y=1000)


def reduce(text,custom_len=10):
    if  custom_len<len(text): return text[:custom_len]+"..."
    else: return text

def ext_choice():
    for_text=[("Video Files","*.txt"),("PDF File","*.pdf")]
    for_video=[("mp4 Files","*.mp4"),("...","*.ts"),("..","*.avi")]
    for_image=[("...","*.png"),("..","*.jpeg"),("...","*.jpe"),("..","*.jpg")]
    for_audio=[("Audio files","*.mp3"),("..","*.m4a")]
    if mode[1]=="Texte": 
        ext=for_text
    if mode[1]=="Image":
        ext=for_image
    if mode[1]=="Audio":
        ext=for_audio
    if mode[1]=="Video":
        ext=for_video
    if mode[0]=="un_lock":
        ext=[("all fille","*.*")]
    return ext
def next_2(file="bof....."):
    clean_next_1()
    type_of_file=ext_choice()
    file_path=filedialog.askopenfilename(filetypes=type_of_file)
    if file_path == "":
        alert("Une erreur est survenue lors de l'ouverture du fichier")
    else:
        file_name=file_path.split("/")[-1]
        print(file_name)
        config[0]=file_path
        config[1]=file_name
        lab6.config(text=reduce(file_name))
        screen_child3.place(x=200,y=379)
        run_thread(txt_add,(reduce(file_name,16),lab7,.400,False,),"a")
        run_thread(txt_add,(estim_unit(path.getsize(file_path)),lab8,.700,False,),"b")
        run_thread(txt_add,(mode[1],lab10,.500,False,),"c")
        put.place(x=490,y=140)
        put_entry.place(x=340,y=140)
        but5.place(x=620,y=310)
        lab7.place(x=3,y=3)
        lab8.place(x=200,y=3)
        put.focus()
        lab10.place(x=400,y=3)
        
        lab6.place(x=220,y=85)
        lab7.config(text="")
        lab8.config(text="")
        if mode[0]=="_lock":
            but5.config(image=img_lock,compound="right",text="Protéger",command=next_3)
        if mode[0]=="un_lock":
            but5.config(image=img_unlock,compound="right",text="Ouvrir",command=next_3)




def clean_next_2():
    lab6.place(x=220,y=1000)
    put.place(x=490,y=1000)
    put_entry.place(x=340,y=1100)
    but5.place(x=220,y=1000)
    put.delete(0,ttk.END)
    screen_child3.place(x=1000,y=2)


def que_dalle():
    pass



def next_3():

    # print(config)
    
    
    # print(mode)
    if mode[0]=="_lock":
        if mode[1]=="Texte" or mode[1]=="Video" or mode[1]=="Audio":
            run_thread(lock_vid,(config[0],put.get()),"d")
        if mode[1]=="Image":
            run_thread(lock_vid,(config[0],put.get()),"e")
    if mode[0]=='un_lock':
        if mode[1]=="Texte" or mode[1]=="Video" or mode[1]=="Audio":
            run_thread(unlock_vid,(config[0],put.get()),"f")
        if mode[1]=="Image":

            run_thread(unlock_img,(config[0],put.get()),"pp")



def clen_next_3():
    lab9.place(x=285,y=1000)
    bar["value"]=0
    bar.place(x=240,y=1000)




def clean_all():
    clean_next_1()
    clean_next_2()
    clen_next_3()
    
    # but5.config(text="",command=next_3,state="normal")


def able(widget):
    widget.config(style='Custom.TButton',width=20)



def desable(widget):
    for elt in widget:
        elt.config(width=15,style='TButton',)


def texte():
    mode[1]="Texte"
    mode[2]=texte
    # pre_img=extrat_content("texte.png")
    # creat_file("mdr.png",pre_img,"wb")
    img=resize_img("texte.png",80,100)
    # print(img)
    lab6.config(image=img)
    lab6.image=img
    able(but1)
    desable((but2,but3,but8))
    clean_all()
    lab3.config(text="Selectionner un fichier Texte :")
    next_1()



def image():
    mode[1]="Image"
    mode[2]=image
    # pre_img=extrat_content("image.png")
    # creat_file("mdr.png",pre_img,"wb")
    img=resize_img("image.png",80,100)
    lab6.config(image=img)
    lab6.image=img
    # print(img)
    able(but2)
    desable((but1,but3,but8))
    clean_all()
    # img2=resize_img("image.png",80,100)
    # lab6=ttk.Label(screen,text="filename",image=img2,compound="top",)
    # lab6.place(x=220,y=85)
    lab3.config(text="Selectionner un fichier Image :")
    next_1()

def video():
    mode[1]="Video"
    mode[2]=video
    
    # pre_img=extrat_content("video.png")
    # creat_file("mdr.png",pre_img,"wb")
    img=resize_img("video.png",80,100)
    lab6.config(image=img)
    lab6.image=img
    # print(img)
    
    able(but8)
    desable((but2,but1,but3))
    clean_all()
    #img3=resize_img("video.png",80,100)
    
    #lab6=ttk.Label(screen,text="filename",image=img3,compound="top",)
    lab3.config(text="Selectionner un fichier Video :")
    next_1()

def audio():
    mode[1]="Audio"
    mode[2]=audio
    # pre_img=extrat_content("video.png")
    # creat_file("mdr.png",pre_img,"wb")
    img=resize_img("audio.png",80,100)
    lab6.config(image=img)
    lab6.image=img
    # print(img)
    
    able(but3)
    desable((but2,but1,but8))
    clean_all()
    #img3=resize_img("video.png",80,100)
    
    #lab6=ttk.Label(screen,text="filename",image=img3,compound="top",)
    lab3.config(text="Selectionner un fichier Audio :")
    next_1()


def mode_unlock():
    mode[0]="un_lock"
    but6.config(style="Custom1.TButton")
    but7.config(style="Custom.TButton")
    but6.place(x=10,y=5)
    but7.place(x=380,y=12)
    on((but1,but2,but3,but8))
    but5.config(image=img_unlock,compound="right",text="Ouvrir",command=next_3)
    clean_all()


def mode_lock():
    
    mode[0]="_lock"
    but7.config(style="Custom1.TButton")
    but6.config(style="Custom.TButton")
    but6.place(x=10,y=12)
    but7.place(x=380,y=5)
    on((but1,but2,but3,but8))
    but5.config(image=img_lock,compound="right",text="Protéger",command=next_3)
    clean_all()

def off(wid):
    for widget in wid:
        widget.config(state="disabled")

def on(wid):
    for widget in wid:
        widget.config(state="normal")

def move_x(widget,init_coord,final_coord,blind=True,f_color="danger"):
    
    if blind:widget.config(style="cos1.TFrame")
    while    init_coord[0]< final_coord[0]:
        init_coord[0]+=5
        widget.place(x=init_coord[0],y=init_coord[1])
        sleep(.100)
    if blind:widget.config(style="cos2.TFrame")

def move_y(widget,init_coord,final_coord,blind=True,f_color="danger"):
    if blind:widget.config(style="cos1.TFrame")
    while    init_coord[1]< final_coord[1]:
        init_coord[1]+=5
        widget.place(x=init_coord[0],y=init_coord[1])
        sleep(.100)
    if blind:
        widget.config(style="cos2.TFrame")
        make_me_move(screen_child1,"x",[-220,0],[0,0],)
    


def make_me_move(widget,way,origin,final,blind=True,f_color=""):
    if way=="x":run_thread(move_x,(widget,[origin[0],origin[1]],[final[0],final[1]]),"1")
    if way=="y":run_thread(move_y,(widget,[origin[0],origin[1]],[final[0],final[1]]),"2")

def Go():
    sleep(2)
    lab11.destroy()
    bar.place(x=1000,y=0)
    make_me_move(screen_child2,"y",[200,-20],[200,0])
    run_thread(txt_add,("Secure",lab1,.500,True,"blue"),"3")
    

#________main________
font1=("Bold",15,"italic")
font2=("Bold",10,"Italic")
screen=ttk.Window(title="Secure",themename="vapor",resizable=(False,False),iconphoto="unlock_done_2.png")
screen.geometry("750x420")
style=ttk.Style()
style.configure('Custom.TButton',background="#190831",foreground="#ffbd05",font=("arial",10,"italic"))
style.configure('Custom1.TButton',background="#329402",foreground="#ffbd05",font=("helvitica"))
style.configure("cos1.TFrame",background="#000000")
style.configure("cos2.TFrame",background="#ffbd05")

screen_child1=ttk.Frame(screen,height=398+20,width=200,borderwidth=5,relief="solid",style="warning",padding=2)
screen_child2=ttk.Frame(screen,height=50,width=550,borderwidth=2,relief="solid",style="warning")
lab1=ttk.Label(screen_child2,text="",font=font1,foreground="blue",background="#ffbd05")
lab2=ttk.Label(screen_child1,text="Options:",font=font1,width=20)
but1=ttk.Button(screen_child1,text="Texte",width=15,command=texte)
but2=ttk.Button(screen_child1,text="Image",width=15,command=image)
but3=ttk.Button(screen_child1,text="Audio",width=15,command=audio)
but8=ttk.Button(screen_child1,text="Video",width=15,command=video )


lab3=ttk.Label(screen,text="",font=("bold",12))
but4=ttk.Button(screen,text="Choisir",command=lambda:next_2())
# pre_img=extrat_content("video.png")
# creat_file("mdr.png",pre_img,"wb")


img=resize_img("video.png",80,100)
lock_picture=resize_img("lock.png",30,30)
unlock_picture=resize_img("unlock.png",30,30)
img_unlock=resize_img("unlock_done_2.png",30,30)
img_lock=resize_img("lock_done.png",30,30)


lab6=ttk.Label(screen,text="filename",compound="top",image=img)
screen_child3=ttk.Frame(screen,height=40,borderwidth=5,width=550,relief="solid",style="primary")
lab7=ttk.Label(screen_child3,text="",background="#6e40c0")
lab8=ttk.Label(screen_child3,text="filesize",background="#6e40c0")
put_entry=ttk.Label(screen,text="Mot de passe:",font=("Italic",11))
put=ttk.Entry(screen,)
bar=ttk.Progressbar(length=300,mode="determinate",value=0)
lab9=ttk.Label(text="Analyse..")
but5=ttk.Button(text="Protéger",style="warning",command=next_3)
but6=ttk.Button(screen_child2,text="Verrouiller",style="Custom1.TButton",width=10,command=mode_lock,image=lock_picture,compound="right")
but7=ttk.Button(screen_child2,text="Deverrouiller",style="Custom1.TButton",width=10,command=mode_unlock,image=unlock_picture,compound="right")
lab10=ttk.Label(screen_child3,text="",background="#6e40c0")
off((but1,but2,but3,but8))
menu=ttk.Menu()
menu.add_command(label="A propos",command=about_Fred)
screen.config(menu=menu)
opening_img=resize_img("unlock_done_2.png",600,370)
lab11=ttk.Label(image=opening_img,text="Secure",compound="top",style="warning",font=("Bold",13))
screen.after(1000,lambda:run_thread(Go,(),"openning"))

# bar.place(x=200,y=400)
but6.place(x=10,y=5)
but7.place(x=380,y=5)
# screen_child2.place(x=200,y=0)
# screen_child1.place(x=-220,y=0)
lab1.place(x=220,y=0)
lab2.place(x=0,y=0)
but1.place(x=0,y=80)
but2.place(x=0,y=140)
but8.place(x=0,y=260)
but3.place(x=0,y=200)
lab11.place(x=50,y=0)
screen.mainloop()