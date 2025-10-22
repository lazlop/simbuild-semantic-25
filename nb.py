from semantic_mpc_interface import (
    LoadModel,
    get_thermostat_data,
    HPFlexSurvey,
    convert_units,
    SHACLHandler,
    inline_shapes
)
from semantic_mpc_interface.utils import query_to_df
from buildingmotif.namespaces import BRICK, RDF, S223
from rdflib import URIRef
from buildingmotif import BuildingMOTIF
from buildingmotif.dataclasses import Library
import csv
from pyshacl.rdfutil import clone

# SELECT ONTOLOGY 
ontology = 'brick'

# base path
base_path = f'{ontology}'


# Please disregard excessive outputs (logging and warnings) from bmotif
import logging
logging.disable(logging.CRITICAL)
import warnings
warnings.filterwarnings("ignore")

handler = SHACLHandler(ontology=ontology, template_dir = 'C:/Users/btuser/Documents/LBNL_work_folder/semantic_s223/simbuild-semantic-25/templates/')

# Generate shapes
handler.generate_shapes()

# Save shapes
handler.save_shapes(f'{base_path}/shapes.ttl')
# also save more human readable shapes
inline_shapes(handler.shapes_graph).serialize(f"{base_path}/inlined_shapes.ttl")