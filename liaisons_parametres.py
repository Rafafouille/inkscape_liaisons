# -- coding: utf-8 --

# ============== LIAISON HÉLICOIDALE ========================

# Parametres généraux
longueur_helicoidale_femelle = 30.
diametre_helicoidale_femelle = 15.

# Hélicoidale 2D coté
h2Dc_diametre = diametre_helicoidale_femelle	# Hauteur du rectangle
h2Dc_longueur = longueur_helicoidale_femelle	# Largeur du rectangle
h2Dc_nbVagues = 4				# Nombre de vaguelette marquant le filet
h2Dc_hauteurVagues = h2Dc_diametre / 4.		# Demi-hauteur des vaguelettes
h2Dc_nbPointsVagues = 100			# Nombre de point pour tracer les vaguelettes
h2Dc_longueur_axe = 2. * h2Dc_longueur		# Longueur de l'axe mâle.
h2Dc_longueur_tige = h2Dc_diametre / 2.		# Longueur de la tige qui part de la pièce femelle

#Hélicoidale 2D face
h2Df_diametre_femelle = diametre_helicoidale_femelle	#Diamètre du cercle femelle
h2Df_longueur_tige = h2Df_diametre_femelle / 2.		#Longueur de la petite tige qui part de la pièce femelle ou mâle
h2Df_diametre_male = h2Df_diametre_femelle * 0.7	#Diamètre de la portion de cercle qui marque l'hélice

#Hélicoidale 3D
h3D_diametre = diametre_helicoidale_femelle	#Diamètre du cylindre
h3D_longueur = h2Dc_longueur			#Longueur du cylindre
h3D_longueur_tige_femelle = h3D_diametre / 2.	#Longueur de la tige qui repart de la pièce femelle
h3D_nombre_helices = 4

# ============== LIAISON SPHERE PLAN ========================

# Parametres généraux
largeur_sphere_plan_plan = 30		# Largeur du plan
diametre_sphere_plan_sphere = 20	# Diamètre de la sphere

#Sphère-plan 2D vue de coté
sp2Dc_largeur_plan = largeur_sphere_plan_plan		# Largeur du plan
sp2Dc_diametre_sphere = diametre_sphere_plan_sphere	# Diamètre Sphère
sp2Dc_longueur_axe_plan = sp2Dc_largeur_plan		# Longueur de sous le plan
sp2Dc_longueur_tige_sphere = sp2Dc_diametre_sphere / 2.	# Longueur de la tige qui part de la sphère
sp2DcOLD_largeur_fleche = sp2Dc_diametre_sphere		# Largeur de la flèche dans l'ancienne norme

#Sphère-plan 2D vue de dessus
sp2Dd_largeur = largeur_sphere_plan_plan		# Largeur du plan
sp2Dd_diametre_sphere = diametre_sphere_plan_sphere	# Diamètre Sphère
sp2Dd_longueur_tige_plan = sp2Dd_largeur / 2.	# Longueur de la tige à coté du plan
sp2Dd_longueur_tige_sphere = sp2Dd_diametre_sphere	# Longueur de la tige qui part de la sphère

#Sphère-plan 3D
sp3D_largeur = largeur_sphere_plan_plan			# Largeur du plan
sp3D_diametre_sphere = diametre_sphere_plan_sphere	# Diamètre Sphère
sp3D_longueur_tige_plan = sp3D_largeur * 0.75		# Longueur de la tige à coté du plan
sp3D_longueur_tige_sphere = sp3D_diametre_sphere	# Longueur de la tige qui part de la sphère

# ============== LIAISON RECTILIGNE ========================

# Parametres généraux
RECTILIGNE_longueur_contact = 30					# Longueur de la ligne de contact
RECTILIGNE_longueur_base_prisme = RECTILIGNE_longueur_contact + 10	# Longueur du rectangle qui fait la base supérieure du prisme
RECTILIGNE_largeur_base_prisme = 20					# Largeur du rectangle qui fait la base supérieure du prisme
RECTILIGNE_hauteur_prisme = 15						# Hauteur du prisme
RECTILIGNE_largeur_plan = RECTILIGNE_largeur_base_prisme + 20		# Largeur du plan
RECTILIGNE_longueur_plan = RECTILIGNE_longueur_contact + 20		# Longueur du plan

# Rectiligne 2D vue de coté
r2Dc_longueur_contact = RECTILIGNE_longueur_contact		# Longueur de la ligne de contact
r2Dc_longueur_plan = RECTILIGNE_longueur_plan			# Longueur du plan
r2Dc_hauteur_prisme = RECTILIGNE_hauteur_prisme			# Hauteur du prisme
r2Dc_longueur_base_prisme = RECTILIGNE_longueur_base_prisme	# Longueur de la base du prisme
r2Dc_longueur_tige_plan = 20					# Longueur de la tige du plan
r2Dc_longueur_tige_prisme = 20					# Longueur de la tige du prisme

# Rectiligne 2D vue du bout
r2Db_largeur_plan = RECTILIGNE_largeur_plan		# Largeur du plan
r2Db_longueur_tige_plan = 20				# Longueur de la tige sous le plan
r2Db_hauteur_prisme = RECTILIGNE_hauteur_prisme		# Hauteur du prisme
r2Db_largeur_prisme = RECTILIGNE_largeur_base_prisme	# Largeur du prisme
r2Db_longueur_tige_prisme = 20				# Longueur de la tige au dessus du prisme

# Rectiligne 3D
r3D_longueur_contact = RECTILIGNE_longueur_contact		# Longueur de la ligne de contact
r3D_longueur_base_prisme = RECTILIGNE_longueur_base_prisme	# Longueur du rectangle qui fait la base supérieure du prisme
r3D_largeur_base_prisme = RECTILIGNE_largeur_base_prisme		# Largeur du rectangle qui fait la base supérieure du prisme
r3D_hauteur_prisme = RECTILIGNE_hauteur_prisme			# Hauteur du prisme
r3D_largeur_plan = RECTILIGNE_largeur_plan			# Largeur du plan
r3D_longueur_plan = RECTILIGNE_longueur_plan			# Longueur du plan
r3D_longueur_tige_prisme = 20					# Longueur de la tige au dessus du prisme
r3D_longueur_tige_plan = 20					# Longueur de la tige sous le plan

