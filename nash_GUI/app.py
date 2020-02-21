#!nasheq/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import traceback
import tkinter as tk
import tkinter.ttk
from tkinter import messagebox
import os, sys
from nash import Nash
import matplotlib.image as mpimg
class Application(tk.Frame):
    def __init__(self, master=None):
        ## initialize
        self.welcome = None
        self.TwoPlayersPanel = None
        self.TwoPlayersLabelsPanel = None
        self.TwoPlayersUtilityPanel = None
        self.ThreePlayersPanel  = None
        self.ThreePlayersUtilityMatrix  = None

        super().__init__(master)
        self.master = master
        self.master.title("Game Theory Solver")
        self.pack(fill=tk.BOTH,expand=1)
        self.logoHolder=tk.PanedWindow(self,orient=tk.VERTICAL,bg='#ffffff')
        self.logoHolder.pack(side=tk.RIGHT,expand=1)
        self.logo = tk.PhotoImage(file="logo.png")
        self.w1 = tk.Label(self.logoHolder, image=self.logo,bg='#ffffff')
        self.w1.grid(padx=(10,10),pady=(10,10))
        self.logoHolder.add(self.w1)
        self.create_welcome_panel()

    def create_welcome_panel(self):
        self.welcome = tk.PanedWindow(self, orient=tk.VERTICAL,bg='#ffffff')
        lb = tk.Label(self.welcome, text="Welcome to game theory solver!!", font=("Helvetica", 36),fg='#421190',bg='#ffffff')
        lb1 = tk.Label(self.welcome, text="Choose your option:", font=("Helvetica", 26),fg='#9d9caa',bg='#ffffff')
        lb.grid(pady=(20,20))
        lb1.grid(pady=(20,20))
        btn_twg = tk.Button(self.welcome,text="Two players Game",font=("Helvetica", 16),fg='#421190',bg='#74da45',command=self.twoplayers)
        btn_twg.grid(pady=(10,10))
        btn_thg = tk.Button(self.welcome,text="Three players Game",font=("Helvetica", 16),fg='#421190',bg='#74da45',command=self.threeplayers)
        btn_thg.grid(pady=(10,10))
        btn_thg = tk.Button(self.welcome, text="Quit", font=("Helvetica", 16), fg='white', bg='tomato',command=self.master.destroy)
        btn_thg.grid(pady=(10, 10))
        self.welcome.pack(side=tk.LEFT, expand=1)
    def threeplayers(self):
        self.clean()
        self.ThreePlayersPanel = tk.PanedWindow(self, orient=tk.VERTICAL, bg='#ffffff')
        self.ThreePlayersPanel.pack(side=tk.LEFT, expand=1)
        lb = tk.Label(self.ThreePlayersPanel, text="Three Players Game", font=("Helvetica", 36), fg='#421190', bg='#ffffff')
        lb1 = tk.Label(self.ThreePlayersPanel, text="Please enter the stratigies for each player:",font=("Helvetica", 26), fg='#9d9caa', bg='#ffffff')
        lb.grid(row=0, columnspan=3, pady=(20, 20))
        lb1.grid(row=1, columnspan=3, pady=(20, 20))
        lb2 = tk.Label(self.ThreePlayersPanel, text="First player  :",borderwidth=2,relief="groove", font=("Helvetica", 14), fg='#fbfbfb',bg='#421190')
        lb3 = tk.Label(self.ThreePlayersPanel, text="Second player :", borderwidth=2,relief="groove",font=("Helvetica", 14), fg='#421190',bg='#74da45')
        lb4 = tk.Label(self.ThreePlayersPanel, text="Third player :", borderwidth=2,relief="groove",font=("Helvetica", 14), fg='black',bg='#9d9caa')
        lb2.grid(column=0, row=2, ipady=3,ipadx=3,sticky=tk.N+tk.S+tk.E+tk.W, pady=(5, 5))
        lb3.grid(column=1, row=2, ipady=3,ipadx=3,sticky=tk.N+tk.S+tk.E+tk.W, pady=(5, 5))
        lb4.grid(column=2, row=2,ipady=3,ipadx=3,sticky=tk.N+tk.S+tk.E+tk.W, pady=(5, 5))
        self.thp_strategies_labels_entry = []
        for i in range(3):
            temp=[]
            for j in range(2):
                temp.append(tk.Entry(self.ThreePlayersPanel, width=12, font=("Helvetica", 15), fg='#421190', bg='#ffffff'))
                temp[-1].grid(column=i,row=4+j,pady=(5, 5))
            self.thp_strategies_labels_entry.append(temp)
        btn_thg = tk.Button(self.ThreePlayersPanel, text="Submit", font=("Helvetica", 16), fg='#421190', bg='#74da45',command=self.threeplayers_utility_matrix)
        btn_thg.grid(pady=(10, 10),columnspan=3)
        btn_thg = tk.Button(self.ThreePlayersPanel, text="Quit", font=("Helvetica", 16), fg='white', bg='tomato',command=self.master.destroy)
        btn_thg.grid(pady=(10, 10),columnspan=3)
    def check_threeplayers_utility_matrix(self):
        for i in self.thp_strategies_labels_entry:
            for j in i:
                if str.strip(j.get())=="":
                    messagebox.showinfo("Error","Please make sure you enter the inputs right!!")
                    return False
        return True
    def threeplayers_utility_matrix(self):
        check = self.check_threeplayers_utility_matrix()
        if check:
            self.thp_strategies_labels = [[j.get() for j in i] for i in self.thp_strategies_labels_entry]
            self.clean()
            self.ThreePlayersUtilityMatrix = tk.PanedWindow(self, orient=tk.VERTICAL, bg='#ffffff')
            self.ThreePlayersUtilityMatrix.pack(side=tk.LEFT, expand=1)
            lb = tk.Label(self.ThreePlayersUtilityMatrix, text="Three Players Game", font=("Helvetica", 36), fg='#421190',bg='#ffffff')
            lb1 = tk.Label(self.ThreePlayersUtilityMatrix, text="Please fill the utility matrix:", font=("Helvetica", 26), fg='#9d9caa', bg='#ffffff')
            lb.grid(row=0, columnspan=8, pady=(10, 10))
            lb1.grid(row=1, columnspan=8, pady=(10, 10))
            tk.Label(self.ThreePlayersUtilityMatrix,borderwidth=2,relief="sunken",  text="Third Player plays "+self.thp_strategies_labels[2][0], font=("Helvetica", 14),fg='white', bg='#7c7c7c').grid(row=3,column=0,sticky=tk.N+tk.S+tk.E+tk.W,columnspan=8,ipady=5)
            tk.Label(self.ThreePlayersUtilityMatrix,borderwidth=2,relief="groove", text="Second player", font=("Helvetica", 14),fg='#421190', bg='#74da45').grid(row=4,column=2,columnspan=6,sticky=tk.N+tk.S+tk.E+tk.W,ipady=3)
            tk.Label(self.ThreePlayersUtilityMatrix,borderwidth=2,relief="groove", text="First player", font=("Helvetica", 14),fg='#74da45', bg='#421190').grid(row=6,column=0,rowspan=2,sticky=tk.N+tk.S+tk.E+tk.W,ipady=3,ipadx=5)
            tk.Label(self.ThreePlayersUtilityMatrix,borderwidth=2,relief="groove",  text=self.thp_strategies_labels[1][0], font=("Helvetica", 14),fg='black', bg='#DEE2EC').grid(row=5,column=2,columnspan=3,sticky=tk.N+tk.S+tk.E+tk.W,ipady=3)
            tk.Label(self.ThreePlayersUtilityMatrix,borderwidth=2,relief="groove",  text=self.thp_strategies_labels[1][1], font=("Helvetica", 14),fg='black', bg='#DEE2EC').grid(row=5,column=5,columnspan=3,sticky=tk.N+tk.S+tk.E+tk.W,ipady=3)
            tk.Label(self.ThreePlayersUtilityMatrix,borderwidth=2,relief="groove",  text=self.thp_strategies_labels[0][0], font=("Helvetica", 14),fg='black', bg='#DEE2EC').grid(row=6, column=1,sticky=tk.N+tk.S+tk.E+tk.W,ipady=3,ipadx=5)
            tk.Label(self.ThreePlayersUtilityMatrix,borderwidth=2,relief="groove",  text=self.thp_strategies_labels[0][1], font=("Helvetica", 14),fg='black', bg='#DEE2EC').grid(row=7, column=1,sticky=tk.N+tk.S+tk.E+tk.W,ipady=3,ipadx=5)
            self.thp_utility_matrix_entry = []
            temp=[]
            for i in range(2):
                temp1=[]
                k=0
                for j in range(2):
                    temp2=[]
                    temp2.append(tk.Entry(self.ThreePlayersUtilityMatrix, width=8, font=("Helvetica", 10), fg='#421190',bg='#ffffff'))
                    temp2[-1].grid(column=2+k, row=6 + i, pady=(2, 2))
                    k+=1
                    temp2.append(tk.Entry(self.ThreePlayersUtilityMatrix, width=8, font=("Helvetica", 10), fg='#421190',bg='#ffffff'))
                    temp2[-1].grid(column=2+k, row=6 + i, pady=(2, 2))
                    k += 1
                    temp2.append(tk.Entry(self.ThreePlayersUtilityMatrix, width=8, font=("Helvetica", 10), fg='#421190',bg='#ffffff'))
                    temp2[-1].grid(column=2 + k, row=6 + i, pady=(2, 2))
                    k += 1
                    temp1.append(temp2)
                temp.append(temp1)
            self.thp_utility_matrix_entry.append(temp)
            tk.Label(self.ThreePlayersUtilityMatrix, borderwidth=2, relief="sunken",text="Third Player plays " + self.thp_strategies_labels[2][1], font=("Helvetica", 14), fg='white',bg='#7c7c7c').grid(row=9, column=0, sticky=tk.N + tk.S + tk.E + tk.W, columnspan=8, ipady=5,pady=(20,0))
            tk.Label(self.ThreePlayersUtilityMatrix, borderwidth=2, relief="groove", text="Second player",font=("Helvetica", 14), fg='#421190', bg='#74da45').grid(row=10, column=2, columnspan=6,sticky=tk.N + tk.S + tk.E + tk.W, ipady=3)
            tk.Label(self.ThreePlayersUtilityMatrix, borderwidth=2, relief="groove", text="First player",font=("Helvetica", 14), fg='#74da45', bg='#421190').grid(row=12, column=0, rowspan=2,sticky=tk.N + tk.S + tk.E + tk.W, ipady=3,ipadx=5)
            tk.Label(self.ThreePlayersUtilityMatrix, borderwidth=2, relief="groove",text=self.thp_strategies_labels[1][0], font=("Helvetica", 14), fg='black', bg='#DEE2EC').grid(row=11, column=2, columnspan=3, sticky=tk.N + tk.S + tk.E + tk.W, ipady=3)
            tk.Label(self.ThreePlayersUtilityMatrix, borderwidth=2, relief="groove",text=self.thp_strategies_labels[1][1], font=("Helvetica", 14), fg='black', bg='#DEE2EC').grid(row=11, column=5, columnspan=3, sticky=tk.N + tk.S + tk.E + tk.W, ipady=3)
            tk.Label(self.ThreePlayersUtilityMatrix, borderwidth=2, relief="groove",text=self.thp_strategies_labels[0][0], font=("Helvetica", 14), fg='black', bg='#DEE2EC').grid(row=12, column=1, sticky=tk.N + tk.S + tk.E + tk.W, ipady=3, ipadx=5)
            tk.Label(self.ThreePlayersUtilityMatrix, borderwidth=2, relief="groove",text=self.thp_strategies_labels[0][1], font=("Helvetica", 14), fg='black', bg='#DEE2EC').grid(row=13, column=1, sticky=tk.N + tk.S + tk.E + tk.W, ipady=3, ipadx=5)
            temp = []
            for i in range(2):
                temp1 = []
                k = 0
                for j in range(2):
                    temp2 = []
                    temp2.append(tk.Entry(self.ThreePlayersUtilityMatrix, width=8, font=("Helvetica", 10), fg='#421190',bg='#ffffff'))
                    temp2[-1].grid(column=2 + k, row=12 + i, pady=(2, 2))
                    k += 1
                    temp2.append(tk.Entry(self.ThreePlayersUtilityMatrix, width=8, font=("Helvetica", 10), fg='#421190',bg='#ffffff'))
                    temp2[-1].grid(column=2 + k, row=12 + i, pady=(2, 2))
                    k += 1
                    temp2.append(tk.Entry(self.ThreePlayersUtilityMatrix, width=8, font=("Helvetica", 10), fg='#421190',bg='#ffffff'))
                    temp2[-1].grid(column=2 + k, row=12 + i, pady=(2, 2))
                    k += 1
                    temp1.append(temp2)
                temp.append(temp1)
            self.thp_utility_matrix_entry.append(temp)
            btn_thg = tk.Button(self.ThreePlayersUtilityMatrix, text="Submit", font=("Helvetica", 16), fg='#421190',bg='#74da45', command=self.threeplayers_results)
            btn_thg.grid(pady=(10, 10), columnspan=8)
            btn_thg = tk.Button(self.ThreePlayersUtilityMatrix, text="Quit", font=("Helvetica", 16), fg='white', bg='tomato',command=self.master.destroy)
            btn_thg.grid(pady=(10, 10), columnspan=8)

    def check_threeplayers_results(self):
        for i in self.thp_utility_matrix_entry:
            for j in i:
                for p in j:
                    for k in p:
                        if str.strip(k.get())=="":
                            messagebox.showinfo("Error", "Please make sure you enter the inputs right!!")
                            return False
                        else:
                            try:
                                float(k.get())
                            except:
                                messagebox.showinfo("Error", "Please make sure you enter the inputs right!!")
                                return False
        return True

    def threeplayers_results(self):
        check = self.check_threeplayers_results()
        if check:
            self.thp_utility_matrix=[]
            for i in self.thp_utility_matrix_entry:
                temp=[]
                for j in i:
                    temp1=[]
                    for k in j:
                        temp1.append((float(k[0].get()),float(k[1].get()),float(k[2].get())))
                    temp.append(temp1)
                self.thp_utility_matrix.append(temp)
            temp =[]
            for i in range(2):
                for j in range(2):
                    temp.append(" ".join(",".join(map(str,self.thp_utility_matrix[i][j][k])) for k in range(2) ))
                temp.append(" ")
            temp.pop()

            self.nash=Nash(temp)
            self.clean()
            self.ThPlayersResultsPanel = tk.PanedWindow(self, orient=tk.VERTICAL, bg='#ffffff')
            self.ThPlayersResultsPanel.pack(side=tk.LEFT, expand=1)
            lb = tk.Label(self.ThPlayersResultsPanel, text="Two Players Game", font=("Helvetica", 36), fg='#421190',
                          bg='#ffffff')
            lb1 = tk.Label(self.ThPlayersResultsPanel, text="Pure strategies Nash Equilibriums", font=("Helvetica", 22),
                           fg='#74da45', bg='#ffffff')
            lb.grid(row=0, columnspan=2, pady=(10, 10))
            lb1.grid(row=1, columnspan=2, pady=(10, 10))
            equilibriums = self.nash.pure_strategy_solutions()
            k = 0
            if len(equilibriums) == 0:
                tk.Label(self.ThPlayersResultsPanel,
                         text="No pure strategy nash equilibriums", font=("Helvetica", 16), fg='#9d9caa',
                         bg='#ffffff').grid(row=2 + i, pady=(10, 10))
                k += 1
            print(self.thp_strategies_labels)
            x = "Pure Nash equilibrium strategy {} is ({}, {}, {}) with the utilities {}"
            print(temp)
            for i, s in enumerate(equilibriums):
                tk.Label(self.ThPlayersResultsPanel,text=x.format(i + 1, self.thp_strategies_labels[0][s[0]],
                                                                         self.thp_strategies_labels[1][s[1]],
                                                                         self.thp_strategies_labels[2][s[2]],
                                                                         self.nash.utility_tableau[s[0]][s[1]][s[2]]),
                                                                          font=("Helvetica", 16), fg='#9d9caa',bg='#ffffff').grid(row=2 + i, pady=(10, 10))
                k += 1
            tk.Label(self.ThPlayersResultsPanel, text="Mixed strategies Nash Equilibriums", font=("Helvetica", 22),fg='#74da45', bg='#ffffff').grid(row=k + 4, pady=(10, 10))
            self.equilibriums = self.nash.mixed_strategy_solutions()
            if self.equilibriums != None:
                o=0
                for i in range(1,4):
                    tk.Label(
                                self.ThPlayersResultsPanel
                                , text="Player %d plays %s %4.1f%% of the time" % (i,self.thp_strategies_labels[i-1][0],self.equilibriums[i-1] * 100)
                                , font=("Helvetica", 16)
                                , fg='#9d9caa', bg='#ffffff'
                            ).grid(row=k + 5 + o, pady=(10, 10))
                    
                    o+=1
                    tk.Label(
                                self.ThPlayersResultsPanel
                                , text="Player %d plays %s %4.1f%% of the time" % (i,self.thp_strategies_labels[i-1][1],100 - self.equilibriums[1] * 100)
                                , font=("Helvetica", 16)
                                , fg='#9d9caa', bg='#ffffff'
                            ).grid(row=k + 5 + o, pady=(10, 10))
                    o+=1    
                    # tk.Label(self.ThPlayersResultsPanel,text="Player 1 plays 0 %4.1f%% of the time" % (self.equilibriums[0] * 100), font=("Helvetica", 16),fg='#9d9caa', bg='#ffffff').grid(row=k + 5, pady=(10, 10))
                    # tk.Label(self.ThPlayersResultsPanel,text="Player 1 plays 1 %4.1f%% of the time\n" % (100 - self.equilibriums[0] * 100),font=("Helvetica", 16), fg='#9d9caa', bg='#ffffff').grid(row=k + 6, pady=(10, 10))
                    # tk.Label(self.ThPlayersResultsPanel,text="Player 2 plays 0 %4.1f%% of the time" % (self.equilibriums[1] * 100), font=("Helvetica", 16),fg='#9d9caa', bg='#ffffff').grid(row=k + 7, pady=(10, 10))
                    # tk.Label(self.ThPlayersResultsPanel,text="Player 2 plays 1 %4.1f%% of the time\n" % (100 - self.equilibriums[1] * 100),font=("Helvetica", 16), fg='#9d9caa', bg='#ffffff').grid(row=k + 8, pady=(10, 10))
                    # tk.Label(self.ThPlayersResultsPanel,text="Player 3 plays 0 %4.1f%% of the time\n" % (self.equilibriums[2] * 100),font=("Helvetica", 16), fg='#9d9caa', bg='#ffffff').grid(row=k + 9, pady=(10, 10))
                    # tk.Label(self.ThPlayersResultsPanel,text="Player 3 plays 1 %4.1f%% of the time\n" % (100 - self.equilibriums[2] * 100),font=("Helvetica", 16), fg='#9d9caa', bg='#ffffff').grid(row=k + 10, pady=(10, 10))
            else:
                tk.Label(self.ThPlayersResultsPanel,text="No other Nash equilibrium than the ones found in the pure strategy", font=("Helvetica", 16),fg='#9d9caa', bg='#ffffff').grid(row=k + 5, pady=(10, 10))

            self.logoHolder.destroy()
            # self.nash.plot3PlayersMixed_GUI(*equilibriums)
            self.thp_plotHolder = tk.PanedWindow(self, orient=tk.VERTICAL, bg='#ffffff')
            self.thp_plotHolder.pack(side=tk.RIGHT, expand=1)
            self.thp_plotHolder.add(tk.Button(self.thp_plotHolder, text="First Player Plot", font=("Helvetica", 16), fg='#ffffff', bg='tomato',command=self.command_fp))
            self.thp_plotHolder.add(tk.Button(self.thp_plotHolder, text="Second Player Plot", font=("Helvetica", 16), fg='#ffffff', bg='tomato',command=self.command_sp))
            self.thp_plotHolder.add(tk.Button(self.thp_plotHolder, text="Third Player Plot", font=("Helvetica", 16), fg='#ffffff', bg='tomato',command=self.command_tp))
            self.thp_plotHolder.add(tk.Button(self.thp_plotHolder, text="Overall Plot", font=("Helvetica", 16), fg='#ffffff', bg='tomato',command=self.command_ap))
            self.thp_plotHolder.add(tk.Button(self.thp_plotHolder, text="Mixed Nash equilibrium plot", font=("Helvetica", 16), fg='#ffffff', bg='tomato',command=self.command_nash))
            back = tk.Button(self.ThPlayersResultsPanel, text="Back", font=("Helvetica", 16), fg='#ffffff', bg='tomato',command=self.homepage)

    def command_fp(self):
        self.nash.plot3PlayersMixed_GUI(*self.equilibriums,0)

    def command_sp(self):
        self.nash.plot3PlayersMixed_GUI(*self.equilibriums,1)

    def command_tp(self):
        self.nash.plot3PlayersMixed_GUI(*self.equilibriums,2)

    def command_ap(self):
        self.nash.plot3PlayersMixed_GUI(*self.equilibriums,3)

    def command_nash(self):
        self.nash.plot3PlayersMixed_GUI(*self.equilibriums,4)


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
                    temp2.append(tk.Entry(self.TwoPlayersUtilityPanel, width=8, font=("Helvetica", 10), fg='#421190',bg='#ffffff'))
                    temp2[-1].grid(column=2+k, row=4 + i, pady=(2, 2))
                    k+=1
                    temp2.append(tk.Entry(self.TwoPlayersUtilityPanel, width=8, font=("Helvetica", 10), fg='#421190',bg='#ffffff'))
                    temp2[-1].grid(column=2+k, row=4 + i, pady=(2, 2))
                    k += 1
                    temp1.append(temp2)
                self.twp_utility_matrix_entry.append(temp1)

            submit = tk.Button(self.TwoPlayersUtilityPanel, text="Submit", font=("Helvetica", 16), fg='#ffffff',bg='#74da45', command=self.twoplayers_results)
            back = tk.Button(self.TwoPlayersUtilityPanel, text="Back", font=("Helvetica", 16), fg='#ffffff', bg='tomato',command=self.homepage)
            submit.grid(row=max(self.twp_stratigies_count[1], self.twp_stratigies_count[0]) + 4, columnspan=21,pady=(10, 10))
            back.grid(row=max(self.twp_stratigies_count[1], self.twp_stratigies_count[0]) + 5, columnspan=21,pady=(10, 10))

    def check_twp_utility_matrix(self):
        for i in range(len(self.twp_utility_matrix_entry)):
            for j in range(len(self.twp_utility_matrix_entry[i])):
                for k in range(len(self.twp_utility_matrix_entry[i][j])):
                    if str.strip(self.twp_utility_matrix_entry[i][j][k].get()) == "":
                        messagebox.showinfo("Error in the input", "Please make sure you input the informations right!!")
                        return False
                    else:
                        try:
                            float(self.twp_utility_matrix_entry[i][j][k].get())
                        except:
                            messagebox.showinfo("Error in the input","Please make sure you input the informations right!!")
                            return False
        return True
    def twoplayers_results(self):
        check=self.check_twp_utility_matrix()
        if check:
            self.twp_utility_matrix = []
            for i in range(len(self.twp_utility_matrix_entry)):
                temp=[]
                for j in range(len(self.twp_utility_matrix_entry[i])):
                    temp1=[]
                    temp.append((float(self.twp_utility_matrix_entry[i][j][0].get()),float(self.twp_utility_matrix_entry[i][j][1].get())))
                self.twp_utility_matrix.append(temp)
            temp =[]
            for i in range(self.twp_stratigies_count[0]):
                    temp.append(" ".join(",".join(map(str,self.twp_utility_matrix[i][j])) for j in range(2)))
            print(temp)
            nsh = Nash(temp)
            # print(nsh.pure_strategy_solutions())
            # print(nsh.mixed_strategy_solutions())
            self.clean()
            self.TwoPlayersResultsPanel = tk.PanedWindow(self, orient=tk.VERTICAL, bg='#ffffff')
            self.TwoPlayersResultsPanel.pack(side=tk.LEFT, expand=1)
            lb = tk.Label(self.TwoPlayersResultsPanel, text="Two Players Game", font=("Helvetica", 36), fg='#421190',
                          bg='#ffffff')
            lb1 = tk.Label(self.TwoPlayersResultsPanel, text="Pure strategies Nash Equilibriums",font=("Helvetica", 26), fg='#74da45', bg='#ffffff')
            lb.grid(row=0, columnspan=2, pady=(20, 20))
            lb1.grid(row=1, columnspan=2, pady=(10, 10))
            equilibriums = nsh.pure_strategy_solutions()
            k=0
            if len(equilibriums) == 0:
                tk.Label(self.TwoPlayersResultsPanel,
                         text="No pure strategy nash equilibriums", font=("Helvetica", 16), fg='#9d9caa',
                         bg='#ffffff').grid(row=2 + i, pady=(10, 10))
                k += 1
            x = "Pure Nash equilibrium strategy {} is ({}, {}) with the utilities {}"
            for i, s in enumerate(equilibriums):
                tk.Label(self.TwoPlayersResultsPanel, text=x.format(i+1,self.twp_stratigies_labels[0][s[0]],self.twp_stratigies_labels[1][s[1]],self.twp_utility_matrix[s[0]][s[1]]),font=("Helvetica", 16), fg='#9d9caa', bg='#ffffff').grid(row=2+i, pady=(10, 10))
                k+=1
            if self.twp_stratigies_count[0]==self.twp_stratigies_count[1]==2:
                tk.Label(self.TwoPlayersResultsPanel, text="Mixed strategies Nash Equilibriums", font=("Helvetica", 26),
                         fg='#74da45', bg='#ffffff').grid(row=k + 4, pady=(10, 10))
                equilibriums = nsh.mixed_strategy_solutions()
                tk.Label(self.TwoPlayersResultsPanel,
                         text="Player 1 plays 0 %4.1f%% of the time" % (equilibriums[0] * 100), font=("Helvetica", 16),
                         fg='#9d9caa', bg='#ffffff').grid(row=k + 5, pady=(10, 10))
                tk.Label(self.TwoPlayersResultsPanel,
                         text="Player 1 plays 1 %4.1f%% of the time\n" % (100 - equilibriums[0] * 100),
                         font=("Helvetica", 16), fg='#9d9caa', bg='#ffffff').grid(row=k + 6, pady=(10, 10))
                tk.Label(self.TwoPlayersResultsPanel,
                         text="Player 2 plays 0 %4.1f%% of the time" % (equilibriums[1] * 100), font=("Helvetica", 16),
                         fg='#9d9caa', bg='#ffffff').grid(row=k + 7, pady=(10, 10))
                tk.Label(self.TwoPlayersResultsPanel,
                         text="Player 2 plays 1 %4.1f%% of the time\n" % (100 - equilibriums[1] * 100),
                         font=("Helvetica", 16), fg='#9d9caa', bg='#ffffff').grid(row=k + 8, pady=(10, 10))
            self.logoHolder.destroy()
            nsh.plot2PlayersMixed(*equilibriums)
            self.twp_plotHolder = tk.PanedWindow(self, orient=tk.VERTICAL, bg='#ffffff')
            self.twp_plotHolder.pack(side=tk.RIGHT, expand=1)
            self.twp_plot = tk.PhotoImage(file="./twp_plot.png")
            self.w12 = tk.Label(self.twp_plotHolder, image=self.twp_plot, bg='#ffffff')
            self.w12.grid(padx=(10, 10), pady=(10, 10))
            self.twp_plotHolder.add(self.w2)
            back = tk.Button(self.TwoPlayersResultsPanel, text="Back", font=("Helvetica", 16), fg='#ffffff', bg='tomato',command=self.homepage)
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
        if self.ThreePlayersPanel !=None:
            self.ThreePlayersPanel.destroy()
        if self.ThreePlayersUtilityMatrix !=None:
            self.ThreePlayersUtilityMatrix.destroy()
        # self.create_widgets()

root = tk.Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

root.geometry("%dx%d+0+0" % (w, h))
app = Application(master=root)
app['bg']='#ffffff'
app.mainloop()






