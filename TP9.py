import random as r




l1=[r.randint(-10,10) for i in range(10**3)] #Une seule liste est initialisée, les autres sont laissées de côté




def concaten(l, i, k, j):                    #La fonction sera appelée lors du travail sur la recursivité
    left_sum,right_sum = 10**99,10**99       #Les sommes minimales de part et d'autres de k sont majorées
    max_left,max_right=0,0                   #On initialise i0 et j0 (tels que l[i0:k] et l[k:j0] soient minima)
    
    sum=0
    for p in range(k,i-1,-1):                #Recherche de i0 pour former la somme minimale "à gauche" de k
        sum+=l[p]
        if sum < left_sum:
            left_sum = sum
            max_left = p
            
    sum=0
    for p in range(k+1,j+1):                 #Recherche de j0 pour former la somme minimale "à droite" de k
        sum+=l[p]
        if sum < right_sum:
            right_sum = sum
            max_right = p
                                             #On retourne i0,j0, et la somme des sommes minimale "à droite" et "à gauche"
    return max_left, max_right, left_sum+right_sum




def recurs(l,low,high):                      #Soit low (resp high) le premier (resp dernier) indice de la portion de la liste
                                             #que l'on souhaite étudier
                                             #L'appel à la fonction pour une liste l complète se fait donc sour la forme :
                                             #recurs(l,0,len(l)-1)
                                             
    if low==high:                            #Si la portion étudiée ne contient qu'un seul terme
        return low,high,l[low]               #Alors on renvoit son rang et sa valeur
    
    k=((high+low)//2)                        #On coupe la portion de liste étudiée en deux
    
    left_low,left_high,a1=recurs(l,low,k)                     #On applique la récursivité à l[low:k]
    right_low,right_high,a2=recurs(l,k+1,high)                #On applique la récursivité à l[k:high]
    cross_low,cross_high,a3=concaten(l,low,k,high)            #On trouve i0, j0, et la somme de termes de la sous-liste l[i0:j0] formée par
                                                              #concaténation des listes de somme minimales "à gauche" et "à droite" de k
    
    if min(a1,a2,a3)==a1:                    #Si une partie de la sous liste l[low:k] forme la somme minimale
        return left_low,left_high,a1         #On retourne les indices de cette partie, ainsi que la somme formée
    elif min(a1,a2,a3)==a2:                  #De même pour l[k:high] 
        return right_low,right_high,a2
    return cross_low,cross_high,a3           #De même pour l[i0:j0]



def lineaire(l):                             #Algorithme au coût linéaire, pour vérifier les resultats
    c=l[0]
    m=l[0]
    for i in range(len(l)):
        c=min(c+l[i],l[i])
        m=min(m,c)
    return m
