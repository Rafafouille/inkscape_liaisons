import math
import inkex
from lxml import etree	# Nécessaire pour les groupes depuis la version 1.0
from liaisons_fonctions_utiles import *
from liaisons_parametres import *


def dessin_Masse_2D(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_masse_2D_x
	y = -options.liaison_masse_2D_y
	#Parametres ****************************
	couleur = options.opt_gene_piece1_couleur
	epaisseur = options.opt_gene_lignes_epaisseur_1
	#Orientation **************************************
	rotation=-options.liaison_masse_2D_orientation_axe #Angle par defaut (sens trigo)
	if(options.liaison_masse_2D_axe=="x"):
		rotation=0
	elif(options.liaison_masse_2D_axe=="y"):
		rotation=-90
	elif(options.liaison_masse_2D_axe=="-x"):
		rotation=180
	elif(options.liaison_masse_2D_axe=="-y"):
		rotation=90

	#Groupes ******************************************
	liaison = etree.SubElement(contexte, 'g')
	masse = etree.SubElement(liaison,'g')
	#Base **************************
	echelle_liaison = options.echelle
	Vx1,Vy1 = getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	# DESSIN ***************************************
	#Trait principal
	trait=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-REF2D_longueur_tige,	-REF2D_largeur/2.),
					(-REF2D_longueur_tige,	REF2D_largeur/2.)	],
				False,base2D)
	trait.set('d',chemin)
	trait.set('stroke',couleur)
	trait.set('stroke-width',str(epaisseur))
	trait.set('style',"stroke-linecap:round")
	masse.append(trait)
	
	# Tige
	tige=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0,	0),
					(-REF2D_longueur_tige,	0)	],
				False,base2D)
	tige.set('d',chemin)
	tige.set('stroke',couleur)
	tige.set('stroke-width',str(epaisseur))
	masse.append(tige)
	
	# hachures
	pas = float(REF2D_largeur) / (REF2D_nombre_hachures-1)
	for i in range(REF2D_nombre_hachures):
		hachure=etree.Element(inkex.addNS('path','svg'))
		chemin=points2D_to_svgd([	(-REF2D_longueur_tige,	-REF2D_largeur/2. + i*pas),
						(-REF2D_longueur_tige-REF2D_longueur_hachures,	-REF2D_largeur/2. + i*pas + REF2D_longueur_hachures*math.tan(REF2D_inclinaison/180.*math.pi))	],
					False,base2D)
		hachure.set('d',chemin)
		hachure.set('stroke',couleur)
		hachure.set('stroke-width',str(epaisseur))
		hachure.set('style',"stroke-linecap:round")
		masse.append(hachure)
	
	# Transformations ***************************************

	masse.set("transform","rotate("+str(rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x,contexte))+","+str(convertLongueur2Inkscape(options,y0+y,contexte))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	








#===============================================================
def dessin_Masse_3D(options,contexte):
	#Origine 2D
	x0 = options.x0
	y0 = options.y0
	#Base Axonometrique
	echelle_liaison=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques()
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x = options.liaison_masse_3D_position_x
	y = options.liaison_masse_3D_position_y
	z = options.liaison_masse_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	couleur = options.opt_gene_piece1_couleur
	epaisseur = options.opt_gene_lignes_epaisseur_1
	pivotement = -float(options.liaison_masse_3D_pivotement)/180.*math.pi
	dessin_3D = options.liaison_masse_3D_representation

	#Repere local de la liaison
	if(options.liaison_masse_3D_type_axe=="liaison_masse_3D_type_axe_quelconque"):
		V=v3D(options.liaison_masse_3D_axe_quelconque_x,options.liaison_masse_3D_axe_quelconque_y,options.liaison_masse_3D_axe_quelconque_z,base)
		if V.x == V.y == V.z == 0 : V=v3D(1,0,0,base) #Si vecteur nul : on prend X par defaut
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle_liaison,pivotement)
	else:	#Si vecteur standard
		if(options.liaison_masse_3D_axe=="x"):
			Vx1,Vy1,Vz1 = getBaseFromVecteur(Vx,echelle_liaison,pivotement)
		elif(options.liaison_masse_3D_axe=="y"):
			Vx1,Vy1,Vz1 = getBaseFromVecteur(Vy,echelle_liaison,pivotement)
		elif(options.liaison_masse_3D_axe=="z"):
			Vx1,Vy1,Vz1 = getBaseFromVecteur(Vz,echelle_liaison,pivotement)
		elif(options.liaison_masse_3D_axe=="-x"):
			Vx1,Vy1,Vz1 = getBaseFromVecteur(-Vx,echelle_liaison,pivotement)
		elif(options.liaison_masse_3D_axe=="-y"):
			Vx1,Vy1,Vz1 = getBaseFromVecteur(-Vy,echelle_liaison,pivotement)
		elif(options.liaison_masse_3D_axe=="-z"):
			Vx1,Vy1,Vz1 = getBaseFromVecteur(-Vz,echelle_liaison,pivotement)
	baseLocale=(Vx1,Vy1,Vz1)
#	baseLocale=(Vx2,Vy2,Vz2)

	
	# Dessin ***************************************
	
	listeObjets=[]
	
	tige=etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	0,	0	),
					(-REF3D_longueur_tige,	0,	0	)
				],False,baseLocale)
	tige.set('d',chemin)
	tige.set('stroke',couleur)
	tige.set('stroke-width',str(epaisseur))
	tige.set('style','stroke-linecap:round')
	tige.set('profondeur',str(profondeur))
	listeObjets.append(tige)

	#DESSIN 3D
	if dessin_3D:
		plan=etree.Element(inkex.addNS('path','svg'))
		chemin,profondeur_trait=points3D_to_svgd([
					(-REF3D_longueur_tige,	REF3D_largeur/2.,	REF3D_largeur/2.	),
					(-REF3D_longueur_tige,	-REF3D_largeur/2.,	REF3D_largeur/2.	),
					(-REF3D_longueur_tige,	-REF3D_largeur/2.,	-REF3D_largeur/2.	),
					(-REF3D_longueur_tige,	REF3D_largeur/2.,	-REF3D_largeur/2.	)
				],True,baseLocale)
		plan.set('d',chemin)
		plan.set('stroke',couleur)
		plan.set('stroke-width',str(epaisseur))
		plan.set('fill','white')
		plan.set('profondeur',str(profondeur_trait))
		plan.set('style',"stroke-linejoin:round")
		listeObjets.append(plan)
		
		# hachures
		pas = float(REF3D_largeur) / (REF3D_nombre_hachures_3D-1)
		for i in range(REF3D_nombre_hachures_plat):
			for j in range(REF3D_nombre_hachures_plat):
				hachure=etree.Element(inkex.addNS('path','svg'))
				chemin,profondeur = points3D_to_svgd([	(-REF3D_longueur_tige,				-REF3D_largeur/2. + i*pas ,									-REF3D_largeur/2. + j*pas ),
									(-REF3D_longueur_tige-REF3D_longueur_hachures_3D,	-REF3D_largeur/2. + i*pas + REF3D_longueur_hachures_3D*math.tan(REF3D_inclinaison_3D/180.*math.pi),	-REF3D_largeur/2. + j*pas)	],
							False,baseLocale)
				hachure.set('d',chemin)
				hachure.set('stroke',couleur)
				hachure.set('stroke-width',str(epaisseur))
				hachure.set('style',"stroke-linecap:round")
				hachure.set('profondeur',str(2 * profondeur_trait))
				listeObjets.append(hachure)
	# DESSIN A PLAT
	else:
		trait=etree.Element(inkex.addNS('path','svg'))
		chemin,profondeur_trait=points3D_to_svgd([
					(-REF3D_longueur_tige,	-REF3D_largeur/2.,	0	),
					(-REF3D_longueur_tige,	REF3D_largeur/2.,	0	)
				],False,baseLocale)
		trait.set('d',chemin)
		trait.set('stroke',couleur)
		trait.set('stroke-width',str(epaisseur))
		trait.set('style','stroke-linecap:round')
		trait.set('profondeur',str(profondeur_trait))
		listeObjets.append(trait)
	
		# hachures
		pas = float(REF3D_largeur) / (REF3D_nombre_hachures_plat-1)
		for i in range(REF3D_nombre_hachures_plat):
			hachure=etree.Element(inkex.addNS('path','svg'))
			chemin,profondeur = points3D_to_svgd([	(-REF3D_longueur_tige,				-REF3D_largeur/2. + i*pas ,									0),
							(-REF3D_longueur_tige-REF3D_longueur_hachures_3D,	-REF3D_largeur/2. + i*pas + REF3D_longueur_hachures_plat*math.tan(REF3D_inclinaison_plat/180.*math.pi),	0)	],
						False,baseLocale)
			hachure.set('d',chemin)
			hachure.set('stroke',couleur)
			hachure.set('stroke-width',str(epaisseur))
			hachure.set('style',"stroke-linecap:round")
			hachure.set('profondeur',str(2 * profondeur_trait))
			listeObjets.append(hachure)

	# Ajout au Groupe ******************************************
	liaison = etree.SubElement(contexte, 'g')
	ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)
        
        
	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x,contexte))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y,contexte))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	
