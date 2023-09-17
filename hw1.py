#Liam Cummings HW 1
#Intro to AI

import sys
#import numpy as np

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
def findPath(filepath, start, end):
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
            #need to return path somehow :(
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
        
#returns T or F
def areNeighbors(word1, word2):
    splitWord1 = [char for char in word1]
    splitWord2 = [char for char in word2]
    difLetters = []
    for element in splitWord1:
        if element not in splitWord2:
            difLetters.append(element)
    if len(difLetters) > 1:
        return False
    return True    
        

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 hw1.py dictionary_file start_word target_word")
        sys.exit(1)
        
    filepath = sys.argv[1]
    start = sys.argv[2].lower()
    end = sys.argv[3].lower()
    reversed = []
    visited = findPath(filepath, start, end)
    #print(visited)
    
    try:
        visited.reverse() 
    except:
        print("No solution")
        
    reversed = visited

    #print(reversed)
    
    #Go backwards throgh list, making sure words connect properly
    i = 0
    path = []
    while i < len(visited) - 1:
        if areNeighbors(reversed[i], reversed[i+1]):
            path.append(reversed[i])
            i = i + 1
        else:
            reversed.pop(i + 1)
        
    path.reverse()
    path.insert(0, start)
    
    #At this point, list is correctly ordered, with extra info
    invalid = []
    i = 0
    while i < len(visited) - 2:
        if areNeighbors(path[i], path[i+2]):
            invalid.append(i + 1)
        i = i + 1
    
    #print(invalid)
        
    invalid.reverse()
    
    final = []
    
    for element in path:
        if element not in invalid:
            final.append(element)
    
    if final is None:
        print("No solution")
    else:
        for word in final:
            print(word)