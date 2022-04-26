content = ""
f = open("GTAfiles.txt", "w")
import os
racine = input("Emplacement racine (X:/.../GTA5) :")
for root, dirs, files in os.walk(racine):
     for file in files:
         content += root+"\\"+file+"\n"
         print(root+"\\"+file)
f.write(content)
f.close()
