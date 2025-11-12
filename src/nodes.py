from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != text_type.TEXT:
            nodes.append(node)
        else:
            if node.text.count(delimiter) % 2 != 0:
                raise Exception("No closing delimiter")
            x = node.text.split(delimiter)
            for i in range(len(x)):
                if i != 0 and i % 2 != 0:
                    type = text_type
                else:
                    type = TextType.TEXT
                temp = TextNode(x[i], type)
                nodes.append(temp)
    return nodes
