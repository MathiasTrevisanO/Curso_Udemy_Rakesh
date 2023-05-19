from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import warnings

# remove os warnings do modelo
warnings.filterwarnings("ignore")

iris = load_iris()
# seleciona as entradas e saidas desejadas
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4, random_state= 42)


def main():
    print('Predição para classificação das plantas {}, {} e {}'.format(iris.target_names[0], 
                                                                       iris.target_names[1],
                                                                       iris.target_names[2]))
    print('\n\n Planta setosa = 0 \n Planta versicolor = 1 \n Planta virginica = 2 \n\n')
    
    logreg = LogisticRegression()
    logreg.fit(X_train,y_train)
    prediction = logreg.predict(X_test)
    print('Predição com regressão logística:\n',prediction) 
    print('\nAcurácia:', metrics.accuracy_score(y_test,prediction))
    
if __name__ == "__main__":
    main()