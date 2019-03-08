# VASP_Simulation_Automation
Generates different combinations of atom positions within a position (POSCAR) file, rotates and manipulates position vectors using numpy

# Usage
## For Natrolite:
Generating possible orientations for a water molecule located at a hydration site (x,y,z) in cartesian coordinates:
 1. Create a template POSCAR file 
    ```
    Natrolite
    1.0
         18.2999992371         0.0000000000         0.0000000000
          0.0000000000        18.6299991608         0.0000000000
          0.0000000000         0.0000000000         6.5999999046
     Na   Si   Al    O   H
     16   24   16   81   2
     Cartesian
     ...
     ... (positions)
     ...
     ```
   Don't include the positions of atoms to be included in the template POSCAR file. 
   i.e. if we're adding atom 4 to atoms 1, 2, and 3, exclude atom 4 from the template file
   
   However, do include this atom when listing the number of atoms per element.
   
   Save this file as template.vasp in your root folder.
   
  2. Generating all possible POSCAR files:
    navigate to the root folder (wherever nat_h_pos.py and combinations_rotations.py are)
    
    ` python nat_h_pos.py x y z foldername ` 
    
    All possible POSCARs will be stored in "foldername"
    
 ## For any other zeolite with known hydration sites 
 1. Replace the framework_o_pos in nat_h_pos.py with the positions of oxygen atoms in your preferred zeolite
 2. Create template.vasp and run nat_h_pos.py as specified in the "For Natrolite" section
     
