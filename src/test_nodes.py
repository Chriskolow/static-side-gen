import unittest
from textnode import TextType, TextNode
from nodes import split_nodes_delimiter

class MyTestCase(unittest.TestCase):
    def test_something(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
    TextNode("This is text with a ", TextType.TEXT, None),
    TextNode("code block", TextType.CODE, None),
    TextNode(" word", TextType.TEXT, None),
    ])

    def test_no_type_text(self):
        node = TextNode("This is text with a `code block` word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a `code block` word", TextType.BOLD, None)])

    def test_invalid_markdown_raises_exception(self):
        node = TextNode("This has an `unclosed delimiter", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == '__main__':
    unittest.main()
