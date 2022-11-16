ここにあるのは「excel」と関係あるプログラム
# 各プログラムについて
## 0.ご注意
`openpyxl`がないと実行できないから、`事前にインストールすること`を忘れないように。
## 1.[create_graph](create_graph.py)
###　1.1 紹介
ライブラリである</p>

###　1.2 使用方法
1.まずはimport
```
import create_graph
```
</pr>2.オブジェクト作る
```
指定した変数名 = create_graph('エクセルファイル名','シート名')

例：example = create_graph('C:/Users/test/Desktop/test_csv/test.xlsx','Sheet')
```
</pr>3.エクセルファイルを`一回`ロードする
```
指定した変数名.load()

例：excel_file = example.load()
```
</pr>4.グラフを作る
```
指定した変数名.create_scatter(excel_file,グラフ横軸のタイトル,グラフ縦軸のタイトル,グラフのタイトル,グラフ置く場所,
                           [xデータ開始x,xデータ開始y,xデータ終了x,xデータ終了,yデータ開始x,yデータ開始y,yデータ終了x,yデータ終了y],……(データ無限追加可能))
```
データについての説明：
```
[1,1,1,5,2,1,2,5] とは xの値は(A1)から(A5)まで、Yの値は(B1)から(B5)まで
```
```
例１(1個のデータの場合)：

```
## 2.[check_data](check_data.py)