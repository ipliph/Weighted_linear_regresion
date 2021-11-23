# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 13:33:21 2021

@author: ipliph
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

class WeightedLinReg:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return('Weighted Linear Regresion:\n{},{},{})'.format(self.x,self.y))

    def __1X2__(x,y):
        
        x = np.array(x).reshape(-1,1)
        
        # Create equal weights and then augment the last 2 ones
        weight_list = []
        for numb in x:
            weight_list.append(1/numb**2)
        sample_weight = np.array(weight_list).reshape(-1)

        # The unweighted model
        #regr = LinearRegression()
        #regr.fit(x, y)

        # The weighted model - scaled weights
        regr = LinearRegression()
        sample_weight = sample_weight / sample_weight.max()
        regr.fit(x, y, sample_weight)

        fig = plt.figure(figsize=(7,4))
        ax = fig.add_subplot(1, 1, 1)
        
        plt.scatter(x,y,c='b')
        plt.plot(x, regr.predict(x), color='red')
        ax.set(xlabel='Concentration', ylabel='Instrument reading')
        
        title = 'Calibration curve; weight: 1/x^2; r2=' + str(regr.score(x, y, sample_weight=sample_weight))
        
        plt.title(title)
        plt.show()

        x_pred = (y - regr.intercept_)/regr.coef_[0]
        x_pred = np.array(x_pred).reshape(-1,1)
        
        diff = ((x_pred - x)/x)*100

        df = pd.DataFrame(x, columns=['x'])
        df['x_pred'] = x_pred
        df['y'] = y
        df['Diff%'] = diff

        print('wlr - results')
        print(df)
        print(regr.coef_[0])
        print(regr.intercept_)
        print(regr.score(x, y, sample_weight=sample_weight))





















