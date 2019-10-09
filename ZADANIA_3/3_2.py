L = [3, 5, 4]; L = L.sort() #Jest ok

x, y = 1, 2, 3 #za dużo wartości przypisywanych do zmiennych

X = 1, 2, 3 ; X[1] = 4 #w tuple nie można przypisywać nowych wartości elementom

X = [1, 2, 3] ; X[3] = 4 #przypisywana wartość byłaby poza rozmiarem kontenera

X = "abc" ; X.append("d") #string nie posiada funkcji 'append'

map(pow, range(8)) #pow przyjmuje dwa argumenty
