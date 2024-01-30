import pandas as pd
import pygwalker as pg

df=pd.read_csv("train.csv",index_col=[0])
pg.walk(df)