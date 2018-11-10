#!/usr/bin/env python

# These two lines are only needed if you don't put the script directly into
# the installation directory
import sys
sys.path.append('/usr/share/inkscape/extensions')

# We will use the inkex module with the predefined Effect base class.
import inkex
import math
# The simplestyle module provides functions for style parsing.
#from simplestyle import *

from liaisons_fonctions_utiles import *
from liaisons_pivot import *
from liaisons_pivot_glissant import *
from liaisons_glissiere import *



class Liaisons(inkex.Effect):
    """
    Example Inkscape effect extension.
    Creates a new layer with a "Hello World!" text centered in the middle of the document.
    """
    def __init__(self):
        """
        Constructor.
        Defines the "--what" option of a script.
        """
        # Call the base class constructor.
        inkex.Effect.__init__(self)

        # Define string option "--what" with "-w" shortcut and default value "World".
        #PRINCIPAL
        self.OptionParser.add_option('--onglets_pricipaux', action = 'store', type = 'string', dest = 'onglets_pricipaux', default = '', help = u"Choix de la liaison")
        
        #LIAISONS...
        self.OptionParser.add_option('--liaison', action = 'store', type = 'string', dest = 'liaison', default = '', help = u"Choix de la liaison")
        
        #LIAISON PIVOT ***************************************************
        self.OptionParser.add_option('--liaison_pivot_type', action = 'store', type = 'string', dest = 'liaison_pivot_type', default = 'liaison_pivot_2D_cote', help = u"Type de representation de la pivot")
        
        self.OptionParser.add_option('--liaison_pivot_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_pivot_2D_cote_x', default = '0', help = u"Position sur X de la liaison pivot 2D cote relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_pivot_2D_cote_y', default = '0', help = u"Position sur Y de la liaison pivot 2D cote relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot2D_cote_axe', action = 'store', type = 'string', dest = 'liaison_pivot2D_cote_axe', default = 'x', help = u"Principales directions de l'axe d'une pivot 2D vue de cote")
        self.OptionParser.add_option('--liaison_pivot2D_cote_orientation', action = 'store', type = 'float', dest = 'liaison_pivot2D_cote_orientation', default = '0', help = u"Orientation Pivot 2D en degres")

        self.OptionParser.add_option('--liaison_pivot_2D_face_x', action = 'store', type = 'float', dest = 'liaison_pivot_2D_face_x', default = 0, help = u"Position sur X de la liaison pivot 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_2D_face_y', action = 'store', type = 'float', dest = 'liaison_pivot_2D_face_y', default = 0, help = u"Position sur Y de la liaison pivot 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot2D_face_axe1', action = 'store', type = 'string', dest = 'liaison_pivot2D_face_axe1', default = 'x', help = u"Principales directions du bras 1 d'une pivot vue de face")
        self.OptionParser.add_option('--liaison_pivot2D_face_orientation1', action = 'store', type = 'float', dest = 'liaison_pivot2D_face_orientation1', default = '0', help = u"Orientation du bras 1 d'une pivot vue de face en degres")
        self.OptionParser.add_option('--liaison_pivot2D_face_axe2', action = 'store', type = 'string', dest = 'liaison_pivot2D_face_axe2', default = '-y', help = u"Principales directions du bras 2 d'une pivot vue de face")
        self.OptionParser.add_option('--liaison_pivot2D_face_orientation2', action = 'store', type = 'float', dest = 'liaison_pivot2D_face_orientation2', default = '0', help = u"Orientation du bras 2 d'une pivot vue de face en degres")

        self.OptionParser.add_option('--liaison_pivot_3D_position_x', action = 'store', type = 'float', dest = 'liaison_pivot_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_position_y', action = 'store', type = 'float', dest = 'liaison_pivot_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_position_z', action = 'store', type = 'float', dest = 'liaison_pivot_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_type_direction', action = 'store', type = 'str', dest = 'liaison_pivot_3D_type_direction', default = "liaison_pivot_3D_type_direction_standard", help = u"Choix du type de direction de la pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_axe', action = 'store', type = 'str', dest = 'liaison_pivot_3D_axe', default = 'x', help = u"Directions standard de l'axe de la pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_type_direction_quelconque_x', action = 'store', type = 'float', dest = 'liaison_pivot_3D_type_direction_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur direceur de la pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_type_direction_quelconque_y', action = 'store', type = 'float', dest = 'liaison_pivot_3D_type_direction_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur direceur de la pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_type_direction_quelconque_z', action = 'store', type = 'float', dest = 'liaison_pivot_3D_type_direction_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur direceur de la pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_orientation_male', action = 'store', type = 'float', dest = 'liaison_pivot_3D_orientation_male', default = 0, help = u"Orientation en degres de la piece male de la pivot")
        self.OptionParser.add_option('--liaison_pivot_3D_orientation_femelle', action = 'store', type = 'float', dest = 'liaison_pivot_3D_orientation_femelle', default = 0, help = u"Orientation en degres de la piece femelle de la pivot")

        #LIAISON PIVOT GLISSANT ******************************************
        self.OptionParser.add_option('--liaison_pivot_glissant_type', action = 'store', type = 'string', dest = 'liaison_pivot_glissant_type', default = 'liaison_pivot_glissant_2D_cote', help = u"Type de representation de la pivot glissant")

        self.OptionParser.add_option('--liaison_pivot_glissant_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_cote_x', default = '0', help = u"Position sur X de la liaison pivot glissant 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_cote_y', default = '0', help = u"Position sur Y de la liaison pivot glissant 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_cote_axe', action = 'store', type = 'string', dest = 'liaison_pivot_glissant_2D_cote_axe', default = 'x', help = u"Principales directions de l'axe d'une pivot glissant 2D vue de cote")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_cote_orientation', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_cote_orientation', default = '0', help = u"Orientation Pivot glissant 2D en degres")

        self.OptionParser.add_option('--liaison_pivot_glissant_2D_face_x', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_face_x', default = '0', help = u"Position sur X de la liaison pivot 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_face_y', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_face_y', default = '0', help = u"Position sur Y de la liaison pivot 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_face_axe1', action = 'store', type = 'string', dest = 'liaison_pivot_glissant_2D_face_axe1', default = 'x', help = u"Principales directions du bras 1 d'une pivot glissant vue de face")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_face_orientation1', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_face_orientation1', default = '0', help = u"Orientation du bras 1 d'une pivot glissant vue de face en degres")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_face_axe2', action = 'store', type = 'string', dest = 'liaison_pivot_glissant_2D_face_axe2', default = '-y', help = u"Principales directions du bras 2 d'une pivot glissant vue de face")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_face_orientation2', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_face_orientation2', default = '0', help = u"Orientation du bras 2 d'une pivot glissant vue de face en degres")

        self.OptionParser.add_option('--liaison_pivot_glissant_3D_position_x', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_position_y', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_position_z', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_type_direction', action = 'store', type = 'str', dest = 'liaison_pivot_glissant_3D_type_direction', default = "liaison_pivot_glissant_3D_type_direction_standard", help = u"Choix du type de direction de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_axe', action = 'store', type = 'str', dest = 'liaison_pivot_glissant_3D_axe', default = 'x', help = u"Orientations standard de l'axe de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_type_direction_quelconque_x', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_type_direction_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_type_direction_quelconque_y', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_type_direction_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_type_direction_quelconque_z', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_type_direction_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_orientation_male', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_orientation_male', default = 0, help = u"Orientation en degres de la piece male de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_orientation_femelle', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_orientation_femelle', default = 0, help = u"Orientation en degres de la piece femelle de la pivot glissant 3D")


        #LIAISON GLISSIERE ******************************************
        self.OptionParser.add_option('--liaison_glissiere_type', action = 'store', type = 'string', dest = 'liaison_glissiere_type', default = 'liaison_glissiere_2D_cote', help = u"Type de representation de la glissiere")

        self.OptionParser.add_option('--liaison_glissiere_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_cote_x', default = '0', help = u"Position sur X de la liaison glissiere 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_glissiere_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_cote_y', default = '0', help = u"Position sur Y de la liaison glissiere 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_glissiere_2D_cote_axe', action = 'store', type = 'string', dest = 'liaison_glissiere_2D_cote_axe', default = 'x', help = u"Principales directions de l'axe d'une glissiere 2D vue de cote")
        self.OptionParser.add_option('--liaison_glissiere_2D_cote_orientation', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_cote_orientation', default = '0', help = u"Orientation glissiere 2D en degres")
        
        self.OptionParser.add_option('--liaison_glissiere_2D_face_x', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_face_x', default = '0', help = u"Position sur X de la glissiere 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_glissiere_2D_face_y', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_face_y', default = '0', help = u"Position sur Y de la glissiere 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_glissiere_2D_face_axe', action = 'store', type = 'string', dest = 'liaison_glissiere_2D_face_axe', default = 'x', help = u"Principales directions du bras de la piece femelle d'une glissiere vue de face")
        self.OptionParser.add_option('--liaison_glissiere_2D_face_orientation', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_face_orientation', default = '0', help = u"Orientation du bras de la piece femelle d'une glissier vue de face en degres")

        self.OptionParser.add_option('--liaison_glissiere_3D_position_x', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_position_y', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_position_z', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_type_direction', action = 'store', type = 'str', dest = 'liaison_glissiere_3D_type_direction', default = "liaison_glissiere_3D_type_orientation_standard", help = u"Choix du type de direction de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_axe', action = 'store', type = 'str', dest = 'liaison_glissiere_3D_axe', default = 'x', help = u"Direction standard de l'axe de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_type_direction_quelconque_x', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_type_direction_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur direceur de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_type_direction_quelconque_y', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_type_direction_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur direceur de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_type_direction_quelconque_z', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_type_direction_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur direceur de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_orientation', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_orientation', default = 0, help = u"Orientation de la glissiere 3D")

        

        #OPTIONS GENERALES ******************************************
        self.OptionParser.add_option('--opt_generales', action = 'store', type = 'string', dest = 'opt_generales', default = 'opt_gene_origine', help = u"Onglet des options generales")
        
        self.OptionParser.add_option('--opt_gene_gene_old', action = 'store', type = 'inkbool', dest = 'opt_gene_gene_old', default = 'False', help = u"Utilisation des anciennes normes")

        self.OptionParser.add_option('--x0', action = 'store', type = 'float', dest = 'x0', default = 0, help = u"Origine (2D) du repere (sur x)")
        self.OptionParser.add_option('--y0', action = 'store', type = 'float', dest = 'y0', default = 0, help = u"Origine (2D) du repere (sur y)")
        self.OptionParser.add_option('--echelle', action = 'store', type = 'float', dest = 'echelle', default = 1, help = u"Coefficient d'echelle")

        self.OptionParser.add_option('--opt_gene_lignes_epaisseur_1', action = 'store', type = 'float', dest = 'opt_gene_lignes_epaisseur_1', default = 1, help = u"Epaisseur des traits de la piece 1")
        self.OptionParser.add_option('--opt_gene_lignes_epaisseur_2', action = 'store', type = 'float', dest = 'opt_gene_lignes_epaisseur_2', default = 1, help = u"Epaisseur des traits de la piece 2")
        
        self.OptionParser.add_option('--opt_gene_piece1_couleur', action = 'store', type = 'int', dest = 'opt_gene_piece1_couleur', default = 16711680, help = u"Couleur de la piece 1")
        self.OptionParser.add_option('--opt_gene_piece2_couleur', action = 'store', type = 'int', dest = 'opt_gene_piece2_couleur', default = 65280, help = u"Couleur de la piece 2")



    def effect(self):
        """
        Effect behaviour.
        Overrides base class' method and inserts "Hello World" text into SVG document.
        """
        # Get script's "--what" option value.
        liaison=self.options.liaison

        # Get access to main SVG document element and get its dimensions.
        svg = self.document.getroot()
        # or alternatively
        # svg = self.document.xpath('//svg:svg',namespaces=inkex.NSS)[0]

        # Again, there are two ways to get the attibutes:
        width  = self.unittouu(svg.get('width'))
        height = self.unittouu(svg.attrib['height'])

	#Conversion des couleurs dans un format correct
	self.options.opt_gene_piece1_couleur=convertIntColor2Hex(self.options.opt_gene_piece1_couleur)
	self.options.opt_gene_piece2_couleur=convertIntColor2Hex(self.options.opt_gene_piece2_couleur)


        # Create a new layer.
        groupe = inkex.etree.SubElement(svg, 'g')
        
	#Dessin :
	if(liaison=="\"liaison_pivot\""):
		type_liaison=self.options.liaison_pivot_type
		if(type_liaison=="\"liaison_pivot_2D_cote\""):
			dessin_Pivot_2D_cote(self.options,svg)
		elif(type_liaison=="\"liaison_pivot_2D_face\""):
			dessin_Pivot_2D_face(self.options,svg)
		elif(type_liaison=="\"liaison_pivot_3D\""):
			dessin_Pivot_3D(self.options,svg)
	if(liaison=="\"liaison_pivot_glissant\""):
		type_liaison=self.options.liaison_pivot_glissant_type
		if(type_liaison=="\"liaison_pivot_glissant_2D_cote\""):
			dessin_Pivot_Glissant_2D_cote(self.options,svg)
		elif(type_liaison=="\"liaison_pivot_glissant_2D_face\""):
			dessin_Pivot_Glissant_2D_face(self.options,svg)
		elif(type_liaison=="\"liaison_pivot_glissant_3D\""):
			dessin_Pivot_Glissant_3D(self.options,svg)
	if(liaison=="\"liaison_glissiere\""):
		type_liaison=self.options.liaison_glissiere_type
		if(type_liaison=="\"liaison_glissiere_2D_cote\""):
			dessin_Glissiere_2D_cote(self.options,svg)
		if(type_liaison=="\"liaison_glissiere_2D_face\""):
			dessin_Glissiere_2D_face(self.options,svg)
		if(type_liaison=="\"liaison_glissiere_3D\""):
			dessin_Glissiere_3D(self.options,svg)
		
	
	



	
	
# Create effect instance and apply it.
effect = Liaisons()
effect.affect()

