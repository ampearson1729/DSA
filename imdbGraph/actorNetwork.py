from collections import defaultdict
import queue

class ActorNetwork:

    def __init__(self):
        """ Creates an actor network object """
        self.costars = defaultdict(set) # actors(string) to acted with (set<string>)
        self.movies  = defaultdict(set) # actors(string) to movies starred in (set<string>)

    def addMovie(self, movie, actors):
        """ Given a movie (str) and actors set(str) in that movie """
        processed = set() 
        while actors:
            actor = actors.pop()
            self.costars[actor] = self.costars[actor].union(actors).union(processed)
            self.movies[actor].add(movie)
            processed.add(actor)

    def getPath(self, actor1, actor2, method = "Vanilla"):
        """ Given two actors gets the path between or returns Not Present """
        if actor1 == actor2: return actor1 
        data, numEdges = self._findConnection(actor1, actor2, method)
        return self._cleanPath([actor1, actor2, data], numEdges, method)

    def countVertices(self):
        """ Returns number of vertices in this graph """
        return len(self.costars)

    def countEdges(self):
        """ Given fields in object count edges in current network """
        numEdges = 0
        for _, val in self.costars.items(): numEdges += len(val) 
        return int(numEdges/2)

    def _findConnection(self, actor1, actor2, method):
        """ returns path of actor1 to actor2 AND number of edges used to explore """
        if method == "Vanilla": return self._vanillaFC(actor1, actor2)
        elif method == "Bidirectional": return self._bidirectionalFC(actor1, actor2)

    def _bidirectionalFC(self, actor0, actor1):
        """ returns path of actor0 to actor1 AND the number of edges used to explore """
        # Number of edges explored in this algorithm
        numEdges = 0
        # Check if actors are in network
        if actor0 not in set(self.costars.keys())\
        or actor1 not in set(self.costars.keys()):
            return False, numEdges
        # Initalize Objects for BFS
        pred0 = defaultdict(None)
        pred1 = defaultdict(None)
        Q0 = queue.SimpleQueue()
        Q0.put(actor0)
        Q1 = queue.SimpleQueue()
        Q1.put(actor1)
        visited0 = defaultdict(bool)
        visited1 = defaultdict(bool)
        # Put these objects in an array for bidirections BFS
        predArr = [pred0,pred1]
        Qarr = [Q0,Q1]
        visitedArr = [visited0,visited1]
        actors = [actor0, actor1]
        # Initialize switch to start with 0th tree 
        switch = 0
        # Terminate early if we find the connection
        foundConnection = False
        # TODO: Clean this up later to account for case where one Q ends before the other
        while not (Qarr[0].empty() and Qarr[1].empty()):
            othIndx = (switch+1)%2 # Other index for objects
            pred = predArr[switch]
            Q = Qarr[switch]
            visited = visitedArr[switch]
            otherActor = actors[othIndx]
            # run iteration of BFS
            u = Q.get()
            for v in self.costars[u]:
                if not visited[v]:
                    numEdges += 1
                    visited[v] = True
                    pred[v] = u
                    if v in visitedArr[othIndx] or v == otherActor: 
                        return [predArr, v], numEdges
                    Q.put(v)
            switch = othIndx
            
        if not foundConnection: 
            return False, numEdges

    def _vanillaFC(self, actor1, actor2):
        """ Finds a shortest path between actor1 and actor 2 AND number of edges explored """
        # Number of edges explored in this algorithm
        numEdges = 0 
        # Check if actors are in network
        if actor1 not in set(self.costars.keys())\
        or actor2 not in set(self.costars.keys()):
            return False, numEdges
        # Initalize Objects for BFS
        pred = defaultdict(None)
        Q = queue.SimpleQueue()
        Q.put(actor1)
        visited = defaultdict(bool)
        # Terminate early if we find the connection
        foundConnection = False
        while not Q.empty():
            u = Q.get()
            for v in self.costars[u]:
                if not visited[v]:
                    numEdges += 1
                    visited[v] = True
                    pred[v] = u
                    # TODO think about what to do if v == actor2
                    if v == actor2: return pred, numEdges
                    Q.put(v)
        if not foundConnection: return False, numEdges

    def _cleanPath(self, data, numEdges, method):
        """ Given a predecesor dictionary create a path """
        if method == "Vanilla":
            actor1, actor2, predDict = data[0],data[1],data[2]
            if not predDict: return "Not present"
            pthLst = [actor2]
            currActor = actor2
            while True:
                nextActor = predDict[currActor]
                intSec = self.movies[currActor].intersection(self.movies[nextActor])
                pthLst.append(" -(" + intSec.pop() + ")- ")
                pthLst.append(nextActor) 
                if nextActor == actor1: 
                    ans = "".join(pthLst[::-1])
                    return "# Edges: " +str(numEdges) + "     " + ans.replace("_"," ")
                currActor = nextActor
        elif method == "Bidirectional":
            actor0, actor1, predArr, actorv = data[0],data[1],data[2][0],data[2][1]
            if not predArr: return "Not present"
            predDict = predArr[0]
            pthLst = [actorv]
            currActor = actorv
            while True:
                nextActor = predDict[currActor]
                intSec = self.movies[currActor].intersection(self.movies[nextActor])
                pthLst.append(" -(" + intSec.pop() + ")- ")
                pthLst.append(nextActor) 
                if nextActor == actor0: 
                    ans0 = pthLst[::-1]
                    break
                currActor = nextActor
            # 
            predDict = predArr[1]
            pthLst = [actorv]
            currActor = actorv
            while True:
                nextActor = predDict[currActor]
                intSec = self.movies[currActor].intersection(self.movies[nextActor])
                pthLst.append(" -(" + intSec.pop() + ")- ")
                pthLst.append(nextActor) 
                if nextActor == actor1: 
                    ans1 = pthLst
                    break
                currActor = nextActor
            ans = "".join(ans0 + ans1[1:])
            return "# Edges: " +str(numEdges) + "     " + ans.replace("_"," ")


if __name__ == "__main__":
    imdbNet = ActorNetwork()
    with open('all_imdb_cleaned.txt', 'r') as file:
        for line in file:
            fullLn = line.strip().split(" ")
            movie, actors = fullLn[0],set(fullLn[1:])        
            imdbNet.addMovie(movie, actors)

    a1, a2 = "Brad_Pitt","Rachel_McAdams"


