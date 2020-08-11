import math
import inkex
from lxml import etree	# Nécessaire pour les groupes depuis la version 1.0
from liaisons_fonctions_utiles import *
from liaisons_parametres import *


def dessin_Pivot_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_pivot_2D_cote_x
	y = -options.liaison_pivot_2D_cote_y
	#Orientation **************************************
	rotation=options.liaison_pivot2D_cote_orientation #Angle par defaut (sens trigo)
	if(options.liaison_pivot2D_cote_axe=="x"):
		rotation=0
	elif(options.liaison_pivot2D_cote_axe=="y"):
		rotation=90.
	elif(options.liaison_pivot2D_cote_axe=="-x"):
		rotation=180.
	elif(options.liaison_pivot2D_cote_axe=="-y"):
		rotation=-90.
	#Base *********************
	echelle_liaison=options.echelle
	Vx1,Vy1=getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	old_liaisons=options.opt_gene_gene_old
	largeur = p2Dc_longueur
	hauteur = diametre_pivot
	espace_arrets = p2Dc_ecarts_arrets
	longueur_axe = p2Dc_longueur_male
	longueur_tige = p2Dc_longueur_tige_femelle
	couleur_femelle = options.opt_gene_piece2_couleur
	couleur_male = options.opt_gene_piece1_couleur
	epaisseur_femelle=  options.opt_gene_lignes_epaisseur_2
	epaisseur_male=  options.opt_gene_lignes_epaisseur_1

	
	#Groupes ******************************************
	liaison = etree.SubElement(contexte, 'g')
	fond_femelle = etree.SubElement(liaison,'g')
	male = etree.SubElement(liaison,'g')
	femelle = etree.SubElement(liaison,'g')
	
	
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
	
	#Arret male 1
	arretM1=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-largeur/2.-espace_arrets	,	-hauteur/2),
					(-largeur/2.-espace_arrets	,	hauteur/2)	]
				,False,base2D)
	arretM1.set('d',chemin)
	arretM1.set('stroke',couleur_male)
	arretM1.set('stroke-width',str(epaisseur_male))
	male.append(arretM1)
	
	#Arret male 2
	arretM2=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(largeur/2.+espace_arrets	,	-hauteur/2),
					(largeur/2.+espace_arrets	,	hauteur/2)	]
				,False,base2D)
	arretM2.set('d',chemin)
	arretM2.set('stroke',couleur_male)
	arretM2.set('stroke-width',str(epaisseur_male))
	male.append(arretM2)
	
	# Femelle ***************************************
	if(old_liaisons):
		barreF1=etree.Element(inkex.addNS('path','svg'))
		chemin=points2D_to_svgd([	(-largeur/2.	,	-hauteur/2),
						(largeur/2.	,	-hauteur/2.)	]
					,False,base2D)
		barreF1.set('d',chemin)
		barreF1.set('stroke',couleur_femelle)
		barreF1.set('stroke-width',str(epaisseur_femelle))
		male.append(barreF1)
		
		barreF2=etree.Element(inkex.addNS('path','svg'))
		chemin=points2D_to_svgd([	(-largeur/2.	,	hauteur/2),
						(largeur/2.	,	hauteur/2.)	]
					,False,base2D)
		barreF2.set('d',chemin)
		barreF2.set('stroke',couleur_femelle)
		barreF2.set('stroke-width',str(epaisseur_femelle))
		male.append(barreF2)
	else:
		#Rectangle
		rectangle=etree.Element(inkex.addNS('rect','svg'))
		rectangle.set('x',str(-largeur*echelle_liaison/2) )
		rectangle.set('y',str(-hauteur*echelle_liaison/2) )
		rectangle.set('width',str(largeur*echelle_liaison))
		rectangle.set('height',str(hauteur*echelle_liaison))
		rectangle.set('style','fill:none')
		rectangle.set('stroke',couleur_femelle)
		rectangle.set('stroke-width',str(epaisseur_femelle))
		femelle.append(rectangle)

		# Fond de femelle opaque ****************************
		#Rectangle - fond
		rectangle=etree.Element(inkex.addNS('rect','svg'))
		rectangle.set('x',str(-largeur*echelle_liaison/2) )
		rectangle.set('y',str(-hauteur*echelle_liaison/2) )
		rectangle.set('width',str(largeur*echelle_liaison))
		rectangle.set('height',str(hauteur*echelle_liaison))
		rectangle.set('style','fill:white')
		fond_femelle.append(rectangle)

	#Tige femelle
	ligneF=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	-hauteur/2.),
					(0	,	-hauteur/2.-longueur_tige)	]
				,True,base2D)
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle))
	femelle.append(ligneF)

	# Transformations ***************************************
	fond_femelle.set("transform","rotate("+str(-rotation)+")")
	male.set("transform","rotate("+str(-rotation)+")")
	femelle.set("transform","rotate("+str(-rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x,contexte))+","+str(convertLongueur2Inkscape(options,y0+y,contexte))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)



def dessin_Pivot_2D_face(options,contexte):
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_pivot_2D_face_x
	y = -options.liaison_pivot_2D_face_y
	#Orientation **************************************
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
	#Base *********************
	echelle_liaison=options.echelle
	Vx1,Vy1=getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	rayon = p2Df_diametre/2
	longueur_tige = p2Df_longueur_tige
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1

	#Groupes ******************************************
	liaison = etree.SubElement(contexte, 'g')
	male=etree.SubElement(liaison,'g')
	femelle=etree.SubElement(liaison,'g')

	# Male ***************************************
	axe1=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	0),
					(rayon+longueur_tige	,	0)	]
				,False,base2D)
	axe1.set('d',chemin)
	axe1.set('stroke',couleur_male)
	axe1.set('stroke-width',str(epaisseur_male))
	male.append(axe1)

	# Femelle ***************************************	
	#axe
	axe2=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	0),
					(longueur_tige+rayon	,	0)	]
				,False,base2D)	
	axe2.set('d',chemin)
	axe2.set('stroke',couleur_femelle)
	axe2.set('stroke-width',str(epaisseur_femelle))
	femelle.append(axe2)
	#cercle
	cercle=etree.Element(inkex.addNS('circle','svg'))
	cercle.set('cx',"0")
	cercle.set('cy',"0")
	cercle.set('r',str(rayon*echelle_liaison))
	cercle.set('stroke',str(couleur_femelle))
	cercle.set('stroke-width',str(epaisseur_femelle))
	cercle.set('style','fill:white')
	femelle.append(cercle)

	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation1)+")")
	femelle.set("transform","rotate("+str(rotation2)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x,contexte))+","+str(convertLongueur2Inkscape(options,y0+y,contexte))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






#===============================================================
def dessin_Pivot_3D(options,contexte):
	#Origine 2D
	x0=options.x0
	y0=options.y0
	#Base Axonometrique
	echelle_liaison=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques()
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x=options.liaison_pivot_3D_position_x
	y=options.liaison_pivot_3D_position_y
	z=options.liaison_pivot_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	ombre = True
	largeur = p3D_longueur
	rayon = p3D_diametre/2.
	rayonTige = p3D_longueur_tige_femelle
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	angle_male=-float(options.liaison_pivot_3D_orientation_male)/180.*math.pi
	angle_femelle=-float(options.liaison_pivot_3D_orientation_femelle)/180.*math.pi
	#Repere local de la liaison
	if(options.liaison_pivot_3D_type_direction=="liaison_pivot_3D_type_direction_quelconque"):
		V=v3D(options.liaison_pivot_3D_type_direction_quelconque_x,options.liaison_pivot_3D_type_direction_quelconque_y,options.liaison_pivot_3D_type_direction_quelconque_z,base)
		if V.x == V.y == V.z == 0 : V=v3D(1,0,0,base) #Si vecteur nul : on prend X par defaut
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle_liaison,angle_male)#Repere male
		Vx2,Vy2,Vz2=getBaseFromVecteur(V,echelle_liaison,angle_femelle)#Repere Femelle
	else:	#Si vecteur standard
		if(options.liaison_pivot_3D_axe=="x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle_liaison,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vx,echelle_liaison,angle_femelle)#Repere Femelle
		elif(options.liaison_pivot_3D_axe=="y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle_liaison,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vy,echelle_liaison,angle_femelle)#Repere Femelle
		else:#z
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle_liaison,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vz,echelle_liaison,angle_femelle)#Repere Femelle
	baseLocale1=(Vx1,Vy1,Vz1)
	baseLocale2=(Vx2,Vy2,Vz2)

	#Groupes 
	liaison = etree.SubElement(contexte, 'g')
	ombres = etree.SubElement(liaison, 'g')
		
	# Male ***************************************
	axe=etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-p3D_longueur_male/2.,	0,	0	),
					(p3D_longueur_male/2.,	0,	0	)
				],False,baseLocale1)
	axe.set('d',chemin)
	axe.set('stroke',couleur_male)
	axe.set('stroke-width',str(epaisseur_male))
	axe.set('style','stroke-linecap:round')
	axe.set('profondeur',str(profondeur))

	#Ombre
	#if ombre:
	#	axe_ombre=etree.Element(inkex.addNS('path','svg'))
	#	axe_ombre.set('d',chemin_ombre)
	#	axe_ombre.set('stroke','#000000')
	#	axe_ombre.set('stroke-width',str(epaisseur_male))
	#	axe_ombre.set('style','stroke-linecap:round')
	#		ombres.append(axe_ombre)

	arret1=etree.Element(inkex.addNS('path','svg'))
	chemin,profondeure=points3D_to_svgd([
					(2*largeur/3,	rayon,	0	),
					(2*largeur/3,	-rayon,	0	)
				],False,baseLocale1)
	arret1.set('d',chemin)
	arret1.set('stroke',couleur_male)
	arret1.set('stroke-width',str(epaisseur_male))
	arret1.set('style','stroke-linecap:round')
	arret1.set('profondeur',str(profondeur))
	
	#Ombre
	#if ombre:
	#	arret1_ombre=etree.Element(inkex.addNS('path','svg'))
	#	arret1_ombre.set('d',chemin_ombre)
	#	arret1_ombre.set('stroke','#000000')
	#	arret1_ombre.set('stroke-width',str(epaisseur_male))
	#	arret1_ombre.set('style','stroke-linecap:round')
	#		ombres.append(arret1_ombre)
	
	arret2=etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.-p3D_ecarts_arrets,	p3D_longueur_arrets/2.,	0	),
					(-largeur/2.-p3D_ecarts_arrets,	-p3D_longueur_arrets/2.,	0	)
				],False,baseLocale1)
	arret2.set('d',chemin)
	arret2.set('stroke',couleur_male)
	arret2.set('stroke-width',str(epaisseur_male))
	arret2.set('style','stroke-linecap:round')
	arret2.set('profondeur',str(profondeur))


	# Femelle ***************************************
	#On recupere les deux angles qui correspondent aux tangentes par rapport a la vue
	thetaCoupure1,thetaCoupure2=getAnglesCoupure(baseLocale2)

	#On construit les arcs de cercles projete
	centre1=v3D(-largeur/2,0,0,baseLocale2) #Vecteur OC1, O=centre liaison
	centre2=v3D(largeur/2,0,0,baseLocale2) #Vecteur OC1, O=centre liaison
	listeArcs1=getListePoints2DCercle(baseLocale2,centre1,rayon,0,math.pi*2,thetaCoupure1,thetaCoupure2)
	listeArcs2=getListePoints2DCercle(baseLocale2,centre2,rayon,0,math.pi*2,thetaCoupure1,thetaCoupure2)
	listeArcs2[0].reverse()#On inverse les arcs de cercle
	listeArcs2[1].reverse()

	#On construit les cylindres
	listeDemiCylindre1=listeArcs1[0]+listeArcs2[0]
	listeDemiCylindre2=listeArcs1[1]+listeArcs2[1]


	chemin,profondeurDemiCylindre1=points3D_to_svgd(listeDemiCylindre1,True,None)
	#formesFemelles1.append((chemin,profondeur))
	demiCylindre1=etree.Element(inkex.addNS('path','svg'))
	demiCylindre1.set('d',chemin)
	demiCylindre1.set('stroke',couleur_femelle)
	demiCylindre1.set('stroke-width',str(epaisseur_femelle))
	demiCylindre1.set('style','stroke-linecap:round')
	demiCylindre1.set('style','fill:white')
	demiCylindre1.set('profondeur',str(profondeurDemiCylindre1))

	chemin,profondeurDemiCylindre2=points3D_to_svgd(listeDemiCylindre2,True)
	#formesFemelles2.append((chemin,profondeur))
	demiCylindre2=etree.Element(inkex.addNS('path','svg'))
	demiCylindre2.set('d',chemin)
	demiCylindre2.set('stroke',couleur_femelle)
	demiCylindre2.set('stroke-width',str(epaisseur_femelle))
	demiCylindre2.set('style','stroke-linecap:round')
	demiCylindre2.set('style','fill:white')
	demiCylindre2.set('profondeur',str(profondeurDemiCylindre2))

	#barre femelle
	barreFemelle=etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	0,	rayon	),
					(0,	0,	rayon+p3D_longueur_tige_femelle)
				],False,baseLocale2)
	barreFemelle.set('d',chemin)
	barreFemelle.set('stroke',couleur_femelle)
	barreFemelle.set('stroke-width',str(epaisseur_femelle))
	barreFemelle.set('style','stroke-linecap:round')
	barreFemelle.set('profondeur',str(profondeur*1e10))
	


	# Ajout au Groupe *****************************************
	listeObjets=[axe,arret1,arret2,demiCylindre1,demiCylindre2,barreFemelle]
		
	ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)

	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x,contexte))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y,contexte))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
0,0
 
