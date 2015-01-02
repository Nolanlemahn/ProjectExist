#######
# File name: placeholderx.rpy
# 
# Description: Implements a different Placeholder(), showing the first image
# with notes if the second image is not present. Second image otherwise.
# 
# Original author: Nolan/NintendoToad
# 
# Type: Library
# Usage:
#     image IMGNAME = PlaceholderX(String, String, **Etc)
#######

init -1 python:
    import os
    from get_image_size import get_image_size, UnknownImageFormat, BadFile
    
    # pseudo-macro for im.Scale
    # http://www.renpy.org/doc/html/displayables.html#im.Scale
    def Resize(image, width, height, bilinear=True, **properties):
        return im.Scale(image, width, height, bilinear, *properties)
    
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
            
        #####
        # Function name: build_image()
        # 
        # Descripiton: Actually assemble a new Image() object
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
        # Descripiton: Parameterize the image without using image.py's
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
            