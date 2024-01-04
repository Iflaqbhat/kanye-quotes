from tkinter import *

import requests


# import requests
# response =requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
#
# data=response.json()
# print(data)
#
# longitude=data["iss_position"]["longitude"]
# latitude=data["iss_position"]["latitude"]
#
# iss_poaition=(latitude,longitude)
# print(iss_poaition)

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)  # quote text is the item we want to configure


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, highlightthickness=0)

canvas = Canvas(width=300, height=414, highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"),
                                fill="black")  # 150 and 207 are the x and the y cordinates
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
