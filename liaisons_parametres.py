# -- coding: utf-8 --

# ============== LIAISON HÉLICOIDALE ========================

# Parametres généraux
longueur_helicoidale_femelle=30.
diametre_helicoidale_femelle=15.

# Hélicoidale 2D coté
h2Dc_diametre=diametre_helicoidale_femelle	#Hauteur du rectangle
h2Dc_longueur=longueur_helicoidale_femelle	#Largeur du rectangle
h2Dc_nbVagues=4					#Nombre de vaguelette marquant le filet
h2Dc_hauteurVagues=h2Dc_diametre/6.		#Demi-hauteur des vaguelettes
h2Dc_nbPointsVagues=100				#Nombre de point pour tracer les vaguelettes
h2Dc_longueur_axe=2.*h2Dc_longueur		#Longueur de l'axe mâle.
h2Dc_longueur_tige=h2Dc_diametre/2.		#Longueur de la tige qui part de la pièce femelle

#Hélicoidale 2D face
h2Df_diametre_femelle=diametre_helicoidale_femelle	#Diamètre du cercle femelle
h2Df_longueur_tige=h2Df_diametre_femelle/2.		#Longueur de la petite tige qui part de la pièce femelle ou mâle
h2Df_diametre_male=h2Df_diametre_femelle*0.7		#Diamètre de la portion de cercle qui marque l'hélice

#Hélicoidale 3D
h3D_diametre=diametre_helicoidale_femelle	#Diamètre du cylindre
h3D_longueur=h2Dc_longueur			#Longueur du cylindre
