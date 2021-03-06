# -- coding: utf-8 --
import math

# ============== LIAISON PIVOT ========================

# Parametres généraux
diametre_pivot = 10.						# Diamètre de la pièce femelle
longueur_pivot = 20.						# Longueur de la pièce femelle
longueur_arrets_pivot = diametre_pivot				# Longueur des arrêts (barres) de la pivot
ecart_arrets_pivot = 0.5 * diametre_pivot			# Ecart entre la pièce femelle et les arrêts
longueur_male_pivot = longueur_pivot + 4*ecart_arrets_pivot	# Longueur de la tige mâle

# Pivot 2D coté
p2Dc_diametre = diametre_pivot			# Diamètre de la pièce femelle
p2Dc_longueur = longueur_pivot			# Longueur de la pièce femelle
p2Dc_longueur_arrets = longueur_arrets_pivot	# Longueur des arrêts de la pivot
p2Dc_ecarts_arrets = ecart_arrets_pivot		# Ecart entre la pièce femelle et les arrêts
p2Dc_longueur_male = longueur_male_pivot	# Longueur de la tige male
p2Dc_longueur_tige_femelle = p2Dc_diametre	# Longueur de la tige femelle

# Pivot 2D face
p2Df_diametre = diametre_pivot		# Diamètre de la pièce femelle
p2Df_longueur_tige = p2Dc_diametre/2.	# Longueur de la tige (male ou femelle)

#Pivot 3D
p3D_diametre = diametre_pivot			# Diamètre de la pièce femelle
p3D_longueur = longueur_pivot			# Longueur de la pièce femelle
p3D_longueur_arrets = longueur_arrets_pivot	# Longueur des arrêts de la pivot
p3D_ecarts_arrets = ecart_arrets_pivot		# Ecart entre la pièce femelle et les arrêts
p3D_longueur_male = longueur_male_pivot	# Longueur de la tige male
p3D_longueur_tige_femelle = p3D_diametre	# Longueur de la tige femelle


# ============== LIAISON PIVOT-GLISSANT ========================

# Parametres généraux
diametre_pivot_glissant = diametre_pivot						# Diamètre de la pièce femelle
longueur_pivot_glissant = longueur_pivot						# Longueur de la pièce femelle
longueur_male_pivot_glissant = longueur_pivot_glissant + 2 * diametre_pivot_glissant	#  Longueur de la tige mâle

# Pivot-glissant 2D coté
pg2Dc_diametre = diametre_pivot_glissant		# Diamètre de la pièce femelle
pg2Dc_longueur = longueur_pivot_glissant		# Longueur de la pièce femelle
pg2Dc_longueur_male = longueur_male_pivot_glissant	# Longueur de la tige mâle
pg2Dc_longueur_tige_femelle = diametre_pivot_glissant	# Longueur de la tige femelle

# Pivot-glissant 2D face
pg2Df_diametre = diametre_pivot_glissant	# Diamètre de la pièce femelle
pg2Df_longueur_tige = pg2Df_diametre / 2.	# Longueur de la tige (male ou femelle)

#Pivot 3D
pg3D_diametre = diametre_pivot_glissant			# Diamètre de la pièce femelle
pg3D_longueur = longueur_pivot_glissant			# Longueur de la pièce femelle
pg3D_longueur_male = longueur_male_pivot_glissant	# Longueur de la tige mâle
pg3D_longueur_tige_femelle = pg3D_diametre		# Longueur de la tige femelle

# ============== LIAISON GLISSIÈRE ========================
# Parametres généraux
largeur_glissiere = 1.25 * diametre_pivot		# Largeur du rectangle
hauteur_glissiere = 0.7 * largeur_glissiere		# Hauteur du rectangle
longueur_glissiere = longueur_pivot			# Longueur de la liaison
longueur_male_glissiere = 2 * longueur_glissiere	# Longueur de la pièce mâle
longueur_tige_femelle = hauteur_glissiere*1.214285714	# Longueur de la tige femelle qui part du rectangle

# Glissiere 2D coté
g2Dc_hauteur = hauteur_glissiere			# Hauteur du rectangle
g2Dc_longueur = longueur_glissiere			# Longueur du rectangle
g2Dc_longueur_male = longueur_male_glissiere		# Longueur de la pièce mâle
g2Dc_longueur_tige_femelle = longueur_tige_femelle	# Longueur de la tige femelle qui part du rectangle

# Glissière 2D face
g2Df_hauteur = hauteur_glissiere			# Hauteur du rectangle
g2Df_largeur = largeur_glissiere			# Largeur du rectangle
g2Df_longueur_tige_femelle = longueur_tige_femelle	# Longueur de la tige femelle qui part du rectangle
g2Df_longueur_tige_male = largeur_glissiere/1.25	# Longueur de la tige qui par de la pièce mâle

# Glissière 3D
g3D_longueur = longueur_glissiere			# Longueur du rectangle
g3D_largeur = largeur_glissiere				# Largeur du rectangle
g3D_hauteur = hauteur_glissiere				# Hauteur du rectangle
g3D_longueur_male = longueur_male_glissiere 		# Longueur de la pièce mâle
g3D_longueur_tige_femelle =  longueur_tige_femelle	# Longueur de la tige de la pièce femelle


# ============== LIAISON PLANE ========================
# Parametres généraux
largeur_plane = 1.5 * diametre_pivot		# Largeur des "plans" de la liaison
ecartement_plane = largeur_plane / 6.		# Espace entre les "plans" de la liaison
longueur_tiges_plane = largeur_plane *7/12	# Longueur des tiges qui repartent de chaque plan

# Plane 2D coté
pl2Dc_largeur = largeur_plane		# Largeur des "plans" de la liaison
pl2Dc_ecartement = ecartement_plane	# Espace entre les "plans" de la liaison
pl2Dc_tiges = longueur_tiges_plane	# Longueur des tiges qui repartent de chaque plan

# Plane 2D dessus
pl2Dd_largeur = largeur_plane			# Dimension moyenne des deux carrés vus du dessus
pl2Dd_ecartement = 0.5 * ecartement_plane	# Espace qui sépare les deux carrés vus du dessus
pl2Dd_tiges = pl2Dd_largeur / 2.		# Longueur des tiges qui partent des liaison, depuis le carré moyen

# Plane 3D
pl3D_largeur = largeur_plane		# Largeur des "plans" de la liaison
pl3D_ecartement = ecartement_plane	# Espace entre les "plans" de la liaison
pl3D_tiges = 1.5 * longueur_tiges_plane	# Longueur des tiges qui repartent de chaque plan

# ============== LIAISON SPHÉRIQUE ========================
# Parametres généraux
diametre_spherique = diametre_pivot					# Diamètre de la boule intérieure
angle_ouverture_spherique = 90.						# Angle ouverture de la calotte femelle
ecart_spherique = diametre_spherique / 5.				# Interstice entre la sphère et la calotte femelle. Prend en compte l'épaisseur des traits
rayon_tiges_spherique = 1.5 * diametre_spherique			# Distance entre le centre de la sphère et le bout des tiges qui sortent de chaque pièce

# Sphérique 2D
s2D_diametre = diametre_spherique			# Diamètre de la boule intérieure
s2D_angle_ouverture = angle_ouverture_spherique		# Angle ouverture de la calotte femelle
s2D_ecart = ecart_spherique				# Interstice entre la sphère et la calotte femelle. Prend en compte l'épaisseur des traits
s2D_rayon_tiges_male = rayon_tiges_spherique * 0.75	# Distance entre le centre de la sphère et le bout des tiges qui sort de la sphère
s2D_rayon_tiges_femelle = rayon_tiges_spherique		# Distance entre le centre de la sphère et le bout des tiges qui sort de la calotte femelle

# Sphérique 3D
s3D_diametre = diametre_spherique			# Diamètre de la boule intérieure
s3D_angle_ouverture = 140.				# Angle ouverture de la calotte femelle
s3D_ecart = ecart_spherique *0.5			# Interstice entre la sphère et la calotte femelle. Prend en compte l'épaisseur des traits
s3D_rayon_tiges = rayon_tiges_spherique * 0.75		# Distance entre le centre de la sphère et le bout des tiges qui sortent de chaque pièce


# ============== LIAISON HÉLICOIDALE ========================

# Parametres généraux
longueur_helicoidale_femelle = longueur_pivot					# Longueur du cylindre femelle
diametre_helicoidale_femelle = diametre_pivot					# Diamètre du cylindre femelle
longueur_helicoidale_male = longueur_pivot + 2.*diametre_helicoidale_femelle	# Longueur de la pièce mâle
longueur_helicoidale_tige_femelle = diametre_helicoidale_femelle / 2.		# Longueur de la tige femelle

# Hélicoidale 2D coté
h2Dc_diametre = diametre_helicoidale_femelle		# Hauteur du rectangle
h2Dc_longueur = longueur_helicoidale_femelle		# Largeur du rectangle
h2Dc_nbVagues = 4.					# Nombre de vaguelette marquant le filet
h2Dc_hauteurVagues = h2Dc_diametre / 5.			# Demi-hauteur des vaguelettes
h2Dc_nbPointsVagues = 100.				# Nombre de point pour tracer les vaguelettes
h2Dc_longueur_axe = longueur_helicoidale_male		# Longueur de l'axe mâle.
h2Dc_longueur_tige = longueur_helicoidale_tige_femelle	# Longueur de la tige qui part de la pièce femelle

#Hélicoidale 2D face
h2Df_diametre_femelle = diametre_helicoidale_femelle	# Diamètre du cercle femelle
h2Df_longueur_tige = longueur_helicoidale_tige_femelle	# Longueur de la petite tige qui part de la pièce femelle ou mâle
h2Df_diametre_male = h2Df_diametre_femelle * 0.7	# Diamètre de la portion de cercle qui marque l'hélice

#Hélicoidale 3D
h3D_diametre = diametre_helicoidale_femelle				# Diamètre du cylindre
h3D_longueur = longueur_helicoidale_femelle				# Longueur du cylindre
h3D_longueur_tige_femelle = longueur_helicoidale_tige_femelle * 2.	# Longueur de la tige qui repart de la pièce femelle
h3D_nombre_helices = 4.							# Nombre d'hélice autour du cylindre
h2D_longueur_axe = longueur_helicoidale_male				# Longueur de la tige qui part de la pièce femelle


# ============== LIAISON SPHERE PLAN ========================

# Parametres généraux
diametre_sphere_plan = diametre_pivot * 0.75			# Diamètre de la sphere
largeur_plan_sphere_plan = diametre_sphere_plan * 2		# Largeur du plan
longueur_tiges_sphere_plan_sphere = diametre_sphere_plan	# Longueurs de la tige qui repart de la sphère
longueur_tiges_sphere_plan_plan = diametre_sphere_plan / 0.75	# Longueurs de la tige qui repart du plan

#Sphère-plan 2D vue de coté
sp2Dc_largeur_plan = largeur_plan_sphere_plan			# Largeur du plan
sp2Dc_diametre_sphere = diametre_sphere_plan			# Diamètre Sphère
sp2Dc_longueur_tige_plan = longueur_tiges_sphere_plan_plan	# Longueur de sous le plan
sp2Dc_longueur_tige_sphere = longueur_tiges_sphere_plan_sphere	# Longueur de la tige qui part de la sphère
sp2DcOLD_largeur_fleche = longueur_tiges_sphere_plan_sphere	# Largeur de la flèche dans l'ancienne norme

#Sphère-plan 2D vue de dessus
sp2Dd_largeur = largeur_plan_sphere_plan * 0.9					# Largeur du plan
sp2Dd_diametre_sphere = diametre_sphere_plan					# Diamètre Sphère
sp2Dd_longueur_tige_plan = sp2Dd_largeur * (1./1.35-0.5)			# Longueur de la tige à coté du plan
sp2Dd_longueur_tige_sphere = sp2Dd_largeur*(1.5/1.35)-sp2Dd_diametre_sphere/2.	# Longueur de la tige qui part de la sphère

#Sphère-plan 3D
sp3D_largeur = largeur_plan_sphere_plan				# Largeur du plan
sp3D_diametre_sphere = diametre_sphere_plan			# Diamètre Sphère
sp3D_longueur_tige_plan = longueur_tiges_sphere_plan_plan	# Longueur de la tige à coté du plan
sp3D_longueur_tige_sphere = longueur_tiges_sphere_plan_sphere	# Longueur de la tige qui part de la sphère

# ============== LIAISON RECTILIGNE ========================

# Parametres généraux
RECTILIGNE_longueur_contact = 0.75 * longueur_pivot							# Longueur de la ligne de contact
RECTILIGNE_hauteur_prisme = diametre_pivot * 0.75							# Hauteur du prisme
RECTILIGNE_longueur_base_prisme = RECTILIGNE_longueur_contact + RECTILIGNE_hauteur_prisme * 0.75	# Longueur du rectangle qui fait la base supérieure du prisme
RECTILIGNE_largeur_base_prisme = RECTILIGNE_hauteur_prisme * 2 / math.sqrt(3)				# Largeur du rectangle qui fait la base supérieure du prisme
RECTILIGNE_largeur_plan = RECTILIGNE_largeur_base_prisme * 2						# Largeur du plan
RECTILIGNE_longueur_plan = RECTILIGNE_longueur_base_prisme  + RECTILIGNE_largeur_base_prisme * 0.75	# Longueur du plan

# Rectiligne 2D vue de coté
r2Dc_longueur_contact = RECTILIGNE_longueur_contact		# Longueur de la ligne de contact
r2Dc_longueur_plan = RECTILIGNE_longueur_plan			# Longueur du plan
r2Dc_hauteur_prisme = RECTILIGNE_hauteur_prisme			# Hauteur du prisme
r2Dc_longueur_base_prisme = RECTILIGNE_longueur_base_prisme	# Longueur de la base du prisme
r2Dc_longueur_tige_plan = RECTILIGNE_hauteur_prisme / 0.75	# Longueur de la tige du plan
r2Dc_longueur_tige_prisme = RECTILIGNE_hauteur_prisme		# Longueur de la tige du prisme

# Rectiligne 2D vue du bout
r2Db_largeur_plan = RECTILIGNE_largeur_plan			# Largeur du plan
r2Db_longueur_tige_plan = RECTILIGNE_hauteur_prisme / 0.74	# Longueur de la tige sous le plan
r2Db_hauteur_prisme = RECTILIGNE_hauteur_prisme			# Hauteur du prisme
r2Db_largeur_prisme = RECTILIGNE_largeur_base_prisme		# Largeur du prisme
r2Db_longueur_tige_prisme = RECTILIGNE_hauteur_prisme		# Longueur de la tige au dessus du prisme

# Rectiligne 3D
r3D_longueur_contact = RECTILIGNE_longueur_contact		# Longueur de la ligne de contact
r3D_longueur_base_prisme = RECTILIGNE_longueur_base_prisme	# Longueur du rectangle qui fait la base supérieure du prisme
r3D_largeur_base_prisme = RECTILIGNE_largeur_base_prisme	# Largeur du rectangle qui fait la base supérieure du prisme
r3D_hauteur_prisme = RECTILIGNE_hauteur_prisme			# Hauteur du prisme
r3D_largeur_plan = RECTILIGNE_largeur_plan			# Largeur du plan
r3D_longueur_plan = RECTILIGNE_longueur_plan			# Longueur du plan
r3D_longueur_tige_prisme = RECTILIGNE_hauteur_prisme		# Longueur de la tige au dessus du prisme
r3D_longueur_tige_plan = RECTILIGNE_hauteur_prisme * 2		# Longueur de la tige sous le plan

# ============== LIAISON SPHÈRE-CYLINDRE ========================

# Parametres généraux
SPHERE_CYLINDRE_longeur = longueur_pivot			# Longueur du cylindre
SPHERE_CYLINDRE_diametre = diametre_pivot 			# Diamètre du cylindre + sphère
SPHERE_CYLINDRE_longueur_tige_sphere = diametre_pivot * 0.5	# Longueur de la tige qui ressort de la sphère
SPHERE_CYLINDRE_longueur_tige_cylindre = diametre_pivot		# Longueur de la tige qui ressort du cylindre

# Sphère-Cylindre 2D vue de coté
SC2Dc_longueur = SPHERE_CYLINDRE_longeur				# Longueur du cylindre
SC2Dc_hauteur = SPHERE_CYLINDRE_diametre * 0.4				# Hauteur de la portion de cylindre projetée
SC2Dc_diametre = SPHERE_CYLINDRE_diametre				# Diamètre du cylindre + sphère
SC2Dc_longueur_tige_cylindre = SPHERE_CYLINDRE_longueur_tige_cylindre	# Longueur de tige sous le cylindre
SC2Dc_longueur_tige_sphere = SPHERE_CYLINDRE_longueur_tige_sphere	# Longueur de tige sur la sphère

# Sphère-Cylindre 2D vue du bout
#SC2Db_largeur_plan = 1.5 * SPHERE_CYLINDRE_diametre			# Largeur du plan
SC2Db_angle_ouverture = 140.						# Angle d'ouverture du cylindre (en degres)
SC2Db_diametre = SPHERE_CYLINDRE_diametre				# Diamètre du cylindre + sphère
SC2Db_intervalle_spheres = 0.1 * SPHERE_CYLINDRE_diametre		# Intervalle
SC2Db_longueur_tige_cylindre = SPHERE_CYLINDRE_longueur_tige_cylindre	# Longueur de tige sous le cylindre
SC2Db_longueur_tige_sphere = SPHERE_CYLINDRE_longueur_tige_sphere	# Longueur de tige sur la sphère

# Sphère-Cylindre 3D
SC3D_longueur = SPHERE_CYLINDRE_longeur					# Longueur du cylindre
SC3D_diametre = SPHERE_CYLINDRE_diametre				# Diamètre du cylindre + sphère
SC3D_longueur_tige_cylindre = SPHERE_CYLINDRE_longueur_tige_cylindre	# Longueur de tige sous le cylindre
SC3D_longueur_tige_sphere = SPHERE_CYLINDRE_longueur_tige_sphere * 1.5	# Longueur de tige sur la sphère
SC3D_angle_ouverture = 140.						# Angle d'ouverture du cylindre (en degres)

# ============== MASSE (Référentiel) ========================

# Parametres généraux
REFERENTIEL_largeur = 0.5 * longueur_pivot			# Longueur du trait principal (sur lequel sont raccrochées les hachures)
REFERENTIEL_longueur_tige = REFERENTIEL_largeur * 0.75		# Longueur de la tige qui sort du trait principal
REFERENTIEL_longueur_hachures = 0.5 * REFERENTIEL_largeur	# Longueur des hachures projetées sur l'axe de la tige
REFERENTIEL_inclinaison = 20					# Inclinaison des hachures par rapport l'axe de la tige (en degrés)
REFERENTIEL_nombre_hachures = 4					# Nombre de hachures

# Référentiel 2D
REF2D_largeur = REFERENTIEL_largeur			# Longueur du trait principal (sur lequel sont raccrochées les hachures)
REF2D_longueur_tige = REFERENTIEL_longueur_tige		# Longueur de la tige qui sort du trait principal
REF2D_longueur_hachures = REFERENTIEL_longueur_hachures	# Longueur des hachures projetées sur l'axe de la tige
REF2D_inclinaison = REFERENTIEL_inclinaison		# Inclinaison des hachures par rapport l'axe de la tige (en degrés)
REF2D_nombre_hachures = REFERENTIEL_nombre_hachures	# Nombre de hachures

# Référentiel 3D
REF3D_largeur = REFERENTIEL_largeur					# Longueur du trait principal (sur lequel sont raccrochées les hachures)
REF3D_longueur_tige = REFERENTIEL_longueur_tige				# Longueur de la tige qui sort du trait principal
REF3D_longueur_hachures_plat = REFERENTIEL_longueur_hachures		# Longueur des hachures projetées sur l'axe de la tige, en représentation à plat
REF3D_longueur_hachures_3D = REFERENTIEL_longueur_hachures * 1.2	# Longueur des hachures projetées sur l'axe de la tige, en représentation 3D
REF3D_inclinaison_plat = REFERENTIEL_inclinaison			# Inclinaison des hachures par rapport l'axe de la tige (en degrés), en représentation plane
REF3D_inclinaison_3D = REFERENTIEL_inclinaison				# Inclinaison des hachures par rapport l'axe de la tige (en degrés), en représentation 3D
REF3D_nombre_hachures_plat = REFERENTIEL_nombre_hachures 		# Nombre de hachures pour la représentation à plat
REF3D_nombre_hachures_3D = REFERENTIEL_nombre_hachures			# Nombre de hachures par coté


