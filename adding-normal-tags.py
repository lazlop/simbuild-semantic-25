from rdflib import Graph
g = Graph()
g.parse('post-processed-model.ttl', format = 'ttl')
from semantic_mpc_interface.namespaces import *

# adding new external reference 
for s in g.subjects(REF.hasExternalReference,REF.BOPTestReference):
    print(s)


# g.serialize('post-processed-model-normal.ttl', format = 'ttl')