import tkinter as tk



class myapps:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("pie")
        self.root.geometry("480x480")
        self.root.configure(background="black")
        self.canvas= tk.Canvas(background="black",width=480,height=480)
        self.canvas.pack(padx=0,pady=0)
        self.colors=["blue","red","green","yellow","black"]
        self.angle=359
        canv=self.canvas
        for a in range(len(self.colors)-1):
            canv.create_arc(0,0,480,480,start=0,extent=self.angle-(a*80),fill=self.colors[a])
 




root=tk.Tk()
apps=myapps(root)
root.mainloop()
