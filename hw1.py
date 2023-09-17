#Liam Cummings HW 1
#Intro to AI

import sys

#Parse dict by line into array
def parseDict(filename):
    words = []
    file = open(filename, 'r')
    for line in file:  
        line = line.strip()
        words.append(line)
    return words
        
#go through all words that are 1 letter off
#takes in start word, returns list of words
def genNeighbors(word, visited):
    neighbors = []
    #split word into its letters
    for i in range (0, len(word)):
        splitWord = [char for char in word]
        #97 -> 122 == lowercase ASCII
        for x in range(97, 123):
            temp = splitWord
            letter = chr(x)
            temp[i] = letter
            combined = ''.join(temp)
            if combined not in visited:
                neighbors.append(combined) 
    return neighbors
      
          
#returns the path between start and end using dictionary "filepath"        
def findPath(filepath, start, end,):
    frontier = [str(start)]
    visited = []
    
    allWords = parseDict(filepath)
    wordLen = len(start)
    
    #remove all incorrect len words from dict
    correctSize = []
    for word in allWords:  
        if len(word) == wordLen:
            correctSize.append(word)         

    #go through gens
    gen = 0
   
    #for item in frontier:
    while len(frontier) > 0:
        item = frontier[0]
        gen = gen + 1  
        
        #goal case
        if item == end:
            visited.append(end)
            return visited
        visited.append(item)
        
        #print(gen)
        #print(item)
        
        neighbors = genNeighbors(item, visited)
        
        nextGen = []
        #go through neighbors and delete all invalid words
        for word in neighbors:
            if word in correctSize and word not in frontier:
                nextGen.append(word)  
        #print(nextGen)
        #Add neighbors to frontier
        for word in nextGen:
            frontier.append(word)
        
        frontier.remove(item)
        #print(frontier)
        #print(visited)
        #print("\n")
    #fail case    
    return None
        

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 hw1.py dictionary_file start_word target_word")
        sys.exit(1)
        
    filepath = sys.argv[1]
    start = sys.argv[2].lower()
    end = sys.argv[3].lower()
          
    finalPath = findPath(filepath, start, end)
    
    if finalPath is None:
        print("No solution")
    else:
        for word in finalPath:
            print(word)