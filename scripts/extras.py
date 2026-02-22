""" Using Button function """
    ## Left Buttons
    # btn0 = Button(screen, L_btns_startX, btns_startY, 100, 40, text="Button 1", onClick = lambda: sel_feature(0), **buttonArgs)
    # btn1 = Button(screen, L_btns_startX, btns_startY + btn_spacingY, 100, 40, text="Button 2", onClick = lambda: sel_feature(1), **buttonArgs)
    # btn2 = Button(screen, L_btns_startX, btns_startY + btn_spacingY*2, 100, 40, text="Button 3", onClick = lambda: sel_feature(2), **buttonArgs)

    ## Right Buttons
    # btn3 = Button(screen, L_btns_startX + btns_spacingX, btns_startY, 100, 40, text="Button 4", **buttonArgs)
    # btn4 = Button(screen, L_btns_startX + btns_spacingX, btns_startY + btn_spacingY, 100, 40, text="Button 5", **buttonArgs)
    # btn5 = Button(screen, L_btns_startX + btns_spacingX, btns_startY + btn_spacingY*2, 100, 40, text="Button 6", **buttonArgs)

""" Using create_featureButton function with loop"""
    ## Left Buttons
    # for i in range(3):
    #     btn = create_featureButton(screen, L_btns_startX, btns_startY + btn_spacingY*i, "Button " + str(i), i)
    #     buttonList.append(btn)
    # for i in range(3):
    #     btn = create_featureButton(screen, L_btns_startX + btns_spacingX, btns_startY + btn_spacingY*i, "Button " + str(i+3), i+3)
    #     buttonList.append(btn)
        
    ## Right Buttons
    # for i in range(3):
    #     btn = create_featureButton(screen, R_btns_startX, btns_startY + btn_spacingY*i, "Button " + str(i+6), i+6)
    #     buttonList.append(btn)
    # for i in range(3):
    #     btn = create_featureButton(screen, R_btns_startX + btns_spacingX, btns_startY + btn_spacingY*(i), "Button " + str(i+9), i+9)
    #     buttonList.append(btn)

""" Button images path and loading without loop """

    # button_path = os.path.join("assets", "images", "button_images", "buttonBox_inactive.png")
    # buttonHover_path = os.path.join("assets", "images", "button_images", "buttonBox_hover.png")
    # buttonPress_path = os.path.join("assets", "images", "button_images", "buttonBox_press.png")
    # button_img = pg.image.load(button_path)
    # buttonHover_img = pg.image.load(buttonHover_path)
    # buttonPress_img = pg.image.load(buttonPress_path)

    # styleBox_path = os.path.join("assets", "images", "button_images", "styleBox_inactive.png")
    # styleBoxHover_path = os.path.join("assets", "images", "button_images", "styleBox_hover.png")
    # styleBoxPress_path = os.path.join("assets", "images", "button_images", "styleBox_press.png")
    # styleBox_img = pg.image.load(styleBox_path)
    # styleBoxHover_img = pg.image.load(styleBoxHover_path)
    # styleBoxPress_img = pg.image.load(styleBoxPress_path)

""" Using list comprehension to create lists for styles and images """
    # styleImageList = [None]
    # for name in styleNames:
    #     path = os.path.join("assets", "images", "character_images", name + "_front.png")
    #     img = pg.image.load(path)
    #     styleImageList.append(img)

    # button_imgList = []
    # for modeName in buttonModeList:
    #     path = os.path.join("assets", "images", "button_images", "buttonBox" + modeName)
    #     img = pg.image.load(path)
    #     button_imgList.append(img)

    # styleBox_imgList = []
    # for modeName in buttonModeList:
    #     path = os.path.join("assets", "images", "button_images", "styleBox" + modeName)
    #     img = pg.image.load(path)
    #     styleBox_imgList.append(img)

    # for modeName in buttonModeList:
    #     path = os.path.join("assets", "images", "button_images", "smallColorBox" + modeName)
    #     img = pg.image.load(path)
    #     smallColorBox_imgList.append(img)

    # for n in range(12):
    #     styleImg = ch.styleImageList[bF.feature].subsurface(pg.Rect(ch.returnCrop(n),(144,240)))
    #     scaledImg = pg.transform.scale(styleImg, (72, 120))
    #     previewImgList.append(scaledImg)

""" Flip Button code """
    # flipButton_imgList = [pg.image.load(os.path.join("assets", "images", "button_images", "flipButton" + modeName)) for modeName in buttonModeList]

    # def set_flip(Bool=None):
    #     global flipSprite
    #     if not Bool == None:
    #         flipSprite = Bool
    #     else:
    #         flipSprite = not flipSprite
    #     print("Flipped:", flipSprite)

    # def create_flipButton(surface, xPos, yPos, buttonText) -> Button:
    #     """
    #     Returns a button that changes the selected feature when clicked
        
    #     :param surface: Surface to place button on
    #     :type surface: pygame.Surface
    #     :param xPos: X-coordinate of the top left corner
    #     :type xPos: int
    #     :param yPos: Y-coordinate of the top left corner
    #     :type yPos: int
    #     :param buttonText: Text of display on button
    #     :type buttonText: str
    #     :param ftN: Number of the feature to set
    #     :type ftN: int
    #     :return: A py_widget button with the given properties
    #     :rtype: Button
    #     """
    #     buttonArgs = {"fontSize": 25, "image": flipButton_imgList[0], "onHoverImage": flipButton_imgList[1], "onPressImage": flipButton_imgList[2]}
    #     button = Button(surface, xPos, yPos, 70, 70, radius=10, text=buttonText, onClick=set_flip, **buttonArgs)
    #     return button