import re
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

def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    output =[]
    for node in old_nodes:
        string = node.text
        alt_url = extract_markdown_images(string)
        i = 0
        while string != "":
            temp = string.split("!", 1)
            string = string.removeprefix(temp[0])
            temp[0] =temp[0].lstrip(")")
            if temp[0] != "":
                output.append(TextNode(temp[0], TextType.TEXT, None))
            temp = string.split(")", 1)
            string = string.removeprefix(temp[0])
            if i < len(alt_url):
                output.append(TextNode(alt_url[i][0], TextType.IMAGE, alt_url[i][1]))
            i += 1

        return output

def split_nodes_link(old_nodes):
    output = []
    for node in old_nodes:
        string = node.text
        alt_url = extract_markdown_links(string)
        i = 0
        while string != "":
            temp = string.split("[", 1)
            string = string.removeprefix(temp[0])
            temp[0] = temp[0].lstrip(")")
            if temp[0] != "":
                output.append(TextNode(temp[0], TextType.TEXT, None))
            temp = string.split(")", 1)
            string = string.removeprefix(temp[0])
            if i < len(alt_url):
                output.append(TextNode(alt_url[i][0], TextType.LINK, alt_url[i][1]))
            i += 1

        return output
