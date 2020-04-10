from tkinter import*
import tkinter.messagebox as msg
from PIL import ImageTk,Image
root=Tk()
def e():
    sumAll=0
    sumAll+=phmVar.get()+phfVar.get()+familyVar.get()+gVar.get()+lVar.get()
    if(phmVar.get()<0 or phfVar.get()<0 or familyVar.get()<0 or gVar.get()<0 or lVar.get()<0):
        msg.showinfo("Input invaild","Negative input")
        root.destroy()
        return
    elif(sumAll>18 or sumAll<0):
        msg.showinfo("Input invaild","More than available seats")
        root.destroy()
        return
    ph={'male':0,'female':0}
    ph['male']=phmVar.get()
    ph['female']=phfVar.get()
    ladies={'single':[0,0,0,0],'group':[0,0,0,0]}
    ladies['single'][2]=lVar.get()
    family={'members':0}
    family['members']=familyVar.get()
    gents={'single':[0,0,0,0],'group':[0,0,0,0]}
    gents['single'][0]=gVar.get()
    seats=18
    van=[[0],[0,0,0,0,0]]
    van[1:1]=[[0,0,0] for x in range(4)]
    if ph['female']!=0:
        for i,x in enumerate(van):
            for j,place in enumerate(x):
                if van[i][j]==0 and ph['female']!=0:
                    van[i][j]='phf'
                    ph['female']-=1
                    seats-=1
    if ph['male']!=0 and seats!=0:
        for i,x in enumerate(van):
            for j,place in enumerate(x):
                if van[i][j]==0 and ph['male']!=0:
                    van[i][j]='phm'
                    ph['male']-=1
                    seats-=1
    k=0
    i=0
    j=0
    while k<4:
        if ladies['group'][k]!=0:
                for i,x in enumerate(van):
                    for j,place in enumerate(x):
                        if van[i][j]==0 and ladies['group'][k]!=0:
                            van[i][j]='Ls'
                            ladies['group'][k]-=1
                            seats-=1
        if ladies['single'][k]!=0:
            if van[0][0]==0 :
                van[i][j]='Ls'
                ladies['single'][k]-=1
                seats-=1
            for i in range(1,5):
                if van[i][2]==0 and ladies['single'][k]!=0:
                    van[i][2]='Ls'
                    ladies['single'][k]-=1
                    seats-=1
            if van[0][0]!=0 and van[1][2]!=0 and van[2][2]!=0 and van[3][2]!=0 and ladies['single'][k]!=0:
                for i,x in enumerate(van):
                    for j,place in enumerate(x):
                        if van[i][j]==0 and ladies['single'][k]!=0 and(j!=2 or i,j==5,2):
                            van[i][j]='Ls'
                            ladies['single'][k]-=1
                            seats-=1
        k+=1
    if family['members']!=0 and seats!=0:
        for i,x in enumerate(van):
            for j,place in enumerate(x):
                if van[i][j]==0 and family['members']!=0:
                    van[i][j]='f'
                    family['members']-=1
                    seats-=1
    k=0
    while k<4:
        if gents['group'][k]!=0:
                for i,x in enumerate(van):
                    for j,place in enumerate(x):
                        if van[i][j]==0 and gents['group'][k]!=0:
                            van[i][j]='Gs'
                            gents['group'][k]-=1
                            seats-=1
        if gents['single'][k]!=0:
            if van[0][0]==0 :
                van[i][j]='Gs'
                gents['single'][k]-=1
                seats-=1
            for i in range(1,5):
                if van[i][2]==0 and gents['single'][k]!=0:
                    van[i][2]='Gs'
                    gents['single'][k]-=1
                    seats-=1
            if van[0][0]!=0 and van[1][2]!=0 and van[2][2]!=0 and van[3][2]!=0 and gents['single'][k]!=0:
                for i,x in enumerate(van):
                    for j,place in enumerate(x):
                        if van[i][j]==0 and gents['single'][k]!=0 and(j!=2 or i,j==5,2):
                            van[i][j]='Gs'
                            gents['single'][k]-=1
                            seats-=1
        k+=1
    li2=[]
    for i in van:
            li2.insert(0,i)
    li3=[x for i in li2 for x in i]
    i=0
    j=0
    k=0
    for i in range(18):
        q=li3[i]
        if(q==0):
            im=img2
        if(q=='Gs'):
            im=g
        if(q=='Ls'):
            im=l
        if(q=='f'):
            im=f
        if(q=='phf'):
            im=phf
        if(q=='phm'):
            im=phm
        if(i<5):
            canvas.create_image(650+42*(i),200,image=im,anchor=NW)
        if(i<17 and i>4):
            if(k%3==0):
                j=j+1
                k=0
            if(k==2):
                canvas.create_image(700+50*(k),200+50*(j),image=im,anchor=NW)
            else:
                canvas.create_image(650+50*(k),200+50*(j),image=im,anchor=NW)
            k=k+1
        if(i<18 and i>16):
            canvas.create_image(650+50*(k),200+50*(j+1),image=im,anchor=NW)
canvas=Canvas(root,width=1680,height=1050,bg="white");
canvas.pack(fill=BOTH,expand=True)
head_label=Label(canvas,text="INTELLIGENT SEAT ALLOCATION SYSTEM",fg="black",font=("Verdana",30),bg="white")
head_label.place(relx=.25,rely=.1)
familyVar=IntVar();
phmVar=IntVar();
phfVar=IntVar();
lVar=IntVar();
gVar=IntVar();
vacent_label=Label(canvas,text="empty:",fg="black",font=("Verdana",20),bg="white")
vacent_label.place(relx=.7,rely=.3)
family_label=Label(canvas,text="family:",fg="black",font=("Verdana",20),bg="white")
family_label.place(relx=.7,rely=.35)
family2_label=Label(canvas,text="family:",fg="black",font=("Verdana",20),bg="white")
family2_label.place(relx=.02,rely=.65)
family_entry=Entry(canvas,textvariable=familyVar,font=("Verdana",20))
family_entry.place(relx=.09,rely=.66,width=100,height=30)
phm_label=Label(canvas,text="Phsically handicapped(M):",fg="black",font=("Verdana",20),bg="white")
phm_label.place(relx=.7,rely=.4)
phm2_label=Label(canvas,text="Phsically handicapped(M):",fg="black",font=("Verdana",20),bg="white")
phm2_label.place(relx=.18,rely=.65)
phm_entry=Entry(canvas,textvariable=phmVar,font=("Verdana",20))
phm_entry.place(relx=.42,rely=.66,width=100,height=30)
phf_label=Label(canvas,text="Phsically handicapped(F):",fg="black",font=("Verdana",20),bg="white")
phf_label.place(relx=.7,rely=.45)
phf2_label=Label(canvas,text="Phsically handicapped(F):",fg="black",font=("Verdana",20),bg="white")
phf2_label.place(relx=.18,rely=.72)
phf_entry=Entry(canvas,textvariable=phfVar,font=("Verdana",20))
phf_entry.place(relx=.42,rely=.73,width=100,height=30)
l_label=Label(canvas,text="Ladies:",fg="black",font=("Verdana",20),bg="white")
l_label.place(relx=.7,rely=.5)
l2_label=Label(canvas,text="Ladies:",fg="black",font=("Verdana",20),bg="white")
l2_label.place(relx=0.02,rely=.72)
l_entry=Entry(canvas,textvariable=lVar,font=("Verdana",20))
l_entry.place(relx=.09,rely=.73,width=100,height=30)
g_label=Label(canvas,text="Gents:",fg="black",font=("Verdana",20),bg="white")
g_label.place(relx=.7,rely=.55)
g_label=Label(canvas,text="Gents:",fg="black",font=("Verdana",20),bg="white")
g_label.place(relx=0.02,rely=.78)
g_entry=Entry(canvas,textvariable=gVar,font=("Verdana",20))
g_entry.place(relx=.09,rely=.79,width=100,height=30)
li=[[0],
 [0, 0, 0],
 [0, 0, 0],
 [0, 0, 0],
 [0, 0, 0],
 [0, 0, 0, 0,0]]
li2=[]
for i in li:
        li2.insert(0,i)
li3=[x for i in li2 for x in i]
generate=Button(canvas,text="Allocate",font=("Verdana",25),fg="#f93f10",bg="Powderblue",command=e)
generate.place(relx=.65,rely=.72,height=50,width=250)
img2=Image.open("em.png")
img2=ImageTk.PhotoImage(img2)
phf=Image.open("phf.png")
phf=ImageTk.PhotoImage(phf)
phm=Image.open("phm.png")
phm=ImageTk.PhotoImage(phm)
f=Image.open("f.png")
f=ImageTk.PhotoImage(f)
l=Image.open("l.png")
l=ImageTk.PhotoImage(l)
g=Image.open("g.png")
g=ImageTk.PhotoImage(g)
details_label=Label(canvas,text="Enter the details",fg="black",font=("Verdana",20),bg="white")
details_label.place(relx=.02,rely=.6)
canvas.create_image(1200,250,image=img2,anchor=NW)
canvas.create_image(1200,295,image=f,anchor=NW)
canvas.create_image(1450,335,image=phm,anchor=NW)
canvas.create_image(1450,378,image=phf,anchor=NW)
canvas.create_image(1200,428,image=l,anchor=NW)
canvas.create_image(1200,470,image=g,anchor=NW)
j=0
k=0
root.mainloop()
