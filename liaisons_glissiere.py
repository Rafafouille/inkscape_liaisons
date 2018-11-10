import math
import inkex
from liaisons_fonctions_utiles import *


def dessin_Glissiere_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_glissiere_2D_cote_x
	y=options.liaison_glissiere_2D_cote_y
	#Orientation **************************************
	rotation=options.liaison_glissiere_2D_cote_orientation #Angle par defaut (sens trigo)
	if(options.liaison_glissiere_2D_cote_axe=="x"):
		rotation=0
	elif(options.liaison_glissiere_2D_cote_axe=="y"):
		rotation=90.
	elif(options.liaison_glissiere_2D_cote_axe=="-x"):
		rotation=180.
	elif(options.liaison_glissiere_2D_cote_axe=="-y"):
		rotation=-90.
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	old_liaisons=options.opt_gene_gene_old
	largeur=30.
	hauteur=15.
	longueur_axe=2.*largeur
	longueur_tige=hauteur/2.
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle=inkex.etree.SubElement(liaison,'g')

	# Male ***************************************
	#Ligne male
	ligneM=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-longueur_axe/2.,0),
					(longueur_axe/2.,0)]
				,False,base2D)
	ligneM.set('d',chemin)
	ligneM.set('stroke',couleur_male)
	ligneM.set('stroke-width',str(epaisseur_male))
	male.append(ligneM)
	
	
	# Femelle ***************************************

	#Rectangle
	rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-largeur*echelle/2) )
	rectangle.set('y',str(-hauteur*echelle/2) )
	rectangle.set('width',str(largeur*echelle))
	rectangle.set('height',str(hauteur*echelle))
	rectangle.set('style','fill:#FFFFFF')
	rectangle.set('stroke',couleur_femelle)
	rectangle.set('stroke-width',str(epaisseur_femelle))
	femelle.append(rectangle)
	
	#Ligne femelle
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	-hauteur/2.),
					(0	,	-hauteur/2.-longueur_tige)	]
				,False,base2D)
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle))
	femelle.append(ligneF)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(-rotation)+")")
	femelle.set("transform","rotate("+str(-rotation)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
	

def dessin_Glissiere_2D_face(options,contexte):
	#Position *****************************************
	x0=options.x0
	y0=options.y0
	x=options.liaison_glissiere_2D_face_x
	y=options.liaison_glissiere_2D_face_y
	#Orientation **************************************
	rotation=options.liaison_glissiere_2D_face_orientation #Angle par defaut (sens trigo)
	if(options.liaison_glissiere_2D_face_axe=="x"):
		rotation=0
	elif(options.liaison_glissiere_2D_face_axe=="y"):
		rotation=90.
	elif(options.liaison_glissiere_2D_face_axe=="-x"):
		rotation=180.
	elif(options.liaison_glissiere_2D_face_axe=="-y"):
		rotation=-90.
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Base *********************
	profondeur=25.
	hauteur=15.
	longueur_tige=hauteur/2.
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1

	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte,'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle=inkex.etree.SubElement(liaison,'g')

	# Femelle ***************************************	
	#rectangle
	rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-profondeur*echelle/2) )
	rectangle.set('y',str(-hauteur*echelle/2) )
	rectangle.set('width',str(profondeur*echelle))
	rectangle.set('height',str(hauteur*echelle))
	rectangle.set('style','fill:none')
	rectangle.set('stroke',couleur_femelle)
	rectangle.set('stroke-width',str(epaisseur_femelle))
	femelle.append(rectangle)
	#cercle
	tige=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	hauteur/2.),
				(0,	hauteur/2.+longueur_tige)	]
				,False,base2D)
	tige.set('d',chemin)
	tige.set('stroke',couleur_femelle)
	tige.set('stroke-width',str(epaisseur_femelle))
	femelle.append(tige)
	
	# Male ***************************************
	#croisillon1
	croix1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-profondeur/2.+epaisseur_femelle/2	,	-hauteur/2.+epaisseur_femelle/2),
				(profondeur/2.-epaisseur_femelle/2,	hauteur/2.-epaisseur_femelle/2)	]
				,False,base2D)
	croix1.set('d',chemin)
	croix1.set('stroke',couleur_male)
	croix1.set('stroke-width',str(epaisseur_male))
	male.append(croix1)
	#croisillon2
	croix2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(profondeur/2.-epaisseur_femelle/2	,	-hauteur/2.+epaisseur_femelle/2),
				(-profondeur/2.+epaisseur_femelle/2,	hauteur/2.-epaisseur_femelle/2)	]
				,False,base2D)
	croix2.set('d',chemin)
	croix2.set('stroke',couleur_male)
	croix2.set('stroke-width',str(epaisseur_male))
	male.append(croix2)
	#Trait
	trait=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	0),
				((-hauteur/2.-longueur_tige)*math.sin(-rotation/180*math.pi),	-(hauteur/2.+longueur_tige)*math.cos(-rotation/180*math.pi))	]
				,False,base2D)
	trait.set('d',chemin)
	trait.set('stroke',couleur_male)
	trait.set('stroke-width',str(epaisseur_male))
	liaison.append(trait)
		
	# Transformations ***************************************
	male.set("transform","rotate("+str(-rotation)+")")
	femelle.set("transform","rotate("+str(-rotation)+")")
	liaison.set("transform","translate("+str(x0+x)+","+str(y0+y)+")")
	






#===============================================================
def dessin_Glissiere_3D(options,contexte):
	#Origine 2D
	x0=options.x0
	y0=options.y0
	#Base Axonometrique
	Vx,Vy,Vz=getVecteursAxonometriques()
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
	epaisseur_femelle=options.opt_gene_lignes2
	epaisseur_male=options.opt_gene_lignes1
	#Repere local de la liaison
	if(options.liaison_pivot_glissant_3D_type_orientation=="\"liaison_pivot_glissant_3D_type_orientation_quelconque\""):
		V=v3D(options.liaison_pivot_glissant_3D_type_orientation_quelconque_x,options.liaison_pivot_glissant_3D_type_orientation_quelconque_y,options.liaison_pivot_glissant_3D_type_orientation_quelconque_z,base)
		Vx1,Vy1,Vz1=getBaseFromVecteur(V)
	else:	#Si vecteur standart
		if(options.liaison_pivot_glissant_3D_axe=="x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx)
		elif(options.liaison_pivot_glissant_3D_axe=="y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy)
		else:#z
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz)
	#A FAIRE : Ajouter le cas d'un vecteur directeur quelconque...
	baseLocale=(Vx1,Vy1,Vz1)

	
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
	demiCylindre1=inkex.etree.Element(inkex.addNS('path','svg'))
	demiCylindre1.set('d',chemin)
	demiCylindre1.set('stroke',couleur_femelle)
	demiCylindre1.set('stroke-width',str(epaisseur_femelle))
	demiCylindre1.set('style','stroke-linecap:round')
	demiCylindre1.set('profondeur',str(profondeurDemiCylindre1))
	demiCylindre1.set('style','fill:white')
	
	chemin,profondeurDemiCylindre2=points3D_to_svgd(listeDemiCylindre2,True)
	demiCylindre2=inkex.etree.Element(inkex.addNS('path','svg'))
	demiCylindre2.set('d',chemin)
	demiCylindre2.set('stroke',couleur_femelle)
	demiCylindre2.set('stroke-width',str(epaisseur_femelle))
	demiCylindre2.set('style','stroke-linecap:round')
	demiCylindre2.set('profondeur',str(profondeurDemiCylindre2))
	demiCylindre2.set('style','fill:white')
	


	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        #On choisit dans quel ordre on ajoute les elements (arriere plan / avant plan)
     	if(profondeurDemiCylindre1<profondeurDemiCylindre2):
        	femelle1=inkex.etree.SubElement(liaison,'g')
		male=inkex.etree.SubElement(liaison,'g')
		femelle2=inkex.etree.SubElement(liaison,'g')
	else:
		femelle2=inkex.etree.SubElement(liaison,'g')
		male=inkex.etree.SubElement(liaison,'g')
        	femelle1=inkex.etree.SubElement(liaison,'g')
		
	#REmplissage des groupes
	male.append(axe)
	
	femelle1.append(demiCylindre1)

	femelle2.append(demiCylindre2)
	
	"""femelle_devant.append(pathDevant)
	femelle_devant.set('profondeur',str(profondeur_devant))"""
	
	
	#Debug *************
	liaison.set("listePoints",str(baseLocale[0].z))
	
	# Transformations ***************************************
	liaison.set("transform","translate("+str(x0+x*Vx.x+y*Vy.x+z*Vz.x)+","+str(y0+x*Vx.y+y*Vy.y+z*Vz.y)+")")
	
