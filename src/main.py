from textnode import TextNode, TextType


def main():
    node = TextNode(
        "This is an ankor text",
        TextType.LINK,
        "https://google.com"
    )
    print(node)

main()
