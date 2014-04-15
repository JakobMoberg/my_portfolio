# -*- coding: cp1252 -*-
import math
import json
import requests 
import threading
import Queue
import time

def splitInTwo(s):
    #Removes the last word from string s.
    # a:= rest of s
    # b:= last word
    split_pos=s.rfind(' ')
    if split_pos>-1:            
        a=s[:split_pos]
        b=s[split_pos+1:]
    else:
        a=s
        b=''
    return(a,b)

def reqSong(s):
    #Reqest for song s
    #Prints an error msg if a bad_status code is recieved
    
    query_params = {'q': 'track:'+s}
    endpoint = 'http://ws.spotify.com/search/1/track.json'
    response = requests.get(endpoint, params= query_params)
    track = {}
    out_trac={}
    if response.status_code == 200:
        i = 0
        data = json.loads(response.content)

        while True:
            #Here checks for availability based on the user´s region
            #etc should be carried out if needed

            if int(data['info']['num_results']) == i or 100 == i:
                #Breaks if no results or 100 tracks looped
                out_track={}
                break
            else:

                track = {'name':data['tracks'][i]['name'], 'artist':data['tracks'][i]['artists'][0]['name'], 'uri':data['tracks'][i]['href']}
                
                if s.upper() == track['name'].upper():
                    #Takes the first track that matches by name
                    out_track=track
                    break
                i+=1
                
        return out_track
    else:
        print(line+' caused an error')
        print(response.status_code)
        

def reqLine(q,line,lineNr):
    #Function parsing a single line with lineNr, lineNr
    # Input:
    # q: an Queue object for storage of the results
    # line: A line to be parsed ad requested until finished
    # lineNR: 'lines' row in the poem
    # Returns:
    # None (stores in q)
    uris = []
    names=[]
    noMatch=[]
    searchStr=line
    rest=''
    run=True
    outVal=[]
    while run: 
        #Starts by matching the whole line. If no matches it contiues to try
        #removing one word at the time until a single word is lef or a
        # sucessful match is found
        track=reqSong(searchStr)
        if len(track)>0:
            #case: found matching track
            uris.append(track['uri'])
            names.append(track['name'])
            searchStr=rest
            rest=''    
        else:
            #case: no match  
            if searchStr.find(' ')==-1:
            #if a single word doesn´t match, it is added to the noMatch list                
                noMatch.append(searchStr)
                searchStr=rest
                rest=''
            else:
                a,b=splitInTwo(searchStr)
                searchStr=a
                rest=b+' '+rest
        if searchStr=='':
            run=False
    outVal.append(lineNr)
    outVal.append(uris)
    outVal.append(names)
    outVal.append(noMatch)
    q.put(outVal)


#
#Script where the magic happens
#Created by: Jakob Moberg
#moberg.jakob@gmail.com

start_time = time.time()
inFile= 'InputFile.txt'
#Inputfile
outFile='OutputFile.txt'
#Output file
ins = open(inFile , 'r' )

playList=[]
noMatchList=[]
poem=[]
q=Queue.Queue()
lineNr=0

print('Input Poem:')
for line in ins:
    print(line.strip())
    #Reads text from ins
    #Each sentence on a new line
    #Note:
    #Could be done to look for '.' depending on input
    #but is not implemented here
    lineNr+=1
    t=threading.Thread(target=reqLine, args= (q, line.strip(), lineNr))
    t.daemon = True
    t.start()

#Waits for all threads to finnish    
q.join()
ins.close()

#Collects the output and arranges it
resLines=[]
for i in range(lineNr):
    s = q.get()                       
    resLines.insert(s[0],s)

sortedL= sorted(resLines)

#Prints/Writes the output data
print('\n'+'Resulting Poem:')
for line in sortedL:
    poemPart=line[2]
    for name in poemPart:
        print name,
    print ''

#This part can be copy-pasted into an playlist in Spotify to create the
#desired playlist

file=open('./'+outFile, 'w+')        
print('\n'+'Spotify Playlist Uri:')
for line in sortedL:
    uriPart=line[1]
    for uri in uriPart:
        print(uri)
        file.write(uri +'\n')
file.close()

i=1
print('\n'+'Missing words:')
for line in sortedL:
    print('On line nr ' + str(i)+' the word(s): ' )
    missingPart=line[3]
    for words in missingPart:
        print(words)
    i+=1

print('\n'+'Input file:'+inFile)
print('Output file:'+outFile)

elapsed_time = time.time() - start_time

print('Elapsed time:')
print(elapsed_time)
