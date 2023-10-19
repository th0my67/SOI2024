#Input treatment
T = int(input()) 
"""Nombre de tests"""

temp_input = input().split()
"""Reception des données"""

n = int(temp_input[0])
"""Nombre de jours dans un mois de souris"""

m = int(temp_input[1])
"""Nombre d'evenements a planifier"""

k = int(temp_input[2]) 
"""Duree du camp"""

del temp_input


#Initialazing important variables
lst_nb_events = [0] * n
"""Liste avec le nombre d'evenements pour chaque jour"""
max_productivity_score=0
"""Score de productivite maximal"""


#Main loop
for num_test in range(T):
    #Storing the number of events for each day
    for i in range(m):
        l,r = input().split()
        for j in range(int(l),int(r)+1):
            lst_nb_events[j]+=1
    
    #Calculating the maximum productivity score
    max_productivity_score = max(map(lambda x: x*n, lst_nb_events))

    #Printing the result
    print("Case #{}: {}".format(num_test, max_productivity_score))

    #Resetting the variables
    lst_nb_events = [0] * n
    max_productivity_score=0


