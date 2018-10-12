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

        self.OptionParser.add_option('--liaison_pivot3D_axe', action = 'store', type = 'str', dest = 'liaison_pivot3D_axe', default = 'x', help = u"Orientation de l'axe de la pivot")

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
		elif(type_liaison=="\"liaison_pivot_3D\""):
			dessin_Pivot_3D(self.options,svg)
	
	
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
		
	def prodSca(self,v2):
		"""Prod scalaire entre ce vecteur et un autre"""
		return self.x*v2.x+self.y*v2.y
		
	def copy(self):
		return v2D(self.x,self.y)
		
class v3D:
	def __init__(self,_x,_y,_z,_base=None):
		self.x=_x
		self.y=_y
		self.z=_z
		self.base=_base
		
		
	def setBase(self,_b):
		self.base=_b
		
	def str(self):
		return "["+str(self.x)+","+str(self.y)+","+str(self.y)+"]"

	def copy(self):
		return v3D(self.x,self.y,self.z)
		
	def getProjX(self):
		return self.x*self.base[0].x+self.y*self.base[1].x+self.z*self.base[2].x
	def getProjY(self):
		return self.x*self.base[0].y+self.y*self.base[1].y+self.z*self.base[2].y
	def getVec2DProj(self):
		return v2D(self.getProjX(),self.getProjY())
		
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
    
def points3D_to_svgd(base3D,p3D, close=True):
    """ convert list of points (x,y) pairs
        into a closed SVG path list
        base 3D est un triplet de vecteurs projetes dans le plan (eventuellement, on peut y rajouter l'axe z, mais cela n'intervient pas)
    """
    (Vx,Vy,Vz)=base3D
    p=[]
    for point in p3D:
    	p.append( (point[0]*Vx.x+point[1]*Vy.x+point[2]*Vz.x	,	point[0]*Vx.y+point[1]*Vy.y+point[2]*Vz.y) )
    return points_to_svgd(p,close)
  
#def recherchePointsEloignes(v,l):
#	"""Cherche les indices des points les plus eloignes par rapport a une droite.
#	v=vecteur directeur de la droite qui definit l'origine
#	"""
#	imax=imin=0
#	vn=v2D(-v.y,v.x)
#	vvv=v2D(l[0][0],l[0][1])#Coordonnees 1er point
#	mini=maxi=vn.prodSca(vvv)
#	for i in range(1,len(l)):
#		p=l[i]
#		vvv=v2D(p[0],p[1])
#		d=vn.prodSca(vvv)
#		if d>maxi:
#			maxi=d
#			imax=i
#		if d<mini:
#			mini=d
#			imin=i
#	return imax,imin
			
	
	

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
	x=options.liaison_pivot_2D_face_x
	y=options.liaison_pivot_2D_face_y
	rayon=15./2
	couleur_femelle="red"#getCouleurFromInt(options.opt_gene_piece2_couleur)
	couleur_male="blue"#getCouleurFromInt(options.opt_gene_piece1_couleur)
	epaisseur_femelle=3
	epaisseur_male=1
	rotation1=-options.liaison_pivot2D_face_orientation1 #Angle par defaut (sens trigo)
	if(options.liaison_pivot2D_face_axe1=="x"):
		rotation1=0
	elif(options.liaison_pivot2D_face_axe1=="y"):
		rotation1=-90
	elif(options.liaison_pivot2D_face_axe1=="-x"):
		rotation1=180
	elif(options.liaison_pivot2D_face_axe1=="-y"):
		rotation1=90
	rotation2=-options.liaison_pivot2D_face_orientation2 #Angle par defaut (sens trigo)
	if(options.liaison_pivot2D_face_axe2=="x"):
		rotation2=0
	elif(options.liaison_pivot2D_face_axe2=="y"):
		rotation2=-90
	elif(options.liaison_pivot2D_face_axe2=="-x"):
		rotation2=180
	elif(options.liaison_pivot2D_face_axe2=="-y"):
		rotation2=90
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        #groupe_rotation = inkex.etree.SubElement(liaison, 'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle=inkex.etree.SubElement(liaison,'g')

	# Male ***************************************
	axe1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(0	,	0),
				(2*rayon,	0)	])
	axe1.set('d',chemin)
	axe1.set('stroke',couleur_male)
	axe1.set('stroke-width',str(epaisseur_male))
	male.append(axe1)
	
	# Femelle ***************************************	
	#axe
	axe2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(0	,	0),
				(2*rayon,	0)	])
	axe2.set('d',chemin)
	axe2.set('stroke',couleur_femelle)
	axe2.set('stroke-width',str(epaisseur_femelle))
	femelle.append(axe2)
	#cercle
	cercle=inkex.etree.Element(inkex.addNS('circle','svg'))
	cercle.set('cx',"0")
	cercle.set('cy',"0")
	cercle.set('r',str(rayon))
	cercle.set('stroke',str(couleur_femelle))
	cercle.set('stroke-width',str(epaisseur_femelle))
	cercle.set('style','fill:white')
	femelle.append(cercle)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation1)+")")
	femelle.set("transform","rotate("+str(rotation2)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
	


	
def dessin_Pivot_3D(options,contexte):
	largeur=30.*math.sqrt(2./3)
	rayon=7.5*math.sqrt(2./3)
	couleur_femelle="red"#getCouleurFromInt(options.opt_gene_piece2_couleur)
	couleur_male="blue"#getCouleurFromInt(options.opt_gene_piece1_couleur)
	epaisseur_femelle=2
	epaisseur_male=1
	#Base de Vecteur ******************************************
	Vx=v3D(	-math.sqrt(2./3)*math.cos(math.pi/6),	math.sqrt(2./3)*math.sin(math.pi/6),	math.sqrt(2./3)*math.tan(math.acos(math.sqrt(2/3))))
	Vy=v3D(	math.sqrt(2./3)*math.cos(math.pi/6),	math.sqrt(2./3)*math.sin(math.pi/6),	math.sqrt(2./3)*math.tan(math.acos(math.sqrt(2/3))))
	Vz=v3D(	0,				math.sqrt(2./3),			math.sqrt(2./3)*math.tan(math.acos(math.sqrt(2./3))))
	#Repere local de la liaison
	if(options.liaison_pivot3D_axe=="x"):
		Vx1=Vx.copy()
		Vy1=Vy.copy()
		Vz1=Vz.copy()
	elif(options.liaison_pivot3D_axe=="y"):
		Vx1=Vy.copy()
		Vy1=Vz.copy()
		Vz1=Vx.copy()
	else:
		Vx1=Vz.copy()
		Vy1=Vx.copy()
		Vz1=Vy.copy()
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	femelle_derriere=inkex.etree.SubElement(liaison,'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle_devant=inkex.etree.SubElement(liaison,'g')
	
	# Male ***************************************
	axe=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points3D_to_svgd((Vx1,Vy1,Vz1),[
					(-largeur,	0,	0	),
					(largeur,	0,	0	)
				])
	axe.set('d',chemin)
	axe.set('stroke',couleur_male)
	axe.set('stroke-width',str(epaisseur_male))
	male.append(axe)
	arret1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points3D_to_svgd((Vx1,Vy1,Vz1),[
					(2*largeur/3,	rayon,	0	),
					(2*largeur/3,	-rayon,	0	)
				])
	arret1.set('d',chemin)
	arret1.set('stroke',couleur_male)
	arret1.set('stroke-width',str(epaisseur_male))
	male.append(arret1)
	arret2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points3D_to_svgd((Vx1,Vy1,Vz1),[
					(-2*largeur/3,	rayon,	0	),
					(-2*largeur/3,	-rayon,	0	)
				])
	arret2.set('d',chemin)
	arret2.set('stroke',couleur_male)
	arret2.set('stroke-width',str(epaisseur_male))
	male.append(arret2)
	
	# Femelle ***************************************


 	#Recherche des points extremes de l'ellipse
	theta1=theta2=None
	dist=distPrec=distPrecPrec=0
	dtheta=math.pi/30.
	theta=0.
	vNormal=v2D(Vx1.x,Vx1.y)	#Vecteur normal au vecteur directeur projete dans le plan, de l'axe de la pivot
	vNormal.rotation(math.pi/2.)
	while theta1==None or theta2==None:
		point3D=v3D(largeur/2.,rayon*math.cos(theta),rayon*math.sin(theta),(Vx1,Vy1,Vz1))
		point2D=point3D.getVec2DProj()
		dist,distPrec,distPrecPrec=point2D.prodSca(vNormal),dist,distPrec
		
		if dist<distPrec and distPrec>distPrecPrec:
			theta1=theta-dtheta
		elif dist>distPrec and distPrec<distPrecPrec:#A SUPPRIMER On n'a pas besoin de theta2
			theta2=theta-dtheta
		
		
		theta+=dtheta
		

	nbPoints=8
	#Objectif : Creer des cercles en 3D et les couper en deux chacun
	listeDemiCercle1sup=[]
	listeDemiCercle1inf=[]
	listeDemiCercle2sup=[]
	listeDemiCercle2inf=[]
	theta=0
	while theta<=math.pi:
		listeDemiCercle1sup.append((largeur/2.,rayon*math.cos(theta1+theta),rayon*math.sin(theta1+theta)))
		listeDemiCercle1inf.append((largeur/2.,rayon*math.cos(theta1-theta),rayon*math.sin(theta1-theta)))
		listeDemiCercle2sup.append((-largeur/2.,rayon*math.cos(theta1+theta),rayon*math.sin(theta1+theta)))
		listeDemiCercle2inf.append((-largeur/2.,rayon*math.cos(theta1-theta),rayon*math.sin(theta1-theta)))
		theta+=0.5
	
	
	listeDerriere=listeDemiCercle1inf
	listeDerriere+=[(largeur/2.,rayon*math.cos(theta1+math.pi),rayon*math.sin(theta1+math.pi)),(-largeur/2.,rayon*math.cos(theta1+math.pi),rayon*math.sin(theta1+math.pi))]
	listeDemiCercle2inf.reverse()
	listeDerriere+=listeDemiCercle2inf
	listeDerriere+=[(-largeur/2.,rayon*math.cos(theta1),rayon*math.sin(theta1)),(largeur/2.,rayon*math.cos(theta1),rayon*math.sin(theta1))]

	listeDevant=listeDemiCercle1sup
	listeDevant+=[(largeur/2.,rayon*math.cos(theta1+math.pi),rayon*math.sin(theta1+math.pi)),(-largeur/2.,rayon*math.cos(theta1+math.pi),rayon*math.sin(theta1+math.pi))]
	listeDemiCercle2sup.reverse()
	listeDevant+=listeDemiCercle2sup
	listeDevant+=[(-largeur/2.,rayon*math.cos(theta1),rayon*math.sin(theta1)),(largeur/2.,rayon*math.cos(theta1),rayon*math.sin(theta1))]
	
	
	
	pathDerriere=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points3D_to_svgd((Vx1,Vy1,Vz1),listeDerriere)
	pathDerriere.set('d',chemin)
	pathDerriere.set('stroke',couleur_femelle)
	pathDerriere.set('stroke-width',str(epaisseur_femelle))
	pathDerriere.set('style','fill:white')
	#cercle1.set('sodipodi:nodetypes','s'*nbPoints)
	femelle_derriere.append(pathDerriere)
	
	pathDevant=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points3D_to_svgd((Vx1,Vy1,Vz1),listeDevant)
	pathDevant.set('d',chemin)
	pathDevant.set('stroke',couleur_femelle)
	pathDevant.set('stroke-width',str(epaisseur_femelle))
	pathDevant.set('style','fill:white')
	#cercle1.set('sodipodi:nodetypes','s'*nbPoints)
	femelle_devant.append(pathDevant)
	
#	cercle1sup=inkex.etree.Element(inkex.addNS('path','svg'))
#	chemin=points3D_to_svgd((Vx1,Vy1,Vz1),listeDemiCercle1sup,False)
#	cercle1sup.set('d',chemin)
#	cercle1sup.set('stroke',couleur_femelle)
#	cercle1sup.set('stroke-width',str(epaisseur_femelle))
#	cercle1sup.set('style','fill:none')
#	#cercle1.set('sodipodi:nodetypes','s'*nbPoints)
#	femelle_devant.append(cercle1sup)
	
#	cercle1inf=inkex.etree.Element(inkex.addNS('path','svg'))
#	chemin=points3D_to_svgd((Vx1,Vy1,Vz1),listeDemiCercle1inf,False)
#	cercle1inf.set('d',chemin)
#	cercle1inf.set('stroke',couleur_femelle)
#	cercle1inf.set('stroke-width',str(epaisseur_femelle))
#	cercle1inf.set('style','fill:none')
	#cercle1.set('sodipodi:nodetypes','s'*nbPoints)
#	femelle_derriere.append(cercle1inf)
	
#	cercle2sup=inkex.etree.Element(inkex.addNS('path','svg'))
#	chemin=points3D_to_svgd((Vx1,Vy1,Vz1),listeDemiCercle2sup,False)
#	cercle2sup.set('d',chemin)
#	cercle2sup.set('stroke',couleur_femelle)
#	cercle2sup.set('stroke-width',str(epaisseur_femelle))
#	cercle2sup.set('style','fill:none')
#	#cercle2.set('sodipodi:nodetypes','s'*nbPoints)
#	femelle_devant.append(cercle2sup)
	
# 	cercle2inf=inkex.etree.Element(inkex.addNS('path','svg'))
#	chemin=points3D_to_svgd((Vx1,Vy1,Vz1),listeDemiCercle2inf,False)
#	cercle2inf.set('d',chemin)
#	cercle2inf.set('stroke',couleur_femelle)
#	cercle2inf.set('stroke-width',str(epaisseur_femelle))
#	cercle2inf.set('style','fill:none')
	#cercle2.set('sodipodi:nodetypes','s'*nbPoints)
#	femelle_derriere.append(cercle2inf)
	
	
# Create effect instance and apply it.
effect = Liaisons()
effect.affect()
