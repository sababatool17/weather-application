from tkinter import *
import requests
import json

window=Tk()
welcome= Label(text="welcome to the weather app!",bg="#FDE2E4",fg="#4B0082",font=("Arial",20))
window.configure(bg="#C8A2C8")
welcome.grid(column=0, row=0)

place_lbl= Label(text="please enter the name of the place:", font=("Arial",15),bg="#FDE2E4",fg="#4B0082")
place_lbl.grid(column=0, row=1)

placename=Entry(width=30, font=("Arial",20))
placename.grid(column=0,row=2)

def weather():
    location = placename.get()
    api_key = "cf68af6b1720ee2d0fb9db397e7632d2"
    api = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response=requests.get(api)
    x=response.json()
    y=x["main"]
    current_temp= round(y["temp"]-273.15)

    if (current_temp>25):
        temperature.configure(text=current_temp, bg="orange", fg="red")
        description.configure(text="it is hot")
    else:
        temperature.configure(text=current_temp, bg="lightblue", fg="navyblue")
        description.configure(text="it is cold")
find=Button(text="fint it!",command=weather, bg="#FFF8E7", fg="#4B0082")
find.grid(column=0 , row= 4)

temperature=Label(text="temperature:", font=("Arial",20), bg="#FDE2E4",fg="#4B0082")
temperature.grid(column=0, row=5)

description= Label(text="weather of the place:", font=("Arial",20), bg="#FDE2E4",fg="#4B0082")
description.grid(column=0, row=6)

window.geometry('600x400')
window.mainloop()