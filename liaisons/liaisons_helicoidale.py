# -- coding: utf-8 --
import math
import inkex
from lxml import etree	# Nécessaire pour les groupes depuis la version 1.0
from liaisons_parametres import *
from liaisons_fonctions_utiles import *


def dessin_helicoidale_2D_cote(options,contexte):
	
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_helicoidale_2D_cote_x
	y = -options.liaison_helicoidale_2D_cote_y
	#Orientation **************************************
	rotation=options.liaison_helicoidale_2D_cote_orientation #Angle par defaut (sens trigo)
	if(options.liaison_helicoidale_2D_cote_axe=="x"):
		rotation=0
	elif(options.liaison_helicoidale_2D_cote_axe=="y"):
		rotation=90.
	elif(options.liaison_helicoidale_2D_cote_axe=="-x"):
		rotation=180.
	elif(options.liaison_helicoidale_2D_cote_axe=="-y"):
		rotation=-90.
	#Base *********************
	echelle_liaison=options.echelle
	Vx1,Vy1=getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	old_liaisons = options.opt_gene_gene_old
	pas_a_gauche = options.liaison_helicoidale_pas_a_gauche
	couleur_femelle = options.opt_gene_piece2_couleur
	couleur_male = options.opt_gene_piece1_couleur
	epaisseur_femelle = options.opt_gene_lignes_epaisseur_2
	epaisseur_male = options.opt_gene_lignes_epaisseur_1

	
	#Groupes ******************************************
	liaison = etree.SubElement(contexte, 'g')
	fond_femelle = etree.SubElement(liaison,'g')
	male=etree.SubElement(liaison,'g')
	femelle=etree.SubElement(liaison,'g')
	
	# Male ***************************************
	#Ligne male (à gauche)
	ligneAxeGauche=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-h2Dc_longueur_axe/2.,0),
					(-h2Dc_longueur/2.,0)]
				,False,base2D)
	ligneAxeGauche.set('d',chemin)
	ligneAxeGauche.set('stroke',couleur_male)
	ligneAxeGauche.set('stroke-width',str(epaisseur_male))
	ligneAxeGauche.set('style','fill:none;stroke-linecap:round')
	male.append(ligneAxeGauche)
	
	#Ligne male (à droite)
	ligneAxeDroite=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(h2Dc_longueur/2.,0),
					(h2Dc_longueur_axe/2.,0)]
				,False,base2D)
	ligneAxeDroite.set('d',chemin)
	ligneAxeDroite.set('stroke',couleur_male)
	ligneAxeDroite.set('stroke-width',str(epaisseur_male))
	ligneAxeDroite.set('style','fill:none;stroke-linecap:round')
	male.append(ligneAxeDroite)
	
	#Helice
	ligneHelice=etree.Element(inkex.addNS('path','svg'))
	
	if(old_liaisons):
		if(pas_a_gauche):
			chemin=points2D_to_svgd([(-h2Dc_longueur/2.,-h2Dc_diametre/2.),
						(h2Dc_longueur/2.,h2Dc_diametre/2.)]
					,False,base2D)
		else:
			chemin=points2D_to_svgd([(h2Dc_longueur/2.,-h2Dc_diametre/2.),
						(-h2Dc_longueur/2.,h2Dc_diametre/2.)]
					,False,base2D)
			
	else:
		
		chemin2D=[];
		xxx = -h2Dc_longueur / 2.

		while xxx<=h2Dc_longueur/2.:#On fait le sinus
			chemin2D.append((xxx,(-1)**(pas_a_gauche)*h2Dc_hauteurVagues*math.sin((xxx-h2Dc_longueur/2.)/h2Dc_longueur*2*math.pi*h2Dc_nbVagues)))
			xxx += float(h2Dc_longueur) / (h2Dc_nbPointsVagues-1)
		chemin=points2D_to_svgd(chemin2D
				,False,base2D)
				
			
		
	ligneHelice.set('d',chemin)
	ligneHelice.set('stroke',couleur_male)
	ligneHelice.set('stroke-width',str(epaisseur_male))
	ligneHelice.set('style','fill:none;stroke-linecap:round')
	male.append(ligneHelice)
	
	
	# Femelle ***************************************
	rectangle=etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-h2Dc_longueur*echelle_liaison/2) )
	rectangle.set('y',str(-h2Dc_diametre*echelle_liaison/2) )
	rectangle.set('width',str(h2Dc_longueur*echelle_liaison))
	rectangle.set('height',str(h2Dc_diametre*echelle_liaison))
	rectangle.set('style','fill:none')
	rectangle.set('stroke',couleur_femelle)
	rectangle.set('stroke-width',str(epaisseur_femelle))
	femelle.append(rectangle)
	
	#Ligne femelle
	ligneF=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	-h2Dc_diametre/2.),
					(0	,	-h2Dc_diametre/2.-h2Dc_longueur_tige)	]
				,True,base2D)
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle))
	femelle.append(ligneF)
	
	# Fond de femelle opaque ****************************
	#Rectangle - fond
	rectangle=etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-h2Dc_longueur*echelle_liaison/2) )
	rectangle.set('y',str(-h2Dc_diametre*echelle_liaison/2) )
	rectangle.set('width',str(h2Dc_longueur*echelle_liaison))
	rectangle.set('height',str(h2Dc_diametre*echelle_liaison))
	rectangle.set('style','fill:white')
	fond_femelle.append(rectangle)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(-rotation)+")")
	femelle.set("transform","rotate("+str(-rotation)+")")
	fond_femelle.set("transform","rotate("+str(-rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x,contexte))+","+str(convertLongueur2Inkscape(options,y0+y,contexte))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	

def dessin_helicoidale_2D_face(options,contexte):
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_helicoidale_2D_face_x
	y = -options.liaison_helicoidale_2D_face_y
	#Orientation **************************************
	rotation1=-options.liaison_helicoidale_2D_face_orientation1 #Angle par defaut (sens trigo)
	if(options.liaison_helicoidale_2D_face_axe1=="x"):
		rotation1=0
	elif(options.liaison_helicoidale_2D_face_axe1=="y"):
		rotation1=-90
	elif(options.liaison_helicoidale_2D_face_axe1=="-x"):
		rotation1=180
	elif(options.liaison_helicoidale_2D_face_axe1=="-y"):
		rotation1=90
	rotation2=-options.liaison_helicoidale_2D_face_orientation2 #Angle par defaut (sens trigo)
	if(options.liaison_helicoidale_2D_face_axe2=="x"):
		rotation2=0
	elif(options.liaison_helicoidale_2D_face_axe2=="y"):
		rotation2=-90
	elif(options.liaison_helicoidale_2D_face_axe2=="-x"):
		rotation2=180
	elif(options.liaison_helicoidale_2D_face_axe2=="-y"):
		rotation2=90
	#Base *********************
	echelle_liaison=options.echelle
	Vx1,Vy1=getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	rayon = h2Df_diametre_femelle / 2.
	rayon_filet = h2Df_diametre_male /2.
	longueur_tige = h2Df_longueur_tige
	pas_a_gauche = options.liaison_helicoidale_pas_a_gauche
	couleur_femelle = options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	#Groupes ******************************************
	liaison = etree.SubElement(contexte, 'g')
	femelle=etree.SubElement(liaison,'g')
	male=etree.SubElement(liaison,'g')

	# Femelle ***************************************	
	#axe
	axe2=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0			,	0),
					(longueur_tige + rayon	,	0)	]
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
	
	# Male ***************************************
	axe1=etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(rayon_filet		,	0),
					(longueur_tige + rayon	,	0)	]
				,False,base2D)
	axe1.set('d',chemin)
	axe1.set('stroke',couleur_male)
	axe1.set('stroke-width',str(epaisseur_male))
	axe1.set('style','stroke-linecap:round')
	male.append(axe1)
	
	pasVis=etree.Element(inkex.addNS('path','svg'))
	cheminVis="M "+str(rayon_filet*echelle_liaison)+",0 A "+str(rayon_filet*echelle_liaison)+" "+str(rayon_filet*echelle_liaison)+" 0 0 "+str(1-int(pas_a_gauche))+" -"+str(rayon_filet*echelle_liaison)+",0"
	pasVis.set('d',cheminVis)
	pasVis.set('stroke',couleur_male)
	pasVis.set('stroke-width',str(epaisseur_male))
	pasVis.set('style','fill:none;stroke-linecap:round')
	male.append(pasVis)


	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation1)+")")
	femelle.set("transform","rotate("+str(rotation2)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x,contexte))+","+str(convertLongueur2Inkscape(options,y0+y,contexte))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






#===============================================================
def dessin_helicoidale_3D(options,contexte):
	#Origine 2D
	x0=options.x0
	y0=options.y0
	#Base Axonometrique
	echelle=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques(echelle)
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x=options.liaison_helicoidale_3D_position_x
	y=options.liaison_helicoidale_3D_position_y
	z=options.liaison_helicoidale_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	pas_a_gauche=options.liaison_helicoidale_pas_a_gauche
	rayon=h3D_diametre/2.
	rayonTige=h3D_diametre/2.+h3D_longueur_tige_femelle
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
#	angle_male=-float(options.liaison_helicoidale_3D_orientation_male)/180.*math.pi
	angle_male=0
	angle_femelle=-float(options.liaison_helicoidale_3D_orientation_femelle)/180.*math.pi
	#Repere local de la liaison
	if(options.liaison_helicoidale_3D_type_direction=="liaison_helicoidale_3D_type_direction_quelconque"):
		V=v3D(options.liaison_helicoidale_3D_type_direction_quelconque_x,options.liaison_helicoidale_3D_type_direction_quelconque_y,options.liaison_helicoidale_3D_type_direction_quelconque_z,base)
		if V.x == V.y == V.z == 0 : V=v3D(1,0,0,base) #Si vecteur nul : on prend X par defaut
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle,angle_male)#Repere male
		Vx2,Vy2,Vz2=getBaseFromVecteur(V,echelle,angle_femelle)#Repere Femelle
	else:	#Si vecteur standard
		if(options.liaison_helicoidale_3D_axe=="x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vx,echelle,angle_femelle)#Repere Femelle
		elif(options.liaison_helicoidale_3D_axe=="y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vy,echelle,angle_femelle)#Repere Femelle
		else:#z
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vz,echelle,angle_femelle)#Repere Femelle
	baseLocale1=(Vx1,Vy1,Vz1)
	baseLocale2=(Vx2,Vy2,Vz2)


	centre1=v3D(-h3D_longueur/2,0,0,baseLocale2) #Vecteur OC1, O=centre liaison
	centre2=v3D(h3D_longueur/2,0,0,baseLocale2) #Vecteur OC2, O=centre liaison
	#On recupere les deux angles qui correspondent aux tangentes par rapport a la vue
	thetaCoupure2_1,thetaCoupure2_2=getAnglesCoupure(baseLocale2)
	thetaCoupure1_1,thetaCoupure1_2=getAnglesCoupure(baseLocale1)
	
	# Male ***************************************
	axe=etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-h3D_longueur,	0,	0	),
					(h3D_longueur,	0,	0	)
				],False,baseLocale1)
	axe.set('d',chemin)
	axe.set('stroke',couleur_male)
	axe.set('stroke-width',str(epaisseur_male))
	axe.set('style','stroke-linecap:round')
	axe.set('profondeur',str(profondeur))


	#Helice
	X=0.	#abcsisse sur x depuis le bout de la liaison
	dx=0.1	#pas
	listeHelice=[]
	cheminHelice1=""
	cheminHelice2=""
	profondeurHelice1=0
	profondeurHelice2=0
	cote=1
	theta=(-1)**(not pas_a_gauche)*2.*math.pi*X/h3D_longueur*h3D_nombre_helices
	while X<h3D_longueur:#Tant qu'on n'est pas arrivé au bout de la liaison
		Vdx=Vx1*X	#V déplacement sur x
		thetaOld=theta
		theta=(-1)**(not pas_a_gauche)*2.*math.pi*X/h3D_longueur*h3D_nombre_helices#Angle pour le point courant
		vRayon=v3D(0,rayon*math.cos(theta),rayon*math.sin(theta),baseLocale1)	#Vecteur rayon
		point=centre1+Vdx+vRayon#Coordonnées du point
		#Si on change de plan, on calcule le chemin SVG du bout d'hélice et on l'ajoute au chemin existant
		if encadreLimite(thetaOld,theta,thetaCoupure1_1) or encadreLimite(thetaOld,theta,thetaCoupure1_2):
			if encadreLimite(thetaOld,theta,thetaCoupure1_1):
				thetaCoupure=thetaCoupure1_1
			else:
				thetaCoupure=thetaCoupure1_2
			#On ajoute le dernier point entre deux jonction (pour faire un raccord continue):
			xDernier=X-dx/2.#+(thetaCoupure-thetaOld)/(theta-thetaOld)*dx
			vRayon=v3D(0,rayon*math.cos(thetaCoupure),rayon*math.sin(thetaCoupure),baseLocale1)	#Vecteur rayon
			Vdx=Vx1*xDernier	#V déplacement sur x
			point=centre1+Vdx+vRayon#Coordonnées du point
			X+=dx
			listeHelice.append((point.x,point.y,point.z))
			#assert 0,(thetaOld,theta,thetaCoupure1_1,thetaCoupure1_2,listeHelice)
			if len(listeHelice)>1:#Cas où listeHelice n'est pas nul (probleme de theta0=0 au début)
				chemin,profondeur=points3D_to_svgd(listeHelice,False)
				listeHelice=[(point.x,point.y,point.z)]#On relance un nouveau bout d'hélice, à partir de la coupure
				if(cote>0):
					cheminHelice1+=chemin
					#profondeurHelice1+=profondeur/h3D_nombre_helices/2.
				else:
					cheminHelice2+=chemin
					#profondeurHelice2+=profondeur/h3D_nombre_helices/2.
				cote*=-1
		
		X+=dx
		listeHelice.append((point.x,point.y,point.z))

		
	if len(listeHelice)>1:#S'il reste une dernier bout..
		chemin,profondeur=points3D_to_svgd(listeHelice,False)
		if(cote>0):
			cheminHelice1+=chemin
			#profondeurHelice1=profondeur/h3D_nombre_helices/2.
		else:
			cheminHelice2+=chemin
			#profondeurHelice2=profondeur/h3D_nombre_helices/2.
#	assert 0,(theta,vRayon)


	#Gestion de la profondeur		
	if baseLocale1[1].z>0:#Si l'axe y1 est positif (ca dit quel coté est au 1er plan)
		profondeurHelice1=1000
	else:
		profondeurHelice1=-1000
	profondeurHelice2=-profondeurHelice1

	
	helice1=etree.Element(inkex.addNS('path','svg'))
#	cheminHelice1,profondeurHelice1=points3D_to_svgd(listeHelice1,False)
	helice1.set('d',cheminHelice1)
	helice1.set('stroke',couleur_male)
	helice1.set('stroke-width',str(epaisseur_male))
	helice1.set('style','stroke-linecap:round')
	helice1.set('style','fill:none')
	helice1.set('profondeur',str(profondeurHelice1))
	
	helice2=etree.Element(inkex.addNS('path','svg'))
#	listeHelice2=[]
#	for p in listeArcsHelice[1]:
#		listeHelice2.append(p)
#	cheminHelice2,profondeurHelice2=points3D_to_svgd(listeHelice2,False)
	helice2.set('d',cheminHelice2)
	helice2.set('stroke',couleur_male)
	helice2.set('stroke-width',str(epaisseur_male))
	helice2.set('style','stroke-linecap:round')
	helice2.set('style','fill:none')
	helice2.set('profondeur',str(profondeurHelice2))
	
	
	# Femelle ***************************************
	
	#On construit les arcs de cercles projete
	listeArcs1=getListePoints2DCercle(baseLocale2,centre1,rayon,0,math.pi*2,thetaCoupure2_1,thetaCoupure2_2)
	listeArcs2=getListePoints2DCercle(baseLocale2,centre2,rayon,0,math.pi*2,thetaCoupure2_1,thetaCoupure2_2)
	listeArcs2[0].reverse()#On inverse les arcs de cercle
	listeArcs2[1].reverse()
	
	#On construit les cylindres
	listeDemiCylindre1=listeArcs1[0]+listeArcs2[0]
	listeDemiCylindre2=listeArcs1[1]+listeArcs2[1]
	
	
	chemin,profondeurDemiCylindre1=points3D_to_svgd(listeDemiCylindre1,True)
	demiCylindre1=etree.Element(inkex.addNS('path','svg'))
	demiCylindre1.set('d',chemin)
	demiCylindre1.set('stroke',couleur_femelle)
	demiCylindre1.set('stroke-width',str(epaisseur_femelle))
	demiCylindre1.set('style','stroke-linecap:round')
	demiCylindre1.set('style','fill:white')
	demiCylindre1.set('profondeur',str(profondeurDemiCylindre1*0.001))
	
	demiCylindreContours1=etree.Element(inkex.addNS('path','svg'))
	demiCylindreContours1.set('d',chemin)
	demiCylindreContours1.set('stroke',couleur_femelle)
	demiCylindreContours1.set('stroke-width',str(epaisseur_femelle))
	demiCylindreContours1.set('style','stroke-linecap:round')
	demiCylindreContours1.set('style','fill:none')
	demiCylindreContours1.set('profondeur',str(profondeurDemiCylindre1*100000))
	
	chemin,profondeurDemiCylindre2=points3D_to_svgd(listeDemiCylindre2,True)
	demiCylindre2=etree.Element(inkex.addNS('path','svg'))
	demiCylindre2.set('d',chemin)
	demiCylindre2.set('stroke',couleur_femelle)
	demiCylindre2.set('stroke-width',str(epaisseur_femelle))
	demiCylindre2.set('style','stroke-linecap:round')
	demiCylindre2.set('style','fill:white')
	demiCylindre2.set('profondeur',str(profondeurDemiCylindre2*0.001))
	
	demiCylindreContours2=etree.Element(inkex.addNS('path','svg'))
	demiCylindreContours2.set('d',chemin)
	demiCylindreContours2.set('stroke',couleur_femelle)
	demiCylindreContours2.set('stroke-width',str(epaisseur_femelle))
	demiCylindreContours2.set('style','stroke-linecap:round')
	demiCylindreContours2.set('style','fill:none')
	demiCylindreContours2.set('profondeur',str(profondeurDemiCylindre2*100000))
	
	
	
	#barre femelle
	barreFemelle=etree.Element(inkex.addNS('path','svg'))
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
	liaison = etree.SubElement(contexte, 'g')
        
	listeObjets=[axe,demiCylindre1,demiCylindreContours1,demiCylindre2,demiCylindreContours2,barreFemelle,helice1,helice2]
        
	ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)

	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x,contexte))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y,contexte))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	
 
