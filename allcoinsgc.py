import samino,time,os,sys
from threading import Thread
vip = [""] # userIds
client = samino.Client("22D3085F471DF87A00FB4CE43052685FE93239644F93AD2140B23F3C77277FF6CAE5A0C164593CD9A8")
client.login(email="kknkk1223@gmail.com",password="912850",asWeb=True)

@client.event("on_message")
def on_message(data: samino.lib.Event):
	msg = data.message.content
	msgId = data.message.messageId
	comId = data.ndcId
	chatId = data.message.chatId
	userId = data.message.userId
	nickname = data.message.author.nickname
	try: mentionIds = data.message.json["extensions"]["mentionedArray"]
	except: pass
	print(f"message : {msg}\n{'_'*20}")
	local = samino.Local(comId)
	if msg.startswith("ss") :
		local.send_message(chatId,f"{nickname} 👀♥️done ",asWeb=True)
		for _ in range(100):
			Thread(target=client.watch_ad, args=(userId, )).start()

client.launch()