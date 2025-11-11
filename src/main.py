from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    node = TextNode("Hello World", TextType.BOLD, "https://boot.dev")
    print(node.__repr__())

    propsdic = {"href": "https://google.com"}
    htmnode = HTMLNode("a", "Hier Link", "Test")
    print(htmnode.__repr__())
    print(htmnode.props_to_html())

    leafnode = LeafNode("a", "Google", propsdic)
    print(leafnode.to_html())

    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())

    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case text_node.text_type.TEXT:
            return LeafNode(None, text_node.text)
        case text_node.text_type.BOLD:
            return LeafNode("b", text_node.text)
        case text_node.text_type.ITALIC:
            return LeafNode("i", text_node.text)
        case text_node.text_type.CODE:
            return LeafNode("code", text_node.text)
        case text_node.text_type.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case text_node.text_type.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Wrong Text Type!")

main()
node = TextNode("This is a Link node", TextType.LINK, "https://google.com")
print(text_node_to_html_node(node))
