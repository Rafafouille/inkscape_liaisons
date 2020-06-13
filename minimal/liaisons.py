# -- coding: utf-8 --
#!/usr/bin/env python

import sys
import inkex
import math

# =====================================================
# =====================================================
# ===== PARAMETRES GEOMETRIQUES =======================
# =====================================================
# =====================================================

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
longueur_male_glissiere = 1.5 * longueur_glissiere	# Longueur de la pièce mâle
longueur_tige_femelle = hauteur_glissiere / 2.		# Longueur de la tige femelle qui part du rectangle

# Glissiere 2D coté
g2Dc_hauteur = hauteur_glissiere			# Hauteur du rectangle
g2Dc_longueur = longueur_glissiere			# Longueur du rectangle
g2Dc_longueur_male = longueur_male_glissiere		# Longueur de la pièce mâle
g2Dc_longueur_tige_femelle = longueur_tige_femelle	# Longueur de la tige femelle qui part du rectangle

# Glissière 2D face
g2Df_hauteur = hauteur_glissiere			# Hauteur du rectangle
g2Df_largeur = largeur_glissiere			# Largeur du rectangle
g2Df_longueur_tige_femelle = longueur_tige_femelle	# Longueur de la tige femelle qui part du rectangle
g2Df_longueur_tige_male = largeur_glissiere		# Longueur de la tige qui par de la pièce mâle

# Glissière 3D
g3D_longueur = longueur_glissiere			# Longueur du rectangle
g3D_largeur = largeur_glissiere				# Largeur du rectangle
g3D_hauteur = hauteur_glissiere				# Hauteur du rectangle
g3D_longueur_male = longueur_male_glissiere * 4./3.	# Longueur de la pièce mâle
g3D_longueur_tige_femelle =  longueur_tige_femelle * 2	# Longueur de la tige de la pièce femelle


# ============== LIAISON PLANE ========================
# Parametres généraux
largeur_plane = 1.5 * diametre_pivot		# Largeur des "plans" de la liaison
ecartement_plane = largeur_plane / 6.		# Espace entre les "plans" de la liaison
longueur_tiges_plane = largeur_plane / 2.	# Longueur des tiges qui repartent de chaque plan

# Plane 2D coté
pl2Dc_largeur = largeur_plane		# Largeur des "plans" de la liaison
pl2Dc_ecartement = ecartement_plane	# Espace entre les "plans" de la liaison
pl2Dc_tiges = longueur_tiges_plane	# Longueur des tiges qui repartent de chaque plan

# Plane 2D dessus
pl2Dd_largeur = largeur_plane			# Dimension moyenne des deux carrés vus du dessus
pl2Dd_ecartement = 0.5 * ecartement_plane	# Espace qui sépare les deux carrés vus du dessus
pl2Dd_tiges = longueur_tiges_plane		# Longueur des tiges qui partent des liaison, depuis le carré moyen

# Plane 3D
pl3D_largeur = largeur_plane		# Largeur des "plans" de la liaison
pl3D_ecartement = ecartement_plane	# Espace entre les "plans" de la liaison
pl3D_tiges = 1.5 * longueur_tiges_plane	# Longueur des tiges qui repartent de chaque plan

# ============== LIAISON SPHÉRIQUE ========================
# Parametres généraux
diametre_spherique = diametre_pivot				# Diamètre de la boule intérieure
angle_ouverture_spherique = 90.						# Angle ouverture de la calotte femelle
ecart_spherique = diametre_spherique / 5.				# Interstice entre la sphère et la calotte femelle. Prend en compte l'épaisseur des traits
rayon_tiges_spherique = 1.5 * diametre_spherique + ecart_spherique	# Distance entre le centre de la sphère et le bout des tiges qui sortent de chaque pièce

# Sphérique 2D coté
s2D_diametre = diametre_spherique			# Diamètre de la boule intérieure
s2D_angle_ouverture = angle_ouverture_spherique		# Angle ouverture de la calotte femelle
s2D_ecart = ecart_spherique				# Interstice entre la sphère et la calotte femelle. Prend en compte l'épaisseur des traits
s2D_rayon_tiges = rayon_tiges_spherique			# Distance entre le centre de la sphère et le bout des tiges qui sortent de chaque pièce

# Sphérique 3D
s3D_diametre = diametre_spherique			# Diamètre de la boule intérieure
s3D_angle_ouverture = 120				# Angle ouverture de la calotte femelle
s3D_ecart = ecart_spherique * 0.05			# Interstice entre la sphère et la calotte femelle. Prend en compte l'épaisseur des traits
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
h3D_diametre = diametre_helicoidale_femelle			# Diamètre du cylindre
h3D_longueur = longueur_helicoidale_femelle					# Longueur du cylindre
h3D_longueur_tige_femelle = longueur_helicoidale_tige_femelle	# Longueur de la tige qui repart de la pièce femelle
h3D_nombre_helices = 4.						# Nombre d'hélice autour du cylindre
h2D_longueur_axe = longueur_helicoidale_male			# Longueur de la tige qui part de la pièce femelle


# ============== LIAISON SPHERE PLAN ========================

# Parametres généraux
largeur_plan_sphere_plan = longueur_pivot * 0.75		# Largeur du plan
diametre_sphere_plan = largeur_plan_sphere_plan * 0.75		# Diamètre de la sphere
longueur_tiges_sphere_plan = diametre_sphere_plan		# Longueurs des tiges qui repartent de la liaison

#Sphère-plan 2D vue de coté
sp2Dc_largeur_plan = largeur_plan_sphere_plan			# Largeur du plan
sp2Dc_diametre_sphere = diametre_sphere_plan			# Diamètre Sphère
sp2Dc_longueur_tige_plan = longueur_tiges_sphere_plan		# Longueur de sous le plan
sp2Dc_longueur_tige_sphere = longueur_tiges_sphere_plan/2.	# Longueur de la tige qui part de la sphère
sp2DcOLD_largeur_fleche = longueur_tiges_sphere_plan		# Largeur de la flèche dans l'ancienne norme

#Sphère-plan 2D vue de dessus
sp2Dd_largeur = largeur_plan_sphere_plan			# Largeur du plan
sp2Dd_diametre_sphere = diametre_sphere_plan			# Diamètre Sphère
sp2Dd_longueur_tige_plan = longueur_tiges_sphere_plan / 1.5	# Longueur de la tige à coté du plan
sp2Dd_longueur_tige_sphere = longueur_tiges_sphere_plan		# Longueur de la tige qui part de la sphère

#Sphère-plan 3D
sp3D_largeur = largeur_plan_sphere_plan			# Largeur du plan
sp3D_diametre_sphere = diametre_sphere_plan	# Diamètre Sphère
sp3D_longueur_tige_plan = longueur_tiges_sphere_plan		# Longueur de la tige à coté du plan
sp3D_longueur_tige_sphere = longueur_tiges_sphere_plan	# Longueur de la tige qui part de la sphère

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
r2Dc_longueur_tige_plan = RECTILIGNE_hauteur_prisme		# Longueur de la tige du plan
r2Dc_longueur_tige_prisme = RECTILIGNE_hauteur_prisme		# Longueur de la tige du prisme

# Rectiligne 2D vue du bout
r2Db_largeur_plan = RECTILIGNE_largeur_plan		# Largeur du plan
r2Db_longueur_tige_plan = RECTILIGNE_hauteur_prisme	# Longueur de la tige sous le plan
r2Db_hauteur_prisme = RECTILIGNE_hauteur_prisme		# Hauteur du prisme
r2Db_largeur_prisme = RECTILIGNE_largeur_base_prisme	# Largeur du prisme
r2Db_longueur_tige_prisme = RECTILIGNE_hauteur_prisme	# Longueur de la tige au dessus du prisme

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
SPHERE_CYLINDRE_longueur_tige_sphere = diametre_pivot * 0.75	# Longueur de la tige qui ressort de la sphère
SPHERE_CYLINDRE_longueur_tige_cylindre = diametre_pivot	* 0.75	# Longueur de la tige qui ressort du cylindre

# Sphère-Cylindre 2D vue de coté
SC2Dc_longueur = SPHERE_CYLINDRE_longeur				# Longueur du cylindre
SC2Dc_hauteur = SPHERE_CYLINDRE_diametre * 0.4				# Hauteur de la portion de cylindre projetée
SC2Dc_diametre = SPHERE_CYLINDRE_diametre				# Diamètre du cylindre + sphère
SC2Dc_longueur_tige_cylindre = SPHERE_CYLINDRE_longueur_tige_sphere	# Longueur de tige sous le cylindre
SC2Dc_longueur_tige_sphere = SPHERE_CYLINDRE_longueur_tige_sphere	# Longueur de tige sur la sphère

# Sphère-Cylindre 2D vue du bout
#SC2Db_largeur_plan = 1.5 * SPHERE_CYLINDRE_diametre		# Largeur du plan
SC2Db_angle_ouverture = 140.					# Angle d'ouverture du cylindre (en degres)
SC2Db_diametre = SPHERE_CYLINDRE_diametre			# Diamètre du cylindre + sphère
SC2Db_intervalle_spheres = 0.1 * SPHERE_CYLINDRE_diametre	# Intervalle
SC2Db_longueur_tige_cylindre = SPHERE_CYLINDRE_diametre * 0.75	# Longueur de tige sous le cylindre
SC2Db_longueur_tige_sphere = SPHERE_CYLINDRE_diametre * 0.75	# Longueur de tige sur la sphère

# Sphère-Cylindre 3D
SC3D_longueur = SPHERE_CYLINDRE_longeur				# Longueur du cylindre
SC3D_diametre = SPHERE_CYLINDRE_diametre			# Diamètre du cylindre + sphère
SC3D_longueur_tige_cylindre = SPHERE_CYLINDRE_diametre * 0.75	# Longueur de tige sous le cylindre
SC3D_longueur_tige_sphere = SPHERE_CYLINDRE_diametre * 0.75	# Longueur de tige sur la sphère
SC3D_angle_ouverture = 140.					# Angle d'ouverture du cylindre (en degres)

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





#=================================================
# Fonctions utiles
#=================================================
#def getCouleurFromInt(i):
#	return "#"+("00000000"+hex(int(i))[2:])[-8:]

CPT=1
def debug(txt,n=1):
	#Affiche un message d'erreur txt, après etre passe n fois par cette fonction (sinon, rien)
	#En lien avec la variable globale CPT
	global CPT
	assert n>CPT,"\n"+("*"*15)+"\nDEBUG ("+str(n)+")\n"+("*"*15)+"\n"+str(txt)
	CPT+=1

#Fonction qui calcule la derivee d'une fonction
def deriv(f,x):
	h=1e-3
	return (f(x+h)-f(x-h))/(2*h)




# Objet vecteur en 2D *******************************************
class v2D:
	def __init__(self,_x,_y,_direct=True):
		self.x=_x
		if(_direct):
			self.y=_y
		else:
			self.y=-_y
		
	def __repr__(self):
		return "<x="+str(self.x)+",y="+str(self.y)+">"
		
	def __add__(self,v):
		return v2D(self.x+v.x,self.y+v.y)
	def __radd__(self,v):
		return self+v
	def __iadd__(self,v):
		self.x+=v.x
		self.y+=v.y
		return self

	def __sub__(self,v):
		return v2D(self.x-v.x,self.y-v.y)
	def __rsub__(self,v):
		return v-self
	def __isub__(self,v):
		self.x-=v.x
		self.y-=v.y
		return self
		
	def __mul__(self,l):
		return v2D(self.x*l,self.y*l)
	def __rmul__(self,l):
		return self*l
	def __imul__(self,l):
		self.x*=l
		self.y*=l
		return self
		
	def __div__(self,l):
		return v2D(self.x/float(l),self.y/float(l))
	def __idiv__(self,l):
		self.x/=float(l)
		self.y/=float(l)
		return self
		
	def rotation(self,theta,trigo=False):
		"""Theta en rad"""
		if(trigo):
			theta*=-1
		self.x,self.y=math.cos(theta)*self.x-math.sin(theta)*self.y , math.sin(theta)*self.x+math.cos(theta)*self.y
		
	def prodSca(self,v2):
		"""Prod scalaire entre ce vecteur et un autre"""
		return self.x*v2.x+self.y*v2.y
		
	def copy(self):
		return v2D(self.x,self.y)


# Objet vecteur en 3D *******************************************	
class v3D:
	def __init__(self,_x,_y,_z,_base=None):
		if(_base==None):
			self.x=_x
			self.y=_y
			self.z=_z
		else:
			self.x=_x*_base[0].x+_y*_base[1].x+_z*_base[2].x
			self.y=_x*_base[0].y+_y*_base[1].y+_z*_base[2].y
			self.z=_x*_base[0].z+_y*_base[1].z+_z*_base[2].z
		self.nom=""
		
	def __repr__(self):
		return "<x="+str(self.x)+",y="+str(self.y)+",z="+str(self.z)+">"

	def __add__(self,v):
		return v3D(self.x+v.x,self.y+v.y,self.z+v.z)
	def __radd__(self,v):
		return self+v
	def __iadd__(self,v):
		self.x+=v.x
		self.y+=v.y
		self.z+=v.z
		return self
		
	def __sub__(self,v):
		return v3D(self.x-v.x,self.y-v.y,self.z-v.z)
	def __rsub__(self,v):
		return v-self
	def __isub__(self,v):
		self.x-=v.x
		self.y-=v.y
		self.z-=v.z
		return self
		
	def __mul__(self,l):
		if l.__class__.__name__=="v3D": #Si c'est pour un produit scalaire
			return self.x*l.x + self.y*l.y + self.z*l.z
		else :#Si c'est pour un produit scalaire
			return v3D(self.x*l,self.y*l,self.z*l)
	def __rmul__(self,l):
		return self*l
	def __imul__(self,l):
		self.x*=float(l)
		self.y*=float(l)
		self.z*=float(l)
		return self
		
	def __div__(self,l):
		return v3D(self.x/float(l),self.y/float(l),self.z/float(l))
	def __idiv__(self,l):
		self.x/=float(l)
		self.y/=float(l)
		self.z/=float(l)
		return self
	
	def __xor__(self,v):
		return v3D(self.y*v.z - self.z*v.y, self.z*v.x - self.x*v.z, self.x*v.y - self.y*v.x)
		
	def __neg__(self):
		return v3D(-self.x,-self.y,-self.z)
		
	def str(self):
		return "["+str(self.x)+","+str(self.y)+","+str(self.y)+"]"

	def copy(self):
		return v3D(self.x,self.y,self.z)
		
	def norme(self):
		return math.sqrt(self.x**2+self.y**2+self.z**2)
		
#	def additionne(self,v):
#		self.x+=v.x
#		self.y+=v.y
#		self.z+=v.z
		
	def normalise(self):
		n=self.norme()
		self.x/=n
		self.y/=n
		self.z/=n
		
	def prodSca(self,v):
		return self.x*v.x+self.y*v.y+self.z*v.z
		
	def prodVect(self,v):
		return v3D(self.y*v.z-self.z*v.y,self.z*v.x-self.x*v.z,self.x*v.y-self.y*v.x)
		
	def getVec2DProj(self):
		return v2D(self.x,self.y)

# Converti une liste de couple de point en chemin inkscape *******************************************	
def points_to_svgd(p, close=True):
    """ convert list of points (x,y) pairs
        into a closed SVG path list
    """
    f = p[0]
    p = p[1:]
    svgd = 'M%.4f,%.4f' % f
    for x in p:
        svgd += 'L%.4f,%.4f' % x
    if close:
        svgd += 'z'
    return svgd


#Idem que points_ti_svgd, mais pour de la 2D projetee sur une base *******************************************
def points2D_to_svgd(p2D,close=True,base2D=None):
	if(base2D!=None):
	    (Vx,Vy)=base2D
	p=[]
	for point in p2D:
		if(base2D==None):
			p.append(point)
		else:
	 	   	p.append( (point[0]*Vx.x+point[1]*Vy.x	,	point[0]*Vx.y+point[1]*Vy.y) )
	return points_to_svgd(p,close)
    
    

#Idem que points_ti_svgd, mais pour de la 3D projetee *******************************************
#Si hauteur_ombre>0, alors renvoie aussi le chemin de l'ombre
def points3D_to_svgd(p3D,close=True,base3D=None,hauteur_ombre=0):
    """ convert list of points (x,y) pairs
        into a closed SVG path list
        base 3D est un triplet de vecteurs projetes dans le plan. Si absent, on prend la base brute de la feuille
    """
    if(base3D!=None):
	    (Vx,Vy,Vz)=base3D
    p=[]
    p_ombre=[]
    for point in p3D:
    	if(base3D==None):
    		p.append((point[0],point[1]))
    	else:
	    	p.append( (point[0]*Vx.x+point[1]*Vy.x+point[2]*Vz.x	,	point[0]*Vx.y+point[1]*Vy.y+point[2]*Vz.y) )
	    	if hauteur_ombre>0 :
		    	p_ombre.append(	(point[0]*Vx.x+point[1]*Vy.x-hauteur_ombre*Vz.x	,	point[0]*Vx.y+point[1]*Vy.y-hauteur_ombre*Vz.y	) )

    profondeur=0
    longueur=0
    for i in range(len(p3D)-1):
    	p1=p3D[i]
    	p2=p3D[i+1]
    	P1P2=(p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2])
    	l=math.sqrt(P1P2[0]**2+P1P2[1]**2+P1P2[2]**2)
    	if(base3D==None):
	    	profondeur+=0.5*(p1[2]+p2[2])*l
	else:
		profondeur+=0.5*((p1[0]*Vx.z+p1[1]*Vy.z+p1[2]*Vz.z)+(p2[0]*Vx.z+p2[1]*Vy.z+p2[2]*Vz.z))*l
    	longueur+=l
    if close:#Ajout du dernier segment
    	p1=p3D[0]
    	p2=p3D[-1]
    	P1P2=(p2[0]-p1[0],p2[1]-p1[1],p2[2]-p1[2])
    	l=math.sqrt(P1P2[0]**2+P1P2[1]**2+P1P2[2]**2)
    	if(base3D==None):
	    	profondeur+=0.5*(p1[2]+p2[2])*l
	else:
		profondeur+=0.5*((p1[0]*Vx.z+p1[1]*Vy.z+p1[2]*Vz.z)+(p2[0]*Vx.z+p2[1]*Vy.z+p2[2]*Vz.z))*l
    	longueur+=l
    	
    profondeur/=longueur
    if hauteur_ombre>0 :
    	return points_to_svgd(p,close),profondeur,points_to_svgd(p_ombre,close),
    return points_to_svgd(p,close),profondeur
  


#Fonction qui convertit les couleurs (short int en hex) *********************************************
def convertIntColor2Hex(i):
	#http://www.hoboes.com/Mimsy/hacks/parsing-and-setting-colors-inkscape-extensions/
	longColor = long(i)
	if longColor < 0:
		longColor = long(longColor & 0xFFFFFFFF)
	color="#"+("00000000"+hex(longColor)[2:-1])[-8:-2]
    	return color



#Fonction qui renvoie 2 vecteurs 2D, dans la base Bfeuille, avec une rotation de theta ****************************************
def getBase2D(echelle=1,theta=0,direct=True):
	if direct:
		theta*=-1
	Vx=echelle*v2D(	math.cos(theta),	math.sin(theta)	)
	Vy=echelle*v2D(	-math.sin(theta),	math.cos(theta)	)
	if direct:
		Vy*=-1
	return Vx,Vy



#Fonction qui renvoie 3 vecteurs 3D, dans la base Bfeuille ****************************************
def getVecteursAxonometriques(echelle=1):
	Vx=echelle*v3D(	-math.sqrt(2./3)*math.cos(math.pi/6),	math.sqrt(2./3)*math.sin(math.pi/6),	math.sqrt(2./3)*math.tan(math.acos(math.sqrt(2./3))))
	Vy=echelle*v3D(	math.sqrt(2./3)*math.cos(math.pi/6),	math.sqrt(2./3)*math.sin(math.pi/6),	math.sqrt(2./3)*math.tan(math.acos(math.sqrt(2./3))))
	Vz=echelle*v3D(	0,				-math.sqrt(2./3),			math.sqrt(2./3)*math.tan(math.acos(math.sqrt(2./3))))
	return Vx,Vy,Vz

#Fonction qui construit une base a partir d'un vecteur directeur vec (v3D) ******************************
#theta est un angle de rotation par rapport a la base initiale
def getBaseFromVecteur(vec,echelle=1,theta=0):
	Vx,Vy,Vz=getVecteursAxonometriques()
	vDiff=Vz
	if vec.prodVect(Vz).norme()<1e-3:#Si vDiff colineaire
		vDiff=Vy	#On change
	u=vec.copy()
	
	#Base de base
	u.normalise()
	v=vDiff.prodVect(u)
	v.normalise()
	w=u.prodVect(v)
	
	#base tournee
	
	X=echelle*u
	X.nom="X"
	Y=echelle*(math.cos(theta)*v+math.sin(theta)*w)
	Y.nom="Y"
	Z=echelle*(-math.sin(theta)*v+math.cos(theta)*w)
	Z.nom="Z"

	return X,Y,Z
	
	
#Fonction qui recherche les angles de "coupure" entre l'avant plan et l'arriere plan d'un cercle
#base = triplet de vecteurs 3D. le premier doit etre l'axe de rotation. Le second est directeur du rayon quand theta=0
def getAnglesCoupure(base):
	theta=0
	n=20
	dtheta=2*math.pi/n
	X,Y,Z=base
	axeProjete=X.getVec2DProj()
	axeNormal=axeProjete.copy()
	axeNormal.rotation(math.pi/2)
	def ecartement(theta):
		point3D=v3D(0,math.cos(theta),math.sin(theta),base)
		point2D=point3D.getVec2DProj()
		return point2D.prodSca(axeNormal)
	while deriv(ecartement,theta)*deriv(ecartement,theta+dtheta)>0:#Recherche d'un encadrement
		theta+=dtheta
	thetaA=theta
	thetaB=theta+dtheta
	while abs(thetaA-thetaB)>10**(-3):
		thetaC=0.5*(thetaA+thetaB)
		if(deriv(ecartement,thetaA)*deriv(ecartement,thetaC)>0):
			thetaA=thetaC
		else:
			thetaB=thetaC
	return thetaC,thetaC+math.pi
	
# Renvoie une liste d'arcs de cercles (triplet de points 3D dans la base de la feuille), en fonction de s'ils sont en avant ou en arriere plan
# Les arcs sont compris entre thetaDeb et thetaFin
# Ils sont centres sur "centre" (V3D, defini par rapport a base), et on un rayon "R"
# La rotation se fait autour de l'axe 1 de "axe", l'angle zero correspond a la direction de l'axe2
def getListePoints2DCercle(axes,centre,R,thetaDeb,thetaFin,thetaCoupure1,thetaCoupure2,n=100):
	arcs=[[]]	#Liste des arcs
	theta=thetaDeb
	dtheta=math.pi*2./n

	
	def getPointForCercle(axes,vcentre,R,theta):
		Vx1,Vy1,Vz1=axes
		
		x1=0
		y1=R*math.cos(theta)
		z1=R*math.sin(theta)
		vRayon=v3D(x1,y1,z1,axes)
		
		point=vcentre+vRayon
		#debug("theta = "+str(theta)+"\n(x1,y1,z1) = "+str((x1,y1,z1))+"\n\n"+"Vx1 = "+str(Vx1)+"\nVy1 = "+str(Vy1)+"\nVz1 = "+str(Vz1)+"\n\nvRayon = "+str(vRayon),2)
		return (point.x,point.y,point.z)
			

	while theta<thetaFin: #Pour chaque angle...
		arcs[-1].append(getPointForCercle(axes,centre,R,theta))#On ajoute le point
		if (theta-thetaCoupure1)*(theta+dtheta-thetaCoupure1)<0:#Si on passe une coupure
			arcs[-1].append(getPointForCercle(axes,centre,R,thetaCoupure1))#On acheve le troncon precedent
			arcs.append([getPointForCercle(axes,centre,R,thetaCoupure1)])#Nouveau troncon
		elif (theta-thetaCoupure2)*(theta+dtheta-thetaCoupure2)<0:#Si on passe une coupure
			arcs[-1].append(getPointForCercle(axes,centre,R,thetaCoupure2))#On acheve le troncon precedent
			arcs.append([getPointForCercle(axes,centre,R,thetaCoupure2)])#Nouveau troncon
		
		theta+=dtheta
	arcs[-1].append(getPointForCercle(axes,centre,R,thetaFin))#On acheve le troncon precedent
	
	#Gesion des cercles entier (relier thetaDeb a thetaFin)
	if(len(arcs)==3):	#S'il y a 3 groupes (1 avant-plan et 2 arriere plan ou vis versa)
		p1=arcs[0][0]
		p2=arcs[-1][-1]
		if((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2<10**(-5)):#Si les 2 points sont les memes
			listeConcat=arcs[-1][:-1]+arcs[0]#On concatene (sauf le dernier point de l'un car meme que le premier de l'autre)
			arcs[0]=listeConcat#On enregistre
			arcs.pop(2)#On vire le dernier troncons 
	return arcs

# Fonction qui prend une liste de listes points 3D, censés être consécutifs
# et qui les reconcatènes dans le bon ordre.
# La liste principale peut être dans le mauvais ordre, mais les listes de troncons doivent être orientees pareil.
"""def concateneChemins3DDansLOrdre(L):
	L_result = L[0][:] # On recopie le premier troncon
	dejaFait = [0] #Troncon deja concatenes
	for k in range(len(L)-1) :
		dist= = 99999999
		cible = -1
		avant = True #Pous savoir sil faut concatener au debut ou pas
		for i in range(len(L)):
			if i not in dejaFait :
				distAvant = ...
				distApres = ...
				if distAvant < dist :
					dist = distAvant
					avant = True
					cible = i
				if distApres < dist :
					dist = distApres
					avant = False
					cible = i
			if avant :
				L_result = L[cible]+L_result
			else :
				L_result += L[cible]
			dejaFait.append(cible)
	return L_result"""


#Fonction qui trie les listes de couple (chemin,profondeur) dans l'ordre croissant
#Et renvoie la profondeur moyenne (non coefficientee)
#Trie bulle
def trieChemins(liste):
	for i in range(len(liste)):
		for j in range(len(liste)-i-1):
			if(float(liste[j].get("profondeur"))>float(liste[j+1].get("profondeur"))):
				liste[j],liste[j+1]=liste[j+1],liste[j]
	moyenne=0.
	for i in range(len(liste)):
		moyenne+=float(liste[i].get("profondeur"))
	moyenne/=len(liste)
	return moyenne
	
#Fonction qui trie une liste de chemin
#en fonction de leur attribut "profondeur" (str, mais qui represente un flottant)
#et les ajoute dans l'ordre dans le groupe de inkscape
def ajouteCheminDansLOrdreAuGroupe(groupe,listeChemins):
	trieChemins(listeChemins)
	for obj in listeChemins:
		groupe.append(obj)
#	assert 0,str(listeChemins)

	
	
# Fonction qui cherche dans une liste "liste" le point le plus proche (en terme de coordonnées) du point "point",
# en 2D (en terme de norme)
# Renvoie l'indice et la distance
def trouvePoint2DProche(point,liste):
	i_min=0
	d_min=math.sqrt((point[0]-liste[0][0])**2+(point[1]-liste[0][1])**2)
	for i in range(1,len(liste)):
		d=math.sqrt((point[0]-liste[i][0])**2+(point[1]-liste[i][1])**2)
		if d<d_min:
			d_min=d
			i_min=i
	return d_min,i_min
	
#Fonction qui renvoie une liste (de la meme taille que liste1), contenant les distances
#entre chaque point de liste1, et le point le plus proche de liste2
def getDistancesListe2Liste(liste1,liste2):
	distances=[]
	for P in liste1:
		res=trouvePoint2DProche(P,liste2)
		distances.append(res[0])
	return distances
	
#Fonction qui renvoie un couple (indices,valeur) des minimums locaux d'une liste, sous forme de liste
def getIndicesMins(L):
	res=[]
	for i in range(len(L)):
		if L[i]<L[i-1] and L[i]<L[(i+1)%len(L)]:
			res.append((i,L[i]))
	return res
	
def lisseListe(L,n):
	aux=[0]*len(L)
	for i in range(n):
		aux[:]=L[:]
		for j in range(len(L)):
			aux[j]=1./3*(L[j-1]+L[j]+L[(j+1)%len(L)])
		L[:]=aux[:]
	return L

#Concatène 2 listes de triplets, en inversant éventuellement la seconde pour permettre une continuité			
def concateneContinu(L1,L2):
	if ((L1[-1][0]-L2[0][0])**2+(L1[-1][1]-L2[0][1])**2+(L1[-1][2]-L2[0][2])**2>(L1[-1][0]-L2[-1][0])**2+(L1[-1][1]-L2[-1][1])**2+(L1[-1][2]-L2[-1][2])**2):
		return L1+[L2[-i] for i in range(1,len(L2)+1)]
	else:
		return L1+L2
		
#Fonction qui teste si deux valeurs a et b encadre une valeur cut %2pi
def encadreLimite(a,b,cut):
	if a>b:#Si dans le désordre
		a,b=b,a
	a=a%(2*math.pi)
	b=b%(2*math.pi)
	cut=cut%(2*math.pi)
	if a>b:#Probleme du modulo 2pi : Cas où a=359° et b=362°
		if cut<b:#cas ou cut=361°
			cut+=2*math.pi
		b+=2*math.pi
	if a<cut and cut<=b:
		return True
	return False
	
#Fonction qui converti longueur (float) supposée etre dans les unité de l'option, en longueur propre a Inkscape
def convertLongueur2Inkscape(options,longueur):	
	unite = options.unite_base
	norme = options.longueur_base
	return options.effect.unittouu(str(longueur*norme)+unite)
	
		



def dessin_Pivot_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_pivot_2D_cote_x
	y = -options.liaison_pivot_2D_cote_y
	#Orientation **************************************
	rotation=options.liaison_pivot2D_cote_orientation #Angle par defaut (sens trigo)
	if(options.liaison_pivot2D_cote_axe=="x"):
		rotation=0
	elif(options.liaison_pivot2D_cote_axe=="y"):
		rotation=90.
	elif(options.liaison_pivot2D_cote_axe=="-x"):
		rotation=180.
	elif(options.liaison_pivot2D_cote_axe=="-y"):
		rotation=-90.
	#Base *********************
	echelle_liaison=options.echelle
	Vx1,Vy1=getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	old_liaisons=options.opt_gene_gene_old
	largeur = p2Dc_longueur
	hauteur = diametre_pivot
	espace_arrets = p2Dc_ecarts_arrets
	longueur_axe = p2Dc_longueur_male
	longueur_tige = p2Dc_longueur_tige_femelle
	couleur_femelle = options.opt_gene_piece2_couleur
	couleur_male = options.opt_gene_piece1_couleur
	epaisseur_femelle=  options.opt_gene_lignes_epaisseur_2
	epaisseur_male=  options.opt_gene_lignes_epaisseur_1

	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        fond_femelle = inkex.etree.SubElement(liaison,'g')
	male = inkex.etree.SubElement(liaison,'g')
	femelle = inkex.etree.SubElement(liaison,'g')
	
	
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
	
	#Arret male 1
	arretM1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-largeur/2.-espace_arrets	,	-hauteur/2),
					(-largeur/2.-espace_arrets	,	hauteur/2)	]
				,False,base2D)
	arretM1.set('d',chemin)
	arretM1.set('stroke',couleur_male)
	arretM1.set('stroke-width',str(epaisseur_male))
	male.append(arretM1)
	
	#Arret male 2
	arretM2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(largeur/2.+espace_arrets	,	-hauteur/2),
					(largeur/2.+espace_arrets	,	hauteur/2)	]
				,False,base2D)
	arretM2.set('d',chemin)
	arretM2.set('stroke',couleur_male)
	arretM2.set('stroke-width',str(epaisseur_male))
	male.append(arretM2)
	
	# Femelle ***************************************
	if(old_liaisons):
		barreF1=inkex.etree.Element(inkex.addNS('path','svg'))
		chemin=points2D_to_svgd([	(-largeur/2.	,	-hauteur/2),
						(largeur/2.	,	-hauteur/2.)	]
					,False,base2D)
		barreF1.set('d',chemin)
		barreF1.set('stroke',couleur_femelle)
		barreF1.set('stroke-width',str(epaisseur_femelle))
		male.append(barreF1)
		
		barreF2=inkex.etree.Element(inkex.addNS('path','svg'))
		chemin=points2D_to_svgd([	(-largeur/2.	,	hauteur/2),
						(largeur/2.	,	hauteur/2.)	]
					,False,base2D)
		barreF2.set('d',chemin)
		barreF2.set('stroke',couleur_femelle)
		barreF2.set('stroke-width',str(epaisseur_femelle))
		male.append(barreF2)
	else:
		#Rectangle
		rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
		rectangle.set('x',str(-largeur*echelle_liaison/2) )
		rectangle.set('y',str(-hauteur*echelle_liaison/2) )
		rectangle.set('width',str(largeur*echelle_liaison))
		rectangle.set('height',str(hauteur*echelle_liaison))
		rectangle.set('style','fill:none')
		rectangle.set('stroke',couleur_femelle)
		rectangle.set('stroke-width',str(epaisseur_femelle))
		femelle.append(rectangle)
	
		# Fond de femelle opaque ****************************
		#Rectangle - fond
		rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
		rectangle.set('x',str(-largeur*echelle_liaison/2) )
		rectangle.set('y',str(-hauteur*echelle_liaison/2) )
		rectangle.set('width',str(largeur*echelle_liaison))
		rectangle.set('height',str(hauteur*echelle_liaison))
		rectangle.set('style','fill:white')
		fond_femelle.append(rectangle)
	
	#Tige femelle
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	-hauteur/2.),
					(0	,	-hauteur/2.-longueur_tige)	]
				,True,base2D)
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle))
	femelle.append(ligneF)
	
	# Transformations ***************************************
	fond_femelle.set("transform","rotate("+str(-rotation)+")")
	male.set("transform","rotate("+str(-rotation)+")")
	femelle.set("transform","rotate("+str(-rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	

def dessin_Pivot_2D_face(options,contexte):
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_pivot_2D_face_x
	y = -options.liaison_pivot_2D_face_y
	#Orientation **************************************
	rotation1=-options.liaison_pivot2D_face_orientation1 #Angle par defaut (sens trigo)
	if(options.liaison_pivot2D_face_axe1=="x"):
		rotation1=0
	elif(options.liaison_pivot2D_face_axe1=="y"):
		rotation1=-90
	elif(options.liaison_pivot2D_face_axe1=="-x"):
		rotation1=180
	elif(options.liaison_pivot2D_face_axe1=="-y"):
		rotation1=90
	rotation2=-options.liaison_pivot2D_face_orientation2 #Angle par defaut (sens trigo)
	if(options.liaison_pivot2D_face_axe2=="x"):
		rotation2=0
	elif(options.liaison_pivot2D_face_axe2=="y"):
		rotation2=-90
	elif(options.liaison_pivot2D_face_axe2=="-x"):
		rotation2=180
	elif(options.liaison_pivot2D_face_axe2=="-y"):
		rotation2=90
	#Base *********************
	echelle_liaison=options.echelle
	Vx1,Vy1=getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	rayon = p2Df_diametre/2
	longueur_tige = p2Df_longueur_tige
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1

	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        #groupe_rotation = inkex.etree.SubElement(liaison, 'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle=inkex.etree.SubElement(liaison,'g')

	# Male ***************************************
	axe1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	0),
					(rayon+longueur_tige	,	0)	]
				,False,base2D)
	axe1.set('d',chemin)
	axe1.set('stroke',couleur_male)
	axe1.set('stroke-width',str(epaisseur_male))
	male.append(axe1)

	# Femelle ***************************************	
	#axe
	axe2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	0),
					(longueur_tige+rayon	,	0)	]
				,False,base2D)	
	axe2.set('d',chemin)
	axe2.set('stroke',couleur_femelle)
	axe2.set('stroke-width',str(epaisseur_femelle))
	femelle.append(axe2)
	#cercle
	cercle=inkex.etree.Element(inkex.addNS('circle','svg'))
	cercle.set('cx',"0")
	cercle.set('cy',"0")
	cercle.set('r',str(rayon*echelle_liaison))
	cercle.set('stroke',str(couleur_femelle))
	cercle.set('stroke-width',str(epaisseur_femelle))
	cercle.set('style','fill:white')
	femelle.append(cercle)

	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation1)+")")
	femelle.set("transform","rotate("+str(rotation2)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






#===============================================================
def dessin_Pivot_3D(options,contexte):
	#Origine 2D
	x0=options.x0
	y0=options.y0
	#Base Axonometrique
	echelle_liaison=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques()
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x=options.liaison_pivot_3D_position_x
	y=options.liaison_pivot_3D_position_y
	z=options.liaison_pivot_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	ombre = True
	largeur = p3D_longueur
	rayon = p3D_diametre/2.
	rayonTige = p3D_longueur_tige_femelle
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	angle_male=-float(options.liaison_pivot_3D_orientation_male)/180.*math.pi
	angle_femelle=-float(options.liaison_pivot_3D_orientation_femelle)/180.*math.pi
	#Repere local de la liaison
	if(options.liaison_pivot_3D_type_direction=="\"liaison_pivot_3D_type_direction_quelconque\""):
		V=v3D(options.liaison_pivot_3D_type_direction_quelconque_x,options.liaison_pivot_3D_type_direction_quelconque_y,options.liaison_pivot_3D_type_direction_quelconque_z,base)
		if V.x == V.y == V.z == 0 : V=v3D(1,0,0,base) #Si vecteur nul : on prend X par defaut
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle_liaison,angle_male)#Repere male
		Vx2,Vy2,Vz2=getBaseFromVecteur(V,echelle_liaison,angle_femelle)#Repere Femelle
	else:	#Si vecteur standard
		if(options.liaison_pivot_3D_axe=="x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle_liaison,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vx,echelle_liaison,angle_femelle)#Repere Femelle
		elif(options.liaison_pivot_3D_axe=="y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle_liaison,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vy,echelle_liaison,angle_femelle)#Repere Femelle
		else:#z
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle_liaison,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vz,echelle_liaison,angle_femelle)#Repere Femelle
	baseLocale1=(Vx1,Vy1,Vz1)
	baseLocale2=(Vx2,Vy2,Vz2)

	#Groupes 
	liaison = inkex.etree.SubElement(contexte, 'g')
        ombres = inkex.etree.SubElement(liaison, 'g')
        
	# Male ***************************************
	axe=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-p3D_longueur_male/2.,	0,	0	),
					(p3D_longueur_male/2.,	0,	0	)
				],False,baseLocale1)
	axe.set('d',chemin)
	axe.set('stroke',couleur_male)
	axe.set('stroke-width',str(epaisseur_male))
	axe.set('style','stroke-linecap:round')
	axe.set('profondeur',str(profondeur))

	#Ombre
	#if ombre:
	#	axe_ombre=inkex.etree.Element(inkex.addNS('path','svg'))
	#	axe_ombre.set('d',chemin_ombre)
	#	axe_ombre.set('stroke','#000000')
	#	axe_ombre.set('stroke-width',str(epaisseur_male))
	#	axe_ombre.set('style','stroke-linecap:round')
	#        ombres.append(axe_ombre)

	arret1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeure=points3D_to_svgd([
					(2*largeur/3,	rayon,	0	),
					(2*largeur/3,	-rayon,	0	)
				],False,baseLocale1)
	arret1.set('d',chemin)
	arret1.set('stroke',couleur_male)
	arret1.set('stroke-width',str(epaisseur_male))
	arret1.set('style','stroke-linecap:round')
	arret1.set('profondeur',str(profondeur))
	
	#Ombre
	#if ombre:
	#	arret1_ombre=inkex.etree.Element(inkex.addNS('path','svg'))
	#	arret1_ombre.set('d',chemin_ombre)
	#	arret1_ombre.set('stroke','#000000')
	#	arret1_ombre.set('stroke-width',str(epaisseur_male))
	#	arret1_ombre.set('style','stroke-linecap:round')
	#        ombres.append(arret1_ombre)
	
	arret2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.-p3D_ecarts_arrets,	p3D_longueur_arrets/2.,	0	),
					(-largeur/2.-p3D_ecarts_arrets,	-p3D_longueur_arrets/2.,	0	)
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
	
	
	chemin,profondeurDemiCylindre1=points3D_to_svgd(listeDemiCylindre1,True,None)
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
					(0,	0,	rayon+p3D_longueur_tige_femelle)
				],False,baseLocale2)
	barreFemelle.set('d',chemin)
	barreFemelle.set('stroke',couleur_femelle)
	barreFemelle.set('stroke-width',str(epaisseur_femelle))
	barreFemelle.set('style','stroke-linecap:round')
	barreFemelle.set('profondeur',str(profondeur*1e10))
	


	# Ajout au Groupe *****************************************
        listeObjets=[axe,arret1,arret2,demiCylindre1,demiCylindre2,barreFemelle]
        
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)

	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	
 

def dessin_Pivot_Glissant_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_pivot_glissant_2D_cote_x
	y = -options.liaison_pivot_glissant_2D_cote_y
	#Parametres ****************************
	old_liaisons = options.opt_gene_gene_old
	largeur = pg2Dc_longueur
	hauteur = pg2Dc_diametre
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	longueur_tige = pg2Dc_longueur_tige_femelle
	#Orientation **************************************
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
        fond_femelle = inkex.etree.SubElement(liaison,'g')
	male=inkex.etree.SubElement(liaison,'g')
	femelle=inkex.etree.SubElement(liaison,'g')
	#Base **************************
	echelle_liaison=options.echelle
	Vx1,Vy1=getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	# Male ***************************************
	#Ligne male
	ligneM=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-pg2Dc_longueur_male/2.,	0),
				(pg2Dc_longueur_male/2.	,	0)	],
				True,base2D)
	ligneM.set('d',chemin)
	ligneM.set('stroke',couleur_male)
	ligneM.set('stroke-width',str(epaisseur_male*echelle_liaison))
	male.append(ligneM)
	
	# Femelle ***************************************
	if(old_liaisons):
		barreF1=inkex.etree.Element(inkex.addNS('path','svg'))
		chemin=points2D_to_svgd([(-largeur/2	,	-hauteur/2),
					(largeur/2	,	-hauteur/2)	],
					False,base2D)
		barreF1.set('d',chemin)
		barreF1.set('stroke',couleur_femelle)
		barreF1.set('stroke-width',str(epaisseur_femelle*echelle_liaison))
		male.append(barreF1)
		
		barreF2=inkex.etree.Element(inkex.addNS('path','svg'))
		chemin=points2D_to_svgd([(-largeur/2	,	hauteur/2),
					(largeur/2	,	hauteur/2)	],
					False,base2D)
		barreF2.set('d',chemin)
		barreF2.set('stroke',couleur_femelle)
		barreF2.set('stroke-width',str(epaisseur_femelle*echelle_liaison))
		male.append(barreF2)
	else:
		#Rectangle
		rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
		rectangle.set('x',str(-largeur*echelle_liaison/2) )
		rectangle.set('y',str(-hauteur*echelle_liaison/2) )
		rectangle.set('width',str(largeur*echelle_liaison))
		rectangle.set('height',str(hauteur*echelle_liaison))
		rectangle.set('style','fill:none')
		rectangle.set('stroke',couleur_femelle)
		rectangle.set('stroke-width',str(epaisseur_femelle*echelle_liaison))
		femelle.append(rectangle)
		# Fond de femelle opaque ****************************
		#Rectangle - fond
		rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
		rectangle.set('x',str(-largeur*echelle_liaison/2) )
		rectangle.set('y',str(-hauteur*echelle_liaison/2) )
		rectangle.set('width',str(largeur*echelle_liaison))
		rectangle.set('height',str(hauteur*echelle_liaison))
		rectangle.set('style','fill:white')
		fond_femelle.append(rectangle)
	
	#Ligne femelle
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	-hauteur/2),
				(0	,	-hauteur/2 - longueur_tige)	],
				False,base2D)
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle*echelle_liaison))
	femelle.append(ligneF)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation)+")")
	femelle.set("transform","rotate("+str(rotation)+")")
	fond_femelle.set("transform","rotate("+str(rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	

def dessin_Pivot_Glissant_2D_face(options,contexte):
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_pivot_glissant_2D_face_x
	y = -options.liaison_pivot_glissant_2D_face_y
	#Parametres ****************************
	rayon = pg2Df_diametre/2.
	couleur_femelle = options.opt_gene_piece2_couleur
	couleur_male = options.opt_gene_piece1_couleur
	epaisseur_femelle = options.opt_gene_lignes_epaisseur_2
	epaisseur_male = options.opt_gene_lignes_epaisseur_1
	rotation1 = -options.liaison_pivot_glissant_2D_face_orientation1 #Angle par defaut (sens trigo)
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
	#Base **************************
	echelle_liaison=options.echelle
	Vx1,Vy1=getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	femelle=inkex.etree.SubElement(liaison,'g')
	male=inkex.etree.SubElement(liaison,'g')

	
	# Femelle ***************************************	
	#axe
	axe2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	0),
					(rayon + pg2Df_longueur_tige,	0)	],
					False,base2D)
	axe2.set('d',chemin)
	axe2.set('stroke',couleur_femelle)
	axe2.set('stroke-width',str(epaisseur_femelle))
	femelle.append(axe2)
	#cercle
	cercle=inkex.etree.Element(inkex.addNS('circle','svg'))
	cercle.set('cx',"0")
	cercle.set('cy',"0")
	cercle.set('r',str(rayon*echelle_liaison))
	cercle.set('stroke',str(couleur_femelle))
	cercle.set('stroke-width',str(epaisseur_femelle))
	cercle.set('style','fill:white')
	femelle.append(cercle)
	
	# Male ***************************************
	axe1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	0),
					(rayon + pg2Df_longueur_tige,	0)	],
					False,base2D)
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
	puce.set('style','fill:'+couleur_male)
	male.append(puce)
		
	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation1)+")")
	femelle.set("transform","rotate("+str(rotation2)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






#===============================================================
def dessin_Pivot_Glissant_3D(options,contexte):
	#Origine 2D
	x0=options.x0
	y0=options.y0
	#Base Axonometrique
	echelle_liaison=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques()
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x=options.liaison_pivot_glissant_3D_position_x
	y=options.liaison_pivot_glissant_3D_position_y
	z=options.liaison_pivot_glissant_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	longueur = pg3D_longueur
	longueu_male = pg3D_longueur_male
	rayon = pg3D_diametre / 2.
	rayonTige = pg3D_longueur_tige_femelle + rayon
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	angle_femelle=-float(options.liaison_pivot_glissant_3D_orientation_femelle)/180.*math.pi
	#Repere local de la liaison
	if(options.liaison_pivot_glissant_3D_type_direction=="\"liaison_pivot_glissant_3D_type_direction_quelconque\""):
		V=v3D(options.liaison_pivot_glissant_3D_type_direction_quelconque_x,options.liaison_pivot_glissant_3D_type_direction_quelconque_y,options.liaison_pivot_glissant_3D_type_direction_quelconque_z,base)
		if V.x == V.y == V.z == 0 : V=v3D(1,0,0,base) #Si vecteur nul : on prend X par defaut
		Vx2,Vy2,Vz2=getBaseFromVecteur(V,echelle_liaison,angle_femelle)#Repere Femelle
	else:	#Si vecteur standard
		if(options.liaison_pivot_glissant_3D_axe=="x"):
#			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle_liaison,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vx,echelle_liaison,angle_femelle)#Repere Femelle
		elif(options.liaison_pivot_glissant_3D_axe=="y"):
#			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle_liaison,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vy,echelle_liaison,angle_femelle)#Repere Femelle
		else:#z
#			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle_liaison,angle_male)#Repere male
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vz,echelle_liaison,angle_femelle)#Repere Femelle
#	baseLocale1=(Vx1,Vy1,Vz1)
	baseLocale=(Vx2,Vy2,Vz2)

	
	# Male ***************************************
	axe=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-pg3D_longueur_male/2.,	0,	0	),
					(pg3D_longueur_male/2.,	0,	0	)
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
	centre1 = v3D(-longueur/2,0,0,baseLocale) #Vecteur OC1, O=centre liaison
	centre2 = v3D(longueur/2,0,0,baseLocale) #Vecteur OC1, O=centre liaison
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
					(0,	0,	rayonTige)
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
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	
def dessin_Glissiere_2D_cote(options,contexte):

	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_glissiere_2D_cote_x
	y = -options.liaison_glissiere_2D_cote_y
	#Orientation **************************************
	rotation=options.liaison_glissiere_2D_cote_direction_quelconque #Angle par defaut (sens trigo)
	if(options.liaison_glissiere_2D_cote_direction_standard=="x"):
		rotation=0
	elif(options.liaison_glissiere_2D_cote_direction_standard=="y"):
		rotation=90.
	elif(options.liaison_glissiere_2D_cote_direction_standard=="-x"):
		rotation=180.
	elif(options.liaison_glissiere_2D_cote_direction_standard=="-y"):
		rotation=-90.
	#Base *********************
	echelle_liaison=options.echelle
	Vx1,Vy1=getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	old_liaisons=options.opt_gene_gene_old
	largeur=g2Dc_longueur
	hauteur=g2Dc_hauteur
	longueur_axe=g2Dc_longueur_male
	longueur_tige=g2Dc_longueur_tige_femelle
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
	rectangle.set('x',str(-largeur*echelle_liaison/2) )
	rectangle.set('y',str(-hauteur*echelle_liaison/2) )
	rectangle.set('width',str(largeur*echelle_liaison))
	rectangle.set('height',str(hauteur*echelle_liaison))
	rectangle.set('style','fill:#FFFFFF')
	rectangle.set('stroke',couleur_femelle)
	rectangle.set('stroke-width',str(epaisseur_femelle))
	femelle.append(rectangle)
	
	#Ligne femelle
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	hauteur/2.),
					(0	,	hauteur/2.+longueur_tige)	]
				,False,base2D)
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle))
	femelle.append(ligneF)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(-rotation)+")")
	femelle.set("transform","rotate("+str(-rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	

def dessin_Glissiere_2D_face(options,contexte):
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_glissiere_2D_face_x
	y = -options.liaison_glissiere_2D_face_y
	#Orientation **************************************
	rotation=options.liaison_glissiere_2D_face_orientation_quelconque_femelle-90 #Angle par defaut (sens trigo)
	if(options.liaison_glissiere_2D_face_orientation_standard_femelle == "x"):
		rotation = -90.
	elif(options.liaison_glissiere_2D_face_orientation_standard_femelle == "y"):
		rotation = 0.
	elif(options.liaison_glissiere_2D_face_orientation_standard_femelle == "-x"):
		rotation = 90.
	elif(options.liaison_glissiere_2D_face_orientation_standard_femelle == "-y"):
		rotation = 180.
	rotation_tige_male = -90+options.liaison_glissiere_2D_face_orientation_quelconque_male
	if(options.liaison_glissiere_2D_face_orientation_standard_male != "autre"):
		rotation_tige_male = rotation+int(options.liaison_glissiere_2D_face_orientation_standard_male)
#	assert 0,rotation_tige_male
	#Base *********************
	echelle_liaiaon = options.echelle
	Vx1, Vy1 = getBase2D(echelle_liaiaon)
	base2D = (Vx1,Vy1)
	#Parametres *********************
	profondeur = g2Df_largeur
	hauteur = g2Df_hauteur
	longueur_tige_femelle = g2Df_longueur_tige_femelle
	longueur_tige_male = g2Df_longueur_tige_male
	couleur_femelle = options.opt_gene_piece2_couleur
	couleur_male = options.opt_gene_piece1_couleur
	epaisseur_femelle = options.opt_gene_lignes_epaisseur_2
	epaisseur_male = options.opt_gene_lignes_epaisseur_1
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte,'g')
	male = inkex.etree.SubElement(liaison,'g')
	femelle = inkex.etree.SubElement(liaison,'g')

	# Femelle ***************************************	
	#rectangle
	rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-profondeur*echelle_liaiaon/2) )
	rectangle.set('y',str(-hauteur*echelle_liaiaon/2) )
	rectangle.set('width',str(profondeur*echelle_liaiaon))
	rectangle.set('height',str(hauteur*echelle_liaiaon))
	rectangle.set('style','fill:none')
	rectangle.set('stroke',couleur_femelle)
	rectangle.set('stroke-width',str(epaisseur_femelle))
	femelle.append(rectangle)
	#cercle
	tige=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	hauteur/2.),
				(0,	hauteur/2.+longueur_tige_femelle)	]
				,False,base2D)
	tige.set('d', chemin)
	tige.set('stroke', couleur_femelle)
	tige.set('stroke-width', str(epaisseur_femelle))
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
	croix2.set('stroke-width', str(epaisseur_male))
	male.append(croix2)
	#Trait
	trait=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	0),
					(longueur_tige_male*math.sin(-rotation_tige_male/180*math.pi),	longueur_tige_male*math.cos(rotation_tige_male/180*math.pi))	]
				,False,base2D)
	trait.set('d',chemin)
	trait.set('stroke',couleur_male)
	trait.set('stroke-width',str(epaisseur_male))
	liaison.append(trait)
		
	# Transformations ***************************************
	male.set("transform","rotate("+str(-rotation)+")")
	femelle.set("transform","rotate("+str(-rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






#===============================================================
def dessin_Glissiere_3D(options,contexte):
	#Origine 2D ********
	x0=options.x0
	y0=options.y0
	#Base Axonometrique *******
	echelle_liaison = options.echelle
	Vx,Vy,Vz = getVecteursAxonometriques()
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D *******
	x = options.liaison_glissiere_3D_position_x
	y = options.liaison_glissiere_3D_position_y
	z = options.liaison_glissiere_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison ******
	epaisseur = g3D_largeur
	hauteur = g3D_hauteur
	largeur = g3D_longueur
	longueur_male = g3D_longueur_male
	longueur_tige_femelle = g3D_longueur_tige_femelle
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	angle=-float(options.liaison_glissiere_3D_orientation)/180.*math.pi
	
	#Repere local de la liaison
	if(options.liaison_glissiere_3D_type_direction=="\"liaison_glissiere_3D_type_direction_quelconque\""):
		V=v3D(options.liaison_glissiere_3D_type_direction_quelconque_x,options.liaison_glissiere_3D_type_direction_quelconque_y,options.liaison_glissiere_3D_type_direction_quelconque_z,base)
		if V.x == V.y == V.z == 0 : V=v3D(1,0,0,base) #Si vecteur nul : on prend X par defaut
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle_liaison,angle)#Repere local
	else:	#Si vecteur standard
		if(options.liaison_glissiere_3D_axe=="x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle_liaison,angle)#Repere local
		elif(options.liaison_glissiere_3D_axe=="y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle_liaison,angle)#Repere local
		else:#z
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle_liaison,angle)#Repere local
	baseLocale=(Vx1,Vy1,Vz1)

	
	# Male ***************************************
	#Axe central
	axe=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-longueur_male/2.,	0,	0	),
					(longueur_male/2.,	0,	0	)
				],False,baseLocale)
	axe.set('d',chemin)
	axe.set('stroke',couleur_male)
	axe.set('stroke-width',str(epaisseur_male))
	axe.set('style','stroke-linecap:round')
	axe.set('profondeur',str(profondeur))

	#Demi croisillon 1
	demicroix1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.,	0,	0	),
					(-largeur/2.,	-epaisseur/2.+epaisseur_femelle/2.,	hauteur/2.-epaisseur_femelle/2.	),
					(largeur/2.,	-epaisseur/2.+epaisseur_femelle/2.,	hauteur/2.-epaisseur_femelle/2.	),
					(largeur/2.,	0	,0	),
				],True,baseLocale)
	demicroix1.set('d',chemin)
	demicroix1.set('stroke',couleur_male)
	demicroix1.set('stroke-width',str(epaisseur_male))
	demicroix1.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
	demicroix1.set('profondeur',str(profondeur))
	
	#Demi croisillon 2
	demicroix2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.,	0,	0	),
					(-largeur/2.,	epaisseur/2.-epaisseur_femelle/2.,	hauteur/2.-epaisseur_femelle/2.	),
					(largeur/2.,	epaisseur/2.-epaisseur_femelle/2.,	hauteur/2.-epaisseur_femelle/2.	),
					(largeur/2.,	0	,0	),
				],True,baseLocale)
	demicroix2.set('d',chemin)
	demicroix2.set('stroke',couleur_male)
	demicroix2.set('stroke-width',str(epaisseur_male))
	demicroix2.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
	demicroix2.set('profondeur',str(profondeur))

	#Demi croisillon 3
	demicroix3=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.,	0,	0	),
					(-largeur/2.,	epaisseur/2.-epaisseur_femelle/2.,	-hauteur/2.+epaisseur_femelle/2.	),
					(largeur/2.,	epaisseur/2.-epaisseur_femelle/2.,	-hauteur/2.+epaisseur_femelle/2.	),
					(largeur/2.,	0	,0	),
				],True,baseLocale)
	demicroix3.set('d',chemin)
	demicroix3.set('stroke',couleur_male)
	demicroix3.set('stroke-width',str(epaisseur_male))
	demicroix3.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
	demicroix3.set('profondeur',str(profondeur))
	
	#Demi croisillon 4
	demicroix4=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.,	0,	0	),
					(-largeur/2.,	-epaisseur/2.+epaisseur_femelle/2.,	-hauteur/2.+epaisseur_femelle/2.	),
					(largeur/2.,	-epaisseur/2.+epaisseur_femelle/2.,	-hauteur/2.+epaisseur_femelle/2.	),
					(largeur/2.,	0	,0	),
				],True,baseLocale)
	demicroix4.set('d',chemin)
	demicroix4.set('stroke',couleur_male)
	demicroix4.set('stroke-width',str(epaisseur_male))
	demicroix4.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
	demicroix4.set('profondeur',str(profondeur))
	
	
	# Femelle ***************************************
	
	#pan1
	pan1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.,	-epaisseur/2.,	hauteur/2.	),
					(largeur/2.,	-epaisseur/2.,	hauteur/2.	),
					(largeur/2.,	epaisseur/2.,	hauteur/2.	),
					(-largeur/2.,	epaisseur/2.,	hauteur/2.	)
				],True,baseLocale)
	pan1.set('d',chemin)
	pan1.set('stroke',couleur_femelle)
	pan1.set('stroke-width',str(epaisseur_femelle))
	pan1.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
	pan1.set('profondeur',str(profondeur*1000))
	
	#pan2
	pan2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.,	epaisseur/2.,	hauteur/2.	),
					(largeur/2.,	epaisseur/2.,	hauteur/2.	),
					(largeur/2.,	epaisseur/2.,	-hauteur/2.	),
					(-largeur/2.,	epaisseur/2.,	-hauteur/2.	)
				],True,baseLocale)
	pan2.set('d',chemin)
	pan2.set('stroke',couleur_femelle)
	pan2.set('stroke-width',str(epaisseur_femelle))
	pan2.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
	pan2.set('profondeur',str(profondeur*1000))

	#pan3
	pan3=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.,	-epaisseur/2.,	-hauteur/2.	),
					(largeur/2.,	-epaisseur/2.,	-hauteur/2.	),
					(largeur/2.,	epaisseur/2.,	-hauteur/2.	),
					(-largeur/2.,	epaisseur/2.,	-hauteur/2.	)
				],True,baseLocale)
	pan3.set('d',chemin)
	pan3.set('stroke',couleur_femelle)
	pan3.set('stroke-width',str(epaisseur_femelle))
	pan3.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
	pan3.set('profondeur',str(profondeur*1000))

	#pan4
	pan4=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-largeur/2.,	-epaisseur/2.,	hauteur/2.	),
					(largeur/2.,	-epaisseur/2.,	hauteur/2.	),
					(largeur/2.,	-epaisseur/2.,	-hauteur/2.	),
					(-largeur/2.,	-epaisseur/2.,	-hauteur/2.	)
				],True,baseLocale)
	pan4.set('d',chemin)
	pan4.set('stroke',couleur_femelle)
	pan4.set('stroke-width',str(epaisseur_femelle))
	pan4.set('style','stroke-linecap:round;fill:#FFFFFF;stroke-linejoin:round')
	pan4.set('profondeur',str(profondeur*1000))
	

	#barre femelle
	barreFemelle=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	0,	hauteur/2.	),
					(0,	0,	hauteur/2. + longueur_tige_femelle)
				],False,baseLocale)
	barreFemelle.set('d',chemin)
	barreFemelle.set('stroke',couleur_femelle)
	barreFemelle.set('stroke-width',str(epaisseur_femelle))
	barreFemelle.set('style','stroke-linecap:round')
	barreFemelle.set('profondeur',str(profondeur*1000000))
	
	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        
        listeObjets=[pan1,pan2,pan3,pan4,axe,demicroix1,demicroix2,demicroix3,demicroix4,barreFemelle]
        
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)

	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y))+")")
	
	# Credits **************************************
	liaison.set("credits",options.credits)

def dessin_plane_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_plane_2D_cote_x
	y = -options.liaison_plane_2D_cote_y
	#Orientation **************************************
	rotation=90-options.liaison_plane_2D_cote_orientation #Angle par defaut (sens trigo)
	if(options.liaison_plane_2D_cote_axe=="y"):
		rotation=0
	elif(options.liaison_plane_2D_cote_axe=="x"):
		rotation=90
	elif(options.liaison_plane_2D_cote_axe=="-x"):
		rotation=-90
	elif(options.liaison_plane_2D_cote_axe=="-y"):
		rotation=180
	#Base *********************
	echelle_liaison=options.echelle
	Vx1,Vy1=getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	largeur = pl2Dc_largeur
	ecart = pl2Dc_ecartement
	longueurTige = pl2Dc_tiges
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	dessus=inkex.etree.SubElement(liaison,'g')
	dessous=inkex.etree.SubElement(liaison,'g')

	
	# DESSUS ***************************************
	#plan dessus
	planDessus=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-largeur/2	,	(ecart+epaisseur_male)/2.),
					(largeur/2	,	(ecart+epaisseur_male)/2.)	]
					,False,base2D)
	planDessus.set('d',chemin)
	planDessus.set('stroke',couleur_male)
	planDessus.set('stroke-width',str(epaisseur_male))
	dessus.append(planDessus)
	
	#tige dessus
	tigeDessus=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	(ecart+epaisseur_male)/2.),
					(0	,	ecart/2.+longueurTige)	]
				,False,base2D)
	tigeDessus.set('d',chemin)
	tigeDessus.set('stroke',couleur_male)
	tigeDessus.set('stroke-width',str(epaisseur_male))
	dessus.append(tigeDessus)
	
	# DESSOUS ***************************************
	#plan dessous
	planDessous=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-largeur/2	,	-(ecart+epaisseur_femelle)/2.),
					(largeur/2	,	-(ecart+epaisseur_femelle)/2.)	]
				,False,base2D)
	planDessous.set('d',chemin)
	planDessous.set('stroke',couleur_femelle)
	planDessous.set('stroke-width',str(epaisseur_femelle))
	dessous.append(planDessous)
	
	#tige dessous
	tigeDessous=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0	,	-(ecart+epaisseur_femelle)/2.),
					(0	,	-ecart/2.-longueurTige)	]
				,False,base2D)
	tigeDessous.set('d',chemin)
	tigeDessous.set('stroke',couleur_femelle)
	tigeDessous.set('stroke-width',str(epaisseur_femelle))
	dessous.append(tigeDessous)
	
	# Transformations ***************************************
	dessus.set("transform","rotate("+str(rotation)+")")
	dessous.set("transform","rotate("+str(rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	

def dessin_plane_2D_dessus(options,contexte):
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_plane_2D_dessus_x
	y = -options.liaison_plane_2D_dessus_y
	#Orientation **************************************
	rotationDessous=-options.liaison_plane_2D_orientation_dessous #Angle par defaut (sens trigo)
	if(options.liaison_plane_2D_axe_dessous=="x"):
		rotationDessous=0
	elif(options.liaison_plane_2D_axe_dessous=="y"):
		rotationDessous=-90
	elif(options.liaison_plane_2D_axe_dessous=="-x"):
		rotationDessous=180
	elif(options.liaison_plane_2D_axe_dessous=="-y"):
		rotationDessous=90
	rotationDessus=-options.liaison_plane_2D_orientation_dessus #Angle par defaut (sens trigo)
	if(options.liaison_plane_2D_axe_dessus=="x"):
		rotationDessus = 0
	elif(options.liaison_plane_2D_axe_dessus=="y"):
		rotationDessus = -90
	elif(options.liaison_plane_2D_axe_dessus=="-x"):
		rotationDessus = 180
	elif(options.liaison_plane_2D_axe_dessus=="-y"):
		rotationDessus = 90
	elif(options.liaison_plane_2D_axe_dessus=="180"):
		rotationDessus = rotationDessous + 180
	elif(options.liaison_plane_2D_axe_dessus=="90"):
		rotationDessus = rotationDessous - 90
	elif(options.liaison_plane_2D_axe_dessus=="-90"):
		rotationDessus = rotationDessous + 90
	elif(options.liaison_plane_2D_axe_dessus=="0"):
		rotationDessus = rotationDessous
	#Base *********************
	echelle_liaison=options.echelle
	Vx1,Vy1=getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	couleur_dessous = options.opt_gene_piece2_couleur
	couleur_dessus = options.opt_gene_piece1_couleur
	epaisseur_dessous = options.opt_gene_lignes_epaisseur_2
	epaisseur_dessus = options.opt_gene_lignes_epaisseur_1
	coteMoyen = pl2Dd_largeur
	coteDessous = pl2Dd_largeur + pl2Dd_ecartement + epaisseur_dessous
	coteDessus = pl2Dd_largeur - pl2Dd_ecartement - epaisseur_dessus
	longueurTrait = pl2Dd_tiges
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	dessous=inkex.etree.SubElement(liaison,'g')
	dessus=inkex.etree.SubElement(liaison,'g')

	
	# Dessous ***************************************	
	# rectangle dessous
	rectangleDessous=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangleDessous.set('x',str(-coteDessous*echelle_liaison/2) )
	rectangleDessous.set('y',str(-coteDessous*echelle_liaison/2) )
	rectangleDessous.set('width',str(coteDessous*echelle_liaison))
	rectangleDessous.set('height',str(coteDessous*echelle_liaison))
	rectangleDessous.set('style','fill:white')
	rectangleDessous.set('stroke',couleur_dessous)
	rectangleDessous.set('stroke-width',str(epaisseur_dessous))
	dessous.append(rectangleDessous)

	traitDessous=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(coteDessous/2.	,	0),
				(coteMoyen/2.+longueurTrait	,	0)	])
	traitDessous.set('d',chemin)
	traitDessous.set('stroke',couleur_dessous)
	traitDessous.set('stroke-width',str(epaisseur_dessous))
	dessous.append(traitDessous)
	
	# Dessus ***************************************
	# rectangle dessus
	rectangleDessus=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangleDessus.set('x',str(-coteDessus*echelle_liaison/2) )
	rectangleDessus.set('y',str(-coteDessus*echelle_liaison/2) )
	rectangleDessus.set('width',str(coteDessus*echelle_liaison))
	rectangleDessus.set('height',str(coteDessus*echelle_liaison))
	rectangleDessus.set('style','fill:white')
	rectangleDessus.set('stroke',couleur_dessus)
	rectangleDessus.set('stroke-width',str(epaisseur_dessus))
	dessus.append(rectangleDessus)

	traitDessus=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(coteDessus/2.			,	0),
				(coteMoyen/2.+longueurTrait	,	0)	])
	traitDessus.set('d',chemin)
	traitDessus.set('stroke',couleur_dessus)
	traitDessus.set('stroke-width',str(epaisseur_dessus))
	dessus.append(traitDessus)
	
	# Transformations ***************************************
	dessous.set("transform","rotate("+str(rotationDessous)+")")
	dessus.set("transform","rotate("+str(rotationDessus)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






#===============================================================
def dessin_plane_3D(options,contexte):
	#Origine 2D
	x0=options.x0
	y0=options.y0
	#Base Axonometrique
	echelle_liaison=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques(echelle_liaison)
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x=options.liaison_plane_3D_position_x
	y=options.liaison_plane_3D_position_y
	z=options.liaison_plane_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	largeur=pl3D_largeur
	longueurTige=pl3D_tiges
	ecart=pl3D_ecartement
	couleur_dessus=options.opt_gene_piece1_couleur
	couleur_dessous=options.opt_gene_piece2_couleur
	epaisseur_dessus=options.opt_gene_lignes_epaisseur_1
	epaisseur_dessous=options.opt_gene_lignes_epaisseur_2
	angle_dessus=-float(options.liaison_plane_3D_orientation1)/180.*math.pi
	angle_dessous=-float(options.liaison_plane_3D_orientation2)/180.*math.pi
	#Repere local de la liaison
	if(options.liaison_plane_3D_type_normale=="\"liaison_plane_3D_type_normale_quelconque\""):
		V=v3D(options.liaison_plane_3D_type_direction_quelconque_x,options.liaison_plane_3D_type_direction_quelconque_y,options.liaison_plane_3D_type_direction_quelconque_z,base)
		if V.x == V.y == V.z == 0 : V=v3D(1,0,0,base) #Si vecteur nul : on prend X par defaut
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle_liaison,angle_dessus)#Repere male
		Vx2,Vy2,Vz2=getBaseFromVecteur(V,echelle_liaison,angle_dessous)#Repere Femelle
	else:	#Si vecteur standard
		if(options.liaison_plane_3D_axe=="x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle_liaison,angle_dessus)#Repere dessus
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vx,echelle_liaison,angle_dessous)#Repere dessous
		elif(options.liaison_plane_3D_axe=="y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle_liaison,angle_dessus)#Repere dessus
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vy,echelle_liaison,angle_dessous)#Repere dessous
		else:#z
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle_liaison,angle_dessus)#Repere dessus
			Vx2,Vy2,Vz2=getBaseFromVecteur(Vz,echelle_liaison,angle_dessous)#Repere dessous
	baseLocale1=(Vx1,Vy1,Vz1)
	baseLocale2=(Vx2,Vy2,Vz2)

	# Dessus ***************************************
	planDessus=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					( (ecart+epaisseur_dessus)/2.,	-largeur/2.,	-largeur/2.	),
					( (ecart+epaisseur_dessus)/2.,	-largeur/2.,	largeur/2.	),
					( (ecart+epaisseur_dessus)/2.,	largeur/2.,	largeur/2.	),
					( (ecart+epaisseur_dessus)/2.,	largeur/2.,	-largeur/2.	)
				],True,baseLocale1)
	planDessus.set('d',chemin)
	planDessus.set('stroke',couleur_dessus)
	planDessus.set('stroke-width',str(epaisseur_dessus))
	planDessus.set('style','fill:white')
	planDessus.set('profondeur',str(profondeur))
	

	tigeDessus=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					( (ecart+epaisseur_dessus)/2.,	0.,	0.	),
					( ecart/2.+longueurTige,	0.,	0.	)
				],False,baseLocale1)
	tigeDessus.set('d',chemin)
	tigeDessus.set('stroke',couleur_dessus)
	tigeDessus.set('stroke-width',str(epaisseur_dessus))
	tigeDessus.set('style','stroke-linecap:round')
	tigeDessus.set('profondeur',str(profondeur))
	
	# Dessous ***************************************
	planDessous=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(-(ecart+epaisseur_dessous)/2.,	-largeur/2.,	-largeur/2.	),
					(-(ecart+epaisseur_dessous)/2.,	-largeur/2.,	largeur/2.	),
					(-(ecart+epaisseur_dessous)/2.,	largeur/2.,	largeur/2.	),
					(-(ecart+epaisseur_dessous)/2.,	largeur/2.,	-largeur/2.	)
				],True,baseLocale2)
	planDessous.set('d',chemin)
	planDessous.set('stroke',couleur_dessous)
	planDessous.set('stroke-width',str(epaisseur_dessous))
	planDessous.set('style','fill:white')
	planDessous.set('profondeur',str(profondeur))

	tigeDessous=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
						(-(ecart+epaisseur_dessous)/2.,	0.,	0.	),
						(-ecart/2.-longueurTige,	0.,	0.	)
				],False,baseLocale2)
	tigeDessous.set('d',chemin)
	tigeDessous.set('stroke',couleur_dessous)
	tigeDessous.set('stroke-width',str(epaisseur_dessous))
	tigeDessous.set('style','stroke-linecap:round')
	tigeDessous.set('profondeur',str(profondeur))
	


	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        listeObjets=[planDessous,tigeDessous,planDessus,tigeDessus]
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)
        
        
	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	

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
	rayon_tige = s2D_rayon_tiges
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
					(rayon_tige	,	0.)	]
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
					(rayon_tige	,	0.)	]
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
        liaison = inkex.etree.SubElement(contexte, 'g')
        fond_femelle = inkex.etree.SubElement(liaison,'g')
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
	rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-h2Dc_longueur*echelle_liaison/2) )
	rectangle.set('y',str(-h2Dc_diametre*echelle_liaison/2) )
	rectangle.set('width',str(h2Dc_longueur*echelle_liaison))
	rectangle.set('height',str(h2Dc_diametre*echelle_liaison))
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
	
	# Fond de femelle opaque ****************************
	#Rectangle - fond
	rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-h2Dc_longueur*echelle_liaison/2) )
	rectangle.set('y',str(-h2Dc_diametre*echelle_liaison/2) )
	rectangle.set('width',str(h2Dc_longueur*echelle_liaison))
	rectangle.set('height',str(h2Dc_diametre*echelle_liaison))
	rectangle.set('style','fill:white')
	fond_femelle.append(rectangle)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(-rotation)+")")
	femelle.set("transform","rotate("+str(-rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
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
        liaison = inkex.etree.SubElement(contexte, 'g')
	femelle=inkex.etree.SubElement(liaison,'g')
	male=inkex.etree.SubElement(liaison,'g')

	# Femelle ***************************************	
	#axe
	axe2=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0			,	0),
					(longueur_tige + rayon	,	0)	]
				,False,base2D)	
	axe2.set('d',chemin)
	axe2.set('stroke',couleur_femelle)
	axe2.set('stroke-width',str(epaisseur_femelle))
	femelle.append(axe2)
	#cercle
	cercle=inkex.etree.Element(inkex.addNS('circle','svg'))
	cercle.set('cx',"0")
	cercle.set('cy',"0")
	cercle.set('r',str(rayon*echelle_liaison))
	cercle.set('stroke',str(couleur_femelle))
	cercle.set('stroke-width',str(epaisseur_femelle))
	cercle.set('style','fill:white')
	femelle.append(cercle)
	
	# Male ***************************************
	axe1=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(rayon_filet		,	0),
					(longueur_tige + rayon	,	0)	]
				,False,base2D)
	axe1.set('d',chemin)
	axe1.set('stroke',couleur_male)
	axe1.set('stroke-width',str(epaisseur_male))
	axe1.set('style','stroke-linecap:round')
	male.append(axe1)
	
	pasVis=inkex.etree.Element(inkex.addNS('path','svg'))
	cheminVis="M "+str(rayon_filet*echelle_liaison)+",0 A "+str(rayon_filet*echelle_liaison)+" "+str(rayon_filet*echelle_liaison)+" 0 0 "+str(1-int(pas_a_gauche))+" -"+str(rayon_filet*echelle_liaison)+",0"
	pasVis.set('d',cheminVis)
	pasVis.set('stroke',couleur_male)
	pasVis.set('stroke-width',str(epaisseur_male))
	pasVis.set('style','fill:none;stroke-linecap:round')
	male.append(pasVis)


	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation1)+")")
	femelle.set("transform","rotate("+str(rotation2)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
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
	if(options.liaison_helicoidale_3D_type_direction=="\"liaison_helicoidale_3D_type_direction_quelconque\""):
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

	
	helice1=inkex.etree.Element(inkex.addNS('path','svg'))
#	cheminHelice1,profondeurHelice1=points3D_to_svgd(listeHelice1,False)
	helice1.set('d',cheminHelice1)
	helice1.set('stroke',couleur_male)
	helice1.set('stroke-width',str(epaisseur_male))
	helice1.set('style','stroke-linecap:round')
	helice1.set('style','fill:none')
	helice1.set('profondeur',str(profondeurHelice1))
	
	helice2=inkex.etree.Element(inkex.addNS('path','svg'))
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
	demiCylindre1=inkex.etree.Element(inkex.addNS('path','svg'))
	demiCylindre1.set('d',chemin)
	demiCylindre1.set('stroke',couleur_femelle)
	demiCylindre1.set('stroke-width',str(epaisseur_femelle))
	demiCylindre1.set('style','stroke-linecap:round')
	demiCylindre1.set('style','fill:white')
	demiCylindre1.set('profondeur',str(profondeurDemiCylindre1*0.001))
	
	demiCylindreContours1=inkex.etree.Element(inkex.addNS('path','svg'))
	demiCylindreContours1.set('d',chemin)
	demiCylindreContours1.set('stroke',couleur_femelle)
	demiCylindreContours1.set('stroke-width',str(epaisseur_femelle))
	demiCylindreContours1.set('style','stroke-linecap:round')
	demiCylindreContours1.set('style','fill:none')
	demiCylindreContours1.set('profondeur',str(profondeurDemiCylindre1*100000))
	
	chemin,profondeurDemiCylindre2=points3D_to_svgd(listeDemiCylindre2,True)
	demiCylindre2=inkex.etree.Element(inkex.addNS('path','svg'))
	demiCylindre2.set('d',chemin)
	demiCylindre2.set('stroke',couleur_femelle)
	demiCylindre2.set('stroke-width',str(epaisseur_femelle))
	demiCylindre2.set('style','stroke-linecap:round')
	demiCylindre2.set('style','fill:white')
	demiCylindre2.set('profondeur',str(profondeurDemiCylindre2*0.001))
	
	demiCylindreContours2=inkex.etree.Element(inkex.addNS('path','svg'))
	demiCylindreContours2.set('d',chemin)
	demiCylindreContours2.set('stroke',couleur_femelle)
	demiCylindreContours2.set('stroke-width',str(epaisseur_femelle))
	demiCylindreContours2.set('style','stroke-linecap:round')
	demiCylindreContours2.set('style','fill:none')
	demiCylindreContours2.set('profondeur',str(profondeurDemiCylindre2*100000))
	
	
	
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
        
        listeObjets=[axe,demiCylindre1,demiCylindreContours1,demiCylindre2,demiCylindreContours2,barreFemelle,helice1,helice2]
        
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)

	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	
 

def dessin_sphere_plan_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_sphere_plan_2D_cote_x
	y = -options.liaison_sphere_plan_2D_cote_y
	#Orientation **************************************
	rotation_normale=options.liaison_sphere_plan_2D_cote_orientation_normale #Angle par defaut (sens trigo)
	if(options.liaison_sphere_plan_2D_cote_axe_normale=="y"):
		rotation_normale=90
	elif(options.liaison_sphere_plan_2D_cote_axe_normale=="x"):
		rotation_normale=0
	elif(options.liaison_sphere_plan_2D_cote_axe_normale=="-x"):
		rotation_normale=180
	elif(options.liaison_sphere_plan_2D_cote_axe_normale=="-y"):
		rotation_normale=-90
	rotation_sphere=options.liaison_sphere_plan_2D_cote_orientation_sphere #Angle par defaut (sens trigo)
	if(options.liaison_sphere_plan_2D_cote_axe_sphere=="y"):
		rotation_sphere=90
	elif(options.liaison_sphere_plan_2D_cote_axe_sphere=="x"):
		rotation_sphere=0
	elif(options.liaison_sphere_plan_2D_cote_axe_sphere=="-x"):
		rotation_sphere=180
	elif(options.liaison_sphere_plan_2D_cote_axe_sphere=="-y"):
		rotation_sphere=-90
	elif(options.liaison_sphere_plan_2D_cote_axe_sphere=="normale"):
		rotation_sphere=rotation_normale
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle,rotation_normale*math.pi/180)
	Vx2,Vy2=getBase2D(echelle,rotation_sphere*math.pi/180)
	base2D_1=(Vx1,Vy1)
	base2D_2=(Vx2,Vy2)
	#Parametres ****************************
	couleur_sphere=options.opt_gene_piece2_couleur
	couleur_plan=options.opt_gene_piece1_couleur
	epaisseur_sphere=options.opt_gene_lignes_epaisseur_2
	epaisseur_plan=options.opt_gene_lignes_epaisseur_1
	old_liaisons=options.opt_gene_gene_old
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	sphere=inkex.etree.SubElement(liaison,'g')
	plan=inkex.etree.SubElement(liaison,'g')

	
	# PLAN ***************************************
	#plan dessus
	plan_plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-epaisseur_plan/2.,	-sp2Dc_largeur_plan/2.),
					(-epaisseur_plan/2.,	sp2Dc_largeur_plan/2)	],
				False,
				base2D_1)
	plan_plan.set('d',chemin)
	plan_plan.set('stroke',couleur_plan)
	plan_plan.set('stroke-width',str(epaisseur_plan))
	plan.append(plan_plan)
	
	#tige
	tige_plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-epaisseur_plan/2.				,	0),
					(-epaisseur_plan/2.-sp2Dc_longueur_tige_plan	,	0)	],
				False,
				base2D_1)
	tige_plan.set('d',chemin)
	tige_plan.set('stroke',couleur_plan)
	tige_plan.set('stroke-width',str(epaisseur_plan))
	plan.append(tige_plan)
	
	# SPHERE ***************************************
	#Sphere
	if not old_liaisons:
		sphere_bout=inkex.etree.Element(inkex.addNS('circle','svg'))
		sphere_bout.set('cx',str((echelle*sp2Dc_diametre_sphere/2.+epaisseur_sphere/2.)*math.cos(-rotation_normale*math.pi/180)))
		sphere_bout.set('cy',str((echelle*sp2Dc_diametre_sphere/2.+epaisseur_sphere/2.)*math.sin(-rotation_normale*math.pi/180)))
		sphere_bout.set('r',str(sp2Dc_diametre_sphere/2.*echelle))
		sphere_bout.set('style','fill:white')
	else :
		sphere_bout=inkex.etree.Element(inkex.addNS('path','svg'))
		chemin=points_to_svgd([	(0	,	0),
					(sp2DcOLD_largeur_fleche*(math.sqrt(3)/2*Vx2.x+0.5*Vy2.x)	,	sp2DcOLD_largeur_fleche*(math.sqrt(3)/2*Vx2.y+0.5*Vy2.y)),
					(sp2DcOLD_largeur_fleche*(math.sqrt(3)/2*Vx2.x-0.5*Vy2.x)	,	sp2DcOLD_largeur_fleche*(math.sqrt(3)/2*Vx2.y-0.5*Vy2.y)), 	])
		sphere_bout.set('d',chemin)
		sphere_bout.set('style','fill:'+couleur_sphere)
	sphere_bout.set('stroke',couleur_sphere)
	sphere_bout.set('stroke-width',str(epaisseur_sphere))
	sphere.append(sphere_bout)
	
	#tige
	sphere_tige=inkex.etree.Element(inkex.addNS('path','svg'))
	if not old_liaisons:
		chemin=points_to_svgd([	(sp2Dc_diametre_sphere/2.*(Vx1.x+Vx2.x) + epaisseur_sphere/2.*Vx1.x					,	sp2Dc_diametre_sphere/2.*(Vx1.y+Vx2.y) + epaisseur_sphere/2.*Vx1.y),
					(sp2Dc_diametre_sphere/2.*(Vx1.x+Vx2.x) + sp2Dc_longueur_tige_sphere*Vx2.x + epaisseur_sphere/2.*Vx1.x	,	sp2Dc_diametre_sphere/2.*(Vx1.y+Vx2.y) + sp2Dc_longueur_tige_sphere*Vy2.x + epaisseur_sphere/2.*Vx1.y)	])
	else:
		chemin=points_to_svgd([	(sp2DcOLD_largeur_fleche*math.sqrt(3)/2.*Vx2.x	,	sp2DcOLD_largeur_fleche*math.sqrt(3)/2.*Vx2.y),
					((sp2DcOLD_largeur_fleche+sp2Dc_longueur_tige_sphere)*Vx2.x	,	(sp2DcOLD_largeur_fleche+sp2Dc_longueur_tige_sphere)*Vx2.y)	])
	sphere_tige.set('d',chemin)
	sphere_tige.set('stroke',couleur_sphere)
	sphere_tige.set('stroke-width',str(epaisseur_sphere))
	sphere.append(sphere_tige)
	
	# Transformations ***************************************
	#dessus.set("transform","rotate("+str(rotation)+")")
	#dessous.set("transform","rotate("+str(rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)





def dessin_sphere_plan_2D_dessus(options,contexte):
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_sphere_plan_2D_dessus_x
	y = -options.liaison_sphere_plan_2D_dessus_y
	#Orientation **************************************
	rotationPlan=-options.liaison_sphere_plan_2D_dessus_orientation_plan #Angle par defaut (sens trigo)
	if(options.liaison_sphere_plan_2D_dessus_axe_plan=="x"):
		rotationPlan=0
	elif(options.liaison_sphere_plan_2D_dessus_axe_plan=="y"):
		rotationPlan=-90
	elif(options.liaison_sphere_plan_2D_dessus_axe_plan=="-x"):
		rotationPlan=180
	elif(options.liaison_sphere_plan_2D_dessus_axe_plan=="-y"):
		rotationPlan=90
	rotationSphere=-options.liaison_sphere_plan_2D_dessus_orientation_sphere #Angle par defaut (sens trigo)
	if(options.liaison_sphere_plan_2D_dessus_axe_sphere=="x"):
		rotationSphere=0
	elif(options.liaison_sphere_plan_2D_dessus_axe_sphere=="y"):
		rotationSphere=-90
	elif(options.liaison_sphere_plan_2D_dessus_axe_sphere=="-x"):
		rotationSphere=180
	elif(options.liaison_sphere_plan_2D_dessus_axe_sphere=="-y"):
		rotationSphere=90
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_femelle=options.opt_gene_lignes_epaisseur_2
	epaisseur_male=options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	groupe_plan=inkex.etree.SubElement(liaison,'g')
	groupe_sphere=inkex.etree.SubElement(liaison,'g')

	
	# Plan ***************************************	
	# rectangle 
	plan=inkex.etree.Element(inkex.addNS('rect','svg'))
	plan.set('x',str(-sp2Dd_largeur*echelle/2) )
	plan.set('y',str(-sp2Dd_largeur*echelle/2) )
	plan.set('width',str(sp2Dd_largeur*echelle))
	plan.set('height',str(sp2Dd_largeur*echelle))
	plan.set('style','fill:white')
	plan.set('stroke',couleur_femelle)
	plan.set('stroke-width',str(epaisseur_femelle))
	groupe_plan.append(plan)
	#trait
	traitPlan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(sp2Dd_largeur/2.*echelle	,	0),
				((sp2Dd_largeur/2.+sp2Dd_longueur_tige_plan)*echelle	,	0)	])
	traitPlan.set('d',chemin)
	traitPlan.set('stroke',couleur_femelle)
	traitPlan.set('stroke-width',str(epaisseur_femelle))
	groupe_plan.append(traitPlan)
	
	# sphere ***************************************
	# sphere
	sphere=inkex.etree.Element(inkex.addNS('circle','svg'))
	sphere.set('cx','0')
	sphere.set('cy','0')
	sphere.set('r',str(sp2Dd_diametre_sphere/2.*echelle))
	sphere.set('style','fill:white')
	sphere.set('stroke',couleur_male)
	sphere.set('stroke-width',str(epaisseur_male))
	groupe_sphere.append(sphere)

	
	#trait
	traitSphere=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(sp2Dd_diametre_sphere/2.*echelle	,0),
				((sp2Dd_diametre_sphere/2.+sp2Dd_longueur_tige_sphere)*echelle	,0)	])
	traitSphere.set('d',chemin)
	traitSphere.set('stroke',couleur_male)
	traitSphere.set('stroke-width',str(epaisseur_male))
	groupe_sphere.append(traitSphere)
	
	# Transformations ***************************************
	groupe_plan.set("transform","rotate("+str(rotationPlan)+")")
	groupe_sphere.set("transform","rotate("+str(rotationSphere)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






#===============================================================
def dessin_sphere_plan_3D(options,contexte):
	#Origine 2D
	x0=options.x0
	y0=options.y0
	#Base Axonometrique
	echelle=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques(echelle)
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x=options.liaison_sphere_plan_3D_position_x
	y=options.liaison_sphere_plan_3D_position_y
	z=options.liaison_sphere_plan_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	couleur_plan=options.opt_gene_piece1_couleur
	couleur_sphere=options.opt_gene_piece2_couleur
	epaisseur_plan=options.opt_gene_lignes_epaisseur_1
	epaisseur_sphere=options.opt_gene_lignes_epaisseur_2
	angle_plan=-float(options.liaison_sphere_plan_3D_rotation_plan)/180.*math.pi
	#Repere local de la liaison
	#Plan
	if(options.liaison_sphere_plan_3D_type_normale=="\"liaison_sphere_plan_3D_type_normale_quelconque\""):
		V=v3D(options.liaison_sphere_plan_3D_normale_quelconque_x,options.liaison_sphere_plan_3D_normale_quelconque_y,options.liaison_sphere_plan_3D_normale_quelconque_z,base)
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle,angle_plan)#Repere plan
	else:	#Si vecteur standard
		if options.liaison_plane_3D_axe == "x" :
			Vx1,Vy1,Vz1 = getBaseFromVecteur(Vx, echelle, angle_plan)
		elif options.liaison_plane_3D_axe == "-x" :
			Vx1,Vy1,Vz1 = getBaseFromVecteur(-Vx, echelle, angle_plan)
		elif options.liaison_plane_3D_axe == "y" :
			Vx1,Vy1,Vz1 = getBaseFromVecteur(Vy, echelle, angle_plan)
		elif options.liaison_plane_3D_axe == "-y" :
			Vx1,Vy1,Vz1 = getBaseFromVecteur(-Vy, echelle, angle_plan)
		elif options.liaison_plane_3D_axe == "z" :
			Vx1,Vy1,Vz1 = getBaseFromVecteur(Vz, echelle, angle_plan)
		else:#z
			Vx1,Vy1,Vz1 = getBaseFromVecteur(-Vz, echelle, angle_plan)
	baseLocale1=(Vx1,Vy1,Vz1)
	#Sphère
	if(options.liaison_sphere_plan_3D_type_direction_sphere=="\"liaison_sphere_plan_3D_type_direction_sphere_quelconque\""):
		V=v3D(options.liaison_sphere_plan_3D_direction_sphere_quelconque_x,options.liaison_sphere_plan_3D_direction_sphere_quelconque_y,options.liaison_sphere_plan_3D_direction_sphere_quelconque_z,base)
		Vx2,Vy2,Vz2=getBaseFromVecteur(V,echelle,angle_plan)#Repere plan
	else:	#Si vecteur standard
		if options.liaison_sphere_plan_3D_axe_sphere == "normale" :
			Vx2,Vy2,Vz2 = Vx1,Vy1,Vz1
		elif options.liaison_sphere_plan_3D_axe_sphere == "x" :
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vx, echelle)
		elif options.liaison_sphere_plan_3D_axe_sphere == "-x" :
			Vx2,Vy2,Vz2 = getBaseFromVecteur(-Vx, echelle)
		elif options.liaison_sphere_plan_3D_axe_sphere == "y" :
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vy, echelle)
		elif options.liaison_sphere_plan_3D_axe_sphere == "-y":
			Vx2,Vy2,Vz2 = getBaseFromVecteur(-Vy, echelle)
		elif options.liaison_sphere_plan_3D_axe_sphere == "z" :
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vz, echelle)
		else :
			Vx2,Vy2,Vz2 = getBaseFromVecteur(-Vz, echelle)
	baseLocale2=(Vx2,Vy2,Vz2)

	# Plan ***************************************
	plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	-sp3D_largeur/2.,	-sp3D_largeur/2.	),
					(0,	-sp3D_largeur/2.,	sp3D_largeur/2.	),
					(0,	sp3D_largeur/2.,	sp3D_largeur/2.	),
					(0,	sp3D_largeur/2.,	-sp3D_largeur/2.	)
				],True,baseLocale1)
	plan.set('d',chemin)
	plan.set('stroke',couleur_plan)
	plan.set('stroke-width',str(epaisseur_plan))
	plan.set('style','fill:white')
	plan.set('profondeur',str(profondeur))
	

	tigePlan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
						(0,				0.,	0.	),
						(-sp3D_longueur_tige_plan,	0.,	0.	)
				],False,baseLocale1)
	tigePlan.set('d',chemin)
	tigePlan.set('stroke',couleur_plan)
	tigePlan.set('stroke-width',str(epaisseur_plan))
	tigePlan.set('style','stroke-linecap:round')
	tigePlan.set('profondeur',str(profondeur))
	
	# Sphère ***************************************
	Vcentre = Vx1 * sp3D_diametre_sphere / 2.
	
	sphere=inkex.etree.Element(inkex.addNS('circle','svg'))
	sphere.set('cx', str(Vx1.x*sp3D_diametre_sphere/2.))
	sphere.set('cy', str(Vx1.y*sp3D_diametre_sphere/2.))
	sphere.set('r',str(sp3D_diametre_sphere/2.*echelle))
	sphere.set('style','fill:white')
	sphere.set('stroke',couleur_sphere)
	sphere.set('stroke-width',str(epaisseur_sphere))
	sphere.set('profondeur',str(Vx1.z))


	tigeSphere=inkex.etree.Element(inkex.addNS('path','svg'))
	P1=(Vx1+Vx2) * sp3D_diametre_sphere/2.
	P2=(Vx1+Vx2) * sp3D_diametre_sphere/2. + Vx2*sp3D_longueur_tige_sphere
	chemin,profondeur=points3D_to_svgd([
					(P1.x,	P1.y,	P1.z	),
					(P2.x,	P2.y,	P2.z	)
				],False)
	tigeSphere.set('d',chemin)
	tigeSphere.set('stroke',couleur_sphere)
	tigeSphere.set('stroke-width',str(epaisseur_sphere))
	tigeSphere.set('style','stroke-linecap:round')
	tigeSphere.set('profondeur',str(profondeur))
	


	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        listeObjets=[sphere,tigeSphere,plan,tigePlan]
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)
        
        
	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	

def dessin_rectiligne_plan_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_rectiligne_2D_cote_x
	y = -options.liaison_rectiligne_2D_cote_y
	#Orientation **************************************
	rotation=-options.liaison_rectiligne_2D_cote_orientation_normale #Angle par defaut (sens trigo)
	if(options.liaison_rectiligne_cote_axe_normale=="y"):
		rotation=-90
	elif(options.liaison_rectiligne_cote_axe_normale=="x"):
		rotation=0
	elif(options.liaison_rectiligne_cote_axe_normale=="-x"):
		rotation=180
	elif(options.liaison_rectiligne_cote_axe_normale=="-y"):
		rotation=90
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	couleur_femelle=options.opt_gene_piece2_couleur
	couleur_male=options.opt_gene_piece1_couleur
	epaisseur_plan=options.opt_gene_lignes_epaisseur_2
	epaisseur_prisme=options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	dessus=inkex.etree.SubElement(liaison,'g')
	dessous=inkex.etree.SubElement(liaison,'g')

	
	# DESSUS ***************************************
	# Prisme
	prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(epaisseur_prisme/2.			,	-r2Dc_longueur_contact/2.),
				(epaisseur_prisme/2.			,	r2Dc_longueur_contact/2.),
				(r2Dc_hauteur_prisme + epaisseur_prisme/2.,	r2Dc_longueur_base_prisme/2.),
				(r2Dc_hauteur_prisme + epaisseur_prisme/2.,	-r2Dc_longueur_base_prisme/2.)	],
				True)
	prisme.set('d',chemin)
	prisme.set('stroke',couleur_male)
	prisme.set('style','fill:white')
	prisme.set('stroke-width',str(epaisseur_prisme))
	dessus.append(prisme)
	
	#tige dessus
	tigeDessus=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(r2Dc_hauteur_prisme+epaisseur_prisme/2.					,	0.),
				(r2Dc_hauteur_prisme + r2Dc_longueur_tige_prisme + epaisseur_prisme/2.	,	0.)	])
	tigeDessus.set('d',chemin)
	tigeDessus.set('stroke',couleur_male)
	tigeDessus.set('stroke-width',str(epaisseur_prisme))
	dessus.append(tigeDessus)
	
	# DESSOUS ***************************************
	#plan dessous
	plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-epaisseur_plan/2.	,	-r2Dc_longueur_plan/2.),
				(-epaisseur_plan/2.	,	r2Dc_longueur_plan/2.)	])
	plan.set('d',chemin)
	plan.set('stroke',couleur_femelle)
	plan.set('stroke-width',str(epaisseur_plan))
	dessous.append(plan)
	
	#tige dessous
	tigePlan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-epaisseur_plan/2.,					0.),
				(-r2Dc_longueur_tige_plan-epaisseur_plan/2.,	0.)	])
	tigePlan.set('d',chemin)
	tigePlan.set('stroke',couleur_femelle)
	tigePlan.set('stroke-width',str(epaisseur_plan))
	dessous.append(tigePlan)
	
	# Transformations ***************************************
	dessus.set("transform","rotate("+str(rotation)+")")
	dessous.set("transform","rotate("+str(rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	

def dessin_rectiligne_2D_bout(options,contexte):
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_rectiligne_2D_bout_x
	y = -options.liaison_rectiligne_2D_bout_y
	#Orientation **************************************
	rotationNormale=-options.liaison_rectiligne_2D_bout_orientation_normale #Angle par defaut (sens trigo)
	if(options.liaison_rectiligne_bout_axe_normale=="x"):
		rotationNormale = 0
	elif(options.liaison_rectiligne_bout_axe_normale=="y"):
		rotationNormale = -90
	elif(options.liaison_rectiligne_bout_axe_normale=="-x"):
		rotationNormale = 180
	elif(options.liaison_rectiligne_bout_axe_normale=="-y"):
		rotationNormale = 90
	rotationPrisme=-options.liaison_rectiligne_2D_bout_orientation_prisme #Angle par defaut (sens trigo)
	if(options.liaison_rectiligne_bout_axe_prisme=="normale"):
		rotationPrisme = rotationNormale
	elif(options.liaison_rectiligne_bout_axe_prisme=="x"):
		rotationPrisme = 0
	elif(options.liaison_rectiligne_bout_axe_prisme=="y"):
		rotationPrisme = -90
	elif(options.liaison_rectiligne_bout_axe_prisme=="-x"):
		rotationPrisme = 180
	elif(options.liaison_rectiligne_bout_axe_prisme=="-y"):
		rotationPrisme = 90
	#Base *********************
	echelle = options.echelle
	Vx1,Vy1 = getBase2D(echelle)
	base2D = (Vx1,Vy1)
	#Parametres ****************************
	couleur_plan = options.opt_gene_piece2_couleur
	couleur_prisme = options.opt_gene_piece1_couleur
	epaisseur_plan = options.opt_gene_lignes_epaisseur_2
	epaisseur_prisme = options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	prisme = inkex.etree.SubElement(liaison,'g')
	plan = inkex.etree.SubElement(liaison,'g')

	
	# Plan ***************************************	
	# plan
	trait_plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-epaisseur_plan/2.	,	-r2Db_largeur_plan/2.),
				(-epaisseur_plan/2.	,	r2Db_largeur_plan/2.)	])
	trait_plan.set('d',chemin)
	trait_plan.set('stroke',couleur_plan)
	trait_plan.set('stroke-width',str(epaisseur_plan))
	plan.append(trait_plan)
	# tige
	tige_plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-r2Db_longueur_tige_plan	,	0),
				(-epaisseur_plan/2.		,	0)	])
	tige_plan.set('d',chemin)
	tige_plan.set('stroke',couleur_plan)
	tige_plan.set('stroke-width',str(epaisseur_plan))
	plan.append(tige_plan)
	
	# prisme ***************************************
	# triangle
	deport_point_fleche = epaisseur_prisme/2. / math.sin( math.atan((r2Db_largeur_prisme/2.)/(r2Db_hauteur_prisme)) )
	triangle=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(deport_point_fleche			,	0),
				(r2Db_hauteur_prisme+deport_point_fleche	,	r2Db_largeur_prisme/2.),
				(r2Db_hauteur_prisme+deport_point_fleche	,	-r2Db_largeur_prisme/2.)	],
				True)
	triangle.set('d',chemin)
	triangle.set('stroke',couleur_prisme)
	triangle.set('stroke-width',str(epaisseur_prisme))
	triangle.set('style','fill:white')
	prisme.append(triangle)

	trait_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(r2Db_hauteur_prisme+deport_point_fleche				,	0),
				(r2Db_hauteur_prisme+r2Db_longueur_tige_prisme+deport_point_fleche	,	0)	])
	trait_prisme.set('d',chemin)
	trait_prisme.set('stroke',couleur_prisme)
	trait_prisme.set('stroke-width',str(epaisseur_prisme))
	prisme.append(trait_prisme)
	
	# Transformations ***************************************
	plan.set("transform","rotate("+str(rotationNormale)+")")
	prisme.set("transform","rotate("+str(rotationPrisme)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






#===============================================================
def dessin_rectiligne_3D(options,contexte):
	#Origine 2D
	x0=options.x0
	y0=options.y0
	#Base Axonometrique
	echelle=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques(echelle)
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x=options.liaison_rectiligne_3D_position_x
	y=options.liaison_rectiligne_3D_position_y
	z=options.liaison_rectiligne_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	inclinaison = options.liaison_rectiligne_3D_inclinaison_prisme/180.*math.pi
	couleur_plan = options.opt_gene_piece1_couleur
	couleur_dessous = options.opt_gene_piece2_couleur
	epaisseur_plan = options.opt_gene_lignes_epaisseur_1
	epaisseur_dessous = options.opt_gene_lignes_epaisseur_2
	#angle_inclinaison_prisme = -float(options.liaison_rectiligne_3D_inclinaison_prisme)/180.*math.pi
	#Repere local de la liaison
	if(options.liaison_rectiligne_3D_type_normale!="\"liaison_rectiligne_3D_type_normale_standard\""):
		Vn = v3D(options.liaison_rectiligne_3D_normale_quelconque_x, options.liaison_rectiligne_3D_normale_quelconque_y, options.liaison_rectiligne_3D_normale_quelconque_z,base)
	else:	#Si vecteur standard
		if(options.liaison_rectiligne_3D_axe_normale=="x"):
			Vn = v3D(1, 0, 0, base)
		elif(options.liaison_rectiligne_3D_axe_normale=="y"):
			Vn = v3D(0, 1, 0, base)
		elif(options.liaison_rectiligne_3D_axe_normale=="z"):
			Vn = v3D(0, 0, 1, base)
		elif(options.liaison_rectiligne_3D_axe_normale=="-x"):
			Vn = v3D(-1, 0, 0, base)
		elif(options.liaison_rectiligne_3D_axe_normale=="-y"):
			Vn = v3D(0, -1, 0, base)
		elif(options.liaison_rectiligne_3D_axe_normale=="-z"):
			Vn = v3D(0, 0, -1, base)
	if(options.liaison_rectiligne_3D_type_direction!="\"liaison_rectiligne_3D_type_direction_standard\""):
		Vd = v3D(options.liaison_rectiligne_3D_direction_quelconque_x, options.liaison_rectiligne_3D_direction_quelconque_y, options.liaison_rectiligne_3D_direction_quelconque_z,base)
	else:
		if(options.liaison_rectiligne_3D_axe_direction=="x"):
			Vd = v3D(1, 0, 0, base)
		elif(options.liaison_rectiligne_3D_axe_direction=="y"):
			Vd = v3D(0, 1, 0, base)
		elif(options.liaison_rectiligne_3D_axe_direction=="z"):
			Vd = v3D(0, 0, 1, base)
		elif(options.liaison_rectiligne_3D_axe_direction=="-x"):
			Vd = v3D(-1, 0, 0, base)
		elif(options.liaison_rectiligne_3D_axe_direction=="-y"):
			Vd = v3D(0, -1, 0, base)
		elif(options.liaison_rectiligne_3D_axe_direction=="-z"):
			Vd = v3D(0, 0, -1, base)
	#============================================
	Vn.normalise()
	Vx1 = Vn
	Vy1 = Vd - (Vd * Vn) * Vn
	Vy1.normalise()
	Vz1 = Vx1 ^Vy1
	
	Vx2 = Vx1*math.cos(inclinaison) + Vz1*math.sin(inclinaison)
	Vy2 = Vy1
	Vz2 = Vx2 ^Vy2
	
	baseLocale1=(Vx1,Vy1,Vz1)
	baseLocale2=(Vx2,Vy2,Vz2)

	# plan ***************************************
	plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	-r3D_longueur_plan/2.,	-r3D_largeur_plan/2.	),
					(0,	-r3D_longueur_plan/2.,	r3D_largeur_plan/2.	),
					(0,	r3D_longueur_plan/2.,	r3D_largeur_plan/2.	),
					(0,	r3D_longueur_plan/2.,	-r3D_largeur_plan/2.	)
				],True,baseLocale1)
	plan.set('d',chemin)
	plan.set('stroke',couleur_plan)
	plan.set('stroke-width',str(epaisseur_plan))
	plan.set('profondeur',str(profondeur))
	plan.set('style','fill:white;stroke-linejoin:round')
	

	tige_plan=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,				0.,	0.	),
					(-r3D_longueur_tige_plan,	0.,	0.	)
				],False,baseLocale1)
	tige_plan.set('d',chemin)
	tige_plan.set('stroke',couleur_plan)
	tige_plan.set('stroke-width',str(epaisseur_plan))
	tige_plan.set('style','stroke-linecap:round')
	tige_plan.set('profondeur',str(profondeur))
	
	# Prisme ***************************************
	base_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(r3D_hauteur_prisme,	-r3D_longueur_base_prisme/2.,	-r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	-r3D_longueur_base_prisme/2.,	r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	r3D_longueur_base_prisme/2.,	r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	r3D_longueur_base_prisme/2.,	-r3D_largeur_base_prisme/2.	)
				],True,baseLocale2)
	base_prisme.set('d',chemin)
	base_prisme.set('stroke',couleur_dessous)
	base_prisme.set('stroke-width',str(epaisseur_dessous))
	base_prisme.set('style','fill:white;stroke-linejoin:round')
	base_prisme.set('profondeur',str(profondeur))
	profondeur_base = profondeur
	
	
	flanc1_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	-r3D_longueur_contact/2.,	0	),
					(0,	r3D_longueur_contact/2.,	0	),
					(r3D_hauteur_prisme,	r3D_longueur_base_prisme/2.,	-r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	-r3D_longueur_base_prisme/2.,	-r3D_largeur_base_prisme/2.	)
				],True,baseLocale2)
	flanc1_prisme.set('d',chemin)
	flanc1_prisme.set('stroke',couleur_dessous)
	flanc1_prisme.set('stroke-width',str(epaisseur_dessous))
	flanc1_prisme.set('style','fill:white;stroke-linejoin:round')
	flanc1_prisme.set('profondeur',str(profondeur_base*0.999+profondeur*0.001))
	
	
	flanc2_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	-r3D_longueur_contact/2.,	0	),
					(0,	r3D_longueur_contact/2.,	0	),
					(r3D_hauteur_prisme,	r3D_longueur_base_prisme/2.,	r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	-r3D_longueur_base_prisme/2.,	r3D_largeur_base_prisme/2.	)
				],True,baseLocale2)
	flanc2_prisme.set('d',chemin)
	flanc2_prisme.set('stroke',couleur_dessous)
	flanc2_prisme.set('stroke-width',str(epaisseur_dessous))
	flanc2_prisme.set('style','fill:white;stroke-linejoin:round')
	flanc2_prisme.set('profondeur',str(profondeur_base*0.999+profondeur*0.001))
	
	
	bout1_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	r3D_longueur_contact/2.,	0	),
					(r3D_hauteur_prisme,	r3D_longueur_base_prisme/2.,	r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	r3D_longueur_base_prisme/2.,	-r3D_largeur_base_prisme/2.	)
				],True,baseLocale2)
	bout1_prisme.set('d',chemin)
	bout1_prisme.set('stroke',couleur_dessous)
	bout1_prisme.set('stroke-width',str(epaisseur_dessous))
	bout1_prisme.set('style','fill:white;stroke-linejoin:round')
	bout1_prisme.set('profondeur',str(profondeur_base*0.999+profondeur*0.001))
	
	
	bout2_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	-r3D_longueur_contact/2.,	0	),
					(r3D_hauteur_prisme,	-r3D_longueur_base_prisme/2.,	r3D_largeur_base_prisme/2.	),
					(r3D_hauteur_prisme,	-r3D_longueur_base_prisme/2.,	-r3D_largeur_base_prisme/2.	)
				],True,baseLocale2)
	bout2_prisme.set('d',chemin)
	bout2_prisme.set('stroke',couleur_dessous)
	bout2_prisme.set('stroke-width',str(epaisseur_dessous))
	bout2_prisme.set('style','fill:white;stroke-linejoin:round')
	bout2_prisme.set('profondeur',str(profondeur_base*0.999+profondeur*0.001))
	



	tige_prisme=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(r3D_hauteur_prisme,	0.,	0.	),
					(r3D_hauteur_prisme+r3D_longueur_tige_prisme,	0.,	0.	)
				],False,baseLocale2)
	tige_prisme.set('d',chemin)
	tige_prisme.set('stroke',couleur_dessous)
	tige_prisme.set('stroke-width',str(epaisseur_dessous))
	tige_prisme.set('style','stroke-linecap:round')
	tige_prisme.set('profondeur',str(profondeur))
	


	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        listeObjets=[plan,tige_plan,base_prisme,tige_prisme,flanc1_prisme,flanc2_prisme,bout1_prisme,bout2_prisme]
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)
        
        
	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	
	


def dessin_Sphere_Cylindre_2D_cote(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_sphere_cylindre_2D_cote_x
	y = -options.liaison_sphere_cylindre_2D_cote_y

	#Orientation **************************************
	rotation_cylindre = -options.liaison_sphere_cylindre_2D_cote_orientation_axe #Angle par defaut (sens trigo)
	if options.liaison_sphere_cylindre_2D_cote_axe=="x" :
		rotation_cylindre = 0
	elif options.liaison_sphere_cylindre_2D_cote_axe=="y" :
		rotation_cylindre = -90
	elif options.liaison_sphere_cylindre_2D_cote_axe=="-x" :
		rotation_cylindre = 180
	elif options.liaison_sphere_cylindre_2D_cote_axe=="-y" :
		rotation_cylindre = 90
	rotation_sphere = -options.liaison_sphere_cylindre_2D_cote_orientation_axe_sphere #Angle par defaut (sens trigo)
	if options.liaison_sphere_cylindre_2D_cote_axe_sphere=="x" :
		rotation_sphere = 0
	elif options.liaison_sphere_cylindre_2D_cote_axe_sphere=="y" :
		rotation_sphere = -90
	elif options.liaison_sphere_cylindre_2D_cote_axe_sphere=="-x" :
		rotation_sphere = 180
	elif options.liaison_sphere_cylindre_2D_cote_axe_sphere=="-y" :
		rotation_sphere = 90
	elif options.liaison_sphere_cylindre_2D_cote_axe_sphere=="normal" :
		rotation_sphere = rotation_cylindre - 90
	#Base *********************
	echelle=options.echelle
	Vx1,Vy1=getBase2D(echelle)
	base2D=(Vx1,Vy1)
	#Parametres ****************************
	echelle = options.echelle
	couleur_femelle = options.opt_gene_piece2_couleur
	couleur_male = options.opt_gene_piece1_couleur
	epaisseur_femelle = options.opt_gene_lignes_epaisseur_2
	epaisseur_male = options.opt_gene_lignes_epaisseur_1
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        #groupe_rotation = inkex.etree.SubElement(liaison, 'g')
	femelle = inkex.etree.SubElement(liaison,'g')
	male = inkex.etree.SubElement(liaison,'g')
	
	# Male ***************************************
	
	#Sphère
	sphere=inkex.etree.Element(inkex.addNS('circle','svg'))
	sphere.set('cx',"0")
	sphere.set('cy',"0")
	sphere.set('r',str(SC2Dc_diametre/2. * echelle))
	sphere.set('stroke',str(couleur_male))
	sphere.set('stroke-width',str(epaisseur_male))
	sphere.set('style','fill:white')
	male.append(sphere)

	#Ligne male
	ligneM=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(SC2Dc_diametre/2.	,	0),
					(SC2Dc_diametre/2. + SC2Dc_longueur_tige_sphere	,	0)	],
				False,
				base2D)
	ligneM.set('d',chemin)
	ligneM.set('stroke',couleur_male)
	ligneM.set('stroke-width',str(epaisseur_male))
	male.append(ligneM)
	
	# Femelle ***************************************

	#Rectangle
	rectangle=inkex.etree.Element(inkex.addNS('rect','svg'))
	rectangle.set('x',str(-SC2Dc_longueur*echelle / 2.) )
	rectangle.set('y',str((SC2Dc_diametre/2.-SC2Dc_hauteur) * echelle) )
	rectangle.set('width',str(SC2Dc_longueur*echelle))
	rectangle.set('height',str( SC2Dc_hauteur*echelle + (epaisseur_femelle+epaisseur_male)/2. ))
	rectangle.set('style','fill:white')
	rectangle.set('stroke',couleur_femelle)
	rectangle.set('stroke-width',str(epaisseur_femelle))
	femelle.append(rectangle)
	
	#Ligne femelle
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(0	,	SC2Dc_diametre/2.*echelle + (epaisseur_femelle+epaisseur_male)/2.),
				(0	,	(SC2Dc_diametre/2.+ SC2Dc_longueur_tige_cylindre)*echelle	)	])
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle))
	femelle.append(ligneF)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation_sphere)+")")
	femelle.set("transform","rotate("+str(rotation_cylindre)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	

def dessin_Sphere_Cylindre_2D_bout(options,contexte):
	global SC2Db_angle_ouverture
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_sphere_cylindre_2D_bout_x
	y = -options.liaison_sphere_cylindre_2D_bout_y

	#Orientation **************************************
	rotation_cylindre = -options.liaison_sphere_cylindre_2D_bout_orientation_axe_base #Angle par defaut (sens trigo)
	if options.liaison_sphere_cylindre_2D_bout_axe_base=="x" :
		rotation_cylindre = 0
	elif options.liaison_sphere_cylindre_2D_bout_axe_base=="y" :
		rotation_cylindre = -90
	elif options.liaison_sphere_cylindre_2D_bout_axe_base=="-x" :
		rotation_cylindre = 180
	elif options.liaison_sphere_cylindre_2D_bout_axe_base=="-y" :
		rotation_cylindre = 90
	rotation_sphere = -options.liaison_sphere_cylindre_2D_bout_orientation_axe_sphere #Angle par defaut (sens trigo)
	if options.liaison_sphere_cylindre_2D_bout_axe_sphere=="x" :
		rotation_sphere = 0
	elif options.liaison_sphere_cylindre_2D_bout_axe_sphere=="y" :
		rotation_sphere = -90
	elif options.liaison_sphere_cylindre_2D_bout_axe_sphere=="-x" :
		rotation_sphere = 180
	elif options.liaison_sphere_cylindre_2D_bout_axe_sphere=="-y" :
		rotation_sphere = 90
	elif options.liaison_sphere_cylindre_2D_bout_axe_sphere=="normal" :
		rotation_sphere = rotation_cylindre
	#Base *********************
	echelle = options.echelle
	Vx1,Vy1 = getBase2D(echelle)
	base2D = (Vx1,Vy1)
	#Parametres ****************************
	echelle = options.echelle
	couleur_femelle = options.opt_gene_piece2_couleur
	couleur_male = options.opt_gene_piece1_couleur
	epaisseur_femelle = options.opt_gene_lignes_epaisseur_2
	epaisseur_male = options.opt_gene_lignes_epaisseur_1
	
	diam_sphere = SC2Db_diametre
	diam_calotte = SC2Db_diametre + SC2Db_intervalle_spheres * 2 + epaisseur_femelle + epaisseur_male
	
	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
	femelle = inkex.etree.SubElement(liaison,'g')
	male = inkex.etree.SubElement(liaison,'g')
	
	# Male ***************************************
	
	#Sphère
	sphere=inkex.etree.Element(inkex.addNS('circle','svg'))
	sphere.set('cx',"0")
	sphere.set('cy',"0")
	sphere.set('r',str(diam_sphere/2. * echelle))
	sphere.set('stroke',str(couleur_male))
	sphere.set('stroke-width',str(epaisseur_male))
	sphere.set('style','fill:white')
	male.append(sphere)

	#Ligne male
	ligneM=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(diam_sphere/2.	,	0),
					(diam_sphere/2. + SC2Db_longueur_tige_sphere	,	0)	],
				False,
				base2D)
	ligneM.set('d',chemin)
	ligneM.set('stroke',couleur_male)
	ligneM.set('stroke-width',str(epaisseur_male))
	male.append(ligneM)
	
	# Femelle ***************************************

	#Calotte
	calotte=inkex.etree.Element(inkex.addNS('path','svg'))
	listeChemin = []
	SC2Db_angle_ouverture = SC2Db_angle_ouverture*math.pi/180
	theta = SC2Db_angle_ouverture/2.
	while theta < 2*math.pi - SC2Db_angle_ouverture/2.:
		listeChemin.append(( 	echelle*math.cos(theta)*(diam_calotte/2.),
					echelle*math.sin(theta)*(diam_calotte/2.) ))
		theta += 0.05
	listeChemin.append(( echelle*math.cos(-SC2Db_angle_ouverture/2.)*(diam_calotte/2.), echelle*math.sin(-SC2Db_angle_ouverture/2.)*(diam_calotte/2.) ))
	chemin=points_to_svgd(listeChemin,False)
	calotte.set('d',chemin)
	calotte.set('stroke',couleur_femelle)
	calotte.set('stroke-width',str(epaisseur_femelle))
	calotte.set('style','fill:none')
	femelle.append(calotte)
	
	#Trait
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(-diam_calotte/2.*echelle	,	echelle*diam_calotte/2.),
				(-diam_calotte/2.*echelle	,	-echelle*diam_calotte/2.	)	])
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle))
	femelle.append(ligneF)
	
	

	#Tige femelle
	ligneF=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points_to_svgd([	(	-diam_calotte/2.*echelle	,	0),
				(	-(diam_calotte+SC2Db_longueur_tige_cylindre)*echelle	,	0)	])
	ligneF.set('d',chemin)
	ligneF.set('stroke',couleur_femelle)
	ligneF.set('stroke-width',str(epaisseur_femelle))
	femelle.append(ligneF)
	
	# Transformations ***************************************
	male.set("transform","rotate("+str(rotation_sphere)+")")
	femelle.set("transform","rotate("+str(rotation_cylindre)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	






#===============================================================
def dessin_Sphere_Cylindre_3D(options,contexte):
	#Origine 2D
	x0 = options.x0
	y0 = options.y0
	#Base Axonometrique
	echelle=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques(echelle)
	base=(Vx,Vy,Vz)
	#Position
	x=options.liaison_sphere_cylindre_3D_position_x
	y=options.liaison_sphere_cylindre_3D_position_y
	z=options.liaison_sphere_cylindre_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres ****************************
	couleur_femelle = options.opt_gene_piece2_couleur
	couleur_male = options.opt_gene_piece1_couleur
	epaisseur_femelle = options.opt_gene_lignes_epaisseur_2
	epaisseur_male = options.opt_gene_lignes_epaisseur_1
	rayon = SC3D_diametre / 2.
	longueur = SC3D_longueur
#	angle_male-=float(options.liaison_pivot_glissant_3D_orientation_male)/180.*math.pi
	angle_cylindre=-float(options.liaison_sphere_cylindre_3D_rotation_cylindre)/180.*math.pi
	#Repere local de la liaison
	if(options.liaison_sphere_cylindre_3D_type_axe=="\"liaison_sphere_cylindre_3D_type_axe_quelconque\""):
		V=v3D(options.liaison_sphere_cylindre_3D_axe_quelconque_x,options.liaison_sphere_cylindre_3D_axe_quelconque_y,options.liaison_sphere_cylindre_3D_axe_quelconque_z,base)
		if V.x == V.y == V.z == 0 : V=v3D(1,0,0,base) #Si vecteur nul : on prend X par defaut
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle,angle_cylindre)#Repere Femelle
	else:	#Si vecteur standard
		if(options.liaison_sphere_cylindre_3D_axe=="x"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vx,echelle,angle_cylindre)#Repere Femelle
		elif(options.liaison_sphere_cylindre_3D_axe=="y"):
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vy,echelle,angle_cylindre)#Repere Femelle
		else:#z
			Vx1,Vy1,Vz1=getBaseFromVecteur(Vz,echelle,angle_cylindre)#Repere Femelle
	if(options.liaison_sphere_cylindre_3D_type_direction_sphere=="\"liaison_sphere_plan_3D_type_direction_sphere_quelconque\""):
		VS=v3D(options.liaison_sphere_cylindre_3D_direction_sphere_quelconque_x,options.liaison_sphere_cylindre_3D_direction_sphere_quelconque_y,options.liaison_sphere_cylindre_3D_direction_sphere_quelconque_z,base)
		if VS.x == VS.y == VS.z == 0 : VS=v3D(1,0,0,base) #Si vecteur nul : on prend X par defaut
		Vx2,Vy2,Vz2=getBaseFromVecteur(VS,echelle,angle_cylindre)#Repere Femelle
	else:	#Si vecteur standard
		if(options.liaison_sphere_cylindre_3D_axe_sphere=="x"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vx,echelle,angle_cylindre)#Repere Femelle
		elif(options.liaison_sphere_cylindre_3D_axe_sphere=="y"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vy,echelle,angle_cylindre)#Repere Femelle
		elif(options.liaison_sphere_cylindre_3D_axe_sphere=="z"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(Vz,echelle,angle_cylindre)#Repere Femelle
		elif(options.liaison_sphere_cylindre_3D_axe_sphere=="-x"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(-Vx,echelle,angle_cylindre)#Repere Femelle
		elif(options.liaison_sphere_cylindre_3D_axe_sphere=="-y"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(-Vy,echelle,angle_cylindre)#Repere Femelle
		elif(options.liaison_sphere_cylindre_3D_axe_sphere=="-z"):
			Vx2,Vy2,Vz2 = getBaseFromVecteur(-Vz,echelle,angle_cylindre)#Repere Femelle
		else:#Dans le prolongement de la piece femelle
			Vx2,Vy2,Vz2 = Vz1,Vx1,Vy1
			
	baseLocale_Cylindre = (Vx1,Vy1,Vz1)
	baseLocale_sphere = (Vx2,Vy2,Vz2)

	
	# Male ***************************************
	
	#Tige
	tigeMale=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(rayon,	0,	0	),
					(rayon + SC3D_longueur_tige_sphere,	0,	0	)
				],False,baseLocale_sphere)
	tigeMale.set('d',chemin)
	tigeMale.set('stroke',couleur_male)
	tigeMale.set('stroke-width',str(epaisseur_male))
	tigeMale.set('style','stroke-linecap:round')
	tigeMale.set('profondeur',str(profondeur))

	#Boule
	boule=inkex.etree.Element(inkex.addNS('circle','svg'))
	boule.set('cx',"0")
	boule.set('cy',"0")
	boule.set('r',str(rayon*echelle))
	boule.set('stroke',str(couleur_male))
	boule.set('stroke-width',str(epaisseur_male))
	boule.set('style','fill:white')
	boule.set('profondeur',"0")


	
	# Femelle ***************************************
	#On recupere les deux angles qui correspondent aux tangentes par rapport a la vue
	thetaCoupure1,thetaCoupure2=getAnglesCoupure(baseLocale_Cylindre)
	
	#On construit les arcs de cercles projete
	centre1 = v3D(-longueur/2, 0, 0, baseLocale_Cylindre) #Vecteur OC1, O=centre liaison
	centre2 = v3D(longueur/2, 0, 0, baseLocale_Cylindre) #Vecteur OC1, O=centre liaison
	ouverture = SC3D_angle_ouverture * math.pi/180
	listeArcs1 = getListePoints2DCercle(baseLocale_Cylindre, centre1, rayon, math.pi/2+ouverture/2, math.pi*5/2.-ouverture/2, thetaCoupure1, thetaCoupure2)
	listeArcs2 = getListePoints2DCercle(baseLocale_Cylindre, centre2, rayon, math.pi/2+ouverture/2, math.pi*5/2.-ouverture/2, thetaCoupure1, thetaCoupure2)
	
	#assert 0,str(listeArcs1)+"\n\n"+str(listeArcs2)
	
	listeArcs2[0].reverse()#On inverse les arcs de cercle
	listeArcs2[1].reverse()
	
	#On construit les cylindres
	listeDemiCylindre1=listeArcs1[0]+listeArcs2[0]
	listeDemiCylindre2=listeArcs1[1]+listeArcs2[1]
	
	
	chemin,profondeurDemiCylindre1 = points3D_to_svgd(listeDemiCylindre1,True)
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
					(0,	0,	-rayon	),
					(0,	0,	-rayon - SC3D_longueur_tige_cylindre)
				],False,baseLocale_Cylindre)
	barreFemelle.set('d',chemin)
	barreFemelle.set('stroke',couleur_femelle)
	barreFemelle.set('stroke-width',str(epaisseur_femelle))
	barreFemelle.set('style','stroke-linecap:round')
	barreFemelle.set('profondeur',str(profondeur*1e10))
	


	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        
        listeObjets=[demiCylindre1,demiCylindre2,barreFemelle,boule,tigeMale]
        
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)
        
        
	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	


def dessin_Masse_2D(options,contexte):
	#https://doczz.fr/doc/4506137/comment-installer-et-programmer-des-scripts-python-dans-i...
	#Position *****************************************
	x0 = options.x0
	y0 = options.y0
	x = options.liaison_masse_2D_x
	y = -options.liaison_masse_2D_y
	#Parametres ****************************
	couleur = options.opt_gene_piece1_couleur
	epaisseur = options.opt_gene_lignes_epaisseur_1
	#Orientation **************************************
	rotation=-options.liaison_masse_2D_orientation_axe #Angle par defaut (sens trigo)
	if(options.liaison_masse_2D_axe=="x"):
		rotation=0
	elif(options.liaison_masse_2D_axe=="y"):
		rotation=-90
	elif(options.liaison_masse_2D_axe=="-x"):
		rotation=180
	elif(options.liaison_masse_2D_axe=="-y"):
		rotation=90

	#Groupes ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        masse = inkex.etree.SubElement(liaison,'g')
	#Base **************************
	echelle_liaison = options.echelle
	Vx1,Vy1 = getBase2D(echelle_liaison)
	base2D=(Vx1,Vy1)
	# DESSIN ***************************************
	#Trait principal
	trait=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(-REF2D_longueur_tige,	-REF2D_largeur/2.),
					(-REF2D_longueur_tige,	REF2D_largeur/2.)	],
				False,base2D)
	trait.set('d',chemin)
	trait.set('stroke',couleur)
	trait.set('stroke-width',str(epaisseur))
	trait.set('style',"stroke-linecap:round")
	masse.append(trait)
	
	# Tige
	tige=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin=points2D_to_svgd([	(0,	0),
					(-REF2D_longueur_tige,	0)	],
				False,base2D)
	tige.set('d',chemin)
	tige.set('stroke',couleur)
	tige.set('stroke-width',str(epaisseur))
	masse.append(tige)
	
	# hachures
	pas = float(REF2D_largeur) / (REF2D_nombre_hachures-1)
	for i in range(REF2D_nombre_hachures):
		hachure=inkex.etree.Element(inkex.addNS('path','svg'))
		chemin=points2D_to_svgd([	(-REF2D_longueur_tige,	-REF2D_largeur/2. + i*pas),
						(-REF2D_longueur_tige-REF2D_longueur_hachures,	-REF2D_largeur/2. + i*pas + REF2D_longueur_hachures*math.tan(REF2D_inclinaison/180.*math.pi))	],
					False,base2D)
		hachure.set('d',chemin)
		hachure.set('stroke',couleur)
		hachure.set('stroke-width',str(epaisseur))
		hachure.set('style',"stroke-linecap:round")
		masse.append(hachure)
	
	# Transformations ***************************************

	masse.set("transform","rotate("+str(rotation)+")")
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x))+","+str(convertLongueur2Inkscape(options,y0+y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)

	








#===============================================================
def dessin_Masse_3D(options,contexte):
	#Origine 2D
	x0 = options.x0
	y0 = options.y0
	#Base Axonometrique
	echelle_liaison=options.echelle
	Vx,Vy,Vz=getVecteursAxonometriques()
	base=(Vx,Vy,Vz)
	#Centre de la liaison dans le repere 3D
	x = options.liaison_masse_3D_position_x
	y = options.liaison_masse_3D_position_y
	z = options.liaison_masse_3D_position_z
	vPosition=v3D(x,y,z,base)#Vecteur position exprime dans la base axono
	#Parametres de la liaison
	couleur = options.opt_gene_piece1_couleur
	epaisseur = options.opt_gene_lignes_epaisseur_1
	pivotement = -float(options.liaison_masse_3D_pivotement)/180.*math.pi
	dessin_3D = options.liaison_masse_3D_representation

	#Repere local de la liaison
	if(options.liaison_masse_3D_type_axe=="\"liaison_masse_3D_type_axe_quelconque\""):
		V=v3D(options.liaison_masse_3D_axe_quelconque_x,options.liaison_masse_3D_axe_quelconque_y,options.liaison_masse_3D_axe_quelconque_z,base)
		if V.x == V.y == V.z == 0 : V=v3D(1,0,0,base) #Si vecteur nul : on prend X par defaut
		Vx1,Vy1,Vz1=getBaseFromVecteur(V,echelle_liaison,pivotement)
	else:	#Si vecteur standard
		if(options.liaison_masse_3D_axe=="x"):
			Vx1,Vy1,Vz1 = getBaseFromVecteur(Vx,echelle_liaison,pivotement)
		elif(options.liaison_masse_3D_axe=="y"):
			Vx1,Vy1,Vz1 = getBaseFromVecteur(Vy,echelle_liaison,pivotement)
		elif(options.liaison_masse_3D_axe=="z"):
			Vx1,Vy1,Vz1 = getBaseFromVecteur(Vz,echelle_liaison,pivotement)
		elif(options.liaison_masse_3D_axe=="-x"):
			Vx1,Vy1,Vz1 = getBaseFromVecteur(-Vx,echelle_liaison,pivotement)
		elif(options.liaison_masse_3D_axe=="-y"):
			Vx1,Vy1,Vz1 = getBaseFromVecteur(-Vy,echelle_liaison,pivotement)
		elif(options.liaison_masse_3D_axe=="-z"):
			Vx1,Vy1,Vz1 = getBaseFromVecteur(-Vz,echelle_liaison,pivotement)
	baseLocale=(Vx1,Vy1,Vz1)
#	baseLocale=(Vx2,Vy2,Vz2)

	
	# Dessin ***************************************
	
	listeObjets=[]
	
	tige=inkex.etree.Element(inkex.addNS('path','svg'))
	chemin,profondeur=points3D_to_svgd([
					(0,	0,	0	),
					(-REF3D_longueur_tige,	0,	0	)
				],False,baseLocale)
	tige.set('d',chemin)
	tige.set('stroke',couleur)
	tige.set('stroke-width',str(epaisseur))
	tige.set('style','stroke-linecap:round')
	tige.set('profondeur',str(profondeur))
	listeObjets.append(tige)

	#DESSIN 3D
	if dessin_3D:
		plan=inkex.etree.Element(inkex.addNS('path','svg'))
		chemin,profondeur_trait=points3D_to_svgd([
					(-REF3D_longueur_tige,	REF3D_largeur/2.,	REF3D_largeur/2.	),
					(-REF3D_longueur_tige,	-REF3D_largeur/2.,	REF3D_largeur/2.	),
					(-REF3D_longueur_tige,	-REF3D_largeur/2.,	-REF3D_largeur/2.	),
					(-REF3D_longueur_tige,	REF3D_largeur/2.,	-REF3D_largeur/2.	)
				],True,baseLocale)
		plan.set('d',chemin)
		plan.set('stroke',couleur)
		plan.set('stroke-width',str(epaisseur))
		plan.set('fill','white')
		plan.set('profondeur',str(profondeur_trait))
		plan.set('style',"stroke-linejoin:round")
		listeObjets.append(plan)
		
		# hachures
		pas = float(REF3D_largeur) / (REF3D_nombre_hachures_3D-1)
		for i in range(REF3D_nombre_hachures_plat):
			for j in range(REF3D_nombre_hachures_plat):
				hachure=inkex.etree.Element(inkex.addNS('path','svg'))
				chemin,profondeur = points3D_to_svgd([	(-REF3D_longueur_tige,				-REF3D_largeur/2. + i*pas ,									-REF3D_largeur/2. + j*pas ),
									(-REF3D_longueur_tige-REF3D_longueur_hachures_3D,	-REF3D_largeur/2. + i*pas + REF3D_longueur_hachures_3D*math.tan(REF3D_inclinaison_3D/180.*math.pi),	-REF3D_largeur/2. + j*pas)	],
							False,baseLocale)
				hachure.set('d',chemin)
				hachure.set('stroke',couleur)
				hachure.set('stroke-width',str(epaisseur))
				hachure.set('style',"stroke-linecap:round")
				hachure.set('profondeur',str(2 * profondeur_trait))
				listeObjets.append(hachure)
	# DESSIN A PLAT
	else:
		trait=inkex.etree.Element(inkex.addNS('path','svg'))
		chemin,profondeur_trait=points3D_to_svgd([
					(-REF3D_longueur_tige,	-REF3D_largeur/2.,	0	),
					(-REF3D_longueur_tige,	REF3D_largeur/2.,	0	)
				],False,baseLocale)
		trait.set('d',chemin)
		trait.set('stroke',couleur)
		trait.set('stroke-width',str(epaisseur))
		trait.set('style','stroke-linecap:round')
		trait.set('profondeur',str(profondeur_trait))
		listeObjets.append(trait)
	
		# hachures
		pas = float(REF3D_largeur) / (REF3D_nombre_hachures_plat-1)
		for i in range(REF3D_nombre_hachures_plat):
			hachure=inkex.etree.Element(inkex.addNS('path','svg'))
			chemin,profondeur = points3D_to_svgd([	(-REF3D_longueur_tige,				-REF3D_largeur/2. + i*pas ,									0),
							(-REF3D_longueur_tige-REF3D_longueur_hachures_3D,	-REF3D_largeur/2. + i*pas + REF3D_longueur_hachures_plat*math.tan(REF3D_inclinaison_plat/180.*math.pi),	0)	],
						False,baseLocale)
			hachure.set('d',chemin)
			hachure.set('stroke',couleur)
			hachure.set('stroke-width',str(epaisseur))
			hachure.set('style',"stroke-linecap:round")
			hachure.set('profondeur',str(2 * profondeur_trait))
			listeObjets.append(hachure)

	# Ajout au Groupe ******************************************
        liaison = inkex.etree.SubElement(contexte, 'g')
        ajouteCheminDansLOrdreAuGroupe(liaison,listeObjets)
        
        
	# Transformations ***************************************
	liaison.set("transform","translate("+str(convertLongueur2Inkscape(options,x0+x*Vx.x+y*Vy.x+z*Vz.x))+","+str(convertLongueur2Inkscape(options,y0+x*Vx.y+y*Vy.y+z*Vz.y))+")")
	# Credits **************************************
	liaison.set("credits",options.credits)
	




class Liaisons(inkex.Effect):
    """
    Example Inkscape effect extension.
    Creates a new layer with a "Hello World!" text centered in the middle of the document.
    """
    def __init__(self):
        """
        Constructor.
        Defines the "--what" option of a script.
        """
        # Call the base class constructor.
        inkex.Effect.__init__(self)
        

        # Define string option "--what" with "-w" shortcut and default value "World".
        #PRINCIPAL
        self.OptionParser.add_option('--onglets_pricipaux', action = 'store', type = 'string', dest = 'onglets_pricipaux', default = '', help = u"Choix de la liaison")
        
        #LIAISONS...
        self.OptionParser.add_option('--liaison', action = 'store', type = 'string', dest = 'liaison', default = '', help = u"Choix de la liaison")
        
        #LIAISON PIVOT ***************************************************
        self.OptionParser.add_option('--liaison_pivot_type', action = 'store', type = 'string', dest = 'liaison_pivot_type', default = 'liaison_pivot_2D_cote', help = u"Type de representation de la pivot")
        
        self.OptionParser.add_option('--liaison_pivot_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_pivot_2D_cote_x', default = '0', help = u"Position sur X de la liaison pivot 2D cote relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_pivot_2D_cote_y', default = '0', help = u"Position sur Y de la liaison pivot 2D cote relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot2D_cote_axe', action = 'store', type = 'string', dest = 'liaison_pivot2D_cote_axe', default = 'x', help = u"Principales directions de l'axe d'une pivot 2D vue de cote")
        self.OptionParser.add_option('--liaison_pivot2D_cote_orientation', action = 'store', type = 'float', dest = 'liaison_pivot2D_cote_orientation', default = '0', help = u"Orientation Pivot 2D en degres")

        self.OptionParser.add_option('--liaison_pivot_2D_face_x', action = 'store', type = 'float', dest = 'liaison_pivot_2D_face_x', default = 0, help = u"Position sur X de la liaison pivot 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_2D_face_y', action = 'store', type = 'float', dest = 'liaison_pivot_2D_face_y', default = 0, help = u"Position sur Y de la liaison pivot 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot2D_face_axe1', action = 'store', type = 'string', dest = 'liaison_pivot2D_face_axe1', default = 'x', help = u"Principales directions du bras 1 d'une pivot vue de face")
        self.OptionParser.add_option('--liaison_pivot2D_face_orientation1', action = 'store', type = 'float', dest = 'liaison_pivot2D_face_orientation1', default = '0', help = u"Orientation du bras 1 d'une pivot vue de face en degres")
        self.OptionParser.add_option('--liaison_pivot2D_face_axe2', action = 'store', type = 'string', dest = 'liaison_pivot2D_face_axe2', default = '-y', help = u"Principales directions du bras 2 d'une pivot vue de face")
        self.OptionParser.add_option('--liaison_pivot2D_face_orientation2', action = 'store', type = 'float', dest = 'liaison_pivot2D_face_orientation2', default = '0', help = u"Orientation du bras 2 d'une pivot vue de face en degres")

        self.OptionParser.add_option('--liaison_pivot_3D_position_x', action = 'store', type = 'float', dest = 'liaison_pivot_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_position_y', action = 'store', type = 'float', dest = 'liaison_pivot_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_position_z', action = 'store', type = 'float', dest = 'liaison_pivot_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_type_direction', action = 'store', type = 'str', dest = 'liaison_pivot_3D_type_direction', default = "liaison_pivot_3D_type_direction_standard", help = u"Choix du type de direction de la pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_axe', action = 'store', type = 'str', dest = 'liaison_pivot_3D_axe', default = 'x', help = u"Directions standard de l'axe de la pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_type_direction_quelconque_x', action = 'store', type = 'float', dest = 'liaison_pivot_3D_type_direction_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur direceur de la pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_type_direction_quelconque_y', action = 'store', type = 'float', dest = 'liaison_pivot_3D_type_direction_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur direceur de la pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_type_direction_quelconque_z', action = 'store', type = 'float', dest = 'liaison_pivot_3D_type_direction_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur direceur de la pivot 3D")
        self.OptionParser.add_option('--liaison_pivot_3D_orientation_male', action = 'store', type = 'float', dest = 'liaison_pivot_3D_orientation_male', default = 0, help = u"Orientation en degres de la piece male de la pivot")
        self.OptionParser.add_option('--liaison_pivot_3D_orientation_femelle', action = 'store', type = 'float', dest = 'liaison_pivot_3D_orientation_femelle', default = 0, help = u"Orientation en degres de la piece femelle de la pivot")

        #LIAISON PIVOT GLISSANT ******************************************
        self.OptionParser.add_option('--liaison_pivot_glissant_type', action = 'store', type = 'string', dest = 'liaison_pivot_glissant_type', default = 'liaison_pivot_glissant_2D_cote', help = u"Type de representation de la pivot glissant")

        self.OptionParser.add_option('--liaison_pivot_glissant_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_cote_x', default = '0', help = u"Position sur X de la liaison pivot glissant 2D coté relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_cote_y', default = '0', help = u"Position sur Y de la liaison pivot glissant 2D coté relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_cote_axe', action = 'store', type = 'string', dest = 'liaison_pivot_glissant_2D_cote_axe', default = 'x', help = u"Principales directions de l'axe d'une pivot glissant 2D vue de cote")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_cote_orientation', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_cote_orientation', default = '0', help = u"Orientation Pivot glissant 2D en degres")

        self.OptionParser.add_option('--liaison_pivot_glissant_2D_face_x', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_face_x', default = '0', help = u"Position sur X de la liaison pivot 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_face_y', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_face_y', default = '0', help = u"Position sur Y de la liaison pivot 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_face_axe1', action = 'store', type = 'string', dest = 'liaison_pivot_glissant_2D_face_axe1', default = 'x', help = u"Principales directions du bras 1 d'une pivot glissant vue de face")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_face_orientation1', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_face_orientation1', default = '0', help = u"Orientation du bras 1 d'une pivot glissant vue de face en degres")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_face_axe2', action = 'store', type = 'string', dest = 'liaison_pivot_glissant_2D_face_axe2', default = '-y', help = u"Principales directions du bras 2 d'une pivot glissant vue de face")
        self.OptionParser.add_option('--liaison_pivot_glissant_2D_face_orientation2', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_2D_face_orientation2', default = '0', help = u"Orientation du bras 2 d'une pivot glissant vue de face en degres")

        self.OptionParser.add_option('--liaison_pivot_glissant_3D_position_x', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_position_y', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_position_z', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_type_direction', action = 'store', type = 'str', dest = 'liaison_pivot_glissant_3D_type_direction', default = "liaison_pivot_glissant_3D_type_direction_standard", help = u"Choix du type de direction de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_axe', action = 'store', type = 'str', dest = 'liaison_pivot_glissant_3D_axe', default = 'x', help = u"Orientations standard de l'axe de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_type_direction_quelconque_x', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_type_direction_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_type_direction_quelconque_y', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_type_direction_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_type_direction_quelconque_z', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_type_direction_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_orientation_male', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_orientation_male', default = 0, help = u"Orientation en degres de la piece male de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_pivot_glissant_3D_orientation_femelle', action = 'store', type = 'float', dest = 'liaison_pivot_glissant_3D_orientation_femelle', default = 0, help = u"Orientation en degres de la piece femelle de la pivot glissant 3D")


        #LIAISON GLISSIERE ******************************************
        self.OptionParser.add_option('--liaison_glissiere_type', action = 'store', type = 'string', dest = 'liaison_glissiere_type', default = 'liaison_glissiere_2D_cote', help = u"Type de representation de la glissiere")

        self.OptionParser.add_option('--liaison_glissiere_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_cote_x', default = '0', help = u"Position sur X de la liaison glissiere 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_glissiere_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_cote_y', default = '0', help = u"Position sur Y de la liaison glissiere 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_glissiere_2D_cote_direction_standard', action = 'store', type = 'string', dest = 'liaison_glissiere_2D_cote_direction_standard', default = 'x', help = u"Principales directions de l'axe d'une glissiere 2D vue de cote")
        self.OptionParser.add_option('--liaison_glissiere_2D_cote_direction_quelconque', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_cote_direction_quelconque', default = '0', help = u"Orientation glissiere 2D en degres")
        
        self.OptionParser.add_option('--liaison_glissiere_2D_face_x', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_face_x', default = '0', help = u"Position sur X de la glissiere 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_glissiere_2D_face_y', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_face_y', default = '0', help = u"Position sur Y de la glissiere 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_glissiere_2D_face_orientation_standard_femelle', action = 'store', type = 'string', dest = 'liaison_glissiere_2D_face_orientation_standard_femelle', default = 'x', help = u"Principales directions du bras de la piece femelle d'une glissiere vue de face")
        self.OptionParser.add_option('--liaison_glissiere_2D_face_orientation_quelconque_femelle', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_face_orientation_quelconque_femelle', default = '0', help = u"Orientation du bras de la piece femelle d'une glissiere vue de face en degres")
        self.OptionParser.add_option('--liaison_glissiere_2D_face_orientation_standard_male', action = 'store', type = 'string', dest = 'liaison_glissiere_2D_face_orientation_standard_male', default = 'x', help = u"Principales directions du bras de la piece male d'une glissiere vue de face")
        self.OptionParser.add_option('--liaison_glissiere_2D_face_orientation_quelconque_male', action = 'store', type = 'float', dest = 'liaison_glissiere_2D_face_orientation_quelconque_male', default = '0', help = u"Orientation du bras de la piece male d'une glissiere vue de face en degres")

        self.OptionParser.add_option('--liaison_glissiere_3D_position_x', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_position_y', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_position_z', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_type_direction', action = 'store', type = 'str', dest = 'liaison_glissiere_3D_type_direction', default = "liaison_glissiere_3D_type_orientation_standard", help = u"Choix du type de direction de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_axe', action = 'store', type = 'str', dest = 'liaison_glissiere_3D_axe', default = 'x', help = u"Direction standard de l'axe de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_type_direction_quelconque_x', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_type_direction_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur direceur de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_type_direction_quelconque_y', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_type_direction_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur direceur de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_type_direction_quelconque_z', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_type_direction_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur direceur de la glissiere 3D")
        self.OptionParser.add_option('--liaison_glissiere_3D_orientation', action = 'store', type = 'float', dest = 'liaison_glissiere_3D_orientation', default = 0, help = u"Orientation de la glissiere 3D")

        
        #LIAISON PLANE ******************************************
        self.OptionParser.add_option('--liaison_plane_type', action = 'store', type = 'string', dest = 'liaison_plane_type', default = 'liaison_plane_2D_cote', help = u"Type de representation de la liaison plane")
        
        self.OptionParser.add_option('--liaison_plane_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_plane_2D_cote_x', default = '0', help = u"Position sur X de la liaison plane 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_plane_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_plane_2D_cote_y', default = '0', help = u"Position sur Y de la liaison plane 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_plane_2D_cote_axe', action = 'store', type = 'string', dest = 'liaison_plane_2D_cote_axe', default = 'x', help = u"Principales directions de l'axe d'une plane 2D vue de cote")
        self.OptionParser.add_option('--liaison_plane_2D_cote_orientation', action = 'store', type = 'float', dest = 'liaison_plane_2D_cote_orientation', default = '0', help = u"Orientation plane 2D en degres")

        self.OptionParser.add_option('--liaison_plane_2D_dessus_x', action = 'store', type = 'float', dest = 'liaison_plane_2D_dessus_x', default = '0', help = u"Position sur X de la liaison plane 2D dessus relativement a l'origine")
        self.OptionParser.add_option('--liaison_plane_2D_dessus_y', action = 'store', type = 'float', dest = 'liaison_plane_2D_dessus_y', default = '0', help = u"Position sur Y de la liaison plane 2D dessus relativement a l'origine")
        self.OptionParser.add_option('--liaison_plane_2D_axe_dessous', action = 'store', type = 'string', dest = 'liaison_plane_2D_axe_dessous', default = 'y', help = u"Principales directions de l'axe d'une plane 2D dessous")
        self.OptionParser.add_option('--liaison_plane_2D_orientation_dessous', action = 'store', type = 'float', dest = 'liaison_plane_2D_orientation_dessous', default = '0', help = u"Orientation plane 2D dessous en degres")
        self.OptionParser.add_option('--liaison_plane_2D_axe_dessus', action = 'store', type = 'string', dest = 'liaison_plane_2D_axe_dessus', default = '-y', help = u"Principales directions de l'axe d'une plane 2D dessus")
        self.OptionParser.add_option('--liaison_plane_2D_orientation_dessus', action = 'store', type = 'float', dest = 'liaison_plane_2D_orientation_dessus', default = '0', help = u"Orientation plane 2D dessus en degres")
 
        self.OptionParser.add_option('--liaison_plane_3D_position_x', action = 'store', type = 'float', dest = 'liaison_plane_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_position_y', action = 'store', type = 'float', dest = 'liaison_plane_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_position_z', action = 'store', type = 'float', dest = 'liaison_plane_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_type_normale', action = 'store', type = 'str', dest = 'liaison_plane_3D_type_normale', default = "liaison_plane_3D_type_normale_standard", help = u"Choix du type de direction de la glissiere 3D")
        self.OptionParser.add_option('--liaison_plane_3D_axe', action = 'store', type = 'str', dest = 'liaison_plane_3D_axe', default = 'x', help = u"Direction standard de l'axe de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_type_direction_quelconque_x', action = 'store', type = 'float', dest = 'liaison_plane_3D_type_direction_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur direceur de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_type_direction_quelconque_y', action = 'store', type = 'float', dest = 'liaison_plane_3D_type_direction_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur direceur de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_type_direction_quelconque_z', action = 'store', type = 'float', dest = 'liaison_plane_3D_type_direction_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur direceur de la liaison plane 3D")
        self.OptionParser.add_option('--liaison_plane_3D_orientation1', action = 'store', type = 'float', dest = 'liaison_plane_3D_orientation1', default = 10, help = u"Orientation de la liaison plane 3D - piece 1")
        self.OptionParser.add_option('--liaison_plane_3D_orientation2', action = 'store', type = 'float', dest = 'liaison_plane_3D_orientation2', default = 0, help = u"Orientation de la liaison plane 3D - piece 2")
            
        #LIAISON SPHERIQUE ******************************************
        self.OptionParser.add_option('--liaison_spherique_type', action = 'store', type = 'string', dest = 'liaison_spherique_type', default = 'liaison_spherique_2D', help = u"Type de representation de la liaison spherique")

        self.OptionParser.add_option('--liaison_spherique_2D_x', action = 'store', type = 'float', dest = 'liaison_spherique_2D_x', default = '0', help = u"Position sur X de la liaison spherique 2D relativement a l'origine")
        self.OptionParser.add_option('--liaison_spherique_2D_y', action = 'store', type = 'float', dest = 'liaison_spherique_2D_y', default = '0', help = u"Position sur Y de la liaison spherique 2D relativement a l'origine")
        self.OptionParser.add_option('--liaison_spherique_2D_axe_male', action = 'store', type = 'string', dest = 'liaison_spherique_2D_axe_male', default = 'x', help = u"Principales directions de l'axe d'une spherique 2D - male")
        self.OptionParser.add_option('--liaison_spherique_2D_orientation_male', action = 'store', type = 'float', dest = 'liaison_spherique_2D_orientation_male', default = '0', help = u"Orientation plane 2D en degres - male")
        self.OptionParser.add_option('--liaison_spherique_2D_axe_femelle', action = 'store', type = 'string', dest = 'liaison_spherique_2D_axe_femelle', default = 'x', help = u"Principales directions de l'axe d'une spherique 2D - femelle")
        self.OptionParser.add_option('--liaison_spherique_2D_orientation_femelle', action = 'store', type = 'float', dest = 'liaison_spherique_2D_orientation_femelle', default = '0', help = u"Orientation plane 2D en degres - femelle")
        self.OptionParser.add_option('--liaison_spherique_2D_calotte_adaptative', action = 'store', type = 'inkbool', dest = 'liaison_spherique_2D_calotte_adaptative', default = 'True', help = u"Permet d'orienter automatiquement la calotte de la pièce femelle")

        self.OptionParser.add_option('--liaison_spherique_3D_position_x', action = 'store', type = 'float', dest = 'liaison_spherique_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison sphérique 3D")
        self.OptionParser.add_option('--liaison_spherique_3D_position_y', action = 'store', type = 'float', dest = 'liaison_spherique_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison sphérique 3D")
        self.OptionParser.add_option('--liaison_spherique_3D_position_z', action = 'store', type = 'float', dest = 'liaison_spherique_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison sphérique 3D")
        self.OptionParser.add_option('--liaison_spherique_3D_type_orientation_male', action = 'store', type = 'str', dest = 'liaison_spherique_3D_type_orientation_male', default = "liaison_spherique_3D_axe_male", help = u"Choix du type de direction de la liaison sphérique 3D mâle")
        self.OptionParser.add_option('--liaison_spherique_3D_axe_male', action = 'store', type = 'str', dest = 'liaison_spherique_3D_axe_male', default = 'y', help = u"Direction standard de l'axe de la liaison sphérique 3D mâle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_direction_male_quelconque_x', action = 'store', type = 'float', dest = 'liaison_spherique_3D_type_direction_male_quelconque_x', default = 0, help = u"Coordonnee sur x du vecteur direceur de la liaison sphérique 3D mâle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_direction_male_quelconque_y', action = 'store', type = 'float', dest = 'liaison_spherique_3D_type_direction_male_quelconque_y', default = 1, help = u"Coordonnee sur y du vecteur direceur de la liaison sphérique 3D mâle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_direction_male_quelconque_z', action = 'store', type = 'float', dest = 'liaison_spherique_3D_type_direction_male_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur direceur de la liaison sphérique 3D mâle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_orientation_femelle', action = 'store', type = 'str', dest = 'liaison_spherique_3D_type_orientation_femelle', default = "liaison_spherique_3D_axe_male", help = u"Choix du type de direction de la liaison sphérique 3D femelle")
        self.OptionParser.add_option('--liaison_spherique_3D_axe_femelle', action = 'store', type = 'str', dest = 'liaison_spherique_3D_axe_femelle', default = 'y', help = u"Direction standard de l'axe de la liaison sphérique 3D femelle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_direction_femelle_quelconque_x', action = 'store', type = 'float', dest = 'liaison_spherique_3D_type_direction_femelle_quelconque_x', default = 0, help = u"Coordonnee sur x du vecteur direceur de la liaison sphérique 3D femelle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_direction_femelle_quelconque_y', action = 'store', type = 'float', dest = 'liaison_spherique_3D_type_direction_femelle_quelconque_y', default = 1, help = u"Coordonnee sur y du vecteur direceur de la liaison sphérique 3D femelle")
        self.OptionParser.add_option('--liaison_spherique_3D_type_direction_femelle_quelconque_z', action = 'store', type = 'float', dest = 'liaison_spherique_3D_type_direction_femelle_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur direceur de la liaison sphérique 3D femelle")
        self.OptionParser.add_option('--liaison_spherique_3D_calotte_adaptative', action = 'store', type = 'inkbool', dest = 'liaison_spherique_3D_calotte_adaptative', default = 'True', help = u"Permet d'orienter automatiquement la calotte de la pièce femelle")


	#LIAISON HELICOIDALE **********************************************
        self.OptionParser.add_option('--liaison_helicoidale_pas_a_gauche', action = 'store', type = 'inkbool', dest = 'liaison_helicoidale_pas_a_gauche', default = 'True', help = u"Vrai si c'est un pas à gauche")
        self.OptionParser.add_option('--liaison_helicoidale_type', action = 'store', type = 'string', dest = 'liaison_helicoidale_type', default = 'liaison_helicoidale_2D_cote', help = u"Type de representation de la liaison hélicoïdale")

        self.OptionParser.add_option('--liaison_helicoidale_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_cote_x', default = '0', help = u"Position sur X de la liaison hélicoidale 2D coté relativement a l'origine")
	self.OptionParser.add_option('--liaison_helicoidale_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_cote_y', default = '0', help = u"Position sur Y de la liaison hélicoidale 2D coté relativement a l'origine")       
        self.OptionParser.add_option('--liaison_helicoidale_2D_cote_axe', action = 'store', type = 'string', dest = 'liaison_helicoidale_2D_cote_axe', default = 'x', help = u"Principales directions de l'axe d'une hélicoidale 2D vue de coté")
        self.OptionParser.add_option('--liaison_helicoidale_2D_cote_orientation', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_cote_orientation', default = '0', help = u"Orientation de l'hélicoidale 2D (coté) en degres")

        self.OptionParser.add_option('--liaison_helicoidale_2D_face_x', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_face_x', default = 0, help = u"Position sur X de la liaison hélicoidale 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_helicoidale_2D_face_y', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_face_y', default = 0, help = u"Position sur Y de la liaison hélicoidale 2D face relativement a l'origine")
        self.OptionParser.add_option('--liaison_helicoidale_2D_face_axe1', action = 'store', type = 'string', dest = 'liaison_helicoidale_2D_face_axe1', default = 'x', help = u"Principales directions du bras 1 d'une hélicoidale vue de face")
        self.OptionParser.add_option('--liaison_helicoidale_2D_face_orientation1', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_face_orientation1', default = '0', help = u"Orientation du bras 1 d'une hélicoidale vue de face en degres")
        self.OptionParser.add_option('--liaison_helicoidale_2D_face_axe2', action = 'store', type = 'string', dest = 'liaison_helicoidale_2D_face_axe2', default = '-y', help = u"Principales directions du bras 2 d'une hélicoidale vue de face")
        self.OptionParser.add_option('--liaison_helicoidale_2D_face_orientation2', action = 'store', type = 'float', dest = 'liaison_helicoidale_2D_face_orientation2', default = '0', help = u"Orientation du bras 2 d'une hélicoidale vue de face en degres")

        self.OptionParser.add_option('--liaison_helicoidale_3D_position_x', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison helicoidale 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_position_y', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison helicoidale 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_position_z', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison helicoidale 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_type_direction', action = 'store', type = 'str', dest = 'liaison_helicoidale_3D_type_direction', default = "liaison_helicoidale_3D_type_direction_standard", help = u"Choix du type de direction de la liaison helicoidale 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_axe', action = 'store', type = 'str', dest = 'liaison_helicoidale_3D_axe', default = 'x', help = u"Orientations standard de l'axe de la pivot glissant 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_type_direction_quelconque_x', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_type_direction_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de l'helicoidale 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_type_direction_quelconque_y', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_type_direction_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de l'helicoidal 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_type_direction_quelconque_z', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_type_direction_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de l'helicoidal 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_orientation_male', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_orientation_male', default = 0, help = u"Orientation en degres de la piece male de l'helicoidal 3D")
        self.OptionParser.add_option('--liaison_helicoidale_3D_orientation_femelle', action = 'store', type = 'float', dest = 'liaison_helicoidale_3D_orientation_femelle', default = 0, help = u"Orientation en degres de la piece femelle de l'helicoidal 3D")

	#LIAISON SPHÈRE-PLAN **********************************************
        self.OptionParser.add_option('--liaison_sphere_plan_type', action = 'store', type = 'string', dest = 'liaison_sphere_plan_type', default = 'liaison_sphere_plan_2D_cote', help = u"Type de representation de la liaison sphère-plan")

        self.OptionParser.add_option('--liaison_sphere_plan_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_cote_x', default = '0', help = u"Position sur X de la liaison Sphère-plan 2D coté relativement a l'origine")
	self.OptionParser.add_option('--liaison_sphere_plan_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_cote_y', default = '0', help = u"Position sur Y de la liaison Sphère-plan 2D coté relativement a l'origine")       
        self.OptionParser.add_option('--liaison_sphere_plan_2D_cote_axe_normale', action = 'store', type = 'string', dest = 'liaison_sphere_plan_2D_cote_axe_normale', default = 'y', help = u"Principales directions de la normale de la Sphère-plan 2D vue de coté")
        self.OptionParser.add_option('--liaison_sphere_plan_2D_cote_orientation_normale', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_cote_orientation_normale', default = '0', help = u"Orientation de la normale de la Sphère-Plan 2D (coté) en degres")
        self.OptionParser.add_option('--liaison_sphere_plan_2D_cote_axe_sphere', action = 'store', type = 'string', dest = 'liaison_sphere_plan_2D_cote_axe_sphere', default = 'normale', help = u"Principales directions de la sphère de la Sphère-plan 2D vue de coté")
        self.OptionParser.add_option('--liaison_sphere_plan_2D_cote_orientation_sphere', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_cote_orientation_sphere', default = '0', help = u"Orientation de la sphère de la Sphère-Plan 2D (coté) en degres")

        self.OptionParser.add_option('--liaison_sphere_plan_2D_dessus_x', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_dessus_x', default = '0', help = u"Position sur X de la liaison Sphère-plan 2D dessus relativement a l'origine")
	self.OptionParser.add_option('--liaison_sphere_plan_2D_dessus_y', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_dessus_y', default = '0', help = u"Position sur Y de la liaison Sphère-plan 2D dessus relativement a l'origine")       
        self.OptionParser.add_option('--liaison_sphere_plan_2D_dessus_axe_plan', action = 'store', type = 'string', dest = 'liaison_sphere_plan_2D_dessus_axe_plan', default = 'y', help = u"Principales directions de l'axe du plan de la Sphère-plan 2D vue de dessus")
        self.OptionParser.add_option('--liaison_sphere_plan_2D_dessus_orientation_plan', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_dessus_orientation_plan', default = '0', help = u"Directions quelconque de l'axe du plan de la Sphère-plan 2D vue de dessus")
        self.OptionParser.add_option('--liaison_sphere_plan_2D_dessus_axe_sphere', action = 'store', type = 'string', dest = 'liaison_sphere_plan_2D_dessus_axe_sphere', default = 'y', help = u"Principales directions de l'axe de la sphère de la Sphère-plan 2D vue de dessus")
        self.OptionParser.add_option('--liaison_sphere_plan_2D_dessus_orientation_sphere', action = 'store', type = 'float', dest = 'liaison_sphere_plan_2D_dessus_orientation_sphere', default = '0', help = u"Directions quelconque de l'axe de la sphère de la Sphère-plan 2D vue de dessus")
        
        self.OptionParser.add_option('--liaison_sphere_plan_3D_position_x', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison sphère-plan 3D")
        self.OptionParser.add_option('--liaison_sphere_plan_3D_position_y', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison sphère-plan 3D")
        self.OptionParser.add_option('--liaison_sphere_plan_3D_position_z', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_type_normale', action = 'store', type = 'str', dest = 'liaison_sphere_plan_3D_type_normale', default = "liaison_sphere_plan_3D_type_normale_standard", help = u"Choix du type de normale de la liaison Sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_axe_normale', action = 'store', type = 'str', dest = 'liaison_sphere_plan_3D_axe_normale', default = 'x', help = u"Orientations standard de l'axe de la sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_normale_quelconque_x', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_normale_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de la sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_normale_quelconque_y', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_normale_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de la sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_normale_quelconque_z', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_normale_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de la sphère-plan 3D")
        self.OptionParser.add_option('--liaison_sphere_plan_3D_rotation_plan', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_rotation_plan', default = 0, help = u"Orientation en degres du plan autour de la normale de la sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_type_direction_sphere', action = 'store', type = 'str', dest = 'liaison_sphere_plan_3D_type_direction_sphere', default = 'liaison_sphere_plan_3D_type_direction_sphere_standard', help = u"Type de direction de l'axe de la sphère de la sphère-plan 3D")
	self.OptionParser.add_option('--liaison_sphere_plan_3D_axe_sphere', action = 'store', type = 'str', dest = 'liaison_sphere_plan_3D_axe_sphere', default = 'x', help = u"Orientations standard de l'axe de la sphère de la sphère-plan 3D")
        self.OptionParser.add_option('--liaison_sphere_plan_3D_direction_sphere_quelconque_x', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_direction_sphere_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de la tige de sphere de la sphère-plan 3D")
        self.OptionParser.add_option('--liaison_sphere_plan_3D_direction_sphere_quelconque_y', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_direction_sphere_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de la tige de sphere de la sphère-plan 3D")
        self.OptionParser.add_option('--liaison_sphere_plan_3D_direction_sphere_quelconque_z', action = 'store', type = 'float', dest = 'liaison_sphere_plan_3D_direction_sphere_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de la tige de sphere de la sphère-plan 3D")

	#LIAISON RECTILIGNE **********************************************
        self.OptionParser.add_option('--liaison_rectiligne_type', action = 'store', type = 'string', dest = 'liaison_rectiligne_type', default = 'liaison_rectiligne_2D_cote', help = u"Type de representation de la liaison rectiligne")
        
        self.OptionParser.add_option('--liaison_rectiligne_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_cote_x', default = '0', help = u"Position sur X de la liaison rectiligne 2D coté relativement a l'origine")
	self.OptionParser.add_option('--liaison_rectiligne_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_cote_y', default = '0', help = u"Position sur Y de la liaison rectiligne 2D coté relativement a l'origine")       
        self.OptionParser.add_option('--liaison_rectiligne_cote_axe_normale', action = 'store', type = 'string', dest = 'liaison_rectiligne_cote_axe_normale', default = 'y', help = u"Principales directions de la normale de la liaison rectiligne 2D vue de coté")
        self.OptionParser.add_option('--liaison_rectiligne_2D_cote_orientation_normale', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_cote_orientation_normale', default = '0', help = u"Orientation de la normale de la liaison rectiligne 2D (coté) en degres")
       
        self.OptionParser.add_option('--liaison_rectiligne_2D_bout_x', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_bout_x', default = '0', help = u"Position sur X de la liaison rectiligne 2D vue du bout relativement a l'origine")
	self.OptionParser.add_option('--liaison_rectiligne_2D_bout_y', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_bout_y', default = '0', help = u"Position sur Y de la liaison rectiligne 2D vue du bout relativement a l'origine")
        self.OptionParser.add_option('--liaison_rectiligne_bout_axe_normale', action = 'store', type = 'string', dest = 'liaison_rectiligne_bout_axe_normale', default = 'y', help = u"Principales directions de la normale de la liaison rectiligne 2D vue du bout")
        self.OptionParser.add_option('--liaison_rectiligne_2D_bout_orientation_normale', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_bout_orientation_normale', default = '0', help = u"Orientation de la normale de la liaison rectiligne 2D (bout) en degres")
        self.OptionParser.add_option('--liaison_rectiligne_bout_axe_prisme', action = 'store', type = 'string', dest = 'liaison_rectiligne_bout_axe_prisme', default = 'y', help = u"Principales directions du prisme de la liaison rectiligne 2D vue du bout")
        self.OptionParser.add_option('--liaison_rectiligne_2D_bout_orientation_prisme', action = 'store', type = 'float', dest = 'liaison_rectiligne_2D_bout_orientation_prisme', default = '0', help = u"Orientation du prisme de la liaison rectiligne 2D (bout) en degres")
        
        self.OptionParser.add_option('--liaison_rectiligne_3D_position_x', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison rectiligne 3D")
        self.OptionParser.add_option('--liaison_rectiligne_3D_position_y', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison rectiligne 3D")
        self.OptionParser.add_option('--liaison_rectiligne_3D_position_z', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_type_normale', action = 'store', type = 'str', dest = 'liaison_rectiligne_3D_type_normale', default = 'liaison_rectiligne_3D_type_normale_standard', help = u"Choix du type de normale de la liaison rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_axe_normale', action = 'store', type = 'str', dest = 'liaison_rectiligne_3D_axe_normale', default = 'z', help = u"Orientations standard de l'axe de la rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_normale_quelconque_x', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_normale_quelconque_x', default = 0, help = u"Coordonnee sur x du vecteur directeur de la normale rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_normale_quelconque_y', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_normale_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de la normale rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_normale_quelconque_z', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_normale_quelconque_z', default = 1, help = u"Coordonnee sur z du vecteur directeur de la normale rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_type_direction', action = 'store', type = 'str', dest = 'liaison_rectiligne_3D_type_direction', default = 'liaison_rectiligne_3D_type_direction_standard', help = u"Choix du type de direction de la liaison rectiligne 3D")
	self.OptionParser.add_option('--liaison_rectiligne_3D_axe_direction', action = 'store', type = 'str', dest = 'liaison_rectiligne_3D_axe_direction', default = 'x', help = u"Orientations standard de la direction de la rectiligne 3D")
        self.OptionParser.add_option('--liaison_rectiligne_3D_direction_quelconque_x', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_direction_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de la direction rectiligne 3D")
        self.OptionParser.add_option('--liaison_rectiligne_3D_direction_quelconque_y', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_direction_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de la direction rectiligne 3D")
        self.OptionParser.add_option('--liaison_rectiligne_3D_direction_quelconque_z', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_direction_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de la direction rectiligne 3D")
        self.OptionParser.add_option('--liaison_rectiligne_3D_inclinaison_prisme', action = 'store', type = 'float', dest = 'liaison_rectiligne_3D_inclinaison_prisme', default = '0', help = u"Orientation du prisme en degres")

	#LIAISON SPHERE-CYLINDRE *****************************************
        self.OptionParser.add_option('--liaison_sphere_cylindre_type', action = 'store', type = 'string', dest = 'liaison_sphere_cylindre_type', default = 'liaison_sphere_cylindre_2D_cote', help = u"Type de representation de la liaison sphère-cylindre")
        
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_cote_x', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_cote_x', default = '0', help = u"Position sur X de la liaison sphère-cylindre 2D coté relativement a l'origine")
	self.OptionParser.add_option('--liaison_sphere_cylindre_2D_cote_y', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_cote_y', default = '0', help = u"Position sur Y de la liaison sphère-cylindre 2D coté relativement a l'origine")       
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_cote_axe', action = 'store', type = 'string', dest = 'liaison_sphere_cylindre_2D_cote_axe', default = 'x', help = u"Principales directions de la direction de la liaison sphère-cylindre 2D vue de coté")
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_cote_orientation_axe', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_cote_orientation_axe', default = '0', help = u"Orientation de la direction de la liaison sphère-cylindre 2D (coté) en degres")
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_cote_axe_sphere', action = 'store', type = 'string', dest = 'liaison_sphere_cylindre_2D_cote_axe_sphere', default = 'normal', help = u"Principales directions de la sphère pour la liaison sphère-cylindre 2D vue de coté")
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_cote_orientation_axe_sphere', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_cote_orientation_axe_sphere', default = '0', help = u"Orientation de la sphère de la liaison sphère-cylindre 2D (coté) en degres")
        
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_bout_x', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_bout_x', default = '0', help = u"Position sur X de la liaison sphère-cylindre 2D vue du bout relativement a l'origine")
	self.OptionParser.add_option('--liaison_sphere_cylindre_2D_bout_y', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_bout_y', default = '0', help = u"Position sur Y de la liaison sphère-cylindre 2D vue du bout relativement a l'origine")       
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_bout_axe_base', action = 'store', type = 'string', dest = 'liaison_sphere_cylindre_2D_bout_axe_base', default = 'y', help = u"Principales directions de la direction de la liaison sphère-cylindre 2D vue du bout")
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_bout_orientation_axe_base', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_bout_orientation_axe_base', default = '0', help = u"Orientation de la direction de la base de la liaison sphère-cylindre 2D (bout) en degres")
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_bout_axe_sphere', action = 'store', type = 'string', dest = 'liaison_sphere_cylindre_2D_bout_axe_sphere', default = 'normal', help = u"Principales directions de la sphère pour la liaison sphère-cylindre 2D vue du bout")
        self.OptionParser.add_option('--liaison_sphere_cylindre_2D_bout_orientation_axe_sphere', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_2D_bout_orientation_axe_sphere', default = '0', help = u"Orientation de la sphère de la liaison sphère-cylindre 2D (bout) en degres")
        
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_position_x', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_position_x', default = 0, help = u"Coordonnee sur x du centre de la liaison Sphère-Cylindre 3D")
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_position_y', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_position_y', default = 0, help = u"Coordonnee sur y du centre de la liaison Sphère-Cylindre 3D")
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_position_z', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_position_z', default = 0, help = u"Coordonnee sur z du centre de la liaison Sphère-Cylindre 3D")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_type_axe', action = 'store', type = 'str', dest = 'liaison_sphere_cylindre_3D_type_axe', default = 'liaison_sphere_cylindre_3D_type_standard', help = u"Choix du type d'axe de la liaison Sphère-Cylindre 3D")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_axe', action = 'store', type = 'str', dest = 'liaison_sphere_cylindre_3D_axe', default = 'x', help = u"Orientations standard de l'axe de la Sphère-Cylindre 3D")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_axe_quelconque_x', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_axe_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de l'axe de Sphère-Cylindre 3D")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_axe_quelconque_y', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_axe_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de l'axe de Sphère-Cylindre 3D")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_axe_quelconque_z', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_axe_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de l'axe de Sphère-Cylindre 3D")
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_rotation_cylindre', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_rotation_cylindre', default = '0', help = u"Rotation (en degrés) du cylindre autour de son axe")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_type_direction_sphere', action = 'store', type = 'str', dest = 'liaison_sphere_cylindre_3D_type_direction_sphere', default = 'liaison_sphere_cylindre_3D_type_standard', help = u"Choix du type d'axe pour la sphère de la liaison Sphère-Cylindre 3D")
	self.OptionParser.add_option('--liaison_sphere_cylindre_3D_axe_sphere', action = 'store', type = 'str', dest = 'liaison_sphere_cylindre_3D_axe_sphere', default = 'x', help = u"Orientations standard de l'axe de la sphère de la Sphère-Cylindre 3D")
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_direction_sphere_quelconque_x', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_direction_sphere_quelconque_x', default = 0, help = u"Coordonnee sur x du vecteur directeur de l'axe de la sphère de la Sphère-Cylindre 3D")
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_direction_sphere_quelconque_y', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_direction_sphere_quelconque_y', default = 0, help = u"Coordonnee sur y du vecteur directeur de l'axe de la sphère de la Sphère-Cylindre 3D")
        self.OptionParser.add_option('--liaison_sphere_cylindre_3D_direction_sphere_quelconque_z', action = 'store', type = 'float', dest = 'liaison_sphere_cylindre_3D_direction_sphere_quelconque_z', default = 0, help = u"Coordonnee sur z du vecteur directeur de l'axe de la sphère de la Sphère-Cylindre 3D")
	
	
	#LIAISON MASSE *****************************************
        self.OptionParser.add_option('--liaison_masse_type', action = 'store', type = 'string', dest = 'liaison_masse_type', default = 'liaison_masse_2D', help = u"Type de representation de la masse du référentiel.")
        
        self.OptionParser.add_option('--liaison_masse_2D_x', action = 'store', type = 'float', dest = 'liaison_masse_2D_x', default = '0', help = u"Position sur X du référentiel 2D relativement a l'origine.")
	self.OptionParser.add_option('--liaison_masse_2D_y', action = 'store', type = 'float', dest = 'liaison_masse_2D_y', default = '0', help = u"Position sur Y du référentiel 2D relativement a l'origine.")       
        self.OptionParser.add_option('--liaison_masse_2D_axe', action = 'store', type = 'string', dest = 'liaison_masse_2D_axe', default = 'x', help = u"Principales directions de la tige de la masse 2D")
        self.OptionParser.add_option('--liaison_masse_2D_orientation_axe', action = 'store', type = 'float', dest = 'liaison_masse_2D_orientation_axe', default = '0', help = u"Orientation de la direction de la tige du referentiel 2D en degres")
        
        self.OptionParser.add_option('--liaison_masse_3D_position_x', action = 'store', type = 'float', dest = 'liaison_masse_3D_position_x', default = 0, help = u"Coordonnee sur x du référentiel 3D")
        self.OptionParser.add_option('--liaison_masse_3D_position_y', action = 'store', type = 'float', dest = 'liaison_masse_3D_position_y', default = 0, help = u"Coordonnee sur y du référentiel 3D")
        self.OptionParser.add_option('--liaison_masse_3D_position_z', action = 'store', type = 'float', dest = 'liaison_masse_3D_position_z', default = 0, help = u"Coordonnee sur z du référentiel 3D")
        self.OptionParser.add_option('--liaison_masse_3D_type_axe', action = 'store', type = 'str', dest = 'liaison_masse_3D_type_axe', default = 'liaison_masse_3D_type_standard', help = u"Choix du type de direction de la tige du référentiel 3D")
	self.OptionParser.add_option('--liaison_masse_3D_axe', action = 'store', type = 'str', dest = 'liaison_masse_3D_axe', default = 'x', help = u"Orientations standard de la tige du referentiel 2D")
	self.OptionParser.add_option('--liaison_masse_3D_axe_quelconque_x', action = 'store', type = 'float', dest = 'liaison_masse_3D_axe_quelconque_x', default = 1, help = u"Coordonnee sur x du vecteur directeur de la tige du referentiel 3D")
	self.OptionParser.add_option('--liaison_masse_3D_axe_quelconque_y', action = 'store', type = 'float', dest = 'liaison_masse_3D_axe_quelconque_y', default = 1, help = u"Coordonnee sur y du vecteur directeur de la tige du referentiel 3D")
	self.OptionParser.add_option('--liaison_masse_3D_axe_quelconque_z', action = 'store', type = 'float', dest = 'liaison_masse_3D_axe_quelconque_z', default = 1, help = u"Coordonnee sur z du vecteur directeur de la tige du referentiel 3D")
        self.OptionParser.add_option('--liaison_masse_3D_pivotement', action = 'store', type = 'float', dest = 'liaison_masse_3D_pivotement', default = '0', help = u"Rotation (en degrés) de la masse autour de sa tige")	
	self.OptionParser.add_option('--liaison_masse_3D_representation', action = 'store', type = 'inkbool', dest = 'liaison_masse_3D_representation', default = 'False', help = u"Représentation 3D de la masse, en dessin 3D")
        
        
        
        #OPTIONS GENERALES ******************************************
        self.OptionParser.add_option('--opt_generales', action = 'store', type = 'string', dest = 'opt_generales', default = 'opt_gene_origine', help = u"Onglet des options generales")
        
        self.OptionParser.add_option('--opt_gene_inverse', action = 'store', type = 'inkbool', dest = 'opt_gene_inverse', default = 'False', help = u"Inverse les parametres piece 1 / piece 2")
        self.OptionParser.add_option('--opt_gene_gene_old', action = 'store', type = 'inkbool', dest = 'opt_gene_gene_old', default = 'False', help = u"Utilisation des anciennes normes")
        
        self.OptionParser.add_option('--x0', action = 'store', type = 'float', dest = 'x0', default = 0, help = u"Origine (2D) du repere (sur x)")
        self.OptionParser.add_option('--y0', action = 'store', type = 'float', dest = 'y0', default = 0, help = u"Origine (2D) du repere (sur y)")
        self.OptionParser.add_option('--longueur_base', action = 'store', type = 'float', dest = 'longueur_base', default = 1, help = u"Longueur des vecteur unitaire de la base")
        self.OptionParser.add_option('--unite_base', action = 'store', type = 'string', dest = 'unite_base', default = "cm", help = u"Unité dans laquelle est exprimé la longueur de la base.")
        self.OptionParser.add_option('--echelle', action = 'store', type = 'float', dest = 'echelle', default = 1, help = u"Coefficient d'echelle pour les liaisons")
        self.OptionParser.add_option('--opt_gene_echelle_epaisseurs', action = 'store', type = 'inkbool', dest = 'opt_gene_echelle_epaisseurs', default = 'False', help = u"L'echelle affecte (ou pas) les épaisseurs")


        self.OptionParser.add_option('--opt_gene_lignes_epaisseur_1', action = 'store', type = 'float', dest = 'opt_gene_lignes_epaisseur_1', default = 1, help = u"Epaisseur des traits de la piece 1")
        self.OptionParser.add_option('--opt_gene_lignes_epaisseur_2', action = 'store', type = 'float', dest = 'opt_gene_lignes_epaisseur_2', default = 1, help = u"Epaisseur des traits de la piece 2")
        
        self.OptionParser.add_option('--opt_gene_piece1_couleur', action = 'store', type = 'int', dest = 'opt_gene_piece1_couleur', default = 16711680, help = u"Couleur de la piece 1")
        self.OptionParser.add_option('--opt_gene_piece2_couleur', action = 'store', type = 'int', dest = 'opt_gene_piece2_couleur', default = 65280, help = u"Couleur de la piece 2")






    def effect(self):
        """
        Effect behaviour.
        Overrides base class' method and inserts "Hello World" text into SVG document.
        """
        # Get script's "--what" option value.
        liaison=self.options.liaison
        self.options.credits=u"Auteur : Raphaël ALLAIS (Lycee G.Eiffel de DIJON) - Éduscol"
        self.options.effect=self	#On passe la référence de l'objet effect dans les options pour y avoir acces dans les fonctions qui ne sont pas membre

        # Get access to main SVG document element and get its dimensions.
        svg = self.document.getroot()
        
        # Again, there are two ways to get the attibutes:
        width  = self.unittouu(svg.get('width'))
        height = self.unittouu(svg.attrib['height'])

	#Conversion des couleurs dans un format correct
	self.options.opt_gene_piece1_couleur=convertIntColor2Hex(self.options.opt_gene_piece1_couleur)
	self.options.opt_gene_piece2_couleur=convertIntColor2Hex(self.options.opt_gene_piece2_couleur)
	
	# Inversion des paramètres pièce 1 / pièce 2
	if self.options.opt_gene_inverse :
		self.options.opt_gene_piece1_couleur, self.options.opt_gene_piece2_couleur = self.options.opt_gene_piece2_couleur , self.options.opt_gene_piece1_couleur
		self.options.opt_gene_lignes_epaisseur_1, self.options.opt_gene_lignes_epaisseur_2 = self.options.opt_gene_lignes_epaisseur_2, self.options.opt_gene_lignes_epaisseur_1
		
	#Echelle des epaisseurs
	if self.options.opt_gene_echelle_epaisseurs :
		self.options.opt_gene_lignes_epaisseur_1 *= self.options.echelle
		self.options.opt_gene_lignes_epaisseur_2 *= self.options.echelle
        # Create a new layer.
        #groupe = inkex.etree.SubElement(svg, 'g')
        
	#Dessin :
	if liaison == "\"liaison_pivot\"" :
		type_liaison=self.options.liaison_pivot_type
		if(type_liaison=="\"liaison_pivot_2D_cote\""):
			dessin_Pivot_2D_cote(self.options,svg)
		elif(type_liaison=="\"liaison_pivot_2D_face\""):
			dessin_Pivot_2D_face(self.options,svg)
		elif(type_liaison=="\"liaison_pivot_3D\""):
			dessin_Pivot_3D(self.options,svg)
	if liaison == "\"liaison_pivot_glissant\"" :
		type_liaison=self.options.liaison_pivot_glissant_type
		if(type_liaison=="\"liaison_pivot_glissant_2D_cote\""):
			dessin_Pivot_Glissant_2D_cote(self.options,svg)
		elif(type_liaison=="\"liaison_pivot_glissant_2D_face\""):
			dessin_Pivot_Glissant_2D_face(self.options,svg)
		elif(type_liaison=="\"liaison_pivot_glissant_3D\""):
			dessin_Pivot_Glissant_3D(self.options,svg)
	if liaison == "\"liaison_glissiere\"" :
		type_liaison=self.options.liaison_glissiere_type
		if(type_liaison=="\"liaison_glissiere_2D_cote\""):
			dessin_Glissiere_2D_cote(self.options,svg)
		if(type_liaison=="\"liaison_glissiere_2D_face\""):
			dessin_Glissiere_2D_face(self.options,svg)
		if(type_liaison=="\"liaison_glissiere_3D\""):
			dessin_Glissiere_3D(self.options,svg)
	if liaison == "\"liaison_plane\"" :
		type_liaison=self.options.liaison_plane_type
		if(type_liaison=="\"liaison_plane_2D_cote\""):
			dessin_plane_2D_cote(self.options,svg)
		if(type_liaison=="\"liaison_plane_2D_dessus\""):
			dessin_plane_2D_dessus(self.options,svg)
		if(type_liaison=="\"liaison_plane_3D\""):
			dessin_plane_3D(self.options,svg)
	if liaison == "\"liaison_spherique\"" :
		type_liaison=self.options.liaison_spherique_type
		if(type_liaison=="\"liaison_spherique_2D\""):
			dessin_spherique_2D(self.options,svg)
		if(type_liaison=="\"liaison_spherique_3D\""):
			dessin_spherique_3D(self.options,svg)
	if liaison == "\"liaison_helicoidale\"" :
		type_liaison=self.options.liaison_helicoidale_type
		if(type_liaison=="\"liaison_helicoidale_2D_cote\""):
			dessin_helicoidale_2D_cote(self.options,svg)
		if(type_liaison=="\"liaison_helicoidale_2D_face\""):
			dessin_helicoidale_2D_face(self.options,svg)
		if(type_liaison=="\"liaison_helicoidale_3D\""):
			dessin_helicoidale_3D(self.options,svg)
	if liaison == "\"liaison_sphere_plan\"" :
		type_liaison=self.options.liaison_sphere_plan_type
		if(type_liaison=="\"liaison_sphere_plan_2D_cote\""):
			dessin_sphere_plan_2D_cote(self.options,svg)
		if(type_liaison=="\"liaison_sphere_plan_2D_dessus\""):
			dessin_sphere_plan_2D_dessus(self.options,svg)
		if(type_liaison=="\"liaison_sphere_plan_3D\""):
			dessin_sphere_plan_3D(self.options,svg)
	if liaison == "\"liaison_rectiligne\"" :
		type_liaison=self.options.liaison_rectiligne_type
		if(type_liaison=="\"liaison_rectiligne_2D_cote\""):
			dessin_rectiligne_plan_2D_cote(self.options,svg)
		if(type_liaison=="\"liaison_rectiligne_2D_bout\""):
			dessin_rectiligne_2D_bout(self.options,svg)
		if(type_liaison=="\"liaison_rectiligne_3D\""):
			dessin_rectiligne_3D(self.options,svg)
	if liaison == "\"liaison_sphere_cylindre\"" :
		type_liaison=self.options.liaison_sphere_cylindre_type
		if(type_liaison=="\"liaison_sphere_cylindre_2D_cote\""):
			dessin_Sphere_Cylindre_2D_cote(self.options,svg)
		if(type_liaison=="\"liaison_sphere_cylindre_2D_bout\""):
			dessin_Sphere_Cylindre_2D_bout(self.options,svg)
		if(type_liaison=="\"liaison_sphere_cylindre_3D\""):
			dessin_Sphere_Cylindre_3D(self.options,svg)
	if liaison == "\"liaison_masse\"" :
		type_liaison=self.options.liaison_masse_type
		if(type_liaison=="\"liaison_masse_2D\""):
			dessin_Masse_2D(self.options,svg)
		if(type_liaison=="\"liaison_masse_3D\""):
			dessin_Masse_3D(self.options,svg)
			
		
		
		
		
	
	



	
	
# Create effect instance and apply it.
effect = Liaisons()
effect.affect()

