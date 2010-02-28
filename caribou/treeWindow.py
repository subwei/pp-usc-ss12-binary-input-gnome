import gconf
import gobject
import gtk
import sys

class TreeWindow(gtk.Frame):
  __gtype_name__ = "TreeWindow"
  
  def __init__(self):
    gtk.Frame.__init__(self)
    #self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    
    self.parentNode = gtk.Button("")
    self.leftChild = gtk.Button("e")
    self.rightChild = gtk.Button("t")
    
    vbox = gtk.VBox(True, 0)
    parentRow = gtk.HBox(True, 0)
    parentRow.pack_start(self.parentNode, True, False, 2)
    childrenRow = gtk.HBox(True, 0)
    childrenRow.pack_start(self.leftChild, True, False, 2)
    childrenRow.pack_start(self.rightChild, True, False, 2)
    
    vbox.pack_start(parentRow, True, False, 2)
    vbox.pack_start(childrenRow, True, False, 2)
    self.add(vbox)
    #self.fixed = gtk.Fixed()
    #self.fixed.put(self.nodeButton, 30, 0)
    #self.fixed.put(self.leftChild, 10, 50)
    #self.fixed.put(self.rightChild, 50, 50)
    #self.morseRoot.show()
    #self.morseLeft.show()
    #self.morseRight.show()
    #self.fixed.show()
    self.show_all()
    
  def refresh(self, currentNode):
        if currentNode != None:
            self.parentNode.set_label(currentNode.value)
            if currentNode.left != None:
                self.leftChild.set_label(currentNode.left.value)
            else:
                self.leftChild.set_label("")

            if currentNode.right != None:
                self.rightChild.set_label(currentNode.right.value)
            else:
                self.rightChild.set_label("")
        else:
            self.parentNode.set_label("")
            self.leftChild.set_label("")
            self.rightChild.set_label("")
            
if __name__ == "__main__":
  treeWindow = TreeWindow()
  window = gtk.Window(gtk.WINDOW_TOPLEVEL)
  window.add(treeWindow)
  window.show_all()
  gtk.main()
