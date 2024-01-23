import glob
# All files and directories ending with .obj and that don't begin with a dot:
all_obj=glob.glob("obj_files/*.obj")
no_of_files=1
dict = {0:"hi"}
for fle in all_obj:
    flespl=fle.split("/")
    print(no_of_files,")",flespl[len(flespl)-1])
    dict[no_of_files]= fle
    no_of_files=no_of_files+1
    
select= int(input())
name=dict[select]
