from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import tensorflow as tf


class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.attributes('-fullscreen',True)

        #background for window
        mg = Image.open("/Users/narimanhosseinzadeh/Documents/Codes/python_ai/Cat_vs_Dog_Classification/images/background_image.jpg")
        bg_photo = ImageTk.PhotoImage(mg)
        self.backL = Label(image=bg_photo)
        self.backL.place(relwidth=1, relheight=1)
        
        

        
        self.root.title("Cat_vs_dog")
        
        self.button = Button(self.root,text="Select Image",bg="Black",command=self.get_image_path)
        self.button.place(relx=0.5,rely=0.2,anchor=CENTER)
        
        self.label1 = Label(self.root)
        self.label1.place(relx=0.5,rely=0.6,anchor=CENTER)
        self.root.mainloop()
    def get_image_path(self):
        self.file_path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("jpg files", "*.jpeg")))
        self.prep_image()
        self.label = Label(self.root,text=self.text,bg="Black")
        self.label.place(relx=0.5,rely=0.3,anchor=CENTER)
         
        self.label1.config(image=self.img_tk)
        
        
        
        
        
    def prep_image(self):
        img = cv2.imread(self.file_path)
        c_img = cv2.resize(img, (64, 64))
        c_img = c_img / 255.0 
        c_img = np.array([c_img]) 
        
        network = tf.keras.models.load_model("/Users/narimanhosseinzadeh/Documents/Codes/python_ai/Cat_vs_Dog_Classification/Cat_Dog_Classifier.h5")
        prediction = network.predict(c_img)
        classes = ["cat","dog"]
        index = np.argmax(prediction)
        self.text = f"{classes[index]}:{prediction[0][index]*100:.2f}"
        img = Image.open(self.file_path)
        img.thumbnail((400, 400))  # Resize image to fit the app
        self.img_tk = ImageTk.PhotoImage(img)
        
        
app = Gui()