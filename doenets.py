import tkinter as tk
import urllib.request
def s():
    print (str(entryIndex.get()))
def getResult(index):
    url = urllib.request.urlopen('https://doenets.lk/result/service/AlResult/'+index)
    content = url.read()
    decContent = content.decode()
    interList = decContent.split(',')
    if(interList[-1].split(':')[1].strip('}').strip('"') != 'Invalid Index Number. Please check your index number and try again.'):
        name = interList[2].split(':')[1].strip('"')
        indexNo = interList[3].split(':')[1].strip('"')
        zScore = interList[8].split(':')[1].strip('"')
        islandRank = interList[5].split(':')[1].strip('"')
        stream = interList[9].split(':')[1].strip('"')
        subjects = [interList[10].split(':')[2].strip('"'), interList[12].split(':')[1].strip('"}'), interList[14].split(':')[1].strip('"}'), interList[16].split(':')[1].strip('"}'), interList[18].split(':')[1].strip('"}')]
        results = [interList[11].split(':')[1].strip('"}'), interList[13].split(':')[1].strip('"}'), interList[15].split(':')[1].strip('"}'), interList[17].split(':')[1].strip('"}'), interList[19].split(':')[1].strip('"}]')]

        entryName.delete(0, 100)
        entryZScore.delete(0, 100)
        entryIslandR.delete(0, 100)
        entryStream.delete(0, 100)
        entryCGM.delete(0, 100)
        entryEM.delete(0, 100)
        entryS1.delete(0, 100)
        entryS2.delete(0, 100)
        entryS3.delete(0, 100)
        entryS1M.delete(0, 100)
        entryS2M.delete(0, 100)
        entryS3M.delete(0, 100)
        
        entryName.insert(1,name)
        entryZScore.insert(1,zScore)
        entryIslandR.insert(1,islandRank)
        entryStream.insert(1,stream)

        entryCGM.insert(1,results[0])
        entryEM.insert(1,results[1])

        entryS1.insert(1,subjects[2])
        entryS1M.insert(1,results[2])

        entryS2.insert(1,subjects[3])
        entryS2M.insert(1,results[3])

        entryS3.insert(1,subjects[4])
        entryS3M.insert(1,results[4])

        
##        entryS3.configure(state="readonly")
        
        print(name)
        print(indexNo)
        print(zScore)
        print(islandRank)
        print(stream)
        print(subjects)
        print(results)
    else:
        entryIndex.delete(0, 10)
        entryName.delete(0, 100)
        entryZScore.delete(0, 100)
        entryIslandR.delete(0, 100)
        entryStream.delete(0, 100)
        entryCGM.delete(0, 100)
        entryEM.delete(0, 100)
        entryS1.delete(0, 100)
        entryS2.delete(0, 100)
        entryS3.delete(0, 100)
        entryS1M.delete(0, 100)
        entryS2M.delete(0, 100)
        entryS3M.delete(0, 100)
        entryIndex.insert(1,'Invalid index number')
    
gui = tk.Tk()
gui.title('GetResults!!')
tk.Label(gui, text='Index Number').grid(row=0) 
entryIndex = tk.Entry(gui,width = 50) 
entryIndex.grid(row=0, column=1) 

button = tk.Button(gui, text='Get Result', width=25, command=lambda: getResult(str(entryIndex.get())))
button.grid(row=2, column=3)

tk.Label(gui, text='Name').grid(row=4)
entryName = tk.Entry(gui,width = 50) 
entryName.grid(row=4, column=1)

tk.Label(gui, text='ZScore').grid(row=6)
entryZScore = tk.Entry(gui,width = 50) 
entryZScore.grid(row=6, column=1)

tk.Label(gui, text='Island Rank').grid(row=7)
entryIslandR = tk.Entry(gui,width = 50) 
entryIslandR.grid(row=7, column=1)

tk.Label(gui, text='Stream').grid(row=8)
entryStream = tk.Entry(gui,width = 50) 
entryStream.grid(row=8, column=1)

tk.Label(gui, text='Common General Test',width = 50).grid(row=10)
entryCGM = tk.Entry(gui,width = 50) 
entryCGM.grid(row=10, column=1)
tk.Label(gui, text='General English',width = 50).grid(row=11)
entryEM = tk.Entry(gui,width = 50) 
entryEM.grid(row=11, column=1)
entryS1 = tk.Entry(gui,width = 50) 
entryS1.grid(row=12, column=0)
entryS1M = tk.Entry(gui,width = 50) 
entryS1M.grid(row=12, column=1)
entryS2 = tk.Entry(gui,width = 50) 
entryS2.grid(row=13, column=0)
entryS2M = tk.Entry(gui,width = 50) 
entryS2M.grid(row=13, column=1)
entryS3 = tk.Entry(gui,width = 50) 
entryS3.grid(row=14, column=0)
entryS3M = tk.Entry(gui,width = 50) 
entryS3M.grid(row=14, column=1)

gui.mainloop()



