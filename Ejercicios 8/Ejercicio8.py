import pandas as pd

def repeatNumbers(array):
    array_copy = array.copy()
    i = 0
    j = 1
    while i < len(array_copy) - 1:
        if array_copy[i] >= array_copy[j]:
            average = (array_copy[i] + array_copy[j]) / 2
            array_copy[i] = (average) - 0.1
            array_copy[j] = average
        i+=1
        j+=1        
    return array_copy


# Se lee el archivo con pandas
data = pd.read_csv('train.csv')
pMlength = []
pMwidth = []
keyWords = ['Iris-setosa','Iris-versicolor','Iris-virginica']
colLength = []
colWidth = []
for i, keyword in enumerate(keyWords):
    # Si la fila contiene la palabra, se guardan los primeros datos
    rows_select = data[data['class'] == keyword] 
    # Se necesita sacar el rango de cada especie
    print("\n", keyword, "\n")
    for index, row in rows_select.iterrows():
        colLength.append(row['petallength'])
        colWidth.append(row['petalwidth'])
        print("Los datos guardados fueron ", row['petallength'], " y ", row['petalwidth'])
    pMlength.append(min(colLength))
    pMlength.append(max(colLength))
    pMwidth.append(min(colWidth))
    pMwidth.append(max(colWidth))
    # Reiniciamos los arreglos de apoyo 
    colLength.clear()
    colWidth.clear()
print("\n-- Los limites de length son: --\n", pMlength)
print("\n-- Los limites de width son: --\n", pMwidth)
print("\nLímites corregidos\n")
lengthLimits = repeatNumbers(pMlength)
print("\n-- Los limites de length son: --\n", lengthLimits)
widthLimits = repeatNumbers(pMwidth)
print("\n-- Los limites de width son: --\n", widthLimits)
# Ahora se necesita clasificar el test por cada una de las columnas

col_test = ['petallength','petalwidth']
test = pd.read_csv('test.csv', usecols=col_test)
testr = pd.read_csv('test.csv')
testdata = pd.DataFrame(testr)
realData = testdata['class'].values
testLength = test['petallength']
testWidth = test['petalwidth']
# Predict length
j = 0
k = 1
arraypredictL = []
for i, value in enumerate(testLength):
    if value <= lengthLimits[1]:
        arraypredictL.append("Iris-setosa")
    elif value >= lengthLimits[2] and value <= lengthLimits[3]:
        arraypredictL.append("Iris-versicolor")
    elif value >= lengthLimits[4]:
        arraypredictL.append("Iris-virginica")

arraypredictW = []
for i, value in enumerate(testWidth):
    if value <= widthLimits[1]:
        arraypredictW.append("Iris-setosa")
    elif value >= widthLimits[2] and value <= widthLimits[3]:
        arraypredictW.append("Iris-versicolor")
    elif value >= widthLimits[4]:
        arraypredictW.append("Iris-virginica")
dataP = {'Clases reales': realData, 'Predict Length': arraypredictL, 'Predict Width': arraypredictW}
predicts = pd.DataFrame(dataP)
print("\n-------Resultados de las predicciones-------\n", predicts)