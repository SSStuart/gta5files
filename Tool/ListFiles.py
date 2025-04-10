content = ""
import os
racine = input("Emplacement racine (X:/.../GTA5) :")
f = open("GTAfiles.txt", "w")
for root, dirs, files in os.walk(racine, True, None, True):
     for file in files:
         content += root+"\\"+file+"\n"
         print(root+"\\"+file)
f.write(content)
f.close()