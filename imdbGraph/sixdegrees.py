#!/usr/bin/env python3
# don't delete these comments!

import sys
from actorNetwork import ActorNetwork

if __name__ == "__main__":
    print(f"got {len(sys.argv) - 1} command line arguments")
    imdbNet = ActorNetwork()

    # create actorNetwork object
    with open('cleaned_movielist.txt', 'r') as file:
        for line in file:
            fullLn = line.strip().split(" ")
            movie, actors = fullLn[0],set(fullLn[1:])        
            imdbNet.addMovie(movie, actors)

    inputFile = sys.argv[1]
    outputNm = sys.argv[2]

    with open(inputFile, 'r') as infile, open(outputNm, 'w') as outfile:
        for line in infile:
            a1,a2 = line.strip().split(" ")    
            outfile.write(imdbNet.getPath(a1,a2)+"\n")

