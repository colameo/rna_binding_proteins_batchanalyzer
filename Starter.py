'''
Created on Mar 19, 2017

@author: david
'''

import sys, time, os
from getIDs import getIDs
from retrieve_sequence_inbatch import startSeqsaving
from readFasta import batch_load_files
start_time = time.time()
Input = ''
Output = ''


if len(sys.argv) == 1:
    while Input == '' and Output == '':
        Input = raw_input('Specify Path to your table with genes: ')
        print ''
        path = ['', Input, Output]    
else:
    path = sys.argv
    
while not os.path.isfile(path[1]):
    print 'Please, specify a path to your genelist!\n'
    Input = raw_input('Specify Path to your table with genes: ')

    print ''
    path = ['', Input, Output]

table_ID = getIDs(path[1])
numberOfGeneGroups = len(table_ID[1])

dict_geneGroups = {}

for i in range(0, len(table_ID[0])):
    dict_geneGroups[table_ID[0][i]] = []
    
for i in range(0, numberOfGeneGroups):
    #dict_geneGroups[str('group' + str(i+1))] = []
    for j in range(1, len(table_ID)):
            dict_geneGroups[table_ID[0][i]].append(table_ID[j][i])
            
#print dict_geneGroups
        
path = raw_input('Where do you want to save the sequences?')

if path != 'no':
    path = path + '/groupedSequences'
    path2groups = {}
    if not os.path.exists(path):
        os.makedirs(path)

    for key in dict_geneGroups:
        pathGroup = path + '/' + key
        path2groups[key] = []
        if not os.path.exists(pathGroup):
            os.makedirs(pathGroup)
            print 'Folder %s created' %key
            print ''
        path2groups[key].append(pathGroup)
        startSeqsaving(dict_geneGroups[key], pathGroup) 

print ''
print 'Groups: '
numberofgenes = 0

for key in dict_geneGroups:
    print key
    for i in range(0, len(dict_geneGroups[key])):
        if dict_geneGroups[key][i]!= '':
            numberofgenes += 1
            

    
print ''
print 'Number of genes are: ', numberofgenes

#Retrieve Sequences from Fasta and save them in a dictionary


for key in path2groups:
    path2groups[key].append(batch_load_files(path2groups[key][0]))

for key in path2groups: 
    print key
    for key1 in path2groups[key]:
        print key1

#next step: build a function which sends the seq to the database and stores the .csv in a folder

timer = str(round((time.time() - start_time), 2))    
print('\n--- Total Time to Process %s seconds ---' % (time.time() - start_time))




