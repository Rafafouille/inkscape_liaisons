import math
import inkex
from liaisons_fonctions_utiles import *
from liaisons_parametres import *


def dessin_rectiligne_plan_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_plane_2D_cote_x
	y=options.liaison_plane_2D_cote_y
	#Orientation **************************************
	rotation=-options.liaison_rectiligne_2D_cote_orientation_normale #Angle par defaut (sens trigo)
	if(options.liaison_rectiligne_cote_axe_normale=="y"):
		rotation=-90
	elif(options.liaison_rectiligne_cote_axe_normale=="x"):
		rotation=0
	elif(options.liaison_rectiligne_cote_axe_normale=="-x"):
		rotation=180
	elif(options.liaison_rectiligne_cote_axe_normale=="-y"):
		rotation=90
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	dessus=inkex.etree.SubElement(liaison,'g')
	dessous=inkex.etree.SubElement(liaison,'g')

	
	# DESSUS ***************************************
	# Prisme
	prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(epaisseur_male/2.			,	-r2Dc_longueur_contact/2.),
				(epaisseur_male/2.			,	r2Dc_longueur_contact/2.),
				(r2Dc_hauteur_prisme + epaisseur_male/2.,	r2Dc_longueur_base_prisme/2.),
				(r2Dc_hauteur_prisme + epaisseur_male/2.,	-r2Dc_longueur_base_prisme/2.)	],
				True)
	prisme.set('d',chemin)
	prisme.set('stroke',couleur_male)
	prisme.set('style','fill:white')
	prisme.set('stroke-width',str(epaisseur_male))
	dessus.append(prisme)
	
	#tige dessus
	tigeDessus=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(r2Dc_hauteur_prisme+epaisseur_male/2.					,	0.),
				(r2Dc_hauteur_prisme + r2Dc_longueur_tige_prisme + epaisseur_male/2.	,	0.)	])
	tigeDessus.set('d',chemin)
	tigeDessus.set('stroke',couleur_male)
	tigeDessus.set('stroke-width',str(epaisseur_male))
	dessus.append(tigeDessus)
	
	# DESSOUS ***************************************
	#plan dessous
	plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-epaisseur_femelle/2.	,	-r2Dc_longueur_plan/2.),
				(-epaisseur_femelle/2.	,	r2Dc_longueur_plan/2.)	])
	plan.set('d',chemin)
	plan.set('stroke',couleur_femelle)
	plan.set('stroke-width',str(epaisseur_femelle))
	dessous.append(plan)
	
	#tige dessous
	tigePlan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-epaisseur_femelle/2.,					0.),
				(-r2Dc_longueur_tige_plan--epaisseur_femelle/2.,	0.)	])
	tigePlan.set('d',chemin)
	tigePlan.set('stroke',couleur_femelle)
	tigePlan.set('stroke-width',str(epaisseur_femelle))
	dessous.append(tigePlan)
	
	# Transformations ***************************************
	dessus.set("transform","rotate("+str(rotation)+")")
	dessous.set("transform","rotate("+str(rotation)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	

def dessin_rectiligne_2D_bout(options,contexte):
	#Position *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_rectiligne_2D_bout_x
	y=options.liaison_rectiligne_2D_bout_y
	#Orientation **************************************
	rotationNormale=-options.liaison_rectiligne_2D_bout_orientation_normale #Angle par defaut (sens trigo)
	if(options.liaison_rectiligne_bout_axe_normale=="x"):
		rotationNormale = 0
	elif(options.liaison_rectiligne_bout_axe_normale=="y"):
		rotationNormale = -90
	elif(options.liaison_rectiligne_bout_axe_normale=="-x"):
		rotationNormale = 180
	elif(options.liaison_rectiligne_bout_axe_normale=="-y"):
		rotationNormale = 90
	rotationPrisme=-options.liaison_rectiligne_2D_bout_orientation_prisme #Angle par defaut (sens trigo)
	if(options.liaison_rectiligne_bout_axe_prisme=="normale"):
		rotationPrisme = rotationNormale
	elif(options.liaison_rectiligne_bout_axe_prisme=="x"):
		rotationPrisme = 0
	elif(options.liaison_rectiligne_bout_axe_prisme=="y"):
		rotationPrisme = -90
	elif(options.liaison_rectiligne_bout_axe_prisme=="-x"):
		rotationPrisme = 180
	elif(options.liaison_rectiligne_bout_axe_prisme=="-y"):
		rotationPrisme = 90
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	couleur_plan=options.opt_gene_piece2_couleur
	couleur_prisme=options.opt_gene_piece1_couleur
	epaisseur_plan=options.opt_gene_lignes_epaisseur_2
	epaisseur_prisme=options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	prisme=inkex.etree.SubElement(liaison,'g')
	plan=inkex.etree.SubElement(liaison,'g')

	
	# Plan ***************************************	
	# plan
	trait_plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-epaisseur_plan/2.	,	-r2Db_largeur_plan/2.),
				(-epaisseur_plan/2.	,	r2Db_largeur_plan/2.)	])
	trait_plan.set('d',chemin)
	trait_plan.set('stroke',couleur_plan)
	trait_plan.set('stroke-width',str(epaisseur_plan))
	plan.append(trait_plan)
	# tige
	tige_plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-r2Db_longueur_tige_plan	,	0),
				(-epaisseur_plan/2.		,	0)	])
	tige_plan.set('d',chemin)
	tige_plan.set('stroke',couleur_plan)
	tige_plan.set('stroke-width',str(epaisseur_plan))
	plan.append(tige_plan)
	
	# prisme ***************************************
	# triangle
	deport_point_fleche = epaisseur_prisme/2. / math.sin( math.atan((r2Db_largeur_prisme/2.)/(r2Db_hauteur_prisme)) )
	triangle=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(deport_point_fleche			,	0),
				(r2Db_hauteur_prisme+deport_point_fleche	,	r2Db_largeur_prisme/2.),
				(r2Db_hauteur_prisme+deport_point_fleche	,	-r2Db_largeur_prisme/2.)	],
				True)
	triangle.set('d',chemin)
	triangle.set('stroke',couleur_prisme)
	triangle.set('stroke-width',str(epaisseur_prisme))
	triangle.set('style','fill:white')
	prisme.append(triangle)

	trait_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(r2Db_hauteur_prisme+deport_point_fleche				,	0),
				(r2Db_hauteur_prisme+r2Db_longueur_tige_prisme+deport_point_fleche	,	0)	])
	trait_prisme.set('d',chemin)
	trait_prisme.set('stroke',couleur_prisme)
	trait_prisme.set('stroke-width',str(epaisseur_prisme))
	prisme.append(trait_prisme)
	
	# Transformations ***************************************
	plan.set("transform","rotate("+str(rotationNormale)+")")
	prisme.set("transform","rotate("+str(rotationPrisme)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






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
	rayonTige=25.
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
					(rayonTige,	0.,	0.	)
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
					(-rayonTige,	0.,	0.	)
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
	# Credits **************************************
	liaison.set("credits",options.credits)
	
