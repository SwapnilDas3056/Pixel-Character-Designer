import pygame as pg
import os

base_front_path = os.path.join("assets", "images", "character_images", "Base_front.png")
base_front_img = pg.image.load(base_front_path)

styleNames = ["backHair", "faceAcc", "eyes", "frontHair", "headAcc", "shirt", "shirtDesign", "pant", "coat", "neck", "shoes"]
styleImageList = [None]+[pg.image.load(os.path.join("assets", "images", "character_images", name + "_front.png")) for name in styleNames]

featureNames = ["Skin", "Back Hair", "Face Acc.", "Eyes", "Front Hair", "Head Acc.", "Shirt", "Shirt\nDesign", "Pant", "Coat", "Neck", "Shoes"]
shapeList = [(6,3), (4,3), (4,1), (4,3), (4,3), (4,2), (4,3), (4,3), (4,3), (4,3), (4,2), (4,2)]
longBoolList = [False,True,False,False,False,False,False,False,False,False,False,False]
resizeList = [(0.8,+2,-19), (1,-6,-30), (1.6,-27.5,-70), (1,-6,-20), (0.8,+2,+5), (1,-6,-60), (1,-6,-60), (1,-6,-65), (1,-6,-62), (1,-6,-50), (1,-6,-70)]
colorModeList = ["white","black","gray","white","gray","gray","black","gray","gray","black","gray"]

featureDict = {"Feature Name": featureNames, "Style Images": styleImageList, "Style Array Shape": shapeList, 
               "Style Box Long": longBoolList, "Resize": resizeList, "Color Mode": colorModeList}

def returnCrop(stN):
    leftPoint = 144*(stN%4)
    topPoint = 240*0
    if 4 <= stN <= 7:
        topPoint = 240*1
    elif stN >= 8:
        topPoint = 240*2
    return (leftPoint, topPoint)