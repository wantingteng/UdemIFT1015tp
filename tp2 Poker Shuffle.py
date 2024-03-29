#tp2 Poker Shuffle
#Le TP2 a pour but de vous faire pratiquer les concepts suivants : les boucles, les tableaux, les fonctions, la décomposition fonctionnelle, le traitement d'événements et la programmation web.
#Le code que vous devez écrire (fichier tp2.py) implémente un jeu qui exécute dans l'environnement codeBoot et spécifiquement la version disponible sur Studium.
#Vous pouvez utiliser le code qui a été montré dans le cours mais vous ne devez pas utiliser du code provenant d'ailleurs, que ce soit du web, d'une autre personne ou même d'un assistant de programmation intelligent.


#Wanting Teng 
#2022/4/12


def init():
    
    main = document.querySelector('#main')
    
    text='<tr>'
    char=''
    
    #tableau pour afficher les images
    
    for i in range(5):
        for j in range(5):
            text=text+('<td id=\"case'+str(i*5+j)+
                   '\" onclick=\"clic('+str(i*5+j)+')\">'+
                  '<img src="http://codeboot.org/cards/empty.svg">'+'</td>')
        text=text+'<td id=\"point'+str(i)+'\">'+'</td>'+'</tr>'+'<tr>'
        
    #table d'enregistrement des partitions
    
    for m in range(5,10):
        char=char+'<td id=\"point'+str(m)+ '\">' +'</td>'           

        
    total=text+char+'<td id=\"point10\">'+'0'+'</td></tr>'
        
    backimg='"http://codeboot.org/cards/back.svg">'
    
    main.innerHTML="""
    
    <button onclick="init()">Nouvelle</br>partie</button>
    <table><tr>
<td id="case25" onclick="clic(25)"><img src="""+backimg+"""</td></tr></table>
    """+'<table>'+total+'</table>' +"""
        <style>
        #main table td {
        width: 70px;
        height: 98px;
        border-radius:5px;
        font-size:24px;
        border:0
 
        }
        
        #main table {
        float: left; 
        margin:20px;
        border-collapse: separate;
        border-spacing:5px;
         
        }
        
        #main table td img { width:100%;}
        
        #main button{float:left; margin:30px; font-size:15px; 
        border-radius:5px;}
        
      </style>
      
      """
   
    
def case(index):  #case(index) -->element(caseindex)
    return element('case'+str(index))


def point(index): #point(index) -->element(pointindex)
    return element('point'+str(index))


def element(id): 
    return document.querySelector('#'+id)




def clic(index):

    back='<img src="http://codeboot.org/cards/back.svg">'
    empty='<img src="http://codeboot.org/cards/empty.svg">'
    
    innerContent=case(index).innerHTML
  
    
    if case(index).hasAttribute('style' )==True:
        case(index).removeAttribute('style')
    
    
    elif innerContent!=empty:
            
        case(index).setAttribute('style', 'background-color: lime')
        
        if index != 25:
            case(25).removeAttribute('style')
        if index== 25:
            for i in range(25):
                case(i).removeAttribute('style') 
        
    #L'indice de la pioche est de 25
    if index==25: 
        
        if case(25).innerHTML==back: 
            
            case(25).innerHTML=linkUtile[0]  #start with index=0
            
            #Pour éviter les répétitions, utiliser un élément
            #et supprimer cet élément
            #linkUtile：Tableau de liens d'images (dans un ordre aléatoire)
            linkUtile.pop(0)   
          
            
    if case(25).hasAttribute('style')== True:
        
        if case(index).innerHTML==empty:
                case(index).innerHTML=case(25).innerHTML
                case(25).innerHTML=back
                case(25).removeAttribute('style')
                case(index).removeAttribute('style')
        
        
    else:
        for i in range(25):
            if case(i).hasAttribute('style' )==True:
                if case(i).innerHTML!=case(index).innerHTML:

                    temp=case(i).innerHTML
                    case(i).innerHTML=case(index).innerHTML
                    case(index).innerHTML=temp
                    case(index).removeAttribute('style')
                    case(i).removeAttribute('style')
                    
    #Appelez la fonction que j'utilise pour enregistrer le score              
    writeGrade(totalRecord())
   

    #enregistrer le score total   
    
    initNum=0 
    for i in range(10):
        if point(i).innerHTML !='':
            content=point(i).innerHTML
            initNum+=int(content)
    point(10).innerHTML=str(initNum)
    
    finalResult=point(10).innerHTML
    
    
    #afficher le score et recommencer
    fullPoker=True
    for j in range(25):
        if case(j).innerHTML==empty:
            fullPoker=False
    if fullPoker==True:
        alert('Votre pointage final est'+' '+finalResult)
        
        init()
  
        
    
#retourner une table originale[0-------52]  

def paquetCarte():
    result=[]
    for i in range(13):
        for j in range(4):
            result.append(i*4+j)
    return result

    
#melanger les elements dans la table

def melangerTab():
    tab=paquetCarte()
    fois=-1
    for i in tab[::-1]:
        num=int(random()*int(i)) #0--4
        temp=tab[num] 
        tab[num]=tab[fois]
        tab[fois]=temp
        fois-=1
        
    return tab    
   
    
    
#Tableau de liens d'images dans l'ordre

def matchCorrect(): 
    ori=paquetCarte()        #[0,1,2,3...........,50,51]
    sign=['H','S','C','D']*13
    resultat=[]
    for i in ori:
        if i>=0 and i<=3:
            resultat.append('<img src="http://codeboot.org/cards/A'+sign[i]
                            +'.svg">')
        elif i>3 and i<40 and i%4==0:
            for j in range(4):
                resultat.append('<img src="http://codeboot.org/cards/'
                                +str(int((i+j)//4)+1)+sign[j]+'.svg">')
        elif i>=40 and i<44:
            resultat.append('<img src="http://codeboot.org/cards/J'+sign[i]
                            +'.svg">')
        elif i>=44 and i<48:
            resultat.append('<img src="http://codeboot.org/cards/Q'+sign[i]
                            +'.svg">')
        elif i>=48 and i<52:
            resultat.append('<img src="http://codeboot.org/cards/K'+sign[i]
                            +'.svg">')
        
    return resultat  
                                       
def mixMatch():
    mat=matchCorrect()
    return list(map(lambda x:mat[x],melangerLinkTab))


#Les éléments de la matrice représentent les nombres correspondant aux cartes
#à jouer (dans l'ordre aléatoire)
#par exemple [4,5,2,8,34,25.............]

melangerLinkTab=melangerTab() 


#Tableau de liens d'images (ordonnés)

correctLink=matchCorrect()


#Tableau de liens d'images (dans un ordre aléatoire)

linkUtile=mixMatch() 


#Enregistrez le numéro correspondant à la carte dans chaque colonne du tableau 
#après chaque clic

def recordTabCol():
    result=[]
    for i in range(5):
        col=[] 
        for j in range(5):  
            for k in range(52):
                if correctLink[k]==case(i+j*5).innerHTML:
                    col.append(k)
                    
        result.append(col)
            
    return  result


#Enregistrez le numéro correspondant à la carte dans chaque ligne du tableau 
#après chaque clic

def recordTabRow():
    resulta=[]
    for i in range(5):
        row=[] 
        for j in range(5):  
            for k in range(52):
                if correctLink[k]==case(i*5+j).innerHTML:
                    row.append(k)
                    
        resulta.append(row)   
    return resulta



#Après avoir récapitulé chaque clic, les indices 0 à 4 représentent 
#les chiffres correspondant à chaque rangée de cartes, et les indices 5 à 9 
#correspondent aux chiffres correspondant à chaque colonne de cartes

def totalRecord():
    return recordTabRow()+recordTabCol()



#Organiser les éléments du tableau dans l'ordre

def arrangeEle(tab): 
    temp = 0
    for i in range(0, len(tab)):    
        for j in range(i+1, len(tab)):    
            if(tab[i] > tab[j]):    
                temp = tab[i]   
                tab[i] = tab[j]    
                tab[j] = temp
    return tab         
  
    
    
#Cette fonction est utilisée pour enregistrer le score   

def writeGrade(matrice):
    for i in matrice:
        if len(i)==0 or 1:
            point(matrice.index(i)).innerHTML=''
  
        if len(i)==2:
            point(matrice.index(i)).innerHTML=twoPoker(i)
                   
        if len(i)==3:
            
            point(matrice.index(i)).innerHTML=troisPoker(i)
            
        if len(i)==4:
            point(matrice.index(i)).innerHTML=fourPoker(i)
          
            
        if len(i)==5:
            point(matrice.index(i)).innerHTML=fivePoker(i)
           
            
            if point(matrice.index(i)).innerHTML=='':
                
                #Déterminez si trois des cinq cartes sont identiques
                
                for j in range(5):
                    m=i.pop(0)
                    point(matrice.index(i)).innerHTML=fourPoker(i)
                    i.append(m)
                    if point(matrice.index(i)).innerHTML=='10':
                       
                            break
                    
                    
               #Déterminez s'il y a deux paires dans cinq cartes
            
                if point(matrice.index(i)).innerHTML!='10':
                    for j in range(5):
                        m=i.pop(0)
                        point(matrice.index(i)).innerHTML=fourPoker(i)
                        i.append(m)
                        if point(matrice.index(i)).innerHTML=='5':
                            break
 

                #Déterminez s'il y a une paire dans cinq cartes     
                
                if point(matrice.index(i)).innerHTML!='10' and \
                                      point(matrice.index(i)).innerHTML!='5': 
                    for j in range(5):
                        m=i.pop(0)
                        point(matrice.index(i)).innerHTML=fourPoker(i)
                        i.append(m)
                        if point(matrice.index(i)).innerHTML=='2':
                            break
   
                
#Lorsqu'il n'y a que deux cartes à jouer dans chaque ligne ou colonne    

def twoPoker(tab):
    if tab[0]//4==tab[1]//4:
        val='2'
        return val
    else:
        val=''
        return val

    
#Lorsqu'il n'y a que trois cartes à jouer dans chaque ligne ou colonne

def troisPoker(tab):
    
    if tab[0]//4==tab[1]//4==tab[2]//4:
            value='10'
            return value
        
    for i in range(3):  
          if tab[i-1]//4==tab[i]//4:
            value='2'
            return value
         
    else:
            value=''
            return value
        
             

 #Lorsqu'il n'y a que quatre cartes à jouer dans chaque ligne ou colonne   

def fourPoker(tab):
    storeTab=tab 
    m=storeTab
    
    #Carré
    if tab[0]//4==tab[1]//4==tab[2]//4==tab[3]//4:
        value='50'
        return value
    
    # Brelan
    for j in range(4):
        n=tab.pop(0)

       
        if tab[0]//4==tab[1]//4==tab[2]//4:
            value='10'
            
            return value
        tab.append(n)
 
    #Double Paire   
    if (tab[0]//4==tab[1]//4 and tab[2]//4==tab[3]//4)or(tab[0]//4==tab[2]//4 \
                       and tab[1]//4==tab[3]//4 )or(tab[0]//4==tab[3]//4 and \
                                                   tab[1]//4==tab[2]//4):
        value='5'
        return value
    
    #Une Paire 
    for i in range(4):
        if tab[i-1]//4==tab[i]//4 or tab[i-3]//4==tab[i]//4 \
                                              or tab[i-2]//4==tab[i]//4:
            value='2'
            return value
    else:
        value=''
        return value

    
    
    
#Lorsqu'il n'y a que cinq cartes à jouer dans chaque ligne ou colonne    

def fivePoker(tab):
 
    #Full House
    tabNew=arrangeEle(tab)
    if (tabNew[0]//4==tabNew[1]//4 and tab[2]//4==tab[3]//4==tab[4]//4) or \
                tabNew[0]//4==tabNew[1]//4==tabNew[2]//4 and tab[3]//4==tab[4]//4:
        val='25'
        return val
    
    test=True
    royaleTest=True
    
    if tab[0]%4==tab[1]%4==tab[2]%4==tab[3]%4==tab[4]%4:
        if (tab[0]>=36 and tab[0]<=39):
            for i in range(len(tab)-1):
                if tab[i+1]-tab[i]!=4:
                    royaleTest=False
            if royaleTest==True:
                val='100'
                return val
            
        if (tab[0]>=0 and tab[0]<=3):
            for i in range(len(tab)-1):
                if tab[i]-tab[i+1]!=4:
                    royaleTest=False
            if royaleTest==True:
                val='100'
                return val
    
  
        for i in range(4):
            if tab[1]>tab[0]:
                if tab[i+1]-tab[i] !=4:
                    test=False
                
            if tab[1]<tab[0]:
                if tab[i]-tab[i+1] !=4:
                    test=False
                
        #Quinte Flush 
        if test==True:
            val='75'
            return val
        
        #Couleur ou Flush 
        else:
            val='20'
            return val
 
        
    #Quinte  
    testAnother=True  
    if tab[1]>tab[0]:
        for i in range(4):
        
            if tab[i+1]//4-tab[i]//4 !=1:
                testAnother=False
                
    if tab[1]<tab[0]:
        for i in range(4):
            if tab[i]//4-tab[i+1]//4 !=1:
                testAnother=False
            
    if testAnother==True and tab[0]>3 and tab[-1]>3:
        val='15'
        return val
    
    
    #Carré in 5 full pokers
    for j in range(5):
        m=tab.pop(0)
        if tab[0]//4==tab[1]//4==tab[2]//4==tab[3]//4:
            value='50'
            return value
        tab.append(m)
    
  
    else:
        value=''
        return value

    
  
    
init()








    
