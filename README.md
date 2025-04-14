obj_loader_via_vpython
=

As we know vpython doesnt support any 3d model rendering rather than normal shapes. this program actually make things easy to render.

It is a project for loading and displaying an obj file in vpython using its triangle and quads to make a compound object.

An obj file contains all information about any 3d object in the form of following parameters:

   Vertices
   
   Normals
   
   Texture positions
   
   Faces __ (in the format "vertex/texpos/normal")
   

For display any obj file ,you need to place it in the obj_files folder ,and run following command

<pre> python obj_loader.py</pre>

and after this ,select your uploaded obj file in program

Ex:
<pre>
1) car.obj
2) building.obj

>> 1
</pre>


![Screenshot from 2024-01-24 05-15-53](https://github.com/rishabh-source/obj_loader_via_vpython/assets/70832073/fa0c098b-4926-4606-85aa-af61f44e0b85)
![Screenshot from 2024-01-24 05-17-52](https://github.com/rishabh-source/obj_loader_via_vpython/assets/70832073/29262fa3-f2ad-41e7-8700-0a39ffcf1d7b)
![Screenshot from 2024-01-24 05-16-51](https://github.com/rishabh-source/obj_loader_via_vpython/assets/70832073/844124c1-48dc-41a8-af4c-eddcd6a902b8)

![Screenshot from 2024-01-24 05-17-16](https://github.com/rishabh-source/obj_loader_via_vpython/assets/70832073/d74ad62c-f23d-4517-9f9c-0ac9af6495e3)


Requirements:
=

python 3.9 

vpython 7.6

