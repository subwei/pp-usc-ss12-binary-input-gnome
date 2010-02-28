#!/usr/bin/env python
# This Python file uses the following encoding: utf-8


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class MorseTree:
    def __init__(self, root):
        self.root = root
        self.current_node = root

    def reset(self):
        self.current_node = self.root

    def dot(self):
        self.current_node = self.current_node.left
        return self.current_node

    def dash(self):
        self.current_node = self.current_node.right
        return self.current_node

    def leaf(self):
        if not self.current_node.left and not self.current_node.right:
            return True
        else:
            return False

    def get_current_node(self):
        return self.current_node

    def __str__(self):
        return self.current_node.value

def get_morse_tree():
    root = TreeNode("")

    # normal alphabet
    node_a = TreeNode("a")
    node_b = TreeNode("b")
    node_c = TreeNode("c")
    node_d = TreeNode("d")
    node_e = TreeNode("e")
    node_f = TreeNode("f")
    node_g = TreeNode("g")
    node_h = TreeNode("h")
    node_i = TreeNode("i")
    node_j = TreeNode("j")
    node_k = TreeNode("k")
    node_l = TreeNode("l")
    node_m = TreeNode("m")
    node_n = TreeNode("n")
    node_o = TreeNode("o")
    node_p = TreeNode("p")
    node_q = TreeNode("q")
    node_r = TreeNode("r")
    node_s = TreeNode("s")
    node_t = TreeNode("t")
    node_u = TreeNode("u")
    node_v = TreeNode("v")
    node_w = TreeNode("w")
    node_x = TreeNode("x")
    node_y = TreeNode("y")
    node_z = TreeNode("z")

    # numbers
    node_0 = TreeNode("0")
    node_1 = TreeNode("1")
    node_2 = TreeNode("2")
    node_3 = TreeNode("3")
    node_4 = TreeNode("4")
    node_5 = TreeNode("5")
    node_6 = TreeNode("6")
    node_7 = TreeNode("7")
    node_8 = TreeNode("8")
    node_9 = TreeNode("9")

    # weird characters
    node_u_umlaut = TreeNode("ü")
    node_a_umlaut = TreeNode("ä")
    node_o_umlaut = TreeNode("ö")
    node_ch = TreeNode("ch")

    # first level
    root.left = node_e
    root.right = node_t

    # second level
    node_e.left = node_i
    node_e.right = node_a

    node_t.left = node_n
    node_t.right = node_m

    # third level
    node_i.left = node_s
    node_i.right = node_u

    node_a.left = node_r
    node_a.right = node_w

    node_n.left = node_d
    node_n.right = node_k

    node_m.left = node_g
    node_m.right = node_o

    # fourth level
    node_s.left = node_h
    node_s.right = node_v

    node_u.left = node_f
    node_u.right = node_u_umlaut

    node_r.left = node_l
    node_r.right = node_a_umlaut

    node_w.left = node_p
    node_w.right = node_j

    node_d.left = node_b
    node_d.right = node_x

    node_k.left = node_c
    node_k.right = node_y

    node_g.left = node_z
    node_g.right = node_q

    node_o.left = node_o_umlaut
    node_o.right = node_ch

    return MorseTree(root)

