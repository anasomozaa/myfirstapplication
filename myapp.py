# -*- coding: utf-8 -*-
"""myapp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dXL4C86QGXvnmHvikYtu2Np21uExpe6o
"""

import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image

image = Image.open('Logo-KDT-JU.webp')
st.image(image, caption='Logo KDT')

st.title('My first web app')

#@st.cache
#def display_dataframe():
df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
  #return(df)


#dataframe1 = display_dataframe()
st.write(df)
 

#option = st.selectbox('Choose an option', ['a', 'b', 'c'])
#st.bar_chart(option)
