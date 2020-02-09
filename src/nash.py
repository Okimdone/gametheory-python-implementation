import numpy as np

class Nash:
    def __init__(self, path, number_of_players=2, labels=[0, 1], strategies=[]):
        with open(path, "r") as f:
            n, self.payout_grid     = self.load_grid(f)
            if n != number_of_players:
                raise Exception(f"The Number of players supplied does not match the file at {path}")

            self.number_of_players  = number_of_players
            self.p_indexes          = list(range(number_of_players))
            self.labels             = list(range(number_of_players))
            if labels[0] != None:
                self.labels[0]      = labels[0]
            if labels[1] != None:
                self.labels[1]      = labels[1]
            if len(labels) == 3 and labels[2]!=None:
                self.labels[2]      = labels[2]

            self.strat_labels       = [   self.generate_labels(len(self.payout_grid)),
                                          self.generate_labels(len(self.payout_grid[0])) ]
            if number_of_players == 3 :
                self.strat_labels.append( self.generate_labels(len(self.payout_grid[0][0])) )
            self.strategies         = strategies

    def load_grid(self, file:__file__):
        grid_1D = []
        depth_1D, depth_3D = 0, 0
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
            else: 
                for i in range(len(grid_2D_line)):
                   grid_1D[depth_1D][i].append( grid_2D_line[i] )
            depth_1D += 1
        return (2, grid_1D[0]) if len(grid_1D)==1 else (3, grid_1D)

    def generate_labels(self, labels_num):
        return list(range(labels_num))

    #def remove_strictly_dominated_moves(self):
    #    while self.remove_strictly_dominated_p1() | self.remove_strictly_dominated_p2():
    #        pass

    #def remove_strictly_dominated_p1(self):
    #    rows_to_keep = set()
    #    row_num = len(self.payout_grid)
    #    col_num = len(self.payout_grid[0])
    #    for c in range(col_num):
    #        max_payout = max([self.payout_grid[r][c][P1] for r in range(row_num)])
    #        for r in range(row_num):
    #            if self.payout_grid[r][c][P1] == max_payout:
    #                rows_to_keep.add(r)
    #
    #    new_payout_grid = [self.payout_grid[i] for i in sorted(rows_to_keep)]
    #    self.payout_grid = new_payout_grid
    #    self.strat_labels[0] = [self.strat_labels[0][i] for i in sorted(rows_to_keep)]
    #    return row_num != len(rows_to_keep);

    #def remove_strictly_dominated_p2(self):
    #    cols_to_keep = set()
    #    row_num = len(self.payout_grid)
        #col_num = len(self.payout_grid[0])
        #for r in range(row_num):
            #max_payout = max([self.payout_grid[r][c][P2] for c in range(col_num)])
            #for c in range(col_num):
                #if self.payout_grid[r][c][P2] == max_payout:
                    #cols_to_keep.add(c)

        #new_payout_grid = [[] for _ in range(row_num)]
        #for c in sorted(cols_to_keep):
            #for r in range(row_num):
                #new_payout_grid[r].append(self.payout_grid[r][c])
        #self.payout_grid = new_payout_grid
        #self.strat_labels[1] = [self.strat_labels[1][i] for i in sorted(cols_to_keep)]
        #return col_num != len(cols_to_keep);

    def remove_dominated_moves(self):
        while self.remove_dominated_p1() | self.remove_dominated_p2():
            pass

    def remove_dominated_p1(self):
        row_num = len(self.payout_grid)
        col_num = len(self.payout_grid[0])
        max_values = []
        for c in range(col_num):
            max_payout = max([self.payout_grid[r][c][self.p_indexes[0]] for r in range(row_num)])
            rows_to_keep = set()
            for r in range(row_num):
                if self.payout_grid[r][c][self.p_indexes[0]] == max_payout:
                    rows_to_keep.add(r)
            max_values.append(rows_to_keep)

        rows_to_keep = []
        while max_values:
            maximum_intersection = max_values[0].copy()
            for c in range(1, len(max_values)):
                if len(maximum_intersection & max_values[c]) != 0:
                    maximum_intersection = maximum_intersection & max_values[c]
            max_index = maximum_intersection.pop()
            rows_to_keep.append(max_index)
            max_values = [row for row in max_values if max_index not in row]

        new_payout_grid = [self.payout_grid[i] for i in sorted(rows_to_keep)]
        self.payout_grid = new_payout_grid
        self.strat_labels[0] = [self.strat_labels[0][i] for i in sorted(rows_to_keep)]
        return row_num != len(rows_to_keep);

    def remove_dominated_p2(self):
        row_num = len(self.payout_grid)
        col_num = len(self.payout_grid[0])
        max_values = []
        for r in range(row_num):
            max_payout = max([self.payout_grid[r][c][self.p_indexes[1]] for c in range(col_num)])
            cols_to_keep = set()
            for c in range(col_num):
                if self.payout_grid[r][c][self.p_indexes[1]] == max_payout:
                    cols_to_keep.add(c)
            max_values.append(cols_to_keep)

        cols_to_keep = []
        while max_values:
            maximum_intersection = max_values[0].copy()
            for c in range(1, len(max_values)):
                if len(maximum_intersection & max_values[c]) != 0:
                    maximum_intersection = maximum_intersection & max_values[c]
            max_index = maximum_intersection.pop()
            cols_to_keep.append(max_index)
            max_values = [col for col in max_values if max_index not in col]

        new_payout_grid = [[] for _ in range(row_num)]
        for c in sorted(cols_to_keep):
            for r in range(row_num):
                new_payout_grid[r].append(self.payout_grid[r][c])
        self.payout_grid = new_payout_grid
        self.strat_labels[1] = [self.strat_labels[1][i] for i in sorted(cols_to_keep)]
        return col_num != len(cols_to_keep);

    def pure_strategy_solutions(self):
        best_payouts = {}
        best_payout_labels = []
        if self.number_of_players == 2 :
            Dim_1 = len(self.payout_grid)
            Dim_2 = len(self.payout_grid[0])
            for c in range(Dim_2):
                max_payout = max([self.payout_grid[r][c][self.p_indexes[0]] for r in range(Dim_1)])
                for r in range(Dim_1):
                    if self.payout_grid[r][c][self.p_indexes[0]] == max_payout:
                        best_payouts[(r, c)] = (self.strat_labels[0][r], self.strat_labels[1][c])

            best_payout_labels = []
            for r in range(Dim_1):
                max_payout = max([self.payout_grid[r][c][self.p_indexes[1]] for c in range(Dim_2)])
                for c in range(Dim_2):
                    if self.payout_grid[r][c][self.p_indexes[1]] == max_payout:
                        if (r, c) in best_payouts:
                            best_payout_labels.append(best_payouts[(r, c)])
        elif self.number_of_players == 3 :
            Dim_1 = len(self.payout_grid)
            Dim_2 = len(self.payout_grid[0])
            Dim_3 = len(self.payout_grid[0][0])
            for d_3 in range(Dim_3):
                for d_2 in range(Dim_2):
                    max_payout = max([self.payout_grid[d_1][d_2][d_3][self.p_indexes[2]] for d_1 in range(Dim_1)])
                    for d_1 in range(Dim_1):
                        if self.payout_grid[d_1][d_2][d_3][self.p_indexes[2]] == max_payout:
                            best_payouts[(d_1, d_2, d_3)] = (self.strat_labels[0][d_1], self.strat_labels[1][d_2], self.strat_labels[2][d_3])

            best_payout_labels_temp = {}
            for d_3 in range(Dim_3):
                for d_1 in range(Dim_1):
                    max_payout = max([self.payout_grid[d_1][d_2][d_3][self.p_indexes[0]] for d_2 in range(Dim_2)])
                    for d_2 in range(Dim_2):
                        if self.payout_grid[d_1][d_2][d_3][self.p_indexes[0]] == max_payout:
                            if (d_1, d_2, d_3) in best_payouts:
                                best_payout_labels_temp[(d_1, d_2, d_3)] = best_payouts[(d_1, d_2, d_3)]

            for d_1 in range(Dim_1):
                for d_2 in range(Dim_2):
                    max_payout = max([self.payout_grid[d_1][d_2][d_3][self.p_indexes[1]] for d_3 in range(Dim_3)])
                    for d_3 in range(Dim_3):
                        if self.payout_grid[d_1][d_2][d_3][self.p_indexes[1]] == max_payout:
                            if (d_1, d_2, d_3) in best_payout_labels_temp:
                                best_payout_labels.append(best_payout_labels_temp[(d_1, d_2, d_3)])

        return best_payout_labels;

    def mixed_strategy_solutions(self):
        self.remove_dominated_moves()
        p1_move_percents = {}
        p2_move_percents = {}
        side_length = len(self.payout_grid)
        if side_length == 1:
            p1_move_percents[self.strat_labels[0][0]] = 100
            p2_move_percents[self.strat_labels[1][0]] = 100
            return (p1_move_percents, p2_move_percents);

        p1_outcomes = [[1] * side_length]
        for c in range(1, side_length):
            p1_outcomes.append([self.payout_grid[r][c][self.p_indexes[1]] - self.payout_grid[r][0][self.p_indexes[1]] for r in range(side_length)])
        p1_solutions = [1] + [0]
        p1_outcomes = np.linalg.solve(np.array(p1_outcomes), np.array(p1_solutions))
        for r in range(len(self.strat_labels[0])):
            p1_move_percents[self.strat_labels[0][r]] = p1_outcomes[r] * 100

        p2_outcomes = [[1] * side_length]
        for r in range(1, side_length):
            p2_outcomes.append([self.payout_grid[r][c][self.p_indexes[0]] - self.payout_grid[0][c][self.p_indexes[0]] for c in range(side_length)])
        p2_solutions = [1] + [0]
        p2_outcomes = np.linalg.solve(np.array(p2_outcomes), np.array(p2_solutions))
        for c in range(len(self.strat_labels[1])):
            p2_move_percents[self.strat_labels[1][c]] = p2_outcomes[c] * 100

        return (p1_move_percents, p2_move_percents);

    def compute_pure_strategies(self):
        equilibriums = self.pure_strategy_solutions()
        if len(equilibriums) == 0:
            print("No pure strategies")
            return
        for i,s in enumerate(equilibriums):
            if self.number_of_players == 2:
                print(f"Pure Nash equilibrium strategy {i+1} is ({s[self.p_indexes[0]]}, {s[self.p_indexes[1]]})")
            elif self.number_of_players == 3:
                print(f"Pure Nash equilibrium strategy {i+1} is ({s[self.p_indexes[1]]}, {s[self.p_indexes[2]]}, {s[self.p_indexes[0]]})")


    def compute_mixed_strategies(self):
        equilibriums = self.mixed_strategy_solutions()
        for r in self.strat_labels[0]:
            print("Player 1 plays", r, equilibriums[0][r], "percent of the time")
        for c in self.strat_labels[1]:
            print("Player 2 plays", c, equilibriums[0][c], "percent of the time")
