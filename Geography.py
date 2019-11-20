from tkinter import Tk, ttk, mainloop,Frame, Wm, PhotoImage
import requests
from bs4 import BeautifulSoup
from platform import system
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

window = Tk()
window.title("Percentage of children in Child Labor (5-14) by country")
window.tk.call('wm','iconphoto', window._w, PhotoImage(file='cl.gif'))
if system() == 'darwin':
    window.iconphoto(True, "cl.gif")
    window.iconbitmap("cl.icns")
treeFrame = Frame(window)
treeview=ttk.Treeview(treeFrame, columns=("country", "percentageChildren"), show='headings')
treeview.heading("country", text="Country")
treeview.heading("percentageChildren", text="Percent(%)")
treeFrame.pack()
treeview.pack(padx=20,pady=10)
treeScroll = ttk.Scrollbar(treeFrame, orient="vertical", command=treeview.yview)
treeScroll.place(x=423, height=240)
treeview.configure(yscrollcommand=treeScroll.set)
for item in dataTuple:
    treeview.insert("", 0, values=(item[0], item[1]), tags=item[2])
# Tags for the background
treeview.tag_configure('1', background='#FF6666')
treeview.tag_configure('2', background='#FF9A55')
treeview.tag_configure('3', background='#FFFF22')
treeview.tag_configure('4', background='#66FF66')
treeview.tag_configure('5', background='#6688FF')
window.mainloop()
