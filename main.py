from altair.vegalite.v4.schema.core import DataFormat
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Stramlit 超入門')

st.write('DataFrame')

df = pd.DataFrame(
  np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
  columns=['lat', 'lon']
)
st.map(df)
#新宿付近の座標を持った情報

#'lat'は緯度、'lon'は経度

st.line_chart(df)
#折れ線グラフを表示

st.area_chart(df)
#折れ線グラフ塗ったグラフ

st.bar_chart(df)
#棒グラフ


st.write(df.style.highlight_max(axis=0))
# axis=0 は列を指定、行は axis=1

st.dataframe(df.style.highlight_max(axis=0))
# 動的


st.table(df.style.highlight_max(axis=0))
# tableはソートができずただ表示するだけ。静的


# マークダウン記法
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

st.write('Display Image')
img = Image.open('隼改のコピー.jpg')
st.image(img, caption='Kensei Ohtani', use_column_width=True)

# use_column_width=Trueとはカラムをレイアウトの横幅に合わせて表示してくれるもの