from tkinter import Tk, ttk, mainloop,Frame
import requests
from bs4 import BeautifulSoup
def merge(list1, list2): 
      
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return merged_list 
url = "https://www.nationmaster.com/country-info/stats/People/Child-labor/Children-ages-5--14/Percentage"

status = requests.get(url)
content = status.content
soup = BeautifulSoup(content, 'html.parser')
numData= soup.find_all('td', {"class":"amount"})
nameData = soup.find_all('span', {"class":"full"})
countryName = []
for country in nameData:
    countryName.append(country.text)
percentage=[]
for data in numData:
    percentage.append(data.attrs['data-raw'])
dataTuple = merge(countryName, percentage)

window = Tk()
window.title("Percentage of children in Child Labor")
treeFrame = Frame(window)
treeview=ttk.Treeview(treeFrame, columns="percentageChildren")
treeview.heading("percentageChildren", text="Percent(%)")
treeFrame.pack()
treeview.pack(padx=20,pady=10)
treeScroll = ttk.Scrollbar(treeFrame, orient="vertical", command=treeview.yview)
treeScroll.place(x=423, height=240)
treeview.configure(yscrollcommand=treeScroll.set)
for item in dataTuple:
    treeview.insert("", 1, values=item[1], text=item[0])
window.mainloop()