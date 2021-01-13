import tkinter
import requests
import json

root = tkinter.Tk()

label = tkinter.Label(root, text="Hello World!") # Create a text label
label.pack(padx=20, pady=20) # Pack it into the window

canvas = tkinter.Canvas(root, width = 300, height = 300)
canvas.pack()
img = tkinter.PhotoImage(file="graphics/buildings/house/texture.png")
canvas.create_image(20,20, anchor=tkinter.NW, image=img)

frame = tkinter.Frame(root)
frame.pack()

def Request():
    r = requests.get('http://127.0.0.1:8888/api/v0')
    #r = requests.get('https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Nc2JKvYFoAEOFCG5JSI6/FeatureServer/2/query?f=json&where=OBJECTID%3D24&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Deaths%20desc&outSR=102100&resultOffset=0&resultRecordCount=200&resultType=standard&cacheHint=true')
    #print(r.text)
    data_warbanner = json.loads(r.text + "sdf")
    data_warbanner_url = data_warbanner["1"]["server"]["homeUrl"]
    print(data_warbanner_url)


button = tkinter.Button(frame, text="QUIT", fg="red", command=Request)
button.pack(side=tkinter.LEFT)

root.mainloop()