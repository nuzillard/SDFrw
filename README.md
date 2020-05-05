# SDFrw
 Python module for the handling of MDL SDF files.

## Description
sdfrw.py provides the following functions:

- sdfReader(fh) yields compounds stored in an opened sdf file (this is an iterator, not a function)
- sdfWrite(fh, mol) that writes a single compound, mol, to a previously opened text file accessed to by file handle fh
- sdfTransform(filenameIn, filenameOut, transformation=defaultTransformation) that reads molecules,
transforms them, and writes them in an other file. The defaultTransformation leaves compounds unchanged.
- sdfHasProp(mol, sdfprop) --> Boolean
- sdfGetPropList(mol) --> List of strings
- sdfGetProp(mol, sdfprop) --> String
- sdfClearProp(mol, sdfprop) --> molecule
- sdfClearAllProps(mol) --> molecule
- sdfSetChangeProp(mol, sdfprop, sdfvalue) --> (Boolean, molecule)
- sdfSetNoChangeProp(mol, sdfprop, sdfvalue) --> (Boolean, molecule)
- sdfEmptyMol() --> molecule
- sdfGetMolBlock(mol) --> String
- sdfSetMolBlock(mol, molblock) --> molecule
- sdfGetTitle(mol) --> String
- sdfChangeTitle(mol, newtitle) --> molecule

sdfrw.py does not depend on any toolkit of cheminformatic functions.

Reading and writing .sdf files with molecule storage as a dictionary with two keys:
- "molblock", giving access to the molblock without the final '\n' and
- "keyvals", giving access to a list of pairs, the first value is a sdf property name
and the second value is a whole property and value text without the final '\n\n'.

## Testing

`python demo.py`

"demo.py" performs a few transformation on file "flavonoids.sdf", writes the result in file "qualified_flavonoids.sdf",
and then queries molecules for the value of the No_CE property.

Demo_result\ contains "qualified_flavonoids.sdf" and "demo_printout.txt", a copy of the text sent to the terminal.

`python updater.py` prints what to do with "updater.py".

Updater_result\ contains "flavonoids_updated.sdf", the result of

`python updater.py Name flavonoid_names.txt < flavonoids.sdf > flavonoids_updated.sdf`

that sets or resets Name property in "flavonoids.sdf" with values from "flavonoid_names.txt"

`python copy.py < fileIn.sdf > fileOut.sdf`

copies "fileIn.sdf" to "fileOut.sdf " with short tag-name lines, such as `>  <idx>`
