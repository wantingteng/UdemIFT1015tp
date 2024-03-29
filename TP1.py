#Le TP1 a pour but de vous faire pratiquer les concepts suivants : les boucles, les tableaux, les structures, les abstractions procédurales,la décomposition fonctionnelle et les tests unitaires.
#Vous devez coder et tester un jeu graphique qui se joue en solitaire sur une grille carrée : le jeu de taquin. Le jeu de taquin est expliqué ici et vous pouvez le jouer sur le web.
#Le développement de votre programme doit se faire en Python à l'aide de l'environnement codeBoot.
#vous devez vous limiter aux aspects du langage que nous avons vus dans le cours jusqu'au chapitre sur les structures et tableaux inclusivement. Utilisez la version 3.1.11 ou plus récente de codeBoot.




#Wanting Teng     

# Ce programme écrit un JEU DE TAQUIN et utilise des tests unitaires pour 
# vérifier les fonctions



import tuiles

# Afficher l'image de taille 16x16 pixels

def afficherImage(x,y,image):
    
#Trouver la relation entre les coordonnées dans la grille de pixels et 
#les coordonnées représentées par la grille de tuiles
#appelez setPixel et, tableau colormap basé sur la relation trouvée

    for a in range(x,x+16):
        for b in range(y,y+16):
            tuiles.images[image]
        
            setPixel(a,b,tuiles.colormap[tuiles.images[image][b-y][a-x]])
            b+=1
    
#Afficher une tuile correspondant au numéro par l'image  

def afficherTuile(x,y,tuile):
    X=x*16
    Y=y*16
    afficherImage(X,Y,tuile)
    

#Pour les jeux d'une largeur de deux à quatre, affichez les coordonnées du clic. 
#C’est-à-dit pour confirmer les coordonnées d'une tuile en 2x2 , 3x3 ou 4x4.

def attendreClic():
    
    while True:
      
        if getMouse().button != 0:
           
            coordonneX=getMouse().x//16
            coordonneY=getMouse().y//16
            
            
            sleep(0.01)        
            return struct(x=coordonneX,y=coordonneY)
     
    
#dessiner un tableau au hasard 

def permutationAleatoire(n):    
    tab=[]
    for i in range(n):
        tab=tab+[i]
      
    for k in tab:
        j=math.floor(n*random())
        if j>=k:
            temp=tab[k]
            tab[k]=tab[j]
            tab[j]=temp
    
    return tab

# Le nombre retourné indique à quel point la valeur x n'est pas bien 
# ordonnée dans le tableau tab

def inversions(tab,x):   
    fois=0
    i=tab.index(x)
    while i<=len(tab)-1:
        if tab[i]<x and tab[i]!=0:
            fois+=1  
        i+=1
    
    return fois
    

# Déterminer si le jeu a une solution, lorsque la somme est paire, il y a une solution
def soluble(tab):
    somme=0
    x=1
    if len(tab)%2==0:
        for i in range(len(tab)):
            if tab[i]==0:
                r=i//math.sqrt(len(tab))+1
    
        while x<=len(tab)-1:
            
            somme+=inversions(tab,x)
            x+=1
    else:
        while x<=len(tab)-1:
            r=0
            somme+=inversions(tab,x)
            x+=1
            
    sommeTotal=somme+r
        
    if sommeTotal % 2 ==0:
        return True
    else:
        return False
        
        
# La fonction retourne un tableau de longeur largeur*largeur contenant 
# les entiers de 0 à largeur*largeur-1 qui correspond à une configuration 
# de tuile qui est soluble.    

def initial(largeur):
    setScreenMode(16*largeur,16*largeur)
    if largeur<=4 and largeur>=2:
        a=permutationAleatoire(largeur*largeur)
        if soluble(a)==True:
            
            return a
        
        else:
            return initial(largeur)
        

        
#La procédure principale du jeu

def taquin(largeur):
    
    #Afficher la grille des tuiles
    
    if largeur<=4 and largeur>=2:
        m=initial(largeur)  
        fois=0
        for y in range(largeur):          
            for x in range(largeur):
                afficherTuile(x,y,m[fois])
                if m[fois]==0:
                    i = fois
                    
                    #Déterminer les coordonnées de la tuile noire initiale(x0,y0)
                    
                    y0=i//largeur
                    x0=i-largeur*y0
                fois+=1
  
    #Lancer le jeu
   
    start=True
    while start:
        start=False
        
        
  # Les coordonnées du clic de souris    

        axeX=attendreClic().x
        axeY=attendreClic().y  
       
  #Si l'abscisse de la tuile cliquée est la même que l'abscisse de la tuile noire
        if axeX==x0:   
            afficherTuile(axeX,axeY,0)
            if axeY>y0:
                for i in range(y0,axeY):
                    afficherTuile(axeX,i,m[i*largeur+axeX+largeur])
                   
                    #tableau de mise à jour

                    m[i*largeur+axeX]=m[i*largeur+axeX+largeur]
                     
                m[axeY*largeur+axeX]=0
                
                    
            if axeY<y0 :              
                for j in range(axeY+1,y0+1):
                    afficherTuile(axeX,j,m[j*largeur+axeX-largeur])
      
                for j in range(y0,axeY,-1):   
            
                    #tableau de mise à jour
                
                    m[j*largeur+axeX]=m[j*largeur+axeX-largeur]
                    
                m[axeY*largeur+axeX]=0
                
  #Si l'ordonnée de la tuile cliquée est la même que l'ordonnée de la tuile noire 

        if axeY==y0:
                
            afficherTuile(axeX,axeY,0)
               
            if axeX>x0:
                for i in range(x0,axeX):
                    afficherTuile(i,axeY,m[axeY*largeur+i+1])
                     
                   #tableau de mise à jour
                
                    m[axeY*largeur+i]=m[axeY*largeur+i+1]
                                            
                m[axeY*largeur+axeX]=0
                  
                   
 
            if axeX<x0:
                for j in range(axeX+1,x0+1):
                    afficherTuile(j,axeY,m[axeY*largeur+j-1])
                        
                for j in range(x0,axeX,-1):
                    
                     #tableau de mise à jour
                        
                    m[axeY*largeur+j]=m[axeY*largeur+j-1]
                                            
                m[axeY*largeur+axeX]=0  
                
 #Mettre à jour les numéros de tuiles pour afficher les coordonnées zéro

        x0=axeX
        y0=axeY
     
 #Vérifiez si les conditions de réussite du jeu sont remplies
 #En cas de succès, affichez le message "Félicitations" et commencez un nouveau

        if m[largeur**2-1]!=0:
            start=True
        for i in range(largeur):
            for j in range(largeur):
                if i==largeur-1 and j== largeur-1:
                    pass
                elif m[i*largeur+j]!=i*largeur+j+1:
                    start=True
                    
    if start==False:
        alert('Toutes nos félicitations!!')
        taquin(largeur)  
        

# Test unitaire 

def testTaquin():
    
    setScreenMode(16,16)  
    
    #Tester la procedure " afficherImage"
    
    image=1
    afficherImage(0,0,image)
            
    
    assert exportScreen() ==str('#fff'*15+'#ccc'+'\n'+'#fff'*14+'#ccc'+'#888'
+'\n'+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+('#fff'*2+'#ccc'*5+'#080'*2+'#ccc'*5
+'#888'*2+'\n')*10+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+'#fff'+'#ccc'+'#888'*14
+'\n'+'#ccc'+'#888'*15)
    
     
    image=2
    afficherImage(0,0,image)
    assert exportScreen() ==str('#fff'*15+'#ccc'+'\n'+'#fff'*14+'#ccc'+'#888'
+'\n'+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+
'#888'*2+'\n')*2+('#fff'*2+'#ccc'*7+'#080'*2+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+('#fff'*2+'#ccc'*3+'#080'*
2+'#ccc'*7+'#888'*2+'\n')*2+('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2
+'\n')*2+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+'#fff'+'#ccc'+'#888'*14+'\n'+'#ccc'+
'#888'*15)
    
    image=3
    afficherImage(0,0,image)
    assert exportScreen() ==str('#fff'*15+'#ccc'+'\n'+'#fff'*14+'#ccc'+'#888'
+'\n'+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*7+'#080'*2+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*5+'#080'*4+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*7+'#080'*2+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+
'#fff'*2+'#ccc'*12+'#888'*2+'\n'+'#fff'+'#ccc'+'#888'*14+'\n'+'#ccc'+
'#888'*15)

    image=4
    afficherImage(0,0,image)
    assert exportScreen() ==str('#fff'*15+'#ccc'+'\n'+'#fff'*14+'#ccc'+'#888'
+'\n'+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+
('#fff'*2+'#ccc'*3+'#080'*2+'#ccc'*2+'#080'*2+'#ccc'*3+'#888'*2+'\n')*4+
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*7+'#080'*2+'#ccc'*3+'#888'*2+'\n')*4+
'#fff'*2+'#ccc'*12+'#888'*2+'\n'+'#fff'+'#ccc'+'#888'*14+'\n'+'#ccc'+
'#888'*15)                              
    
    image=5
    afficherImage(0,0,image)
    assert exportScreen() ==str('#fff'*15+'#ccc'+'\n'+'#fff'*14+'#ccc'+'#888'
+'\n'+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+    
('#fff'*2+'#ccc'*3+'#080'*2+'#ccc'*7+'#888'*2+'\n')*2+                               
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*7+'#080'*2+'#ccc'*3+'#888'*2+'\n')*2+                              
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+
'#fff'*2+'#ccc'*12+'#888'*2+'\n'+'#fff'+'#ccc'+'#888'*14+'\n'+'#ccc'+
'#888'*15)                                
    
    
    #Tester la procedure "afficherTuile"
    
    setScreenMode(16,16)  
    tuile=1
    afficherTuile(0,0,tuile)  
    
    assert exportScreen() ==str('#fff'*15+'#ccc'+'\n'+'#fff'*14+'#ccc'+'#888'
+'\n'+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+('#fff'*2+'#ccc'*5+'#080'*2+'#ccc'*5
+'#888'*2+'\n')*10+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+'#fff'+'#ccc'+'#888'*14
+'\n'+'#ccc'+'#888'*15)
    
    tuile=2
    afficherTuile(0,0,tuile)
    assert exportScreen() ==str('#fff'*15+'#ccc'+'\n'+'#fff'*14+'#ccc'+'#888'
+'\n'+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+
'#888'*2+'\n')*2+('#fff'*2+'#ccc'*7+'#080'*2+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+('#fff'*2+'#ccc'*3+'#080'
*2+'#ccc'*7+'#888'*2+'\n')*2+('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2
+'\n')*2+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+'#fff'+'#ccc'+'#888'*14+'\n'+'#ccc'+
'#888'*15)
        
    tuile=3
    afficherTuile(0,0,tuile)
    assert exportScreen() ==str('#fff'*15+'#ccc'+'\n'+'#fff'*14+'#ccc'+'#888'
+'\n'+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*7+'#080'*2+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*5+'#080'*4+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*7+'#080'*2+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+
'#fff'*2+'#ccc'*12+'#888'*2+'\n'+'#fff'+'#ccc'+'#888'*14+'\n'+'#ccc'+
'#888'*15)    
        
    tuile=4
    afficherTuile(0,0,tuile)
    assert exportScreen() ==str('#fff'*15+'#ccc'+'\n'+'#fff'*14+'#ccc'+'#888'
+'\n'+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+
('#fff'*2+'#ccc'*3+'#080'*2+'#ccc'*2+'#080'*2+'#ccc'*3+'#888'*2+'\n')*4+
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*7+'#080'*2+'#ccc'*3+'#888'*2+'\n')*4+
'#fff'*2+'#ccc'*12+'#888'*2+'\n'+'#fff'+'#ccc'+'#888'*14+'\n'+'#ccc'+
'#888'*15)    
        
    tuile=5
    afficherTuile(0,0,tuile)
    assert exportScreen() ==str('#fff'*15+'#ccc'+'\n'+'#fff'*14+'#ccc'+'#888'
+'\n'+'#fff'*2+'#ccc'*12+'#888'*2+'\n'+
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+    
('#fff'*2+'#ccc'*3+'#080'*2+'#ccc'*7+'#888'*2+'\n')*2+                               
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+
('#fff'*2+'#ccc'*7+'#080'*2+'#ccc'*3+'#888'*2+'\n')*2+                              
('#fff'*2+'#ccc'*3+'#080'*6+'#ccc'*3+'#888'*2+'\n')*2+
'#fff'*2+'#ccc'*12+'#888'*2+'\n'+'#fff'+'#ccc'+'#888'*14+'\n'+'#ccc'+
'#888'*15)    
 

 # Tester la procedure "permutationAleatoire(n)"
    
    assert permutationAleatoire(4)==[2,0,1,3] or [3,1,2,0]
    assert permutationAleatoire(4)==[2,3,0,1] or [1,0,3,2]
    assert permutationAleatoire(4)==[3,0,2,1] or [2,3,1,0]
    assert permutationAleatoire(9)==[3,8,7,1,0,5,4,2,6] or[2,1,6,3,4,5,0,7,8]
    assert permutationAleatoire(16)==[13,2,4,3,1,5,6,0,8,10,9,7,15,11,14,12] or [5,13,7,3,11,9,0,2,1,8,10,4,6,15,14,12]
    
    
    
    
    
    
 # Tester la fonction inversions(tab,x)   

    tab=[2,1,3,0,6,5,8,4,9,7]
    x=2
    y=3
    z=4
    a=5
    b=6
    assert inversions(tab,x)==1
    assert inversions(tab,y)==0
    assert inversions(tab,z)==0
    assert inversions(tab,a)==1
    assert inversions(tab,b)==2
 

 # Tester la fonction "soluble(tab)"
    
    assert soluble([5,3,0,7,8,2,4,1,6])==True
    assert soluble([0,1,2,7,4,3,6,5,8])==True
    assert soluble([14,1,11,3,4,5,13,7,8,9,15,2,12,0,6,10])==True
    assert soluble([13,7,15,5,2,4,6,10,8,9,11,3,12,0,14,1])==True
    assert soluble([1,2,3,0])==True
    
    
 # Tester la fonction "initial(largeur)"
    assert initial(2)==[2,0,1,3] or [3,1,2,0]
    assert initial(2)==[2,3,0,1] or [1,0,3,2]
    assert initial(2)==[3,0,2,1] or [2,3,1,0]
    assert initial(3)==[3,8,7,1,0,5,4,2,6] or[2,1,6,3,4,5,0,7,8]
    assert initial(4)==[13,2,4,3,1,5,6,0,8,10,9,7,15,11,14,12] or [5,13,7,3,11,9,0,2,1,8,10,4,6,15,14,12]
    
testTaquin()
