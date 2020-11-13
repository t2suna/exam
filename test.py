import wave
import pyaudio
import sys 
import tkinter as tk 
from tkinter import ttk
from tkinter import *

def evaluation(event=None):
    try:
        #what_do = txtBox.get()

        #path_w = 'test/exam.txt'
        #with open(path_w, mode='a') as f:
                #if len(lb.curselection())!= 0:
                    #f.write(str(lb.curselection()[0]+1)+".wav ")
                if len(lb2.curselection())!= 0:   
                #elif len(lb2.curselection())!= 0:
                    #f.write("a:"+str(v1.get())+" ")
                    lb2.insert(lb2.curselection()[0], v1.get())
                    lb2.delete(lb2.curselection()[0])
                elif len(lb3.curselection())!= 0:
                    #f.write("b:"+str(v1.get())+" ")
                    lb3.insert(lb3.curselection()[0], v1.get())
                    lb3.delete(lb3.curselection()[0])
                elif len(lb4.curselection())!= 0:
                    #f.write("c:"+str(v1.get())+" ")
                    lb4.insert(lb4.curselection()[0], v1.get())
                    lb4.delete(lb4.curselection()[0])
                elif len(lb5.curselection())!= 0:
                    #f.write("d:"+str(v1.get())+" ")
                    lb5.insert(lb5.curselection()[0], v1.get())
                    lb5.delete(lb5.curselection()[0])
                elif len(lb6.curselection())!= 0:
                    #f.write("e:"+str(v1.get())+" ")
                    lb6.insert(lb6.curselection()[0], v1.get())
                    lb6.delete(lb6.curselection()[0])
                elif len(lb7.curselection())!= 0:
                    #f.write("f:"+str(v1.get())+" ")
                    lb7.insert(lb7.curselection()[0], v1.get())
                    lb7.delete(lb7.curselection()[0])
                elif len(lb8.curselection())!= 0:
                    #f.write("g:"+str(v1.get())+" ")
                    lb8.insert(lb8.curselection()[0], v1.get())
                    lb8.delete(lb8.curselection()[0])
                elif len(lb9.curselection())!= 0:
                    #f.write("h:"+str(v1.get())+" ")
                    lb9.insert(lb9.curselection()[0], v1.get())
                    lb9.delete(lb9.curselection()[0])
                elif len(lb10.curselection())!= 0:
                    #f.write("i:"+str(v1.get())+" ")
                    lb10.insert(lb10.curselection()[0], v1.get())
                    lb10.delete(lb10.curselection()[0])
                elif len(lb11.curselection())!= 0:
                    #f.write("j:"+str(v1.get())+"\n")
                    lb11.insert(lb11.curselection()[0], v1.get())
                    lb11.delete(lb11.curselection()[0])
    except ValueError:
        # ユーザーIDが文字だった場合は何もしない
        pass
    except IndexError:
        # ユーザーIDが文字だった場合は何もしない
        pass

def play(event=None):
    # チャンクサイズ(粒度)
    CHUNK_SIZE = 1024
    # WAVファイルを開く  
    if len(lb.curselection())!= 0:
        wf = wave.open("test/"+str(lb.curselection()[0]+1)+ '.wav', 'rb')
    elif len(lb2.curselection())!= 0:
        wf = wave.open("test/"+str(lb2.curselection()[0]+1)+ '.wav', 'rb')    
    elif len(lb3.curselection())!= 0:
        wf = wave.open("test/"+str(lb3.curselection()[0]+1)+ '.wav', 'rb')
    elif len(lb4.curselection())!= 0:
        wf = wave.open("test/"+str(lb4.curselection()[0]+1)+ '.wav', 'rb')
    elif len(lb5.curselection())!= 0:
        wf = wave.open("test/"+str(lb5.curselection()[0]+1)+ '.wav', 'rb')
    elif len(lb6.curselection())!= 0:
        wf = wave.open("test/"+str(lb6.curselection()[0]+1)+ '.wav', 'rb')
    elif len(lb7.curselection())!= 0:
        wf = wave.open("test/"+str(lb7.curselection()[0]+1)+ '.wav', 'rb')
    elif len(lb8.curselection())!= 0:
        wf = wave.open("test/"+str(lb8.curselection()[0]+1)+ '.wav', 'rb')    
    elif len(lb9.curselection())!= 0:
        wf = wave.open("test/"+str(lb9.curselection()[0]+1)+ '.wav', 'rb') 
    elif len(lb10.curselection())!= 0:
        wf = wave.open("test/"+str(lb10.curselection()[0]+1)+ '.wav', 'rb')      
    elif len(lb11.curselection())!= 0:
        wf = wave.open("test/"+str(lb11.curselection()[0]+1)+ '.wav', 'rb')     
    else:
        wf = wave.open("test/volume.wav", 'rb')
            
    # PyAudioインスタンスを作成する
    p = pyaudio.PyAudio()
    
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    
    # データをチャンクサイズだけ読み込む
    data = wf.readframes(CHUNK_SIZE)
    
    # Streamに読み取ったデータを書き込む＝再生する
    while len(data) > 0:
        # Streamに書き込む
        stream.write(data)
    
        # 再度チャンクサイズだけ読み込む。これを繰り返す
        data = wf.readframes(CHUNK_SIZE)
    
    # Streamを止めて、closeする。closeしなければ、start_stream()で再開できる
    stream.stop_stream()
    stream.close()
    
    # PyAudioインスタンスを破棄する
    p.terminate()

def save(event=None):
    path_w = 'test/exam.txt'
    with open(path_w, mode='a') as f:
        f.write("\n"+nametxt.get()+" \n")
        for i in range(10):
            chr_s = chr(i+97)
            f.write(str(chr_s)+" "+int_var[i].get()+"\n")
root = tk.Tk()
root.title("実験用プログラム")
root.geometry("850x600")

frame1 = ttk.Frame(root, padding=5)
frame1.grid()


 # Label Frame
label_frame = ttk.Labelframe(
    frame1,
    text='Score',
    padding=(10),
    style='My.TLabelframe')

v1 = IntVar()
rb1 = ttk.Radiobutton(
    label_frame,
    text='非常に',
    value=1,
    variable=v1)

rb2 = ttk.Radiobutton(
    label_frame,
    text='かなり',
    value=2,
    variable=v1)

rb3 = ttk.Radiobutton(
    label_frame,
    text='やや',
    value=3,
    variable=v1)

rb4 = ttk.Radiobutton(
    label_frame,
    text='どちらともいえない',
    value=4,
    variable=v1)

rb5 = ttk.Radiobutton(
    label_frame,
    text='やや',
    value=5,
    variable=v1)

rb6 = ttk.Radiobutton(
    label_frame,
    text='かなり',
    value=6,
    variable=v1)    

rb7 = ttk.Radiobutton(
    label_frame,
    text='非常に',
    value=7,
    variable=v1)    
# Layout
frame1.grid()
label_frame.grid(row=1, column=0)



button_a = ttk.Button(frame1,text='評価', width=20)
button_a.grid(row=3, column=0)
button_a.bind('<Button>',evaluation)




rb1.grid(row=0, column=1) # LabelFrame
rb2.grid(row=0, column=2) # LabelFrame
rb3.grid(row=0, column=3) # LabelFrame
rb4.grid(row=0, column=4) # LabelFrame
rb5.grid(row=0, column=5) # LabelFrame
rb6.grid(row=0, column=6) # LabelFrame
rb7.grid(row=0, column=7) # LabelFrame





frame2 = ttk.Frame(root)
frame2.grid()

#リストボックス
listarray = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
txt = tk.StringVar(value=listarray) #文字列なのでStringVar()でオブジェクトを生成
lb = tk.Listbox(frame2, listvariable=txt, width=5, height=16)

listvalue = [[0] for _ in range(len(listarray))]
int_var = []
for i in range(10):
    #int_var.append(IntVar(value=listvalue))
    int_var.append(tk.StringVar(value=listvalue))
lb2 = tk.Listbox(frame2, listvariable=int_var[0], width=5, height=16)
lb3 = tk.Listbox(frame2, listvariable=int_var[1], width=5, height=16)
lb4 = tk.Listbox(frame2, listvariable=int_var[2], width=5, height=16)
lb5 = tk.Listbox(frame2, listvariable=int_var[3], width=5, height=16)
lb6 = tk.Listbox(frame2, listvariable=int_var[4], width=5, height=16)
lb7 = tk.Listbox(frame2, listvariable=int_var[5], width=5, height=16)
lb8 = tk.Listbox(frame2, listvariable=int_var[6], width=5, height=16)
lb9 = tk.Listbox(frame2, listvariable=int_var[7], width=5, height=16)
lb10 = tk.Listbox(frame2, listvariable=int_var[8], width=5, height=16)
lb11 = tk.Listbox(frame2, listvariable=int_var[9], width=5, height=16)

"""
#スクロールバーの生成・配置
scrollbar = ttk.Scrollbar(frame2, orient=tk.VERTICAL, command=lb.yview)
scrollbar.pack(fill='y', side='right')
"""




label1 = tk.Label(frame2,text="番号",width=10)  #文字ラベル設定
label1.grid(row=1, column=0) # 場所を指定　（top, bottom, left, or right）
label2 = tk.Label(frame2, text="快適な/不快な")  #文字ラベル設定
label2.grid(row=1, column=1) 
label3 = tk.Label(frame2, text="明るい/暗い")  #文字ラベル設定
label3.grid(row=1, column=2) 
label4 = tk.Label(frame2, text="滑らか/ざらついた")  #文字ラベル設定
label4.grid(row=1, column=3) 
label5 = tk.Label(frame2, text="鋭い/鈍い")  #文字ラベル設定
label5.grid(row=1, column=4) 
label6 = tk.Label(frame2, text="騒々しい/静かな")  #文字ラベル設定
label6.grid(row=1, column=5) 
label7 = tk.Label(frame2, text="硬い/柔らかい")  #文字ラベル設定
label7.grid(row=1, column=6) 
label8 = tk.Label(frame2, text="高い/低い")  #文字ラベル設定
label8.grid(row=1, column=7) 
label9 = tk.Label(frame2, text="澄んだ/濁った")  #文字ラベル設定
label9.grid(row=1, column=8) 
label10 = tk.Label(frame2, text="弱い/強い")  #文字ラベル設定
label10.grid(row=1, column=9) 
label11 = tk.Label(frame2, text="変動の大きい/小さい")  #文字ラベル設定
label11.grid(row=1, column=10) 




lb.grid(row=2, column=0) 
lb2.grid(row=2, column=1)

lb3.grid(row=2, column=2)
lb4.grid(row=2, column=3)
lb5.grid(row=2, column=4)
lb6.grid(row=2, column=5)
lb7.grid(row=2, column=6)
lb8.grid(row=2, column=7)
lb9.grid(row=2, column=8)
lb10.grid(row=2, column=9)
lb11.grid(row=2, column=10)

frame3 = ttk.Frame(root)
frame3.grid()


button_d = ttk.Button(frame3,text='再生', width=20)
button_d.grid(row=2, column=1,pady=20)
button_d.bind('<Button>',play)


lbl = tk.Label(frame3,text='名前')
lbl.grid(row=3, column=1)

nametxt = tk.Entry(frame3,width=20)
nametxt.grid(row=4,column=1,padx=20)

button_ok = ttk.Button(frame3,text='OK', width=5)
button_ok.grid(row=5, column=1,padx=50,pady=10)
button_ok.bind('<Button>',save)

root.mainloop()
