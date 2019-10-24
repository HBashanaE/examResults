import tkinter as tk
import urllib.request
import json

def s():
    print(str(entryIndex.get()))

def getResult(index):
    url = urllib.request.urlopen('https://doenets.lk/result/service/AlResult/' + index)
    content = url.read()
    decContent = content.decode()
    decContent = decContent.replace("'", '"')
    decDic = json.loads(decContent)
    print(decDic)
    exam = decDic['examination']
    year = decDic['year']
    name = decDic['name']
    indexNo = decDic['indexNo']
    dRank = decDic['districtRank']
    iRank = decDic['islandRank']
    marks = decDic['marks']
    status = decDic['status']
    zScore = decDic['zScore']
    stream = decDic['stream']
    subRes = decDic['subjectResults']
    print(exam)
    interList = decContent.split(',')
    if (exam != None):
        print(subRes[0])
        cgt = subRes[0]
        ge = subRes[1]
        s1 = subRes[2]
        s2 = subRes[3]
        s3 = subRes[4]

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

        entryName.insert(1, name)
        entryZScore.insert(1, zScore)
        entryIslandR.insert(1, iRank)
        entryStream.insert(1, stream)

        entryCGM.insert(1, cgt['subjectResult'])
        entryEM.insert(1, ge['subjectResult'])

        entryS1.insert(1, s1['subjectName'])
        entryS1M.insert(1, s1['subjectResult'])

        entryS2.insert(1, s2['subjectName'])
        entryS2M.insert(1, s2['subjectResult'])

        entryS3.insert(1, s3['subjectName'])
        entryS3M.insert(1, s3['subjectResult'])

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
        entryIndex.insert(1, 'Invalid index number')


gui = tk.Tk()
gui.title('GetResults!!')
tk.Label(gui, text='Index Number').grid(row=0)
entryIndex = tk.Entry(gui, width=50)
entryIndex.grid(row=0, column=1)

button = tk.Button(gui, text='Get Result', width=25, command=lambda: getResult(str(entryIndex.get())))
button.grid(row=2, column=3)

tk.Label(gui, text='Name').grid(row=4)
entryName = tk.Entry(gui, width=50)
entryName.grid(row=4, column=1)

tk.Label(gui, text='ZScore').grid(row=6)
entryZScore = tk.Entry(gui, width=50)
entryZScore.grid(row=6, column=1)

tk.Label(gui, text='Island Rank').grid(row=7)
entryIslandR = tk.Entry(gui, width=50)
entryIslandR.grid(row=7, column=1)

tk.Label(gui, text='Stream').grid(row=8)
entryStream = tk.Entry(gui, width=50)
entryStream.grid(row=8, column=1)

tk.Label(gui, text='Common General Test', width=50).grid(row=10)
entryCGM = tk.Entry(gui, width=50)
entryCGM.grid(row=10, column=1)
tk.Label(gui, text='General English', width=50).grid(row=11)
entryEM = tk.Entry(gui, width=50)
entryEM.grid(row=11, column=1)
entryS1 = tk.Entry(gui, width=50)
entryS1.grid(row=12, column=0)
entryS1M = tk.Entry(gui, width=50)
entryS1M.grid(row=12, column=1)
entryS2 = tk.Entry(gui, width=50)
entryS2.grid(row=13, column=0)
entryS2M = tk.Entry(gui, width=50)
entryS2M.grid(row=13, column=1)
entryS3 = tk.Entry(gui, width=50)
entryS3.grid(row=14, column=0)
entryS3M = tk.Entry(gui, width=50)
entryS3M.grid(row=14, column=1)

gui.mainloop()
