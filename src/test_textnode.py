import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("This is the text" , TextType.ITALIC )
        node1 = TextNode("This is other node", TextType.ITALIC )
        self.assertNotEqual(node, node1)

    def test_not_equal(self):
        node = TextNode("This is the text" , TextType.LINK, "http://google.com" )
        node1 = TextNode("This is the text", TextType.ITALIC  )
        self.assertNotEqual(node, node1)

if __name__ == "__main__":
    unittest.main()