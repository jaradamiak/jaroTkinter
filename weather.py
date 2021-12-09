# python grid.py
from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Windows")
root.iconbitmap('images/unisa.ico')
root.geometry("600x100")

def zipLookup():
    # zipLabel = Label(root, text=zip.get())
    # zipLabel.grid(row=1, column=0, columnspan=2)
    
    try:
        weather_color = ""
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=23256AA9-F5C5-4B00-9001-62E272E7F35C")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        if category == "Good":
            weather_color = "green"
        elif category == "Moderate":
            weather_color = "yellow"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ffff00"
        elif category == "Unhealthy":
            weather_color = "#ff0000"
        elif category == "Very Unhealthy":
            weather_color = "#990006"
        elif category == "Hazardous":
            weather_color = "#660000"
        root.configure(background=weather_color)
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + 
                    category, font=("Helvetica", 20), background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."

# https://docs.airnowapi.org/CurrentObservationsByZip/query
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=23256AA9-F5C5-4B00-9001-62E272E7F35C



zip = Entry(root)
zip.grid(row=0, column=0)

zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1)
root.mainloop()