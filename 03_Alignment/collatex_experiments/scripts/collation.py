#!usr/bin/env python
# -*- coding: utf-8 -*-

from collatex import *
import json

JSON_data = open('Corpus3500-3600.JSON').read()
collation = json.loads(JSON_data)
result = collate(collation, output="tei", indent=True, segmentation=False, near_match=True, detect_transpositions=True)
#collate(collation, output="table", layout="horizontal", segmentation=True, near_match=False, astar=False,  detect_transpositions=False, debug_scores=False, properties_filter=None, svg_output=None, indent=False, scheduler=Scheduler()):

#Parmi ces options, 
# # Valid options for output are:
# "table" for the alignment table (default)
# "graph" for the variant graph
# "json" for the alignment table exported as JSON
# "xml" for the alignment table as pseudo-TEI XML
#   All columns are output as <app> elements, regardless of whether they have variation
#   Each witness is in a separate <rdg> element with the siglum in a @wit attribute
#       (i.e, witnesses with identical readings are nonetheless in separate <rdg> elements)
# "tei" for the alignment table as TEI XML parallel segmentation (but in no namespace)
#   Wrapper element is always <p>
#   indent=True pretty-prints the output
#       (for proofreading convenience only; does not observe proper white-space behavior)

#astar correspond à l'experimental astar (a* ) aligner, cf. https://en.wikipedia.org/wiki/A*_search_algorithm

f = open('results.xml', 'w')
print(result, file=f)
f.close()

#result = collate_pretokenized_json( JSON_input, output='table' ) #With pretokenized_json

