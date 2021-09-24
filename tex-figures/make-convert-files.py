#! /urs/bin/env python
import os
import glob

def write_image_file(data):
    base = './'
    top = '\\documentclass{standalone}\n\\input{preamble}\n\n\\begin{document}\n'
    bottom = '\n\\end{document}'
    
    out = top + data['text'] + bottom
    
    file = open(base + 'fig_' + data['name']+'.tex','a')
    file.write(out)
    file.close()
    
def write_table_file(data):
    base = './'
    top = '\\documentclass{standalone}\n\\input{preamble}\n\n\\begin{document}\n'
    bottom = '\n\\end{document}'
    
    out = top + data['text'] + bottom
    
    file = open(base + 'tab_' + data['name']+'.tex','a')
    file.write(out)
    file.close()

# Read the file
file = open('all-fig.tex','r')
text = file.read()
file.close()

# Cleanup any old files
for file_type in ['fig*']:
    files = glob.glob(file_type)
    for f in files: 
        os.remove(f)

#------------------------------------#
# Work on the images
#------------------------------------#
s = {'start':'\\begin{myTikz}','end':r'\end{myTikz}','name': '%File name:'} #String
p ={'start':0,'end':0,'name':0}                                             # Positions
f = {'name':'','text':''}                                                   # File data 

l = s.copy()                                                                # Lengths

for i in s:
    l[i] = len(s[i])
 
current_text = text

while True:
    # Get the start and end of the block
    p['start'] = current_text.find(s['start']) 
    if p['start'] == -1: break

    p['end'] = current_text.find(s['end']) 

    # Correct for the length of the string
    p['end'] += l['end']

    # Get the file name
    p['name'] = current_text.find(s['name'])
    t = current_text[p['name']:].find('\n')
    f['name'] = current_text[p['name']+l['name']+1:p['name']+t]
    f['text'] = current_text[p['start']:p['end']]

    write_image_file(f)
    
    print('Wrote {}'.format(f['name']+'.tex'))
    
    current_text = current_text[p['end']:]
    
    
    
#------------------------------------#
# Work on the tables
#------------------------------------#
s = {'start':'%Table-start','end':'%Table-end','name': '%Table name:'} #String
p ={'start':0,'end':0,'name':0}                                             # Positions
f = {'name':'','text':''}                                                   # File data 

l = s.copy()                                                                # Lengths

for i in s:
    l[i] = len(s[i])
 
current_text = text

while True:
    # Get the start and end of the block
    p['start'] = current_text.find(s['start']) 
    if p['start'] == -1: break

    p['end'] = current_text.find(s['end']) 

    # Correct for the length of the string
    p['end'] += l['end']

    # Get the file name
    p['name'] = current_text.find(s['name'])
    t = current_text[p['name']:].find('\n')
    f['name'] = current_text[p['name']+l['name']+1:p['name']+t]
    f['text'] = current_text[p['start']:p['end']]

    write_table_file(f)
    
    print('Wrote {}'.format(f['name']+'.tex'))
    
    current_text = current_text[p['end']:]
