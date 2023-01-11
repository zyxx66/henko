import requests
import os
import rclone_method
import time
import calendar

ExchangeMounth = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

while True:
    try:
        requests.packages.urllib3.disable_warnings()
        request_result = requests.get(url='http://www.google.com/',verify=False)
        
        if request_result.status_code == 200:
            net_date = request_result.headers.get("date")
            print(net_date)

            year_now = net_date[12:16]

            mounth_now = ExchangeMounth[net_date[8:11]]
            
            day_now = int(net_date[5:7])

            hour_now = int(net_date[17:19]) + 9
            minute_now = net_date[20:22]
            second_now = net_date[23:25]

            # 今月はday_in_mounth日ある
            days_in_mounth = calendar.monthrange(int(year_now), int(mounth_now))[1]

            if hour_now < 10:
                hour_now = '0' + str(hour_now)
            # もし時が24超えるとの操作
            elif hour_now >= 24:
                hour_now -= 24
                day_now = int(day_now) + 1
                hour_now = '0' + str(hour_now)

            # 1月32日みたいな結果が出る場合の操作
            if day_now > days_in_mounth:
                day_now -= days_in_mounth
                mounth_now = int(mounth_now) + 1

            # 2022年13月みたいな結果が出る場合の操作
            if mounth_now > 12:
                mounth_now -= 12
                year_now = int(year_now) + 1

            time_now = str(hour_now) + ":" + minute_now + ":" + second_now
          
            date_now = year_now + "-" + str(mounth_now) + "-" + day_now + " " + time_now

            os.system('sudo date -s' + '"' + date_now + '"')
            print(date_now)

            rclone_method.line_send_message('時間設定完了')

            break
    except Exception as e:
        print(e)
        time.sleep(3)
        continue