#!/usr/bin/python

import gtk

class MorseWindow:
    
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.morseRoot = gtk.Button("")
        self.morseLeft = gtk.Button("e")
        self.morseRight = gtk.Button("i")
        self.fixed = gtk.Fixed()
        self.window.add(self.fixed)
        self.fixed.put(self.morseRoot, 30, 0)
        self.fixed.put(self.morseLeft, 10, 50)
        self.fixed.put(self.morseRight, 50, 50)
        self.morseRoot.show()
        self.morseLeft.show()
        self.morseRight.show()
        self.fixed.show()
        self.window.show()

    def refresh(self, currentNode):
        if currentNode != None:
            self.morseRoot.set_label(currentNode.value)
            if currentNode.left != None:
                self.morseLeft.set_label(currentNode.left.value)
            else:
                self.morseLeft.set_label("")

            if currentNode.right != None:
                self.morseRight.set_label(currentNode.right.value)
            else:
                self.morseRight.set_label("")
        else:
            self.morseRoot.set_label("")
            self.morseLeft.set_label("")
            self.morseRight.set_label("")

    def main(self):
        gtk.main()

if __name__ == "__main__":
    print "Hello world!"
    morse_window = MorseWindow()
    morse.main() 
