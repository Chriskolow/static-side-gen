from textnode import TextNode, TextType

def main():
    node = TextNode("Hello World", TextType.BOLD, "https://boot.dev")
    print(node.__repr__())

main()
