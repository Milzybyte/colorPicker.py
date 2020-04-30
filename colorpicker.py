"""
Program: colorpicker.py
"""

from breezypythongui import EasyFrame
import tkinter.colorchooser

class ColorPicker(EasyFrame):
    """Display the resualt of pickin a color."""
    def __init__(self):
        EasyFrame.__init__(self, title = "Choose yout color!",
                           background = "tan")
        
        #Labels amd output fields
        self.r = self.addLabel("R", row = 0, column = 0,
                               background = "red")
        self.g = self.addLabel("G", row = 1, column = 0,
                               background = "green")
        self.b = self.addLabel("B", row = 2, column = 0,
                               background = "blue")
        self.addLabel("Color", row = 3, column = 0)
        self.r = self.addIntegerField(value = 0,
                                      row = 0, column = 1)
        self.g = self.addIntegerField(value = 0,
                                      row = 1, column = 1)
        self.b = self.addIntegerField(value = 0,
                                      row = 2, column = 1)                                    
        self.hex = self.addTextField(text = "#000000",
                                     row = 3, column = 1,
                                     width = 10)
        
        
        #Canvas with an inital black background
        self.canvas = self.addCanvas(row = 0, column = 2,
                                      rowspan = 4,
                                      width = 50,
                                      background = "#000000")
        
        #Command button
        self.button = self.addButton(text = "Choose color",
                       row = 4, column = 0,
                       columnspan = 3,
                       command = self.chooseColor)
        self.button["background"] = "cyan"               
    #Event handling method
    def chooseColor(self):
        """Pops uup a color chooser and outputs the result"""
        colorTuple = tkinter.colorchooser.askcolor()
        if not colorTuple[0]: 
            return
        ((r,g,b), hexString) = colorTuple
        #Assing the values of our colorTuple to the gui
        self.r.setNumber(int(r))
        self.g.setNumber(int(g))
        self.b.setNumber(int(b))
        self.hex.setText(hexString)
        self.canvas["background"] = hexString
            
#Definition of the main() function
def main():
    """instantiantes and pops up the window"""
    ColorPicker().mainloop()
    
if __name__ == "__main__":
    main()                 