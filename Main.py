from tkinter import *


class Main(object):
    """Main Class from where the count object created"""  
    root = Tk()
    countNumberLabel = Label(root, text=0, bg='#5DD062', width=8, height=2)    
    
    
    def __init__(self, bgColor):
        self.bgColor = bgColor
    
    
    def resetCount(self):
        self.countNumberLabel['text'] = 0
    
    
    def count(self):
        self.countNumberLabel['text'] += 1
    
    
    def main(self):
        """we create our window and button,
        on the method"""
        self.root.geometry('300x294')
        self.root.title('Count App')
        self.root.config(bg=self.bgColor)
   
        
        resetButton = Button(self.root, text='Reset', bg='#5DD062', activebackground='#5DD062', command=self.resetCount)
        resetButton.pack()
        
          
        self.countNumberLabel.pack()
        
        
        countButton = Button(self.root, text='count', bg='#5DD062', activebackground='#5DD062', command=self.count)
        countButton.pack()
        
        
        self.root.mainloop()


if __name__ == '__main__':
    countApp = Main('#CAE9E1')
    countApp.main()