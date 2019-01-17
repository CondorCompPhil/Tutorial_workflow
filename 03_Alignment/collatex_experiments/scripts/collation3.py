#!usr/bin/env python
# -*- coding: utf-8 -*-

import collatex
from collatex.edit_graph_aligner import *
from collatex.core_classes import *
from collatex.near_matching import *
from lxml import etree
import json
from fonctions2 import *

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

layout="horizontal"
scheduler=Scheduler()

collation = json_input
json_collation = Collation()
for witness in collation["witnesses"]:
    json_collation.add_witness(witness)
collation = json_collation

algorithm = EditGraphAligner(collation)#, near_match=TRUE)
# build graph
graph = VariantGraph()
algorithm.collate(graph, collation)
ranking = VariantGraphRanking.of(graph)
highestRank = ranking.byVertex[graph.end]
witnessCount = len(collation.witnesses)
# do-while loop to avoid looping through ranking while modifying it
rank = highestRank - 1
condition = True
while condition:
    rank = process_rank(scheduler, rank, collation, ranking, witnessCount)
    rank -= 1
    condition = rank > 0

# join parallel segments
#TODO: à éclaircir
#join(graph)/home/jbc
ranking = VariantGraphRanking.of(graph)
# check which output format is requested: graph or table
table = AlignmentTable(collation, graph, layout, ranking)

result = table_to_xml(table)

f = open('results3.xml', 'w')
print(result, file=f)
f.close()

