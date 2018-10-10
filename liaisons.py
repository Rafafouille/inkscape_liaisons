#!/usr/bin/env python

# These two lines are only needed if you don't put the script directly into
# the installation directory
import sys
sys.path.append('/usr/share/inkscape/extensions')

# We will use the inkex module with the predefined Effect base class.
import inkex
import math
# The simplestyle module provides functions for style parsing.
from simplestyle import *



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
        self.OptionParser.add_option('--liaison', action = 'store', type = 'string', dest = 'liaison', default = '', help = u"Choix de la liaison")
        
        self.OptionParser.add_option('--liaison_pivot_type', action = 'store', type = 'string', dest = 'liaison_pivot_type', default = 'liaison_pivot_2D_cote', help = u"Type de representation")
        
        self.OptionParser.add_option('--liaison_pivot_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_pivot_2D_cote_x', default = '0', help = u"Position sur X de la liaison relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_pivot_2D_cote_y', default = '0', help = u"Position sur Y de la liaison relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot2D_cote_axe', action = 'store', type = 'string', dest = 'liaison_pivot2D_cote_axe', default = 'x', help = u"Principales directions de l'axe d'une pivot 2D vue de cote")
        self.OptionParser.add_option('--liaison_pivot2D_cote_orientation', action = 'store', type = 'float', dest = 'liaison_pivot2D_cote_orientation', default = '0', help = u"Orientation Pivot 2D en degres")
        
        self.OptionParser.add_option('--liaison_pivot_2D_face_x', action = 'store', type = 'float', dest = 'liaison_pivot_2D_face_x', default = '0', help = u"Position sur X de la liaison relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_2D_face_y', action = 'store', type = 'float', dest = 'liaison_pivot_2D_face_y', default = '0', help = u"Position sur Y de la liaison relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot2D_face_axe1', action = 'store', type = 'string', dest = 'liaison_pivot2D_face_axe1', default = 'x', help = u"Principales directions du bras 1 d'une pivot vue de face")
        self.OptionParser.add_option('--liaison_pivot2D_face_orientation1', action = 'store', type = 'float', dest = 'liaison_pivot2D_face_orientation1', default = '0', help = u"Orientation du bras 1 d'une pivot vue de face en degres")
        self.OptionParser.add_option('--liaison_pivot2D_face_axe2', action = 'store', type = 'string', dest = 'liaison_pivot2D_face_axe2', default = '-y', help = u"Principales directions du bras 2 d'une pivot vue de face")
        self.OptionParser.add_option('--liaison_pivot2D_face_orientation2', action = 'store', type = 'float', dest = 'liaison_pivot2D_face_orientation2', default = '0', help = u"Orientation du bras 2 d'une pivot vue de face en degres")

        self.OptionParser.add_option('--opt_generales', action = 'store', type = 'string', dest = 'opt_generales', default = 'opt_gene_origine', help = u"Onglet des options generales")
        
        self.OptionParser.add_option('--opt_gene_gene_old', action = 'store', type = 'inkbool', dest = 'opt_gene_gene_old', default = 'False', help = u"Utilisation des anciennes normes")
        self.OptionParser.add_option('--x0', action = 'store', type = 'float', dest = 'x0', default = '0', help = u"Origine (2D) du repere (sur x)")
        self.OptionParser.add_option('--y0', action = 'store', type = 'float', dest = 'y0', default = '0', help = u"Origine (2D) du repere (sur y)")
        self.OptionParser.add_option('--echelle', action = 'store', type = 'float', dest = 'echelle', default = 1, help = u"Coefficient d'echelle")
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

        # Create a new layer.
        groupe = inkex.etree.SubElement(svg, 'g')
        
	#Dessin :
	if(liaison=="\"liaison_pivot\""):
		type_liaison=self.options.liaison_pivot_type
		if(type_liaison=="\"liaison_pivot_2D_cote\""):
			dessin_Pivot_2D_cote(self.options,svg)
		elif(type_liaison=="\"liaison_pivot_2D_face\""):
			dessin_Pivot_2D_face(self.options,svg)
	
	
        # Create text element
        #text = inkex.etree.Element(inkex.addNS('text','svg'))
        #text.text = 'Hello toto !'

        # Set text position to center of document.
        #text.set('x', str(width / 2))
        #text.set('y', str(height / 2))

        # Center text horizontally with CSS style.
        #style = {'text-align' : 'center', 'text-anchor': 'middle'}
        #text.set('style', formatStyle(style))

        # Connect elements together.
        #layer.append(text)







#=================================================
# Fonctions utiles
#=================================================
def getCouleurFromInt(i):
	return "#"+("00000000"+hex(int(i))[2:])[-8:]

class v2D:
	def __init__(self,_x,_y):
		self.x0=_x
		self.y0=_y
		self.x=_x
		self.y=_y
		
	def rotation(self,theta,trigo=False):
		"""Theta en rad"""
		if(trigo):
			theta*=-1
		self.x,self.y=math.cos(theta)*self.x-math.sin(theta)*self.y , math.sin(theta)*self.x+math.cos(theta)*self.y
		
		
def points_to_svgd(p, close=True):
    """ convert list of points (x,y) pairs
        into a closed SVG path list
    """
    f = p[0]
    p = p[1:]
    svgd = 'M%.4f,%.4f' % f
    for x in p:
        svgd += 'L%.4f,%.4f' % x
    if close:
        svgd += 'z'
    return svgd

#=================================================
# Fonctions utiles
#=================================================
def dessin_Pivot_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Variables *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_pivot_2D_cote_x
	y=options.liaison_pivot_2D_cote_y
	old_liaisons=options.opt_gene_gene_old
	echelle=options.echelle
	largeur=30
	hauteur=15
	couleur_femelle="red"#getCouleurFromInt(options.opt_gene_piece2_couleur)
	couleur_male="blue"#getCouleurFromInt(options.opt_gene_piece1_couleur)
	epaisseur_femelle=3
	epaisseur_male=1
	rotation=-options.liaison_pivot2D_cote_orientation #Angle par defaut (sens trigo)
	if(options.liaison_pivot2D_cote_axe=="x"):
		rotation=0
	elif(options.liaison_pivot2D_cote_axe=="y"):
		rotation=-90
	elif(options.liaison_pivot2D_cote_axe=="-x"):
		rotation=180
	elif(options.liaison_pivot2D_cote_axe=="-y"):
		rotation=90
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        #groupe_rotation = inkex.etree.SubElement(liaison, 'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle=inkex.etree.SubElement(liaison,'g')
	
	#Base
	vx=v2D(echelle,0)
	vy=v2D(0,echelle)
	vx.rotation(rotation)
	vy.rotation(rotation)
	
	# Male ***************************************
	#Ligne male
	ligneM=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-largeur/2-epaisseur_femelle-10*epaisseur_male	,	0),
				(largeur/2+epaisseur_femelle+10*epaisseur_male	,	0)	])
	ligneM.set('d',chemin)
	ligneM.set('stroke',couleur_male)
	ligneM.set('stroke-width',str(epaisseur_male))
	ligneM.set('debug',str(options.opt_gene_piece1_couleur))
	male.append(ligneM)
	
	#Arret male 1
	arretM1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-largeur/2-epaisseur_femelle-3*epaisseur_male	,	-hauteur/2),
				(-largeur/2-epaisseur_femelle-3*epaisseur_male	,	hauteur/2)	])
	arretM1.set('d',chemin)
	arretM1.set('stroke',couleur_male)
	arretM1.set('stroke-width',str(epaisseur_male))
	male.append(arretM1)
	
	#Arret male 2
	arretM2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(largeur/2+epaisseur_femelle+3*epaisseur_male	,	-hauteur/2),
				(largeur/2+epaisseur_femelle+3*epaisseur_male	,	hauteur/2)	])
	arretM2.set('d',chemin)
	arretM2.set('stroke',couleur_male)
	arretM2.set('stroke-width',str(epaisseur_male))
	male.append(arretM2)
	
	# Femelle ***************************************
	if(old_liaisons):
		barreF1=inkex.etree.Element(inkex.addNS('path','svg'))
		chemin=points_to_svgd([	(-largeur/2	,	-hauteur/2),
					(largeur/2	,	-hauteur/2)	])
		barreF1.set('d',chemin)
		barreF1.set('stroke',couleur_femelle)
		barreF1.set('stroke-width',str(epaisseur_femelle))
		male.append(barreF1)
		
		barreF2=inkex.etree.Element(inkex.addNS('path','svg'))
		chemin=points_to_svgd([	(-largeur/2	,	hauteur/2),
					(largeur/2	,	hauteur/2)	])
		barreF2.set('d',chemin)
		barreF2.set('stroke',couleur_femelle)
		barreF2.set('stroke-width',str(epaisseur_femelle))
		male.append(barreF2)
	else:
		#Rectangle
		rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
		rectangle.set('x',str(-largeur*echelle/2) )
		rectangle.set('y',str(-hauteur*echelle/2) )
		rectangle.set('width',str(largeur*echelle))
		rectangle.set('height',str(hauteur*echelle))
		rectangle.set('style','fill:none')
		rectangle.set('stroke',couleur_femelle)
		rectangle.set('stroke-width',str(epaisseur_femelle))
		#rectangle.set('transform','rotate('+str(rotation/math.pi*180)+')')
		femelle.append(rectangle)
	
	#Ligne femelle
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(0	,	hauteur/2),
				(0	,	hauteur)	])
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle*echelle))
	femelle.append(ligneF)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation)+")")
	femelle.set("transform","rotate("+str(rotation)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")

	

def dessin_Pivot_2D_face(options,contexte):
	x0=options.x0
	y0=options.y0
	x=options.liaison_pivot_2D_cote_x
	y=options.liaison_pivot_2D_cote_y

	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        #groupe_rotation = inkex.etree.SubElement(liaison, 'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle=inkex.etree.SubElement(liaison,'g')



	
# Create effect instance and apply it.
effect = Liaisons()
effect.affect()
