# Minimal Brick Example 

These files are a minimal example of a 231 controller on a brick ontology building with 223 function blocks, based on the simbuild 25 paper example with some trimming and cleanup. 

**1. building.ttl:** This is a brick model for a single zone of a VAV system from the BOPTest simple office air building. It is trimmed down from the 5 zone model, and some external references were removed for both BOPtest and the normal platform. We may want to add new external references for BACnet for this example. 

**2. controls-231.ttl:** This is a ttl serialized CXF export for the demand flexibility ratcheting controller. This was slightly cleaned up by editing prefixes. I have left in all the parameters, schedules, etc. which we may choose to remove for the purpose of this example. 

**3. controls-implemented.ttl:** This defines the CXF exports according to s223 function concepts, and links them to points in the building model 

To clarify the differences between our approach in the paper and the minimal example, some additional files are included in this directory. If we want to set up a more advanced example configuring controls using 231/brick, we may build off of these. 

The below files are specific to the workflow we did for setting up controls in the Normal platform. We are experimenting with some approaches leveraging templates, shapes, and inference to create application specific data models. These application specific data models are similar to the object oriented approach we investigated in NAWI, and the G36 extension for S223. 

The new files we created have shapes that define the controller and controls IO according to s223 concepts and brick classes. The files also includes some simple properties to specify how an implemented controller should relate to these shapes. These were used to create controller configurations for the Normal platform. Because the controllers were created in Normal, we are missing individual functions/function blocks that represent the fully configured controlers for each zone. 

 - extra_controls-223.ttl: This defines shapes for the CXF controller. These shapes describe IO for the controller, how each IO should relate to points, the brick classes, qudt units, and ext. references of these points, and how an entity of focus (e.g. a zone) relates to these points. This is the application specific data model. It serves the same function as a SPARQL query, but the fragments are reusable and machine readable. It was automatically generated based on BMotif templates, so it is not pretty. I cleaned up some of the external reference related shapes and 'inlined' the shapes to improve readability. By 'inlining' I mean that if there was a tree structure I got rid of subject nodes and used blank nodes instead. There is code not in this repo used for querying the data into a dictionary based on these shapes.

 - extra_controls-specified.ttl: This file links the CXF controller nodes to the 223 shapes that define how they should be implemented. 
This file also defines two new properties in a new namespace (OBC): 'obc:binds' and 'obc:controls'. These properties are used to treat the controller not as one discrete IO controller, but as a template for other controllers, or as function logic that can have different groups of inputs and outputs, which is how Normal works. 
'obc:controls' relates the controller to the shape of entity it is related to (e.g. obc:zone). This entity links to all the points relevant to the IO, using paths specified in the shapes. 'obc:binds' relates controller IO to the shapes of brick point it should relate too. 
The obc:binds relationship is redundant with the some information in the SHACL shapes, which already describes how the function IO should relate to the data in the building model, but I think having it explicit improves clarity. 


