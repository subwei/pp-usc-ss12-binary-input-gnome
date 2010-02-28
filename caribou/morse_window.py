#!/usr/bin/python

import gtk
import colorhandler

class MorseWindow:
    
    colorHandler = colorhandler.ColorHandler()

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

    def colorKeys(self, startingNode):
	self.colorHandler.colorAll(colorhandler.ColorOptions.standard) #Reset all colors to gray
	self.colorHandler.setColorFromChar(startingNode.value, colorhandler.ColorOptions.morseCurrentNode) #color our current node
	leftNode = startingNode.left
	rightNode = startingNode.right
	if leftNode != None:
		self.colorHandler.setColorFromChar(leftNode.value, colorhandler.ColorOptions.morseLeftNode) #color our direct descendant
		self.recursiveColorNodes(leftNode, colorhandler.ColorOptions.morseLeftNode) #and color its descendants
	if rightNode != None:
		self.colorHandler.setColorFromChar(rightNode.value, colorhandler.ColorOptions.morseRightNode) #color our direct descendant
		self.recursiveColorNodes(rightNode, colorhandler.ColorOptions.morseRightNode) #and color its descendants

    def recursiveColorNodes(self, startingNode, color):
	if startingNode.left != None: #If we have an instantiated node to go to
	    self.colorHandler.setColorFromChar(startingNode.left.value, color)
	    self.recursiveColorNodes(startingNode.left, color)
	if startingNode.right != None: #If we have an instantiated node to go to
	    self.colorHandler.setColorFromChar(startingNode.right.value, color)
	    self.recursiveColorNodes(startingNode.right, color)


    def refresh(self, currentNode):
        if currentNode != None:
	    self.colorKeys(currentNode)
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
