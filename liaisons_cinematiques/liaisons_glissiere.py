import math
import inkex
from lxml import etree	# Nécessaire pour les groupes depuis la version 1.0
from liaisons_fonctions_utiles import *
from liaisons_parametres import *


def dessin_Glissiere_2D_cote(options,contexte):

	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_glissiere_2D_cote_x
	y = -options.liaison_glissiere_2D_cote_y
	#Orientation **************************************
	rotation=options.liaison_glissiere_2D_cote_direction_quelconque #Angle par defaut (sens trigo)
	if(options.liaison_glissiere_2D_cote_direction_standard=="x"):
		rotation=0
	elif(options.liaison_glissiere_2D_cote_direction_standard=="y"):
		rotation=90.
	elif(options.liaison_glissiere_2D_cote_direction_standard=="-x"):
		rotation=180.
	elif(options.liaison_glissiere_2D_cote_direction_standard=="-y"):
		rotation=-90.
	#Base *********************
	echelle_liaison=options.echelle
	Vx1,Vy1=getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	old_liaisons=options.opt_gene_gene_old
	largeur=g2Dc_longueur
	hauteur=g2Dc_hauteur
	longueur_axe=g2Dc_longueur_male
	longueur_tige=g2Dc_longueur_tige_femelle
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
	liaison = etree.SubElement(contexte, 'g')
	male=etree.SubElement(liaison,'g')
	femelle=etree.SubElement(liaison,'g')

	# Male ***************************************
	#Ligne male
	ligneM=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-longueur_axe/2.,0),
					(longueur_axe/2.,0)]
				,False,base2D)
	ligneM.set('d',chemin)
	ligneM.set('stroke',couleur_male)
	ligneM.set('stroke-width',str(epaisseur_male))
	male.append(ligneM)
	
	
	# Femelle ***************************************

	#Rectangle
	rectangle=etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-largeur*echelle_liaison/2) )
	rectangle.set('y',str(-hauteur*echelle_liaison/2) )
	rectangle.set('width',str(largeur*echelle_liaison))
	rectangle.set('height',str(hauteur*echelle_liaison))
	rectangle.set('style','fill:#FFFFFF')
	rectangle.set('stroke',couleur_femelle)
	rectangle.set('stroke-width',str(epaisseur_femelle))
	femelle.append(rectangle)
	
	#Ligne femelle
	ligneF=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	hauteur/2.),
					(0	,	hauteur/2.+longueur_tige)	]
				,False,base2D)
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle))
	femelle.append(ligneF)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(-rotation)+")")
	femelle.set("transform","rotate("+str(-rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x,contexte))+","+str(convertLongueur2Inkscape(options,y0+y,contexte))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	

def dessin_Glissiere_2D_face(options,contexte):
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_glissiere_2D_face_x
	y = -options.liaison_glissiere_2D_face_y
	#Orientation **************************************
	rotation=options.liaison_glissiere_2D_face_orientation_quelconque_femelle-90 #Angle par defaut (sens trigo)
	if(options.liaison_glissiere_2D_face_orientation_standard_femelle == "x"):
		rotation = -90.
	elif(options.liaison_glissiere_2D_face_orientation_standard_femelle == "y"):
		rotation = 0.
	elif(options.liaison_glissiere_2D_face_orientation_standard_femelle == "-x"):
		rotation = 90.
	elif(options.liaison_glissiere_2D_face_orientation_standard_femelle == "-y"):
		rotation = 180.
	rotation_tige_male = -90+options.liaison_glissiere_2D_face_orientation_quelconque_male
	if(options.liaison_glissiere_2D_face_orientation_standard_male != "autre"):
		rotation_tige_male = rotation+int(options.liaison_glissiere_2D_face_orientation_standard_male)
#	assert 0,rotation_tige_male
	#Base *********************
	echelle_liaiaon = options.echelle
	Vx1, Vy1 = getBase2D(echelle_liaiaon)
	base2D = (Vx1,Vy1)
	#Parametres *********************
	profondeur = g2Df_largeur
	hauteur = g2Df_hauteur
	longueur_tige_femelle = g2Df_longueur_tige_femelle
	longueur_tige_male = g2Df_longueur_tige_male
	couleur_femelle = options.opt_gene_piece2_couleur
	couleur_male = options.opt_gene_piece1_couleur
	epaisseur_femelle = options.opt_gene_lignes_epaisseur_2
	epaisseur_male = options.opt_gene_lignes_epaisseur_1
	#Groupes ******************************************
	liaison = etree.SubElement(contexte,'g')
	male = etree.SubElement(liaison,'g')
	femelle = etree.SubElement(liaison,'g')

	# Femelle ***************************************	
	#rectangle
	rectangle=etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-profondeur*echelle_liaiaon/2) )
	rectangle.set('y',str(-hauteur*echelle_liaiaon/2) )
	rectangle.set('width',str(profondeur*echelle_liaiaon))
	rectangle.set('height',str(hauteur*echelle_liaiaon))
	rectangle.set('style','fill:none')
	rectangle.set('stroke',couleur_femelle)
	rectangle.set('stroke-width',str(epaisseur_femelle))
	femelle.append(rectangle)
	#cercle
	tige=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	hauteur/2.),
				(0,	hauteur/2.+longueur_tige_femelle)	]
				,False,base2D)
	tige.set('d', chemin)
	tige.set('stroke', couleur_femelle)
	tige.set('stroke-width', str(epaisseur_femelle))
	femelle.append(tige)
	
	# Male ***************************************
	#croisillon1
	croix1=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-profondeur/2.+epaisseur_femelle/2	,	-hauteur/2.+epaisseur_femelle/2),
					(profondeur/2.-epaisseur_femelle/2,	hauteur/2.-epaisseur_femelle/2)	]
				,False,base2D)
	croix1.set('d',chemin)
	croix1.set('stroke',couleur_male)
	croix1.set('stroke-width',str(epaisseur_male))
	male.append(croix1)
	#croisillon2
	croix2=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(profondeur/2.-epaisseur_femelle/2	,	-hauteur/2.+epaisseur_femelle/2),
					(-profondeur/2.+epaisseur_femelle/2,	hauteur/2.-epaisseur_femelle/2)	]
				,False,base2D)
	croix2.set('d',chemin)
	croix2.set('stroke',couleur_male)
	croix2.set('stroke-width', str(epaisseur_male))
	male.append(croix2)
	#Trait
	trait=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	0),
					(longueur_tige_male*math.sin(-rotation_tige_male/180*math.pi),	longueur_tige_male*math.cos(rotation_tige_male/180*math.pi))	]
				,False,base2D)
	trait.set('d',chemin)
	trait.set('stroke',couleur_male)
	trait.set('stroke-width',str(epaisseur_male))
	liaison.append(trait)
		
	# Transformations ***************************************
	male.set("transform","rotate("+str(-rotation)+")")
	femelle.set("transform","rotate("+str(-rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x,contexte))+","+str(convertLongueur2Inkscape(options,y0+y,contexte))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






#===============================================================
def dessin_Glissiere_3D(options,contexte):
	#Origine 2D ********
	x0=options.x0
	y0=options.y0
	#Base Axonometrique *******
	echelle_liaison = options.echelle
	Vx,Vy,Vz = getVecteursAxonometriques()
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D *******
	x = options.liaison_glissiere_3D_position_x
	y = options.liaison_glissiere_3D_position_y
	z = options.liaison_glissiere_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison ******
	epaisseur = g3D_largeur
	hauteur = g3D_hauteur
	largeur = g3D_longueur
	longueur_male = g3D_longueur_male
	longueur_tige_femelle = g3D_longueur_tige_femelle
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	angle=-float(options.liaison_glissiere_3D_orientation)/180.*math.pi
	
	#Repere local de la liaison
	if(options.liaison_glissiere_3D_type_direction=="liaison_glissiere_3D_type_direction_quelconque"):
		V=v3D(options.liaison_glissiere_3D_type_direction_quelconque_x,options.liaison_glissiere_3D_type_direction_quelconque_y,options.liaison_glissiere_3D_type_direction_quelconque_z,base)
		if V.x == V.y == V.z == 0 : V=v3D(1,0,0,base) #Si vecteur nul : on prend X par defaut
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle_liaison,angle)#Repere local
	else:	#Si vecteur standard
		if(options.liaison_glissiere_3D_axe=="x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle_liaison,angle)#Repere local
		elif(options.liaison_glissiere_3D_axe=="y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle_liaison,angle)#Repere local
		else:#z
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle_liaison,angle)#Repere local
	baseLocale=(Vx1,Vy1,Vz1)

	listeObjets = []
	
	# Male ***************************************
	#Axe central
	axe=etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-longueur_male/2.,	0,	0	),
					(longueur_male/2.,	0,	0	)
				],False,baseLocale)
	axe.set('d',chemin)
	axe.set('stroke',couleur_male)
	axe.set('stroke-width',str(epaisseur_male))
	axe.set('style','stroke-linecap:round')
	axe.set('profondeur',str(profondeur))
	listeObjets.append(axe)


	if(options.liaison_glissiere_3D_representation) : # Si croisillon 3D
		#	Demi croisillon 1
		demicroix1=etree.Element(inkex.addNS('path','svg'))
		chemin,profondeur=points3D_to_svgd([
						(-largeur/2.,	0,	0	),
						(-largeur/2.,	-epaisseur/2.+epaisseur_femelle/2.,	hauteur/2.-epaisseur_femelle/2.	),
						(largeur/2.,	-epaisseur/2.+epaisseur_femelle/2.,	hauteur/2.-epaisseur_femelle/2.	),
						(largeur/2.,	0	,0	),
					],True,baseLocale)
		demicroix1.set('d',chemin)
		demicroix1.set('stroke',couleur_male)
		demicroix1.set('stroke-width',str(epaisseur_male))
		demicroix1.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
		demicroix1.set('profondeur',str(profondeur))
		listeObjets.append(demicroix1)
		
		#Demi croisillon 2
		demicroix2=etree.Element(inkex.addNS('path','svg'))
		chemin,profondeur=points3D_to_svgd([
						(-largeur/2.,	0,	0	),
						(-largeur/2.,	epaisseur/2.-epaisseur_femelle/2.,	hauteur/2.-epaisseur_femelle/2.	),
						(largeur/2.,	epaisseur/2.-epaisseur_femelle/2.,	hauteur/2.-epaisseur_femelle/2.	),
						(largeur/2.,	0	,0	),
					],True,baseLocale)
		demicroix2.set('d',chemin)
		demicroix2.set('stroke',couleur_male)
		demicroix2.set('stroke-width',str(epaisseur_male))
		demicroix2.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
		demicroix2.set('profondeur',str(profondeur))
		listeObjets.append(demicroix2)

		#Demi croisillon 3
		demicroix3=etree.Element(inkex.addNS('path','svg'))
		chemin,profondeur=points3D_to_svgd([
						(-largeur/2.,	0,	0	),
						(-largeur/2.,	epaisseur/2.-epaisseur_femelle/2.,	-hauteur/2.+epaisseur_femelle/2.	),
						(largeur/2.,	epaisseur/2.-epaisseur_femelle/2.,	-hauteur/2.+epaisseur_femelle/2.	),
						(largeur/2.,	0	,0	),
					],True,baseLocale)
		demicroix3.set('d',chemin)
		demicroix3.set('stroke',couleur_male)
		demicroix3.set('stroke-width',str(epaisseur_male))
		demicroix3.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
		demicroix3.set('profondeur',str(profondeur))
		listeObjets.append(demicroix3)
		
		#Demi croisillon 4
		demicroix4=etree.Element(inkex.addNS('path','svg'))
		chemin,profondeur=points3D_to_svgd([
						(-largeur/2.,	0,	0	),
						(-largeur/2.,	-epaisseur/2.+epaisseur_femelle/2.,	-hauteur/2.+epaisseur_femelle/2.	),
						(largeur/2.,	-epaisseur/2.+epaisseur_femelle/2.,	-hauteur/2.+epaisseur_femelle/2.	),
						(largeur/2.,	0	,0	),
					],True,baseLocale)
		demicroix4.set('d',chemin)
		demicroix4.set('stroke',couleur_male)
		demicroix4.set('stroke-width',str(epaisseur_male))
		demicroix4.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
		demicroix4.set('profondeur',str(profondeur))
		listeObjets.append(demicroix4)
	
	else : #Si croisillon pas 3D
		
		#croisillon 1
		croix1=etree.Element(inkex.addNS('path','svg'))
		chemin,profondeur=points3D_to_svgd([
						(-largeur/2.,	-epaisseur/2.+(epaisseur_femelle+epaisseur_male)/2.,	-hauteur/2.+(epaisseur_femelle+epaisseur_male)/2.	),
						(-largeur/2.,	epaisseur/2.-(epaisseur_femelle+epaisseur_male)/2.,	hauteur/2.-(epaisseur_femelle+epaisseur_male)/2.	)
					],False,baseLocale)
		croix1.set('d',chemin)
		croix1.set('stroke',couleur_male)
		croix1.set('stroke-width',str(epaisseur_male))
		croix1.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
		croix1.set('profondeur',str(profondeur))
		listeObjets.append(croix1)
		
		
		#croisillon 2
		croix2 = etree.Element(inkex.addNS('path','svg'))
		chemin,profondeur=points3D_to_svgd([
						(-largeur/2.,	epaisseur/2.-(epaisseur_femelle+epaisseur_male)/2.,	-hauteur/2.+(epaisseur_femelle+epaisseur_male)/2.	),
						(-largeur/2.,	-epaisseur/2.+(epaisseur_femelle+epaisseur_male)/2.,	hauteur/2.-(epaisseur_femelle+epaisseur_male)/2.	)
					],False,baseLocale)
		croix2.set('d',chemin)
		croix2.set('stroke',couleur_male)
		croix2.set('stroke-width',str(epaisseur_male))
		croix2.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
		croix2.set('profondeur',str(profondeur))
		listeObjets.append(croix2)
	
	
		#croisillon 3
		croix3 = etree.Element(inkex.addNS('path','svg'))
		chemin,profondeur=points3D_to_svgd([
						(largeur/2.,	epaisseur/2.-(epaisseur_femelle+epaisseur_male)/2.,	-hauteur/2.+(epaisseur_femelle+epaisseur_male)/2.	),
						(largeur/2.,	-epaisseur/2.+(epaisseur_femelle+epaisseur_male)/2.,	hauteur/2.-(epaisseur_femelle+epaisseur_male)/2.	)
					],False,baseLocale)
		croix3.set('d',chemin)
		croix3.set('stroke',couleur_male)
		croix3.set('stroke-width',str(epaisseur_male))
		croix3.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
		croix3.set('profondeur',str(profondeur))
		listeObjets.append(croix3)
		
		
		#croisillon 4
		croix4=etree.Element(inkex.addNS('path','svg'))
		chemin,profondeur=points3D_to_svgd([
						(largeur/2.,	-epaisseur/2.+(epaisseur_femelle+epaisseur_male)/2.,	-hauteur/2.+(epaisseur_femelle+epaisseur_male)/2.	),
						(largeur/2.,	epaisseur/2.-(epaisseur_femelle+epaisseur_male)/2.,	hauteur/2.-(epaisseur_femelle+epaisseur_male)/2.	)
					],False,baseLocale)
		croix4.set('d',chemin)
		croix4.set('stroke',couleur_male)
		croix4.set('stroke-width',str(epaisseur_male))
		croix4.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
		croix4.set('profondeur',str(profondeur))
		listeObjets.append(croix4)
	
	# Femelle ***************************************
	
	#pan1
	pan1=etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.,	-epaisseur/2.,	hauteur/2.	),
					(largeur/2.,	-epaisseur/2.,	hauteur/2.	),
					(largeur/2.,	epaisseur/2.,	hauteur/2.	),
					(-largeur/2.,	epaisseur/2.,	hauteur/2.	)
				],True,baseLocale)
	pan1.set('d',chemin)
	pan1.set('stroke',couleur_femelle)
	pan1.set('stroke-width',str(epaisseur_femelle))
	pan1.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
	pan1.set('profondeur',str(profondeur*1000))
	listeObjets.append(pan1)
	
	#pan2
	pan2=etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.,	epaisseur/2.,	hauteur/2.	),
					(largeur/2.,	epaisseur/2.,	hauteur/2.	),
					(largeur/2.,	epaisseur/2.,	-hauteur/2.	),
					(-largeur/2.,	epaisseur/2.,	-hauteur/2.	)
				],True,baseLocale)
	pan2.set('d',chemin)
	pan2.set('stroke',couleur_femelle)
	pan2.set('stroke-width',str(epaisseur_femelle))
	pan2.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
	pan2.set('profondeur',str(profondeur*1000))
	listeObjets.append(pan2)

	#pan3
	pan3=etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.,	-epaisseur/2.,	-hauteur/2.	),
					(largeur/2.,	-epaisseur/2.,	-hauteur/2.	),
					(largeur/2.,	epaisseur/2.,	-hauteur/2.	),
					(-largeur/2.,	epaisseur/2.,	-hauteur/2.	)
				],True,baseLocale)
	pan3.set('d',chemin)
	pan3.set('stroke',couleur_femelle)
	pan3.set('stroke-width',str(epaisseur_femelle))
	pan3.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
	pan3.set('profondeur',str(profondeur*1000))
	listeObjets.append(pan3)

	#pan4
	pan4=etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.,	-epaisseur/2.,	hauteur/2.	),
					(largeur/2.,	-epaisseur/2.,	hauteur/2.	),
					(largeur/2.,	-epaisseur/2.,	-hauteur/2.	),
					(-largeur/2.,	-epaisseur/2.,	-hauteur/2.	)
				],True,baseLocale)
	pan4.set('d',chemin)
	pan4.set('stroke',couleur_femelle)
	pan4.set('stroke-width',str(epaisseur_femelle))
	pan4.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
	pan4.set('profondeur',str(profondeur*1000))
	listeObjets.append(pan4)
	

	#barre femelle
	barreFemelle=etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	0,	hauteur/2.	),
					(0,	0,	hauteur/2. + longueur_tige_femelle)
				],False,baseLocale)
	barreFemelle.set('d',chemin)
	barreFemelle.set('stroke',couleur_femelle)
	barreFemelle.set('stroke-width',str(epaisseur_femelle))
	barreFemelle.set('style','stroke-linecap:round')
	barreFemelle.set('profondeur',str(profondeur*1000000))
	listeObjets.append(barreFemelle)
	
	# Ajout au Groupe ******************************************
	liaison = etree.SubElement(contexte, 'g')
        
	#listeObjets=[pan1,pan2,pan3,pan4,axe,demicroix1,demicroix2,demicroix3,demicroix4,barreFemelle]
        
	ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)

	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x,contexte))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y,contexte))+")")
	
	# Credits **************************************
	liaison.set("credits",options.credits)
