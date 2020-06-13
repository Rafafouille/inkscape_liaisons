import math
import inkex
from liaisons_fonctions_utiles import *
from liaisons_parametres import *


def dessin_rectiligne_plan_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_rectiligne_2D_cote_x
	y = -options.liaison_rectiligne_2D_cote_y
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
	epaisseur_plan=options.opt_gene_lignes_epaisseur_2
	epaisseur_prisme=options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	dessus=inkex.etree.SubElement(liaison,'g')
	dessous=inkex.etree.SubElement(liaison,'g')

	
	# DESSUS ***************************************
	# Prisme
	prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(epaisseur_prisme/2.			,	-r2Dc_longueur_contact/2.),
				(epaisseur_prisme/2.			,	r2Dc_longueur_contact/2.),
				(r2Dc_hauteur_prisme + epaisseur_prisme/2.,	r2Dc_longueur_base_prisme/2.),
				(r2Dc_hauteur_prisme + epaisseur_prisme/2.,	-r2Dc_longueur_base_prisme/2.)	],
				True)
	prisme.set('d',chemin)
	prisme.set('stroke',couleur_male)
	prisme.set('style','fill:white')
	prisme.set('stroke-width',str(epaisseur_prisme))
	dessus.append(prisme)
	
	#tige dessus
	tigeDessus=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(r2Dc_hauteur_prisme+epaisseur_prisme/2.					,	0.),
				(r2Dc_hauteur_prisme + r2Dc_longueur_tige_prisme + epaisseur_prisme/2.	,	0.)	])
	tigeDessus.set('d',chemin)
	tigeDessus.set('stroke',couleur_male)
	tigeDessus.set('stroke-width',str(epaisseur_prisme))
	dessus.append(tigeDessus)
	
	# DESSOUS ***************************************
	#plan dessous
	plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-epaisseur_plan/2.	,	-r2Dc_longueur_plan/2.),
				(-epaisseur_plan/2.	,	r2Dc_longueur_plan/2.)	])
	plan.set('d',chemin)
	plan.set('stroke',couleur_femelle)
	plan.set('stroke-width',str(epaisseur_plan))
	dessous.append(plan)
	
	#tige dessous
	tigePlan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-epaisseur_plan/2.,					0.),
				(-r2Dc_longueur_tige_plan-epaisseur_plan/2.,	0.)	])
	tigePlan.set('d',chemin)
	tigePlan.set('stroke',couleur_femelle)
	tigePlan.set('stroke-width',str(epaisseur_plan))
	dessous.append(tigePlan)
	
	# Transformations ***************************************
	dessus.set("transform","rotate("+str(rotation)+")")
	dessous.set("transform","rotate("+str(rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	

def dessin_rectiligne_2D_bout(options,contexte):
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_rectiligne_2D_bout_x
	y = -options.liaison_rectiligne_2D_bout_y
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
	echelle = options.echelle
	Vx1,Vy1 = getBase2D(echelle)
	base2D = (Vx1,Vy1)
	#Parametres ****************************
	couleur_plan = options.opt_gene_piece2_couleur
	couleur_prisme = options.opt_gene_piece1_couleur
	epaisseur_plan = options.opt_gene_lignes_epaisseur_2
	epaisseur_prisme = options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	prisme = inkex.etree.SubElement(liaison,'g')
	plan = inkex.etree.SubElement(liaison,'g')

	
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
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






#===============================================================
def dessin_rectiligne_3D(options,contexte):
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
	inclinaison = options.liaison_rectiligne_3D_inclinaison_prisme/180.*math.pi
	couleur_plan = options.opt_gene_piece1_couleur
	couleur_dessous = options.opt_gene_piece2_couleur
	epaisseur_plan = options.opt_gene_lignes_epaisseur_1
	epaisseur_dessous = options.opt_gene_lignes_epaisseur_2
	#angle_inclinaison_prisme = -float(options.liaison_rectiligne_3D_inclinaison_prisme)/180.*math.pi
	#Repere local de la liaison
	if(options.liaison_rectiligne_3D_type_normale!="\"liaison_rectiligne_3D_type_normale_standard\""):
		Vn = v3D(options.liaison_rectiligne_3D_normale_quelconque_x, options.liaison_rectiligne_3D_normale_quelconque_y, options.liaison_rectiligne_3D_normale_quelconque_z,base)
	else:	#Si vecteur standard
		if(options.liaison_rectiligne_3D_axe_normale=="x"):
			Vn = v3D(1, 0, 0, base)
		elif(options.liaison_rectiligne_3D_axe_normale=="y"):
			Vn = v3D(0, 1, 0, base)
		elif(options.liaison_rectiligne_3D_axe_normale=="z"):
			Vn = v3D(0, 0, 1, base)
		elif(options.liaison_rectiligne_3D_axe_normale=="-x"):
			Vn = v3D(-1, 0, 0, base)
		elif(options.liaison_rectiligne_3D_axe_normale=="-y"):
			Vn = v3D(0, -1, 0, base)
		elif(options.liaison_rectiligne_3D_axe_normale=="-z"):
			Vn = v3D(0, 0, -1, base)
	if(options.liaison_rectiligne_3D_type_direction!="\"liaison_rectiligne_3D_type_direction_standard\""):
		Vd = v3D(options.liaison_rectiligne_3D_direction_quelconque_x, options.liaison_rectiligne_3D_direction_quelconque_y, options.liaison_rectiligne_3D_direction_quelconque_z,base)
	else:
		if(options.liaison_rectiligne_3D_axe_direction=="x"):
			Vd = v3D(1, 0, 0, base)
		elif(options.liaison_rectiligne_3D_axe_direction=="y"):
			Vd = v3D(0, 1, 0, base)
		elif(options.liaison_rectiligne_3D_axe_direction=="z"):
			Vd = v3D(0, 0, 1, base)
		elif(options.liaison_rectiligne_3D_axe_direction=="-x"):
			Vd = v3D(-1, 0, 0, base)
		elif(options.liaison_rectiligne_3D_axe_direction=="-y"):
			Vd = v3D(0, -1, 0, base)
		elif(options.liaison_rectiligne_3D_axe_direction=="-z"):
			Vd = v3D(0, 0, -1, base)
	#============================================
	Vn.normalise()
	Vx1 = Vn
	Vy1 = Vd - (Vd * Vn) * Vn
	Vy1.normalise()
	Vz1 = Vx1 ^Vy1
	
	Vx2 = Vx1*math.cos(inclinaison) + Vz1*math.sin(inclinaison)
	Vy2 = Vy1
	Vz2 = Vx2 ^Vy2
	
	baseLocale1=(Vx1,Vy1,Vz1)
	baseLocale2=(Vx2,Vy2,Vz2)

	# plan ***************************************
	plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	-r3D_longueur_plan/2.,	-r3D_largeur_plan/2.	),
					(0,	-r3D_longueur_plan/2.,	r3D_largeur_plan/2.	),
					(0,	r3D_longueur_plan/2.,	r3D_largeur_plan/2.	),
					(0,	r3D_longueur_plan/2.,	-r3D_largeur_plan/2.	)
				],True,baseLocale1)
	plan.set('d',chemin)
	plan.set('stroke',couleur_plan)
	plan.set('stroke-width',str(epaisseur_plan))
	plan.set('profondeur',str(profondeur))
	plan.set('style','fill:white;stroke-linejoin:round')
	

	tige_plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,				0.,	0.	),
					(-r3D_longueur_tige_plan,	0.,	0.	)
				],False,baseLocale1)
	tige_plan.set('d',chemin)
	tige_plan.set('stroke',couleur_plan)
	tige_plan.set('stroke-width',str(epaisseur_plan))
	tige_plan.set('style','stroke-linecap:round')
	tige_plan.set('profondeur',str(profondeur))
	
	# Prisme ***************************************
	base_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(r3D_hauteur_prisme,	-r3D_longueur_base_prisme/2.,	-r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	-r3D_longueur_base_prisme/2.,	r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	r3D_longueur_base_prisme/2.,	r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	r3D_longueur_base_prisme/2.,	-r3D_largeur_base_prisme/2.	)
				],True,baseLocale2)
	base_prisme.set('d',chemin)
	base_prisme.set('stroke',couleur_dessous)
	base_prisme.set('stroke-width',str(epaisseur_dessous))
	base_prisme.set('style','fill:white;stroke-linejoin:round')
	base_prisme.set('profondeur',str(profondeur))
	profondeur_base = profondeur
	
	
	flanc1_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	-r3D_longueur_contact/2.,	0	),
					(0,	r3D_longueur_contact/2.,	0	),
					(r3D_hauteur_prisme,	r3D_longueur_base_prisme/2.,	-r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	-r3D_longueur_base_prisme/2.,	-r3D_largeur_base_prisme/2.	)
				],True,baseLocale2)
	flanc1_prisme.set('d',chemin)
	flanc1_prisme.set('stroke',couleur_dessous)
	flanc1_prisme.set('stroke-width',str(epaisseur_dessous))
	flanc1_prisme.set('style','fill:white;stroke-linejoin:round')
	flanc1_prisme.set('profondeur',str(profondeur_base*0.999+profondeur*0.001))
	
	
	flanc2_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	-r3D_longueur_contact/2.,	0	),
					(0,	r3D_longueur_contact/2.,	0	),
					(r3D_hauteur_prisme,	r3D_longueur_base_prisme/2.,	r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	-r3D_longueur_base_prisme/2.,	r3D_largeur_base_prisme/2.	)
				],True,baseLocale2)
	flanc2_prisme.set('d',chemin)
	flanc2_prisme.set('stroke',couleur_dessous)
	flanc2_prisme.set('stroke-width',str(epaisseur_dessous))
	flanc2_prisme.set('style','fill:white;stroke-linejoin:round')
	flanc2_prisme.set('profondeur',str(profondeur_base*0.999+profondeur*0.001))
	
	
	bout1_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	r3D_longueur_contact/2.,	0	),
					(r3D_hauteur_prisme,	r3D_longueur_base_prisme/2.,	r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	r3D_longueur_base_prisme/2.,	-r3D_largeur_base_prisme/2.	)
				],True,baseLocale2)
	bout1_prisme.set('d',chemin)
	bout1_prisme.set('stroke',couleur_dessous)
	bout1_prisme.set('stroke-width',str(epaisseur_dessous))
	bout1_prisme.set('style','fill:white;stroke-linejoin:round')
	bout1_prisme.set('profondeur',str(profondeur_base*0.999+profondeur*0.001))
	
	
	bout2_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	-r3D_longueur_contact/2.,	0	),
					(r3D_hauteur_prisme,	-r3D_longueur_base_prisme/2.,	r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	-r3D_longueur_base_prisme/2.,	-r3D_largeur_base_prisme/2.	)
				],True,baseLocale2)
	bout2_prisme.set('d',chemin)
	bout2_prisme.set('stroke',couleur_dessous)
	bout2_prisme.set('stroke-width',str(epaisseur_dessous))
	bout2_prisme.set('style','fill:white;stroke-linejoin:round')
	bout2_prisme.set('profondeur',str(profondeur_base*0.999+profondeur*0.001))
	



	tige_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(r3D_hauteur_prisme,	0.,	0.	),
					(r3D_hauteur_prisme+r3D_longueur_tige_prisme,	0.,	0.	)
				],False,baseLocale2)
	tige_prisme.set('d',chemin)
	tige_prisme.set('stroke',couleur_dessous)
	tige_prisme.set('stroke-width',str(epaisseur_dessous))
	tige_prisme.set('style','stroke-linecap:round')
	tige_prisme.set('profondeur',str(profondeur))
	


	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        listeObjets=[plan,tige_plan,base_prisme,tige_prisme,flanc1_prisme,flanc2_prisme,bout1_prisme,bout2_prisme]
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)
        
        
	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	
