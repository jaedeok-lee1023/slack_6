import os
import sys
import datetime
import arrow
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from kurly import clusters

# 🎯 한국 공휴일 목록 (YYYY-MM-DD 형식)
HOLIDAYS = {
    "2026-09-24",  # 다음날 추석
    "2026-10-08",  # 다음날 한글날
    "2026-12-24",  # 다음날 크리스마스
}

# 📆 오늘 날짜 가져오기
today = datetime.date.today().strftime("%Y-%m-%d")

# 🚫 오늘이 공휴일이면 실행하지 않고 종료
if today in HOLIDAYS:
    print(f"📢 오늘({today})은 공휴일이므로 실행하지 않습니다.")
    sys.exit(0)

# 환경 변수에서 Slack 토큰 로드
load_dotenv()
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

def send_slack_message(message, channel):
    try:
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"⚠️ Error sending message to {channel} : {e}")

def main():
    for cluster in clusters:
        # 메시지 제목 설정
        header = f"*[공지｜컬리스라운지 냉장고 사용 안내]*\n\n\n"

        notice_msg = (
            f"1. *중요도* : 하\n"
            f"2. *대상* : 평택 클러스터 임직원 전체\n"
            f"3. *주요 내용*\n\n"
            f"\n"
            f"안녕하세요? 평택 클러스터 구성원 여러분!\n
            f"우리 클러스터 6층 컬리스라운지 냉장고 사용 에티켓 안내드립니다.\n\n"
            f"\n"
            f":k체크: *<https://static.wixstatic.com/media/50072f_41299341619d417b9508c48964cb1e08~mv2.jpg|공용 사용 냉장고>로써 다음 사용자를 위해 깨끗이 이용 부탁드립니다.*\n"
            f":k체크: *냉장고 위생관리 차원에서 *매주 금요일 오전 점검* 을 진행 합니다.*\n"
            f":k체크: *냉장고 내 스티커 부착물의 대해 D+7일 이후 폐기 진행 되오니 많은 협조 바랍니다.*\n\n"
            f"\n"
            f"모두가 사용하는 공용공간의 깨끗하고 위생적인 운영을 위해 많은 양해와 협조 바랍니다.\n\n"
            f"\n"
            f"*:slack: 문의사항 : 인사총무팀 총무/시설 담당자*\n\n"
            f"감사합니다.\n"
        )
 
        # 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()

