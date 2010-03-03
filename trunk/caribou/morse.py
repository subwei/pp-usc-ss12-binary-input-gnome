#!/usr/bin/python

import virtkey
import time
from morsetree import get_morse_tree

class Morse:
    def  __init__(self):
        self._tree_update_callback = None
        self.mt = get_morse_tree()
        self._dot_down = False
        self._dash_down = False
        self._select_state = False
        self._firstkeydowntime = 0
        self._twokeys_starttime = 0
        self._backspace = False
        self._newline = False
        self.vk = virtkey.virtkey()
        self._morse_enabled = True
        
        # The following is a hack to make this program initially type with
        # lower-case letters instead of upper-case; because we're using
        # l-shift and r-shift as our two buttons, it capitalizes whatever
        # we type. We'll start with caps-lock on to reverse that.
        self.vk.press_keycode(66)    # 66 is capslock
        self.vk.release_keycode(66)

    def send_unicode(self, key):
        if len(key) == 1:
            char = ord(key.decode('utf-8'))
            self.vk.press_unicode(char)
            self.vk.release_unicode(char)

    def registerListener(self, callback):
        self._tree_update_callback = callback

    def enable(self):
        self._morse_enabled = True

    def disable(self):
        self._morse_enabled = False

    def key_up(self, event):
        """Listens for when the dot button (l-shift) and the dash button
        (r-shift) are released.
        
        The morse code tree is traversed on button releases, and backspaces
        are entered by holding dash (r-shift) and tapping dot (l-shift). Also,
        newlines are entered by holding dot (l-shift) and tapping dash 
        (r-shift)
        """
        if self._morse_enabled == True:
            if event.event_string == "Shift_L":
                self._dot_down = False
                if self._backspace == True:
                    self.vk.press_keysym(0xff08)     # 0xff08 is backspace
                    self.vk.release_keysym(0xff08)  
                    self.mt.reset()
                elif self._newline == True:
                    self._newline = False  
                    firstkeydowntime = 0
                elif self._select_state == False:
                    if self.mt.get_current_node().left:
                        self.mt.dot()
                    else:
                        self.mt.reset()
                    self._tree_update_callback(self.mt.get_current_node())
                elif self._select_state == True and self._dash_down == False:
                    self._select_state = False  
                    if (time.time() - self._twokeys_starttime) > 0.5:
                        self.vk.press_keysym(0xff08)     # 0xff08 is backspace
                        self.vk.release_keysym(0xff08)
                        self.vk.press_keycode(66)   # 66 is capslock
                        self.vk.release_keycode(66)          
            elif event.event_string == "Shift_R":
                self._dash_down = False
                if self._newline == True:
                    self.vk.press_keysym(0xff0d)    # 0xff0d is newline
                    self.vk.release_keysym(0xff0d)
                    self.mt.reset()
                elif self._backspace == True:
                    self._backspace = False
                    firstkeydowntime = 0    
                elif self._select_state == False:
                    if self.mt.get_current_node().right:
                        self.mt.dash()
                    else:
                        self.mt.reset()
                    self._tree_update_callback(self.mt.get_current_node())
                elif self._select_state == True and self._dot_down == False:
                    self._select_state = False
                    if (time.time() - self._twokeys_starttime) > 0.5:
                        self.vk.press_keysym(0xff08)     # 0xff08 is backspace
                        self.vk.release_keysym(0xff08)
                        self.vk.press_keycode(66)   # 66 is capslock
                        self.vk.release_keycode(66)

    def key_down(self, event):
        """Listens for when the input buttons--the dot button (l-shift), the 
        dash button (r-shift), and the quit button (r-ctrl)--are pressed.
        
        If both the dot and the dash buttons are pressed, the current 
        character of the morse code tree is selected and the tree is reset.
        """
        if self._morse_enabled == True:
            if event.event_string == "Shift_L":
                self._dot_down = True
                if self._dash_down == False:
                    self._firstkeydowntime = time.time()
                else:
                    self._twokeys_starttime = time.time()
                    twokeytime = time.time() - self._firstkeydowntime
                    if twokeytime < 0.25:
                        self._select_state = True
                        self.send_unicode(self.mt.current_node.value)
                        self.mt.reset()
                        self._tree_update_callback(self.mt.get_current_node())
                    else:
                        self._backspace = True
            elif event.event_string == "Shift_R":
                self._dash_down = True
                if self._dot_down == False:
                    self._firstkeydowntime = time.time()
                else:
                    self._twokeys_starttime = time.time()
                    twokeytime = time.time() - self._firstkeydowntime
                    if twokeytime < 0.25:
                        self._select_state = True
                        self.send_unicode(self.mt.current_node.value)
                        self.mt.reset()
                        self._tree_update_callback(self.mt.get_current_node())
                    else:
                        self._newline = True

if __name__ == "__main__":
    morse = Morse()
    for x in range(10):
        print x
