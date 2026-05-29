import tkinter as tk



class myapps:
    def __init__(self,root:tk.Tk,backgrounds:str,colors:list,widths:int,heights:int,values:list,titles:str):
        self.root=root
        self.root.title(titles)
        self.root.geometry(str(widths)+"x"+str(heights))
        self.root.configure(background=backgrounds)
        self.canvas= tk.Canvas(background=backgrounds,width=widths,height=heights)
        self.canvas.pack(padx=0,pady=0)
        self.colors=colors
        self.angle=359.99
        canv=self.canvas
        angl=0
        aaa=0
        for a in values:
            aa:float=3.60 * float(a)
            if aaa>=len(self.colors):
                aaa=len(self.colors)-1
            canv.create_arc(0,0,widths,heights,start=angl,extent=aa,fill=self.colors[aaa])
            angl=angl+aa
            aaa=aaa+1



def starts(backgrounds:str,colors:list,widths:int,heights:int,values:int,titles:str):
    root=tk.Tk()
    apps=myapps(root,backgrounds,colors,widths,heights,values,titles)
    root.mainloop()

titles="pie"
backgrounds="black"
widths=480
heights=480
colors=["blue","red","green","yellow","white","black"]
values=[20,20,20,20,20]

starts(backgrounds,colors,widths,heights,values,titles)
