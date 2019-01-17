#!usr/bin/env python
# -*- coding: utf-8 -*-

from collatex import *
from lxml import etree
import json
from fonctions import *

#Création des témoins
#import A F G H M P R S V
A = open('A.xml').read()
A = etree.XML(A)
F = open('F.xml').read()
F = etree.XML(F)
G = open('G.xml').read()
G = etree.XML(G)
H = open('H.xml').read()
H = etree.XML(H)
M = open('M.xml').read()
M = etree.XML(M)
P = open('P.xml').read()
P = etree.XML(P)
R = open('R.xml').read()
R = etree.XML(R)
S = open('S.xml').read()
S = etree.XML(S)
V = open('V.xml').read()
V = etree.XML(V)


#Add A F G H M P R S V to input
json_input = {}
json_input['witnesses'] = []
json_input['witnesses'].append(XMLtoJson('A',A))
json_input['witnesses'].append(XMLtoJson('F',F))
json_input['witnesses'].append(XMLtoJson('G',G))
json_input['witnesses'].append(XMLtoJson('H',H))
json_input['witnesses'].append(XMLtoJson('M',M))
json_input['witnesses'].append(XMLtoJson('P',P))
json_input['witnesses'].append(XMLtoJson('R',R))
json_input['witnesses'].append(XMLtoJson('S',S))
json_input['witnesses'].append(XMLtoJson('V',V))

#collate(json_input, output="table", layout="horizontal", segmentation=True, near_match=False, astar=False,
#            detect_transpositions=False, debug_scores=False, properties_filter=None, svg_output=True, indent=False)

result = collate(json_input, output="table", layout="vertical", segmentation=False,near_match=True)#,svg_output=True)

f = open('results2.table', 'w')
print(result, file=f)
f.close()

result = collate(json_input, output="tei", segmentation=False,near_match=True)

f = open('results2_tei.xml', 'w')
print(result, file=f)
f.close()

result = collate(json_input, output="xml", segmentation=False,near_match=True)

f = open('results2.xml', 'w')
print(result, file=f)
f.close()

result = collate(json_input, output="json", segmentation=False,near_match=True)

f = open('results2.json', 'w')
print(result, file=f)
f.close()

#result = collate(json_input, output="svg", segmentation=False,near_match=True)
