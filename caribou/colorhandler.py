import gtk

class ColorOptions: #This is basically just an enum
	standard = 0
	morseLeftNode = 1
	morseRightNode = 2
	test = 3

class ColorHandler:

 	e = gtk.Entry()
	map = e.get_colormap()

	buttonList = dict() #key = letter of the button, value = style of button (that style will use color colorOption)
	morseLeftNodeColor = map.alloc_color("#7171f0")
	morseRightNodeColor = map.alloc_color("#f07171")
	standardColor = map.alloc_color("#cccccc")
	testColor = map.alloc_color("#ff99ff")
	colorMap = {ColorOptions.standard: standardColor, ColorOptions.morseLeftNode: morseLeftNodeColor, ColorOptions.morseRightNode: morseRightNodeColor, ColorOptions.test: testColor}  

	def addButton(self, button, colorOption):
		label = button.get_label()
		self.buttonList[label] = button
		self.setColor(button, colorOption)

	def setColorFromEncodedChar(self, encodedchar, colorOption):
		char = unichr(encodedchar)
		self.setColor(self.buttonList.get(char), colorOption)

	def setColor(self, button, colorOption):
		button.modify_bg(gtk.STATE_NORMAL, self.colorMap.get(colorOption))
		button.modify_bg(gtk.STATE_ACTIVE, self.colorMap.get(colorOption))

	def _colorAll(self, colorOption):
		for button in self.buttonList.values():
			button.modify_bg(gtk.STATE_NORMAL, self.colorMap.get(colorOption))
			button.modify_bg(gtk.STATE_ACTIVE, self.colorMap.get(colorOption))
