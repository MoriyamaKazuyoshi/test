#ライブラリをインポート
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

#タイトル
#st.title("moriyama")

#テキストの追加
#st.write("DataFrame")

#動的な表
#df = pd.DataFrame({
#    "1列目":[1, 2, 3, 4],
#    "2列目":[10, 20, 30, 40]
#})
#st.dataframe(df, width=500, height=200)
#表に色を付ける場合　df.style.highlight_max(axis=0)
#静的なテーブル　st.table(df)

#"""
# 章
## 節
### 項
 
#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#"""#

#折れ線グラフ
#st.line_chart(df)

#地図
#df_map = pd.DataFrame(
#    np.random.rand(100,2)/[50,50]+[35.69, 139.70],
#    columns=["lat","lon"]
#)
#st.map(df_map)

#画像
#チェックボックス
#if st.checkbox("Show Image"):
#    img = Image.open("Shiki.jpg")
#    st.image(img, caption="Shiki", use_column_width=True)
#セレクトボックス
#option = st.selectbox(
#    "掘削深度",
#    list(range(1,11))
#    )
#"金額は=", option, "です"

#テキスト入力
#st.write('Interactive Widgets')
#text = st.text_input("会社名を記入ください")
#"会社名：", text

#スライダー
#date = st.slider("施工予定日は？", 1,12,1)
#"施工日：", date

#レイアウト
#サイドバー
#st.sidebar.write(df)

#2カラムレイアウト
#left_column, right_column = st.columns(2)
#button = left_column.button("右カラムに文字を表示")
#if button:
#    right_column.write("ここは右カラムです")

#エクスパンダー
#expander = st.expander("問い合わせ内容1")
#expander.write("回答")
#expander = st.expander("問い合わせ内容2")
#expander.write("回答")

#タイム
#st.write("プログレスバーの表示")
#"スタート！"
#latest_iteration = st.empty()
#bar = st.progress(0)
#for i in range(100):
#    latest_iteration.text(f"Iteration{i+1}")
#    bar.progress(i+1)
#    time.sleep(0.01)
#"完了！"

#マラウイグラフ
#st.area_chart(df_malawi)

import streamlit as st
import pandas as pd
import geopandas as gpd
import pydeck as pdk

st.subheader("給水量")
chart_data = pd.read_excel("エリア別水利用量.xlsx")
chart_data = pd.DataFrame(chart_data)
#chart_data = pd.DataFrame({
#    "latitude":[-13.52013, -13.52056, -13.52143, -13.522, -13.52389],
#    "longitude":[32.95585, 32.95572, 32.95484, 32.95566, 32.95634],
#})

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=-13.521,
        longitude=32.955,
        #zoom=11,
        #pitch=10,
        #bearing=-27.36,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[longitude, latitude]',
           #auto_highlight=True,
           #radius=15, #直径
           elevation_scale=20,
           elevation_range=[0, 500],
           #pickable=True,
           extruded=True, #色
           #coverage=1,
        )],
))
