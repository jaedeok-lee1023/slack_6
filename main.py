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
        header = f":loudspeaker: *『인사총무팀 공지』*\n\n"

        notice_msg = (
            f"안녕하세요? 평택 클러스터 구성원 여러분!\n평택 클러스터 6층 컬리스라운지 냉장고 사용 에티켓 안내드립니다.\n\n"
            f"\n"
            f":k체크: *공용 사용 냉장고로 항상 깨끗하게 사용 부탁드립니다.*\n"
            f":k체크: *위생관리를 위해 매주 금요일 오전11시 냉장고 내부상품을 폐기 합니다.*\n"
            f"\n"
            f"사우님들께서는 이점 숙지하시어 공용 냉장고 사용 부탁드립니다.\n"
            f":point_right: (Click) *<https://static.wixstatic.com/media/50072f_989ee3daa50049b0ba4f6106e3da1357~mv2.jpg|매주 금요일 폐기 안내>*\n"
            f"\n"
            f"*문의사항 : 인사총무팀 총무/시설 담당자*\n\n"
            f"감사합니다.\n"
        )
 
        # 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()

