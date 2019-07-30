# -- coding: utf-8 --

import math
import inkex
from liaisons_parametres import *
from liaisons_fonctions_utiles import *


def dessin_sphere_plan_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_sphere_plan_2D_cote_x
	y=options.liaison_sphere_plan_2D_cote_y
	#Orientation **************************************
	rotation_normale=options.liaison_sphere_plan_2D_cote_orientation_normale #Angle par defaut (sens trigo)
	if(options.liaison_sphere_plan_2D_cote_axe_normale=="y"):
		rotation_normale=90
	elif(options.liaison_sphere_plan_2D_cote_axe_normale=="x"):
		rotation_normale=0
	elif(options.liaison_sphere_plan_2D_cote_axe_normale=="-x"):
		rotation_normale=180
	elif(options.liaison_sphere_plan_2D_cote_axe_normale=="-y"):
		rotation_normale=-90
	rotation_sphere=options.liaison_sphere_plan_2D_cote_orientation_sphere #Angle par defaut (sens trigo)
	if(options.liaison_sphere_plan_2D_cote_axe_sphere=="y"):
		rotation_sphere=90
	elif(options.liaison_sphere_plan_2D_cote_axe_sphere=="x"):
		rotation_sphere=0
	elif(options.liaison_sphere_plan_2D_cote_axe_sphere=="-x"):
		rotation_sphere=180
	elif(options.liaison_sphere_plan_2D_cote_axe_sphere=="-y"):
		rotation_sphere=-90
	elif(options.liaison_sphere_plan_2D_cote_axe_sphere=="normale"):
		rotation_sphere=rotation_normale
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle,rotation_normale*math.pi/180)
	Vx2,Vy2=getBase2D(echelle,rotation_sphere*math.pi/180)
	base2D_1=(Vx1,Vy1)
	base2D_2=(Vx2,Vy2)
	#Parametres ****************************
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	old_liaisons=options.opt_gene_gene_old
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	sphere=inkex.etree.SubElement(liaison,'g')
	plan=inkex.etree.SubElement(liaison,'g')

	
	# PLAN ***************************************
	#plan dessus
	plan_plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0,	-sp2Dc_largeur_plan/2.),
					(0,	sp2Dc_largeur_plan/2)	],
				False,
				base2D_1)
	plan_plan.set('d',chemin)
	plan_plan.set('stroke',couleur_male)
	plan_plan.set('stroke-width',str(epaisseur_male))
	plan.append(plan_plan)
	
	#tige
	tige_plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0			,	0),
					(-sp2Dc_diametre_sphere	,	0)	],
				False,
				base2D_1)
	tige_plan.set('d',chemin)
	tige_plan.set('stroke',couleur_male)
	tige_plan.set('stroke-width',str(epaisseur_male))
	plan.append(tige_plan)
	
	# SPHERE ***************************************
	#plan dessous
	if not old_liaisons:
		sphere_bout=inkex.etree.Element(inkex.addNS('circle','svg'))
		sphere_bout.set('cx',str(sp2Dc_diametre_sphere/2.*math.cos(-rotation_normale*math.pi/180)))
		sphere_bout.set('cy',str(sp2Dc_diametre_sphere/2.*math.sin(-rotation_normale*math.pi/180)))
		sphere_bout.set('r',str(sp2Dc_diametre_sphere/2.*echelle))
		sphere_bout.set('style','fill:white')
	else :
		sphere_bout=inkex.etree.Element(inkex.addNS('path','svg'))
		chemin=points_to_svgd([	(0	,	0),
					(sp2DcOLD_largeur_fleche*(math.sqrt(3)/2*Vx2.x+0.5*Vy2.x)	,	sp2DcOLD_largeur_fleche*(math.sqrt(3)/2*Vx2.y+0.5*Vy2.y)),
					(sp2DcOLD_largeur_fleche*(math.sqrt(3)/2*Vx2.x-0.5*Vy2.x)	,	sp2DcOLD_largeur_fleche*(math.sqrt(3)/2*Vx2.y-0.5*Vy2.y)), 	])
		sphere_bout.set('d',chemin)
		sphere_bout.set('style','fill:'+couleur_femelle)
	sphere_bout.set('stroke',couleur_femelle)
	sphere_bout.set('stroke-width',str(epaisseur_femelle))
	sphere.append(sphere_bout)
	
	#tige
	sphere_tige=inkex.etree.Element(inkex.addNS('path','svg'))
	if not old_liaisons:
		chemin=points_to_svgd([	(sp2Dc_diametre_sphere/2.*(Vx1.x+Vx2.x)	,	sp2Dc_diametre_sphere/2.*(Vx1.y+Vx2.y)),
					(sp2Dc_diametre_sphere/2.*(Vx1.x+Vx2.x)+sp2Dc_longueur_tige_sphere*Vx2.x	,	sp2Dc_diametre_sphere/2.*(Vx1.y+Vx2.y)+sp2Dc_longueur_tige_sphere*Vy2.x)	])
	else:
		chemin=points_to_svgd([	(sp2DcOLD_largeur_fleche*math.sqrt(3)/2.*Vx2.x	,	sp2DcOLD_largeur_fleche*math.sqrt(3)/2.*Vx2.y),
					((sp2DcOLD_largeur_fleche+sp2Dc_longueur_tige_sphere)*Vx2.x	,	(sp2DcOLD_largeur_fleche+sp2Dc_longueur_tige_sphere)*Vx2.y)	])
	sphere_tige.set('d',chemin)
	sphere_tige.set('stroke',couleur_femelle)
	sphere_tige.set('stroke-width',str(epaisseur_femelle))
	sphere.append(sphere_tige)
	
	# Transformations ***************************************
	#dessus.set("transform","rotate("+str(rotation)+")")
	#dessous.set("transform","rotate("+str(rotation)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
	# Credits **************************************
	liaison.set("credits",options.credits)





def dessin_sphere_plan_2D_dessus(options,contexte):
	#Position *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_sphere_plan_2D_dessus_x
	y=options.liaison_sphere_plan_2D_dessus_y
	#Orientation **************************************
	rotationPlan=-options.liaison_sphere_plan_2D_dessus_orientation_plan #Angle par defaut (sens trigo)
	if(options.liaison_sphere_plan_2D_dessus_axe_plan=="x"):
		rotationPlan=0
	elif(options.liaison_sphere_plan_2D_dessus_axe_plan=="y"):
		rotationPlan=-90
	elif(options.liaison_sphere_plan_2D_dessus_axe_plan=="-x"):
		rotationPlan=180
	elif(options.liaison_sphere_plan_2D_dessus_axe_plan=="-y"):
		rotationPlan=90
	rotationSphere=-options.liaison_sphere_plan_2D_dessus_orientation_sphere #Angle par defaut (sens trigo)
	if(options.liaison_sphere_plan_2D_dessus_axe_sphere=="x"):
		rotationSphere=0
	elif(options.liaison_sphere_plan_2D_dessus_axe_sphere=="y"):
		rotationSphere=-90
	elif(options.liaison_sphere_plan_2D_dessus_axe_sphere=="-x"):
		rotationSphere=180
	elif(options.liaison_sphere_plan_2D_dessus_axe_sphere=="-y"):
		rotationSphere=90
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
	groupe_plan=inkex.etree.SubElement(liaison,'g')
	groupe_sphere=inkex.etree.SubElement(liaison,'g')

	
	# Plan ***************************************	
	# rectangle 
	plan=inkex.etree.Element(inkex.addNS('rect','svg'))
	plan.set('x',str(-sp2Dd_largeur*echelle/2) )
	plan.set('y',str(-sp2Dd_largeur*echelle/2) )
	plan.set('width',str(sp2Dd_largeur*echelle))
	plan.set('height',str(sp2Dd_largeur*echelle))
	plan.set('style','fill:white')
	plan.set('stroke',couleur_femelle)
	plan.set('stroke-width',str(epaisseur_femelle))
	groupe_plan.append(plan)
	#trait
	traitPlan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(sp2Dd_largeur/2.*echelle	,	0),
				((sp2Dd_largeur/2.+sp2Dd_longueur_tige_plan)*echelle	,	0)	])
	traitPlan.set('d',chemin)
	traitPlan.set('stroke',couleur_femelle)
	traitPlan.set('stroke-width',str(epaisseur_femelle))
	groupe_plan.append(traitPlan)
	
	# sphere ***************************************
	# sphere
	sphere=inkex.etree.Element(inkex.addNS('circle','svg'))
	sphere.set('cx','0')
	sphere.set('cy','0')
	sphere.set('r',str(sp2Dc_diametre_sphere/2.*echelle))
	sphere.set('style','fill:white')
	sphere.set('stroke',couleur_male)
	sphere.set('stroke-width',str(epaisseur_male))
	groupe_sphere.append(sphere)

	
	#trait
	traitSphere=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(sp2Dc_diametre_sphere/2.*echelle	,0),
				((sp2Dc_diametre_sphere/2.+sp2Dd_longueur_tige_sphere)*echelle	,0)	])
	traitSphere.set('d',chemin)
	traitSphere.set('stroke',couleur_male)
	traitSphere.set('stroke-width',str(epaisseur_male))
	groupe_sphere.append(traitSphere)
	
	# Transformations ***************************************
	groupe_plan.set("transform","rotate("+str(rotationPlan)+")")
	groupe_sphere.set("transform","rotate("+str(rotationSphere)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






#===============================================================
def dessin_sphere_plan_3D(options,contexte):
	#Origine 2D
	x0=options.x0
	y0=options.y0
	#Base Axonometrique
	echelle=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques(echelle)
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x=options.liaison_sphere_plan_3D_position_x
	y=options.liaison_sphere_plan_3D_position_y
	z=options.liaison_sphere_plan_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	couleur_plan=options.opt_gene_piece1_couleur
	couleur_sphere=options.opt_gene_piece2_couleur
	epaisseur_plan=options.opt_gene_lignes_epaisseur_1
	epaisseur_sphere=options.opt_gene_lignes_epaisseur_2
	angle_plan=-float(options.liaison_sphere_plan_3D_rotation_plan)/180.*math.pi
	#Repere local de la liaison
	#Plan
	if(options.liaison_sphere_plan_3D_type_normale=="\"liaison_sphere_plan_3D_type_normale_quelconque\""):
		V=v3D(options.liaison_sphere_plan_3D_normale_quelconque_x,options.liaison_sphere_plan_3D_normale_quelconque_y,options.liaison_sphere_plan_3D_normale_quelconque_z,base)
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle,angle_plan)#Repere plan
	else:	#Si vecteur standard
		if options.liaison_plane_3D_axe == "x" :
			Vx1,Vy1,Vz1 = getBaseFromVecteur(Vx, echelle, angle_plan)
		elif options.liaison_plane_3D_axe == "-x" :
			Vx1,Vy1,Vz1 = getBaseFromVecteur(-Vx, echelle, angle_plan)
		elif options.liaison_plane_3D_axe == "y" :
			Vx1,Vy1,Vz1 = getBaseFromVecteur(Vy, echelle, angle_plan)
		elif options.liaison_plane_3D_axe == "-y" :
			Vx1,Vy1,Vz1 = getBaseFromVecteur(-Vy, echelle, angle_plan)
		elif options.liaison_plane_3D_axe == "z" :
			Vx1,Vy1,Vz1 = getBaseFromVecteur(Vz, echelle, angle_plan)
		else:#z
			Vx1,Vy1,Vz1 = getBaseFromVecteur(-Vz, echelle, angle_plan)
	baseLocale1=(Vx1,Vy1,Vz1)
	#Sphère
	if(options.liaison_sphere_plan_3D_type_direction_sphere=="\"liaison_sphere_plan_3D_type_direction_sphere_quelconque\""):
		V=v3D(options.liaison_sphere_plan_3D_direction_sphere_quelconque_x,options.liaison_sphere_plan_3D_direction_sphere_quelconque_y,options.liaison_sphere_plan_3D_direction_sphere_quelconque_z,base)
		Vx2,Vy2,Vz2=getBaseFromVecteur(V,echelle,angle_plan)#Repere plan
	else:	#Si vecteur standard
		if options.liaison_sphere_plan_3D_axe_sphere == "normale" :
			Vx2,Vy2,Vz2 = Vx1,Vy1,Vz1
		elif options.liaison_sphere_plan_3D_axe_sphere == "x" :
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vx, echelle)
		elif options.liaison_sphere_plan_3D_axe_sphere == "-x" :
			Vx2,Vy2,Vz2 = getBaseFromVecteur(-Vx, echelle)
		elif options.liaison_sphere_plan_3D_axe_sphere == "y" :
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vy, echelle)
		elif options.liaison_sphere_plan_3D_axe_sphere == "-y":
			Vx2,Vy2,Vz2 = getBaseFromVecteur(-Vy, echelle)
		elif options.liaison_sphere_plan_3D_axe_sphere == "z" :
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vz, echelle)
		else :
			Vx2,Vy2,Vz2 = getBaseFromVecteur(-Vz, echelle)
	baseLocale2=(Vx2,Vy2,Vz2)

	# Plan ***************************************
	plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	-sp3D_largeur/2.,	-sp3D_largeur/2.	),
					(0,	-sp3D_largeur/2.,	sp3D_largeur/2.	),
					(0,	sp3D_largeur/2.,	sp3D_largeur/2.	),
					(0,	sp3D_largeur/2.,	-sp3D_largeur/2.	)
				],True,baseLocale1)
	plan.set('d',chemin)
	plan.set('stroke',couleur_plan)
	plan.set('stroke-width',str(epaisseur_plan))
	plan.set('style','fill:white')
	plan.set('profondeur',str(profondeur))
	

	tigePlan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
						(0,				0.,	0.	),
						(-sp3D_longueur_tige_plan,	0.,	0.	)
				],False,baseLocale1)
	tigePlan.set('d',chemin)
	tigePlan.set('stroke',couleur_plan)
	tigePlan.set('stroke-width',str(epaisseur_plan))
	tigePlan.set('style','stroke-linecap:round')
	tigePlan.set('profondeur',str(profondeur))
	
	# Sphère ***************************************
	Vcentre = Vx1 * sp3D_diametre_sphere / 2.
	
	sphere=inkex.etree.Element(inkex.addNS('circle','svg'))
	sphere.set('cx', str(Vx1.x*sp3D_diametre_sphere/2.))
	sphere.set('cy', str(Vx1.y*sp3D_diametre_sphere/2.))
	sphere.set('r',str(sp3D_diametre_sphere/2.*echelle))
	sphere.set('style','fill:white')
	sphere.set('stroke',couleur_sphere)
	sphere.set('stroke-width',str(epaisseur_sphere))
	sphere.set('profondeur',str(Vx1.z))


	tigeSphere=inkex.etree.Element(inkex.addNS('path','svg'))
	P1=(Vx1+Vx2) * sp3D_diametre_sphere/2.
	P2=(Vx1+Vx2) * sp3D_diametre_sphere/2. + Vx2*sp3D_longueur_tige_sphere
	chemin,profondeur=points3D_to_svgd([
					(P1.x,	P1.y,	P1.z	),
					(P2.x,	P2.y,	P2.z	)
				],False)
	tigeSphere.set('d',chemin)
	tigeSphere.set('stroke',couleur_sphere)
	tigeSphere.set('stroke-width',str(epaisseur_sphere))
	tigeSphere.set('style','stroke-linecap:round')
	tigeSphere.set('profondeur',str(profondeur))
	


	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        listeObjets=[sphere,tigeSphere,plan,tigePlan]
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)
        
        
	# Transformations ***************************************
	liaison.set("transform","translate("+str(x0+x*Vx.x+y*Vy.x+z*Vz.x)+","+str(y0+x*Vx.y+y*Vy.y+z*Vz.y)+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	
