import sys

number = {1: '薄力小麦粉(20~50㎛)',
          2: 'トマトパウダー(100~500㎛)',
          3: '黒鉛粉末(5~11㎛)',
          4: 'トルマリン(3㎛)',
          5: 'トルマリン(1.8㎛)',
          6: 'トルマリン(0.8㎛)',
          7: 'RX OX(40nm)',
          8: 'スギ花粉(30㎛)'}

diameter = {'薄力小麦粉(20~50㎛)': '20~50㎛',
            'トマトパウダー(100~500㎛)': '100~500㎛',
            '黒鉛粉末(5~11㎛)': '5~11㎛',
            'トルマリン(3㎛)': '3㎛',
            'トルマリン(1.8㎛)': '1.8㎛',
            'トルマリン(0.8㎛)': '0.8㎛',
            'RX OX(40nm)': '40nm',
            'スギ花粉(30㎛)': '30㎛'}
try:
    target_number = int(input('測定目標の番号を入力してください？'))
except:
    print('数字を入力してください！')
    sys.exit()
try:
    target_name = number[target_number]
except:
    print('正しい番号を入力してください!')
    sys.exit()
target_diameter = diameter[target_name]

print(target_name)

print(target_diameter)
