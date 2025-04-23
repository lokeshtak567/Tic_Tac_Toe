import tkinter as tk
import random
import time
import os
#----------------------------------------------------------------------------------------------------------------#
window=tk.Tk()
window.title("TIC TAC TOE")
window.geometry("250x300")
window.resizable(False,False)

#----------------------------------------------------------------------------------------------------------------#
sl=[None,0,0,0,0,0,0,0,0,0]

def load():
    global ml
    ml=[None,
        [ sl[1],sl[2],sl[3] ],
        [ sl[4],sl[5],sl[6] ],
        [ sl[7],sl[8],sl[9] ],
        [ sl[1],sl[4],sl[7] ],
        [ sl[2],sl[5],sl[8] ],
        [ sl[3],sl[6],sl[9] ],
        [ sl[1],sl[5],sl[9] ],
        [ sl[3],sl[5],sl[7] ] ]


icon1=tk.PhotoImage(master=window,file="images/mmbg.png")
icon2=tk.PhotoImage(master=window,file="images/ai_btn.png")
icon3=tk.PhotoImage(master=window,file="images/mp_btn.png")
icon4=tk.PhotoImage(master=window,file="images/exit_btn.png")
icon5=tk.PhotoImage(master=window,file="images/credits_btn.png")
icon6=tk.PhotoImage(master=window,file="images/mpbg.png")
icon17=tk.PhotoImage(master=window,file="images/aibg.png")
icon7=tk.PhotoImage(master=window,file="images/menu_btn.png")
icon8=tk.PhotoImage(master=window,file="images/rst_btn.png")
icon9=tk.PhotoImage(master=window,file="images/ext2_btn.png")
icon10=tk.PhotoImage(master=window,file="images/board.png")
icon12=tk.PhotoImage(master=window,file="images/playn.png")
icon16=tk.PhotoImage(master=window,file="images/st_btn.png")
def mainmenu():
    try:
        playframe.destroy()
    except Exception as e:
        None
    try:
        credframe.destroy()
    except Exception as e:
        None
    global mmframe,icon1,icon2,icon3,icon4,icon5
    
    mmframe=tk.Frame(window)
    mmframe.pack(fill=tk.BOTH,expand=False)
    
    

    mmbg=tk.Label(mmframe,image=icon1,bg='black').pack(fill=tk.BOTH,expand=True)

    ai=tk.Button(mmframe,image=icon2,bg="black",fg="black",command=AI).place(x=49,y=70)
    mp=tk.Button(mmframe,image=icon3,bg="black",fg="black",command=multiplayer).place(x=49,y=140)
    ext=tk.Button(mmframe,image=icon4,bg="black",fg="black",command=window.destroy).place(x=49,y=215)
    cdt=tk.Button(mmframe,image=icon5,bg="black",fg="black",command=credits).place(x=100,y=285)


pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9=None,None,None,None,None,None,None,None,None

def AIplay():
    global flaga
    flaga=0
    def wb():
        print('wb was called')
        def wb1():
            for k in range(3):
                if ml[i][k]==0:
                    if ((i==1 and k==0) or (i==4 and k==0) or (i==7 and k==0)):
                        bf1()
                        flaga=1
                        return
                        
                    elif ((i==1 and k==1) or (i==5 and k==0)):
                        bf2()
                        flaga=1
                        return
                        
                    elif ((i==1 and k==2) or (i==6 and k==0) or (i==8 and k==0)):
                        bf3()
                        print("button3 was pressed inside wb")
                        flaga=1
                        print("flaga is changed to 1")
                        print(flaga)
                        return
                        
                        
                    elif ((i==2 and k==0) or (i==4 and k==1)):
                        bf4()
                        flaga=1
                        return
                        
                    elif ((i==2 and k==1) or (i==5 and k==1) or (i==7 and k==1) or (i==8 and k==1)):
                        bf5()
                        flaga=1
                        return
                        
                    elif ((i==2 and k==2) or (i==6 and k==1)):
                        bf6()
                        flaga=1
                        return
                        
                    elif ((i==3 and k==0) or (i==4 and k==2) or (i==8 and k==2)):
                        bf7()
                        flaga=1
                        return
                        
                    elif ((i==3 and k==1) or (i==5 and k==2)):
                        bf8()
                        flaga=1
                        return
                        
                    elif ((i==3 and k==2) or (i==6 and k==2) or (i==7 and k==2)):
                        bf9()
                        flaga=1
                        return
                        
                else:
                    continue
            return

        load()
        for i in range(1,9):
            countx,counto,empos=0,0,None
            for j in range(3):
                if ml[i][j]==1:
                    countx+=1
                elif ml[i][j]==2:
                    counto+=1
                else:
                    continue
            if counto==2:
                wb1()
            elif countx==2:
                wb1()
            else:
                continue
        return
        
                
                



    global pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9
    
    if ((count!=10) and (count in cai)):
        print("AI CALLED",count)
        load()
        if cai==[1,3,5,7,9]:
            if count==1:
                R2=random.choice([1,3,7,9])
                if R2==1:
                    pos1=1
                    bf1()
                elif R2==3:
                    pos1=3
                    bf3()
                elif R2==7:
                    pos1=7
                    bf7()
                elif R2==9:
                    pos1=9
                    bf9()
                print('pos1 is',pos1)       
            
            elif count==3:
                print("entered in 3")
                for i in range(1,10):
                    if sl[i]==1:
                        pos2=i
                    else:
                        continue
                print(f"pos1{pos1} pos2{pos2}")
                if pos2 ==5:
                    if pos1==1:
                        R5=random.choice([6,8,9])
                        if R5==6:
                            bf6()
                            return
                        elif R5==8:
                            bf7()
                            return
                        elif R5==9:
                            bf9()
                            return
                    elif pos1==3:
                        R5=random.choice([4,7,8])
                        if R5==4:
                            bf4()
                            return
                        elif R5==7:
                            bf7()
                            return
                        elif R5==8:
                            bf8()
                            return
                    elif pos1==7:
                        R5=random.choice([2,3,6])
                        if R5==2:
                            bf2()
                            return
                        elif R5==3:
                            bf3()
                            return
                        elif R5==6:
                            bf6()
                            return
                    elif pos1==9:
                        R5=random.choice([1,2,4])
                        if R5==1:
                            bf1()
                            return
                        elif R5==2:
                            bf2()
                            return
                        elif R5==4:
                            bf4()
                            return
                    
            elif count==5:
                print("iss ghotale me count=5 involved he")
                wb()
                if flaga==1:
                    return
            elif count==7:
                wb()
                if flaga==1:
                    return
            elif count==9:
                wb()
                if flaga==1:
                    return

        elif cai==[2,4,6,8]:

            
            if count==2:
                for i in range(1,10):
                    if sl[i]==1:
                        pos1=i
                    else:
                        continue
                if (pos1 in [1,3,7,9]):
                    bf5()
                elif (pos1 in [2,4,6,8]):

                    if pos1==2:
                        R3=random.choice([7,9])
                        if R3==7:
                            bf7()
                        elif R3==9:
                            bf9()
                    elif pos1==4:
                        R3=random.choice([3,9])
                        if R3==3:
                            bf3()
                        elif R3==9:
                            bf9()
                    elif pos1==6:
                        R3=random.choice([1,7])
                        if R3==1:
                            bf1()
                        elif R3==7:
                            bf7()
                    elif pos1==8:
                        R3=random.choice([1,3])
                        if R3==1:
                            bf1()
                        elif R3==7:
                            bf7()
                
                elif (pos1==5):
                    R3=random.choice([1,3,7,9])
                    if R3==1:
                        bf1()
                    elif R3==3:
                        bf3()
                    elif R3==7:
                        bf7()
                    elif R3==9:
                        bf9()

            elif count==4:
                wb()
                print("checking if flaga is equal to 1")
                print(flaga)
                if flaga==1:
                    print("yes flaga is equal to 1")
                    print("exiting AIPLAY")
                    return

                print("continuing in c==4 after wb")
                for i in range(1,10):
                    if (i!=pos1) and (sl[i]==1):
                        pos3=i    
                    else:
                        continue 
                if (pos1==1 and pos3==9) or (pos1==9 and pos3==1) or (pos1==3 and pos3==7) or (pos1==7 and pos3==3):
                    R4=random.choice([2,4,6,8])
                    if R4==2:
                        bf2()
                        return
                    elif R4==4:
                        bf4()
                        return
                    elif R4==6:
                        bf6()
                        return
                    elif R4==8:
                        bf8()
                        return

            elif count==6:
                wb()
                if flaga==1:
                    return
            elif count==8:
                wb()
                if flaga==1:
                    return
        else:
            return

    else:
        return





def play():
    global chance,count,bf1,bf2,bf3,bf4,bf5,bf6,bf7,bf8,bf9
    count=1
    def check():
        global iconx,icono,iconn
        load()
        flag=0
        for i in range(1,9):
            countx,counto=0,0
            for j in range(0,3):
                if ml[i][j]==1:
                    countx+=1
                elif ml[i][j]==2:
                    counto+=1
                else:
                    continue
            if countx==3:
                p1.destroy()
                p2.destroy()
                p3.destroy()
                p4.destroy()
                p5.destroy()
                p6.destroy()
                p7.destroy()
                p8.destroy()
                p9.destroy()
                iconx=tk.PhotoImage(master=window,file="images/xwon.png")
                xwon=tk.Label(playframe,image=iconx,bg="black").place(x=80,y=55)
                flag=1
                break

            elif counto==3:
                p1.destroy()
                p2.destroy()
                p3.destroy()
                p4.destroy()
                p5.destroy()
                p6.destroy()
                p7.destroy()
                p8.destroy()
                p9.destroy()
                icono=tk.PhotoImage(master=window,file="images/owon.png")
                owon=tk.Label(playframe,image=icono,bg="black").place(x=80,y=55)
                flag=1
                break
            else:
                if count in cai:
                    print("count here is ",count)
                    AIplay()

        
        if (flag==0 and count==10):
            iconn=tk.PhotoImage(master=window,file="images/nwon.png")
            nwon=tk.Label(playframe,image=iconn,bg="black").place(x=90,y=55)    

    def chance(R):
        global ch,icon11,R1
        R1=R
        ch=0
        if R1==1:
            icon11=tk.PhotoImage(master=window,file="images/showo.png")
            showchance=tk.Label(playframe,image=icon11,bg="black").place(x=115,y=55)
            ch=1
            R1=2
            return ch,R1

        elif R1==2:
            icon11=tk.PhotoImage(master=window,file="images/showx.png")
            showchance=tk.Label(playframe,image=icon11,bg="black").place(x=115,y=55)
            ch=2
            R1=1
            return ch,R1


        
    def bf1():
        global iconp1,R,count
        p1.destroy()
        chance(R)
        R=R1
        if ch==1:
            iconp1=tk.PhotoImage(master=window,file="images/playx.png")
        elif ch==2:
            iconp1=tk.PhotoImage(master=window,file="images/playo.png")
        playc1=tk.Label(playframe,image=iconp1,bg="black").place(x=46,y=90)
        sl[1]=ch
        count+=1
        check()
        
        
            
    def bf2():
        global iconp2,R,count
        p2.destroy()
        chance(R)
        R=R1
        if ch==1:
            iconp2=tk.PhotoImage(master=window,file="images/playx.png")
        elif ch==2:
            iconp2=tk.PhotoImage(master=window,file="images/playo.png")
        playc2=tk.Label(playframe,image=iconp2,bg="black").place(x=104,y=90)
        sl[2]=ch
        count+=1
        check()
        
            
    def bf3():
        global iconp3,R,count
        p3.destroy()
        chance(R)
        R=R1
        if ch==1:
            iconp3=tk.PhotoImage(master=window,file="images/playx.png")
        elif ch==2:
            iconp3=tk.PhotoImage(master=window,file="images/playo.png")
        playc3=tk.Label(playframe,image=iconp3,bg="black").place(x=159,y=90)
        sl[3]=ch
        count+=1
        check()
        
            
    def bf4():
        global iconp4,R,count
        p4.destroy()
        chance(R)
        R=R1
        if ch==1:
            iconp4=tk.PhotoImage(master=window,file="images/playx.png")
        elif ch==2:
            iconp4=tk.PhotoImage(master=window,file="images/playo.png")
        playc4=tk.Label(playframe,image=iconp4,bg="black").place(x=46,y=147)
        sl[4]=ch
        count+=1
        check()
        
           

    def bf5():
        global iconp5,R,count
        p5.destroy()
        chance(R)
        R=R1
        if ch==1:
            iconp5=tk.PhotoImage(master=window,file="images/playx.png")
        elif ch==2:
            iconp5=tk.PhotoImage(master=window,file="images/playo.png")
        playc5=tk.Label(playframe,image=iconp5,bg="black").place(x=104,y=147)
        sl[5]=ch
        count+=1
        check()
        
            

    def bf6():
        global iconp6,R,count
        p6.destroy()
        chance(R)
        R=R1
        if ch==1:
            iconp6=tk.PhotoImage(master=window,file="images/playx.png")
        elif ch==2:
            iconp6=tk.PhotoImage(master=window,file="images/playo.png")
        playc6=tk.Label(playframe,image=iconp6,bg="black").place(x=159,y=147)
        sl[6]=ch
        count+=1
        check()
        
            

    def bf7():
        global iconp7,R,count
        p7.destroy()
        chance(R)
        R=R1
        if ch==1:
            iconp7=tk.PhotoImage(master=window,file="images/playx.png")
        elif ch==2:
            iconp7=tk.PhotoImage(master=window,file="images/playo.png")
        playc7=tk.Label(playframe,image=iconp7,bg="black").place(x=46,y=204)
        sl[7]=ch
        count+=1
        check()
        

    def bf8():
        global iconp8,R,count
        p8.destroy()
        chance(R)
        R=R1
        if ch==1:
            iconp8=tk.PhotoImage(master=window,file="images/playx.png")
        elif ch==2:
            iconp8=tk.PhotoImage(master=window,file="images/playo.png")
        playc8=tk.Label(playframe,image=iconp8,bg="black").place(x=104,y=204)
        sl[8]=ch
        count+=1
        check()
        
            

    def bf9():
        global iconp9,R,count
        p9.destroy()
        chance(R)
        R=R1
        if ch==1:
            iconp9=tk.PhotoImage(master=window,file="images/playx.png")
        elif ch==2:
            iconp9=tk.PhotoImage(master=window,file="images/playo.png")
        playc9=tk.Label(playframe,image=iconp9,bg="black").place(x=159,y=204)
        sl[9]=ch
        count+=1
        check()
        
            

    p1=tk.Button(playframe,image=icon12,bg="black",fg="black",command=bf1)
    p1.place(x=46,y=90)
    p2=tk.Button(playframe,image=icon12,bg="black",fg="black",command=bf2)
    p2.place(x=104,y=90)
    p3=tk.Button(playframe,image=icon12,bg="black",fg="black",command=bf3)
    p3.place(x=159,y=90)
    p4=tk.Button(playframe,image=icon12,bg="black",fg="black",command=bf4)
    p4.place(x=46,y=147)
    p5=tk.Button(playframe,image=icon12,bg="black",fg="black",command=bf5)
    p5.place(x=104,y=147)
    p6=tk.Button(playframe,image=icon12,bg="black",fg="black",command=bf6)
    p6.place(x=159,y=147)
    p7=tk.Button(playframe,image=icon12,bg="black",fg="black",command=bf7)
    p7.place(x=46,y=204)
    p8=tk.Button(playframe,image=icon12,bg="black",fg="black",command=bf8)
    p8.place(x=104,y=204)
    p9=tk.Button(playframe,image=icon12,bg="black",fg="black",command=bf9)
    p9.place(x=159,y=204)

def start1():
    global icon11,R,play,st1,rst1,cai
    play()
    R=random.randint(1,2)
    if R==1:
        icon11=tk.PhotoImage(master=window,file="images/showx.png")
        showchance=tk.Label(playframe,image=icon11,bg="black").place(x=115,y=55)
        cai=[2,4,6,8]
            
    elif R==2:
        icon11=tk.PhotoImage(master=window,file="images/showo.png")
        showchance=tk.Label(playframe,image=icon11,bg="black").place(x=115,y=55)
        cai=[1,3,5,7,9]

    def restart1(): 
         
        playframe.destroy()
        AI()
        global sl
        sl=[None,0,0,0,0,0,0,0,0,0]
    st1=tk.Button(playframe,image=icon16,bg="black",fg="black",command=start1)
    rst1=tk.Button(playframe,image=icon8,bg="black",fg="black",command=restart1)
    st1.destroy()
    rst1.place(x=96,y=275)
    AIplay()
    
def start2():
    global icon11,R,play,st2,rst2
    play()
    R=random.randint(1,2)
        

    if R==1:
        icon11=tk.PhotoImage(master=window,file="images/showx.png")
        showchance=tk.Label(playframe,image=icon11,bg="black").place(x=115,y=55)
            
    elif R==2:
        icon11=tk.PhotoImage(master=window,file="images/showo.png")
        showchance=tk.Label(playframe,image=icon11,bg="black").place(x=115,y=55) 
    def restart2(): 
        
        playframe.destroy()
        multiplayer()
        global sl
        sl=[None,0,0,0,0,0,0,0,0,0]
    st2=tk.Button(playframe,image=icon16,bg="black",fg="black",command=start2)
    rst2=tk.Button(playframe,image=icon8,bg="black",fg="black",command=restart2)
    st2.destroy()
    rst2.place(x=96,y=275)



 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def AI():
    
    try:
        mmframe.destroy()
    except Exception as e:
        None


    global playframe
    playframe=tk.Frame(window,)
    playframe.pack(fill=tk.BOTH,expand=False)
    aibg=tk.Label(playframe,image=icon17,bg="black").pack(fill=tk.BOTH,expand=True)
    board=tk.Label(playframe,image=icon10,bg="black").place(x=38,y=80)
    mm=tk.Button(playframe,image=icon7,bg="black",fg="black",command=mainmenu).place(x=18,y=275)
    st1=tk.Button(playframe,image=icon16,bg="black",fg="black",command=start1)        
    st1.place(x=96,y=275)
    ext=tk.Button(playframe,image=icon9,bg="black",fg="black",command=window.destroy).place(x=170,y=275)
    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def multiplayer():

    try:
        mmframe.destroy()
    except Exception as e:
        None

    global playframe
    playframe=tk.Frame(window,)
    playframe.pack(fill=tk.BOTH,expand=False)
    mpbg=tk.Label(playframe,image=icon6,bg="black").pack(fill=tk.BOTH,expand=True)
    board=tk.Label(playframe,image=icon10,bg="black").place(x=38,y=80)
    mm=tk.Button(playframe,image=icon7,bg="black",fg="black",command=mainmenu).place(x=18,y=275)
    st2=tk.Button(playframe,image=icon16,bg="black",fg="black",command=start2)        
    st2.place(x=96,y=275)
    ext=tk.Button(playframe,image=icon9,bg="black",fg="black",command=window.destroy).place(x=170,y=275)
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def credits():
    global credframe,cred2
    mmframe.destroy()
    credframe=tk.Frame(window,)
    credframe.pack(fill=tk.BOTH,expand=False)
    
    cred1=tk.Label(credframe,image=icon1,bg="black").pack(fill=tk.BOTH,expand=True)
    cred2=tk.PhotoImage(master=window,file="images/credits.png")
    cred3=tk.Label(credframe,image=cred2,bg="black").place(x=38,y=80)
    mm=tk.Button(credframe,image=icon7,bg="black",fg="black",command=mainmenu).place(x=18,y=275)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
mainmenu()
window.mainloop()
