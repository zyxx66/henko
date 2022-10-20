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
## 4.[create_graph](create_graph)
測定データをグラフ化するプログラミング<br>
未完成(2022-10-19)<br>
