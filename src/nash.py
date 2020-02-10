import numpy as np
from fractions import Fraction
from gekko import GEKKO

class Nash:
    def __init__(self, path, number_of_players=None, labels=[0, 1], strategies=[]):
        with open(path, "r") as f:
            n, self.utility_tableau     = self.load_grid(f)
            if number_of_players!=None and n != number_of_players:
                raise Exception(f"The Number of players supplied does not match the file at {path}")

            self.number_of_players  = n
            self.p_indexes          = list(range(n))
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
                grid_2D_line.append(tuple(int(payout) for payout in payouts.split(",")))

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
    def compute_mixed_strategies(self):
        equilibriums = self.mixed_strategy_solutions()

        print("\nPlayer 1 plays 0 %4.1f%% of the time" % (equilibriums[0]*100))
        print("Player 1 plays 1 %4.1f%% of the time\n" % (100-equilibriums[0]*100))

        print("Player 2 plays 0 %4.1f%% of the time" % (equilibriums[1]*100))
        print("Player 2 plays 1 %4.1f%% of the time\n" % (100-equilibriums[1]*100))

        if self.number_of_players == 3 :
            print("Player 3 plays 0 %4.1f%% of the time" % (equilibriums[2]*100))
            print("Player 3 plays 1 %4.1f%% of the time\n" % (100-equilibriums[2]*100))

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
                x = Fraction(b, a)
                return x
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
            eq.solve(disp=False)
            return q.value[0],r.value[0],p.value[0]

        if self.number_of_players == 2:
            q=twoPlayersEUtility(0)
            r=twoPlayersEUtility(1)
            return(q,r)
        elif self.number_of_players == 3:
            return threePlayersEUtility()