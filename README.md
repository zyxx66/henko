# henko
偏光測定器用プログラム。
<br>ご自由に使ってください。
<br>(編集可)
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
zyxxフォルダにあるプログラムのファイルを更新する.
## 2.実行方法
```
python3 <ファイル位置>
例： python3 /home/pi/Documents/test/test1.py
```
## 3.各プログラムの説明
##　実行環境：　Raspberry　OS
### 1.[check_sensor](check_sensor.py)
センサの状態を確認する

### 2.[p_8_zyxx](p_8_zyxx.py)
測定プログラム本体<br>
先輩が書いた [ts1.py](/p_8/ts1.py)　に依存すくことを注意

## 4.各フォルダの説明
### 1.[how_to_use](/how_to_use)
### 2.[p_8/](/p_8)
先輩が作ったもののバックアップ場所<br>
ts1は　ライブラリ<br>
p_8は　測定プログラム
### 3.[rclone](/rclone)
内容待つ
### 4,[test](/test)
内容待つ
### 5.[tiem](/time)
内容待つ
### 6.[use github](/use github)
内容待つ
### 7.[with_excel](/with_excel)
内容待つ

## 5.参照
参照ページ1：https://akizukidenshi.com/catalog/g/gK-15536/ <br>
(赤外線を測る機能が存在する) <br>
参照ページ2：https://s-design-tokyo.com/use-tsl25721/ <br>
(赤外線の照度の読み取り方法)<br>