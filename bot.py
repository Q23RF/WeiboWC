from WeiboBot import Bot
from WeiboBot.message import Chat
from WeiboBot.weibo import Weibo
from WeiboBot.comment import Comment
from datetime import datetime
import env

cookies = env.get_cookies()
myBot = Bot(cookies=cookies)


@myBot.onNewMsg
async def on_msg(chat: Chat):
    for msg in chat.msg_list:
        if msg.text[:4] == "【投稿】":
            myBot.post_weibo(msg.text)
            myBot.send_message(msg.sender_id, "已自動發稿")

@myBot.onNewWeibo
async def on_weibo(weibo: Weibo):
    pass


@myBot.onMentionCmt
async def on_mention_cmt(cmt: Comment):
    pass


@myBot.onTick
async def on_tick():
    print(datetime.now())


if __name__ == '__main__':
    myBot.run()