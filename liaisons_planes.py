import math
import inkex
from liaisons_fonctions_utiles import *


def dessin_plane_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_plane_2D_cote_x
	y=options.liaison_plane_2D_cote_y
	#Orientation **************************************
	rotation=-options.liaison_plane_2D_cote_orientation #Angle par defaut (sens trigo)
	if(options.liaison_plane_2D_cote_axe=="y"):
		rotation=0
	elif(options.liaison_plane_2D_cote_axe=="x"):
		rotation=90
	elif(options.liaison_plane_2D_cote_axe=="-x"):
		rotation=-90
	elif(options.liaison_plane_2D_cote_axe=="-y"):
		rotation=180
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	largeur=30.
	ecart=5.
	longueurTige=10.
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	dessus=inkex.etree.SubElement(liaison,'g')
	dessous=inkex.etree.SubElement(liaison,'g')

	
	# DESSUS ***************************************
	#plan dessus
	planDessus=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-largeur/2	,	ecart/2.),
				(largeur/2	,	ecart/2.)	])
	planDessus.set('d',chemin)
	planDessus.set('stroke',couleur_male)
	planDessus.set('stroke-width',str(epaisseur_male))
	dessus.append(planDessus)
	
	#tige dessus
	tigeDessus=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(0	,	ecart/2.),
				(0	,	ecart/2.+longueurTige)	])
	tigeDessus.set('d',chemin)
	tigeDessus.set('stroke',couleur_male)
	tigeDessus.set('stroke-width',str(epaisseur_male))
	dessus.append(tigeDessus)
	
	# DESSOUS ***************************************
	#plan dessous
	planDessous=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-largeur/2	,	-ecart/2.),
				(largeur/2	,	-ecart/2.)	])
	planDessous.set('d',chemin)
	planDessous.set('stroke',couleur_femelle)
	planDessous.set('stroke-width',str(epaisseur_femelle))
	dessous.append(planDessous)
	
	#tige dessous
	tigeDessous=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(0	,	-ecart/2.),
				(0	,	-ecart/2.-longueurTige)	])
	tigeDessous.set('d',chemin)
	tigeDessous.set('stroke',couleur_femelle)
	tigeDessous.set('stroke-width',str(epaisseur_femelle))
	dessous.append(tigeDessous)
	
	# Transformations ***************************************
	dessus.set("transform","rotate("+str(rotation)+")")
	dessous.set("transform","rotate("+str(rotation)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")

	

def dessin_plane_2D_dessus(options,contexte):
	#Position *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_plane_2D_dessus_x
	y=options.liaison_plane_2D_dessus_y
	#Orientation **************************************
	rotationDessous=-options.liaison_plane_2D_orientation_dessous #Angle par defaut (sens trigo)
	if(options.liaison_plane_2D_axe_dessous=="x"):
		rotationDessous=0
	elif(options.liaison_plane_2D_axe_dessous=="y"):
		rotationDessous=-90
	elif(options.liaison_plane_2D_axe_dessous=="-x"):
		rotationDessous=180
	elif(options.liaison_plane_2D_axe_dessous=="-y"):
		rotationDessous=90
	rotationDessus=-options.liaison_plane_2D_orientation_dessus #Angle par defaut (sens trigo)
	if(options.liaison_plane_2D_axe_dessus=="x"):
		rotationDessus=0
	elif(options.liaison_plane_2D_axe_dessus=="y"):
		rotationDessus=-90
	elif(options.liaison_plane_2D_axe_dessus=="-x"):
		rotationDessus=180
	elif(options.liaison_plane_2D_axe_dessus=="-y"):
		rotationDessus=90
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	coteDessous=30.
	coteDessus=20.
	longueurTrait=10.
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	dessous=inkex.etree.SubElement(liaison,'g')
	dessus=inkex.etree.SubElement(liaison,'g')

	
	# Dessous ***************************************	
	# rectangle dessous
	rectangleDessous=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangleDessous.set('x',str(-coteDessous*echelle/2) )
	rectangleDessous.set('y',str(-coteDessous*echelle/2) )
	rectangleDessous.set('width',str(coteDessous*echelle))
	rectangleDessous.set('height',str(coteDessous*echelle))
	rectangleDessous.set('style','fill:white')
	rectangleDessous.set('stroke',couleur_femelle)
	rectangleDessous.set('stroke-width',str(epaisseur_femelle))
	dessous.append(rectangleDessous)

	traitDessous=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(coteDessous/2.	,	0),
				(coteDessous/2.+longueurTrait	,	0)	])
	traitDessous.set('d',chemin)
	traitDessous.set('stroke',couleur_femelle)
	traitDessous.set('stroke-width',str(epaisseur_femelle))
	dessous.append(traitDessous)
	
	# Dessus ***************************************
	# rectangle dessus
	rectangleDessus=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangleDessus.set('x',str(-coteDessus*echelle/2) )
	rectangleDessus.set('y',str(-coteDessus*echelle/2) )
	rectangleDessus.set('width',str(coteDessus*echelle))
	rectangleDessus.set('height',str(coteDessus*echelle))
	rectangleDessus.set('style','fill:white')
	rectangleDessus.set('stroke',couleur_male)
	rectangleDessus.set('stroke-width',str(epaisseur_male))
	dessus.append(rectangleDessus)

	traitDessus=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(coteDessus/2.	,	0),
				(coteDessous/2.+longueurTrait	,	0)	])
	traitDessus.set('d',chemin)
	traitDessus.set('stroke',couleur_male)
	traitDessus.set('stroke-width',str(epaisseur_male))
	dessus.append(traitDessus)
	
	# Transformations ***************************************
	dessous.set("transform","rotate("+str(rotationDessous)+")")
	dessus.set("transform","rotate("+str(rotationDessus)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
	






#===============================================================
def dessin_plane_3D(options,contexte):

	#Origine 2D
	x0=options.x0
	y0=options.y0
	#Base Axonometrique
	echelle=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques(echelle)
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x=options.liaison_plane_3D_position_x
	y=options.liaison_plane_3D_position_y
	z=options.liaison_plane_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	largeur=30.
	longueur_tige=25.
	ecart=2.5
	couleur_dessus=options.opt_gene_piece1_couleur
	couleur_dessous=options.opt_gene_piece2_couleur
	epaisseur_dessus=options.opt_gene_lignes_epaisseur_1
	epaisseur_dessous=options.opt_gene_lignes_epaisseur_2
	angle_dessus=-float(options.liaison_plane_3D_orientation1)/180.*math.pi
	angle_dessous=-float(options.liaison_plane_3D_orientation2)/180.*math.pi
	#Repere local de la liaison
	if(options.liaison_plane_3D_type_normale=="\"liaison_plane_3D_type_normale_quelconque\""):
		V=v3D(options.liaison_plane_3D_type_direction_quelconque_x,options.liaison_plane_3D_type_direction_quelconque_y,options.liaison_plane_3D_type_direction_quelconque_z,base)
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle,angle_dessus)#Repere male
		Vx2,Vy2,Vz2=getBaseFromVecteur(V,echelle,angle_dessous)#Repere Femelle
	else:	#Si vecteur standard
		if(options.liaison_plane_3D_axe=="x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle,angle_dessus)#Repere dessus
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vx,echelle,angle_dessous)#Repere dessous
		elif(options.liaison_plane_3D_axe=="y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle,angle_dessus)#Repere dessus
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vy,echelle,angle_dessous)#Repere dessous
		else:#z
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle,angle_dessus)#Repere dessus
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vz,echelle,angle_dessous)#Repere dessous
	baseLocale1=(Vx1,Vy1,Vz1)
	baseLocale2=(Vx2,Vy2,Vz2)

	# Dessus ***************************************
	planDessus=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(ecart,	-largeur/2.,	-largeur/2.	),
					(ecart,	-largeur/2.,	largeur/2.	),
					(ecart,	largeur/2.,	largeur/2.	),
					(ecart,	largeur/2.,	-largeur/2.	)
				],True,baseLocale1)
	planDessus.set('d',chemin)
	planDessus.set('stroke',couleur_dessus)
	planDessus.set('stroke-width',str(epaisseur_dessus))
	planDessus.set('style','fill:white')
	planDessus.set('profondeur',str(profondeur))
	

	tigeDessus=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(ecart,	0.,	0.	),
					(longueur_tige,	0.,	0.	)
				],False,baseLocale1)
	tigeDessus.set('d',chemin)
	tigeDessus.set('stroke',couleur_dessus)
	tigeDessus.set('stroke-width',str(epaisseur_dessus))
	tigeDessus.set('style','stroke-linecap:round')
	tigeDessus.set('profondeur',str(profondeur))
	
	# Dessous ***************************************
	planDessous=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-ecart,	-largeur/2.,	-largeur/2.	),
					(-ecart,	-largeur/2.,	largeur/2.	),
					(-ecart,	largeur/2.,	largeur/2.	),
					(-ecart,	largeur/2.,	-largeur/2.	)
				],True,baseLocale2)
	planDessous.set('d',chemin)
	planDessous.set('stroke',couleur_dessous)
	planDessous.set('stroke-width',str(epaisseur_dessous))
	planDessous.set('style','fill:white')
	planDessous.set('profondeur',str(profondeur))

	tigeDessous=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-ecart,	0.,	0.	),
					(-longueur_tige,	0.,	0.	)
				],False,baseLocale2)
	tigeDessous.set('d',chemin)
	tigeDessous.set('stroke',couleur_dessous)
	tigeDessous.set('stroke-width',str(epaisseur_dessous))
	tigeDessous.set('style','stroke-linecap:round')
	tigeDessous.set('profondeur',str(profondeur))
	


	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        listeObjets=[planDessous,tigeDessous,planDessus,tigeDessus]
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)
        
        
	# Transformations ***************************************
	liaison.set("transform","translate("+str(x0+x*Vx.x+y*Vy.x+z*Vz.x)+","+str(y0+x*Vx.y+y*Vy.y+z*Vz.y)+")")
	
