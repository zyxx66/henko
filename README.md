# henko
偏光測定器用プログラム。
<br>ご自由に使ってください。
<br>(編集もご自由に)

# 使用方法
## 1.ダウンロード方法
```
１．git clone https://github.com/zyxx66/henko.git
```
を実行すると、すべてのファイルをラズベリーパイにダウンロードすることができる。
実験室中にあるラズパイは既にダウンロード済です。

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

### 2.[granule_experiment](granule_experiment.py)
粒子実験用プログラム<br>
実行する粒子に当てはまる番号を入力してエンターキーを押すと、測定が始まります。<br>
測定結果は
```
'/home/pi/henko/result/'
```
中日別で保存します。<br>
詳細データとまとめデータ2つあります。<br>
詳細データは2週波になるかどうかを確認するために、まとめデータは偏光度と照度のデータしか保存してない。

### 3.[granule_experiment_2](granule_experiment_2.py)
粒子実験用２<br>
2番との区別は、こちらの実験はモータを回転させないこと。<br>
今後の実験中活用できると考える。

### 4.[p_8_zyxx](p_8_zyxx.py)
測定プログラム本体<br>
先輩が書いた [ts1.py](/p_8/ts1.py)　に依存すくことを注意

## 4.各フォルダの説明
### 1.[how_to_use](/how_to_use)
測定プログラムの使い方である

### 2.[p_8/](/p_8)
先輩が作ったプログラムを **バックアップ** する場所<br>
* [ts1.py](/p_8/ts1.py) 　
  * ライブラリ
* [p_8.py](/p_8/p_8.py) 　
  * 測定プログラム

### 3.[rclone](/rclone)
gdrive (google drive)　に関するプログラムである
* [gdrive.py](/rclone/gdrive.py)
  * 毎日*18時40分*実行している
  * 本日記録したデータをアップロードするプログラムである
* [gdrive_one.py](/rclone/gdrive_one.py)　　　
  * 一定時間内のデータをアップロードするプログラムである
  * 一般的にはデータを修正する時使う(ラズパイのデータファイルを修正してください)
* [rclone_method.py](/rclone/rclone_method.py)　
  * ライブラリ
  * pcのアドレス(C://*** D://***みたいなもの)を自分のアドレスに変更してください

### 4,[test](/test)
たまにあるコードを試してみたい時に使うフォルダ<br>
**削除可**

### 5.[time](/time)
* [time.py](/time/time.py)
  * 毎回ラズベリーパイ起動する時実行するプログラムである
  * 時刻合わせ用プログラム

### 6.[use_github](/use_github)
* GitHubの使い方を簡単に書きたいが
* **まだ完成してない**（2023/01/17）
* この実験はGitHubを使わなくても大丈夫ので、諦めた。

### 7.[with_excel](/with_excel)
* [check_data.py](/with_excel/check_daily_data.py)
* [check_experimental_data.py](/with_excel/check_experimental_data.py)
* [download_data.py](/with_excel/download_data.py)

## 5.参照になれるページ
参照ページ1：(赤外線を測る機能が存在する) <br>
https://akizukidenshi.com/catalog/g/gK-15536/ <br>
参照ページ2：(赤外線の照度の読み取り方法)<br>
https://s-design-tokyo.com/use-tsl25721/ <br>
参照ページ3:(偏光)<br>
http://www.wakariyasui.sakura.ne.jp/p/wave/kouha/kouha.html<br>
参照ページ4:(散乱)<br>
https://tadao-sakamoto.com/rayleigh-scattering-mie-scattering/<br>
参照ページ5:(空の偏光度)<br>
http://www.takuichi.net/hobby/edu/em/sky_polarization/index-j.html<br>
