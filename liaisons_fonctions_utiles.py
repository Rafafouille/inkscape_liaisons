# -- coding: utf-8 --
import math

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
		
