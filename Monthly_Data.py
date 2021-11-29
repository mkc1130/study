from tkinter import *
 
from tkinter import filedialog

from tkinter import scrolledtext

import numpy as np

import pandas as pd

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

        self.root.title("Monthly Data")
        self.label = Label(self.root, text='데이터를 불러오면 이 곳에 표시됩니다.')
        self.label.grid(row=0, column=0)

        self.label1 = Label(self.root, text='데이터를 정렬하면 이 곳에 표시됩니다.')
        self.label1.grid(row=0, column=1)
        
        menubar = Menu(self.root)
        self.root.geometry('1100x500')
        
        self.text = scrolledtext.ScrolledText(self.root, width=75, height=35)
        
        self.text.grid(row=1, column=0)

        self.text1 = scrolledtext.ScrolledText(self.root, width=75, height=35)

        self.text1.grid(row=1, column=1)
        
        filemenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="File", menu=filemenu)
        
        filemenu.add_command(label="데이터 파일 불러오기", command=self.Load)

        filemenu.add_command(label="데이터 삽입하기", command=self.Insert)
        
        filemenu.add_command(label="데이터 정렬하기", command=self.Sort)
        
        filemenu.add_command(label="초미세먼지 그래프 출력하기", command=self.Graph_PM2)
        
        filemenu.add_command(label="미세먼지 그래프 출력하기", command=self.Graph_PM10)
        
        filemenu.add_separator()
        
        filemenu.add_command(label="Exit", command=self.root.quit)
 
        self.root.config(menu=menubar)
        
        self.root.mainloop()
 
    def Load(self):
        global filename
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("text files", "*.txt"),
                                              ("all files", "*.*")))

        print(filename)
        
        #global df
        #df = pd.read_csv(filename, header=None, names=['date','temperature','humidity','pm2.5','dis_pm2.5','pm10','dis_pm10','purifi_amount','purifi_tree','is_working','is_warter_short'])

        #for i in range(0, 44637) :
        #    temp = str(df['date'][i][1:17])
        #    df['date'][i] = temp
        
        #df.reset_index(drop=True)
        #self.text.delete('1.0', END)
        
        #self.text.insert(END, df)
        data=open(filename,'rt',encoding="utf-8")
        
        self.text.delete('1.0', END)
        
        self.text.insert(END,data.read())
        self.label = Label(self.root, text='데이터를 추가적으로 삽입하시거나 정렬시키십시오.')
        self.label.grid(row=0, column=0)

    def Insert(self):
        global filename
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("text files", "*.txt"),
                                              ("all files", "*.*")))
        
        print(filename)
        data=open(filename,'rt',encoding="utf-8")
        self.text.insert(END,data.read())
        f = filedialog.asksaveasfile(mode = "w", defaultextension=".txt")
        if f is None:
            return
        ts = str(self.text.get(1.0, END))
        f.write(ts)
        f.close()
    def Sort(self):
        
        global filename
        global df
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("text files", "*.txt"),
                                              ("all files", "*.*")))

        # 데이터 불러오기

        pd.set_option('mode.chained_assignment',  None)
        pd.set_option('display.max_row', None)

        df = pd.read_csv(filename, header=None, names=['date','temperature','humidity','pm2.5','dis_pm2.5','pm10','dis_pm10','purifi_amount','purifi_tree','is_working','is_warter_short'])


        year = df['date'][0][1:5]
        month = df['date'][0][6:8]
        global day
        day = []
        temp = [0,1,2,3,4,5,6,7,8,9]
        temp2 = ['01','03','05','07','08','10','12']
        if int(year) % 4 == 0 and month == '02' : day = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29']
        elif month in temp2 : day = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
        else : day = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
        length = len(day) * 1440    
                
        hour = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']

        minute = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59']
                
        df2 = df

        #데이터 정렬

        d = 0
        h = 0
        m = 0

        for i in range(length) : 
            tempStr= year + '-' + month + '-' + day[d] + ' ' + hour[h] + ':' + minute[m]
            if len(df) > i :
                df['date'][i] = tempStr
            else : 
                temperature = np.around(df['temperature'][len(df)-2:len(df)].mean(),2)
                humidity = np.around(df['humidity'][len(df)-2:len(df)].mean(),2)
                pm2 = np.around(df['pm2.5'][len(df)-2:len(df)].mean(),2)
                dis_pm2 = np.around(df['dis_pm2.5'][len(df)-2:len(df)].mean(),2)
                pm10 = np.around(df['pm10'][len(df)-2:len(df)].mean(),2)
                dis_pm10 = np.around(df['dis_pm10'][len(df)-2:len(df)].mean(),2)
                date = tempStr   
                df.loc[len(df)] = [date,temperature, humidity, pm2, dis_pm2, pm10, dis_pm10, 202125, 49, 0 , 1]
                df.tail()
            m += 1
            if m == 60 :
                m = 0
                h += 1
                if h == 24 :
                    h = 0
                    d += 1


        self.text1.delete('1.0', END)
        
        self.text1.insert(END, df[['date', 'pm2.5', 'dis_pm2.5', 'pm10', 'dis_pm10', 'is_working']])
        self.text1.configure(state='disabled')
        self.label1 = Label(self.root, text='정렬된 데이터를 시각화 하기위해 그래프를 출력하십시오.')
        self.label1.grid(row=0, column=1)

    def Graph_PM2(self):
        def createFolder(directory):
            try:
                if not os.path.exists(directory):
                    os.makedirs(directory, exist_ok=True)
            except OSError:
                print ('Error: Creating directory. ' +  directory)
        
        path_dir = os.path.dirname(os.path.realpath(__file__))
        createFolder(path_dir + '/pm2')
        global df
        list = []
        temp = df.date[0][0:10]
        list.append(temp)
        for i in range(1,len(df)) :
            if i % 1440 == 0 : list.append(df['date'][i][0:10])
            else : continue

        list1 = []
        list1.append(0)
        for i in range(1,len(df)) :
            if i % 1440 == 0 : list1.append(i)
            else : continue
        
        dis_pm2 = []
        for i in range(0,len(df)) :
            if  df['pm2.5'][i] == df['dis_pm2.5'][i] : dis_pm2.append(0)
            else : dis_pm2.append(df['dis_pm2.5'][i])

        pm2 = pd.to_numeric(df['pm2.5'])
        dis_pm2 = pd.to_numeric(dis_pm2)

        mat.rcParams['font.family'] = 'AppleGothic'
        month = str(df['date'][0][5:7])
        day_minus = 0
        if day[len(day)-1] == '31' :
            day_minus = 0
        elif day[len(day)-1] == '30' :
            day_minus = 1
        elif day[len(day)-1] == '29' :
            day_minus = 2
        else :
            day_minus = 3
        # 1~7
        plt.figure(figsize=(18, 8))
        plt.title(month + '월 1주차', fontsize=20)
        plt.plot(df['date'][0:10080], pm2[0:10080] , label = '초미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df['date'][0:10080], dis_pm2[0:10080],  label = '정화된 초미세먼지', color = 'b', linewidth=0.5)
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
        plt.plot(df['date'][10080:20160], pm2[10080:20160] , label = '초미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df['date'][10080:20160], dis_pm2[10080:20160], label = '정화된 초미세먼지', color = 'b', linewidth=0.5)
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
        plt.plot(df['date'][20160:30240], pm2[20160:30240] , label = '초미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df['date'][20160:30240], dis_pm2[20160:30240],  label = '정화된 초미세먼지', color = 'b', linewidth=0.5)
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
        plt.plot(df['date'][30240:len(df)], pm2[30240:len(df)] , label = '초미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df['date'][30240:len(df)], dis_pm2[30240:len(df)],  label = '정화된 초미세먼지', color = 'b', linewidth=0.5)
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
        root.geometry("1080x600")
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
        label_1 = Label(root,text=month + '월 초미세먼지',font=("AppleGothic",26))
        label_2 = Label(root, image=image)
        label_1.pack(side='top')
   
        btn.place(x=565,y=50)
        btn2.place(x=415,y=50)
        label_2.pack(side='bottom',fill="x")

    def Graph_PM10(self):
        def createFolder(directory):
            try:
                if not os.path.exists(directory):
                    os.makedirs(directory, exist_ok=True)
            except OSError:
                print ('Error: Creating directory. ' +  directory)
        
        path_dir = os.path.dirname(os.path.realpath(__file__))
        createFolder(path_dir + '/pm10')
        global df
        list = []
        temp = df.date[0][0:10]
        list.append(temp)
        for i in range(1,len(df)) :
            if i % 1440 == 0 : list.append(df['date'][i][0:10])
            else : continue

        list1 = []
        list1.append(0)
        for i in range(1,len(df)) :
            if i % 1440 == 0 : list1.append(i)
            else : continue
        
        dis_pm10 = []
        for i in range(0,len(df)) :
            if  df['pm10'][i] == df['dis_pm10'][i] : dis_pm10.append(0)
            else : dis_pm10.append(df['dis_pm10'][i])

        pm10 = pd.to_numeric(df['pm10'])
        dis_pm10 = pd.to_numeric(dis_pm10)

        mat.rcParams['font.family'] = 'AppleGothic'
        month = str(df['date'][0][5:7])
        day_minus = 0
        if day[len(day)-1] == '31' :
            day_minus = 0
        elif day[len(day)-1] == '30' :
            day_minus = 1
        elif day[len(day)-1] == '29' :
            day_minus = 2
        else :
            day_minus = 3
        # 1~7
        plt.figure(figsize=(18, 8))
        plt.title(month + '월 1주차', fontsize=20)
        plt.plot(df['date'][0:10080], pm10[0:10080] , label = '미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df['date'][0:10080], dis_pm10[0:10080],  label = '정화된 미세먼지', color = 'b', linewidth=0.5)
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
        plt.plot(df['date'][10080:20160], pm10[10080:20160] , label = '미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df['date'][10080:20160], dis_pm10[10080:20160], label = '정화된 미세먼지', color = 'b', linewidth=0.5)
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
        plt.plot(df['date'][20160:30240], pm10[20160:30240] , label = '미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df['date'][20160:30240], dis_pm10[20160:30240],  label = '정화된 미세먼지', color = 'b', linewidth=0.5)
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
        plt.plot(df['date'][30240:len(df)], pm10[30240:len(df)] , label = '미세먼지', color = 'r', linewidth=0.5)
        plt.plot(df['date'][30240:len(df)], dis_pm10[30240:len(df)],  label = '정화된 미세먼지', color = 'b', linewidth=0.5)
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
        root.geometry("1080x600")
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
        label_1 = Label(root,text=month + '월 미세먼지',font=("AppleGothic",26))
        label_2 = Label(root, image=image)
        label_1.pack(side='top')
   
        btn.place(x=565,y=50)
        btn2.place(x=415,y=50)
        label_2.pack(side='bottom',fill="x")

if __name__ == '__main__':
 
    Example = tkGUi()