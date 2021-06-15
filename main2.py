from altair.vegalite.v4.schema.core import DataFormat
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Stramlit 超入門')

st.write('Interactive Widgets')

text = st.text_input('あなたの趣味を教えて下さい。')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)




#0, 100, 50は最小値が0、最大値が100、初期値が50
#sliderバーを実装
# sidebarを表示

'あなたの趣味:', text
'コンディション:', condition




# option = st.selectbox(
#   'あなたが好きな数字を教えて下さい。',
#   list(range(1, 11))
#   )

# 'あなたの好きな数字は、', option, 'です。'
#1−10のlistを作りoptionに代入し、selectboxでoptionを指定して表示を変化させる。


# if st.checkbox('Show Image'):
#   img = Image.open('隼改のコピー.jpg')
#   st.image(img, caption='Kensei Ohtani', use_column_width=True)
#チェックボックスにチェックすると画像が表示される実装

