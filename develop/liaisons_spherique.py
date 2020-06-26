# -- coding: utf-8 --
import math
import inkex
from liaisons_fonctions_utiles import *
from liaisons_parametres import *

def dessin_spherique_2D(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_spherique_2D_x
	y = -options.liaison_spherique_2D_y
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
	echelle_liaison=options.echelle
	Vx1,Vy1=getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	couleur_femelle = options.opt_gene_piece2_couleur
	couleur_male = options.opt_gene_piece1_couleur
	epaisseur_femelle = options.opt_gene_lignes_epaisseur_2
	epaisseur_male = options.opt_gene_lignes_epaisseur_1
	old_liaisons = options.opt_gene_gene_old
	rayon_male = s2D_diametre / 2.
	rayon_femelle = rayon_male + s2D_ecart + (epaisseur_femelle+epaisseur_male)/2.
	rayon_tige_male = s2D_rayon_tiges_male
	rayon_tige_femelle = s2D_rayon_tiges_femelle
	thetaOuverture = s2D_angle_ouverture
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle=inkex.etree.SubElement(liaison,'g')
	# Male ***************************************
	#cercle male
	cercle=inkex.etree.Element(inkex.addNS('circle','svg'))
	cercle.set('cx',"0")
	cercle.set('cy',"0")
	cercle.set('r',str(rayon_male*echelle_liaison))
	cercle.set('stroke',str(couleur_male))
	cercle.set('stroke-width',str(epaisseur_male))
	cercle.set('style','fill:white')
	male.append(cercle)
	#Tige male
	tige_male=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(rayon_male	,	0.),
					(rayon_tige_male	,	0.)	]
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
					(rayon_tige_femelle	,	0.)	]
				,True,base2D)
	tige_femelle.set('d',chemin)
	tige_femelle.set('stroke',couleur_femelle)
	tige_femelle.set('stroke-width',str(epaisseur_femelle))
	tige_femelle.set('style','fill:none;stroke-linecap:round')
	femelle.append(tige_femelle)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(-rotation_male)+")")
	femelle.set("transform","rotate("+str(-rotation_femelle)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	



#===============================================================
def dessin_spherique_3D(options,contexte):
	#Origine 2D
	x0 = options.x0
	y0 = options.y0
	#Base Axonometrique
	echelle = options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques()
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x = options.liaison_spherique_3D_position_x
	y = options.liaison_spherique_3D_position_y
	z = options.liaison_spherique_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	couleur_femelle = options.opt_gene_piece2_couleur
	couleur_male = options.opt_gene_piece1_couleur
	epaisseur_femelle = options.opt_gene_lignes_epaisseur_2
	epaisseur_male = options.opt_gene_lignes_epaisseur_1
	rayon_male = s3D_diametre / 2.
	rayon_femelle = rayon_male + s3D_ecart + (epaisseur_femelle+epaisseur_male)/2.
	angle_ouverture = s3D_angle_ouverture
	if angle_ouverture == 180 :
		angle_ouverture = 179.9
	thetaOuverture = angle_ouverture / 2. * math.pi/180. #Demi angle d'ouverture #90 interdit !!!
	rayonTige = s3D_rayon_tiges 
	rayon_ouverture = rayon_femelle * math.sin(thetaOuverture)
	#Repere local de la liaison, partie male
	if(options.liaison_spherique_3D_type_orientation_male=="\"liaison_spherique_3D_type_orientation_male_quelconque\""):
		V=v3D(options.liaison_spherique_3D_type_direction_male_quelconque_x,options.liaison_spherique_3D_type_direction_male_quelconque_y,options.liaison_spherique_3D_type_direction_male_quelconque_z,base)
		if V.x == V.y == V.z == 0 : V=v3D(1,0,0,base) #Si vecteur nul : on prend X par defaut
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
		if V.x == V.y == V.z == 0 : V=v3D(1,0,0,base) #Si vecteur nul : on prend X par defaut
		Vx2,Vy2,Vz2=getBaseFromVecteur(V,echelle)#Repere male
	else:	#Si vecteur standard
		if(options.liaison_spherique_3D_axe_femelle=="x"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vx,echelle)#Repere femelle
		elif(options.liaison_spherique_3D_axe_femelle=="y"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vy,echelle)#Repere femelle
		elif(options.liaison_spherique_3D_axe_femelle=="z"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vz,echelle)#Repere femelle
		elif(options.liaison_spherique_3D_axe_femelle=="-x"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vx*(-1),echelle)#Repere femelle
		elif(options.liaison_spherique_3D_axe_femelle=="-y"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vy*(-1),echelle)#Repere femelle
		elif(options.liaison_spherique_3D_axe_femelle=="-z"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vz*(-1),echelle)#Repere femelle
		else : #opposé à la piece male
			Vx2,Vy2,Vz2 = -Vx1,-Vy1,-Vz1 #Repere femelle
	#A SUPPRIMER	
	#Vx2,Vy2,Vz2=getBaseFromVecteur(Vx,echelle)#Repere femelle
	baseLocaleTige=(Vx2,Vy2,Vz2)
	
	#Repere pièce femelle, juste pour la calotte
	if options.liaison_spherique_3D_calotte_adaptative:
		Vx3, Vy3, Vz3 = -Vx1, -Vy1, -Vz1
	else :
		Vx3, Vy3, Vz3 = Vx2, Vy2, Vz2
	baseLocaleCalotte=(Vx3,Vy3,Vz3)
	
	listeObjets = [] # Liste des dessins à classer dans l'espace
		
	angle_ecran = math.acos((Vx3*v3D(0,0,-1))/Vx3.norme()) # Angle entre la direction de -Vx3 (opposé à la femelle) et la normale à l'écran
	angle_bord_ouverture_ecran_max = angle_ecran + thetaOuverture	# S'il est supérieur à 90°, cela veut dire que le bord de l'ouverture "le plus en arriere plan" est au dela du plan médian
	angle_bord_ouverture_ecran_min = angle_ecran - thetaOuverture		# S'il est supérieur à 90°, cela veut dire que le bord de l'ouverture est derrière le cercle

		
	
	
	
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
	listeObjets.append(tigeMale)

	#Boule
	boule=inkex.etree.Element(inkex.addNS('circle','svg'))
	boule.set('cx',"0")
	boule.set('cy',"0")
	boule.set('r',str(rayon_male*echelle))
	boule.set('stroke',str(couleur_male))
	boule.set('stroke-width',str(epaisseur_male))
	boule.set('style','fill:white')
	boule.set('profondeur',"0")
	listeObjets.append(boule)

	
	# Femelle ***************************************

	
	
	text = " ( "+str(angle_ecran/math.pi*180)+" , "+str(angle_bord_ouverture_ecran_min/math.pi*180)+" , "+str(angle_bord_ouverture_ecran_max/math.pi*180)+" )"
	# CAS OU L'OUVERTURE EST DERRIERE LA SPHERE
	if angle_bord_ouverture_ecran_min > math.pi/2 : # Si l'ouverture est derriere le disque
		boule_femelle=inkex.etree.Element(inkex.addNS('circle','svg'))
		boule_femelle.set('cx',"0")
		boule_femelle.set('cy',"0")
		boule_femelle.set('r',str(rayon_femelle*echelle))
		boule_femelle.set('stroke',str(couleur_femelle))
		boule_femelle.set('stroke-width',str(epaisseur_femelle))
		boule_femelle.set('style','fill:white')
		boule_femelle.set('profondeur',"0.00001") # Juste devant la boule
		listeObjets.append(boule_femelle)
	#CAS OU L'OUVERTURE EST ENTIEREMENT DEVANT LA SPHERE
	elif angle_bord_ouverture_ecran_max < math.pi/2 : # Si l'ouverture est totalement devant le disque
		#assert 0, "devant le cercle"+text
		n = 100
		liste_points_calotte = [( rayon_femelle*math.cos(2*math.pi/n*i)*echelle, rayon_femelle*math.sin(2*math.pi/n*i)*echelle, 0 ) for i in range(n)] # Dans la base normale à l'écran
		liste_points_ouverture = [( -rayon_femelle*math.cos(thetaOuverture) , rayon_ouverture*math.cos(2*math.pi/n*i), rayon_ouverture*math.sin(2*math.pi/n*i) ) for i in range(n)] # Dans la base normale à l'écran
		liste_points_ouverture.reverse() #Pour avoir le chemin dans l'autre sens
		
		calotte=inkex.etree.Element(inkex.addNS('path','svg'))
		
		chemin_calotte,profondeur_calotte=points3D_to_svgd(liste_points_calotte,True,(v3D(1,0,0),v3D(0,1,0),v3D(0,0,1)))
		chemin_ouverture,profondeur_ouverture=points3D_to_svgd(liste_points_ouverture,True,baseLocaleCalotte)
		
		#assert 0, chemin_calotte
		calotte.set('d',chemin_calotte+chemin_ouverture)
		calotte.set('stroke',couleur_femelle)
		calotte.set('stroke-width',str(epaisseur_femelle))
		calotte.set('fill',"white")
		calotte.set('style','stroke-linecap:round')
		calotte.set('profondeur',str(profondeur_calotte))
		listeObjets.append(calotte)

		
	# l'ouverture est cachée, mais on voit l'un de ses bords
	elif angle_ecran > math.pi/2 :

		# On calcule l'ouverture ******
		ouverture=inkex.etree.Element(inkex.addNS('path','svg'))
		n = 100
		

		liste_points_ouverture = [( -rayon_femelle*math.cos(thetaOuverture) , rayon_ouverture*math.cos(2*math.pi/n*i), rayon_ouverture*math.sin(2*math.pi/n*i) ) for i in range(n)] # Dans la base normale à l'écran
		
		liste_points_ouverture_ecran=[v3D(liste_points_ouverture[i][0],liste_points_ouverture[i][1],liste_points_ouverture[i][2],baseLocaleCalotte) for i in range(len(liste_points_ouverture))]

		#assert 0,liste_points_ouverture_ecran
		
		# On va couper le bout d'ouverture qui n'est pas visible
		liste_troncons = []	# On va couper le chemin de l'ellipse en troncons
		troncon=[]
		for i in range(len(liste_points_ouverture)) : #On va enlever les points qui sont en avant plan, dans l'ellipse
			point=liste_points_ouverture_ecran[i] #Projection dans la base de l'ecran
			if point.z >= 0: #Si on le garde (en avant plan)
				troncon.append(liste_points_ouverture[i])
				#assert 0,str(liste_points_ouverture[i])+"\n"+str(point)
			elif len(troncon)!=0: # Si on le garde pas, mais qu'on gardait le precedent (on coupe le troncon precedent)
				liste_troncons.append(troncon)
				troncon=[]
				#assert 0,"point vide"
		if len(troncon)!=0 : liste_troncons.append(troncon) #Dernier tour
		liste_troncons.reverse()
		liste_points_ouverture = [] #On refait la liste de points juste avec les bons troncons
		for i in range(len(liste_troncons)):
			liste_points_ouverture+=liste_troncons[i]
		chemin_ouverture,profondeur_ouverture=points3D_to_svgd(liste_points_ouverture,False,baseLocaleCalotte)

		
		
		# On calcule la sphere
		p_ouverture_min= v3D(liste_points_ouverture[0][0],liste_points_ouverture[0][1],liste_points_ouverture[0][2],baseLocaleCalotte) # onnrecupere les extremités de louverture
		p_ouverture_max= v3D(liste_points_ouverture[-1][0],liste_points_ouverture[-1][1],liste_points_ouverture[-1][2],baseLocaleCalotte)
		theta_min = math.atan2(p_ouverture_min.y,p_ouverture_min.x) % (2*math.pi)	# Angles (projeté dans le plan de l'écran) entre les deux extrémités de la courbe qui décrit la calotte
		theta_max = math.atan2(p_ouverture_max.y,p_ouverture_max.x) % (2*math.pi)
		theta_min,theta_max = min([theta_min,theta_max]),max([theta_min,theta_max])
		# Dans quel sens on dessine ?
		if (math.pi-(theta_max-theta_min)) > 0 and angle_ouverture < 180 :
			theta_min, theta_max = theta_max-2*math.pi, theta_min
		if (math.pi-(theta_max-theta_min)) < 0 and angle_ouverture > 180 :
			theta_min, theta_max = theta_max-2*math.pi, theta_min
			
		pas = (theta_max-theta_min)/float(n)
		
		liste_points_calotte = [( rayon_femelle*math.cos(theta_min+i*pas)*echelle, rayon_femelle*math.sin(theta_min+i*pas)*echelle, 0 ) for i in range(n+1)] # Dans la base normale à l'écran
		#assert 0, liste_troncons
		
		chemin_calotte,profondeur_calotte=points3D_to_svgd(liste_points_calotte,False,(v3D(1,0,0),v3D(0,1,0),v3D(0,0,1)))
		
		calotte=inkex.etree.Element(inkex.addNS('path','svg'))	
		calotte.set('d',chemin_calotte+chemin_ouverture)
		calotte.set('stroke',couleur_femelle)
		calotte.set('stroke-width',str(epaisseur_femelle))
		calotte.set('fill',"white")
		calotte.set('style','stroke-linecap:round')
		calotte.set('profondeur',str(profondeur_calotte))
		listeObjets.append(calotte)	
			
	else:# angle_ecran < math.pi/2 :
		ouverture=inkex.etree.Element(inkex.addNS('path','svg'))
		n = 100
		liste_points_ouverture = [( -rayon_femelle*math.cos(thetaOuverture) , rayon_ouverture*math.cos(2*math.pi/n*i), rayon_ouverture*math.sin(2*math.pi/n*i) ) for i in range(n)] # Dans la base normale à l'écran
		liste_points_ouverture_ecran=[v3D(liste_points_ouverture[i][0],liste_points_ouverture[i][1],liste_points_ouverture[i][2],baseLocaleCalotte) for i in range(len(liste_points_ouverture))]


		# On va couper le bout d'ouverture en deux (avant plan / arriere plan)
		liste_troncons_devant = []	# On va couper le chemin de l'ellipse en troncons
		liste_troncons_arriere = []	
		
		troncon = []
		plan = "" # d= devant, a =arriere
		
		for i in range(len(liste_points_ouverture)) : #On va enlever les points qui sont en avant plan, dans l'ellipse
			point=liste_points_ouverture_ecran[i] #Projection dans la base de l'ecran
			if point.z >= 0: #Si le point appartient à l'avant plan
				if plan == "a" : #Si on suivait un troncons d'arriere plan
					liste_troncons_arriere.append(troncon) # On le stocke dans la liste des troncons arriere
					troncon = [] #On réinitialise avec le 1er point du nouveau troncon
				troncon.append(liste_points_ouverture[i])
				plan = "d"
			else :	# Si le point appartient à l'arriere plan
				if plan == "d" : #Si on suivait un troncon en avant plan arriere plan
					liste_troncons_devant.append(troncon) # On le stocke dans la liste des troncons arriere
					troncon = [] #On réinitialise avec le 1er point du nouveau troncon
				troncon.append(liste_points_ouverture[i])
				plan = "a"
				
		if len(troncon)!=0 : # On finalise le dernier tour
			if plan == "a" :
				liste_troncons_arriere.append(troncon) #Si c'est un arriere plan
			else:
				liste_troncons_devant.append(troncon) #Si c'est une avant plan
				
		if len(liste_troncons_arriere) > 1 :
			liste_troncons_arriere.reverse()
		if len(liste_troncons_devant) > 1 :
			liste_troncons_devant.reverse()

		liste_points_ouverture_arriere = [] #On refait la liste de points juste avec les bons troncons
		for i in range(len(liste_troncons_arriere)):
			liste_points_ouverture_arriere+=liste_troncons_arriere[i]
		liste_points_ouverture_devant = [] #On refait la liste de points juste avec les bons troncons
		for i in range(len(liste_troncons_devant)):
			liste_points_ouverture_devant+=liste_troncons_devant[i]
			
			



		# On calcule la sphere
		p_ouverture_min= v3D(liste_points_ouverture_arriere[0][0],liste_points_ouverture_arriere[0][1],liste_points_ouverture_arriere[0][2],baseLocaleCalotte) # onnrecupere les extremités de louverture
		p_ouverture_max= v3D(liste_points_ouverture_arriere[-1][0],liste_points_ouverture_arriere[-1][1],liste_points_ouverture_arriere[-1][2],baseLocaleCalotte)
		theta_min = math.atan2(p_ouverture_min.y,p_ouverture_min.x) % (2*math.pi)	# Angles (projeté dans le plan de l'écran) entre les deux extrémités de la courbe qui décrit la calotte
		theta_max = math.atan2(p_ouverture_max.y,p_ouverture_max.x) % (2*math.pi)
		theta_min,theta_max = min([theta_min,theta_max]),max([theta_min,theta_max])
		#	assert 0, str(theta_min*180/math.pi)+"    "+str(theta_max*180/math.pi)
		# Dans quel sens on dessine la sphere ?
		if (math.pi-(theta_max-theta_min)) > 0 and angle_ouverture < 180 :
			theta_min, theta_max = theta_max-2*math.pi, theta_min
		if (math.pi-(theta_max-theta_min)) < 0 and angle_ouverture > 180 :
			theta_min, theta_max = theta_max-2*math.pi, theta_min
			
		pas = (theta_max-theta_min)/float(n)
		liste_points_calotte = [( rayon_femelle*math.cos(theta_min+i*pas)*echelle, rayon_femelle*math.sin(theta_min+i*pas)*echelle, 0 ) for i in range(n+1)] # Dans la base normale à l'écran

		
		
		# On inverse éventuellement les chemins pour qu'il y ait une continuité
		deb_ouverture_devant_ecran = v3D(liste_points_ouverture_devant[0][0],liste_points_ouverture_devant[0][1],liste_points_ouverture_devant[0][2],baseLocaleCalotte)
		fin_ouverture_devant_ecran = v3D(liste_points_ouverture_devant[-1][0],liste_points_ouverture_devant[-1][1],liste_points_ouverture_devant[-1][2],baseLocaleCalotte)
		deb_ouverture_derriere_ecran = v3D(liste_points_ouverture_arriere[0][0],liste_points_ouverture_arriere[0][1],liste_points_ouverture_arriere[0][2],baseLocaleCalotte)
		fin_ouverture_derriere_ecran = v3D(liste_points_ouverture_arriere[0][0],liste_points_ouverture_arriere[0][1],liste_points_ouverture_arriere[0][2],baseLocaleCalotte)
		deb_calotte=v3D(liste_points_calotte[0][0],liste_points_calotte[0][1],liste_points_calotte[0][2])
		fin_calotte=v3D(liste_points_calotte[-1][0],liste_points_calotte[-1][1],liste_points_calotte[-1][2])
		
		if (deb_ouverture_devant_ecran-deb_calotte).norme() < (deb_ouverture_devant_ecran-fin_calotte).norme():
			liste_points_ouverture_devant.reverse()
		
		if (deb_ouverture_derriere_ecran-deb_calotte).norme() < (deb_ouverture_derriere_ecran-fin_calotte).norme():
			liste_points_ouverture_arriere.reverse()
			

		
		#Conversion en chemin SVG
		chemin_ouverture_devant, profondeur_ouverture_devant = points3D_to_svgd(liste_points_ouverture_devant, False, baseLocaleCalotte)
		chemin_ouverture_arriere, profondeur_ouverture_arriere = points3D_to_svgd(liste_points_ouverture_arriere, False, baseLocaleCalotte)
		
		chemin_calotte,profondeur_calotte=points3D_to_svgd(liste_points_calotte,True,(v3D(1,0,0),v3D(0,1,0),v3D(0,0,1)))
		
		devant=inkex.etree.Element(inkex.addNS('path','svg'))	
		devant.set('d',chemin_ouverture_devant+"L"+chemin_calotte[1:]) # Z pour fermer
		devant.set('stroke',couleur_femelle)
		devant.set('stroke-width',str(epaisseur_femelle))
		devant.set('fill',"white")
		devant.set('style','stroke-linecap:round;stroke-linejoin:round')
		devant.set('profondeur','0.00001')
		listeObjets.append(devant)	
	
		arriere=inkex.etree.Element(inkex.addNS('path','svg'))	
		arriere.set('d',chemin_ouverture_arriere+"L"+chemin_calotte[1:])
		arriere.set('stroke',couleur_femelle)
		arriere.set('stroke-width',str(epaisseur_femelle))
		arriere.set('fill',"white")
		arriere.set('style','stroke-linecap:round;stroke-linejoin:round')
		arriere.set('profondeur','-0.00001')
		listeObjets.append(arriere)
	
	#Tige
	tigeFemelle=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(rayon_femelle,	0,	0	),
					(rayonTige,	0,	0	)
				],False,baseLocaleTige)
	tigeFemelle.set('d',chemin)
	tigeFemelle.set('stroke',couleur_femelle)
	tigeFemelle.set('stroke-width',str(epaisseur_femelle))
	tigeFemelle.set('style','stroke-linecap:round')
	tigeFemelle.set('profondeur',str(profondeur))
	listeObjets.append(tigeFemelle)

	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        
        #listeObjets=[tigeMale,boule,tigeFemelle,calotteDevant,calotteDerriere]
        
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)

	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	
 
