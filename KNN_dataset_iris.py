from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt


iris = load_iris()

# print(iris.data)
# print(iris.target)

# # O modelo fit deve receber valores de X e y sendo valores numericos numpy
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

# print(type(X))
# print(type(y))

def knn_one_neighbor():
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train,y_train)
    # # faz a predicao de qual planta será onde retorna valores de 0 a 2 em um vetor
    prediction = knn.predict(X_test)
    print('Acurácia:', metrics.accuracy_score(y_test,prediction))
    print('\n')
    return prediction

def knn_five_neighbors():
    knn5 = KNeighborsClassifier(n_neighbors=5)
    knn5.fit(X_train,y_train)
    prediction5 = knn5.predict(X_test)
    print('Acurácia:', metrics.accuracy_score(y_test,prediction5))
    print('\n')
    return prediction5

def knn_eight_neighbors():
    knn8 = KNeighborsClassifier(n_neighbors=8)
    knn8.fit(X_train,y_train)
    prediction8 = knn8.predict(X_test)
    print('Acurácia:', metrics.accuracy_score(y_test,prediction8))
    print('\n')
    return prediction8

def grafico(acuracia, neighbors):
    plt.figure(figsize=(16,6))
    plt.plot(neighbors, acuracia, color= 'b')
    plt.xlabel('K-Neighbors')
    plt.ylabel('Acurácia')
    plt.grid()
    plt.title("Acurácia para cada K-NN.")
    
def more_cases():
    neighbors = np.arange(1,31)
    prediction = []
    knn = []
    acuracia =[]
    
    for i in neighbors: 
        knn.append(KNeighborsClassifier(n_neighbors=i))
        knn[i-1].fit(X_train,y_train)
        prediction.append(knn[i-1].predict(X_test))
        print('Predição com {} neighbor(s): {}'.format(i,prediction[i-1]))
        acuracia.append(metrics.accuracy_score(y_test,prediction[i-1]))
        print('Acurácia:', acuracia[i-1])
        print('\n')
    print("Maior acurácia: {:.2f}\n".format(max([metrics.accuracy_score(y_test, p) for p in prediction])))
    
    grafico(acuracia, neighbors)


def grafico2(k_range,k_scores):
    plt.figure(figsize=(16,6))
    plt.plot(k_range, k_scores, color= 'r')
    plt.xlabel('K-Neighbors')
    plt.ylabel('Acurácia')
    plt.grid()
    plt.title("Cross-Validation para 45 neighbors.")
    plt.show()
    

def Kfold_cross_validation45():
    k_range = range(1,45)
    k_scores = []
    scores = [] #utilizando cross-validation
    for k in k_range:
        knn45 = KNeighborsClassifier(n_neighbors= k)
        scores = cross_val_score(knn45, X, y, cv=10, scoring='accuracy')
        k_scores.append(scores.mean())
    grafico2(k_range,k_scores) 
       

def main():
    print('Predição para classificação das plantas {}, {} e {}'.format(iris.target_names[0], 
                                                                       iris.target_names[1],
                                                                       iris.target_names[2]))
    print('\n\n Planta setosa = 0 \n Planta versicolor = 1 \n Planta virginica = 2 \n\n')
    print('Predição utilizando as dimensões [2,4,3,1],[4,6,5,3] para classificação das plantas.\n\n')
    pred1 = knn_one_neighbor()
    print('Predição com 1 neighbor:',pred1) 
    pred5 =  knn_five_neighbors()
    print('Predição com 5 neighbor:',pred5) 
    pred8 = knn_eight_neighbors()
    print('Predição com 8 neighbor:',pred8)
    print('\n\n\nPredição até 30 neighbors:\n')
    more_cases() 
    Kfold_cross_validation45()
    
if __name__ == "__main__":
    main()