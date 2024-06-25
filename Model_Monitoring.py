
# <h1>Model Monitoring Application</h1>
# <hr>
# <p><strong>Author: Tyrese Morris</strong></p>
# <p><strong>Date: 6/24</strong></p>
# <p><strong>Version: 1.0</strong></p>
# <hr> 

# # Import the needed packages for the plot and the GUI
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
import gzip
import os
from tkinter import StringVar, filedialog
import tkinter as tk
from tkinter import ttk
import sys

# =============================================================================================================================================
# Create Window and set Font for GUI
LARGE_FONT= ("Calbri", 12)
root = tk.Tk()
root.withdraw() #use to hide tkinter window
File_in_uz2 = currdir = os.getcwd()

# Functions for buttons in the GUI

def search_for_file2 ():
    '''
    This function opens a file explorer window which enables the use to choode the files for the live Mechanical monitoring
    '''
    currdir = os.getcwd()
    File_name = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select Mechanical Monitoring text file')
    return File_name

def Compress(File_in,File_out): #1/3 the size 
    '''
    This Function saves the txt by compressing it as a .gz file which is read for veiwing old saved graphs
    '''
    inf = open(File_in, "rb")
    outf = gzip.open(File_out, "wb")
    outf.write(inf.read())
    outf.close()
    inf.close()
    os.remove(File_in)
    inf = open(File_in,"w")
    inf.close()
    
def decompress(File_in,File_out):
    '''
    This function is unused in this version but was for decompressing before reading file
    '''
    inf=gzip.open(File_in,'rb')
    outf = open(File_out, "rb")
    outf.write(inf.read())
    outf.close()
    inf.close()
 
def File_Locations():
    '''
    This function declares the file names for the saved files and the selected live monitoring files as well as 
    sets the file directory name so that the model being modeled is displayed
    '''
    # global File_in_uz1
    global File_in_uz2
    # global File_in1
    global File_in2
    global dir
    # File_in_uz1 = search_for_file1()
    File_in_uz2 =search_for_file2()
    # File_in1 = 'Modelmonitoring.txt.gz'
    dir = os.path.dirname(File_in_uz2)
    File_in2 = dir + '/MechMonitoring.txt.gz'
File_Locations()
# =============================================================================================================================================
# This section builed the graphs for both the live monitoring and the saved data 
f = Figure(figsize=(5,5),dpi=100,layout='constrained')
ax2 = f.add_subplot(3,1,1)
ax3 = f.add_subplot(3,1,2)
ax4 = f.add_subplot(3,1,3)
'''
ax1 #Zone Count  
ax2 #Mech ratio
ax3 #Creep time total
ax4 #Creep timestep
'''
def animate2(i):
    pulldata2 = open(File_in_uz2,'r').read()
    dataArray2 = pulldata2.split('\n')
    

    xvar2=[] # Cycle Number
    yvar2=[] # unbal_max
    yvar3=[] # Creep timestep
    yvar4=[] # Mechanical Ratio
    yvar5=[] # Creep Time Total

    for eachline2 in dataArray2:
        if len(eachline2)>1:
            Cycle,unbal_max,creep_timestep,Mech_ratio,creep_timetotal = eachline2.split(',')
            xvar2.append(float(Cycle))
            yvar2.append(float(unbal_max))
            yvar3.append(float(creep_timestep))
            yvar4.append(float(Mech_ratio))
            yvar5.append(float(creep_timetotal))

    ax2.clear()
    ax3.clear()
    ax4.clear()

    ax2.plot(xvar2,yvar2)
    ax2.set(title='Model Mechanical Monitoring')
    ax2.set_xlabel('Cycle #') 
    ax2.set_ylabel('Unbalced-Maximum')
    ax3.plot(yvar5,yvar3)
    ax3.set_ylabel('Creep Timestep')
    ax3.set_xlabel('Creep Total Time')
    ax3.set_yscale('log')
    ax4.plot(xvar2,yvar4)
    ax4.set_ylabel('Mechanical ratio')
    ax4.set_yscale('log')
    ax4.set_xlabel('Cycle #') 
       

f2 = Figure(figsize=(5,5),dpi=100,layout='constrained')
ax22 = f2.add_subplot(3,1,1)
ax23 = f2.add_subplot(3,1,2)
ax24 = f2.add_subplot(3,1,3)
def animate22(i):
    if os.path.isfile(File_in2) == True:
    
        pulldata2 = gzip.open(File_in2,'rt').read()
        dataArray2 = pulldata2.split('\n')
    
        xvar2=[] # Cycle Number
        yvar2=[] # unbal_max
        yvar3=[] # Creep timestep
        yvar4=[] # Mechanical Ratio
        yvar5=[] # creep total time    
        for eachline2 in dataArray2:
            if len(eachline2)>1:
                Cycle,unbal_max,creep_timestep,Mech_ratio,creep_timetotal = eachline2.split(',')
                xvar2.append(float(Cycle))
                yvar2.append(float(unbal_max))
                yvar3.append(float(creep_timestep))
                yvar4.append(float(Mech_ratio))
                yvar5.append(float(creep_timetotal))
    
        ax22.clear()
        ax23.clear()
        ax24.clear()
    
        ax22.plot(xvar2,yvar2)
        ax22.set(title='Model Mechanical Monitoring')
        ax22.set_ylabel('Unbalced-Maximum')
        ax22.set_xlabel('Cycle #')
        ax23.plot(yvar5,yvar3)
        ax23.set_ylabel('Creep Timestep')
        ax23.set_xlabel('Creep Total Time')
        ax23.set_yscale('log')
        ax23.set_xscale('log')
        ax24.plot(xvar2,yvar4)
        ax24.set_ylabel('Mechanical ratio')
        ax24.set_yscale('log')
        ax24.set_xlabel('Cycle #')
    else: 
        0  
#=============================================================================================================================================

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        
        tk.Tk.wm_title(self, "Model Monitoring GUI")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Home Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        label2 = tk.Label(self,text="File Directory: {}".format(dir))
        label2.pack(pady=10,padx=10)

        button = ttk.Button(self, text="About ME",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="View Saved Graphs",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Live Monitoring page",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()
    
        # button4 = ttk.Button(self,text="Browse for data",command=lambda: )
        # button4.pack()

        button5 = ttk.Button(self,text="Save Mechanical live data",command=lambda: Compress(File_in_uz2,File_in2))
        button5.pack()
        

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='''This is an application hat can be used to minor a model that is cycling without logging into a remote machine.''', font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="View Saved Graphs",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Saved Graph", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="About me",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        canvas = FigureCanvasTkAgg(f2, self)
        canvas.draw()
        
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Live Model Monitoring", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
       

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
# =============================================================================================================================================

app = SeaofBTCapp()
ani = animation.FuncAnimation(f,animate2,interval=500,cache_frame_data=False)
ani2 = animation.FuncAnimation(f2,animate22,interval=4500,cache_frame_data=False)
app.mainloop()
sys.exit()




