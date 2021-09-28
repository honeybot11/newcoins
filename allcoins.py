import samino
from threading import Thread

client = samino.Client("22D3085F471DF87A00FB4CE43052685FE93239644F93AD2140B23F3C77277FF6CAE5A0C164593CD9A8")
pswd = input("Password: ")
for email in open("emails.txt").read().split():
	client.login(email,pswd)
	coins = client.get_wallet_info().coins
	print(f"Coins Before the ad: {coins}")
	for _ in range(200):
		Thread(target=client.watch_ad).start()
		print(f"Claim {_}")
	coins = client.get_wallet_info().coins
	print(f"Coins After ad {coins}")