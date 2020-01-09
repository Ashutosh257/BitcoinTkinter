from tkinter import *
import requests
import json

crypto = Tk()
crypto.title("Ashutosh")

def font_color(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"

# x = float(input())
# print(font_color(float("{0:.2f}".format(x))))

def my_portfolio():
    # api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
    
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=PASTE_YOUR_API_KEY_HERE") #PASTE_YOUR_API_KEY_HERE
    api = json.loads(api_request.content)


    # print("----------------")
    # print("----------------")

    coins = [
      {
        "symbol":"BTC",
        "amount_owned": 2,
        "price_per_coin": 5200
      }, 
      {
        "symbol":"ETH",
        "amount_owned": 10,
        "price_per_coin": 189
      }, 
      {
        "symbol":"LTC",
        "amount_owned": 5,
        "price_per_coin": 125
      }, 
      {
        "symbol":"XMR",
        "amount_owned": 10,
        "price_per_coin": 48.05
      }
    ]

    total_pl = 0
    coin_row = 1
    total_current_value = 0



    for i in range(0, 100):
      for coin in coins:
        if api["data"][i]["symbol"] == coin["symbol"]:
            total_paid = coin["amount_owned"] * coin["price_per_coin"]
            current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
            pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
            total_pl_coin = pl_percoin * coin["amount_owned"]
        
            total_pl = total_pl + total_pl_coin
            total_current_value = total_current_value + current_value
        #   print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
        #   print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
        #   print("Number Of Coin:", coin["amount_owned"])
        #   print("Total Amount Paid:", "${0:.2f}".format(total_paid))
        #   print("Current Value:", "${0:.2f}".format(current_value))
        #   print("P/L Per Coin:", "${0:.2f}".format(pl_percoin))
        #   print("Total P/L With Coin:", "${0:.2f}".format(total_pl_coin))
        #   print("----------------")


        
            name = Label(crypto, text=api["data"][i]["symbol"], bg="#F3F4F6", fg="black", font="Arial 12", padx="2", pady="2", borderwidth="2", relief="groove")
            name.grid(row=coin_row, column=0, sticky=N+S+E+W)

            price = Label(crypto, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="#F3F4F6", fg="black", font="Arial 12", padx="2", pady="2", borderwidth="2", relief="groove")
            price.grid(row=coin_row, column=1, sticky=N+S+E+W)

            no_coins = Label(crypto, text=coin["amount_owned"], bg="#F3F4F6", fg="black", font="Arial 12", padx="2", pady="2", borderwidth="2", relief="groove")
            no_coins.grid(row=coin_row, column=2, sticky=N+S+E+W)

            amount_paid = Label(crypto, text="${0:.2f}".format(total_paid), bg="#F3F4F6", fg="black", font="Arial 12", padx="2", pady="2", borderwidth="2", relief="groove")
            amount_paid.grid(row=coin_row, column=3, sticky=N+S+E+W)

            current_val = Label(crypto, text="${0:.2f}".format(current_value), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(current_value))), font="Arial 12", padx="2", pady="2", borderwidth="2", relief="groove")
            current_val.grid(row=coin_row, column=4, sticky=N+S+E+W)

            pl_coin = Label(crypto, text= "${0:.2f}".format(pl_percoin), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(pl_percoin))), font="Arial 12", padx="2", pady="2", borderwidth="2", relief="groove")
            pl_coin.grid(row=coin_row, column=5, sticky=N+S+E+W)

            totalpl = Label(crypto, text="${0:.2f}".format(total_pl_coin), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(total_pl_coin))), font="Arial 12", padx="2", pady="2", borderwidth="2", relief="groove")
            totalpl.grid(row=coin_row, column=6, sticky=N+S+E+W)

            coin_row = coin_row + 1

    totalcv = Label(crypto, text="${0:.2f}".format(total_current_value), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(total_current_value))), font="Arial 12", padx="2", pady="2", borderwidth="2", relief="groove")
    totalcv.grid(row=coin_row, column=4, sticky=N+S+E+W)

    totalpl = Label(crypto, text="${0:.2f}".format(total_pl), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(total_pl))), font="Arial 12", padx="2", pady="2", borderwidth="2", relief="groove")
    totalpl.grid(row=coin_row, column=6, sticky=N+S+E+W)
    # print("Total P/L For Portfolio:", "${0:.2f}".format(total_pl))

    api = " "
    update = Button(crypto, text="Update", bg="#F3F4F6", fg="black", command=my_portfolio, font="Arial 12", padx="2", pady="2", borderwidth="2", relief="groove")
    update.grid(row=coin_row + 1, column=6, sticky=N+S+E+W)

name = Label(crypto, text="Coin Name", bg="#142E54", fg="white", font="Arial 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(crypto, text="Price", bg="#142E54", fg="white", font="Arial 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
price.grid(row=0, column=1, sticky=N+S+E+W)

no_coins = Label(crypto, text="Coins Owned", bg="#142E54", fg="white", font="Arial 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
no_coins.grid(row=0, column=2, sticky=N+S+E+W)

amount_paid = Label(crypto, text="Total Amount Paid", bg="#142E54", fg="white", font="Arial 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
amount_paid.grid(row=0, column=3, sticky=N+S+E+W)

current_val = Label(crypto, text="Current Value", bg="#142E54", fg="white", font="Arial 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
current_val.grid(row=0, column=4, sticky=N+S+E+W)

pl_coin = Label(crypto, text="P/L Per Coin", bg="#142E54", fg="white", font="Arial 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
pl_coin.grid(row=0, column=5, sticky=N+S+E+W)

totalpl = Label(crypto, text="Total P/L With coin", bg="#142E54", fg="white", font="Arial 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
totalpl.grid(row=0, column=6, sticky=N+S+E+W)

my_portfolio()

crypto.mainloop()

print("Program Completed")
