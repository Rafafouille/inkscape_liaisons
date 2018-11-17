import math
import inkex
from liaisons_fonctions_utiles import *


def dessin_spherique_2D(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_spherique_2D_x
	y=options.liaison_spherique_2D_y
	#Orientation **************************************
	rotation_male=options.liaison_spherique_2D_orientation_male #Angle par defaut (sens trigo)
	if(options.liaison_spherique_2D_axe_male=="x"):
		rotation_male=0
	elif(options.liaison_spherique_2D_axe_male=="y"):
		rotation_male=90.
	elif(options.liaison_spherique_2D_axe_male=="-x"):
		rotation_male=180.
	elif(options.liaison_spherique_2D_axe_male=="-y"):
		rotation_male=-90.
	rotation_femelle=options.liaison_spherique_2D_orientation_femelle #Angle par defaut (sens trigo)
	if(options.liaison_spherique_2D_axe_femelle=="x"):
		rotation_femelle=0
	elif(options.liaison_spherique_2D_axe_femelle=="y"):
		rotation_femelle=90.
	elif(options.liaison_spherique_2D_axe_femelle=="-x"):
		rotation_femelle=180.
	elif(options.liaison_spherique_2D_axe_femelle=="-y"):
		rotation_femelle=-90.
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	old_liaisons=options.opt_gene_gene_old
	rayon_male=25./2
	rayon_femelle=rayon_male+5.
	longueur_tige=40.
	thetaOuverture=90
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1

	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle=inkex.etree.SubElement(liaison,'g')
	
	
	# Male ***************************************
	#cercle male
	cercle=inkex.etree.Element(inkex.addNS('circle','svg'))
	cercle.set('cx',"0")
	cercle.set('cy',"0")
	cercle.set('r',str(rayon_male*echelle))
	cercle.set('stroke',str(couleur_male))
	cercle.set('stroke-width',str(epaisseur_male))
	cercle.set('style','fill:white')
	male.append(cercle)
	
	#Tige male
	tige_male=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(rayon_male	,	0.),
					(longueur_tige	,	0.)	]
				,False,base2D)
	tige_male.set('d',chemin)
	tige_male.set('stroke',couleur_male)
	tige_male.set('stroke-width',str(epaisseur_male))
	male.append(tige_male)
	
	# Femelle ***************************************
	#cercle fmelle
	arc=inkex.etree.Element(inkex.addNS('path','svg'))
	liste=[]
	N=50.
	thetaMilieu=rotation_male-rotation_femelle	#Rotation de la piece male, relativement a le piece femelle
	margeTheta=5.
	if(thetaMilieu%360<thetaOuverture/2.+margeTheta):
		thetaMilieu=thetaOuverture/2.+margeTheta
	elif(thetaMilieu%360>360-thetaOuverture/2.-margeTheta):
		thetaMilieu=360-thetaOuverture/2.-margeTheta
	thetaDeb=thetaMilieu+thetaOuverture/2.
	thetaFin=thetaDeb+360-thetaOuverture
	dTheta=(thetaFin-thetaDeb)/N*math.pi/180.
	theta=thetaDeb*math.pi/180.
	while theta<thetaFin*math.pi/180.:
		liste.append((rayon_femelle*math.cos(theta),rayon_femelle*math.sin(theta)))
		theta+=dTheta
	liste.append((rayon_femelle*math.cos(theta),rayon_femelle*math.sin(theta)))
	chemin=points2D_to_svgd(liste,False,base2D)
	arc.set('d',chemin)	
	arc.set('stroke',str(couleur_femelle))
	arc.set('stroke-width',str(epaisseur_femelle))
	arc.set('style','fill:none;stroke-linecap:round')
	femelle.append(arc)
	
	
	#Tige femelle
	tige_femelle=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(rayon_femelle	,	0.),
					(longueur_tige	,	0.)	]
				,True,base2D)
	tige_femelle.set('d',chemin)
	tige_femelle.set('stroke',couleur_femelle)
	tige_femelle.set('stroke-width',str(epaisseur_femelle))
	tige_femelle.set('style','fill:none;stroke-linecap:round')
	femelle.append(tige_femelle)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(-rotation_male)+")")
	femelle.set("transform","rotate("+str(-rotation_femelle)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	



#===============================================================
def dessin_spherique_3D(options,contexte):
	#Origine 2D
	x0=options.x0
	y0=options.y0
	#Base Axonometrique
	echelle=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques(echelle)
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x=options.liaison_pivot_3D_position_x
	y=options.liaison_pivot_3D_position_y
	z=options.liaison_pivot_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	largeur=30.
	rayon=7.5
	rayonTige=25.
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	angle_male=-float(options.liaison_pivot_3D_orientation_male)/180.*math.pi
	angle_femelle=-float(options.liaison_pivot_3D_orientation_femelle)/180.*math.pi
	#Repere local de la liaison
	if(options.liaison_pivot_3D_type_direction=="\"liaison_pivot_3D_type_direction_quelconque\""):
		V=v3D(options.liaison_pivot_3D_type_direction_quelconque_x,options.liaison_pivot_3D_type_direction_quelconque_y,options.liaison_pivot_3D_type_direction_quelconque_z,base)
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle,angle_male)#Repere male
		Vx2,Vy2,Vz2=getBaseFromVecteur(V,echelle,angle_femelle)#Repere Femelle
	else:	#Si vecteur standard
		if(options.liaison_pivot_3D_axe=="x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vx,echelle,angle_femelle)#Repere Femelle
		elif(options.liaison_pivot_3D_axe=="y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vy,echelle,angle_femelle)#Repere Femelle
		else:#z
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vz,echelle,angle_femelle)#Repere Femelle
	baseLocale1=(Vx1,Vy1,Vz1)
	baseLocale2=(Vx2,Vy2,Vz2)

	
	# Male ***************************************
	axe=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur,	0,	0	),
					(largeur,	0,	0	)
				],False,baseLocale1)
	axe.set('d',chemin)
	axe.set('stroke',couleur_male)
	axe.set('stroke-width',str(epaisseur_male))
	axe.set('style','stroke-linecap:round')
	axe.set('profondeur',str(profondeur))

	
	arret1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(2*largeur/3,	rayon,	0	),
					(2*largeur/3,	-rayon,	0	)
				],False,baseLocale1)
	arret1.set('d',chemin)
	arret1.set('stroke',couleur_male)
	arret1.set('stroke-width',str(epaisseur_male))
	arret1.set('style','stroke-linecap:round')
	arret1.set('profondeur',str(profondeur))
	
	arret2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-2*largeur/3,	rayon,	0	),
					(-2*largeur/3,	-rayon,	0	)
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
	
	
	chemin,profondeurDemiCylindre1=points3D_to_svgd(listeDemiCylindre1,True)
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
					(0,	0,	rayon	),
					(0,	0,	rayonTige)
				],False,baseLocale2)
	barreFemelle.set('d',chemin)
	barreFemelle.set('stroke',couleur_femelle)
	barreFemelle.set('stroke-width',str(epaisseur_femelle))
	barreFemelle.set('style','stroke-linecap:round')
	barreFemelle.set('profondeur',str(profondeur*1e10))
	


	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        
        listeObjets=[axe,arret1,arret2,demiCylindre1,demiCylindre2,barreFemelle]
        
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)

	# Transformations ***************************************
	liaison.set("transform","translate("+str(x0+x*Vx.x+y*Vy.x+z*Vz.x)+","+str(y0+x*Vx.y+y*Vy.y+z*Vz.y)+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	
 
