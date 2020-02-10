#!nasheq/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import traceback
import tkinter as tk
import tkinter.ttk
from tkinter import messagebox
import os, sys
from src.nash import Nash

#class ApplicationR(tk.Frame):
    #def __init__(self, master=None):
        #super().__init__(master)
        #self.master = master
        #self.master.title("Game Theory Solver")
        #self.pack()
        #self.logo = tk.PhotoImage(file="log.png")
        #self.w1 = tk.Label(self, image=self.logo)
        #self.w1.grid(padx=(10,10),pady=(10,10))
        #self.welcome=tk.PanedWindow(orient=tk.VERTICAL)
        #self.welcome.pack(expand=1)
        #self.create_widgets()

    #def create_widgets(self):
        ## self.w1.pack(side="right")
        #title = tk.Label(self.welcome,text="Welcome to game theory solver",font=("Helvetica", 16))
        #self.welcome.add(title)
        ## self.title.pack()
        #tplayers = tk.Button(self.welcome)
        #tplayers["text"] = "Two Players Game"
        #tplayers["command"] = self.two_players
        ## self.tplayers.pack(side="top")
        #self.welcome.add(tplayers)
        #thplayers = tk.Button(self.welcome)
        #thplayers["text"] = "Three Players Game"
        #thplayers["command"] = self.three_players
        #self.welcome.add(thplayers)
        ## self.thplayers.pack(side="top")
        #quit = tk.Button(self.welcome, text="QUIT", fg="red",command=self.master.destroy)
        #self.welcome.add(quit)
        ## self.quit.pack(side="bottom")

    #def three_players(self):
        #self.welcome.destroy()
        #self.threeplayers = tk.PanedWindow(orient=tk.VERTICAL)
        #self.threeplayers.pack(expand=1)
        #tk.Label(self.threeplayers, text="Three Players Game", font=("Helvetica", 16)).grid(row=1, columnspan=4,padx=(10, 10))
        #tk.Label(self.threeplayers, text="Please enter the stratigies for every player",font=("Helvetica", 12)).grid(row=2, columnspan=4, padx=(10, 10))
        #tk.Label(self.threeplayers, text="First Player").grid(row=3, column=1, padx=(10, 10))
        #tk.Label(self.threeplayers, text="Second Player").grid(row=3, column=2, padx=(10, 10))
        #tk.Label(self.threeplayers, text="Third Player").grid(row=3, column=3, padx=(10, 10))
        #tk.Label(self.threeplayers, text="Strategy 1").grid(row=4, column=0, padx=(10, 10))
        #tk.Label(self.threeplayers, text="Strategy 2").grid(row=5, column=0, padx=(10, 10))
        #self.flabels_three_players = []
        #self.flabels_three_players.append(tk.Entry(self.threeplayers))
        #self.flabels_three_players[-1].grid(row=4,column=1,padx=(10, 10),pady=(10, 10))
        #self.flabels_three_players.append(tk.Entry(self.threeplayers))
        #self.flabels_three_players[-1].grid(row=5, column=1, padx=(10, 10), pady=(10, 10))
        #self.slabels_three_players = []
        #self.slabels_three_players.append(tk.Entry(self.threeplayers))
        #self.slabels_three_players[-1].grid(row=4, column=2, padx=(10, 10), pady=(10, 10))
        #self.slabels_three_players.append(tk.Entry(self.threeplayers))
        #self.slabels_three_players[-1].grid(row=5, column=2, padx=(10, 10), pady=(10, 10))
        #self.tlabels_three_players = []
        #self.tlabels_three_players.append(tk.Entry(self.threeplayers))
        #self.tlabels_three_players[-1].grid(row=4, column=3, padx=(10, 10), pady=(10, 10))
        #self.tlabels_three_players.append(tk.Entry(self.threeplayers))
        #self.tlabels_three_players[-1].grid(row=5, column=3, padx=(10, 10), pady=(10, 10))
        #tk.Button(self.threeplayers, text="Submit", command=self.three_players_Utility).grid(row=6, column=3,padx=(10, 10),pady=(10, 10))

    #def three_players_Utility(self):
        #check=True
        #for i in self.slabels_three_players:
            #if len(i.get())==0:
                #check=False
                #messagebox.showinfo("Error in the input", "Please make sure you fill all the inputs!!!")
                #break
        #if check:
            #for i in self.flabels_three_players:
                #if len(i.get())==0:
                    #check=False
                    #messagebox.showinfo("Error in the input", "Please make sure you fill all the inputs!!!")
                    #break
            #if check:
                #for i in self.tlabels_three_players:
                    #if len(i.get())==0:
                        #check=False
                        #messagebox.showinfo("Error in the input", "Please make sure you fill all the inputs!!!")
                        #break
        #if check:
            #self.threeplayersU = tk.PanedWindow(orient=tk.VERTICAL)
            #self.threeplayersU.pack()
            #tk.Label(self.threeplayersU, text="Three Players Game", font=("Helvetica", 16)).grid(row=1, columnspan=21,padx=(10, 10))
            #tk.Label(self.threeplayersU, text="Please fill the utility matrices", font=("Helvetica", 12)).grid(row=2, columnspan=21, padx=(10, 10))
            #tk.Label(self.threeplayersU, text="Third player plays "+self.tlabels_three_players[0].get(), font=("Helvetica", 12)).grid(row=4,column=0,columnspan=8,padx=(10, 10),pady=(10, 10))
            #tk.Label(self.threeplayersU, text="Third player plays " + self.tlabels_three_players[1].get(),font=("Helvetica", 12)).grid(row=4, column=11,columnspan=8,padx=(10, 10),pady=(10, 10))
            #tk.Label(self.threeplayersU, text="Second Player " ,font=("Helvetica", 12)).grid(row=5, column=2,columnspan=6,padx=(10, 10))
            #tk.Label(self.threeplayersU, text=self.slabels_three_players[0].get() ,font=("Helvetica", 12)).grid(row=6, column=2,columnspan=3,padx=(10, 10))
            #tk.Label(self.threeplayersU, text=self.slabels_three_players[1].get() ,font=("Helvetica", 12)).grid(row=6, column=5,columnspan=3,padx=(10, 10))
            #tk.Label(self.threeplayersU, text="Second Player " ,font=("Helvetica", 12)).grid(row=5, column=13,columnspan=6,padx=(10, 10))
            #tk.Label(self.threeplayersU, text=self.slabels_three_players[0].get(), font=("Helvetica", 12)).grid(row=6,column=13,columnspan=3,padx=(10, 10))
            #tk.Label(self.threeplayersU, text=self.slabels_three_players[1].get(), font=("Helvetica", 12)).grid(row=6,column=16,columnspan=3,padx=(10, 10))
            #tkinter.ttk.Separator(self.threeplayersU, orient=tk.HORIZONTAL).grid( row=3, columnspan=21,sticky="ew")
            #tkinter.ttk.Separator(self.threeplayersU, orient=tk.VERTICAL).grid(column=10, row=4, rowspan=5, sticky='ns',padx=(10,10))
            #tkinter.ttk.Separator(self.threeplayersU, orient=tk.VERTICAL).grid(column=19, row=4, rowspan=5, sticky='ns',padx=(10,10))
            #tk.Label(self.threeplayersU, text="First Player " ,font=("Helvetica", 12)).grid(row=7,rowspan=2, column=0,padx=(10, 10))
            #tk.Label(self.threeplayersU, text=self.flabels_three_players[0].get(),font=("Helvetica", 12)).grid(row=7,column=1,padx=(10, 10))
            #tk.Label(self.threeplayersU, text=self.flabels_three_players[1].get(),font=("Helvetica", 12)).grid(row=8,column=1,padx=(10, 10))
            #tk.Label(self.threeplayersU, text="First Player " ,font=("Helvetica", 12)).grid(row=7,rowspan=2, column=11,padx=(10, 10))
            #tk.Label(self.threeplayersU, text=self.flabels_three_players[0].get(), font=("Helvetica", 12)).grid(row=7,column=12,padx=(10, 10))
            #tk.Label(self.threeplayersU, text=self.flabels_three_players[1].get(), font=("Helvetica", 12)).grid(row=8,column=12,padx=(10, 10))

            #self.UtilityTHreePlayers=[]
            #tempo=[]
            #for i in range(2):
                #temp=[]
                #k=0
                #for _ in range(2):
                    #temp1=[]
                    #temp1.append(tk.Entry(self.threeplayersU, width=5))
                    #temp1[-1].grid(row=7 + i, column=2 + k, padx=(5, 5), pady=(5, 5))
                    #k+=1
                    #temp1.append(tk.Entry(self.threeplayersU, width=5))
                    #temp1[-1].grid(row=7 + i, column=2 + k, padx=(5, 5), pady=(5, 5))
                    #k+=1
                    #temp1.append(tk.Entry(self.threeplayersU, width=5))
                    #temp1[-1].grid(row=7 + i, column=2 + k, padx=(5, 5), pady=(5, 5))
                    #k += 1
                    #temp.append(temp1)
                #tempo.append(temp)
            #self.UtilityTHreePlayers.append(tempo)
            #tempo = []
            #for i in range(2):
                #temp=[]
                #k=0
                #for _ in range(2):
                    #temp1=[]
                    #temp1.append(tk.Entry(self.threeplayersU, width=5))
                    #temp1[-1].grid(row=7 + i, column=13 + k, padx=(5, 5), pady=(5, 5))
                    #k+=1
                    #temp1.append(tk.Entry(self.threeplayersU, width=5))
                    #temp1[-1].grid(row=7+ i, column=13 + k, padx=(5, 5), pady=(5, 5))
                    #k+=1
                    #temp1.append(tk.Entry(self.threeplayersU, width=5))
                    #temp1[-1].grid(row=7 + i, column=13 + k, padx=(5, 5), pady=(5, 5))
                    #k += 1
                    #temp.append(temp1)
                #tempo.append(temp)
            #self.UtilityTHreePlayers.append(tempo)
            #print(self.UtilityTHreePlayers)
            #tk.Button(self.threeplayersU, text="Submit", command=self.generateThreePlayersUtility).grid(row=7, column=20,padx=(10, 10), pady=(10, 10))
            #tk.Button(self.threeplayersU, text="Home Page", command=self.restart_program).grid(row=8, column=20,padx=(10, 10), pady=(10, 10))
            #self.threeplayers.destroy()

    #def restart_program(self):
        #"""Restarts the current program.
        #Note: this function does not return. Any cleanup action (like
        #saving data) must be done before calling this function."""
        #python = sys.executable
        #os.execl(python, python, *sys.argv)
    #def generateThreePlayersUtility(self):
        #self.UtilityThPlayers = []
        #try:
            #for i in range(len(self.UtilityTHreePlayers)):
                #temp = []
                #for j in range(len(self.UtilityTHreePlayers[i])):
                    #temp1 = []
                    #for k in range(len(self.UtilityTHreePlayers[i][j])):
                        #temp2 = []
                        #for u in range(len(self.UtilityTHreePlayers[i][j][k])):
                            #temp2.append(int(self.UtilityTHreePlayers[i][j][k][u].get()))
                        #temp1.append(temp2)
                    #temp.append(temp1)
                #self.UtilityThPlayers.append(temp)
        #except SystemExit as msg:
            #print("error")
            #raise SystemExit(msg)
        #except:
            #raise SystemExit("error1")

        #print(self.UtilityThPlayers)

    #def two_players(self):
        #self.welcome.destroy()
        #self.twplayers = tk.PanedWindow(orient=tk.VERTICAL)
        #self.twplayers.pack()
        #tk.Label(self.twplayers, text="Two Players Game", font=("Helvetica", 16)).grid(row=1, column=1,padx=(10, 10))
        #tk.Label(self.twplayers, text="Please enter how many stratigies for every player",font=("Helvetica", 12)).grid(row=2, column=1, padx=(10, 10))
        #tk.Label(self.twplayers, text="First Player").grid(row=3, column=0, padx=(10, 10))
        #self.FplayerSC = tk.Entry(self.twplayers)
        #self.FplayerSC.grid(row=3, column=1, padx=(10, 10))
        #tk.Label(self.twplayers, text="Second Player").grid(row=4, column=0, padx=(10, 10))
        #self.SplayerSC = tk.Entry(self.twplayers)
        #self.SplayerSC.grid(row=4, column=1, padx=(10, 10))
        #tk.Button(self.twplayers, text="Submit", command=self.two_players_labels).grid(row=5, column=1, padx=(10, 10),pady=(10,10))
        ## self.twplayers.add(title)
        ## self.twplayers.add(inputL)

    #def two_players_labels(self):
        #f=int(self.FplayerSC.get())
        #s=int(self.SplayerSC.get())
        #self.twplayers.destroy()
        #self.twplayerslabels=tk.PanedWindow(orient=tk.VERTICAL)
        #self.twplayerslabels.pack()
        #tk.Label(self.twplayerslabels, text="Two Players Game", font=("Helvetica", 16)).grid(row=1,columnspan=2,padx=(10, 10))
        #tk.Label(self.twplayerslabels, text="Please enter the stratigies labels for every player",font=("Helvetica", 12)).grid(row=2,columnspan=2, padx=(10, 10))
        #tk.Label(self.twplayerslabels, text="First Player").grid(row=3, column=0, padx=(10, 10))
        #self.flabels=[]
        #for i in range(f):
            #self.flabels.append(tk.Entry(self.twplayerslabels))
            #self.flabels[-1].grid(row=4+i, column=0, padx=(10, 10))
        ## self.FplayerSC = tk.Entry(self.twplayerslabels).grid(row=3, column=1, padx=(10, 10))
        #tk.Label(self.twplayerslabels, text="Second Player").grid(row=3, column=1, padx=(10, 10))
        #self.slabels = []
        #for i in range(s):
            #self.slabels.append(tk.Entry(self.twplayerslabels))
            #self.slabels[-1].grid(row=4 + i, column=1, padx=(10, 10))
        #tk.Button(self.twplayerslabels, text="Submit", command=self.two_players_utility).grid(row=4+max(s,f), columnspan=2, padx=(10, 10),pady=(10, 10))

    #def two_players_utility(self):
        #self.twplayersUtility = tk.PanedWindow(orient=tk.VERTICAL)
        #self.twplayersUtility.pack()
        #tk.Label(self.twplayersUtility, text="Two Players Game", font=("Helvetica", 16)).grid(row=1,columnspan=2*len(self.slabels)+2,padx=(10, 10))
        #tk.Label(self.twplayersUtility, text="Please fill the utility matrix",font=("Helvetica", 12)).grid(row=2, columnspan=2*len(self.slabels)+2, padx=(10, 10))
        #tk.Label(self.twplayersUtility,anchor="e", text="First Player").grid(row=3, column=2,columnspan=2*len(self.slabels), padx=(10, 10))
        #for i in range(len(self.slabels)):
            #tk.Label(self.twplayersUtility, text=self.slabels[i].get()).grid(row=4, column=2+2*i,columnspan=2,padx=(10, 10))
        #self.GUtility=[]
        #for i in range(len(self.flabels)):
            #tk.Label(self.twplayersUtility, text=self.flabels[i].get()).grid(row=5+i, column=1, padx=(10, 10))
            #temp = []
            #k=0
            #for _ in range(len(self.slabels)):
                #temp1=[]
                #temp1.append(tk.Entry(self.twplayersUtility,width=10))
                #temp1[-1].grid(row=5+i,column=2+k,padx=(5, 5),pady=(5, 5))
                #k+=1
                #temp1.append(tk.Entry(self.twplayersUtility,width=10))
                #temp1[-1].grid(row=5+i,column=2+k,padx=(5, 5),pady=(5, 5))
                #k += 1
                #temp.append(temp1)
            #self.GUtility.append(temp)
        #tk.Label(self.twplayersUtility, text="Second Player").grid(row=5, rowspan=len(self.flabels), padx=(10, 10))
        #tk.Button(self.twplayersUtility, text="Submit", command=self.generateTwoPlayersUtility).grid(row=6+len(self.flabels), column=(2*len(self.slabels)+2)//2, padx=(10, 10),pady=(10, 10))
        #self.twplayerslabels.destroy()
    #def generateTwoPlayersUtility(self):
        #self.Utility=[]
        #for i in range(len(self.GUtility)):
            #temp=[]
            #for j in range(len(self.GUtility[i])):
                #temp1=[]
                #for k in range(len(self.GUtility[i][j])):
                    #temp1.append(int(self.GUtility[i][j][k].get()))
                #temp.append(temp1)
            #self.Utility.append(temp)
        #print(self.Utility)


class Application(tk.Frame):
    def __init__(self, master=None):
        ## initialize
        self.welcome = None
        self.TwoPlayersPanel = None
        self.TwoPlayersLabelsPanel = None
        self.TwoPlayersUtilityPanel = None

        super().__init__(master)
        self.master = master
        self.master.title("Game Theory Solver")
        self.pack(fill=tk.BOTH,expand=1)
        self.logoHolder=tk.PanedWindow(self,orient=tk.VERTICAL,bg='#ffffff')
        self.logoHolder.pack(side=tk.RIGHT,expand=1)
        self.logo = tk.PhotoImage(file="nash_GUI/logo.png")
        self.w1 = tk.Label(self.logoHolder, image=self.logo,bg='#ffffff')
        self.logoHolder.add(self.w1)
        self.w1.grid(padx=(10,10),pady=(10,10))
        self.create_welcome_panel()

    def create_welcome_panel(self):
        self.welcome = tk.PanedWindow(self, orient=tk.VERTICAL,bg='#ffffff')
        lb = tk.Label(self.welcome, text="Welcome to game theory solver!!", font=("Helvetica", 36),fg='#421190',bg='#ffffff')
        lb1 = tk.Label(self.welcome, text="Choose your option:", font=("Helvetica", 26),fg='#9d9caa',bg='#ffffff')
        lb.grid(pady=(20,20))
        lb1.grid(pady=(20,20))
        btn_twg = tk.Button(self.welcome,text="Two players Game",font=("Helvetica", 16),fg='#421190',bg='#74da45',command=self.twoplayers)
        btn_twg.grid(pady=(10,10))
        btn_thg = tk.Button(self.welcome,text="Three players Game",font=("Helvetica", 16),fg='#421190',bg='#74da45')
        btn_thg.grid(pady=(10,10))
        btn_thg = tk.Button(self.welcome, text="Quit", font=("Helvetica", 16), fg='white', bg='tomato',command=self.master.destroy)
        btn_thg.grid(pady=(10, 10))
        self.welcome.pack(side=tk.LEFT, expand=1)

    def twoplayers(self):
        self.clean()
        self.TwoPlayersPanel = tk.PanedWindow(self, orient=tk.VERTICAL, bg='#ffffff')
        self.TwoPlayersPanel.pack(side=tk.LEFT, expand=1)
        lb = tk.Label(self.TwoPlayersPanel, text="Two Players Game", font=("Helvetica", 36), fg='#421190',bg='#ffffff')
        lb1 = tk.Label(self.TwoPlayersPanel, text="Please enter how many stratigies for each player:", font=("Helvetica", 26), fg='#9d9caa', bg='#ffffff')
        lb.grid(row=0,columnspan=2,pady=(20, 20))
        lb1.grid(row=1,columnspan=2,pady=(20, 20))
        lb2 = tk.Label(self.TwoPlayersPanel, text="First player  :", font=("Helvetica", 16), fg='#421190', bg='#ffffff')
        tm1=tk.Entry(self.TwoPlayersPanel,  font=("Helvetica", 16), fg='#421190', bg='#ffffff')
        tm1.grid(column=1,row=2,pady=(20, 20))
        tm2=tk.Entry(self.TwoPlayersPanel, font=("Helvetica", 16), fg='#421190', bg='#ffffff')
        tm2.grid(column=1,row=3,pady=(20, 20))
        self.twp_stratigies_count_entry=[]
        self.twp_stratigies_count_entry.append(tm1)
        self.twp_stratigies_count_entry.append(tm2)
        print(self.twp_stratigies_count_entry[0].get())
        lb2 = tk.Label(self.TwoPlayersPanel, text="First player  :", font=("Helvetica", 16), fg='#74da45', bg='#ffffff')
        lb3 = tk.Label(self.TwoPlayersPanel, text="Second player :", font=("Helvetica", 16), fg='#74da45', bg='#ffffff')
        lb2.grid(column=0,row=2,pady=(20, 20))
        lb3.grid(column=0,row=3,pady=(20, 20))
        submit = tk.Button(self.TwoPlayersPanel, text="Submit", font=("Helvetica", 16), fg='#ffffff', bg='#74da45',command=self.twoplayers_labels)
        back = tk.Button(self.TwoPlayersPanel, text="Back", font=("Helvetica", 16), fg='#ffffff', bg='tomato',command=self.twoplayers_back)
        submit.grid(row=4,columnspan=2,pady=(10, 10))
        back.grid(row=5,columnspan=2,pady=(10, 10))

    def twoplayers_back(self):
        self.clean()
        self.create_welcome_panel()

    def twoplayers_labels(self):
        check = True
        print("Entrires edfs,nkjes ###",self.twp_stratigies_count_entry)
        for i in range(len(self.twp_stratigies_count_entry)):
            print(len(self.twp_stratigies_count_entry[i].get()))
            if str.strip(self.twp_stratigies_count_entry[i].get())=="":
                check = False
                messagebox.showinfo("Error in the input","Please make sure you input the informations right!!")
                break
            else:
                try:
                    float(self.twp_stratigies_count_entry[i].get())
                except:
                    check = False
                    messagebox.showinfo("Error in the input", "Please make sure you input the informations right!!")
                    break
            if check:
                self.twp_stratigies_count = [int(i.get()) for i in self.twp_stratigies_count_entry]
                self.clean()
                self.TwoPlayersLabelsPanel = tk.PanedWindow(self, orient=tk.VERTICAL, bg='#ffffff')
                self.TwoPlayersLabelsPanel.pack(side=tk.LEFT, expand=1)
                lb = tk.Label(self.TwoPlayersLabelsPanel, text="Two Players Game", font=("Helvetica", 36), fg='#421190',bg='#ffffff')
                lb1 = tk.Label(self.TwoPlayersLabelsPanel, text="Please enter labels for the stratigies of each player:",font=("Helvetica", 26), fg='#9d9caa', bg='#ffffff')
                lb.grid(row=0, columnspan=2, pady=(20, 20))
                lb1.grid(row=1, columnspan=2, pady=(20, 20))
                lb2 = tk.Label(self.TwoPlayersLabelsPanel, text="First player  :", font=("Helvetica", 16), fg='#74da45',bg='#ffffff')
                lb3 = tk.Label(self.TwoPlayersLabelsPanel, text="Second player :", font=("Helvetica", 16), fg='#74da45',bg='#ffffff')
                lb2.grid(column=0, row=2, pady=(20, 20))
                lb3.grid(column=1, row=2, pady=(20, 20))
                self.twp_stratigies_labels_entry=[]
                temp = []
                for i in range(int(self.twp_stratigies_count[0])):
                    temp.append(tk.Entry(self.TwoPlayersLabelsPanel, width=20, font=("Helvetica", 16), fg='#421190', bg='#ffffff'))
                    temp[-1].grid(column=0,row=3+i,pady=(5, 5))
                self.twp_stratigies_labels_entry.append(temp)
                temp = []
                for i in range(int(self.twp_stratigies_count[1])):
                    temp.append(tk.Entry(self.TwoPlayersLabelsPanel,width=20, font=("Helvetica", 16), fg='#421190', bg='#ffffff'))
                    temp[-1].grid(column=1, row=3 + i, pady=(5, 5))
                self.twp_stratigies_labels_entry.append(temp)

                submit = tk.Button(self.TwoPlayersLabelsPanel, text="Submit", font=("Helvetica", 16), fg='#ffffff',bg='#74da45', command=self.twoplayers_utility_matrix)
                back = tk.Button(self.TwoPlayersLabelsPanel, text="Back", font=("Helvetica", 16), fg='#ffffff', bg='tomato',command=self.homepage)
                submit.grid(row=max(self.twp_stratigies_count[1],self.twp_stratigies_count[0])+3, columnspan=2, pady=(10, 10))
                back.grid(row=max(self.twp_stratigies_count[1],self.twp_stratigies_count[0])+4, columnspan=2, pady=(10, 10))
                print(self.twp_stratigies_labels_entry)

    def twoplayers_utility_matrix(self):
        check = True
        for i in self.twp_stratigies_labels_entry:
            for j in i:
                if str.strip(j.get())=="":
                    check = False
                    messagebox.showinfo("Error in the input", "Please make sure you input the informations right!!")
                    break
        if check:
            self.twp_stratigies_labels = [[i.get() for i in j] for j in self.twp_stratigies_labels_entry]
            self.clean()
            self.TwoPlayersUtilityPanel = tk.PanedWindow(self, orient=tk.VERTICAL, bg='#ffffff')
            self.TwoPlayersUtilityPanel.pack(side=tk.LEFT, expand=1)
            lb = tk.Label(self.TwoPlayersUtilityPanel, text="Two Players Game", font=("Helvetica", 36), fg='#421190',bg='#ffffff')
            lb1 = tk.Label(self.TwoPlayersUtilityPanel, text="Please enter labels for the stratigies of each player:",font=("Helvetica", 26), fg='#9d9caa', bg='#ffffff')
            lb.grid(row=0, columnspan=2+2*len(self.twp_stratigies_labels[1]), pady=(20, 20))
            lb1.grid(row=1, columnspan=2+2*len(self.twp_stratigies_labels[1]), pady=(20, 20))
            lb2 = tk.Label(self.TwoPlayersUtilityPanel, text="Second player  :", font=("Helvetica", 16), fg='#74da45',bg='#ffffff')
            lb3 = tk.Label(self.TwoPlayersUtilityPanel, text="First player :", font=("Helvetica", 16), fg='#421190', bg='#ffffff')
            lb2.grid(column=2, row=2,columnspan=2*len(self.twp_stratigies_labels[1]),pady=(10, 10))
            lb3.grid(column=0, row=4,rowspan=len(self.twp_stratigies_labels[0]), pady=(10, 10))
            for i in range(len(self.twp_stratigies_labels[1])):
                tk.Label(self.TwoPlayersUtilityPanel, text=self.twp_stratigies_labels[1][i],borderwidth=2,relief="groove", font=("Helvetica", 16), fg='#421190',bg='#74da45').grid(column=2*(i+1), row=3, columnspan=2 , pady=(10, 10),sticky=tk.N+tk.S+tk.E+tk.W)
            self.twp_utility_matrix_entry = []
            for i in range(len(self.twp_stratigies_labels[0])):
                tk.Label(self.TwoPlayersUtilityPanel, text=self.twp_stratigies_labels[0][i],borderwidth=2,relief="groove", font=("Helvetica", 16),fg='#74da45', bg='#421190').grid(column=1, row=4+i, pady=(2, 2),sticky=tk.N+tk.S+tk.E+tk.W)
                temp1=[]
                k=0
                for j in range(len(self.twp_stratigies_labels[1])):
                    temp2=[]
                    temp2.append(tk.Entry(self.TwoPlayersUtilityPanel, width=10, font=("Helvetica", 16), fg='#421190',bg='#ffffff'))
                    temp2[-1].grid(column=2+k, row=4 + i, pady=(2, 2))
                    k+=1
                    temp2.append(tk.Entry(self.TwoPlayersUtilityPanel, width=10, font=("Helvetica", 16), fg='#421190',bg='#ffffff'))
                    temp2[-1].grid(column=2+k, row=4 + i, pady=(2, 2))
                    k += 1
                    temp1.append(temp2)
                self.twp_utility_matrix_entry.append(temp1)
            print(self.twp_utility_matrix_entry)

            submit = tk.Button(self.TwoPlayersUtilityPanel, text="Submit", font=("Helvetica", 16), fg='#ffffff',bg='#74da45', command=self.twoplayers_results)
            back = tk.Button(self.TwoPlayersUtilityPanel, text="Back", font=("Helvetica", 16), fg='#ffffff', bg='tomato',command=self.homepage)
            submit.grid(row=max(self.twp_stratigies_count[1], self.twp_stratigies_count[0]) + 4, columnspan=21,pady=(10, 10))
            back.grid(row=max(self.twp_stratigies_count[1], self.twp_stratigies_count[0]) + 5, columnspan=21,pady=(10, 10))

    def check_twp_utility_matrix(self):
        check = False
        for i in range(len(self.twp_utility_matrix_entry)):
            for j in range(len(self.twp_utility_matrix_entry[i])):
                for k in range(len(self.twp_utility_matrix_entry[i][j])):
                    if str.strip(self.twp_utility_matrix_entry[i][j][k].get()) == "":
                        check = False
                        messagebox.showinfo("Error in the input", "Please make sure you input the informations right!!")
                        return False
                    else:
                        try:
                            float(self.twp_utility_matrix_entry[i][j][k].get())
                        except:
                            check = False
                            messagebox.showinfo("Error in the input",
                                                "Please make sure you input the informations right!!")
                            return False
    def twoplayers_results(self):
        self.check_twp_utility_matrix()

    def homepage(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def clean(self):
        if self.welcome!=None:
            self.welcome.destroy()
        if self.TwoPlayersPanel!=None:
            self.TwoPlayersPanel.destroy()
        if self.TwoPlayersLabelsPanel!=None:
            self.TwoPlayersLabelsPanel.destroy()
        if self.TwoPlayersUtilityPanel!=None:
            self.TwoPlayersUtilityPanel.destroy()
        # self.create_widgets()

root = tk.Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

root.geometry("%dx%d+0+0" % (w, h))
app = Application(master=root)
app['bg']='#ffffff'
app.mainloop()






