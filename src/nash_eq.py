import sys, argparse, nash

# Defining Parsing arguments :
parser = argparse.ArgumentParser(description='Calculates pure and mixed Nash equilibrium strategies.')

parser.add_argument("-f", "--file", dest="filename", help="defines the path to the file containing the utility function", metavar="FILE", required=True)
parser.add_argument("-p","--pure", dest="pure", action='store_true', help="search for pure nash strategies")
parser.add_argument("-m","--mixed", dest="mixed", action='store_true', help="search for mixed nash strategies")
parser.add_argument("-N","--number-of-players",nargs='?',dest="number_players", help="defines the number for playing players, default to 2 if not specified", default=2, metavar="NumberOfPlayers", type=int)
parser.add_argument("-l1","--label-p1", dest="label1", default=None, help="define a label for player 1", metavar="LABEL")
parser.add_argument("-l2","--label-p2", dest="label2", default=None, help="define a label for player 2", metavar="LABEL")
parser.add_argument("-l3","--label-p3", dest="label3", default=None, help="define a label for player 3", metavar="LABEL")
parser.add_argument("-s1","--strategies-p1", nargs='*', dest="strategies1", default=None, help="define strategies' labels for player 1", metavar="LABEL")
parser.add_argument("-s2","--strategies-p2", nargs='*', dest="strategies2", default=None, help="define strategies' labels for player 2", metavar="LABEL")
parser.add_argument("-s3","--strategies-p3", nargs='*', dest="strategies3", default=None, help="define strategies' labels for player 3", metavar="LABEL")

args = parser.parse_args()

# Checking arguments :
if not (args.pure or args.mixed) :
    parser.print_help(file=sys.stderr)
    print("\n\nSpecify a strategy to use, available options : [-p, -m]", file=sys.stderr)
    exit(1)
# Check for the supplied number of players
elif 2 != args.number_players != 3 :
    parser.print_help(file=sys.stderr)
    print("\n\nSpecify the number of players, available options : [2, 3]", file=sys.stderr)
    exit(2)
elif args.number_players != 3 and args.label3 != None :
    parser.print_help(file=sys.stderr)
    print("\n\nA label was specified for a played which doesn't exist", file=sys.stderr)
    exit(3)
elif args.number_players != 3 and args.strategies3 != None :
    parser.print_help(file=sys.stderr)
    print("\n\nStrategy labels were specified for a played which doesn't exist", file=sys.stderr)
    exit(4)

# TODO TODELETE
print(args)

nsh = nash.Nash(args.filename, 
                number_of_players=args.number_players,
                labels=[args.label1, args.label2, args.label3],
                strategies=[args.strategies1, args.strategies2, args.strategies3])

if args.pure:
    nsh.compute_pure_strategies()
if args.mixed:
    nsh.compute_mixed_strategies()
