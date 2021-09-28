import aminofix
import re

#emp
#import os ;os.system("pip install amino.fix")
W=aminofix.Client("22D3085F471DF87A00FB4CE43052685FE93239644F93AD2140B23F3C77277FF6CAE5A0C164593CD9A8")
emails = open("email.txt", "r")
link = W.get_from_code(input("blog Link >> ")) 
blog=link.objectId
comId=link.path[1:link.path.index('/')]

password = input(("Password For All Accounts >> "))
for line in emails:
 email = line.strip()

 try:
    W.login(email=email, password=password)
    SUB=aminofix.SubClient(comId,profile=W.profile)
 except aminofix.lib.util.exceptions. VerificationRequired as e:
               print(f"VerificationRequired for {email}")
               url = re.search("(?P<url>https?://[^\s'\"]+)", str(e)).group("url")                                                                             
 try:
       W.join_community(comId)
 except:
               print(comId,"no way")              

 try:
  acc=W.get_wallet_info().totalCoins
  print(f"You own{acc}coins from {email} ")
  if acc>500 and acc!=0:
   N=int(acc/500) 
   for _ in range(N):
    SUB.send_coins(500,blog)
    print("500 coins sent")
    print(f"You now own {W.get_wallet_info().totalCoins} coins.") 
    print("_______________________")
 except:
    print(f"try again.{ W.get_wallet_info().totalCoins} ")

 try:
          totals=W.get_wallet_info().totalCoins      
          if totals!=0:
           print("......")
          if totals!=0 and totals<500 or totals==500:
                   SUB.send_coins(totals,blog)
                   print(f"You now own {W.get_wallet_info().totalCoins} coins.") 
                   print("_______________________") 
 except:
    print(f"try again {W.get_wallet_info().totalCoins}.")