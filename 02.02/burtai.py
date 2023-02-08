# Create a program which would take 5 separate sentences containing 5 words.
# Make those sentences in separate lists and sort them out (reverse=False)
# Create 5 five new lists what would contain first, second  indexed elements from those lists. (first list containing
# all first elements of those five, second list second elements and so on).
# print the length of all list items and print the longest lenght list and shortest.
pirmas = input("Sakinys is penkiu zodziu: ")
antras = input("Sakinys is penkiu zodziu: ")
trecias = input("Sakinys is penkiu zodziu: ")
ketvirtas = input("Sakinys is penkiu zodziu: ")
penktas  = input("Sakinys is penkiu zodziu: ")
listas_pirmas = []
listas_antras = []
listas_trecias = []
listas_ketvirtas = []
listas_penktas = []
# ilgis_pirmo = []
# ilgis_antro = []
# ilgis_trecio = []
# ilgis_ketvirto = []
# ilgis_penkto = []

# ilgis_pirmo.append(len(pirmas))
# ilgis_antro.append(len(antras))
# ilgis_trecio.append(len(trecias))
# ilgis_ketvirto.append(len(ketvirtas))
# ilgis_penkto.append(len(penktas))
listas_pirmas.append(pirmas)
listas_pirmas.append(len(pirmas))
listas_antras.append(antras)
listas_antras.append(len(antras))
listas_trecias.append(trecias)
listas_trecias.append(len(trecias))
listas_ketvirtas.append(ketvirtas)
listas_ketvirtas.append(len(ketvirtas))
listas_penktas.append(penktas)
listas_penktas.append(len(penktas))
bendras = []
bendras.append(listas_pirmas[-1])
bendras.append(listas_antras[-1])
bendras.append(listas_trecias[-1])
bendras.append(listas_ketvirtas[-1])
bendras.append(listas_penktas[-1])
max = max(bendras)
min = min(bendras)
l_max = []
l_min = []

for x in listas_pirmas ,listas_antras,listas_trecias,listas_ketvirtas,listas_penktas:
    if x[-1] == max:
        
        x.remove(x[-1])    
        x = str(x).replace("['",'').replace("']",'')
        l_max.append(str(x))
        
        
    elif x[-1] == min:
        
        x.remove(x[-1])
        x = str(x).replace("['",'').replace("']",'')
        l_min.append(str(x))
        
    else:
        pass

print("MAX: ", (l_max))
print("MIN: ", (l_min))