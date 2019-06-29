# -- coding: utf-8 --
import math
import inkex
from liaisons_parametres import *
from liaisons_fonctions_utiles import *


def dessin_helicoidale_2D_cote(options,contexte):
	
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_helicoidale_2D_cote_x
	y=options.liaison_helicoidale_2D_cote_y
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
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	old_liaisons=options.opt_gene_gene_old
	pas_a_gauche=options.liaison_helicoidale_pas_a_gauche
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1

	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle=inkex.etree.SubElement(liaison,'g')
	
	
	# Male ***************************************
	#Ligne male (à gauche)
	ligneAxeGauche=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-h2Dc_longueur_axe/2.,0),
					(-h2Dc_longueur/2.,0)]
				,False,base2D)
	ligneAxeGauche.set('d',chemin)
	ligneAxeGauche.set('stroke',couleur_male)
	ligneAxeGauche.set('stroke-width',str(epaisseur_male))
	ligneAxeGauche.set('style','fill:none;stroke-linecap:round')
	male.append(ligneAxeGauche)
	
	#Ligne male (à droite)
	ligneAxeDroite=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(h2Dc_longueur/2.,0),
					(h2Dc_longueur_axe/2.,0)]
				,False,base2D)
	ligneAxeDroite.set('d',chemin)
	ligneAxeDroite.set('stroke',couleur_male)
	ligneAxeDroite.set('stroke-width',str(epaisseur_male))
	ligneAxeDroite.set('style','fill:none;stroke-linecap:round')
	male.append(ligneAxeDroite)
	
	#Helice
	ligneHelice=inkex.etree.Element(inkex.addNS('path','svg'))
	
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
		xxx=-h2Dc_longueur/2
		#nbVagues=4
		#hauteurVagues=h2Dc_diametre/6.
		#nbPointsVagues=100
		while xxx<=h2Dc_longueur/2:#On fait le sinus
			chemin2D.append((xxx,(-1)**(pas_a_gauche)*h2Dc_hauteurVagues*math.sin((xxx-h2Dc_longueur/2.)/h2Dc_longueur*2*math.pi*h2Dc_nbVagues)))
			xxx+=h2Dc_longueur/(h2Dc_nbPointsVagues-1)
		chemin=points2D_to_svgd(chemin2D
				,False,base2D)
		
	ligneHelice.set('d',chemin)
	ligneHelice.set('stroke',couleur_male)
	ligneHelice.set('stroke-width',str(epaisseur_male))
	ligneHelice.set('style','fill:none;stroke-linecap:round')
	male.append(ligneHelice)
	
	
	# Femelle ***************************************
	rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-h2Dc_longueur*echelle/2) )
	rectangle.set('y',str(-h2Dc_diametre*echelle/2) )
	rectangle.set('width',str(h2Dc_longueur*echelle))
	rectangle.set('height',str(h2Dc_diametre*echelle))
	rectangle.set('style','fill:none')
	rectangle.set('stroke',couleur_femelle)
	rectangle.set('stroke-width',str(epaisseur_femelle))
	femelle.append(rectangle)
	
	#Ligne femelle
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	-h2Dc_diametre/2.),
					(0	,	-h2Dc_diametre/2.-h2Dc_longueur_tige)	]
				,True,base2D)
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle))
	femelle.append(ligneF)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(-rotation)+")")
	femelle.set("transform","rotate("+str(-rotation)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	

def dessin_helicoidale_2D_face(options,contexte):
	#Position *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_helicoidale_2D_face_x
	y=options.liaison_helicoidale_2D_face_y
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
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	rayon=h2Df_diametre_femelle/2.
	h2Df_longueur_tige=rayon
	pas_a_gauche=options.liaison_helicoidale_pas_a_gauche
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1

	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        #groupe_rotation = inkex.etree.SubElement(liaison, 'g')
	femelle=inkex.etree.SubElement(liaison,'g')
	male=inkex.etree.SubElement(liaison,'g')

	# Femelle ***************************************	
	#axe
	axe2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	0),
					(h2Df_longueur_tige+rayon	,	0)	]
				,False,base2D)	
	axe2.set('d',chemin)
	axe2.set('stroke',couleur_femelle)
	axe2.set('stroke-width',str(epaisseur_femelle))
	femelle.append(axe2)
	#cercle
	cercle=inkex.etree.Element(inkex.addNS('circle','svg'))
	cercle.set('cx',"0")
	cercle.set('cy',"0")
	cercle.set('r',str(rayon*echelle))
	cercle.set('stroke',str(couleur_femelle))
	cercle.set('stroke-width',str(epaisseur_femelle))
	cercle.set('style','fill:white')
	femelle.append(cercle)
	
	# Male ***************************************
	axe1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(h2Df_diametre_male/2. ,	0),
					(rayon+h2Df_longueur_tige,	0)	]
				,False,base2D)
	axe1.set('d',chemin)
	axe1.set('stroke',couleur_male)
	axe1.set('stroke-width',str(epaisseur_male))
	axe1.set('style','stroke-linecap:round')
	male.append(axe1)
	
	pasVis=inkex.etree.Element(inkex.addNS('path','svg'))
	cheminVis="M "+str(h2Df_diametre_male/2.)+",0 A "+str(h2Df_diametre_male/2.)+" "+str(h2Df_diametre_male/2.)+" 0 0 "+str(1-int(pas_a_gauche))+" -"+str(h2Df_diametre_male/2.)+",0"
	pasVis.set('d',cheminVis)
	pasVis.set('stroke',couleur_male)
	pasVis.set('stroke-width',str(epaisseur_male))
	pasVis.set('style','fill:none;stroke-linecap:round')
	male.append(pasVis)


	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation1)+")")
	femelle.set("transform","rotate("+str(rotation2)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
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
	x=options.liaison_pivot_3D_position_x
	y=options.liaison_pivot_3D_position_y
	z=options.liaison_pivot_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	rayon=h3D_diametre/2.
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
					(-h3D_longueur,	0,	0	),
					(h3D_longueur,	0,	0	)
				],False,baseLocale1)
	axe.set('d',chemin)
	axe.set('stroke',couleur_male)
	axe.set('stroke-width',str(epaisseur_male))
	axe.set('style','stroke-linecap:round')
	axe.set('profondeur',str(profondeur))

	
	arret1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(2*h3D_longueur/3,	rayon,	0	),
					(2*h3D_longueur/3,	-rayon,	0	)
				],False,baseLocale1)
	arret1.set('d',chemin)
	arret1.set('stroke',couleur_male)
	arret1.set('stroke-width',str(epaisseur_male))
	arret1.set('style','stroke-linecap:round')
	arret1.set('profondeur',str(profondeur))
	
	arret2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-2*h3D_longueur/3,	rayon,	0	),
					(-2*h3D_longueur/3,	-rayon,	0	)
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
	centre1=v3D(-h3D_longueur/2,0,0,baseLocale2) #Vecteur OC1, O=centre liaison
	centre2=v3D(h3D_longueur/2,0,0,baseLocale2) #Vecteur OC1, O=centre liaison
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
	
 
