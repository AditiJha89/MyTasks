from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=facecfee7e3b4f5bcbb788c6ac8dfdcb").json()
    
    hum_label1.config(text=data["main"]["humidity"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    wind_label1.config(text=data["wind"]["speed"])
    wb_label1.config(text=data["weather"][0]["description"])

win = Tk()
win.title("Weather Forecast API")
win.config(bg = "cornflowerblue")
win.geometry("500x570")


name_label = Label(win,text=" Current Weather Forecast ",font=("Time New Roman",22,"bold"),fg="darkgreen")
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()

city_list = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand",
             "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu",
             "Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu",
             "Lakshadweep","National Capital Territory of Delhi","Puducherry"]

combo = ttk.Combobox(win,text="Weather Forecast ",values=city_list,font=("Time New Roman",18,"bold"),textvariable=city_name)
combo.place(x=25,y=120,height=50,width=450)


# ------------------------------------------------------------------------------------------------

hum_label = Label(win,text="Humidity",font=("Time New Roman",15,"bold"))
hum_label.place(x=25,y=260,height=50,width=210)

hum_label1 = Label(win,text="",font=("Time New Roman",15,"bold"),fg="lightseagreen")
hum_label1.place(x=250,y=260,height=50,width=210)

# -----------------------------------------------------------------------------------

temp_label = Label(win,text="Tempreture",font=("Time New Roman",15,"bold"))
temp_label.place(x=25,y=330,height=50,width=210)

temp_label1 = Label(win,text=" ",font=("Time New Roman",15,"bold"),fg="red")
temp_label1.place(x=250,y=330,height=50,width=210)

# ---------------------------------------------------------------------------------

wind_label = Label(win,text="Wind Speed",font=("Time New Roman",15,"bold"))
wind_label.place(x=25,y=400,height=50,width=210)

wind_label1 = Label(win,text=" ",font=("Time New Roman",15,"bold"),fg="deepskyblue")
wind_label1.place(x=250,y=400,height=50,width=210)

# -------------------------------------------------------------------------------
wb_label = Label(win,text="Weather Description",font=("Time New Roman",15,"bold"))
wb_label.place(x=25,y=470,height=50,width=210)

wb_label1 = Label(win,text=" ",font=("Time New Roman",15,"bold"),fg="purple")
wb_label1.place(x=250,y=470,height=50,width=210)

#-----------------------------------------------------------------------------------------

done_button = Button(win,text="Search",font=("Time New Roman",15,"bold"),bg="darkgreen",command=data_get)
done_button.place(y=190,height=50,width=120,x=210)



win.mainloop()