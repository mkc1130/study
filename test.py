from tkinter import *
 
from tkinter import filedialog

from tkinter import scrolledtext

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import matplotlib as mat

import os

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
pd.set_option('mode.chained_assignment',  None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

 
class tkGUi :
 
 
    def __init__(self):
        
        self.root = Tk()

        self.root.title("Data Import")
        
        menubar = Menu(self.root)
        self.root.geometry('1000x500')
        
        self.text = scrolledtext.ScrolledText(self.root, width=1000, height=500)
        
        self.text.pack()
        
        filemenu = Menu(menubar, tearoff=0)
        
        menubar.add_cascade(label="File", menu=filemenu)
        
        filemenu.add_command(label="New", command=self.domenu)
        
        filemenu.add_command(label="Open", command=self.Load)
        
        filemenu.add_command(label="Sort", command=self.Sort)
        
        filemenu.add_command(label="Save", command=self.Save)
        
        filemenu.add_command(label="Save as...", command=self.Save)
        
        filemenu.add_command(label="Graph PM2.5", command=self.Graph_PM2)
        
        filemenu.add_command(label="Graph PM10", command=self.Graph_PM10)
        
        filemenu.add_separator()
        
        filemenu.add_command(label="Exit", command=self.root.quit)
        
        editmenu = Menu(menubar, tearoff=0)
        
        menubar.add_cascade(label="Edit", menu=editmenu)
        
        editmenu.add_command(label="Copy", command=self.domenu)
        
        editmenu.add_command(label="Paste", command=self.domenu)
        
        editmenu.add_separator()
        
        editmenu.add_command(label="Delete", command=self.domenu)
        
        helpmenu = Menu(menubar, tearoff=0)
        
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        helpmenu.add_command(label="About...", command=self.domenu)
 
        self.root.config(menu=menubar)
        
        self.root.mainloop()
 
 
    def Load(self):
        global filename
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("text files", "*.txt"),
                                              ("all files", "*.*")))
        
        print(filename)
        
        #global df3
        #df3 = pd.read_csv(filename, header=None, names=['date','temperature','humidity','pm2.5','dis_pm2.5','pm10','dis_pm10','purifi_amount','purifi_tree','is_working','is_warter_short'])

        #for i in range(0, 44637) :
        #    temp = str(df3['date'][i][1:17])
        #    df3['date'][i] = temp
        
        #df3.reset_index(drop=True)
        #self.text.delete('1.0', END)
        
        #self.text.insert(END, df3)
        data=open(filename,'rt',encoding="utf-8")
        
        
        self.text.delete('1.0', END)
        
        self.text.insert(END,data.read())
        self.text.configure(state='disabled')
        
    def Sort(self):
        
        global filename
        global df3
        df3 = pd.read_csv(filename, header=None, names=['date','temperature','humidity','pm2.5','dis_pm2.5','pm10','dis_pm10','purifi_amount','purifi_tree','is_working','is_warter_short'])

        for i in range(0, 44637) :
            temp = str(df3['date'][i][1:17])
            df3['date'][i] = temp
        #작업하기 위한 복사본 생성
        
        df4 = df3

        #밀린 값 수정 후 정렬

        temp4 = True
        temp3 = []
        global temp1
        global temp2
        for i in range(0,44635) :
            if df4['date'][i][14:16] == '00' : temp1 = 0
            else : temp1 = int(df4['date'][i][14:16])
            if df4['date'][i+1][14:16] == '00' : temp2 = 60
            else : temp2 = int(df4['date'][i+1][14:16])
            if temp1+1 != temp2 :
                if int(df4['date'][i][14:16])+1 == 60 : temp1 = '00'
                elif int(df4['date'][i][14:16]) == 0 or (int(df4['date'][i][14:16]) == 1) or (int(df4['date'][i][14:16]) == 2) or (int(df4['date'][i][14:16]) == 3) or (int(df4['date'][i][14:16]) == 4) or (int(df4['date'][i][14:16]) == 5) or (int(df4['date'][i][14:16]) == 6) or (int(df4['date'][i][14:16]) == 7) or (int(df4['date'][i][14:16]) == 8) : temp1 = '0'+str(int(df4['date'][i][14:16])+1)
                else : temp1 = str(int(df4['date'][i][14:16])+1)
        
        
        
                if df4['date'][i+2][14:16] == df4['date'][i+3][14:16] :
                    df4['date'][i+3] = df4['date'][i][0:14]+temp1
                    df4.sort_values(by=['date'], inplace=True, ascending=True)     

                elif df4['date'][i+1][14:16] == df4['date'][i+2][14:16] :
                    df4['date'][i+2] = df4['date'][i][0:14]+temp1
                    df4.sort_values(by=['date'], inplace=True, ascending=True)     

                elif df4['date'][i][14:16] == df4['date'][i+1][14:16] :
                    df4['date'][i+1] = df4['date'][i][0:14]+temp1
                    df4.sort_values(by=['date'], inplace=True, ascending=True)     
            
                elif df4['date'][i-1][14:16] == df4['date'][i][14:16] :
                    df4['date'][i] = df4['date'][i][0:14]+temp1
                    df4.sort_values(by=['date'], inplace=True, ascending=True)     
        
                else : continue
                



        #원본데이터에 날짜부분만 삽입

        for i in range(0, len(df3)) :
            temp = df4['date'][i]
            df3['date'][i] = temp
    
        #빈 값 채우기

        for i in range(0,len(df3)) :
            if df3['date'][i][14:16] == '00' : temp1 = 0
            else : temp1 = int(df3['date'][i][14:16])
            if df3['date'][i+1][14:16] == '00' : temp2 = 60
            else : temp2 = int(df3['date'][i+1][14:16])
            if temp1+1 != temp2 :
                if int(df3['date'][i][14:16])+1 == 60 : temp1 = '00'
                elif int(df3['date'][i][14:16]) == 0 or (int(df3['date'][i][14:16]) == 1) or (int(df3['date'][i][14:16]) == 2) or (int(df3['date'][i][14:16]) == 3) or (int(df3['date'][i][14:16]) == 4) or (int(df3['date'][i][14:16]) == 5) or (int(df3['date'][i][14:16]) == 6) or (int(df3['date'][i][14:16]) == 7) or (int(df3['date'][i][14:16]) == 8) : temp1 = '0'+str(int(df3['date'][i][14:16])+1)
                else : temp1 = str(int(df3['date'][i][14:16])+1)
                temperature = np.around(df3['temperature'][i-1:i+1].mean(),2)
                humidity = np.around(df3['humidity'][i-1:i+1].mean(),2)
                pm2 = np.around(df3['pm2.5'][i-1:i+1].mean(),2)
                dis_pm2 = np.around(df3['dis_pm2.5'][i-1:i+1].mean(),2)
                pm10 = np.around(df3['pm10'][i-1:i+1].mean(),2)
                dis_pm10 = np.around(df3['dis_pm10'][i-1:i+1].mean(),2)
                date = df3['date'][i][0:14]+temp1   
                df3.loc[len(df3)] = [date,temperature, humidity, pm2, dis_pm2, pm10, dis_pm10, 202125, 49, 0 , 1]
                df3.tail()
                df3.sort_values(by=['date'], inplace=True, ascending=True)     

        

        df4.sort_values(by=['date'], inplace=True, ascending=True)

        #중복된 값 제거
        df3 = df3.drop_duplicates(['date'])
        
        temp = []
        for i in range(0, len(df3)) :
            temp.append(i)
        df3.index=temp
        
        new = Toplevel()
        new.title("Sorted Data")
        text = scrolledtext.ScrolledText(new, width=600, height=500)
        text.pack()
        
        text.delete('1.0', END)
        
        text.insert(END, df3[['date', 'pm2.5', 'dis_pm2.5', 'pm10', 'dis_pm10', 'is_working']])
        text.configure(state='disabled')
        
 
        
 
    def Save(self):
        filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                              filetypes=(("text files", "*.txt"),
                                              ("all files", "*.*")))
        
        print(filename)

    def Graph_PM2(self):
        
        path_dir = os.path.dirname(os.path.realpath(__file__))
        global df3
        list = []
        temp = df3.date[0][0:10]
        list.append(temp)
        for i in range(1,len(df3)) :
            if i % 1440 == 0 : list.append(df3['date'][i][0:10])
            else : continue

        list1 = []
        list1.append(0)
        for i in range(1,len(df3)) :
            if i % 1440 == 0 : list1.append(i)
            else : continue
        
        dis_pm2 = []
        for i in range(0,len(df3)) :
            if  df3['pm2.5'][i] == df3['dis_pm2.5'][i] : dis_pm2.append(0)
            else : dis_pm2.append(df3['dis_pm2.5'][i])

        pm2 = pd.to_numeric(df3['pm2.5'])
        dis_pm2 = pd.to_numeric(dis_pm2)

        mat.rcParams['font.family'] = 'AppleMyungjo'
        month = str(df3['date'][0][5:7])
        day_minus = 0
        if str(df3['date'][len(df3)-1][8:10]) == '31' :
            day_minus = 0
        elif str(df3['date'][len(df3)-1][8:10]) == '30' :
            day_minus = 1
        elif str(df3['date'][len(df3)-1][8:10]) == '29' :
            day_minus = 2
        else :
            day_minus = 3
        mat.rcParams['font.family'] = 'AppleMyungjo'
        # 1~7
        plt.figure(figsize=(18, 8))
        plt.title(month + '월 1주차', fontsize=20)
        plt.plot(df3['date'][0:10080], pm2[0:10080] , label = '초미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df3['date'][0:10080], dis_pm2[0:10080],  label = '정화된 초미세먼지', color = 'b', linewidth=0.5)
        plt.legend(loc=(0.85, 0.9), fontsize=12)

        plt.ylabel('㎍/㎥', fontsize=14)
        plt.ylim(0.0, 150.0)

        plt.xticks(list1[0:7],list[0:7])
        plt.axhline(y=35, color='r', linewidth=1)
        plt.text(10665, 35, '초미세먼지 나쁨 기준', fontsize = 12, color ='maroon')

        plt.grid()
        plt.savefig(path_dir+'/pm2/pm_2.5 1st.png', dpi=60)
        plt.close()

        # 8~14
        plt.figure(figsize=(18, 8))
        plt.title(month + '월 2주차', fontsize=20)
        plt.plot(df3['date'][10080:20160], pm2[10080:20160] , label = '초미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df3['date'][10080:20160], dis_pm2[10080:20160], label = '정화된 초미세먼지', color = 'b', linewidth=0.5)
        plt.legend(loc=(0.85, 0.9), fontsize=12)

        plt.ylabel('㎍/㎥', fontsize=14)
        plt.ylim(0.0, 150.0)

        plt.xticks(list1[0:7],list[7:14])
        plt.axhline(y=35, color='r', linewidth=1)
        plt.text(10665, 35, '초미세먼지 나쁨 기준', fontsize = 12, color ='maroon')

        plt.grid()
        plt.savefig(path_dir+'/pm2/pm_2.5 2nd.png', dpi=60)
        plt.close()

        # 15~21
        plt.figure(figsize=(18, 8))
        plt.title(month + '월 3주차', fontsize=20)
        plt.plot(df3['date'][20160:30240], pm2[20160:30240] , label = '초미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df3['date'][20160:30240], dis_pm2[20160:30240],  label = '정화된 초미세먼지', color = 'b', linewidth=0.5)
        plt.legend(loc=(0.85, 0.9), fontsize=12)

        plt.ylabel('㎍/㎥', fontsize=14)
        plt.ylim(0.0, 150.0)

        plt.xticks(list1[0:7],list[14:21])
        plt.axhline(y=35, color='r', linewidth=1)
        plt.text(10665, 35, '초미세먼지 나쁨 기준', fontsize = 12, color ='maroon')

        plt.grid()
        plt.savefig(path_dir+'/pm2/pm_2.5 3rd.png', dpi=60)
        plt.close()
        

        # 22~31
        plt.figure(figsize=(18, 8))
        plt.title(month + '월 4주차', fontsize=20)
        plt.plot(df3['date'][30240:len(df3)], pm2[30240:len(df3)] , label = '초미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df3['date'][30240:len(df3)], dis_pm2[30240:len(df3)],  label = '정화된 초미세먼지', color = 'b', linewidth=0.5)
        plt.legend(loc=(0.85, 0.9), fontsize=12)

        plt.ylabel('㎍/㎥', fontsize=14)
        plt.ylim(0.0, 150.0)

        plt.xticks(list1[0:10-day_minus],list[21:len(list)])
        plt.axhline(y=35, color='r', linewidth=1)
        plt.text(15275, 35, '초미세먼지 나쁨 기준', fontsize = 12, color ='maroon')

        plt.grid()
        plt.savefig(path_dir+'/pm2/pm_2.5 4th.png', dpi=60)
        plt.close()

        file_list = os.listdir(path_dir+'/pm2')
        real_file_list = [x for x in file_list if(x.endswith(".PNG") or (x.endswith(".png")==True))]
        real_file_list.sort(key=lambda x: x[7:8])
        print(real_file_list)
        root=Toplevel()
        root.title("Graph PM2.5")
        root.geometry("1080x720")
        root.resizable(0,0)
        global xn
        xn = 0
        image=PhotoImage(file=os.path.realpath(path_dir+'/pm2/' + real_file_list[xn]))
        xn = -1
        def showimg_next():
            global xn
            global image
            xn += 1
            if(xn >= len(real_file_list)-1):
                xn = len(real_file_list)-1
            image=PhotoImage(file=os.path.realpath(path_dir+'/pm2/' + real_file_list[xn]))
            label_2 = Label(root, image=image)
            label_2.place(x=0,y=150)
        
        def showimg_previous():
            global xn
            global image
            xn -= 1
            if(xn <= 0):
                xn=0
            image=PhotoImage(file=os.path.realpath(path_dir+'/pm2/' + real_file_list[xn]))
            label_2 = Label(root, image=image)
            label_2.place(x=0,y=150)
        
            
        
        btn = Button(root,text="next",command=showimg_next,width=7,height=1) 
        btn2 = Button(root,text="previous",command=showimg_previous,width=7,height=1) 
        label_1 = Label(root,text=month + '월 초미세먼지',font="NanumGothic 20")
        label_2 = Label(root, image=image)
        label_1.place(x=475,y=10)
        label_2.place(x=0,y=150)
        btn.place(x=575,y=50)
        btn2.place(x=425,y=50)

    def Graph_PM10(self):
        path_dir = os.path.dirname(os.path.realpath(__file__))
        global df3
        list = []
        temp = df3.date[0][0:10]
        list.append(temp)
        for i in range(1,len(df3)) :
            if i % 1440 == 0 : list.append(df3['date'][i][0:10])
            else : continue

        list1 = []
        list1.append(0)
        for i in range(1,len(df3)) :
            if i % 1440 == 0 : list1.append(i)
            else : continue
        
        dis_pm10 = []
        for i in range(0,len(df3)) :
            if  df3['pm10'][i] == df3['dis_pm10'][i] : dis_pm10.append(0)
            else : dis_pm10.append(df3['dis_pm10'][i])

        pm10 = pd.to_numeric(df3['pm10'])
        dis_pm10 = pd.to_numeric(dis_pm10)

        mat.rcParams['font.family'] = 'AppleMyungjo'
        month = str(df3['date'][0][5:7])
        day_minus = 0
        if str(df3['date'][len(df3)-1][8:10]) == '31' :
            day_minus = 0
        elif str(df3['date'][len(df3)-1][8:10]) == '30' :
            day_minus = 1
        elif str(df3['date'][len(df3)-1][8:10]) == '29' :
            day_minus = 2
        else :
            day_minus = 3
        mat.rcParams['font.family'] = 'AppleMyungjo'
        # 1~7
        plt.figure(figsize=(18, 8))
        plt.title(month + '월 1주차', fontsize=20)
        plt.plot(df3['date'][0:10080], pm10[0:10080] , label = '미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df3['date'][0:10080], dis_pm10[0:10080],  label = '정화된 미세먼지', color = 'b', linewidth=0.5)
        plt.legend(loc=(0.86, 0.9), fontsize=12)

        plt.ylabel('㎍/㎥', fontsize=14)
        plt.ylim(0.0, 200.0)

        plt.xticks(list1[0:7],list[0:7])
        plt.axhline(y=80, color='r', linewidth=1)
        plt.text(10665, 80, '미세먼지 나쁨 기준', fontsize = 12, color ='maroon')

        plt.grid()
        plt.savefig(path_dir+'/pm10/pm_10 1st.png', dpi=60)
        plt.close()

        # 8~14
        plt.figure(figsize=(18, 8))
        plt.title(month + '월 2주차', fontsize=20)
        plt.plot(df3['date'][10080:20160], pm10[10080:20160] , label = '미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df3['date'][10080:20160], dis_pm10[10080:20160], label = '정화된 미세먼지', color = 'b', linewidth=0.5)
        plt.legend(loc=(0.86, 0.9), fontsize=12)

        plt.ylabel('㎍/㎥', fontsize=14)
        plt.ylim(0.0, 200.0)

        plt.xticks(list1[0:7],list[7:14])
        plt.axhline(y=80, color='r', linewidth=1)
        plt.text(10665, 80, '미세먼지 나쁨 기준', fontsize = 12, color ='maroon')

        plt.grid()
        plt.savefig(path_dir+'/pm10/pm_10 2nd.png', dpi=60)
        plt.close()

        # 15~21
        plt.figure(figsize=(18, 8))
        plt.title(month + '월 3주차', fontsize=20)
        plt.plot(df3['date'][20160:30240], pm10[20160:30240] , label = '미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df3['date'][20160:30240], dis_pm10[20160:30240],  label = '정화된 미세먼지', color = 'b', linewidth=0.5)
        plt.legend(loc=(0.86, 0.9), fontsize=12)

        plt.ylabel('㎍/㎥', fontsize=14)
        plt.ylim(0.0, 200.0)

        plt.xticks(list1[0:7],list[14:21])
        plt.axhline(y=80, color='r', linewidth=1)
        plt.text(10665, 80, '미세먼지 나쁨 기준', fontsize = 12, color ='maroon')

        plt.grid()
        plt.savefig(path_dir+'/pm10/pm_10 3rd.png', dpi=60)
        plt.close()
        

        # 22~31
        plt.figure(figsize=(18, 8))
        plt.title(month + '월 4주차', fontsize=20)
        plt.plot(df3['date'][30240:len(df3)], pm10[30240:len(df3)] , label = '미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df3['date'][30240:len(df3)], dis_pm10[30240:len(df3)],  label = '정화된 미세먼지', color = 'b', linewidth=0.5)
        plt.legend(loc=(0.86, 0.9), fontsize=12)

        plt.ylabel('㎍/㎥', fontsize=14)
        plt.ylim(0.0, 200.0)

        plt.xticks(list1[0:10-day_minus],list[21:len(list)])
        plt.axhline(y=80, color='r', linewidth=1)
        plt.text(15275, 80, '미세먼지 나쁨 기준', fontsize = 12, color ='maroon')

        plt.grid()
        plt.savefig(path_dir+'/pm10/pm_10 4th.png', dpi=60)
        plt.close()

        file_list = os.listdir(path_dir+'/pm10')
        real_file_list = [x for x in file_list if(x.endswith(".PNG") or (x.endswith(".png")==True))]
        real_file_list.sort(key=lambda x: x[6:7])
        print(real_file_list)
        root=Toplevel()
        root.title("Graph PM10")
        root.geometry("1080x720")
        root.resizable(0,0)
        global xn
        xn = 0
        image=PhotoImage(file=os.path.realpath(path_dir+'/pm10/' + real_file_list[xn]))
        xn = -1
        def showimg_next():
            global xn
            global image
            xn += 1
            if(xn >= len(real_file_list)-1):
                xn = len(real_file_list)-1
            image=PhotoImage(file=os.path.realpath(path_dir+'/pm10/' + real_file_list[xn]))
            label_2 = Label(root, image=image)
            label_2.place(x=0,y=150)
        
        def showimg_previous():
            global xn
            global image
            xn -= 1
            if(xn <= 0):
                xn=0
            image=PhotoImage(file=os.path.realpath(path_dir+'/pm10/' + real_file_list[xn]))
            label_2 = Label(root, image=image)
            label_2.place(x=0,y=150)
        
            
        
        btn = Button(root,text="next",command=showimg_next,width=7,height=1) 
        btn2 = Button(root,text="previous",command=showimg_previous,width=7,height=1) 
        label_1 = Label(root,text=month + '월 미세먼지',font="NanumGothic 20")
        label_2 = Label(root, image=image)
        label_1.place(x=475,y=10)
        label_2.place(x=0,y=150)
        btn.place(x=575,y=50)
        btn2.place(x=425,y=50)

    def domenu(self):
    
        print("OK")
 
 
if __name__ == '__main__':
 
    Example = tkGUi()
