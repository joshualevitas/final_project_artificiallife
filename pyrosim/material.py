from pyrosim.commonFunctions import Save_Whitespace

class MATERIAL: 

    def __init__(self, color =  'Cyan', rgba = ["0", "1.0", "1.0", "1.0"]):

        self.depth  = 3

        self.string1 = '<material name="{}">'.format(color)

        self.string2 = '    <color rgba="{} {} {} {}"/>'.format(rgba[0],rgba[1],rgba[2],rgba[3])

        self.string3 = '</material>'

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )
