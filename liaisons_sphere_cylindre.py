# -- coding: utf-8 --
import math
import inkex
from liaisons_fonctions_utiles import *
from liaisons_parametres import *


def dessin_Sphere_Cylindre_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_sphere_cylindre_2D_cote_x
	y = -options.liaison_sphere_cylindre_2D_cote_y

	#Orientation **************************************
	rotation_cylindre = -options.liaison_sphere_cylindre_2D_cote_orientation_axe #Angle par defaut (sens trigo)
	if options.liaison_sphere_cylindre_2D_cote_axe=="x" :
		rotation_cylindre = 0
	elif options.liaison_sphere_cylindre_2D_cote_axe=="y" :
		rotation_cylindre = -90
	elif options.liaison_sphere_cylindre_2D_cote_axe=="-x" :
		rotation_cylindre = 180
	elif options.liaison_sphere_cylindre_2D_cote_axe=="-y" :
		rotation_cylindre = 90
	rotation_sphere = -options.liaison_sphere_cylindre_2D_cote_orientation_axe_sphere #Angle par defaut (sens trigo)
	if options.liaison_sphere_cylindre_2D_cote_axe_sphere=="x" :
		rotation_sphere = 0
	elif options.liaison_sphere_cylindre_2D_cote_axe_sphere=="y" :
		rotation_sphere = -90
	elif options.liaison_sphere_cylindre_2D_cote_axe_sphere=="-x" :
		rotation_sphere = 180
	elif options.liaison_sphere_cylindre_2D_cote_axe_sphere=="-y" :
		rotation_sphere = 90
	elif options.liaison_sphere_cylindre_2D_cote_axe_sphere=="normal" :
		rotation_sphere = rotation_cylindre - 90
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	echelle=options.echelle
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        #groupe_rotation = inkex.etree.SubElement(liaison, 'g')
	femelle=inkex.etree.SubElement(liaison,'g')
	male=inkex.etree.SubElement(liaison,'g')
	
	
	
	# Male ***************************************
	
	#Sphère
	sphere=inkex.etree.Element(inkex.addNS('circle','svg'))
	sphere.set('cx',"0")
	sphere.set('cy',"0")
	sphere.set('r',str(SC2Dc_diametre/2. * echelle))
	sphere.set('stroke',str(couleur_male))
	sphere.set('stroke-width',str(epaisseur_male))
	sphere.set('style','fill:white')
	male.append(sphere)

	#Ligne male
	ligneM=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(SC2Dc_diametre/2.	,	0),
					(SC2Dc_diametre/2. + SC2Dc_longueur_tige_sphere	,	0)	],
				False,
				base2D)
	ligneM.set('d',chemin)
	ligneM.set('stroke',couleur_male)
	ligneM.set('stroke-width',str(epaisseur_male))
	male.append(ligneM)
	
	# Femelle ***************************************

	#Rectangle
	rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-SC2Dc_longueur*echelle / 2.) )
	rectangle.set('y',str((SC2Dc_diametre/2.-SC2Dc_hauteur) * echelle) )
	rectangle.set('width',str(SC2Dc_longueur*echelle))
	rectangle.set('height',str( SC2Dc_hauteur*echelle + (epaisseur_femelle+epaisseur_male)/2. ))
	rectangle.set('style','fill:none')
	rectangle.set('stroke',couleur_femelle)
	rectangle.set('stroke-width',str(epaisseur_femelle))
	femelle.append(rectangle)
	
	#Ligne femelle
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(0	,	SC2Dc_diametre/2.*echelle + (epaisseur_femelle+epaisseur_male)/2.),
				(0	,	(SC2Dc_diametre/2.+ SC2Dc_longueur_tige_cylindre)*echelle	)	])
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle*echelle))
	femelle.append(ligneF)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation_sphere)+")")
	femelle.set("transform","rotate("+str(rotation_cylindre)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	

def dessin_Sphere_Cylindre_2D_bout(options,contexte):
	global SC2Db_angle_ouverture
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_sphere_cylindre_2D_bout_x
	y = -options.liaison_sphere_cylindre_2D_bout_y

	#Orientation **************************************
	rotation_cylindre = -options.liaison_sphere_cylindre_2D_bout_orientation_axe_base #Angle par defaut (sens trigo)
	if options.liaison_sphere_cylindre_2D_bout_axe_base=="x" :
		rotation_cylindre = 0
	elif options.liaison_sphere_cylindre_2D_bout_axe_base=="y" :
		rotation_cylindre = -90
	elif options.liaison_sphere_cylindre_2D_bout_axe_base=="-x" :
		rotation_cylindre = 180
	elif options.liaison_sphere_cylindre_2D_bout_axe_base=="-y" :
		rotation_cylindre = 90
	rotation_sphere = -options.liaison_sphere_cylindre_2D_bout_orientation_axe_sphere #Angle par defaut (sens trigo)
	if options.liaison_sphere_cylindre_2D_bout_axe_sphere=="x" :
		rotation_sphere = 0
	elif options.liaison_sphere_cylindre_2D_bout_axe_sphere=="y" :
		rotation_sphere = -90
	elif options.liaison_sphere_cylindre_2D_bout_axe_sphere=="-x" :
		rotation_sphere = 180
	elif options.liaison_sphere_cylindre_2D_bout_axe_sphere=="-y" :
		rotation_sphere = 90
	elif options.liaison_sphere_cylindre_2D_bout_axe_sphere=="normal" :
		rotation_sphere = rotation_cylindre
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	echelle=options.echelle
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        #groupe_rotation = inkex.etree.SubElement(liaison, 'g')
	femelle=inkex.etree.SubElement(liaison,'g')
	male=inkex.etree.SubElement(liaison,'g')
	
	
	
	# Male ***************************************
	
	#Sphère
	sphere=inkex.etree.Element(inkex.addNS('circle','svg'))
	sphere.set('cx',"0")
	sphere.set('cy',"0")
	sphere.set('r',str(SC2Db_diametre/2. * echelle))
	sphere.set('stroke',str(couleur_male))
	sphere.set('stroke-width',str(epaisseur_male))
	sphere.set('style','fill:white')
	male.append(sphere)

	#Ligne male
	ligneM=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(SC2Db_diametre/2.	,	0),
					(SC2Db_diametre/2. + SC2Db_longueur_tige_sphere	,	0)	],
				False,
				base2D)
	ligneM.set('d',chemin)
	ligneM.set('stroke',couleur_male)
	ligneM.set('stroke-width',str(epaisseur_male))
	male.append(ligneM)
	
	# Femelle ***************************************

	#Calotte
	calotte=inkex.etree.Element(inkex.addNS('path','svg'))
	listeChemin = []
	SC2Db_angle_ouverture = SC2Db_angle_ouverture*math.pi/180
	theta = SC2Db_angle_ouverture/2.
	while theta < 2*math.pi - SC2Db_angle_ouverture/2.:
		listeChemin.append(( 	echelle*math.cos(theta)*(SC2Db_diametre/2.+SC2Db_intervalle_spheres),
					echelle*math.sin(theta)*(SC2Db_diametre/2.+SC2Db_intervalle_spheres) ))
		theta += 0.05
	listeChemin.append(( echelle*math.cos(-SC2Db_angle_ouverture/2.)*(SC2Db_diametre/2.+SC2Db_intervalle_spheres), echelle*math.sin(-SC2Db_angle_ouverture/2.)*(SC2Db_diametre/2.+SC2Db_intervalle_spheres) ))
	chemin=points_to_svgd(listeChemin,False)
	calotte.set('d',chemin)
	calotte.set('stroke',couleur_femelle)
	calotte.set('stroke-width',str(epaisseur_femelle*echelle))
	calotte.set('style','fill:none')
	femelle.append(calotte)
	
	#Trait
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	((-SC2Db_diametre/2.-SC2Db_intervalle_spheres)*echelle	,	echelle*SC2Db_largeur_plan/2.),
				((-SC2Db_diametre/2.-SC2Db_intervalle_spheres)*echelle	,	-echelle*SC2Db_largeur_plan/2.	)	])
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle*echelle))
	femelle.append(ligneF)
	
	

	#Tige femelle
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-(SC2Dc_diametre/2.+SC2Db_intervalle_spheres)*echelle	,	0),
				(	-(SC2Dc_diametre/2.+SC2Db_intervalle_spheres+SC2Db_longueur_tige_cylindre)*echelle	,	0)	])
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle*echelle))
	femelle.append(ligneF)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation_sphere)+")")
	femelle.set("transform","rotate("+str(rotation_cylindre)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






#===============================================================
def dessin_Sphere_Cylindre_3D(options,contexte):
	#Origine 2D
	x0 = options.x0
	y0 = options.y0
	#Base Axonometrique
	echelle=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques(echelle)
	base=(Vx,Vy,Vz)
	#Position
	x=options.liaison_sphere_cylindre_3D_position_x
	y=options.liaison_sphere_cylindre_3D_position_y
	z=options.liaison_sphere_cylindre_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres ****************************
	couleur_femelle = options.opt_gene_piece2_couleur
	couleur_male = options.opt_gene_piece1_couleur
	epaisseur_femelle = options.opt_gene_lignes_epaisseur_2
	epaisseur_male = options.opt_gene_lignes_epaisseur_1
	rayon = SC3D_diametre / 2.
	longueur = SC3D_longueur
#	angle_male-=float(options.liaison_pivot_glissant_3D_orientation_male)/180.*math.pi
	angle_cylindre=-float(options.liaison_sphere_cylindre_3D_rotation_cylindre)/180.*math.pi
	#Repere local de la liaison
	if(options.liaison_sphere_cylindre_3D_type_axe=="\"liaison_sphere_cylindre_3D_type_axe_quelconque\""):
		V=v3D(options.liaison_sphere_cylindre_3D_axe_quelconque_x,options.liaison_sphere_cylindre_3D_axe_quelconque_y,options.liaison_sphere_cylindre_3D_axe_quelconque_z,base)
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle,angle_cylindre)#Repere Femelle
	else:	#Si vecteur standard
		if(options.liaison_sphere_cylindre_3D_axe=="x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle,angle_cylindre)#Repere Femelle
		elif(options.liaison_sphere_cylindre_3D_axe=="y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle,angle_cylindre)#Repere Femelle
		else:#z
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle,angle_cylindre)#Repere Femelle
	if(options.liaison_sphere_cylindre_3D_type_direction_sphere=="\"liaison_sphere_plan_3D_type_direction_sphere_quelconque\""):
		VS=v3D(options.liaison_sphere_cylindre_3D_direction_sphere_quelconque_x,options.liaison_sphere_cylindre_3D_direction_sphere_quelconque_y,options.liaison_sphere_cylindre_3D_direction_sphere_quelconque_z,base)
		Vx2,Vy2,Vz2=getBaseFromVecteur(VS,echelle,angle_cylindre)#Repere Femelle
	else:	#Si vecteur standard
		if(options.liaison_sphere_cylindre_3D_axe_sphere=="x"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vx,echelle,angle_cylindre)#Repere Femelle
		elif(options.liaison_sphere_cylindre_3D_axe_sphere=="y"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vy,echelle,angle_cylindre)#Repere Femelle
		elif(options.liaison_sphere_cylindre_3D_axe_sphere=="z"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vz,echelle,angle_cylindre)#Repere Femelle
		elif(options.liaison_sphere_cylindre_3D_axe_sphere=="-x"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(-Vx,echelle,angle_cylindre)#Repere Femelle
		elif(options.liaison_sphere_cylindre_3D_axe_sphere=="-y"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(-Vy,echelle,angle_cylindre)#Repere Femelle
		elif(options.liaison_sphere_cylindre_3D_axe_sphere=="-z"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(-Vz,echelle,angle_cylindre)#Repere Femelle
		else:#Dans le prolongement de la piece femelle
			Vx2,Vy2,Vz2 = Vz1,Vx1,Vy1
			
	baseLocale_Cylindre = (Vx1,Vy1,Vz1)
	baseLocale_sphere = (Vx2,Vy2,Vz2)

	
	# Male ***************************************
	
	#Tige
	tigeMale=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(rayon,	0,	0	),
					(rayon + SC3D_longueur_tige_sphere,	0,	0	)
				],False,baseLocale_sphere)
	tigeMale.set('d',chemin)
	tigeMale.set('stroke',couleur_male)
	tigeMale.set('stroke-width',str(epaisseur_male))
	tigeMale.set('style','stroke-linecap:round')
	tigeMale.set('profondeur',str(profondeur))

	#Boule
	boule=inkex.etree.Element(inkex.addNS('circle','svg'))
	boule.set('cx',"0")
	boule.set('cy',"0")
	boule.set('r',str(rayon*echelle))
	boule.set('stroke',str(couleur_male))
	boule.set('stroke-width',str(epaisseur_male))
	boule.set('style','fill:white')
	boule.set('profondeur',"0")


	
	# Femelle ***************************************
	#On recupere les deux angles qui correspondent aux tangentes par rapport a la vue
	thetaCoupure1,thetaCoupure2=getAnglesCoupure(baseLocale_Cylindre)
	
	#On construit les arcs de cercles projete
	centre1 = v3D(-longueur/2, 0, 0, baseLocale_Cylindre) #Vecteur OC1, O=centre liaison
	centre2 = v3D(longueur/2, 0, 0, baseLocale_Cylindre) #Vecteur OC1, O=centre liaison
	ouverture = SC3D_angle_ouverture * math.pi/180
	listeArcs1 = getListePoints2DCercle(baseLocale_Cylindre, centre1, rayon, math.pi/2+ouverture/2, math.pi*5/2.-ouverture/2, thetaCoupure1, thetaCoupure2)
	listeArcs2 = getListePoints2DCercle(baseLocale_Cylindre, centre2, rayon, math.pi/2+ouverture/2, math.pi*5/2.-ouverture/2, thetaCoupure1, thetaCoupure2)
	
	#assert 0,str(listeArcs1)+"\n\n"+str(listeArcs2)
	
	listeArcs2[0].reverse()#On inverse les arcs de cercle
	listeArcs2[1].reverse()
	
	#On construit les cylindres
	listeDemiCylindre1=listeArcs1[0]+listeArcs2[0]
	listeDemiCylindre2=listeArcs1[1]+listeArcs2[1]
	
	
	chemin,profondeurDemiCylindre1 = points3D_to_svgd(listeDemiCylindre1,True)
	#formesFemelles1.append((chemin,profondeur))
	demiCylindre1=inkex.etree.Element(inkex.addNS('path','svg'))
	demiCylindre1.set('d',chemin)
	demiCylindre1.set('stroke',couleur_femelle)
	demiCylindre1.set('stroke-width',str(epaisseur_femelle))
	demiCylindre1.set('style','stroke-linecap:round')
	demiCylindre1.set('style','fill:white')
	demiCylindre1.set('profondeur',str(profondeurDemiCylindre1))
	
	chemin,profondeurDemiCylindre2=points3D_to_svgd(listeDemiCylindre2,True)
	#formesFemelles2.append((chemin,profondeur))
	demiCylindre2=inkex.etree.Element(inkex.addNS('path','svg'))
	demiCylindre2.set('d',chemin)
	demiCylindre2.set('stroke',couleur_femelle)
	demiCylindre2.set('stroke-width',str(epaisseur_femelle))
	demiCylindre2.set('style','stroke-linecap:round')
	demiCylindre2.set('style','fill:white')
	demiCylindre2.set('profondeur',str(profondeurDemiCylindre2))
	
	#barre femelle
	barreFemelle=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	0,	-rayon	),
					(0,	0,	-rayon - SC3D_longueur_tige_cylindre)
				],False,baseLocale_Cylindre)
	barreFemelle.set('d',chemin)
	barreFemelle.set('stroke',couleur_femelle)
	barreFemelle.set('stroke-width',str(epaisseur_femelle))
	barreFemelle.set('style','stroke-linecap:round')
	barreFemelle.set('profondeur',str(profondeur*1e10))
	


	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        
        listeObjets=[demiCylindre1,demiCylindre2,barreFemelle,boule,tigeMale]
        
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)
        
        
	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	
