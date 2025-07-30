from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import requests
from datetime import datetime

# 웹훅 URL
WEBHOOK_URL = "'https://discord.com/api/webhooks/1399913282449444874/qoGbySHdgyqXlNWHqrNqsNpfSunIwIzEkXP8oM8di_rLXex2kmzyrKT1Socovx5yaSEu'"

# 메시지 전송 함수
def send_discord_message(msg):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        "content": f"⏰ {msg} ({now})"
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print(f"✅ 전송됨: {msg}")
    else:
        print(f"❌ 실패: {response.status_code}, {response.text}")

# 스케줄러 생성
scheduler = BlockingScheduler()

# CronTrigger 사용: 월~금(weekday=0~4), 09:00
scheduler.add_job(
    send_discord_message,
    CronTrigger(day_of_week='mon-fri', hour=9, minute=0),
    args=["🟢 오전 9시 입실"]
)

# 월~금 17:55
scheduler.add_job(
    send_discord_message,
    CronTrigger(day_of_week='mon-fri', hour=17, minute=55),
    args=["🔴 오후 5시 55분 퇴실"]
)

print("⏳ APScheduler 알림 봇 실행 중...")
scheduler.start()