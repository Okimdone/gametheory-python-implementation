import numpy as np
from fractions import Fraction
from gekko import GEKKO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
plt.style.use('ggplot')
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.color'] = 'r'

class Nash:
    def __init__(self, path, number_of_players=None, labels=[0, 1], strategies=[]):
        if type(path) == list:
            n, self.utility_tableau = self.load_grid(path)
            self.number_of_players = n
        else :
            with open(path, "r") as f:
                n, self.utility_tableau     = self.load_grid(f)
                if number_of_players!=None and n != number_of_players:
                    raise Exception(f"The Number of players supplied does not match the file at {path}")

                self.number_of_players  = n
        n=self.number_of_players
        self.p_indexes = list(range(self.number_of_players))
        # Defining the players' labels
        self.labels             = list(range(n))
        if labels[0] != None:
            self.labels[0]      = labels[0]
        if labels[1] != None:
            self.labels[1]      = labels[1]
        if len(labels) == 3 and labels[2]!=None:
            self.labels[2]      = labels[2]
        # Strategies labels : metadata that might prove useful w plotting 
        self.strat_labels       = [   self.generate_labels(len(self.utility_tableau)),
                                    self.generate_labels(len(self.utility_tableau[0])) ]
        if n == 3 :
            self.strat_labels.append( self.generate_labels(len(self.utility_tableau[0][0])) )
        self.strategies         = strategies


    def modified_init(self,f):
        n, self.utility_tableau = self.load_grid(f)
        self.number_of_players = n

        n = self.number_of_players
        self.p_indexes = list(range(self.number_of_players))
        # Defining the players' labels
        self.labels = list(range(n))

        # Strategies labels : metadata that might prove useful w plotting
        self.strat_labels = [self.generate_labels(len(self.utility_tableau)),
                             self.generate_labels(len(self.utility_tableau[0]))]
        if n == 3:
            self.strat_labels.append(self.generate_labels(len(self.utility_tableau[0][0])))

    def load_grid(self, file:__file__):
        grid_1D = []
        depth_1D, depth_3D = 0, 0
        gridIsCube = False
        for line in file:
            if line.rstrip()=='':
                depth_1D = 0
                depth_3D += 1
                continue

            # Read the 2d line from the file
            grid_2D_line = []
            for payouts in line.split(" "):
                grid_2D_line.append(tuple(float(payout) for payout in payouts.split(",")))

            if depth_3D == 0:
                grid_1D.append(grid_2D_line)
            elif depth_3D == 1:
                for i in range(len(grid_2D_line)):
                    grid_1D[depth_1D][i] = [grid_1D[depth_1D][i], grid_2D_line[i]]
                gridIsCube = True
            else: 
                for i in range(len(grid_2D_line)):
                   grid_1D[depth_1D][i].append( grid_2D_line[i] )
            depth_1D += 1
        return (3, grid_1D) if gridIsCube else (2, grid_1D)

    def generate_labels(self, labels_num):
        return list(range(labels_num))

    '''
    This section handles finding pure nash eq
    '''
    def compute_pure_strategies(self):
        equilibriums = self.pure_strategy_solutions()
        if len(equilibriums) == 0:
            print("No pure strategies")
            return
        for i,s in enumerate(equilibriums):
            if self.number_of_players == 2:
                print(f"Pure Nash equilibrium strategy {i+1} is ({s[0]}, {s[1]}) with the utilities {self.utility_tableau[s[0]][s[1]]}.")
            elif self.number_of_players == 3:
                print(f"Pure Nash equilibrium strategy {i+1} is ({s[0]}, {s[1]}, {s[2]}) with the utilities {self.utility_tableau[s[0]][s[1]][s[2]]}.")

    def pure_strategy_solutions(self):
        best_payout_labels = []
        # For two players
        Dim_1 = len(self.utility_tableau)
        Dim_2 = len(self.utility_tableau[0])
        if self.number_of_players == 2:
            best_payouts = set()
            # Looping through the first rows/dim1 fixing them and then finding the positions of the strategies where the 
            # best responses of player 2 to player 1 are located :
            for d_1 in range(Dim_1):
                max_payout = max((self.utility_tableau[d_1][d_2][1] for d_2 in range(Dim_2)))
                for d_2 in range(Dim_2):
                    if self.utility_tableau[d_1][d_2][1] == max_payout:
                        best_payouts.add((d_1, d_2))
            # Looping through the second columns/dim2 fixing them and then finding the positions of the strategies where the 
            # best responses of player 1 to player 2 are located :
            for d_2 in range(Dim_2):
                max_payout = max((self.utility_tableau[d_1][d_2][0] for d_1 in range(Dim_1)))
                for d_1 in range(Dim_1):
                    if self.utility_tableau[d_1][d_2][0] == max_payout:
                        if (d_1, d_2) in best_payouts:
                            best_payout_labels.append((d_1, d_2))
        # For three players
        elif self.number_of_players == 3 :
            best_payouts = set()
            Dim_3 = len(self.utility_tableau[0][0])
            # Fix third and second and find maximum for dim 1
            for d_3 in range(Dim_3):
                for d_2 in range(Dim_2):
                    max_payout = max((self.utility_tableau[d_1][d_2][d_3][0] for d_1 in range(Dim_1)))
                    for d_1 in range(Dim_1):
                        if self.utility_tableau[d_1][d_2][d_3][0] == max_payout:
                            best_payouts.add((d_1, d_2, d_3))

            best_payout_labels_temp = set()
            for d_3 in range(Dim_3):
                for d_1 in range(Dim_1):
                    max_payout = max((self.utility_tableau[d_1][d_2][d_3][1] for d_2 in range(Dim_2)))
                    for d_2 in range(Dim_2):
                        if self.utility_tableau[d_1][d_2][d_3][1] == max_payout:
                            best_payout_labels_temp.add((d_1, d_2, d_3))
            best_payouts = best_payouts & best_payout_labels_temp

            for d_1 in range(Dim_1):
                for d_2 in range(Dim_2):
                    max_payout = max([self.utility_tableau[d_1][d_2][d_3][2] for d_3 in range(Dim_3)])
                    for d_3 in range(Dim_3):
                        if self.utility_tableau[d_1][d_2][d_3][2] == max_payout:
                            if (d_1, d_2, d_3) in best_payouts:
                                best_payout_labels.append((d_1, d_2, d_3))

        return best_payout_labels


    '''
    This section handles finding mixed nash eq
    '''
    def compute_mixed_strategies(self, plot=False):
        equilibriums = self.mixed_strategy_solutions()

        print("\nPlayer 1 plays 0 %4.1f%% of the time" % (equilibriums[0]*100))
        print("Player 1 plays 1 %4.1f%% of the time\n" % (100-equilibriums[0]*100))

        print("Player 2 plays 0 %4.1f%% of the time" % (equilibriums[1]*100))
        print("Player 2 plays 1 %4.1f%% of the time\n" % (100-equilibriums[1]*100))

        if self.number_of_players == 3 :
            print("Player 3 plays 0 %4.1f%% of the time" % (equilibriums[2]*100))
            print("Player 3 plays 1 %4.1f%% of the time\n" % (100-equilibriums[2]*100))
        
        #Check if plotting is requested and plote
        if plot : 
            if self.number_of_players == 2 :
                self.plot2PlayersMixed(*equilibriums)
            elif self.number_of_players == 3 :
                self.plot3PlayersMixed(p=equilibriums[0], q=equilibriums[1], r=equilibriums[2])

    def mixed_strategy_solutions(self):
        def twoPlayersEUtility( playerId ):
            a = b = None
            if playerId == 0:
                a = ( self.utility_tableau[0][0][0]
                    - self.utility_tableau[0][1][0]
                    - self.utility_tableau[1][0][0]
                    + self.utility_tableau[1][1][0])
                
                b = ( self.utility_tableau[1][1][0]
                    - self.utility_tableau[0][1][0])
            elif playerId == 1:
                a = ( self.utility_tableau[0][0][1]
                    - self.utility_tableau[1][0][1]
                    - self.utility_tableau[0][1][1]
                    + self.utility_tableau[1][1][1]
                    )
                b = ( self.utility_tableau[1][1][1]
                    - self.utility_tableau[1][0][1]
                    )

            if a!=None!=b :
                # x = Fraction(b, a)
                if a==0:
                    return None
                return b/a
            else:
                return None

        def threePlayersEUtility():
            eq = GEKKO(remote=False)
            p, q, r = eq.Var(), eq.Var(), eq.Var()
            ## U1(A) == U1(B)
            eq.Equation(q*p*Fraction(self.utility_tableau[0][0][0][0])+p*(1-q)*self.utility_tableau[0][1][0][0]+(1-p)*q*self.utility_tableau[0][0][1][0]+(1-p)*(1-q)*self.utility_tableau[0][1][1][0]==q*p*self.utility_tableau[1][0][0][0]+p*(1-q)*self.utility_tableau[1][1][0][0]+(1-p)*q*self.utility_tableau[1][0][1][0]+(1-p)*(1-q)*self.utility_tableau[1][1][1][0])
            ## U2(A) == U2(B)
            eq.Equation(r*p*self.utility_tableau[0][0][0][1]+(1-r)*p*self.utility_tableau[1][0][0][1]+r*(1-p)*self.utility_tableau[0][0][1][1]+(1-r)*(1-p)*self.utility_tableau[1][0][1][1]==r*p*self.utility_tableau[0][1][0][1]+(1-r)*p*self.utility_tableau[1][1][0][1]+r*(1-p)*self.utility_tableau[0][1][1][1]+(1-r)*(1-p)*self.utility_tableau[1][1][1][1])

            ## U3(A) == U3(B)
            eq.Equation(r*q*self.utility_tableau[0][0][0][2]+(1-q)*r*self.utility_tableau[0][1][0][2]+(1-r)*q*self.utility_tableau[1][0][0][2]+(1-r)*(1-q)*self.utility_tableau[1][1][0][2]==r*q*self.utility_tableau[0][0][1][2]+(1-q)*r*self.utility_tableau[0][1][1][2]+(1-r)*q*self.utility_tableau[1][0][1][2]+(1-r)*(1-q)*self.utility_tableau[1][1][1][2])
            eq.Equation(0<=r)
            eq.Equation(r<=1)
            eq.Equation(0<=q)
            eq.Equation(q<=1)
            eq.Equation(0<=p)
            eq.Equation(p<=1)
            eq.solve(disp=False)
            return q.value[0],r.value[0],p.value[0]

        if self.number_of_players == 2:
            q=twoPlayersEUtility(0)
            r=twoPlayersEUtility(1)
            return(q,r)
        elif self.number_of_players == 3:
            return threePlayersEUtility()

    def U2P(self,q):
        if q * (self.utility_tableau[0][0][0] - self.utility_tableau[0][1][0] - self.utility_tableau[1][0][0] + self.utility_tableau[1][1][0]) + self.utility_tableau[0][1][0] - self.utility_tableau[1][1][0] > 0:
            return 1
        else:
            return 0
    def U1P(self,r):
        if r * (self.utility_tableau[0][0][1] - self.utility_tableau[1][0][1] - self.utility_tableau[0][1][1] + self.utility_tableau[1][1][1]) + self.utility_tableau[1][0][1] - self.utility_tableau[1][1][1] > 0:
            return 1
        else:
            return 0
            
    '''
    This section handles plotting
    '''
    def plot2PlayersMixed(self, p, q):
        x = np.linspace(0,1,100)
        y=[]
        y1=[]
        for i in x: 
            y.append(self.U1P(i))
            y1.append(self.U2P(i))
        plt.savefig("./twp_plot.png")
        plt.plot(x,y,label="player 1")
        plt.plot(y1,x,label="player 2")
        plt.legend()
        plt.savefig("./twp_plot.png")
        # plt.show()

    def plot3PlayersMixed(self, p, q, r):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x2 = np.linspace(0, 1, 100)
        y2 = np.linspace(0, 1, 100)
        X2, Y2 = np.meshgrid(x2, y2)
        z2 = np.zeros((X2.shape[0], X2.shape[1]))
        for i in range(X2.shape[0]):
            for j in range(Y2.shape[1]):
                z2[i][j] = self.derivateU1(X2[i][j], Y2[i][j])  # z y
        ax.plot_wireframe(X2, Y2, z2, color="blue")
        plt.title('First player ')
        plt.xlabel('Second Player', fontsize=14)
        plt.ylabel('Third Player', fontsize=14)
        plt.show()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x1 = np.linspace(0, 1, 100)
        y1 = np.linspace(0, 1, 100)
        X1, Y1 = np.meshgrid(x1, y1)
        z1 = np.zeros((X1.shape[0], X1.shape[1]))
        for i in range(X1.shape[0]):
            for j in range(Y1.shape[1]):
                z1[i][j] = self.derivateU2(X1[i][j], Y1[i][j])  # z x
        ax.plot_wireframe(X1, Y1, z1, color="red")
        plt.title('Second player ')
        plt.xlabel('Third Player', fontsize=14)
        plt.ylabel('First Player', fontsize=14)
        plt.show()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x = np.linspace(0, 1, 100)
        y = np.linspace(0, 1, 100)
        X, Y = np.meshgrid(x, y)
        z = np.zeros((X.shape[0], X.shape[1]))
        for i in range(X.shape[0]):
            for j in range(Y.shape[1]):
                z[i][j] = self.derivateU3(X[i][j], Y[i][j])  # y x
        plt.title('Third player ')
        plt.xlabel('Second Player', fontsize=14)
        plt.ylabel('First Player', fontsize=14)
        ax.plot_wireframe(X,Y, z, color="green")
        plt.show()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_wireframe(X2, Y2, z2, color="blue")
        ax.plot_wireframe(X1, z1, Y1, color="red")
        ax.plot_wireframe(z, X,Y, color="green")
        plt.title('Third player')
        plt.xlabel('First Player', fontsize=14)
        plt.ylabel('Second Player', fontsize=14)
        plt.show()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        plt.xlabel('Second Player', fontsize=14)
        plt.ylabel('First Player', fontsize=14)
        ax.scatter(r,q, p, color="black")
        plt.show()

    def plot3PlayersMixed_GUI(self, p, q, r, k):

        x2 = np.linspace(0, 1, 100)
        y2 = np.linspace(0, 1, 100)
        X2, Y2 = np.meshgrid(x2, y2)
        z2 = np.zeros((X2.shape[0], X2.shape[1]))

        x1 = np.linspace(0, 1, 100)
        y1 = np.linspace(0, 1, 100)
        X1, Y1 = np.meshgrid(x1, y1)
        z1 = np.zeros((X1.shape[0], X1.shape[1]))

        x = np.linspace(0, 1, 100)
        y = np.linspace(0, 1, 100)
        X, Y = np.meshgrid(x, y)
        z = np.zeros((X.shape[0], X.shape[1]))

        for i in range(X2.shape[0]):
                for j in range(Y2.shape[1]):
                    z2[i][j] = self.derivateU1(X2[i][j], Y2[i][j])  # z y

        for i in range(X1.shape[0]):
                for j in range(Y1.shape[1]):
                    z1[i][j] = self.derivateU2(X1[i][j], Y1[i][j])  # z x
        
        for i in range(X.shape[0]):
                for j in range(Y.shape[1]):
                    z[i][j] = self.derivateU3(X[i][j], Y[i][j])  # y x

        if k==0:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_wireframe(X2, Y2, z2, color="blue")
            plt.title('First player ')
            plt.xlabel('Second Player', fontsize=14)
            plt.ylabel('Third Player', fontsize=14)
            plt.show()
        if k == 1:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_wireframe(X1, Y1, z1, color="red")
            plt.title('Second player ')
            plt.xlabel('Third Player', fontsize=14)
            plt.ylabel('First Player', fontsize=14)
            plt.show()
        if k == 2:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            plt.title('Third player ')
            plt.xlabel('Second Player', fontsize=14)
            plt.ylabel('First Player', fontsize=14)
            ax.plot_wireframe(X,Y, z, color="green")
            plt.show()
        if k == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_wireframe(z2, X2, Y2, color="blue")
            ax.plot_wireframe(X1, z1, Y1, color="red")
            ax.plot_wireframe(Y, X,z, color="green")
            plt.title('Third player')
            plt.xlabel('First Player', fontsize=14)
            plt.ylabel('Second Player', fontsize=14)
            plt.show()
        if k == 4:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            plt.xlabel('Second Player', fontsize=14)
            plt.ylabel('First Player', fontsize=14)
            ax.scatter(r,q, p, color="black")
            plt.show()

    def derivateU1(self, q, p):
        c = (   q*p*Fraction(self.utility_tableau[0][0][0][0])+p*(1-q)*self.utility_tableau[0][1][0][0]+(1-p)*q*self.utility_tableau[0][0][1][0]+(1-p)*(1-q)*self.utility_tableau[0][1][1][0]
                >=
                q*p*self.utility_tableau[1][0][0][0]+p*(1-q)*self.utility_tableau[1][1][0][0]+(1-p)*q*self.utility_tableau[1][0][1][0]+(1-p)*(1-q)*self.utility_tableau[1][1][1][0])
        return 1 if c else 0

    def derivateU2(self, p, r):
        c = (  r*p*self.utility_tableau[0][0][0][1]+(1-r)*p*self.utility_tableau[1][0][0][1]+r*(1-p)*self.utility_tableau[0][0][1][1]+(1-r)*(1-p)*self.utility_tableau[1][0][1][1]
                >=
                r*p*self.utility_tableau[0][1][0][1]+(1-r)*p*self.utility_tableau[1][1][0][1]+r*(1-p)*self.utility_tableau[0][1][1][1]+(1-r)*(1-p)*self.utility_tableau[1][1][1][1])
        return 1 if c else 0

    def derivateU3(self, q, r):
        c = (   r*q*self.utility_tableau[0][0][0][2]+(1-q)*r*self.utility_tableau[0][1][0][2]+(1-r)*q*self.utility_tableau[1][0][0][2]+(1-r)*(1-q)*self.utility_tableau[1][1][0][2]
                >=r
                *q*self.utility_tableau[0][0][1][2]+(1-q)*r*self.utility_tableau[0][1][1][2]+(1-r)*q*self.utility_tableau[1][0][1][2]+(1-r)*(1-q)*self.utility_tableau[1][1][1][2])
        return 1 if c else 0
