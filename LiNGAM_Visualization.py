import pandas as pd
import numpy as np
from graphviz import Digraph
from LiNGAM_model import estimate


class LiNGAM():
    def __init__(self, thresh=0):
        """
        thresh(int): あまりいじらなくていい
        """
        self.thresh = thresh
        
    def calc_causalyty_matrix(self, X):
        """
        X(pandas.DataFrame): データ 
        """
        matrix =  estimate(X.values)
        matrix = pd.DataFrame(matrix,columns=X.columns,index=X.columns)
        self.matrix = matrix
        return matrix

    def viz_directed_acyclic_graph(self, magnification=5):
        """
        magnification(int): edgeを描写する際の太さ。因果値の絶対値を0~1で標準化した後にこの値をかけてedgeの太さにしている。
        """
        max_value = self.matrix.abs().max().max()
        min_value = self.matrix.abs().min().min()
        G = Digraph(format="png")
        G.attr("node", style="filled")
        for i in self.matrix.columns:
            tmp_series = self.matrix[i][self.matrix[i]!=0]
            for n,j in enumerate(tmp_series):
                value = np.round(tmp_series.iloc[n],2)
                width = (np.abs(value)-min_value)/(max_value-min_value)
                try:
                    width = int(width*magnification)
                except:
                    print(width,self.magnification)
                    
                if width>self.thresh:
                    if value>0:
                        G.edge(i,tmp_series.index[n],penwidth=str(width),label=f"{value}")
                    else:
                        G.edge(i,tmp_series.index[n],penwidth=str(width),label=f"{value}", color="red")
        self.G = G
        return G
    
    def save_fig(self, fname):
        self.G.render(fname)