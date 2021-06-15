import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)
'Done!!'
# プログレスバーの表示
# time.sleep.(0.1)があることで0.1秒ごとに+1される
# バーが100に達したときに下の文字が表示される


left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラム')


expander1 = st.beta_expander('問い合わせ１')
expander1.write('問い合わせ１の回答内容を書く')
expander2 = st.beta_expander('問い合わせ２')
expander2.write('問い合わせ２の回答内容を書く')
expander3 = st.beta_expander('問い合わせ３')
expander3.write('問い合わせ３の回答内容を書く')
expander4 = st.beta_expander('問い合わせ４')
expander4.write('問い合わせ４の回答内容を書く')




# text = st.text_input('あなたの趣味を教えて下さい。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味:', text
# 'コンディション:', condition


# if st.checkbox('Show Image'):
#   img = Image.open('隼改のコピー.jpg')
#   st.image(img, caption='Kensei Ohtani', use_column_width=True)
#チェックボックスにチェックすると画像が表示される実装

