import math
import inkex
from liaisons_fonctions_utiles import *


def dessin_Glissiere_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_glissiere_2D_cote_x
	y=options.liaison_glissiere_2D_cote_y
	#Orientation **************************************
	rotation=options.liaison_glissiere_2D_cote_orientation #Angle par defaut (sens trigo)
	if(options.liaison_glissiere_2D_cote_axe=="x"):
		rotation=0
	elif(options.liaison_glissiere_2D_cote_axe=="y"):
		rotation=90.
	elif(options.liaison_glissiere_2D_cote_axe=="-x"):
		rotation=180.
	elif(options.liaison_glissiere_2D_cote_axe=="-y"):
		rotation=-90.
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	old_liaisons=options.opt_gene_gene_old
	largeur=30.
	hauteur=15.
	longueur_axe=2.*largeur
	longueur_tige=hauteur/2.
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle=inkex.etree.SubElement(liaison,'g')

	# Male ***************************************
	#Ligne male
	ligneM=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-longueur_axe/2.,0),
					(longueur_axe/2.,0)]
				,False,base2D)
	ligneM.set('d',chemin)
	ligneM.set('stroke',couleur_male)
	ligneM.set('stroke-width',str(epaisseur_male))
	male.append(ligneM)
	
	
	# Femelle ***************************************

	#Rectangle
	rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-largeur*echelle/2) )
	rectangle.set('y',str(-hauteur*echelle/2) )
	rectangle.set('width',str(largeur*echelle))
	rectangle.set('height',str(hauteur*echelle))
	rectangle.set('style','fill:#FFFFFF')
	rectangle.set('stroke',couleur_femelle)
	rectangle.set('stroke-width',str(epaisseur_femelle))
	femelle.append(rectangle)
	
	#Ligne femelle
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	-hauteur/2.),
					(0	,	-hauteur/2.-longueur_tige)	]
				,False,base2D)
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle))
	femelle.append(ligneF)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(-rotation)+")")
	femelle.set("transform","rotate("+str(-rotation)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
	

def dessin_Glissiere_2D_face(options,contexte):
	#Position *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_glissiere_2D_face_x
	y=options.liaison_glissiere_2D_face_y
	#Orientation **************************************
	rotation=options.liaison_glissiere_2D_face_orientation #Angle par defaut (sens trigo)
	if(options.liaison_glissiere_2D_face_axe=="x"):
		rotation=0
	elif(options.liaison_glissiere_2D_face_axe=="y"):
		rotation=90.
	elif(options.liaison_glissiere_2D_face_axe=="-x"):
		rotation=180.
	elif(options.liaison_glissiere_2D_face_axe=="-y"):
		rotation=-90.
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres *********************
	profondeur=25.
	hauteur=15.
	longueur_tige=hauteur/2.
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1

	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte,'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle=inkex.etree.SubElement(liaison,'g')

	# Femelle ***************************************	
	#rectangle
	rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-profondeur*echelle/2) )
	rectangle.set('y',str(-hauteur*echelle/2) )
	rectangle.set('width',str(profondeur*echelle))
	rectangle.set('height',str(hauteur*echelle))
	rectangle.set('style','fill:none')
	rectangle.set('stroke',couleur_femelle)
	rectangle.set('stroke-width',str(epaisseur_femelle))
	femelle.append(rectangle)
	#cercle
	tige=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	hauteur/2.),
				(0,	hauteur/2.+longueur_tige)	]
				,False,base2D)
	tige.set('d',chemin)
	tige.set('stroke',couleur_femelle)
	tige.set('stroke-width',str(epaisseur_femelle))
	femelle.append(tige)
	
	# Male ***************************************
	#croisillon1
	croix1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-profondeur/2.+epaisseur_femelle/2	,	-hauteur/2.+epaisseur_femelle/2),
				(profondeur/2.-epaisseur_femelle/2,	hauteur/2.-epaisseur_femelle/2)	]
				,False,base2D)
	croix1.set('d',chemin)
	croix1.set('stroke',couleur_male)
	croix1.set('stroke-width',str(epaisseur_male))
	male.append(croix1)
	#croisillon2
	croix2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(profondeur/2.-epaisseur_femelle/2	,	-hauteur/2.+epaisseur_femelle/2),
				(-profondeur/2.+epaisseur_femelle/2,	hauteur/2.-epaisseur_femelle/2)	]
				,False,base2D)
	croix2.set('d',chemin)
	croix2.set('stroke',couleur_male)
	croix2.set('stroke-width',str(epaisseur_male))
	male.append(croix2)
	#Trait
	trait=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	0),
				((-hauteur/2.-longueur_tige)*math.sin(-rotation/180*math.pi),	-(hauteur/2.+longueur_tige)*math.cos(-rotation/180*math.pi))	]
				,False,base2D)
	trait.set('d',chemin)
	trait.set('stroke',couleur_male)
	trait.set('stroke-width',str(epaisseur_male))
	liaison.append(trait)
		
	# Transformations ***************************************
	male.set("transform","rotate("+str(-rotation)+")")
	femelle.set("transform","rotate("+str(-rotation)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
	






#===============================================================
def dessin_Glissiere_3D(options,contexte):
	#Origine 2D
	x0=options.x0
	y0=options.y0
	#Base Axonometrique
	echelle=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques(echelle)
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x=options.liaison_glissiere_3D_position_x
	y=options.liaison_glissiere_3D_position_y
	z=options.liaison_glissiere_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	epaisseur=20.
	hauteur=15.
	largeur=30.
	rayonTige=25.
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	angle=-float(options.liaison_glissiere_3D_orientation)/180.*math.pi
	#Repere local de la liaison
	if(options.liaison_glissiere_3D_type_direction=="\"liaison_glissiere_3D_type_direction_quelconque\""):
		V=v3D(options.liaison_glissiere_3D_type_direction_quelconque_x,options.liaison_glissiere_3D_type_direction_quelconque_y,options.liaison_glissiere_3D_type_direction_quelconque_z,base)
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle,angle)#Repere local
	else:	#Si vecteur standard
		if(options.liaison_glissiere_3D_axe=="x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle,angle)#Repere local
		elif(options.liaison_glissiere_3D_axe=="y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle,angle)#Repere local
		else:#z
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle,angle)#Repere local
	baseLocale=(Vx1,Vy1,Vz1)

	
	# Male ***************************************
	#Axe central
	axe=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur,	0,	0	),
					(largeur,	0,	0	)
				],False,baseLocale)
	axe.set('d',chemin)
	axe.set('stroke',couleur_male)
	axe.set('stroke-width',str(epaisseur_male))
	axe.set('style','stroke-linecap:round')
	axe.set('profondeur',str(profondeur))

	#Demi croisillon 1
	demicroix1=inkex.etree.Element(inkex.addNS('path','svg'))
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
	
	#Demi croisillon 2
	demicroix2=inkex.etree.Element(inkex.addNS('path','svg'))
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

	#Demi croisillon 3
	demicroix3=inkex.etree.Element(inkex.addNS('path','svg'))
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
	
	#Demi croisillon 4
	demicroix4=inkex.etree.Element(inkex.addNS('path','svg'))
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
	
	
	# Femelle ***************************************
	
	#pan1
	pan1=inkex.etree.Element(inkex.addNS('path','svg'))
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
	
	#pan2
	pan2=inkex.etree.Element(inkex.addNS('path','svg'))
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

	#pan3
	pan3=inkex.etree.Element(inkex.addNS('path','svg'))
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

	#pan4
	pan4=inkex.etree.Element(inkex.addNS('path','svg'))
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
	

	#barre femelle
	barreFemelle=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	0,	hauteur/2.	),
					(0,	0,	rayonTige)
				],False,baseLocale)
	barreFemelle.set('d',chemin)
	barreFemelle.set('stroke',couleur_femelle)
	barreFemelle.set('stroke-width',str(epaisseur_femelle))
	barreFemelle.set('style','stroke-linecap:round')
	barreFemelle.set('profondeur',str(profondeur*1000000))
	
	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        
        listeObjets=[pan1,pan2,pan3,pan4,axe,demicroix1,demicroix2,demicroix3,demicroix4,barreFemelle]
        
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)

	# Transformations ***************************************
	liaison.set("transform","translate("+str(x0+x*Vx.x+y*Vy.x+z*Vz.x)+","+str(y0+x*Vx.y+y*Vy.y+z*Vz.y)+")")
