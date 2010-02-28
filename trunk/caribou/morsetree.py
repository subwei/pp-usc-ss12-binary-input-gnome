#!/usr/bin/env python

class TreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

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

	def __str__(self):
		return self.current_node.value

def get_morse_tree():
	root = TreeNode("")
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

	root.left = node_e
	root.right = node_t

	node_e.left = node_i
	node_e.right = node_a

	node_t.left = node_n
	node_t.right = node_m

	node_i.left = node_s
	node_i.right = node_u

	node_a.left = node_r
	node_a.right = node_w

	node_n.left = node_d
	node_n.right = node_k

	node_m.left = node_g
	node_m.right = node_o

	morse_tree = MorseTree(root)

	return morse_tree



