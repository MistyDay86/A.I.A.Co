import random
import os
import string
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.utils import to_categorical
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import scikeras
from scikeras.wrappers import KerasRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

df.to_excel('Sentenze_Random_Labelled.xlsx')
df.drop('Unnamed: 0', inplace=True, axis=1)
df.dropna(inplace=True)
df["Percentuale di riduzione richiesta rispetto al totale della rata"].replace("no", 0, inplace=True)
df["Mensilità cauzione"].replace("no", 0, inplace=True)
df["Importo misure di sostegno"].replace("no", 0, inplace=True)
df["Percentuale credito d'imposta"].replace("no", 0, inplace=True)
df["Periodicità del canone"].replace("mensili", 12, inplace=True)
df["Periodicità del canone"].replace("semestrali", 2, inplace=True)
df["Periodicità del canone"].replace("annuali", 1, inplace=True)
df.drop("Descrizione attività", axis=1, inplace=True)
df.drop("Comune del locale", axis=1, inplace=True)
df.drop("Natura delle garanzie", axis=1, inplace=True)

columns = {'Natura del locatore':'Nature of the owner', 'Natura del conduttore':'Nature of the tenant', 'Qualità del locatore': 'Quality of the owner',
           'Qualità del conduttore': 'Quality of the tenant', 'Unica fonte di reddito?':'Only source of income?','Quantifica riduzione richiesta?':'Does the tenant quantify the reduction in his demand? ',
           'Eventuale diritto di recesso': 'Right of withdrawal', 'Eventuale clausola risolutiva':'Termination clause', 'Eventuale presenza di garanzie':'Presence of guarantees ',
           'Eventuali misure di sostegno':'Income support measures','Eventuale credito d’imposta':'Tax credit', 'Percentuale dell’affitto rispetto a reddito totale':'Percentage of rent compared to the tenant total income',
           'Percentuale di perdita degli incassi rispetto al totale dei redditi del conduttore':'Percentage of loss in relation to the tenant total income',
           'Percentuale di riduzione richiesta rispetto al totale della rata':'Percentage of requested reduction compared to rental fee',
       'Destinazione del locale commerciale (ATECO)':'Description of the activity',
       'Importo affitto mensile':'Monthly rent amount', 'Periodicità del canone':'Frequency of the rental fee',
       'Importo pagamento del canone':'Amount payment of rental fee',
       'Per quante rate si chiede la riduzione':'For how many rents the reduction is requested','Mensilità cauzione':'Monthly deposit','Importo misure di sostegno':'Amount of support measures','Percentuale credito d\'imposta':'Percentage of tax credit', 'Sentenza':'Verdict'}
df.rename(columns = columns, inplace = True)


# constant prediction

def constant_model():
    mean_abs_error_const = []
    for i in range(0,101):
      df_const = df["Verdict"]
      cont = 0
      for j in range(556):
        cont+= np.abs(df["Verdict"].iloc[j]-(i/100))
      mean_abs_error_const.append(cont/556)
    return mean_abs_error_const

# average and median prediction

def median_model():
    mean = df['Verdict'].mean()
    median = df['Verdict'].median()

    cont_1 = 0
    cont_2 = 0
    for i in range(556):
        cont_1 += np.abs(df["Verdict"].iloc[i] - mean)
        cont_2 += np.abs(df["Verdict"].iloc[i] - median)

    return cont_1/556, cont_2/556

# regression model

def regression_model():

    X = pd.get_dummies(data=df, drop_first=True)
    y = df["Verdict"]
    X = X.drop("Verdict", axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, df['Verdict'], test_size=0.2, random_state=101)

    def baseline_model():
        # create model
        model = Sequential()
        model.add(Dense(50, input_dim=21, kernel_initializer='normal', activation='relu'))
        model.add(Dense(50, kernel_initializer='normal', activation='relu'))
        model.add(Dense(50, kernel_initializer='normal', activation='relu'))
        # model.add(Dense(32, kernel_initializer='normal', activation='relu'))
        # model.add(Dense(16, kernel_initializer='normal', activation='relu'))
        # model.add(Dense(8, kernel_initializer='normal', activation='relu'))
        # model.add(Dense(4, kernel_initializer='normal', activation='relu'))
        # model.add(Dense(64, kernel_initializer='normal', activation='relu'))
        # model.add(Dense(100, kernel_initializer='normal', activation='relu'))
        model.add(Dense(1, kernel_initializer='normal', activation='linear'))
        # Compile model
        model.compile(loss='mean_squared_error', optimizer='adam')
        return model

    # evaluate model
    model = baseline_model()
    model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])
    model.summary()
    # estimator = KerasRegressor(model=baseline_model, epochs=1000, batch_size=32, verbose=1)
    history = model.fit(X_train, y_train, epochs=200, batch_size=32, validation_data=(X_test, y_test))
    prediction = model.predict(X_test)

    train_error = np.abs(y_test - prediction)
    mean_error = np.mean(train_error)
    min_error = np.min(train_error)
    max_error = np.max(train_error)
    std_error = np.std(train_error)
    print("train error: ", train_error)
    print("mean error: ", mean_error)
    print("min error: ", min_error)
    print("max error: ", max_error)
    print("std error: ", std_error)
    rms = mean_squared_error(y_test, prediction, squared=False)


def linear_model():
    X = pd.get_dummies(data=df, drop_first=True)
    y = df["Verdict"]
    X = X.drop("Verdict", axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, df['Verdict'], test_size=0.2, random_state=101)
    model = LinearRegression().fit(X_train, y_train)
    prediction = model.predict(X_test)
    test_error = np.abs(y_test - prediction)
    mean_error = np.mean(test_error)
    min_error = np.min(test_error)
    max_error = np.max(test_error)
    std_error = np.std(test_error)
    print("train error: ", test_error)
    print("mean error: ", mean_error)
    print("min error: ", min_error)
    print("max error: ", max_error)
    print("std error: ", std_error)

def decision_tree():
    X = pd.get_dummies(data=df, drop_first=True)
    y = df["Verdict"]
    X = X.drop("Verdict", axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, df['Verdict'], test_size=0.2, random_state=101)
    model = DecisionTreeRegressor(min_samples_split=30).fit(X_train, y_train)
    prediction = model.predict(X_test)
    test_error = np.abs(y_test - prediction)
    mean_error = np.mean(test_error)
    min_error = np.min(test_error)
    max_error = np.max(test_error)
    std_error = np.std(test_error)
    print("train error: ", test_error)
    print("mean error: ", mean_error)
    print("min error: ", min_error)
    print("max error: ", max_error)
    print("std error: ", std_error)

def random_forest():
    X = pd.get_dummies(data=df, drop_first=True)
    y = df["Verdict"]
    X = X.drop("Verdict", axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, df['Verdict'], test_size=0.2, random_state=101)
    model = RandomForestRegressor(n_estimators=100, min_samples_split=5)
    cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
    n_scores = cross_val_score(model, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1, error_score='raise',
                               verbose=1)
    print('MAE: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))
    model.fit(X_train, y_train)
    model.score(X_test, y_test)
    prediction = model.predict(X_test)
    test_error = np.abs(y_test - prediction)
    mean_error = np.mean(test_error)
    min_error = np.min(test_error)
    max_error = np.max(test_error)
    std_error = np.std(test_error)
    print("train error: ", test_error)
    print("mean error: ", mean_error)
    print("min error: ", min_error)
    print("max error: ", max_error)
    print("std error: ", std_error)



