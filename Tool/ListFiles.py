content = ""
f = open("C:\\Users\\Dubromel Rémy\\Desktop\\GTAfiles.txt", "w")
import os
for root, dirs, files in os.walk('D:\Rockstar\Grand Theft Auto V'):
     for file in files:
         content += root+"\\"+file+"\n"
         print(root+"\\"+file)
f.write(content)
f.close()
