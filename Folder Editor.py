import os , sys
path = "E:/Practice/test/"
# os.renames(new="E:\\Practice\\test\\Sun ice mode.jpg" , old = "E:\\Practice\\test\\Sun ice mode.jpg")

directory = os.listdir(path)

def itmecounter(list):
    length = 0
    for itm in list:
        length += 1
    return  length
i = 0
for itm in directory:
    i+=1
    str(itm)
    print(f"{itm} renaming to {i}")
    os.renames(old=f"E:\\Practice\\test\\{itm}" , new=f"E:\\Practice\\test\\{str(i)}.jpg")
    print(f"renamed to {itm}")
