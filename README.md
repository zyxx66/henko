# henko
偏光測定器用プログラミング，ご自由に使ってください。
# 使用方法
## 1.ダウンロード方法
```
１．git clone https://github.com/zyxx66/henko.git
```
を実行すると、すべてのファイルをラズベリーパイにダウンロードすることができる。
```
２．
cd /home/pi/Documents/test/zyxx
git pull
```
zyxxフォルダにあるファイルを更新する.
## 2.実行方法
```
python3 <ファイル位置>
例： python3 /home/pi/Documents/test/test1.py
```
# 各プログラミングの説明
## 1.[rclone_method](rclone_method.py)
メインプログラミング<br>
これを必ずダウンロードしてください。
## 2.[gdrive](gdrive.py)
測定データをgoogle driveにアップロードするプログラミングである。<br>
毎日18時40分実行しているプログラミングである。<br>
動作：当日の測定結果（写真とデータ）を google driveにアップロードする<br>
## 3.[gdrive_one](gdrive_one.py)
指定期間の測定結果をgoogle driveにアップロードするプログラミングである。<br>
停電または不具合があれば、自動的にアップロードできなかったデータをアップロードする<br>
動作：一定時間内のデータをアップロードする<br>
## 4.[create_graph](create_graph.py)
測定データをグラフ化するプログラミング<br>
未完成(2022-10-19)<br>
## 5.[csv_update_to_gdrive](csv_update_to_gdrive.py)
今まですべてのcsvファイルを　google drive　にある<偏光測定器_照度データ>と<偏光測定器_雲量データ>フォルダにアップロードする。
```
rclone sync （省略）を使用している
```
## 6.[test_infrared_sensor](test_infrared_sensor.py)
モーターを5度ずつ回しながらデータを読み取るプログラムである。<br>
赤外線照度(60%完成)、自然光と赤外線照度(60%完成)、
未完成理由：検証していない<br>

<br>自然光照度(100%完成)



参照ページ1：https://akizukidenshi.com/catalog/g/gK-15536/ <br>
(赤外線を測る機能が存在する) <br>
参照ページ2：https://s-design-tokyo.com/use-tsl25721/ <br>
(赤外線の照度の読み取り方法)<br>