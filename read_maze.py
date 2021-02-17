def read_maze(filename):
    try:
        with open(filename) as fh:
            maze = [[char for char in line.strip('\n')] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print ("The maze is not rectangular.")
                    raise SystemExit
            return maze
    except OSError:
        print ("There is a problem with the file you have selected.")
        raise SystemExit