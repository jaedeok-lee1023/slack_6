import os

import arrow
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from kurly import clusters

# 환경 변수에서 Slack 토큰, 채널을 로드
load_dotenv()
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
def send_slack_message(message, channel):
    try:
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Error sending message to {channel} : {e}")
def main():
    for cluster in clusters:
        # 메시지 제목 설정
        header = f":loudspeaker: *『인사총무팀 공지』* <!channel>\n\n"

        notice_msg = (
            f"안녕하세요? 평택 클러스터 구성원 여러분!\n평택 클러스터 6층 컬리스라운지 냉장고 사용 에티켓 안내드립니다.\n\n"
            f"\n"
            f"\n"
            f":k체크: *공용 사용 냉장고로 항상 깨끗하게 사용 부탁드립니다.*\n"
            f":k체크: *위생관리를 위해 매주 금요일 오전11시 냉장고 내부상품을 폐기 합니다.*\n"
            f"\n"
            f"사우님들께서는 이점 숙지하시어 공용 냉장고 사용 부탁드립니다.\n"
            f"\n"
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
