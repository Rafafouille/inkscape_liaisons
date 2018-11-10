import math
import inkex
from liaisons_fonctions_utiles import *


def dessin_Pivot_Glissant_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Variables *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_pivot_glissant_2D_cote_x
	y=options.liaison_pivot_glissant_2D_cote_y
	old_liaisons=options.opt_gene_gene_old
	echelle=options.echelle
	largeur=30.
	hauteur=15.
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	rotation=-options.liaison_pivot_glissant_2D_cote_orientation #Angle par defaut (sens trigo)
	if(options.liaison_pivot_glissant_2D_cote_axe=="x"):
		rotation=0
	elif(options.liaison_pivot_glissant_2D_cote_axe=="y"):
		rotation=-90
	elif(options.liaison_pivot_glissant_2D_cote_axe=="-x"):
		rotation=180
	elif(options.liaison_pivot_glissant_2D_cote_axe=="-y"):
		rotation=90
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        #groupe_rotation = inkex.etree.SubElement(liaison, 'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle=inkex.etree.SubElement(liaison,'g')
	
	#Base
	vx=v2D(echelle,0)
	vy=v2D(0,echelle)
	vx.rotation(rotation)
	vy.rotation(rotation)
	
	# Male ***************************************
	#Ligne male
	ligneM=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-largeur/2-epaisseur_femelle-10*epaisseur_male	,	0),
				(largeur/2+epaisseur_femelle+10*epaisseur_male	,	0)	])
	ligneM.set('d',chemin)
	ligneM.set('stroke',couleur_male)
	ligneM.set('stroke-width',str(epaisseur_male))
	male.append(ligneM)
	
	# Femelle ***************************************
	if(old_liaisons):
		barreF1=inkex.etree.Element(inkex.addNS('path','svg'))
		chemin=points_to_svgd([	(-largeur/2	,	-hauteur/2),
					(largeur/2	,	-hauteur/2)	])
		barreF1.set('d',chemin)
		barreF1.set('stroke',couleur_femelle)
		barreF1.set('stroke-width',str(epaisseur_femelle))
		male.append(barreF1)
		
		barreF2=inkex.etree.Element(inkex.addNS('path','svg'))
		chemin=points_to_svgd([	(-largeur/2	,	hauteur/2),
					(largeur/2	,	hauteur/2)	])
		barreF2.set('d',chemin)
		barreF2.set('stroke',couleur_femelle)
		barreF2.set('stroke-width',str(epaisseur_femelle))
		male.append(barreF2)
	else:
		#Rectangle
		rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
		rectangle.set('x',str(-largeur*echelle/2) )
		rectangle.set('y',str(-hauteur*echelle/2) )
		rectangle.set('width',str(largeur*echelle))
		rectangle.set('height',str(hauteur*echelle))
		rectangle.set('style','fill:none')
		rectangle.set('stroke',couleur_femelle)
		rectangle.set('stroke-width',str(epaisseur_femelle))
		femelle.append(rectangle)
	
	#Ligne femelle
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(0	,	hauteur/2),
				(0	,	hauteur)	])
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle*echelle))
	femelle.append(ligneF)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation)+")")
	femelle.set("transform","rotate("+str(rotation)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")

	

def dessin_Pivot_Glissant_2D_face(options,contexte):
	x0=options.x0
	y0=options.y0
	x=options.liaison_pivot_glissant_2D_face_x
	y=options.liaison_pivot_glissant_2D_face_y
	rayon=15./2
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	rotation1=-options.liaison_pivot_glissant_2D_face_orientation1 #Angle par defaut (sens trigo)
	if(options.liaison_pivot_glissant_2D_face_axe1=="x"):
		rotation1=0
	elif(options.liaison_pivot_glissant_2D_face_axe1=="y"):
		rotation1=-90
	elif(options.liaison_pivot_glissant_2D_face_axe1=="-x"):
		rotation1=180
	elif(options.liaison_pivot_glissant_2D_face_axe1=="-y"):
		rotation1=90
	rotation2=-options.liaison_pivot_glissant_2D_face_orientation2 #Angle par defaut (sens trigo)
	if(options.liaison_pivot_glissant_2D_face_axe2=="x"):
		rotation2=0
	elif(options.liaison_pivot_glissant_2D_face_axe2=="y"):
		rotation2=-90
	elif(options.liaison_pivot_glissant_2D_face_axe2=="-x"):
		rotation2=180
	elif(options.liaison_pivot_glissant_2D_face_axe2=="-y"):
		rotation2=90
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        #groupe_rotation = inkex.etree.SubElement(liaison, 'g')
	femelle=inkex.etree.SubElement(liaison,'g')
	male=inkex.etree.SubElement(liaison,'g')

	
	# Femelle ***************************************	
	#axe
	axe2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(0	,	0),
				(2*rayon,	0)	])
	axe2.set('d',chemin)
	axe2.set('stroke',couleur_femelle)
	axe2.set('stroke-width',str(epaisseur_femelle))
	femelle.append(axe2)
	#cercle
	cercle=inkex.etree.Element(inkex.addNS('circle','svg'))
	cercle.set('cx',"0")
	cercle.set('cy',"0")
	cercle.set('r',str(rayon))
	cercle.set('stroke',str(couleur_femelle))
	cercle.set('stroke-width',str(epaisseur_femelle))
	cercle.set('style','fill:white')
	femelle.append(cercle)
	
	# Male ***************************************
	axe1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(0	,	0),
				(2*rayon,	0)	])
	axe1.set('d',chemin)
	axe1.set('stroke',couleur_male)
	axe1.set('stroke-width',str(epaisseur_male))
	male.append(axe1)
	#Puce
	puce=inkex.etree.Element(inkex.addNS('circle','svg'))
	puce.set('cx',"0")
	puce.set('cy',"0")
	puce.set('r',str(2*epaisseur_male))
	puce.set('stroke','none')
#	puce.set('stroke-width',str(epaisseur_femelle))
	puce.set('style','fill:'+couleur_male)
	male.append(puce)
		
	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation1)+")")
	femelle.set("transform","rotate("+str(rotation2)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
	






#===============================================================
def dessin_Pivot_Glissant_3D(options,contexte):
	#Origine 2D
	x0=options.x0
	y0=options.y0
	#Base Axonometrique
	echelle=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques(echelle)
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x=options.liaison_pivot_glissant_3D_position_x
	y=options.liaison_pivot_glissant_3D_position_y
	z=options.liaison_pivot_glissant_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	largeur=30.*math.sqrt(2./3)
	rayon=7.5*math.sqrt(2./3)
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
#	angle_male-=float(options.liaison_pivot_glissant_3D_orientation_male)/180.*math.pi
	angle_femelle=-float(options.liaison_pivot_glissant_3D_orientation_femelle)/180.*math.pi
	#Repere local de la liaison
	if(options.liaison_pivot_glissant_3D_type_direction=="\"liaison_pivot_glissant_3D_type_direction_quelconque\""):
		V=v3D(options.liaison_pivot_glissant_3D_type_direction_quelconque_x,options.liaison_pivot_glissant_3D_type_direction_quelconque_y,options.liaison_pivot_glissant_3D_type_direction_quelconque_z,base)
#		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle,angle_male)#Repere male
		Vx2,Vy2,Vz2=getBaseFromVecteur(V,echelle,angle_femelle)#Repere Femelle
	else:	#Si vecteur standard
		if(options.liaison_pivot_glissant_3D_axe=="x"):
#			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vx,echelle,angle_femelle)#Repere Femelle
		elif(options.liaison_pivot_glissant_3D_axe=="y"):
#			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vy,echelle,angle_femelle)#Repere Femelle
		else:#z
#			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vz,echelle,angle_femelle)#Repere Femelle
#	baseLocale1=(Vx1,Vy1,Vz1)
	baseLocale=(Vx2,Vy2,Vz2)

	
	# Male ***************************************
	axe=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur,	0,	0	),
					(largeur,	0,	0	)
				],False,baseLocale)
	axe.set('d',chemin)
	axe.set('stroke',couleur_male)
	axe.set('stroke-width',str(epaisseur_male))
	axe.set('style','stroke-linecap:round')
	axe.set('profondeur',str(profondeur))


	
	# Femelle ***************************************
	#On recupere les deux angles qui correspondent aux tangentes par rapport a la vue
	thetaCoupure1,thetaCoupure2=getAnglesCoupure(baseLocale)
	
	#On construit les arcs de cercles projete
	centre1=v3D(-largeur/2,0,0,baseLocale) #Vecteur OC1, O=centre liaison
	centre2=v3D(largeur/2,0,0,baseLocale) #Vecteur OC1, O=centre liaison
	listeArcs1=getListePoints2DCercle(baseLocale,centre1,rayon,0,math.pi*2,thetaCoupure1,thetaCoupure2)
	listeArcs2=getListePoints2DCercle(baseLocale,centre2,rayon,0,math.pi*2,thetaCoupure1,thetaCoupure2)
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
					(0,	0,	3.*rayon)
				],False,baseLocale)
	barreFemelle.set('d',chemin)
	barreFemelle.set('stroke',couleur_femelle)
	barreFemelle.set('stroke-width',str(epaisseur_femelle))
	barreFemelle.set('style','stroke-linecap:round')
	barreFemelle.set('profondeur',str(profondeur*1e10))
	


	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        
        listeObjets=[axe,demiCylindre1,demiCylindre2,barreFemelle]
        
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)
        
        
	# Transformations ***************************************
	liaison.set("transform","translate("+str(x0+x*Vx.x+y*Vy.x+z*Vz.x)+","+str(y0+x*Vx.y+y*Vy.y+z*Vz.y)+")")
	
