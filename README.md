# Nash-Equilibrium

This program can compute pure and mixed strategy Nash equilibria for 2 and 3 players. In pure strategy, each player plays only one move.

## Requirements:
You must have installed python 3.x:

#### On Linux
```bash
sudo apt-get update
sudo apt-get install python3
```

#### On Windows 
You can download it and install it from https://www.python.org/downloads/windows/

## Dependencies : 
To install the dependencies and set up the application, follow the following instructions :

```bash
$ virtualenv nashENV
$ source nashENV/bin/activate
$ pip install -r requirements.txt
```

## Usage
### For the terminal interface:
To run the program, provide an input file as the first argument and a choice of strategy as the second argument. E.g. :
```bash
$ python src/nash_eq.py path_to_file.txt -p
```

### For the graphical interface:
#### Linux
execute the following instruction on your terminal:
```
./launch.sh
```

#### Windows
execute the following instruction on your terminal:
```
./launch.bat
```

## Help For Linux interface :
```bash
usage: nash_eq.py [-h] -f FILE [-p] [-m] [-N [NumberOfPlayers]] [-l1 LABEL]
                  [-l2 LABEL] [-l3 LABEL] [-s1 [LABEL [LABEL ...]]]
                  [-s2 [LABEL [LABEL ...]]] [-s3 [LABEL [LABEL ...]]]

Calculates pure and mixed Nash equilibrium strategies.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  defines the path to the file containing the utility
                        function
  -p, --pure            search for pure nash strategies
  -m, --mixed           search for mixed nash strategies
  -N [NumberOfPlayers], --number-of-players [NumberOfPlayers]
                        defines the number for playing players, default to 2
                        if not specified
  -l1 LABEL, --label-p1 LABEL
                        define a label for player 1
  -l2 LABEL, --label-p2 LABEL
                        define a label for player 2
  -l3 LABEL, --label-p3 LABEL
                        define a label for player 3
  -s1 [LABEL [LABEL ...]], --strategies-p1 [LABEL [LABEL ...]]
                        define strategies' labels for player 1
  -s2 [LABEL [LABEL ...]], --strategies-p2 [LABEL [LABEL ...]]
                        define strategies' labels for player 2
  -s3 [LABEL [LABEL ...]], --strategies-p3 [LABEL [LABEL ...]]
                        define strategies' labels for player 3
```

## Input file format
Input files have the following format :

### For two players :

    1,1 1,2 1,3
    2,1 2,2 2,3
    3,1 3,2 3,3

Rows represent player 1's moves while columns represent player 2's moves. Each (row, column) pair represents the payouts from the players' corresponding moves. The first value is player 1's payout, the second value is player 2's payout.

### For three players :

    0,0,0 3,3,3
    3,3,3 2,2,4
    
    3,3,3 4,2,2
    2,4,2 1,1,1

Rows represent player 1's moves while columns represent player 2's moves. Each (row, column) pair represents the payouts from the players' corresponding moves. The first value is player 1's payout, the second value is player 2's payout.

The strategies of the third player are represented by the two tables separated by an empty line, the first table represent the first strategy of the third players, while the second table represents the second strategy of the third player.