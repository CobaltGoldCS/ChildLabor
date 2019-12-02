from tkinter import Tk, ttk, mainloop,Frame, Wm, PhotoImage, Button, Label, messagebox
import requests
from bs4 import BeautifulSoup
from platform import system
from pathlib import Path
def merge(list1, list2, list3): 
      
    merged_list = [(list1[i], list2[i], list3[i]) for i in range(0, len(list1))] 
    return merged_list 
url = "https://www.nationmaster.com/country-info/stats/People/Child-labor/Children-ages-5--14/Percentage"

status = requests.get(url)
content = status.content
soup = BeautifulSoup(content, 'html.parser')
numData= soup.find_all('td', {"class":"amount"})
nameData = soup.find_all('span', {"class":"full"})
flagData = soup.find_all('i', {"class": "flag"})
countryName = []
for country in nameData:
    countryName.append(country.text)
percentage=[]
severity=[]
for data in numData:
    percentage.append(data.attrs['data-raw'])
    if float(data.attrs['data-raw']) >= 50.0:
        severityValue = 1
    elif float(data.attrs['data-raw']) >= 40.0:
        severityValue = 2
    elif float(data.attrs['data-raw']) >= 25.0:
        severityValue = 3
    elif float(data.attrs['data-raw']) >= 10.0:
        severityValue =4
    else:
        severityValue =5
    severity.append(severityValue)
dataTuple = merge(countryName, percentage, severity)



class app:
    def __init__(self):
        url = "https://www.nationmaster.com/country-info/stats/People/Child-labor/Children-ages-5--14/Percentage"

        status = requests.get(url)
        content = status.content
        soup = BeautifulSoup(content, 'html.parser')
        numData= soup.find_all('td', {"class":"amount"})
        nameData = soup.find_all('span', {"class":"full"})
        flagData = soup.find_all('i', {"class": "flag"})
        countryName = []
        for country in nameData:
            countryName.append(country.text)
        percentage=[]
        severity=[]
        for data in numData:
            percentage.append(data.attrs['data-raw'])
            if float(data.attrs['data-raw']) >= 50.0:
                severityValue = 1
            elif float(data.attrs['data-raw']) >= 40.0:
                severityValue = 2
            elif float(data.attrs['data-raw']) >= 25.0:
                severityValue = 3
            elif float(data.attrs['data-raw']) >= 10.0:
                severityValue =4
            else:
                severityValue =5
            severity.append(severityValue)
        self.dataTuple = merge(countryName, percentage, severity)
    def onClick(self, event):
        item = self.treeview.selection()
        for i in item:
            self.title = self.treeview.item(i, "values")[0]
            self.percent = self.treeview.item(i, "values")[1]
            messagebox.showinfo("Data", self.percent+"% of children in "+self.title+"\n are workers in child labor.")
            
    def mainApp(self):
        self.root.destroy()
        window = Tk()
        window.title("Percentage of children in Child Labor (5-14) by country")
        window.tk.call('wm','iconphoto', window._w, PhotoImage(file='cl.gif'))
        if system() == 'darwin':
            window.iconphoto(True, "cl.gif")
            window.iconbitmap("cl.icns")
        treeFrame = Frame(window)
        self.treeview=ttk.Treeview(treeFrame, columns=("country", "percentageChildren"), show='headings')
        self.treeview.heading("country", text="Country")
        self.treeview.heading("percentageChildren", text="Percent(%)")
        treeFrame.pack()
        self.treeview.pack(padx=20,pady=10)
        treeScroll = ttk.Scrollbar(treeFrame, orient="vertical", command=self.treeview.yview)
        treeScroll.place(x=430, height=220)
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
        welcomeImg = PhotoImage( file= ( "welcomeImage.gif"))
        imgLabel = Label(welcomeFrame, image= welcomeImg)
        imgLabel.grid(row=1)
        self.root.mainloop()
if __name__ == "__main__":
    app = app()
    app.welcomeApp()
