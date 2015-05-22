#######
# File name: placeholderx.rpy
# 
# Description: Implements a different Placeholder(), showing the first image
# with notes if the second image is not present. Second image otherwise.
# 
# Original author: Nolan/NintendoToad
# 
# Type: Library
# 
# Usage:
#     image IMGNAME = PlaceholderX(String, String, **Etc)
#######

init -1 python:
    import os
    from get_image_size import get_image_size, UnknownImageFormat, BadFile
    
    #####
    # Function name: Resize()
    # 
    # Description: Somewhat-intelligently resize an image. Basically a macro for
    # im.scale with more math. Ratio only works for downscaling.
    # 
    # Parameters:
    # image - location of the image
    # width - either pixel width or ratio for scaling both width and height
    # height - pixel height
    # 
    # Returns: the transformed image
    #####
    # http://www.renpy.org/doc/html/displayables.html#im.Scale
    def Resize(image, width, height=-1, bilinear=True, **properties):
        # get the actual image width and height
        setloc = os.path.abspath(config.gamedir + "/" + image)
        try:
            truwidth, truheight = get_image_size(setloc)
        except UnknownImageFormat:
            # passthrough if the image exists and worked
            return Image(image)# make someone else deal with it.
        renpy.log("Resize Parameters: " + str(truwidth) + " " + str(truheight))
        ###
        
        # ratio case, width is the ratio
        if(width > 0.0 and width < 1.0):
            ratio = width
            width = int(truwidth * ratio)
            height = int(truheight * ratio)
            renpy.log("Resize Attempt: " + str(width) + " " + str(height))
            return im.Scale(image, width, height, bilinear, *properties)
        ###
        
        # width without height case - scale to width
        if(height == -1):
            # multiply things by ratio
            ratio = width / truwidth
            height = int(truheight * ratio)
            renpy.log("Resize Attempt: " + str(width) + " " + str(height))
            return im.Scale(image, width, height, bilinear, *properties)
        ###
        
        # height without width case - scale to height
        if(width == -1):
            # multiply things by ratio
            ratio = height / truheight
            width = int(truwidth * ratio)
            renpy.log("Resize Attempt: " + str(width) + " " + str(height))
            return im.Scale(image, width, height, bilinear, *properties)
        ###
        
        return Image(image)# make someone else deal with it.
    

    
    #####
    # Class name: PlaceholderX()
    # 
    # Description: Be a write-once placeholder - in other words, show a placeholder image
    # only if the "actual" image does not exist. Do other fancy stuff, like with debug text.
    # 
    # Parameters:
    # img1 - the placeholder
    # img2 - the real image
    # tsize - size of debug text
    # tcolor - color of debug text
    # talign - x, y alignment of debug text within the image
    # pretext - text to show before the standard debug text
    # 
    # Returns: the transformed image
    #####
    class PlaceholderX(renpy.Displayable):

        def after_setstate(self):
            self.build = None

        def __init__(self, img1, img2, tsize=12, tcolor="#000", talign=(0.0, 0.0), pretext = "", **properties):
            super(PlaceholderX, self).__init__(**properties)
            self.img1 = img1
            self.img2 = img2
            self.tsize = tsize
            self.tcolor = tcolor
            self.talign = talign
            self.pretext = pretext
            self.build = None
            self.verify()

        def verify(self):
            # throw a hissy-fit if the neither image exists
            loc1 = os.path.abspath(config.gamedir + "/" + self.img1)
            loc2 = os.path.abspath(config.gamedir + "/" + self.img2)
            if((not os.path.isfile(loc1)) and (not os.path.isfile(loc2))):
                renpy.error("PlaceholderX requires that at least one of the images \
 actually exist. Check: %s" % loc2)

        #####
        # Function name: build_image()
        # 
        # Description: Actually assemble a new Image() object
        # 
        # Parameters:
        # self - the current object
        # 
        # Returns: the transformed image
        #####
        def build_image(self):
            # If already built, STFU and move on
            if self.build:
                return self.build
            
            # Check both images
            loc1 = os.path.abspath(config.gamedir + "/" + self.img1)
            loc2 = os.path.abspath(config.gamedir + "/" + self.img2)
            
            # Show second image if available
            # Clear text because correct image
            if(os.path.isfile(loc2)):
                setimage = self.img2
                setloc = loc2
                text = ""
            # First image otherwise
            # Generate text if wrong image
            else:
                # throw a hissy-fit if the neither image exists
                self.verify()
                setimage = self.img1
                setloc = loc1
                text = self.pretext + " ".join(self.name) + ": " + self.img2
            
            # Do damnedest to get image parameters
            try:
                width, height = get_image_size(setloc)
            except UnknownImageFormat:
                width, height = -1, -1

            # Scale text position to given text alignment and image parameters
            size = ((width), (height))
            textpos = (int(width * self.talign[0]), int(height * self.talign[1]))
            
            # Build the current version of the image
            placeheld = Fixed(
                Image(setimage),
                Text(text, pos=textpos, xanchor=self.talign[0], yanchor=self.talign[1], style="_default", color=self.tcolor, text_align=0.0, size = self.tsize),
                xysize=size,
            )

            self.build = placeheld
            return placeheld
        
        #####
        # Function name: parameterize()
        # 
        # Description: Parameterize the image without using image.py's
        # parameterize() call.
        # 
        # Parameters:
        # self - the current object
        # name - the base name of the image
        # paramaters - etcetera for the image
        # 
        # Returns: the transformed image with new parameters
        #####
        def parameterize(self, name, parameters):
            placeheld = PlaceholderX(self.img1, self.img2, self.tsize, self.tcolor, self.talign, self.pretext)
            placeheld.name = list(name) + list(parameters)
            return placeheld

        # Be prepared for Callbacks
        def visit(self):
            return [ self.build_image() ]

        # Hold the complete image
        def render(self, width, height, st, at):
            build = self.build_image()
            return renpy.render(build, width, height, st, at)
            