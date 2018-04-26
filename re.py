import os
import sys
import re

txtFile = sys.argv[1]
regFile = sys.argv[2]

with open(txtFile, 'r') as f1:
    txtlines = f1.readlines()

with open(regFile, 'r') as f2:
    regLines = f2.readlines()
    
for regLine in regLines:
    tp_ls = regLine.split('\t')
    p = re.compile(tp_ls[1])
    tg_lines = list()
    for txtline in txtlines:
        txtchain = txtline.split('\t')
        if txtchain[2] == 'S' and p.search(txtchain):
            tg_lines.append(txtline)
    with open(tp_ls[0]+'.txt', 'w') as w3:
        w3.writelines(tg_lines)
    