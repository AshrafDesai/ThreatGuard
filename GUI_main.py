from glob import glob
from tkinter import*
import psutil
import pystray
import PIL.Image
from screeninfo import get_monitors


window = Tk()

window.title("BitLink End-Point")
window.geometry("1200x850")
window.minsize("1200","850")
window.maxsize("1200","850")

winFrame = Frame(window,width="1200",height="850",bg="gray17")
winFrame.pack()
winFrame.pack_propagate(0)

title_bar = Frame(window, bg='gray17', relief='raised')
title_bar.pack(expand=1, fill=X)




def CloseWindow(event):
    window.overrideredirect(True)
    window.withdraw()

    def OpenWindow():
        window.deiconify()
        window.overrideredirect(True)
        iconIo.stop()

    ioIconImange = PIL.Image.open("res\\Logo\\logo.png")
    iconIo = pystray.Icon("logo",ioIconImange,menu=pystray.Menu(
        pystray.MenuItem("Open",OpenWindow,default=True)
    ))
    iconIo.run()

def CloseButtonEnter(event):
    close_button.config(image=close_buttonImgHoved)

def CloseButtonLeave(event):
    close_button.config(image=close_buttonImg)


close_buttonImg = PhotoImage(file='res\\Title Bar\\close non-hoved.png').subsample(20,20)
close_buttonImgHoved = PhotoImage(file='res\\Title Bar\\close hoved.png').subsample(20,20)
close_button = Label(title_bar, cursor="hand2",image=close_buttonImg,bg='gray17')
close_button.pack(side=RIGHT)
close_button.bind('<Button-1>',CloseWindow)
close_button.bind('<Enter>',CloseButtonEnter)
close_button.bind('<Leave>',CloseButtonLeave)


def MinimizeWindow(event):
    window.overrideredirect(False)
    window.iconify()

def MinimizeButtonEnter(event):
    minimize_button.config(image=minimize_buttonImgHoved)

def MinimizeButtonLeave(event):
    minimize_button.config(image=minimize_buttonImg)


minimize_buttonImg = PhotoImage(file='res\\Title Bar\\minimize non-hoved.png').subsample(20,20)
minimize_buttonImgHoved = PhotoImage(file='res\\Title Bar\\minimize hoved.png').subsample(20,20)
minimize_button = Label(title_bar, cursor="hand2",image=minimize_buttonImg,bg='gray17')
minimize_button.pack(side=RIGHT)
minimize_button.bind('<Button-1>',MinimizeWindow)
minimize_button.bind('<Enter>',MinimizeButtonEnter)
minimize_button.bind('<Leave>',MinimizeButtonLeave)

def MaximizeScreen(event):
    window.overrideredirect(True)
    window.deiconify()

title_bar.bind('<Map>',MaximizeScreen)




def get_pos(event):
    xwin = window.winfo_x()
    ywin = window.winfo_y()
    startx = event.x_root
    starty = event.y_root

    ywin = ywin - starty
    xwin = xwin - startx


    def move_window(event):
        window.geometry("1200x850" + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))
    startx = event.x_root
    starty = event.y_root


    title_bar.bind('<B1-Motion>', move_window)
title_bar.bind('<Button-1>', get_pos)

window.overrideredirect(True) # turns off title bar, geometry
window.geometry('1200x850+30+30')

#--------------------Tkinter Base Setup End ------------------# 




def HomeFrame():


    #--------------------Global Var --------------------#  
    global winFrame
    

    #--------------------Global Var End -----------------# 

    winFrame.destroy()



    #--------------------Main Frame ---------------------# 

    winFrame = Frame(window,width="1200",height="850",bg="gray17")
    winFrame.pack()
    winFrame.pack_propagate(0)

    #--------------------Main Frame End ------------------# 

    #--------------------Footer Frame --------------------#

    global footerImg
    footerImg = PhotoImage(file='res\\footer.png')

    footerLabel = Label(winFrame,image=footerImg,bg="gray17")
    footerLabel.place(x=310,y=773)

    #--------------------Footer Frame End ----------------#

    #--------------------Logo Frame start --------------#

    global logoLabelImg
    logoLabelImg = PhotoImage(file='res\\Logo\\logo.png')
    logoLabel = Label(winFrame,image=logoLabelImg,bg='gray17')
    logoLabel.place(x=10,y=0)

    global nameLabelImg
    nameLabelImg = PhotoImage(file='res\\Logo\\b logo.png').subsample(2,2)
    nameLabel = Label(winFrame,image=nameLabelImg,bg='gray17')
    nameLabel.place(x=90,y=20)
    #--------------------Logo Frame End ----------------#

    #--------------------Home Button --------------------#
    global homeButtonImg

    homeButtonImg = PhotoImage(file="res\\Home Frame\\Current\\Home.png")


    homeButton = Label(winFrame,image=homeButtonImg,bg="gray17",cursor="hand2")
    homeButton.place(x=155,y=570)


    #--------------------Home Button End------------------#

    #--------------------Scan Button ---------------------#

    scanButtonImg = PhotoImage(file="res\\Scan Frame\\Non-Hoved\\Scan.png")
    hovScanButtonImg = PhotoImage(file="res\\Scan Frame\\Hoved\\Scan.png")
    def ScanButtonEnterFrame(event):
        scanButton.config(image=hovScanButtonImg)

    def ScanButtonLeaveFrame(event):
        scanButton.config(image=scanButtonImg)
    
    def ScanButtonCall(event):
        ScanFrame()


    scanButton = Label(winFrame,image=scanButtonImg,bg="gray17",cursor="hand2")
    scanButton.place(x=335,y=570)

    scanButton.bind('<Enter>',ScanButtonEnterFrame)
    scanButton.bind('<Leave>',ScanButtonLeaveFrame)
    scanButton.bind('<Button-1>',ScanButtonCall)

    # #--------------------Scan Button End------------------#

    # #--------------------System Button -------------------#

    systemButtonImg = PhotoImage(file="res\\System Frame\\Non-Hoved\\System.png")
    hovsystemButtonImg = PhotoImage(file="res\\System Frame\\Hoved\\System.png")

    def SystemButtonEnterFrame(event):
        systemButton.config(image=hovsystemButtonImg)

    def SystemButtonLeaveFrame(event):
        systemButton.config(image=systemButtonImg)

    def SystemButtonCall(event):
        SystemFrame()


    systemButton = Label(winFrame,image=systemButtonImg,bg="gray17",cursor="hand2")
    systemButton.place(x=515,y=570)

    systemButton.bind('<Enter>',SystemButtonEnterFrame)
    systemButton.bind('<Leave>',SystemButtonLeaveFrame)
    systemButton.bind('<Button-1>',SystemButtonCall)

    # #--------------------System Button End ---------------#

    #--------------------Web Button -----------------#

    webButtonImg = PhotoImage(file="res\\Web Frame\\Non-Hoved\\Web.png")
    hovWebButtonImg = PhotoImage(file="res\\Web Frame\\Hoved\\Web.png")

    def WebButtonEnterFrame(event):
        webButton.config(image=hovWebButtonImg)

    def WebButtonLeaveFrame(event):
        webButton.config(image=webButtonImg)

    def WebButtonCall(event):
        WebFrame()


    webButton = Label(winFrame,image=webButtonImg,bg="gray17",cursor="hand2")
    webButton.place(x=695,y=570)

    webButton.bind('<Enter>',WebButtonEnterFrame)
    webButton.bind('<Leave>',WebButtonLeaveFrame)
    webButton.bind('<Button-1>',WebButtonCall)

    #--------------------Web Button End -------------#

    # #--------------------Tools Button -----------------#

    toolsButtonImg = PhotoImage(file="res\\Tools Frame\\Non-Hoved\\Tools.png")
    hovToolsButtonImg = PhotoImage(file="res\\Tools Frame\\Hoved\\Tools.png")

    def ToolsButtonEnterFrame(event):
        toolsButton.config(image=hovToolsButtonImg)

    def ToolsButtonLeaveFrame(event):
        toolsButton.config(image=toolsButtonImg)

    def ToolsButtonCall(event):
        ToolsFrame()


    toolsButton = Label(winFrame,image=toolsButtonImg,bg="gray17",cursor="hand2")
    toolsButton.place(x=875,y=570)

    toolsButton.bind('<Enter>',ToolsButtonEnterFrame)
    toolsButton.bind('<Leave>',ToolsButtonLeaveFrame)
    toolsButton.bind('<Button-1>',ToolsButtonCall)

    # #--------------------Tools Button End -------------#


    # #--------------------Animation --- ----------------#

    global robotImg
    robotImg = PhotoImage(file='res\\Home Frame\\Animation\\robotlink.png')

    robotAnimation = Label(winFrame,image=robotImg,bg="gray17")
    robotAnimation.place(x=405,y=150)

    global ani
    ani = 0
    def RobotAnimation():
        global ani

        if ani == 4:
            robotAnimation.place_configure(y=153)
            ani = 0
        
        elif ani == 2:
            robotAnimation.place_configure(y=150)


        ani += 1

        robotAnimation.after(200,RobotAnimation)

    RobotAnimation()

    # #--------------------Animation End ----------------#

    # #--------------------Sub-Frame --- ----------------#

    # #--------------------Proction-Frame --- ----------------#

    global protectionOn0Img

    protectionOn0Img = PhotoImage(file="res\\Home Frame\\Non-Hoved\\protection on0.png").subsample(2,2)
    protectionOn0ImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\protection on.png").subsample(2,2)

    def ProtectionEnter(event):
        protectionOn0.config(image=protectionOn0ImgHov)
    
    def ProtectionLeave(event):
        protectionOn0.config(image = protectionOn0Img)

    protectionOn0 = Label(winFrame, image=protectionOn0Img, bg="gray17", cursor="hand2")
    protectionOn0.place(x=180,y=160)
    protectionOn0.bind('<Enter>',ProtectionEnter)
    protectionOn0.bind('<Leave>',ProtectionLeave)

    # #--------------------Proction-Frame End ----------------#




    # #--------------------Web-Frame --- ----------------#

    global webShieldImg

    webShieldImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\web sh.png").subsample(2,2)
    webShieldImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\web shield.png").subsample(2,2)

    def WebShieldEnter(event):
        webShield.config(image=webShieldImgHov)
    
    def WebShieldLeave(event):
        webShield.config(image=webShieldImg)

    webShield = Label(winFrame, image=webShieldImg, bg="gray17", cursor="hand2")
    webShield.place(x=810,y=160)
    webShield.bind('<Enter>',WebShieldEnter)
    webShield.bind('<Leave>',WebShieldLeave)


    # #--------------------Web-Frame End ----------------#

    # #--------------------FireWall-Frame --- ----------------#

    global fireWallOnImg

    fireWallOnImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\fire wall on.png").subsample(2,2)
    fireWallOnImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\firewall.png").subsample(2,2)

    def FireWallEnter(event):
        fireWallOn.config(image=fireWallOnImgHov)

    def FireWallLeave(event):
        fireWallOn.config(image=fireWallOnImg)

    fireWallOn = Label(winFrame, image=fireWallOnImg, bg="gray17", cursor="hand2")
    fireWallOn.place(x=160,y=220)

    fireWallOn.bind('<Enter>',FireWallEnter)
    fireWallOn.bind('<Leave>',FireWallLeave)
    

    # #--------------------FireWall-Frame End ----------------#


    # #--------------------FullScan-Frame --- ----------------#

    global fullScanImg

    fullScanImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\full scan.png").subsample(2,2)
    fullScanImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\full scan.png").subsample(2,2)

    def FullScanEnter(e):
        fullScan.config(image=fullScanImgHov)
    
    def FullScanLeave(e):
        fullScan.config(image=fullScanImg)

    fullScan = Label(winFrame, image=fullScanImg, bg="gray17", cursor="hand2")
    fullScan.place(x=830,y=220)
    fullScan.bind('<Enter>',FullScanEnter)
    fullScan.bind('<Leave>',FullScanLeave)

    # #--------------------FullScan-Frame End ----------------#
    

    # #--------------------QuickScan-Frame --- ----------------#

    global quickScanImg

    quickScanImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\quick scan.png").subsample(2,2)
    quickScanImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\Quck Scan.png").subsample(2,2)

    def QuickScanEnter(e):
        quickScan.config(image=quickScanImgHov)

    def QuickScanLeave(e):
        quickScan.config(image=quickScanImg)


    quickScan = Label(winFrame, image=quickScanImg, bg="gray17", cursor="hand2")
    quickScan.place(x=150,y=280)
    quickScan.bind('<Enter>',QuickScanEnter)
    quickScan.bind('<Leave>',QuickScanLeave)

    # #--------------------QuickScan-Frame End ----------------#


    # #--------------------RamBooster-Frame --- ----------------#

    global ramBoosterImg

    ramBoosterImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\ram boost.png").subsample(2,2)
    ramBoosterImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\ram boost.png").subsample(2,2)

    def RamBoosterEnter(e):
        ramBooster.config(image=ramBoosterImgHov)

    def RamBoosterLeave(e):
        ramBooster.config(image=ramBoosterImg)

    ramBooster = Label(winFrame, image=ramBoosterImg, bg="gray17", cursor="hand2")
    ramBooster.place(x=840,y=280)
    ramBooster.bind('<Enter>',RamBoosterEnter)
    ramBooster.bind('<Leave>',RamBoosterLeave)


    # #--------------------RamBooster-Frame End ----------------#


    # #--------------------Smart Scan-Frame --- ----------------#

    global smartScanLblImg

    smartScanLblImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\smart scan.png").subsample(2,2)
    smartScanLblImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\smart scan.png").subsample(2,2)

    def smartScanLblEnter(e):
        smartScanLbl.config(image=smartScanLblImgHov)
    
    def smartScanLblLeave(e):
        smartScanLbl.config(image=smartScanLblImg)

    smartScanLbl = Label(winFrame, image=smartScanLblImg, bg="gray17", cursor="hand2")
    smartScanLbl.place(x=160,y=340)
    smartScanLbl.bind('<Enter>',smartScanLblEnter)
    smartScanLbl.bind('<Leave>',smartScanLblLeave)


    # #--------------------Smart Scan-Frame End ----------------#


    # #--------------------Deep Scan-Frame --- ----------------#

    global deepScanImg

    deepScanImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\deep scan.png").subsample(2,2)
    deepScanImgHov = PhotoImage(file='res\\Home Frame\\Hoved\\deep scan.png').subsample(2,2)

    def DeepScanEnter(e):
        deepScan.config(image=deepScanImgHov)

    def DeepScanLeave(e):
        deepScan.config(image=deepScanImg)

    deepScan = Label(winFrame, image=deepScanImg, bg="gray17", cursor="hand2")
    deepScan.place(x=830,y=340)
    deepScan.bind("<Enter>",DeepScanEnter)
    deepScan.bind("<Leave>",DeepScanLeave)

    # #--------------------Deep Scan-Frame End ----------------#



    # #--------------------Help-Frame --- ----------------#

    global helpNsupportImg

    helpNsupportImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\help & support.png").subsample(2,2)
    helpNsupportImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\help.png").subsample(2,2)

    def HelpEnter(e):
        helpNsupport.config(image=helpNsupportImgHov)
    
    def HelpLeave(e):
        helpNsupport.config(image=helpNsupportImg)

    helpNsupport = Label(winFrame, image=helpNsupportImg, bg="gray17", cursor="hand2")
    helpNsupport.place(x=180,y=400)
    helpNsupport.bind("<Enter>",HelpEnter)
    helpNsupport.bind("<Leave>",HelpLeave)

    # #--------------------Help-Frame End ----------------#


    # #--------------------Driver Update-Frame --- ----------------#

    global driverUpdateImg

    driverUpdateImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\driver update.png").subsample(2,2)
    driverUpdateImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\driver update.png").subsample(2,2)

    def DriverUpdateEnter(e):
        driverUpdate.config(image=driverUpdateImgHov)

    def DriverUpdateLeave(e):
        driverUpdate.config(image=driverUpdateImg)

    driverUpdate = Label(winFrame, image=driverUpdateImg, bg="gray17", cursor="hand2")
    driverUpdate.place(x=810,y=400)
    driverUpdate.bind("<Enter>",DriverUpdateEnter)
    driverUpdate.bind("<Leave>",DriverUpdateLeave)

    # #--------------------Driver Update-Frame End ----------------#

    # #--------------------Sub-Frame End ----------------#


##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################


def ScanFrame():

    #--------------------Global Var --------------------#  
    global winFrame
    

    #--------------------Global Var End -----------------# 

    winFrame.destroy()



    #--------------------Main Frame ---------------------# 

    winFrame = Frame(window,width="1200",height="850",bg="gray17")
    winFrame.pack()
    winFrame.pack_propagate(0)

    #--------------------Main Frame End ------------------# 

    #--------------------Footer Frame --------------------#

    global footerImg
    footerImg = PhotoImage(file='res\\footer.png')

    footerLabel = Label(winFrame,image=footerImg,bg="gray17")
    footerLabel.place(x=310,y=773)

    #--------------------Footer Frame End ----------------#

    #--------------------Logo Frame start --------------#

    global logoLabelImg
    logoLabelImg = PhotoImage(file='res\\Logo\\logo.png')
    logoLabel = Label(winFrame,image=logoLabelImg,bg='gray17')
    logoLabel.place(x=10,y=0)

    global nameLabelImg
    nameLabelImg = PhotoImage(file='res\\Logo\\b logo.png').subsample(2,2)
    nameLabel = Label(winFrame,image=nameLabelImg,bg='gray17')
    nameLabel.place(x=90,y=20)
    #--------------------Logo Frame End ----------------#


    #--------------------Quick_Scan --------------------#

    global quickScanButton_1
    global quickScanButton_1_Hoved

    quickScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Quick Scan.png').subsample(2,2)
    quickScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Quick Scan.png').subsample(2,2)

    def quickScanButton_1_Enter(e):
        quickScanButton_1place.config(image=quickScanButton_1_Hoved)
    
    def quickScanButton_1_Leave(e):
        quickScanButton_1place.config(image=quickScanButton_1)

    quickScanButton_1place = Label(winFrame,image=quickScanButton_1,bg='gray17', cursor="hand2")
    quickScanButton_1place.place(x=530,y=100)

    quickScanButton_1place.bind('<Enter>',quickScanButton_1_Enter)
    quickScanButton_1place.bind('<Leave>',quickScanButton_1_Leave)

    #--------------------Quick_Scan End ----------------#

    #--------------------Smart_Scan --------------------#

    global smartScanButton_1
    global smartScanButton_1_Hoved

    smartScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\smart Scan.png').subsample(2,2)
    smartScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\smart Scan.png').subsample(2,2)

    def smartScanButton_1_Enter(e):
        smartScanButton_1place.config(image=smartScanButton_1_Hoved)
    
    def smartScanButton_1_Leave(e):
        smartScanButton_1place.config(image=smartScanButton_1)

    smartScanButton_1place = Label(winFrame,image=smartScanButton_1,bg='gray17', cursor="hand2")
    smartScanButton_1place.place(x=510,y=170)

    smartScanButton_1place.bind('<Enter>',smartScanButton_1_Enter)
    smartScanButton_1place.bind('<Leave>',smartScanButton_1_Leave)

    #--------------------Smart_Scan End ----------------#

    #--------------------Full_Scan --------------------#

    global fullScanButton_1
    global fullScanButton_1_Hoved

    fullScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Full Scan.png').subsample(2,2)
    fullScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Full Scan.png').subsample(2,2)

    def fullScanButton_1_Enter(e):
        fullScanButton_1place.config(image=fullScanButton_1_Hoved)
    
    def fullScanButton_1_Leave(e):
        fullScanButton_1place.config(image=fullScanButton_1)


    fullScanButton_1place = Label(winFrame,image=fullScanButton_1,bg='gray17', cursor="hand2")
    fullScanButton_1place.place(x=510,y=240)

    fullScanButton_1place.bind('<Enter>',fullScanButton_1_Enter)
    fullScanButton_1place.bind('<Leave>',fullScanButton_1_Leave)

    #--------------------Full_Scan End ----------------#

    #--------------------Deep_Scan --------------------#

    global deepScanButton_1
    global deepScanButton_1_Hoved

    deepScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Deep Scan.png').subsample(2,2)
    deepScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Deep Scan.png').subsample(2,2)

    def deepScanButton_1_Enter(e):
        deepScanButton_1place.config(image=deepScanButton_1_Hoved)
    
    def deepScanButton_1_Leave(e):
        deepScanButton_1place.config(image=deepScanButton_1)

    deepScanButton_1place = Label(winFrame,image=deepScanButton_1,bg='gray17', cursor="hand2")
    deepScanButton_1place.place(x=510,y=310)

    deepScanButton_1place.bind('<Enter>',deepScanButton_1_Enter)
    deepScanButton_1place.bind('<Leave>',deepScanButton_1_Leave)

    #--------------------Deep_Scan End ----------------#

    #--------------------Custom_Scan --------------------#

    global CustomScanButton_1
    global CustomScanButton_1_Hoved

    CustomScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Custom Scan.png').subsample(2,2)
    CustomScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Custom Scan.png').subsample(2,2)

    def CustomScanButton_1_Enter(e):
        CustomScanButton_1place.config(image=CustomScanButton_1_Hoved)
    
    def CustomScanButton_1_Leave(e):
        CustomScanButton_1place.config(image=CustomScanButton_1)

    CustomScanButton_1place = Label(winFrame,image=CustomScanButton_1,bg='gray17', cursor="hand2")
    CustomScanButton_1place.place(x=530,y=380)

    CustomScanButton_1place.bind('<Enter>',CustomScanButton_1_Enter)
    CustomScanButton_1place.bind('<Leave>',CustomScanButton_1_Leave)

    #--------------------Custom_Scan End ----------------#

    #--------------------Main Logo ----------------------#

    global scanFrameMainLogo
    global scanFrameMainLogoHoved
    scanFrameMainLogo = PhotoImage(file='res\\Scan Frame\\main logo.png')
    scanFrameMainLogoHoved = PhotoImage(file='res\\Scan Frame\\main logo hoved.png')

    def scanFrameMainLogoEnter(event):
        scanFrameMainLogoPlace.config(image=scanFrameMainLogoHoved)
    
    def scanFrameMainLogoLeave(event):
        scanFrameMainLogoPlace.config(image=scanFrameMainLogo)

    
    scanFrameMainLogoPlace = Label(winFrame,image=scanFrameMainLogo,bg='gray17', cursor="hand2")
    scanFrameMainLogoPlace.place(x=772,y=100)

    scanFrameMainLogoPlace.bind('<Enter>',scanFrameMainLogoEnter)
    scanFrameMainLogoPlace.bind('<Leave>',scanFrameMainLogoLeave)

    #--------------------Main Logo End-------------------#

    #--------------------Home Button --------------------#

    homeButtonImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\Home.png")
    hovHomeButtonImg = PhotoImage(file="res\\Home Frame\\Hoved\\Home.png")

    def HomeButtonEnterFrame(event):
        homeButton.config(image=hovHomeButtonImg)

    def HomeButtonLeaveFrame(event):
        homeButton.config(image=homeButtonImg)
    
    def HomeButtonCall(event):
        HomeFrame()

    homeButton = Label(winFrame,image=homeButtonImg,bg="gray17",cursor="hand2")
    homeButton.place(x=155,y=570)

    homeButton.bind('<Enter>',HomeButtonEnterFrame)
    homeButton.bind('<Leave>',HomeButtonLeaveFrame)
    homeButton.bind('<Button-1>',HomeButtonCall)


    #--------------------Home Button End------------------#

    #--------------------Scan Button ---------------------#

    global scanButtonImg

    scanButtonImg = PhotoImage(file="res\\Scan Frame\\Current\\Scan.png")


    scanButton = Label(winFrame,image=scanButtonImg,bg="gray17",cursor="hand2")
    scanButton.place(x=335,y=570)

    # #--------------------Scan Button End------------------#

    # #--------------------System Button -------------------#

    systemButtonImg = PhotoImage(file="res\\System Frame\\Non-Hoved\\System.png")
    hovsystemButtonImg = PhotoImage(file="res\\System Frame\\Hoved\\System.png")

    def SystemButtonEnterFrame(event):
        systemButton.config(image=hovsystemButtonImg)

    def SystemButtonLeaveFrame(event):
        systemButton.config(image=systemButtonImg)

    def SystemButtonCall(event):
        SystemFrame()


    systemButton = Label(winFrame,image=systemButtonImg,bg="gray17",cursor="hand2")
    systemButton.place(x=515,y=570)

    systemButton.bind('<Enter>',SystemButtonEnterFrame)
    systemButton.bind('<Leave>',SystemButtonLeaveFrame)
    systemButton.bind('<Button-1>',SystemButtonCall)

    # #--------------------System Button End ---------------#

    #--------------------Web Button -----------------#

    webButtonImg = PhotoImage(file="res\\Web Frame\\Non-Hoved\\Web.png")
    hovWebButtonImg = PhotoImage(file="res\\Web Frame\\Hoved\\Web.png")

    def WebButtonEnterFrame(event):
        webButton.config(image=hovWebButtonImg)

    def WebButtonLeaveFrame(event):
        webButton.config(image=webButtonImg)

    def WebButtonCall(event):
        WebFrame()


    webButton = Label(winFrame,image=webButtonImg,bg="gray17",cursor="hand2")
    webButton.place(x=695,y=570)

    webButton.bind('<Enter>',WebButtonEnterFrame)
    webButton.bind('<Leave>',WebButtonLeaveFrame)
    webButton.bind('<Button-1>',WebButtonCall)

    #--------------------Web Button End -------------#

    # #--------------------Tools Button -----------------#

    toolsButtonImg = PhotoImage(file="res\\Tools Frame\\Non-Hoved\\Tools.png")
    hovToolsButtonImg = PhotoImage(file="res\\Tools Frame\\Hoved\\Tools.png")

    def ToolsButtonEnterFrame(event):
        toolsButton.config(image=hovToolsButtonImg)

    def ToolsButtonLeaveFrame(event):
        toolsButton.config(image=toolsButtonImg)

    def ToolsButtonCall(event):
        ToolsFrame()


    toolsButton = Label(winFrame,image=toolsButtonImg,bg="gray17",cursor="hand2")
    toolsButton.place(x=875,y=570)

    toolsButton.bind('<Enter>',ToolsButtonEnterFrame)
    toolsButton.bind('<Leave>',ToolsButtonLeaveFrame)
    toolsButton.bind('<Button-1>',ToolsButtonCall)

    # #--------------------Tools Button End -------------#



##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################



def SystemFrame():

    #--------------------Global Var --------------------#  
    global winFrame
    

    #--------------------Global Var End -----------------# 

    winFrame.destroy()



    #--------------------Main Frame ---------------------# 

    winFrame = Frame(window,width="1200",height="850",bg="gray17")
    winFrame.pack()
    winFrame.pack_propagate(0)

    #--------------------Main Frame End ------------------# 

    #--------------------Footer Frame --------------------#

    global footerImg
    footerImg = PhotoImage(file='res\\footer.png')

    footerLabel = Label(winFrame,image=footerImg,bg="gray17")
    footerLabel.place(x=310,y=773)

    #--------------------Footer Frame End ----------------#

    #--------------------Logo Frame start --------------#

    global logoLabelImg
    logoLabelImg = PhotoImage(file='res\\Logo\\logo.png')
    logoLabel = Label(winFrame,image=logoLabelImg,bg='gray17')
    logoLabel.place(x=10,y=0)

    global nameLabelImg
    nameLabelImg = PhotoImage(file='res\\Logo\\b logo.png').subsample(2,2)
    nameLabel = Label(winFrame,image=nameLabelImg,bg='gray17')
    nameLabel.place(x=90,y=20)
    #--------------------Logo Frame End ----------------#

    #--------------------Protection --------------------#

    global protectionButton_1
    global protectionButton_1_Hoved

    protectionButton_1 = PhotoImage(file='res\\System Frame\\Non-Hoved\\protection.png').subsample(2,2)
    protectionButton_1_Hoved = PhotoImage(file='res\\System Frame\\Hoved\\protection.png').subsample(2,2)

    def protectionButton_1_Enter(e):
        protectionButton_1place.config(image=protectionButton_1_Hoved)
    
    def protectionButton_1_Leave(e):
        protectionButton_1place.config(image=protectionButton_1)

    protectionButton_1place = Label(winFrame,image=protectionButton_1,bg='gray17', cursor="hand2")
    protectionButton_1place.place(x=530,y=100)

    protectionButton_1place.bind('<Enter>',protectionButton_1_Enter)
    protectionButton_1place.bind('<Leave>',protectionButton_1_Leave)

    #--------------------Protection End ----------------#   

    #--------------------Firewall --------------------#

    global firewallButton_1
    global firewallButton_1_Hoved

    firewallButton_1 = PhotoImage(file='res\\System Frame\\Non-Hoved\\firewall.png').subsample(2,2)
    firewallButton_1_Hoved = PhotoImage(file='res\\System Frame\\Hoved\\firewall.png').subsample(2,2)

    def firewallButton_1_Enter(e):
        firewallButton_1place.config(image=firewallButton_1_Hoved)
    
    def firewallButton_1_Leave(e):
        firewallButton_1place.config(image=firewallButton_1)

    firewallButton_1place = Label(winFrame,image=firewallButton_1,bg='gray17', cursor="hand2")
    firewallButton_1place.place(x=510,y=170)

    firewallButton_1place.bind('<Enter>',firewallButton_1_Enter)
    firewallButton_1place.bind('<Leave>',firewallButton_1_Leave)

    #--------------------Firewall End ----------------#  

    #--------------------System Health --------------------#

    global systemHealthButton_1
    global systemHealthButton_1_Hoved

    systemHealthButton_1 = PhotoImage(file='res\\System Frame\\Non-Hoved\\system health.png').subsample(2,2)
    systemHealthButton_1_Hoved = PhotoImage(file='res\\System Frame\\Hoved\\system health.png').subsample(2,2)

    def systemHealthButton_1_Enter(e):
        systemHealthButton_1place.config(image=systemHealthButton_1_Hoved)
    
    def systemHealthButton_1_Leave(e):
        systemHealthButton_1place.config(image=systemHealthButton_1)

    systemHealthButton_1place = Label(winFrame,image=systemHealthButton_1,bg='gray17', cursor="hand2")
    systemHealthButton_1place.place(x=510,y=240)

    systemHealthButton_1place.bind('<Enter>',systemHealthButton_1_Enter)
    systemHealthButton_1place.bind('<Leave>',systemHealthButton_1_Leave)

    #--------------------System Health End ----------------#  

    #--------------------System Report --------------------#

    global systemReportButton_1
    global systemReportButton_1_Hoved

    systemReportButton_1 = PhotoImage(file='res\\System Frame\\Non-Hoved\\system report.png').subsample(2,2)
    systemReportButton_1_Hoved = PhotoImage(file='res\\System Frame\\Hoved\\system report.png').subsample(2,2)

    def systemReportButton_1_Enter(e):
        systemReportButton_1place.config(image=systemReportButton_1_Hoved)
    
    def systemReportButton_1_Leave(e):
        systemReportButton_1place.config(image=systemReportButton_1)

    systemReportButton_1place = Label(winFrame,image=systemReportButton_1,bg='gray17', cursor="hand2")
    systemReportButton_1place.place(x=530,y=310)

    systemReportButton_1place.bind('<Enter>',systemReportButton_1_Enter)
    systemReportButton_1place.bind('<Leave>',systemReportButton_1_Leave)

    #--------------------System Report End ----------------#  


    #--------------------Main Logo ----------------------#

    global systemFrameMainLogo
    global systemFrameMainLogoHoved
    systemFrameMainLogo = PhotoImage(file='res\\System Frame\\main frame logo.png')
    systemFrameMainLogoHoved = PhotoImage(file='res\\System Frame\\main frame logo hoved.png')

    def systemFrameMainLogoEnter(event):
        systemFrameMainLogoPlace.config(image=systemFrameMainLogoHoved)
    
    def systemFrameMainLogoLeave(event):
        systemFrameMainLogoPlace.config(image=systemFrameMainLogo)

    
    systemFrameMainLogo = PhotoImage(file='res\\System Frame\\main frame logo.png')
    systemFrameMainLogoPlace = Label(winFrame,image=systemFrameMainLogo,bg='gray17')
    systemFrameMainLogoPlace.place(x=772,y=100)

    systemFrameMainLogoPlace.bind('<Enter>',systemFrameMainLogoEnter)
    systemFrameMainLogoPlace.bind('<Leave>',systemFrameMainLogoLeave)


    #--------------------Main Logo End-------------------#

    #--------------------Home Button --------------------#

    homeButtonImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\Home.png")
    hovHomeButtonImg = PhotoImage(file="res\\Home Frame\\Hoved\\Home.png")

    def HomeButtonEnterFrame(event):
        homeButton.config(image=hovHomeButtonImg)

    def HomeButtonLeaveFrame(event):
        homeButton.config(image=homeButtonImg)
    
    def HomeButtonCall(event):
        HomeFrame()

    homeButton = Label(winFrame,image=homeButtonImg,bg="gray17",cursor="hand2")
    homeButton.place(x=155,y=570)

    homeButton.bind('<Enter>',HomeButtonEnterFrame)
    homeButton.bind('<Leave>',HomeButtonLeaveFrame)
    homeButton.bind('<Button-1>',HomeButtonCall)


    #--------------------Home Button End------------------#

    #--------------------Scan Button ---------------------#

    scanButtonImg = PhotoImage(file="res\\Scan Frame\\Non-Hoved\\Scan.png")
    hovScanButtonImg = PhotoImage(file="res\\Scan Frame\\Hoved\\Scan.png")
    def ScanButtonEnterFrame(event):
        scanButton.config(image=hovScanButtonImg)

    def ScanButtonLeaveFrame(event):
        scanButton.config(image=scanButtonImg)
    
    def ScanButtonCall(event):
        ScanFrame()


    scanButton = Label(winFrame,image=scanButtonImg,bg="gray17",cursor="hand2")
    scanButton.place(x=335,y=570)

    scanButton.bind('<Enter>',ScanButtonEnterFrame)
    scanButton.bind('<Leave>',ScanButtonLeaveFrame)
    scanButton.bind('<Button-1>',ScanButtonCall)

    # #--------------------Scan Button End------------------#

    # #--------------------System Button -------------------#

    global systemButtonImg

    systemButtonImg = PhotoImage(file="res\\System Frame\\Current\\System.png")


    systemButton = Label(winFrame,image=systemButtonImg,bg="gray17",cursor="hand2")
    systemButton.place(x=515,y=570)

    # #--------------------System Button End ---------------#

    #--------------------Web Button -----------------#

    webButtonImg = PhotoImage(file="res\\Web Frame\\Non-Hoved\\Web.png")
    hovWebButtonImg = PhotoImage(file="res\\Web Frame\\Hoved\\Web.png")

    def WebButtonEnterFrame(event):
        webButton.config(image=hovWebButtonImg)

    def WebButtonLeaveFrame(event):
        webButton.config(image=webButtonImg)

    def WebButtonCall(event):
        WebFrame()


    webButton = Label(winFrame,image=webButtonImg,bg="gray17",cursor="hand2")
    webButton.place(x=695,y=570)

    webButton.bind('<Enter>',WebButtonEnterFrame)
    webButton.bind('<Leave>',WebButtonLeaveFrame)
    webButton.bind('<Button-1>',WebButtonCall)

    #--------------------Web Button End -------------#

    # #--------------------Tools Button -----------------#

    toolsButtonImg = PhotoImage(file="res\\Tools Frame\\Non-Hoved\\Tools.png")
    hovToolsButtonImg = PhotoImage(file="res\\Tools Frame\\Hoved\\Tools.png")

    def ToolsButtonEnterFrame(event):
        toolsButton.config(image=hovToolsButtonImg)

    def ToolsButtonLeaveFrame(event):
        toolsButton.config(image=toolsButtonImg)

    def ToolsButtonCall(event):
        ToolsFrame()


    toolsButton = Label(winFrame,image=toolsButtonImg,bg="gray17",cursor="hand2")
    toolsButton.place(x=875,y=570)

    toolsButton.bind('<Enter>',ToolsButtonEnterFrame)
    toolsButton.bind('<Leave>',ToolsButtonLeaveFrame)
    toolsButton.bind('<Button-1>',ToolsButtonCall)

    # #--------------------Tools Button End -------------#


##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

def WebFrame():

    #--------------------Global Var --------------------#  
    global winFrame
    

    #--------------------Global Var End -----------------# 

    winFrame.destroy()



    #--------------------Main Frame ---------------------# 

    winFrame = Frame(window,width="1200",height="850",bg="gray17")
    winFrame.pack()
    winFrame.pack_propagate(0)

    #--------------------Main Frame End ------------------# 

    #--------------------Footer Frame --------------------#

    global footerImg
    footerImg = PhotoImage(file='res\\footer.png')

    footerLabel = Label(winFrame,image=footerImg,bg="gray17")
    footerLabel.place(x=310,y=773)

    #--------------------Footer Frame End ----------------#

    #--------------------Logo Frame start --------------#

    global logoLabelImg
    logoLabelImg = PhotoImage(file='res\\Logo\\logo.png')
    logoLabel = Label(winFrame,image=logoLabelImg,bg='gray17')
    logoLabel.place(x=10,y=0)

    global nameLabelImg
    nameLabelImg = PhotoImage(file='res\\Logo\\b logo.png').subsample(2,2)
    nameLabel = Label(winFrame,image=nameLabelImg,bg='gray17')
    nameLabel.place(x=90,y=20)
    #--------------------Logo Frame End ----------------#

    #--------------------web shield --------------------#

    global webShieldButton_1
    global webShieldButton_1_Hoved

    webShieldButton_1 = PhotoImage(file='res\\Web Frame\\Non-Hoved\\web shield.png').subsample(2,2)
    webShieldButton_1_Hoved = PhotoImage(file='res\\Web Frame\\Hoved\\web shield.png').subsample(2,2)

    def webShieldButton_1_Enter(e):
        webShieldButton_1place.config(image=webShieldButton_1_Hoved)
    
    def webShieldButton_1_Leave(e):
        webShieldButton_1place.config(image=webShieldButton_1)

    webShieldButton_1place = Label(winFrame,image=webShieldButton_1,bg='gray17', cursor="hand2")
    webShieldButton_1place.place(x=530,y=100)

    webShieldButton_1place.bind('<Enter>',webShieldButton_1_Enter)
    webShieldButton_1place.bind('<Leave>',webShieldButton_1_Leave)

    #--------------------web shield End ----------------# 

    #--------------------Child Safty --------------------#

    global childSaftyButton_1
    global childSaftyButton_1_Hoved

    childSaftyButton_1 = PhotoImage(file='res\\Web Frame\\Non-Hoved\\chield safty.png').subsample(2,2)
    childSaftyButton_1_Hoved = PhotoImage(file='res\\Web Frame\\Hoved\\child safty.png').subsample(2,2)

    def childSaftyButton_1_Enter(e):
        childSaftyButton_1place.config(image=childSaftyButton_1_Hoved)
    
    def childSaftyButton_1_Leave(e):
        childSaftyButton_1place.config(image=childSaftyButton_1)

    childSaftyButton_1place = Label(winFrame,image=childSaftyButton_1,bg='gray17', cursor="hand2")
    childSaftyButton_1place.place(x=510,y=170)

    childSaftyButton_1place.bind('<Enter>',childSaftyButton_1_Enter)
    childSaftyButton_1place.bind('<Leave>',childSaftyButton_1_Leave)

    #--------------------Child Safty End ----------------#

    #--------------------Content Filter --------------------#

    global contentFilterButton_1
    global contentFilterButton_1_Hoved

    contentFilterButton_1 = PhotoImage(file='res\\Web Frame\\Non-Hoved\\content filter.png').subsample(2,2)
    contentFilterButton_1_Hoved = PhotoImage(file='res\\Web Frame\\Hoved\\content filter.png').subsample(2,2)

    def contentFilterButton_1_Enter(e):
        contentFilterButton_1place.config(image=contentFilterButton_1_Hoved)
    
    def contentFilterButton_1_Leave(e):
        contentFilterButton_1place.config(image=contentFilterButton_1)

    contentFilterButton_1place = Label(winFrame,image=contentFilterButton_1,bg='gray17', cursor="hand2")
    contentFilterButton_1place.place(x=510,y=240)

    contentFilterButton_1place.bind('<Enter>',contentFilterButton_1_Enter)
    contentFilterButton_1place.bind('<Leave>',contentFilterButton_1_Leave)

    #--------------------Content Filter End ----------------#

    #--------------------Web Report --------------------#

    global webReportButton_1
    global webReportButton_1_Hoved

    webReportButton_1 = PhotoImage(file='res\\Web Frame\\Non-Hoved\\web report.png').subsample(2,2)
    webReportButton_1_Hoved = PhotoImage(file='res\\Web Frame\\Hoved\\web report.png').subsample(2,2)

    def webReportButton_1_Enter(e):
        webReportButton_1place.config(image=webReportButton_1_Hoved)
    
    def webReportButton_1_Leave(e):
        webReportButton_1place.config(image=webReportButton_1)

    webReportButton_1place = Label(winFrame,image=webReportButton_1,bg='gray17', cursor="hand2")
    webReportButton_1place.place(x=530,y=310)

    webReportButton_1place.bind('<Enter>',webReportButton_1_Enter)
    webReportButton_1place.bind('<Leave>',webReportButton_1_Leave)

    #--------------------Web Report End ----------------# 

    #--------------------Main Logo ----------------------#

    global webFrameMainLogo
    global webFrameMainLogoHoved
    webFrameMainLogo = PhotoImage(file='res\\Web Frame\\main frame logo.png')
    webFrameMainLogoHoved = PhotoImage(file='res\\Web Frame\\main frame logo hoved.png')

    def webFrameMainLogoEnter(event):
        webFrameMainLogoPlace.config(image=webFrameMainLogoHoved)
    
    def webFrameMainLogoLeave(event):
        webFrameMainLogoPlace.config(image=webFrameMainLogo)

    
    webFrameMainLogo = PhotoImage(file='res\\web Frame\\main frame logo.png')
    webFrameMainLogoPlace = Label(winFrame,image=webFrameMainLogo,bg='gray17')
    webFrameMainLogoPlace.place(x=772,y=100)

    webFrameMainLogoPlace.bind('<Enter>',webFrameMainLogoEnter)
    webFrameMainLogoPlace.bind('<Leave>',webFrameMainLogoLeave)


    #--------------------Main Logo End-------------------#

    #--------------------Home Button --------------------#

    homeButtonImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\Home.png")
    hovHomeButtonImg = PhotoImage(file="res\\Home Frame\\Hoved\\Home.png")

    def HomeButtonEnterFrame(event):
        homeButton.config(image=hovHomeButtonImg)

    def HomeButtonLeaveFrame(event):
        homeButton.config(image=homeButtonImg)
    
    def HomeButtonCall(event):
        HomeFrame()

    homeButton = Label(winFrame,image=homeButtonImg,bg="gray17",cursor="hand2")
    homeButton.place(x=155,y=570)

    homeButton.bind('<Enter>',HomeButtonEnterFrame)
    homeButton.bind('<Leave>',HomeButtonLeaveFrame)
    homeButton.bind('<Button-1>',HomeButtonCall)


    #--------------------Home Button End------------------#

    #--------------------Scan Button ---------------------#

    scanButtonImg = PhotoImage(file="res\\Scan Frame\\Non-Hoved\\Scan.png")
    hovScanButtonImg = PhotoImage(file="res\\Scan Frame\\Hoved\\Scan.png")
    def ScanButtonEnterFrame(event):
        scanButton.config(image=hovScanButtonImg)

    def ScanButtonLeaveFrame(event):
        scanButton.config(image=scanButtonImg)
    
    def ScanButtonCall(event):
        ScanFrame()


    scanButton = Label(winFrame,image=scanButtonImg,bg="gray17",cursor="hand2")
    scanButton.place(x=335,y=570)

    scanButton.bind('<Enter>',ScanButtonEnterFrame)
    scanButton.bind('<Leave>',ScanButtonLeaveFrame)
    scanButton.bind('<Button-1>',ScanButtonCall)

    # #--------------------Scan Button End------------------#

    # #--------------------System Button -------------------#

    systemButtonImg = PhotoImage(file="res\\System Frame\\Non-Hoved\\System.png")
    hovsystemButtonImg = PhotoImage(file="res\\System Frame\\Hoved\\System.png")

    def SystemButtonEnterFrame(event):
        systemButton.config(image=hovsystemButtonImg)

    def SystemButtonLeaveFrame(event):
        systemButton.config(image=systemButtonImg)

    def SystemButtonCall(event):
        SystemFrame()


    systemButton = Label(winFrame,image=systemButtonImg,bg="gray17",cursor="hand2")
    systemButton.place(x=515,y=570)

    systemButton.bind('<Enter>',SystemButtonEnterFrame)
    systemButton.bind('<Leave>',SystemButtonLeaveFrame)
    systemButton.bind('<Button-1>',SystemButtonCall)

    # #--------------------System Button End ---------------#

    #--------------------Web Button -----------------#

    global webButtonImg
    webButtonImg = PhotoImage(file="res\\Web Frame\\Current\\Web.png")

    webButton = Label(winFrame,image=webButtonImg,bg="gray17",cursor="hand2")
    webButton.place(x=695,y=570)

    #--------------------Web Button End -------------#

    # #--------------------Tools Button -----------------#

    toolsButtonImg = PhotoImage(file="res\\Tools Frame\\Non-Hoved\\Tools.png")
    hovToolsButtonImg = PhotoImage(file="res\\Tools Frame\\Hoved\\Tools.png")

    def ToolsButtonEnterFrame(event):
        toolsButton.config(image=hovToolsButtonImg)

    def ToolsButtonLeaveFrame(event):
        toolsButton.config(image=toolsButtonImg)

    def ToolsButtonCall(event):
        ToolsFrame()


    toolsButton = Label(winFrame,image=toolsButtonImg,bg="gray17",cursor="hand2")
    toolsButton.place(x=875,y=570)

    toolsButton.bind('<Enter>',ToolsButtonEnterFrame)
    toolsButton.bind('<Leave>',ToolsButtonLeaveFrame)
    toolsButton.bind('<Button-1>',ToolsButtonCall)

    # #--------------------Tools Button End -------------#


##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################


def ToolsFrame():

    #--------------------Global Var --------------------#  
    global winFrame
    

    #--------------------Global Var End -----------------# 

    winFrame.destroy()



    #--------------------Main Frame ---------------------# 

    winFrame = Frame(window,width="1200",height="850",bg="gray17")
    winFrame.pack()
    winFrame.pack_propagate(0)

    #--------------------Main Frame End ------------------# 

    #--------------------Footer Frame --------------------#

    global footerImg
    footerImg = PhotoImage(file='res\\footer.png')

    footerLabel = Label(winFrame,image=footerImg,bg="gray17")
    footerLabel.place(x=310,y=773)

    #--------------------Footer Frame End ----------------#

    #--------------------Logo Frame start --------------#

    global logoLabelImg
    logoLabelImg = PhotoImage(file='res\\Logo\\logo.png')
    logoLabel = Label(winFrame,image=logoLabelImg,bg='gray17')
    logoLabel.place(x=10,y=0)

    global nameLabelImg
    nameLabelImg = PhotoImage(file='res\\Logo\\b logo.png').subsample(2,2)
    nameLabel = Label(winFrame,image=nameLabelImg,bg='gray17')
    nameLabel.place(x=90,y=20)
    #--------------------Logo Frame End ----------------#

    #--------------------Ram Booster --------------------#

    global ramBoosterButton_1
    global ramBoosterButton_1_Hoved

    ramBoosterButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\ram booster.png').subsample(2,2)
    ramBoosterButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\ram booster.png').subsample(2,2)

    def ramBoosterButton_1_Enter(e):
        ramBoosterButton_1place.config(image=ramBoosterButton_1_Hoved)
    
    def ramBoosterButton_1_Leave(e):
        ramBoosterButton_1place.config(image=ramBoosterButton_1)

    ramBoosterButton_1place = Label(winFrame,image=ramBoosterButton_1,bg='gray17', cursor="hand2")
    ramBoosterButton_1place.place(x=530,y=100)

    ramBoosterButton_1place.bind('<Enter>',ramBoosterButton_1_Enter)
    ramBoosterButton_1place.bind('<Leave>',ramBoosterButton_1_Leave)

    #--------------------Ram Booster End ----------------# 

    #--------------------Driver Update --------------------#

    global driverUpdateButton_1
    global driverUpdateButton_1_Hoved

    driverUpdateButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\driver update.png').subsample(2,2)
    driverUpdateButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\driver update.png').subsample(2,2)

    def driverUpdateButton_1_Enter(e):
        driverUpdateButton_1place.config(image=driverUpdateButton_1_Hoved)
    
    def driverUpdateButton_1_Leave(e):
        driverUpdateButton_1place.config(image=driverUpdateButton_1)

    driverUpdateButton_1place = Label(winFrame,image=driverUpdateButton_1,bg='gray17', cursor="hand2")
    driverUpdateButton_1place.place(x=510,y=160)

    driverUpdateButton_1place.bind('<Enter>',driverUpdateButton_1_Enter)
    driverUpdateButton_1place.bind('<Leave>',driverUpdateButton_1_Leave)

    #--------------------Driver Update End ----------------# 

    #--------------------Proxy --------------------#

    global proxyButton_1
    global proxyButton_1_Hoved

    proxyButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\proxy.png').subsample(2,2)
    proxyButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\proxy.png').subsample(2,2)

    def proxyButton_1_Enter(e):
        proxyButton_1place.config(image=proxyButton_1_Hoved)
    
    def proxyButton_1_Leave(e):
        proxyButton_1place.config(image=proxyButton_1)

    proxyButton_1place = Label(winFrame,image=proxyButton_1,bg='gray17', cursor="hand2")
    proxyButton_1place.place(x=510,y=220)

    proxyButton_1place.bind('<Enter>',proxyButton_1_Enter)
    proxyButton_1place.bind('<Leave>',proxyButton_1_Leave)

    #--------------------Proxy End ----------------#

    #--------------------Cache Cleaner --------------------#

    global cacheCleanerButton_1
    global cacheCleanerButton_1_Hoved

    cacheCleanerButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\cache cleaner.png').subsample(2,2)
    cacheCleanerButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\cache cleaner.png').subsample(2,2)

    def cacheCleanerButton_1_Enter(e):
        cacheCleanerButton_1place.config(image=cacheCleanerButton_1_Hoved)
    
    def cacheCleanerButton_1_Leave(e):
        cacheCleanerButton_1place.config(image=cacheCleanerButton_1)

    cacheCleanerButton_1place = Label(winFrame,image=cacheCleanerButton_1,bg='gray17', cursor="hand2")
    cacheCleanerButton_1place.place(x=510,y=280)

    cacheCleanerButton_1place.bind('<Enter>',cacheCleanerButton_1_Enter)
    cacheCleanerButton_1place.bind('<Leave>',cacheCleanerButton_1_Leave)

    #--------------------Cache Cleaner End ----------------#

    #--------------------Web Blocker --------------------#

    global webBlockerButton_1
    global webBlockerButton_1_Hoved

    webBlockerButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\web blocker.png').subsample(2,2)
    webBlockerButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\web blocker.png').subsample(2,2)

    def webBlockerButton_1_Enter(e):
        webBlockerButton_1place.config(image=webBlockerButton_1_Hoved)
    
    def webBlockerButton_1_Leave(e):
        webBlockerButton_1place.config(image=webBlockerButton_1)

    webBlockerButton_1place = Label(winFrame,image=webBlockerButton_1,bg='gray17', cursor="hand2")
    webBlockerButton_1place.place(x=530,y=340)

    webBlockerButton_1place.bind('<Enter>',webBlockerButton_1_Enter)
    webBlockerButton_1place.bind('<Leave>',webBlockerButton_1_Leave)

    #--------------------Web Blocker End ----------------#

    #--------------------History Clean --------------------#

    global historyCleanButton_1
    global historyCleanButton_1_Hoved

    historyCleanButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\history clean.png').subsample(2,2)
    historyCleanButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\history clean.png').subsample(2,2)

    def historyCleanButton_1_Enter(e):
        historyCleanButton_1place.config(image=historyCleanButton_1_Hoved)
    
    def historyCleanButton_1_Leave(e):
        historyCleanButton_1place.config(image=historyCleanButton_1)

    historyCleanButton_1place = Label(winFrame,image=historyCleanButton_1,bg='gray17', cursor="hand2")
    historyCleanButton_1place.place(x=300,y=100)

    historyCleanButton_1place.bind('<Enter>',historyCleanButton_1_Enter)
    historyCleanButton_1place.bind('<Leave>',historyCleanButton_1_Leave)

    #--------------------History Clean End ----------------#

    #--------------------File Recovery --------------------#

    global fileRecoveryButton_1
    global fileRecoveryButton_1_Hoved

    fileRecoveryButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\file recovery.png').subsample(2,2)
    fileRecoveryButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\file recovery.png').subsample(2,2)

    def fileRecoveryButton_1_Enter(e):
        fileRecoveryButton_1place.config(image=fileRecoveryButton_1_Hoved)
    
    def fileRecoveryButton_1_Leave(e):
        fileRecoveryButton_1place.config(image=fileRecoveryButton_1)

    fileRecoveryButton_1place = Label(winFrame,image=fileRecoveryButton_1,bg='gray17', cursor="hand2")
    fileRecoveryButton_1place.place(x=280,y=160)

    fileRecoveryButton_1place.bind('<Enter>',fileRecoveryButton_1_Enter)
    fileRecoveryButton_1place.bind('<Leave>',fileRecoveryButton_1_Leave)

    #--------------------File Recovery End ----------------#

    #--------------------Web Checker --------------------#

    global webCheckerButton_1
    global webCheckerButton_1_Hoved

    webCheckerButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\web checker.png').subsample(2,2)
    webCheckerButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\web checker.png').subsample(2,2)

    def webCheckerButton_1_Enter(e):
        webCheckerButton_1place.config(image=webCheckerButton_1_Hoved)
    
    def webCheckerButton_1_Leave(e):
        webCheckerButton_1place.config(image=webCheckerButton_1)

    webCheckerButton_1place = Label(winFrame,image=webCheckerButton_1,bg='gray17', cursor="hand2")
    webCheckerButton_1place.place(x=280,y=220)

    webCheckerButton_1place.bind('<Enter>',webCheckerButton_1_Enter)
    webCheckerButton_1place.bind('<Leave>',webCheckerButton_1_Leave)

    #--------------------Web Checker End ----------------#

    #--------------------Help --------------------#

    global helpButton_1
    global helpButton_1_Hoved

    helpButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\help.png').subsample(2,2)
    helpButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\help.png').subsample(2,2)

    def helpButton_1_Enter(e):
        helpButton_1place.config(image=helpButton_1_Hoved)
    
    def helpButton_1_Leave(e):
        helpButton_1place.config(image=helpButton_1)

    helpButton_1place = Label(winFrame,image=helpButton_1,bg='gray17', cursor="hand2")
    helpButton_1place.place(x=280,y=280)

    helpButton_1place.bind('<Enter>',helpButton_1_Enter)
    helpButton_1place.bind('<Leave>',helpButton_1_Leave)

    #--------------------Help End ----------------#

    #--------------------About --------------------#

    global aboutButton_1
    global aboutButton_1_Hoved

    aboutButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\about.png').subsample(2,2)
    aboutButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\about.png').subsample(2,2)

    def aboutButton_1_Enter(e):
        aboutButton_1place.config(image=aboutButton_1_Hoved)
    
    def aboutButton_1_Leave(e):
        aboutButton_1place.config(image=aboutButton_1)

    aboutButton_1place = Label(winFrame,image=aboutButton_1,bg='gray17', cursor="hand2")
    aboutButton_1place.place(x=300,y=340)

    aboutButton_1place.bind('<Enter>',aboutButton_1_Enter)
    aboutButton_1place.bind('<Leave>',aboutButton_1_Leave)

    #--------------------About End ----------------#

    #--------------------File Vault --------------------#

    global fileVaultButton_1
    global fileVaultButton_1_Hoved

    fileVaultButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\file vault.png').subsample(2,2)
    fileVaultButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\file vault.png').subsample(2,2)

    def fileVaultButton_1_Enter(e):
        fileVaultButton_1place.config(image=fileVaultButton_1_Hoved)
    
    def fileVaultButton_1_Leave(e):
        fileVaultButton_1place.config(image=fileVaultButton_1)

    fileVaultButton_1place = Label(winFrame,image=fileVaultButton_1,bg='gray17', cursor="hand2")
    fileVaultButton_1place.place(x=80,y=100)

    fileVaultButton_1place.bind('<Enter>',fileVaultButton_1_Enter)
    fileVaultButton_1place.bind('<Leave>',fileVaultButton_1_Leave)

    #--------------------File Vault End ----------------# 

    #--------------------Auto Silent --------------------#

    global autoSilentButton_1
    global autoSilentButton_1_Hoved

    autoSilentButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\auto silent.png').subsample(2,2)
    autoSilentButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\auto silent.png').subsample(2,2)

    def autoSilentButton_1_Enter(e):
        autoSilentButton_1place.config(image=autoSilentButton_1_Hoved)
    
    def autoSilentButton_1_Leave(e):
        autoSilentButton_1place.config(image=autoSilentButton_1)

    autoSilentButton_1place = Label(winFrame,image=autoSilentButton_1,bg='gray17', cursor="hand2")
    autoSilentButton_1place.place(x=60,y=160)

    autoSilentButton_1place.bind('<Enter>',autoSilentButton_1_Enter)
    autoSilentButton_1place.bind('<Leave>',autoSilentButton_1_Leave)

    #--------------------Auto Silent End ----------------#

    #--------------------Game Booster --------------------#

    global gameBoosterButton_1
    global gameBoosterButton_1_Hoved

    gameBoosterButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\game booster.png').subsample(2,2)
    gameBoosterButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\game booster.png').subsample(2,2)

    def gameBoosterButton_1_Enter(e):
        gameBoosterButton_1place.config(image=gameBoosterButton_1_Hoved)
    
    def gameBoosterButton_1_Leave(e):
        gameBoosterButton_1place.config(image=gameBoosterButton_1)

    gameBoosterButton_1place = Label(winFrame,image=gameBoosterButton_1,bg='gray17', cursor="hand2")
    gameBoosterButton_1place.place(x=60,y=220)

    gameBoosterButton_1place.bind('<Enter>',gameBoosterButton_1_Enter)
    gameBoosterButton_1place.bind('<Leave>',gameBoosterButton_1_Leave)

    #--------------------Game Booster End ----------------#

    #--------------------PC Tuner --------------------#

    global PC_TunnerButton_1
    global PC_TunnerButton_1_Hoved

    PC_TunnerButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\pc tuner.png').subsample(2,2)
    PC_TunnerButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\pc tuner.png').subsample(2,2)

    def PC_TunnerButton_1_Enter(e):
        PC_TunnerButton_1place.config(image=PC_TunnerButton_1_Hoved)
    
    def PC_TunnerButton_1_Leave(e):
        PC_TunnerButton_1place.config(image=PC_TunnerButton_1)

    PC_TunnerButton_1place = Label(winFrame,image=PC_TunnerButton_1,bg='gray17', cursor="hand2")
    PC_TunnerButton_1place.place(x=60,y=280)

    PC_TunnerButton_1place.bind('<Enter>',PC_TunnerButton_1_Enter)
    PC_TunnerButton_1place.bind('<Leave>',PC_TunnerButton_1_Leave)

    #--------------------PC Tuner End ----------------#

    #--------------------Parental Mode --------------------#

    global parentalModeButton_1
    global parentalModeButton_1_Hoved

    parentalModeButton_1 = PhotoImage(file='res\\Tools Frame\\Non-Hoved\\parental mode.png').subsample(2,2)
    parentalModeButton_1_Hoved = PhotoImage(file='res\\Tools Frame\\Hoved\\parental mode.png').subsample(2,2)

    def parentalModeButton_1_Enter(e):
        parentalModeButton_1place.config(image=parentalModeButton_1_Hoved)
    
    def parentalModeButton_1_Leave(e):
        parentalModeButton_1place.config(image=parentalModeButton_1)

    parentalModeButton_1place = Label(winFrame,image=parentalModeButton_1,bg='gray17', cursor="hand2")
    parentalModeButton_1place.place(x=80,y=340)

    parentalModeButton_1place.bind('<Enter>',parentalModeButton_1_Enter)
    parentalModeButton_1place.bind('<Leave>',parentalModeButton_1_Leave)

    #--------------------Parental Mode End ----------------#

    #--------------------Main Logo ----------------------#

    global toolsFrameMainLogo
    global toolsFrameMainLogoHoved
    toolsFrameMainLogo = PhotoImage(file='res\\Tools Frame\\main frame logo.png')
    toolsFrameMainLogoHoved = PhotoImage(file='res\\Tools Frame\\main frame logo hoved.png')

    def toolsFrameMainLogoEnter(event):
        toolsFrameMainLogoPlace.config(image=toolsFrameMainLogoHoved)
    
    def toolsFrameMainLogoLeave(event):
        toolsFrameMainLogoPlace.config(image=toolsFrameMainLogo)

    
    toolsFrameMainLogo = PhotoImage(file='res\\Tools Frame\\main frame logo.png')
    toolsFrameMainLogoPlace = Label(winFrame,image=toolsFrameMainLogo,bg='gray17')
    toolsFrameMainLogoPlace.place(x=772,y=100)

    toolsFrameMainLogoPlace.bind('<Enter>',toolsFrameMainLogoEnter)
    toolsFrameMainLogoPlace.bind('<Leave>',toolsFrameMainLogoLeave)


    #--------------------Main Logo End---------------------#

    #--------------------Home Button --------------------#
    
    homeButtonImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\Home.png")
    hovHomeButtonImg = PhotoImage(file="res\\Home Frame\\Hoved\\Home.png")

    def HomeButtonEnterFrame(event):
        homeButton.config(image=hovHomeButtonImg)

    def HomeButtonLeaveFrame(event):
        homeButton.config(image=homeButtonImg)
    
    def HomeButtonCall(event):
        HomeFrame()

    homeButton = Label(winFrame,image=homeButtonImg,bg="gray17",cursor="hand2")
    homeButton.place(x=155,y=570)

    homeButton.bind('<Enter>',HomeButtonEnterFrame)
    homeButton.bind('<Leave>',HomeButtonLeaveFrame)
    homeButton.bind('<Button-1>',HomeButtonCall)

    #--------------------Home Button End------------------#

    #--------------------Scan Button ---------------------#

    scanButtonImg = PhotoImage(file="res\\Scan Frame\\Non-Hoved\\Scan.png")
    hovScanButtonImg = PhotoImage(file="res\\Scan Frame\\Hoved\\Scan.png")
    def ScanButtonEnterFrame(event):
        scanButton.config(image=hovScanButtonImg)

    def ScanButtonLeaveFrame(event):
        scanButton.config(image=scanButtonImg)
    
    def ScanButtonCall(event):
        ScanFrame()


    scanButton = Label(winFrame,image=scanButtonImg,bg="gray17",cursor="hand2")
    scanButton.place(x=335,y=570)

    scanButton.bind('<Enter>',ScanButtonEnterFrame)
    scanButton.bind('<Leave>',ScanButtonLeaveFrame)
    scanButton.bind('<Button-1>',ScanButtonCall)

    # #--------------------Scan Button End------------------#

    # #--------------------System Button -------------------#

    systemButtonImg = PhotoImage(file="res\\System Frame\\Non-Hoved\\System.png")
    hovsystemButtonImg = PhotoImage(file="res\\System Frame\\Hoved\\System.png")

    def SystemButtonEnterFrame(event):
        systemButton.config(image=hovsystemButtonImg)

    def SystemButtonLeaveFrame(event):
        systemButton.config(image=systemButtonImg)

    def SystemButtonCall(event):
        SystemFrame()


    systemButton = Label(winFrame,image=systemButtonImg,bg="gray17",cursor="hand2")
    systemButton.place(x=515,y=570)

    systemButton.bind('<Enter>',SystemButtonEnterFrame)
    systemButton.bind('<Leave>',SystemButtonLeaveFrame)
    systemButton.bind('<Button-1>',SystemButtonCall)

    # #--------------------System Button End ---------------#

    #--------------------Web Button -----------------#

    webButtonImg = PhotoImage(file="res\\Web Frame\\Non-Hoved\\Web.png")
    hovWebButtonImg = PhotoImage(file="res\\Web Frame\\Hoved\\Web.png")

    def WebButtonEnterFrame(event):
        webButton.config(image=hovWebButtonImg)

    def WebButtonLeaveFrame(event):
        webButton.config(image=webButtonImg)

    def WebButtonCall(event):
        WebFrame()


    webButton = Label(winFrame,image=webButtonImg,bg="gray17",cursor="hand2")
    webButton.place(x=695,y=570)

    webButton.bind('<Enter>',WebButtonEnterFrame)
    webButton.bind('<Leave>',WebButtonLeaveFrame)
    webButton.bind('<Button-1>',WebButtonCall)

    #--------------------Web Button End -------------#

    # #--------------------Tools Button -----------------#

    global toolsButtonImg
    toolsButtonImg = PhotoImage(file="res\\Tools Frame\\Current\\Tools.png")


    toolsButton = Label(winFrame,image=toolsButtonImg,bg="gray17",cursor="hand2")
    toolsButton.place(x=875,y=570)

    # #--------------------Tools Button End -------------#

def ProxyFrame():
        #--------------------Global Var --------------------#  
    global winFrame
    

    #--------------------Global Var End -----------------# 

    winFrame.destroy()



    #--------------------Main Frame ---------------------# 

    winFrame = Frame(window,width="1200",height="850",bg="gray17")
    winFrame.pack()
    winFrame.pack_propagate(0)

    #--------------------Main Frame End ------------------# 

    #--------------------Footer Frame --------------------#

    global footerImg
    footerImg = PhotoImage(file='res\\footer.png')

    footerLabel = Label(winFrame,image=footerImg,bg="gray17")
    footerLabel.place(x=310,y=773)

    #--------------------Footer Frame End ----------------#

    #--------------------Logo Frame start --------------#

    global logoLabelImg
    logoLabelImg = PhotoImage(file='res\\Logo\\logo.png')
    logoLabel = Label(winFrame,image=logoLabelImg,bg='gray17')
    logoLabel.place(x=10,y=0)

    global nameLabelImg
    nameLabelImg = PhotoImage(file='res\\Logo\\b logo.png').subsample(2,2)
    nameLabel = Label(winFrame,image=nameLabelImg,bg='gray17')
    nameLabel.place(x=90,y=20)
    #--------------------Logo Frame End ----------------#

    #--------------------Back Logo --------------#

    global backbtnlogo
    global backbtnlogoHov

    backbtnlogo = PhotoImage(file='res\\Common Element\\Non-Hoved\\back btn.png').subsample(6,6)
    backbtnlogoLabel = Label(winFrame,image=backbtnlogo,bg='gray17',cursor="hand2")
    backbtnlogoLabel.place(x=90,y=120)

    #--------------------Back Logo End --------------#


HomeFrame()
  



window.mainloop()