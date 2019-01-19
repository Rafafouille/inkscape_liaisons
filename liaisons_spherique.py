# -- coding: utf-8 --
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
	longueur_tige=30.
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
	if(options.liaison_spherique_2D_calotte_adaptative):
		thetaMilieu=rotation_male-rotation_femelle	#Rotation de la piece male, relativement a le piece femelle
	else :
		thetaMilieu=180
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
	rayon_male=25./2
	rayon_femelle=rayon_male+2.
	thetaOuverture=60.#90 interdit !!!
	rayonTige=25.
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	#Repere local de la liaison, partie male
	if(options.liaison_spherique_3D_type_orientation_male=="\"liaison_spherique_3D_type_orientation_male_quelconque\""):
		V=v3D(options.liaison_spherique_3D_type_direction_male_quelconque_x,options.liaison_spherique_3D_type_direction_male_quelconque_y,options.liaison_spherique_3D_type_direction_male_quelconque_z,base)
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle)#Repere male
	else:	#Si vecteur standard
		if(options.liaison_spherique_3D_axe_male=="x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle)#Repere male
		elif(options.liaison_spherique_3D_axe_male=="y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle)#Repere male
		elif(options.liaison_spherique_3D_axe_male=="z"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle)#Repere male
		elif(options.liaison_spherique_3D_axe_male=="-x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx*(-1),echelle)#Repere male
		elif(options.liaison_spherique_3D_axe_male=="-y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy*(-1),echelle)#Repere male
		else:#z
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz*(-1),echelle)#Repere male
	baseLocale1=(Vx1,Vy1,Vz1)
	#Repere local de la liaison, partie femelle
	if(options.liaison_spherique_3D_type_orientation_femelle=="\"liaison_spherique_3D_type_orientation_femelle_quelconque\""):
		V=v3D(options.liaison_spherique_3D_type_direction_femelle_quelconque_x,options.liaison_spherique_3D_type_direction_femelle_quelconque_y,options.liaison_spherique_3D_type_direction_femelle_quelconque_z,base)
		Vx2,Vy2,Vz2=getBaseFromVecteur(V,echelle)#Repere male
	else:	#Si vecteur standard
		if(options.liaison_spherique_3D_axe_femelle=="x"):
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vx,echelle)#Repere femelle
		elif(options.liaison_spherique_3D_axe_femelle=="y"):
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vy,echelle)#Repere femelle
		elif(options.liaison_spherique_3D_axe_femelle=="z"):
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vz,echelle)#Repere femelle
		elif(options.liaison_spherique_3D_axe_femelle=="-x"):
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vx*(-1),echelle)#Repere femelle
		elif(options.liaison_spherique_3D_axe_femelle=="-y"):
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vy*(-1),echelle)#Repere femelle
		else:#z
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vz*(-1),echelle)#Repere femelle
	#A SUPPRIMER	
	#Vx2,Vy2,Vz2=getBaseFromVecteur(Vx,echelle)#Repere femelle
	baseLocale2=(Vx2,Vy2,Vz2)
	
	# Male ***************************************
	#Tige
	tigeMale=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(rayon_male,	0,	0	),
					(rayonTige,	0,	0	)
				],False,baseLocale1)
	tigeMale.set('d',chemin)
	tigeMale.set('stroke',couleur_male)
	tigeMale.set('stroke-width',str(epaisseur_male))
	tigeMale.set('style','stroke-linecap:round')
	tigeMale.set('profondeur',str(profondeur))

	#Boule
	boule=inkex.etree.Element(inkex.addNS('circle','svg'))
	boule.set('cx',"0")
	boule.set('cy',"0")
	boule.set('r',str(rayon_male*echelle))
	boule.set('stroke',str(couleur_male))
	boule.set('stroke-width',str(epaisseur_male))
	boule.set('style','fill:white')
	boule.set('profondeur',"0")

	
	# Femelle ***************************************
	thetaCoupure1,thetaCoupure2=getAnglesCoupure(baseLocale2)

	centre=v3D(-rayon_femelle*math.cos(thetaOuverture/180*math.pi),0,0,baseLocale2) #Vecteur OC1, O=centre liaison
	rayon=rayon_femelle*math.sin(thetaOuverture/180*math.pi)#Rayon de l'ouverture de la calotte
	listeArcsOuverture=getListePoints2DCercle(baseLocale2,centre,rayon,0,math.pi*2,thetaCoupure1,thetaCoupure2,100)
	listeOuverture=listeArcsOuverture[0][:-1]+listeArcsOuverture[1][:-1]#On rassemble les deux arcs en une seule liste
	
	
	
	#Dans cette partie, on trace le cercle qui va faire le tour de la calotte...
	n=100
	pointsCalotteAutour=[(echelle*rayon_femelle*math.cos(i*2*math.pi/n),echelle*rayon_femelle*math.sin(i*2*math.pi/n),0) for i in range(n)] #Cercle de la calotte, entier (n'y a-t-il pas un pb d'echelle) ?
	#...Puis on cherche les deux points de tangeance (s'ils existent) en calculant la distance de chaque point d'une courbe à l'autre et en gardant les minimums
	distancesCalotteAutour=getDistancesListe2Liste(pointsCalotteAutour,listeOuverture)
	distancesOuverture=getDistancesListe2Liste(listeOuverture,pointsCalotteAutour)
	#Lissage pour éviter les artefacts de discrétisation
	distancesCalotteAutour=lisseListe(distancesCalotteAutour,3)
	distancesOuverture=lisseListe(distancesOuverture,3)
	#Recherche des indices des points tangent dans chaque courbe
	indicesMiniCalotteAutour=getIndicesMins(distancesCalotteAutour)
	indicesMiniOuverture=getIndicesMins(distancesOuverture)
	
	#debug(distancesCalotteAutour)
	#debug(indicesMiniCalotteAutour)
	
	#S'il n'y a pas 2 distances minimum (s'il n'y a pas 2 points de tangence, si l'un des cercles est inclu dans l'autre)
	if len(indicesMiniCalotteAutour)<=1 or len(indicesMiniOuverture)<=1:
		
		cheminSVGOuverture,profondeurOuverture=points3D_to_svgd(listeOuverture,True)#Attention, on travaille dans la base globale
		cheminSVGCalotte,profondeurDerriere=points3D_to_svgd(pointsCalotteAutour,True)#Attention, on travaille dans la base globale
		
		
		if(profondeurOuverture>0):#Si l'ouverture est devant, on met la coque derriere, loin !
			profondeurDerriere=-0.0001
		else:#Sinon, on le met juste en avant plan
			profondeurDerriere=0.0001
			
		
		#debug(cheminSVGOuverture+cheminSVGOuverture)
		cheminSVGdevant,profondeurDevant=cheminSVGCalotte+cheminSVGOuverture,profondeurOuverture
		cheminSVGderriere,profondeurDerriere=cheminSVGCalotte,profondeurDerriere
		
	else:	#S'il y a 2 points de tangence
		#On decoupe les arcs en deux :
		calotteAutour1_1=pointsCalotteAutour[:indicesMiniCalotteAutour[0][0]+1]
		calotteAutour2=pointsCalotteAutour[indicesMiniCalotteAutour[0][0]:indicesMiniCalotteAutour[1][0]+1]
		calotteAutour1_2=pointsCalotteAutour[indicesMiniCalotteAutour[1][0]:]
		calotteAutour1=calotteAutour1_2+calotteAutour1_1
		ouverture1_1=listeOuverture[:indicesMiniOuverture[0][0]+1]
		ouverture2=listeOuverture[indicesMiniOuverture[0][0]:indicesMiniOuverture[1][0]+1]
		ouverture1_2=listeOuverture[indicesMiniOuverture[1][0]:]
		ouverture1=ouverture1_2+ouverture1_1
	
		#Quel arc de cercle pour la calotte ?
		# Si l'angle d'ouverture est <90, c'est la plus grande courbe.
		if(thetaOuverture<90):
			if len(calotteAutour1)>len(calotteAutour2):
				calotteAutour=calotteAutour1
			else:
				calotteAutour=calotteAutour2
		else:
			if len(calotteAutour1)>len(calotteAutour2):
				calotteAutour=calotteAutour2
			else:
				calotteAutour=calotteAutour1
	
		#On concatene les bouts de chemin
		cheminDevant=concateneContinu(calotteAutour,ouverture1)
		cheminDerriere=concateneContinu(calotteAutour,ouverture2)
		
		cheminSVGdevant,profondeurDevant=points3D_to_svgd(cheminDevant,True)#Attention, on travaille dans la base globale
		cheminSVGderriere,profondeurDerriere=points3D_to_svgd(cheminDerriere,True)#Attention, on travaille dans la base globale
	
	
	calotteDevant=inkex.etree.Element(inkex.addNS('path','svg'))
	calotteDevant.set('d',cheminSVGdevant)
	calotteDevant.set('stroke',couleur_femelle)
	calotteDevant.set('stroke-width',str(epaisseur_femelle))
	calotteDevant.set('style','fill:white')
	calotteDevant.set('profondeur',str(profondeurDevant))
	
	calotteDerriere=inkex.etree.Element(inkex.addNS('path','svg'))
	calotteDerriere.set('d',cheminSVGderriere)
	calotteDerriere.set('stroke',couleur_femelle)
	calotteDerriere.set('stroke-width',str(epaisseur_femelle))
	calotteDerriere.set('style','fill:white')
	calotteDerriere.set('profondeur',str(profondeurDerriere))
	

	
	
	
	#Tige
	tigeFemelle=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(rayon_femelle,	0,	0	),
					(rayonTige,	0,	0	)
				],False,baseLocale2)
	tigeFemelle.set('d',chemin)
	tigeFemelle.set('stroke',couleur_femelle)
	tigeFemelle.set('stroke-width',str(epaisseur_femelle))
	tigeFemelle.set('style','stroke-linecap:round')
	tigeFemelle.set('profondeur',str(profondeur))

	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        
        listeObjets=[tigeMale,boule,tigeFemelle,calotteDevant,calotteDerriere]
        
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)

	# Transformations ***************************************
	liaison.set("transform","translate("+str(x0+x*Vx.x+y*Vy.x+z*Vz.x)+","+str(y0+x*Vx.y+y*Vy.y+z*Vz.y)+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	
 
