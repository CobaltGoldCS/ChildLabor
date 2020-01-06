from tkinter import Tk, ttk, mainloop,Frame, Wm, PhotoImage, Button, StringVar, Label, messagebox, Canvas,OptionMenu
import requests
from bs4 import BeautifulSoup
from platform import system

def merge(list1, list2, list3): 
        """Merges 3 lists (used for the datatuple)"""
    merged_list = [(list1[i], list2[i], list3[i]) for i in range(0, len(list1))] 
    return merged_list

class app:
    def __init__(self):
        # Gets the web content
        url = "https://www.nationmaster.com/country-info/stats/People/Child-labor/Children-ages-5--14/Percentage"
        status = requests.get(url)
        content = status.content
        soup = BeautifulSoup(content, 'html.parser')
        numData= soup.find_all('td', {"class":"amount"})
        nameData = soup.find_all('span', {"class":"full"})
        self.countryName = []
        for country in nameData:
            self.countryName.append(country.text)
        percentage=[]
        self.severity=[]
        # Sets severity level by using the percentage
        for data in numData:
            percentage.append(data.attrs['data-raw'])
            if float(data.attrs['data-raw']) >= 47.0:
                severityValue = 1
            elif float(data.attrs['data-raw']) >= 35.0:
                severityValue = 2
            elif float(data.attrs['data-raw']) >= 25.0:
                severityValue = 3
            elif float(data.attrs['data-raw']) >= 10.0:
                severityValue =4
            else:
                severityValue =5
            self.severity.append(severityValue)
        # Creates tuple that contains the treeview data
        self.dataTuple = merge(self.countryName, percentage, self.severity)
        # List for all of the severity levels used in the dropdown menu
        self.allsev = [1,2,3,4,5]

                
    def onClick(self, event):
        # When an item in the treeview is clicked
        item = self.treeview.selection()
        for i in item:
            self.title = self.treeview.item(i, "values")[0]
            self.percent = self.treeview.item(i, "values")[1]
            messagebox.showinfo("Data", self.percent+"% of children in "+self.title+" "+"\n are workers in child labor.")

    def onSelected(self, selected):
        # When an item in the dropdown menu is selected
        if selected == "Severity Level":
            self.reset()
        else:
            self.treeview.delete(*self.treeview.get_children())
            for item in self.dataTuple:
                if item[2] == selected:
                    self.treeview.insert("", 0, values=(item[0], item[1]), tags=item[2])

    def reset(self):
        # Resets the the selected items to normal
        self.treeview.delete(*self.treeview.get_children())
        for item in self.dataTuple:
            self.treeview.insert("", 0, values=(item[0], item[1]), tags=item[2])

    def mainApp(self):
        self.root.destroy()
        window = Tk()
        window.title("Percentage of children in Child Labor (5-14) by country")
        window.tk.call('wm','iconphoto', window._w, PhotoImage(file='cl.gif'))
        if system() == 'darwin':
            window.iconphoto(True, "cl.gif")
            window.iconbitmap("cl.icns")
        # Dropdown Menu
        top = Canvas(window, height = 25, width = 370, bg= 'white')
        top.pack()
        self.selected = StringVar(window)
        self.allsev.insert(0, "Severity Level")
        caller = self.onSelected
        select = OptionMenu(top, self.selected, *self.allsev, command = self.onSelected)
        self.selected.set(self.allsev[0])
        select.grid(sticky = 'w')
        # Treeview /data container
        treeFrame = Frame(window)
        self.treeview=ttk.Treeview(treeFrame, columns=("country", "percentageChildren"), show='headings')
        self.treeview.heading("country", text="Country")
        self.treeview.column("country", minwidth=0, width=300)
        self.treeview.heading("percentageChildren", text="Percent(%)")
        self.treeview.column("percentageChildren", minwidth = 0, width = 70)
        treeFrame.pack()
        self.treeview.pack(padx=20,pady=10)
        #ScrollBar
        treeScroll = ttk.Scrollbar(window, orient="vertical", command=self.treeview.yview)
        treeScroll.place(x=400, height=245)
        self.treeview.configure(yscrollcommand=treeScroll.set)
        for item in self.dataTuple:
            self.treeview.insert("", 0, values=(item[0], item[1]), tags=item[2])
        # Tags for the background
        self.treeview.tag_configure('1', background='#FF6666')
        self.treeview.tag_configure('2', background='#FF9A55')
        self.treeview.tag_configure('3', background='#FFFF22')
        self.treeview.tag_configure('4', background='#66FF66')
        self.treeview.tag_configure('5', background='#6688FF')
        self.treeview.bind("<Double-1>", self.onClick)
        window.mainloop()
    def welcomeApp(self):
        self.root = Tk()
        self.root.title("Welcome to my project")
        welcomeFrame = Frame(self.root)
        welcomeLabel= Label(welcomeFrame, text="This is a project made to bring attention to the alarming rate of child Labor in some countries")
        welcomeFrame.pack()
        welcomeLabel.grid()
        welcomeButton = Button(welcomeFrame, text="Start", command=self.mainApp)
        welcomeButton.grid(row=2, column=1)
        welcomeImg = PhotoImage( file= ("welcomeImage.gif"))
        imgLabel = Label(welcomeFrame, image= welcomeImg)
        imgLabel.grid(row=1)
        self.root.mainloop()
if __name__ == "__main__":
    app = app()
    app.welcomeApp()
