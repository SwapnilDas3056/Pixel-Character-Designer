import pygame as pg

colList_skins = []

startColors_skins = [[pg.Color(255,240,240), (6, 10, 15)], [pg.Color(255,240,200), (0, 8, 12)], [pg.Color(240,182,160), (15, 12, 10)], [pg.Color(150,110,100), (15, 12, 10)]]
for i in range(4):
    for j in range(6):
        rShift, gShift, bShift = startColors_skins[i][1]
        col = startColors_skins[i][0] - pg.Color(j*rShift,j*gShift,j*bShift)
        colList_skins.append(col)

whiteBlack = [pg.Color(255,255,255), (63,63,63)]
browns =  [pg.Color(200,160,120), (27, 42, 52)]
yellowRed = [pg.Color(255,255,0), (0, 50, 0)]
greens = [pg.Color(200,255,150), (50, 38, 37)]
blues = [pg.Color(150,255,255), (37, 63, 26)]
pinkPurple = [pg.Color(255,200,255), (46, 50, 26)]
startColors_styles = [whiteBlack, browns, yellowRed, greens, blues, pinkPurple]

colList_styles = []

for j in range(5):
    for i in range(6):
        rShift, gShift, bShift = startColors_styles[i][1]
        col = startColors_styles[i][0] - pg.Color(j*rShift,j*gShift,j*bShift)
        colList_styles.append(col)

def palette_swap(surface: pg.Surface, newCol: pg.Color, mode="white"):
    img = surface.copy()
    R = newCol.r
    G = newCol.g
    B = newCol.b
    newCol.a = 255
    
    newCol1 = pg.Color(R,G,B) - pg.Color(30,30,30)
    newCol1.a = 255
    newCol2 = pg.Color(R,G,B) - pg.Color(60,60,60)
    newCol2.a = 255
    
    if mode == "white":
        with pg.PixelArray(img) as pixelarr:
            pixelarr.replace(pg.Color(255,255,255,255), newCol)
        with pg.PixelArray(img) as pixelarr:
            pixelarr.replace(pg.Color(170,170,170,255), newCol1)
        with pg.PixelArray(img) as pixelarr:
            pixelarr.replace(pg.Color(85,85,85,255), newCol2)
    elif mode == "gray":
        with pg.PixelArray(img) as pixelarr:
            pixelarr.replace(pg.Color(170,170,170,255), newCol)
        with pg.PixelArray(img) as pixelarr:
            pixelarr.replace(pg.Color(85,85,85,255), newCol1)
    elif mode == "black":
        with pg.PixelArray(img) as pixelarr:
            pixelarr.replace(pg.Color(0,0,0,255), newCol)
    
    return img