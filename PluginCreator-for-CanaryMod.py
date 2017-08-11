import sys
import os

noTest = True

name=input("name:")
Name=input("Name:")
version=input("Version:")
path="C:/Users/David Kaiser/Documents/IdeaProjects/"+Name+"/src/"+Name
os.makedirs(path)
canary=open("C:/Users/David Kaiser/Documents/IdeaProjects/"+Name+"/Canary.inf","w")
canary.write("main-class = "+name+"."+Name+"\nname = "+Name+"\nauthor = David Kaiser\nversion = "+version)
canary.close
IDEA=open(path+"/"+Name+".java","w")
IDEA.close
Man=open("C:/Users/David Kaiser/Documents/IdeaProjects/"+Name+"/Manifest.txt","w")
Man.write("Class-Path: ../lib/EZPlugin.jar\n\n")
Man.close
