import unittest
from textnode import TextType, TextNode
from nodes import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [Link Text](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("Link Text", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == '__main__':
    unittest.main()
