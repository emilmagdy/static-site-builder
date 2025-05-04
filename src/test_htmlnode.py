import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
      
    def test_Non_equal_nodes(self):
        node =HTMLNode("a", "soem text", "child")
        node1 =HTMLNode("p", "some text", "child")
        self.assertNotEqual(node, node1)

    def test_leaf_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")  
        st2 ="<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), st2)

    def test_leaf_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        st = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), st)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
        