
import obj_file_detector
from vpython import*
from math import*
from time import*
file_name=obj_file_detector.name
f=open(file_name,'r')
scene=canvas(width=1600, height=720, background=color.black)
s=f.read()
lst=s.split()
objects=[]

vs=[]
vns=[]
fs=[]
ss=[]
vts=[]

# loading faces,vertices etc in lists

for a in range(len(lst)):
    if (lst[a] not in ["v","vn","f","s","vt"]):
        continue
    else :
        if (lst[a]=="v"):
            vs.append([float(lst[a+1]),float(lst[a+2]),float(lst[a+3])])
        elif (lst[a]=="vn"):
            vns.append([float(lst[a+1]),float(lst[a+2]),float(lst[a+3])])
        elif (lst[a]=="f"):
            three_size=[]
            for pos in range(1,5):
                if (len(lst)<=a+pos):
                    continue
                if ( len(lst[a+pos])==0  or lst[a+pos][0].isnumeric()==False):
                    continue
                temp=lst[a+pos].split("/")
                a1=int(temp[0])
                a2=int(temp[1])
                a3=int(temp[2])
                three_size.append([a1,a2,a3])
            fs.append(three_size)



            
# implementation of vertices,normal of vertices ,texpos,faces

for one_face in fs:
    if (len(one_face)==3):
        pos1=vs[one_face[0][0]-1];norm1=vns[one_face[0][2]-1]#;tex1=vts[one_face[0][1]-1]
        pos11=pos1[0];pos12=pos1[1];pos13=pos1[2]
        norm11=norm1[0];norm12=norm1[1];norm13=norm1[2]
        #tex11=tex1[0];tex12=tex[1];tex13=tex1[2]
        a=vertex( pos=vec(pos11,pos12,pos13),normal=vec(norm11,norm12,norm13),color=color. white )

        pos2=vs[one_face[1][0]-1];norm2=vns[one_face[1][2]-1]#;tex2=vts[one_face[1][1]-1]
        pos21=pos2[0];pos22=pos2[1];pos23=pos2[2]
        norm21=norm2[0];norm22=norm2[1];norm23=norm2[2]
        #tex21=tex2[0];tex22=tex2[1];tex23=tex2[2]
        b=vertex( pos=vec(pos21,pos22,pos23),normal=vec(norm21,norm22,norm23),color=color. white )

        pos3=vs[one_face[2][0]-1];norm3=vns[one_face[2][2]-1]#;tex3=vts[one_face[2][1]-1]
        pos31=pos3[0];pos32=pos3[1];pos33=pos3[2]
        norm31=norm3[0];norm32=norm3[1];norm33=norm3[2]
        #tex31=tex3[0];tex32=tex3[1];tex33=tex3[2]
        c=vertex( pos=vec(pos31,pos32,pos33),normal=vec(norm31,norm32,norm33),color=color. white )

        t=triangle(v0=a,v1=b,v2=c) # it is for triangle

        objects.append(t)
        
    elif (len(one_face)==4):
        
        pos1=vs[one_face[0][0]-1];norm1=vns[one_face[0][2]-1]#;tex1=vts[one_face[0][1]-1]
        pos11=pos1[0];pos12=pos1[1];pos13=pos1[2]
        norm11=norm1[0];norm12=norm1[1];norm13=norm1[2]
        #tex11=tex1[0];tex12=tex1[1];tex13=tex1[2]
        a=vertex( pos=vec(pos11,pos12,pos13),normal=vec(norm11,norm12,norm13),color=color. white )

        pos2=vs[one_face[1][0]-1];norm2=vns[one_face[1][2]-1]#;tex2=vts[one_face[1][1]-1]
        pos21=pos2[0];pos22=pos2[1];pos23=pos2[2]
        norm21=norm2[0];norm22=norm2[1];norm23=norm2[2]
        #tex21=tex2[0];tex22=tex2[1];tex23=tex2[2]
        b=vertex( pos=vec(pos21,pos22,pos23),normal=vec(norm21,norm22,norm23),color=color. white )

        pos3=vs[one_face[2][0]-1];norm3=vns[one_face[2][2]-1]#;tex3=vts[one_face[2][1]-1]
        pos31=pos3[0];pos32=pos3[1];pos33=pos3[2]
        norm31=norm3[0];norm32=norm3[1];norm33=norm3[2]
        #tex31=tex3[0];tex32=tex3[1];tex33=tex3[2]
        c=vertex( pos=vec(pos31,pos32,pos33),normal=vec(norm31,norm32,norm33),color=color. white )

        pos4=vs[one_face[3][0]-1];norm4=vns[one_face[3][2]-1]#;tex4=vts[one_face[3][1]-1]
        pos41=pos4[0];pos42=pos4[1];pos43=pos4[2]
        norm41=norm4[0];norm42=norm4[1];norm43=norm4[2]
        #tex41=tex4[0];tex42=tex4[1];tex43=tex4[2]
        d=vertex( pos=vec(pos41,pos42,pos43),normal=vec(norm41,norm42,norm43),color=color.white )

        q=quad(v0=a,v1=b,v2=c,v3=d) # it is for quad
        
        objects.append(q)

object_of_the_day=compound(objects)







            
        
