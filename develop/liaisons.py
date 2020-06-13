# -- coding: utf-8 --
#!/usr/bin/env python

# These two lines are only needed if you don't put the script directly into
# the installation directory
import sys
#sys.path.append('/usr/share/inkscape/extensions')

# We will use the inkex module with the predefined Effect base class.
import inkex
import math
# The simplestyle module provides functions for style parsing.
#from simplestyle import *


from liaisons_parametres import *
from liaisons_fonctions_utiles import *
from liaisons_pivot import *
from liaisons_pivot_glissant import *
from liaisons_glissiere import *
from liaisons_plane import *
from liaisons_spherique import *
from liaisons_helicoidale import *
from liaisons_sphere_plan import *
from liaisons_rectiligne import *
from liaisons_sphere_cylindre import *
from liaisons_masse import *




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

        self.OptionParser.add_option('--liaison_pivot_glissant_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_cote_x', default = '0', help = u"Position sur X de la liaison pivot glissant 2D coté relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_cote_y', default = '0', help = u"Position sur Y de la liaison pivot glissant 2D coté relativement a l'origine")
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
        self.OptionParser.add_option('--liaison_glissiere_2D_cote_direction_standard', action = 'store', type = 'string', dest = 'liaison_glissiere_2D_cote_direction_standard', default = 'x', help = u"Principales directions de l'axe d'une glissiere 2D vue de cote")
        self.OptionParser.add_option('--liaison_glissiere_2D_cote_direction_quelconque', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_cote_direction_quelconque', default = '0', help = u"Orientation glissiere 2D en degres")
        
        self.OptionParser.add_option('--liaison_glissiere_2D_face_x', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_face_x', default = '0', help = u"Position sur X de la glissiere 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_glissiere_2D_face_y', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_face_y', default = '0', help = u"Position sur Y de la glissiere 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_glissiere_2D_face_orientation_standard_femelle', action = 'store', type = 'string', dest = 'liaison_glissiere_2D_face_orientation_standard_femelle', default = 'x', help = u"Principales directions du bras de la piece femelle d'une glissiere vue de face")
        self.OptionParser.add_option('--liaison_glissiere_2D_face_orientation_quelconque_femelle', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_face_orientation_quelconque_femelle', default = '0', help = u"Orientation du bras de la piece femelle d'une glissiere vue de face en degres")
        self.OptionParser.add_option('--liaison_glissiere_2D_face_orientation_standard_male', action = 'store', type = 'string', dest = 'liaison_glissiere_2D_face_orientation_standard_male', default = 'x', help = u"Principales directions du bras de la piece male d'une glissiere vue de face")
        self.OptionParser.add_option('--liaison_glissiere_2D_face_orientation_quelconque_male', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_face_orientation_quelconque_male', default = '0', help = u"Orientation du bras de la piece male d'une glissiere vue de face en degres")

        self.OptionParser.add_option('--liaison_glissiere_3D_position_x', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_position_y', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_position_z', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_type_direction', action = 'store', type = 'str', dest = 'liaison_glissiere_3D_type_direction', default = "liaison_glissiere_3D_type_orientation_standard", help = u"Choix du type de direction de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_axe', action = 'store', type = 'str', dest = 'liaison_glissiere_3D_axe', default = 'x', help = u"Direction standard de l'axe de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_type_direction_quelconque_x', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_type_direction_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur direceur de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_type_direction_quelconque_y', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_type_direction_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur direceur de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_type_direction_quelconque_z', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_type_direction_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur direceur de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_orientation', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_orientation', default = 0, help = u"Orientation de la glissiere 3D")

        
        #LIAISON PLANE ******************************************
        self.OptionParser.add_option('--liaison_plane_type', action = 'store', type = 'string', dest = 'liaison_plane_type', default = 'liaison_plane_2D_cote', help = u"Type de representation de la liaison plane")
        
        self.OptionParser.add_option('--liaison_plane_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_plane_2D_cote_x', default = '0', help = u"Position sur X de la liaison plane 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_plane_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_plane_2D_cote_y', default = '0', help = u"Position sur Y de la liaison plane 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_plane_2D_cote_axe', action = 'store', type = 'string', dest = 'liaison_plane_2D_cote_axe', default = 'x', help = u"Principales directions de l'axe d'une plane 2D vue de cote")
        self.OptionParser.add_option('--liaison_plane_2D_cote_orientation', action = 'store', type = 'float', dest = 'liaison_plane_2D_cote_orientation', default = '0', help = u"Orientation plane 2D en degres")

        self.OptionParser.add_option('--liaison_plane_2D_dessus_x', action = 'store', type = 'float', dest = 'liaison_plane_2D_dessus_x', default = '0', help = u"Position sur X de la liaison plane 2D dessus relativement a l'origine")
        self.OptionParser.add_option('--liaison_plane_2D_dessus_y', action = 'store', type = 'float', dest = 'liaison_plane_2D_dessus_y', default = '0', help = u"Position sur Y de la liaison plane 2D dessus relativement a l'origine")
        self.OptionParser.add_option('--liaison_plane_2D_axe_dessous', action = 'store', type = 'string', dest = 'liaison_plane_2D_axe_dessous', default = 'y', help = u"Principales directions de l'axe d'une plane 2D dessous")
        self.OptionParser.add_option('--liaison_plane_2D_orientation_dessous', action = 'store', type = 'float', dest = 'liaison_plane_2D_orientation_dessous', default = '0', help = u"Orientation plane 2D dessous en degres")
        self.OptionParser.add_option('--liaison_plane_2D_axe_dessus', action = 'store', type = 'string', dest = 'liaison_plane_2D_axe_dessus', default = '-y', help = u"Principales directions de l'axe d'une plane 2D dessus")
        self.OptionParser.add_option('--liaison_plane_2D_orientation_dessus', action = 'store', type = 'float', dest = 'liaison_plane_2D_orientation_dessus', default = '0', help = u"Orientation plane 2D dessus en degres")
 
        self.OptionParser.add_option('--liaison_plane_3D_position_x', action = 'store', type = 'float', dest = 'liaison_plane_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_position_y', action = 'store', type = 'float', dest = 'liaison_plane_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_position_z', action = 'store', type = 'float', dest = 'liaison_plane_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_type_normale', action = 'store', type = 'str', dest = 'liaison_plane_3D_type_normale', default = "liaison_plane_3D_type_normale_standard", help = u"Choix du type de direction de la glissiere 3D")
        self.OptionParser.add_option('--liaison_plane_3D_axe', action = 'store', type = 'str', dest = 'liaison_plane_3D_axe', default = 'x', help = u"Direction standard de l'axe de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_type_direction_quelconque_x', action = 'store', type = 'float', dest = 'liaison_plane_3D_type_direction_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur direceur de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_type_direction_quelconque_y', action = 'store', type = 'float', dest = 'liaison_plane_3D_type_direction_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur direceur de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_type_direction_quelconque_z', action = 'store', type = 'float', dest = 'liaison_plane_3D_type_direction_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur direceur de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_orientation1', action = 'store', type = 'float', dest = 'liaison_plane_3D_orientation1', default = 10, help = u"Orientation de la liaison plane 3D - piece 1")
        self.OptionParser.add_option('--liaison_plane_3D_orientation2', action = 'store', type = 'float', dest = 'liaison_plane_3D_orientation2', default = 0, help = u"Orientation de la liaison plane 3D - piece 2")
            
        #LIAISON SPHERIQUE ******************************************
        self.OptionParser.add_option('--liaison_spherique_type', action = 'store', type = 'string', dest = 'liaison_spherique_type', default = 'liaison_spherique_2D', help = u"Type de representation de la liaison spherique")

        self.OptionParser.add_option('--liaison_spherique_2D_x', action = 'store', type = 'float', dest = 'liaison_spherique_2D_x', default = '0', help = u"Position sur X de la liaison spherique 2D relativement a l'origine")
        self.OptionParser.add_option('--liaison_spherique_2D_y', action = 'store', type = 'float', dest = 'liaison_spherique_2D_y', default = '0', help = u"Position sur Y de la liaison spherique 2D relativement a l'origine")
        self.OptionParser.add_option('--liaison_spherique_2D_axe_male', action = 'store', type = 'string', dest = 'liaison_spherique_2D_axe_male', default = 'x', help = u"Principales directions de l'axe d'une spherique 2D - male")
        self.OptionParser.add_option('--liaison_spherique_2D_orientation_male', action = 'store', type = 'float', dest = 'liaison_spherique_2D_orientation_male', default = '0', help = u"Orientation plane 2D en degres - male")
        self.OptionParser.add_option('--liaison_spherique_2D_axe_femelle', action = 'store', type = 'string', dest = 'liaison_spherique_2D_axe_femelle', default = 'x', help = u"Principales directions de l'axe d'une spherique 2D - femelle")
        self.OptionParser.add_option('--liaison_spherique_2D_orientation_femelle', action = 'store', type = 'float', dest = 'liaison_spherique_2D_orientation_femelle', default = '0', help = u"Orientation plane 2D en degres - femelle")
        self.OptionParser.add_option('--liaison_spherique_2D_calotte_adaptative', action = 'store', type = 'inkbool', dest = 'liaison_spherique_2D_calotte_adaptative', default = 'True', help = u"Permet d'orienter automatiquement la calotte de la pièce femelle")

        self.OptionParser.add_option('--liaison_spherique_3D_position_x', action = 'store', type = 'float', dest = 'liaison_spherique_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison sphérique 3D")
        self.OptionParser.add_option('--liaison_spherique_3D_position_y', action = 'store', type = 'float', dest = 'liaison_spherique_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison sphérique 3D")
        self.OptionParser.add_option('--liaison_spherique_3D_position_z', action = 'store', type = 'float', dest = 'liaison_spherique_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison sphérique 3D")
        self.OptionParser.add_option('--liaison_spherique_3D_type_orientation_male', action = 'store', type = 'str', dest = 'liaison_spherique_3D_type_orientation_male', default = "liaison_spherique_3D_axe_male", help = u"Choix du type de direction de la liaison sphérique 3D mâle")
        self.OptionParser.add_option('--liaison_spherique_3D_axe_male', action = 'store', type = 'str', dest = 'liaison_spherique_3D_axe_male', default = 'y', help = u"Direction standard de l'axe de la liaison sphérique 3D mâle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_direction_male_quelconque_x', action = 'store', type = 'float', dest = 'liaison_spherique_3D_type_direction_male_quelconque_x', default = 0, help = u"Coordonnee sur x du vecteur direceur de la liaison sphérique 3D mâle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_direction_male_quelconque_y', action = 'store', type = 'float', dest = 'liaison_spherique_3D_type_direction_male_quelconque_y', default = 1, help = u"Coordonnee sur y du vecteur direceur de la liaison sphérique 3D mâle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_direction_male_quelconque_z', action = 'store', type = 'float', dest = 'liaison_spherique_3D_type_direction_male_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur direceur de la liaison sphérique 3D mâle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_orientation_femelle', action = 'store', type = 'str', dest = 'liaison_spherique_3D_type_orientation_femelle', default = "liaison_spherique_3D_axe_male", help = u"Choix du type de direction de la liaison sphérique 3D femelle")
        self.OptionParser.add_option('--liaison_spherique_3D_axe_femelle', action = 'store', type = 'str', dest = 'liaison_spherique_3D_axe_femelle', default = 'y', help = u"Direction standard de l'axe de la liaison sphérique 3D femelle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_direction_femelle_quelconque_x', action = 'store', type = 'float', dest = 'liaison_spherique_3D_type_direction_femelle_quelconque_x', default = 0, help = u"Coordonnee sur x du vecteur direceur de la liaison sphérique 3D femelle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_direction_femelle_quelconque_y', action = 'store', type = 'float', dest = 'liaison_spherique_3D_type_direction_femelle_quelconque_y', default = 1, help = u"Coordonnee sur y du vecteur direceur de la liaison sphérique 3D femelle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_direction_femelle_quelconque_z', action = 'store', type = 'float', dest = 'liaison_spherique_3D_type_direction_femelle_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur direceur de la liaison sphérique 3D femelle")
        self.OptionParser.add_option('--liaison_spherique_3D_calotte_adaptative', action = 'store', type = 'inkbool', dest = 'liaison_spherique_3D_calotte_adaptative', default = 'True', help = u"Permet d'orienter automatiquement la calotte de la pièce femelle")


	#LIAISON HELICOIDALE **********************************************
        self.OptionParser.add_option('--liaison_helicoidale_pas_a_gauche', action = 'store', type = 'inkbool', dest = 'liaison_helicoidale_pas_a_gauche', default = 'True', help = u"Vrai si c'est un pas à gauche")
        self.OptionParser.add_option('--liaison_helicoidale_type', action = 'store', type = 'string', dest = 'liaison_helicoidale_type', default = 'liaison_helicoidale_2D_cote', help = u"Type de representation de la liaison hélicoïdale")

        self.OptionParser.add_option('--liaison_helicoidale_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_cote_x', default = '0', help = u"Position sur X de la liaison hélicoidale 2D coté relativement a l'origine")
	self.OptionParser.add_option('--liaison_helicoidale_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_cote_y', default = '0', help = u"Position sur Y de la liaison hélicoidale 2D coté relativement a l'origine")       
        self.OptionParser.add_option('--liaison_helicoidale_2D_cote_axe', action = 'store', type = 'string', dest = 'liaison_helicoidale_2D_cote_axe', default = 'x', help = u"Principales directions de l'axe d'une hélicoidale 2D vue de coté")
        self.OptionParser.add_option('--liaison_helicoidale_2D_cote_orientation', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_cote_orientation', default = '0', help = u"Orientation de l'hélicoidale 2D (coté) en degres")

        self.OptionParser.add_option('--liaison_helicoidale_2D_face_x', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_face_x', default = 0, help = u"Position sur X de la liaison hélicoidale 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_helicoidale_2D_face_y', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_face_y', default = 0, help = u"Position sur Y de la liaison hélicoidale 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_helicoidale_2D_face_axe1', action = 'store', type = 'string', dest = 'liaison_helicoidale_2D_face_axe1', default = 'x', help = u"Principales directions du bras 1 d'une hélicoidale vue de face")
        self.OptionParser.add_option('--liaison_helicoidale_2D_face_orientation1', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_face_orientation1', default = '0', help = u"Orientation du bras 1 d'une hélicoidale vue de face en degres")
        self.OptionParser.add_option('--liaison_helicoidale_2D_face_axe2', action = 'store', type = 'string', dest = 'liaison_helicoidale_2D_face_axe2', default = '-y', help = u"Principales directions du bras 2 d'une hélicoidale vue de face")
        self.OptionParser.add_option('--liaison_helicoidale_2D_face_orientation2', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_face_orientation2', default = '0', help = u"Orientation du bras 2 d'une hélicoidale vue de face en degres")

        self.OptionParser.add_option('--liaison_helicoidale_3D_position_x', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison helicoidale 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_position_y', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison helicoidale 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_position_z', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison helicoidale 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_type_direction', action = 'store', type = 'str', dest = 'liaison_helicoidale_3D_type_direction', default = "liaison_helicoidale_3D_type_direction_standard", help = u"Choix du type de direction de la liaison helicoidale 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_axe', action = 'store', type = 'str', dest = 'liaison_helicoidale_3D_axe', default = 'x', help = u"Orientations standard de l'axe de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_type_direction_quelconque_x', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_type_direction_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de l'helicoidale 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_type_direction_quelconque_y', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_type_direction_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de l'helicoidal 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_type_direction_quelconque_z', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_type_direction_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de l'helicoidal 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_orientation_male', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_orientation_male', default = 0, help = u"Orientation en degres de la piece male de l'helicoidal 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_orientation_femelle', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_orientation_femelle', default = 0, help = u"Orientation en degres de la piece femelle de l'helicoidal 3D")

	#LIAISON SPHÈRE-PLAN **********************************************
        self.OptionParser.add_option('--liaison_sphere_plan_type', action = 'store', type = 'string', dest = 'liaison_sphere_plan_type', default = 'liaison_sphere_plan_2D_cote', help = u"Type de representation de la liaison sphère-plan")

        self.OptionParser.add_option('--liaison_sphere_plan_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_cote_x', default = '0', help = u"Position sur X de la liaison Sphère-plan 2D coté relativement a l'origine")
	self.OptionParser.add_option('--liaison_sphere_plan_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_cote_y', default = '0', help = u"Position sur Y de la liaison Sphère-plan 2D coté relativement a l'origine")       
        self.OptionParser.add_option('--liaison_sphere_plan_2D_cote_axe_normale', action = 'store', type = 'string', dest = 'liaison_sphere_plan_2D_cote_axe_normale', default = 'y', help = u"Principales directions de la normale de la Sphère-plan 2D vue de coté")
        self.OptionParser.add_option('--liaison_sphere_plan_2D_cote_orientation_normale', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_cote_orientation_normale', default = '0', help = u"Orientation de la normale de la Sphère-Plan 2D (coté) en degres")
        self.OptionParser.add_option('--liaison_sphere_plan_2D_cote_axe_sphere', action = 'store', type = 'string', dest = 'liaison_sphere_plan_2D_cote_axe_sphere', default = 'normale', help = u"Principales directions de la sphère de la Sphère-plan 2D vue de coté")
        self.OptionParser.add_option('--liaison_sphere_plan_2D_cote_orientation_sphere', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_cote_orientation_sphere', default = '0', help = u"Orientation de la sphère de la Sphère-Plan 2D (coté) en degres")

        self.OptionParser.add_option('--liaison_sphere_plan_2D_dessus_x', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_dessus_x', default = '0', help = u"Position sur X de la liaison Sphère-plan 2D dessus relativement a l'origine")
	self.OptionParser.add_option('--liaison_sphere_plan_2D_dessus_y', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_dessus_y', default = '0', help = u"Position sur Y de la liaison Sphère-plan 2D dessus relativement a l'origine")       
        self.OptionParser.add_option('--liaison_sphere_plan_2D_dessus_axe_plan', action = 'store', type = 'string', dest = 'liaison_sphere_plan_2D_dessus_axe_plan', default = 'y', help = u"Principales directions de l'axe du plan de la Sphère-plan 2D vue de dessus")
        self.OptionParser.add_option('--liaison_sphere_plan_2D_dessus_orientation_plan', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_dessus_orientation_plan', default = '0', help = u"Directions quelconque de l'axe du plan de la Sphère-plan 2D vue de dessus")
        self.OptionParser.add_option('--liaison_sphere_plan_2D_dessus_axe_sphere', action = 'store', type = 'string', dest = 'liaison_sphere_plan_2D_dessus_axe_sphere', default = 'y', help = u"Principales directions de l'axe de la sphère de la Sphère-plan 2D vue de dessus")
        self.OptionParser.add_option('--liaison_sphere_plan_2D_dessus_orientation_sphere', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_dessus_orientation_sphere', default = '0', help = u"Directions quelconque de l'axe de la sphère de la Sphère-plan 2D vue de dessus")
        
        self.OptionParser.add_option('--liaison_sphere_plan_3D_position_x', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison sphère-plan 3D")
        self.OptionParser.add_option('--liaison_sphere_plan_3D_position_y', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison sphère-plan 3D")
        self.OptionParser.add_option('--liaison_sphere_plan_3D_position_z', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_type_normale', action = 'store', type = 'str', dest = 'liaison_sphere_plan_3D_type_normale', default = "liaison_sphere_plan_3D_type_normale_standard", help = u"Choix du type de normale de la liaison Sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_axe_normale', action = 'store', type = 'str', dest = 'liaison_sphere_plan_3D_axe_normale', default = 'x', help = u"Orientations standard de l'axe de la sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_normale_quelconque_x', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_normale_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de la sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_normale_quelconque_y', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_normale_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de la sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_normale_quelconque_z', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_normale_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de la sphère-plan 3D")
        self.OptionParser.add_option('--liaison_sphere_plan_3D_rotation_plan', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_rotation_plan', default = 0, help = u"Orientation en degres du plan autour de la normale de la sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_type_direction_sphere', action = 'store', type = 'str', dest = 'liaison_sphere_plan_3D_type_direction_sphere', default = 'liaison_sphere_plan_3D_type_direction_sphere_standard', help = u"Type de direction de l'axe de la sphère de la sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_axe_sphere', action = 'store', type = 'str', dest = 'liaison_sphere_plan_3D_axe_sphere', default = 'x', help = u"Orientations standard de l'axe de la sphère de la sphère-plan 3D")
        self.OptionParser.add_option('--liaison_sphere_plan_3D_direction_sphere_quelconque_x', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_direction_sphere_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de la tige de sphere de la sphère-plan 3D")
        self.OptionParser.add_option('--liaison_sphere_plan_3D_direction_sphere_quelconque_y', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_direction_sphere_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de la tige de sphere de la sphère-plan 3D")
        self.OptionParser.add_option('--liaison_sphere_plan_3D_direction_sphere_quelconque_z', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_direction_sphere_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de la tige de sphere de la sphère-plan 3D")

	#LIAISON RECTILIGNE **********************************************
        self.OptionParser.add_option('--liaison_rectiligne_type', action = 'store', type = 'string', dest = 'liaison_rectiligne_type', default = 'liaison_rectiligne_2D_cote', help = u"Type de representation de la liaison rectiligne")
        
        self.OptionParser.add_option('--liaison_rectiligne_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_cote_x', default = '0', help = u"Position sur X de la liaison rectiligne 2D coté relativement a l'origine")
	self.OptionParser.add_option('--liaison_rectiligne_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_cote_y', default = '0', help = u"Position sur Y de la liaison rectiligne 2D coté relativement a l'origine")       
        self.OptionParser.add_option('--liaison_rectiligne_cote_axe_normale', action = 'store', type = 'string', dest = 'liaison_rectiligne_cote_axe_normale', default = 'y', help = u"Principales directions de la normale de la liaison rectiligne 2D vue de coté")
        self.OptionParser.add_option('--liaison_rectiligne_2D_cote_orientation_normale', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_cote_orientation_normale', default = '0', help = u"Orientation de la normale de la liaison rectiligne 2D (coté) en degres")
       
        self.OptionParser.add_option('--liaison_rectiligne_2D_bout_x', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_bout_x', default = '0', help = u"Position sur X de la liaison rectiligne 2D vue du bout relativement a l'origine")
	self.OptionParser.add_option('--liaison_rectiligne_2D_bout_y', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_bout_y', default = '0', help = u"Position sur Y de la liaison rectiligne 2D vue du bout relativement a l'origine")
        self.OptionParser.add_option('--liaison_rectiligne_bout_axe_normale', action = 'store', type = 'string', dest = 'liaison_rectiligne_bout_axe_normale', default = 'y', help = u"Principales directions de la normale de la liaison rectiligne 2D vue du bout")
        self.OptionParser.add_option('--liaison_rectiligne_2D_bout_orientation_normale', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_bout_orientation_normale', default = '0', help = u"Orientation de la normale de la liaison rectiligne 2D (bout) en degres")
        self.OptionParser.add_option('--liaison_rectiligne_bout_axe_prisme', action = 'store', type = 'string', dest = 'liaison_rectiligne_bout_axe_prisme', default = 'y', help = u"Principales directions du prisme de la liaison rectiligne 2D vue du bout")
        self.OptionParser.add_option('--liaison_rectiligne_2D_bout_orientation_prisme', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_bout_orientation_prisme', default = '0', help = u"Orientation du prisme de la liaison rectiligne 2D (bout) en degres")
        
        self.OptionParser.add_option('--liaison_rectiligne_3D_position_x', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison rectiligne 3D")
        self.OptionParser.add_option('--liaison_rectiligne_3D_position_y', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison rectiligne 3D")
        self.OptionParser.add_option('--liaison_rectiligne_3D_position_z', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_type_normale', action = 'store', type = 'str', dest = 'liaison_rectiligne_3D_type_normale', default = 'liaison_rectiligne_3D_type_normale_standard', help = u"Choix du type de normale de la liaison rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_axe_normale', action = 'store', type = 'str', dest = 'liaison_rectiligne_3D_axe_normale', default = 'z', help = u"Orientations standard de l'axe de la rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_normale_quelconque_x', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_normale_quelconque_x', default = 0, help = u"Coordonnee sur x du vecteur directeur de la normale rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_normale_quelconque_y', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_normale_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de la normale rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_normale_quelconque_z', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_normale_quelconque_z', default = 1, help = u"Coordonnee sur z du vecteur directeur de la normale rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_type_direction', action = 'store', type = 'str', dest = 'liaison_rectiligne_3D_type_direction', default = 'liaison_rectiligne_3D_type_direction_standard', help = u"Choix du type de direction de la liaison rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_axe_direction', action = 'store', type = 'str', dest = 'liaison_rectiligne_3D_axe_direction', default = 'x', help = u"Orientations standard de la direction de la rectiligne 3D")
        self.OptionParser.add_option('--liaison_rectiligne_3D_direction_quelconque_x', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_direction_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de la direction rectiligne 3D")
        self.OptionParser.add_option('--liaison_rectiligne_3D_direction_quelconque_y', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_direction_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de la direction rectiligne 3D")
        self.OptionParser.add_option('--liaison_rectiligne_3D_direction_quelconque_z', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_direction_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de la direction rectiligne 3D")
        self.OptionParser.add_option('--liaison_rectiligne_3D_inclinaison_prisme', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_inclinaison_prisme', default = '0', help = u"Orientation du prisme en degres")

	#LIAISON SPHERE-CYLINDRE *****************************************
        self.OptionParser.add_option('--liaison_sphere_cylindre_type', action = 'store', type = 'string', dest = 'liaison_sphere_cylindre_type', default = 'liaison_sphere_cylindre_2D_cote', help = u"Type de representation de la liaison sphère-cylindre")
        
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_cote_x', default = '0', help = u"Position sur X de la liaison sphère-cylindre 2D coté relativement a l'origine")
	self.OptionParser.add_option('--liaison_sphere_cylindre_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_cote_y', default = '0', help = u"Position sur Y de la liaison sphère-cylindre 2D coté relativement a l'origine")       
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_cote_axe', action = 'store', type = 'string', dest = 'liaison_sphere_cylindre_2D_cote_axe', default = 'x', help = u"Principales directions de la direction de la liaison sphère-cylindre 2D vue de coté")
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_cote_orientation_axe', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_cote_orientation_axe', default = '0', help = u"Orientation de la direction de la liaison sphère-cylindre 2D (coté) en degres")
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_cote_axe_sphere', action = 'store', type = 'string', dest = 'liaison_sphere_cylindre_2D_cote_axe_sphere', default = 'normal', help = u"Principales directions de la sphère pour la liaison sphère-cylindre 2D vue de coté")
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_cote_orientation_axe_sphere', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_cote_orientation_axe_sphere', default = '0', help = u"Orientation de la sphère de la liaison sphère-cylindre 2D (coté) en degres")
        
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_bout_x', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_bout_x', default = '0', help = u"Position sur X de la liaison sphère-cylindre 2D vue du bout relativement a l'origine")
	self.OptionParser.add_option('--liaison_sphere_cylindre_2D_bout_y', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_bout_y', default = '0', help = u"Position sur Y de la liaison sphère-cylindre 2D vue du bout relativement a l'origine")       
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_bout_axe_base', action = 'store', type = 'string', dest = 'liaison_sphere_cylindre_2D_bout_axe_base', default = 'y', help = u"Principales directions de la direction de la liaison sphère-cylindre 2D vue du bout")
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_bout_orientation_axe_base', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_bout_orientation_axe_base', default = '0', help = u"Orientation de la direction de la base de la liaison sphère-cylindre 2D (bout) en degres")
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_bout_axe_sphere', action = 'store', type = 'string', dest = 'liaison_sphere_cylindre_2D_bout_axe_sphere', default = 'normal', help = u"Principales directions de la sphère pour la liaison sphère-cylindre 2D vue du bout")
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_bout_orientation_axe_sphere', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_bout_orientation_axe_sphere', default = '0', help = u"Orientation de la sphère de la liaison sphère-cylindre 2D (bout) en degres")
        
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_position_x', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison Sphère-Cylindre 3D")
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_position_y', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison Sphère-Cylindre 3D")
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_position_z', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison Sphère-Cylindre 3D")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_type_axe', action = 'store', type = 'str', dest = 'liaison_sphere_cylindre_3D_type_axe', default = 'liaison_sphere_cylindre_3D_type_standard', help = u"Choix du type d'axe de la liaison Sphère-Cylindre 3D")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_axe', action = 'store', type = 'str', dest = 'liaison_sphere_cylindre_3D_axe', default = 'x', help = u"Orientations standard de l'axe de la Sphère-Cylindre 3D")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_axe_quelconque_x', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_axe_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de l'axe de Sphère-Cylindre 3D")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_axe_quelconque_y', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_axe_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de l'axe de Sphère-Cylindre 3D")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_axe_quelconque_z', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_axe_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de l'axe de Sphère-Cylindre 3D")
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_rotation_cylindre', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_rotation_cylindre', default = '0', help = u"Rotation (en degrés) du cylindre autour de son axe")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_type_direction_sphere', action = 'store', type = 'str', dest = 'liaison_sphere_cylindre_3D_type_direction_sphere', default = 'liaison_sphere_cylindre_3D_type_standard', help = u"Choix du type d'axe pour la sphère de la liaison Sphère-Cylindre 3D")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_axe_sphere', action = 'store', type = 'str', dest = 'liaison_sphere_cylindre_3D_axe_sphere', default = 'x', help = u"Orientations standard de l'axe de la sphère de la Sphère-Cylindre 3D")
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_direction_sphere_quelconque_x', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_direction_sphere_quelconque_x', default = 0, help = u"Coordonnee sur x du vecteur directeur de l'axe de la sphère de la Sphère-Cylindre 3D")
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_direction_sphere_quelconque_y', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_direction_sphere_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de l'axe de la sphère de la Sphère-Cylindre 3D")
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_direction_sphere_quelconque_z', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_direction_sphere_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de l'axe de la sphère de la Sphère-Cylindre 3D")
	
	
	#LIAISON MASSE *****************************************
        self.OptionParser.add_option('--liaison_masse_type', action = 'store', type = 'string', dest = 'liaison_masse_type', default = 'liaison_masse_2D', help = u"Type de representation de la masse du référentiel.")
        
        self.OptionParser.add_option('--liaison_masse_2D_x', action = 'store', type = 'float', dest = 'liaison_masse_2D_x', default = '0', help = u"Position sur X du référentiel 2D relativement a l'origine.")
	self.OptionParser.add_option('--liaison_masse_2D_y', action = 'store', type = 'float', dest = 'liaison_masse_2D_y', default = '0', help = u"Position sur Y du référentiel 2D relativement a l'origine.")       
        self.OptionParser.add_option('--liaison_masse_2D_axe', action = 'store', type = 'string', dest = 'liaison_masse_2D_axe', default = 'x', help = u"Principales directions de la tige de la masse 2D")
        self.OptionParser.add_option('--liaison_masse_2D_orientation_axe', action = 'store', type = 'float', dest = 'liaison_masse_2D_orientation_axe', default = '0', help = u"Orientation de la direction de la tige du referentiel 2D en degres")
        
        self.OptionParser.add_option('--liaison_masse_3D_position_x', action = 'store', type = 'float', dest = 'liaison_masse_3D_position_x', default = 0, help = u"Coordonnee sur x du référentiel 3D")
        self.OptionParser.add_option('--liaison_masse_3D_position_y', action = 'store', type = 'float', dest = 'liaison_masse_3D_position_y', default = 0, help = u"Coordonnee sur y du référentiel 3D")
        self.OptionParser.add_option('--liaison_masse_3D_position_z', action = 'store', type = 'float', dest = 'liaison_masse_3D_position_z', default = 0, help = u"Coordonnee sur z du référentiel 3D")
        self.OptionParser.add_option('--liaison_masse_3D_type_axe', action = 'store', type = 'str', dest = 'liaison_masse_3D_type_axe', default = 'liaison_masse_3D_type_standard', help = u"Choix du type de direction de la tige du référentiel 3D")
	self.OptionParser.add_option('--liaison_masse_3D_axe', action = 'store', type = 'str', dest = 'liaison_masse_3D_axe', default = 'x', help = u"Orientations standard de la tige du referentiel 2D")
	self.OptionParser.add_option('--liaison_masse_3D_axe_quelconque_x', action = 'store', type = 'float', dest = 'liaison_masse_3D_axe_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de la tige du referentiel 3D")
	self.OptionParser.add_option('--liaison_masse_3D_axe_quelconque_y', action = 'store', type = 'float', dest = 'liaison_masse_3D_axe_quelconque_y', default = 1, help = u"Coordonnee sur y du vecteur directeur de la tige du referentiel 3D")
	self.OptionParser.add_option('--liaison_masse_3D_axe_quelconque_z', action = 'store', type = 'float', dest = 'liaison_masse_3D_axe_quelconque_z', default = 1, help = u"Coordonnee sur z du vecteur directeur de la tige du referentiel 3D")
        self.OptionParser.add_option('--liaison_masse_3D_pivotement', action = 'store', type = 'float', dest = 'liaison_masse_3D_pivotement', default = '0', help = u"Rotation (en degrés) de la masse autour de sa tige")	
	self.OptionParser.add_option('--liaison_masse_3D_representation', action = 'store', type = 'inkbool', dest = 'liaison_masse_3D_representation', default = 'False', help = u"Représentation 3D de la masse, en dessin 3D")
        
        
        
        #OPTIONS GENERALES ******************************************
        self.OptionParser.add_option('--opt_generales', action = 'store', type = 'string', dest = 'opt_generales', default = 'opt_gene_origine', help = u"Onglet des options generales")
        
        self.OptionParser.add_option('--opt_gene_inverse', action = 'store', type = 'inkbool', dest = 'opt_gene_inverse', default = 'False', help = u"Inverse les parametres piece 1 / piece 2")
        self.OptionParser.add_option('--opt_gene_gene_old', action = 'store', type = 'inkbool', dest = 'opt_gene_gene_old', default = 'False', help = u"Utilisation des anciennes normes")
        
        self.OptionParser.add_option('--x0', action = 'store', type = 'float', dest = 'x0', default = 0, help = u"Origine (2D) du repere (sur x)")
        self.OptionParser.add_option('--y0', action = 'store', type = 'float', dest = 'y0', default = 0, help = u"Origine (2D) du repere (sur y)")
        self.OptionParser.add_option('--longueur_base', action = 'store', type = 'float', dest = 'longueur_base', default = 1, help = u"Longueur des vecteur unitaire de la base")
        self.OptionParser.add_option('--unite_base', action = 'store', type = 'string', dest = 'unite_base', default = "cm", help = u"Unité dans laquelle est exprimé la longueur de la base.")
        self.OptionParser.add_option('--echelle', action = 'store', type = 'float', dest = 'echelle', default = 1, help = u"Coefficient d'echelle pour les liaisons")
        self.OptionParser.add_option('--opt_gene_echelle_epaisseurs', action = 'store', type = 'inkbool', dest = 'opt_gene_echelle_epaisseurs', default = 'False', help = u"L'echelle affecte (ou pas) les épaisseurs")


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
        self.options.credits=u"Auteur : Raphaël ALLAIS (Lycee G.Eiffel de DIJON) - Éduscol"
        self.options.effect=self	#On passe la référence de l'objet effect dans les options pour y avoir acces dans les fonctions qui ne sont pas membre

        # Get access to main SVG document element and get its dimensions.
        svg = self.document.getroot()
        
        # Again, there are two ways to get the attibutes:
        width  = self.unittouu(svg.get('width'))
        height = self.unittouu(svg.attrib['height'])

	#Conversion des couleurs dans un format correct
	self.options.opt_gene_piece1_couleur=convertIntColor2Hex(self.options.opt_gene_piece1_couleur)
	self.options.opt_gene_piece2_couleur=convertIntColor2Hex(self.options.opt_gene_piece2_couleur)
	
	# Inversion des paramètres pièce 1 / pièce 2
	if self.options.opt_gene_inverse :
		self.options.opt_gene_piece1_couleur, self.options.opt_gene_piece2_couleur = self.options.opt_gene_piece2_couleur , self.options.opt_gene_piece1_couleur
		self.options.opt_gene_lignes_epaisseur_1, self.options.opt_gene_lignes_epaisseur_2 = self.options.opt_gene_lignes_epaisseur_2, self.options.opt_gene_lignes_epaisseur_1
		
	#Echelle des epaisseurs
	if self.options.opt_gene_echelle_epaisseurs :
		self.options.opt_gene_lignes_epaisseur_1 *= self.options.echelle
		self.options.opt_gene_lignes_epaisseur_2 *= self.options.echelle
        # Create a new layer.
        #groupe = inkex.etree.SubElement(svg, 'g')
        
	#Dessin :
	if liaison == "\"liaison_pivot\"" :
		type_liaison=self.options.liaison_pivot_type
		if(type_liaison=="\"liaison_pivot_2D_cote\""):
			dessin_Pivot_2D_cote(self.options,svg)
		elif(type_liaison=="\"liaison_pivot_2D_face\""):
			dessin_Pivot_2D_face(self.options,svg)
		elif(type_liaison=="\"liaison_pivot_3D\""):
			dessin_Pivot_3D(self.options,svg)
	if liaison == "\"liaison_pivot_glissant\"" :
		type_liaison=self.options.liaison_pivot_glissant_type
		if(type_liaison=="\"liaison_pivot_glissant_2D_cote\""):
			dessin_Pivot_Glissant_2D_cote(self.options,svg)
		elif(type_liaison=="\"liaison_pivot_glissant_2D_face\""):
			dessin_Pivot_Glissant_2D_face(self.options,svg)
		elif(type_liaison=="\"liaison_pivot_glissant_3D\""):
			dessin_Pivot_Glissant_3D(self.options,svg)
	if liaison == "\"liaison_glissiere\"" :
		type_liaison=self.options.liaison_glissiere_type
		if(type_liaison=="\"liaison_glissiere_2D_cote\""):
			dessin_Glissiere_2D_cote(self.options,svg)
		if(type_liaison=="\"liaison_glissiere_2D_face\""):
			dessin_Glissiere_2D_face(self.options,svg)
		if(type_liaison=="\"liaison_glissiere_3D\""):
			dessin_Glissiere_3D(self.options,svg)
	if liaison == "\"liaison_plane\"" :
		type_liaison=self.options.liaison_plane_type
		if(type_liaison=="\"liaison_plane_2D_cote\""):
			dessin_plane_2D_cote(self.options,svg)
		if(type_liaison=="\"liaison_plane_2D_dessus\""):
			dessin_plane_2D_dessus(self.options,svg)
		if(type_liaison=="\"liaison_plane_3D\""):
			dessin_plane_3D(self.options,svg)
	if liaison == "\"liaison_spherique\"" :
		type_liaison=self.options.liaison_spherique_type
		if(type_liaison=="\"liaison_spherique_2D\""):
			dessin_spherique_2D(self.options,svg)
		if(type_liaison=="\"liaison_spherique_3D\""):
			dessin_spherique_3D(self.options,svg)
	if liaison == "\"liaison_helicoidale\"" :
		type_liaison=self.options.liaison_helicoidale_type
		if(type_liaison=="\"liaison_helicoidale_2D_cote\""):
			dessin_helicoidale_2D_cote(self.options,svg)
		if(type_liaison=="\"liaison_helicoidale_2D_face\""):
			dessin_helicoidale_2D_face(self.options,svg)
		if(type_liaison=="\"liaison_helicoidale_3D\""):
			dessin_helicoidale_3D(self.options,svg)
	if liaison == "\"liaison_sphere_plan\"" :
		type_liaison=self.options.liaison_sphere_plan_type
		if(type_liaison=="\"liaison_sphere_plan_2D_cote\""):
			dessin_sphere_plan_2D_cote(self.options,svg)
		if(type_liaison=="\"liaison_sphere_plan_2D_dessus\""):
			dessin_sphere_plan_2D_dessus(self.options,svg)
		if(type_liaison=="\"liaison_sphere_plan_3D\""):
			dessin_sphere_plan_3D(self.options,svg)
	if liaison == "\"liaison_rectiligne\"" :
		type_liaison=self.options.liaison_rectiligne_type
		if(type_liaison=="\"liaison_rectiligne_2D_cote\""):
			dessin_rectiligne_plan_2D_cote(self.options,svg)
		if(type_liaison=="\"liaison_rectiligne_2D_bout\""):
			dessin_rectiligne_2D_bout(self.options,svg)
		if(type_liaison=="\"liaison_rectiligne_3D\""):
			dessin_rectiligne_3D(self.options,svg)
	if liaison == "\"liaison_sphere_cylindre\"" :
		type_liaison=self.options.liaison_sphere_cylindre_type
		if(type_liaison=="\"liaison_sphere_cylindre_2D_cote\""):
			dessin_Sphere_Cylindre_2D_cote(self.options,svg)
		if(type_liaison=="\"liaison_sphere_cylindre_2D_bout\""):
			dessin_Sphere_Cylindre_2D_bout(self.options,svg)
		if(type_liaison=="\"liaison_sphere_cylindre_3D\""):
			dessin_Sphere_Cylindre_3D(self.options,svg)
	if liaison == "\"liaison_masse\"" :
		type_liaison=self.options.liaison_masse_type
		if(type_liaison=="\"liaison_masse_2D\""):
			dessin_Masse_2D(self.options,svg)
		if(type_liaison=="\"liaison_masse_3D\""):
			dessin_Masse_3D(self.options,svg)
			
		
		
		
		
	
	



	
	
# Create effect instance and apply it.
effect = Liaisons()
effect.affect()
