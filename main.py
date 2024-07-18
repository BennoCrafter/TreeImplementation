from src.node import Node

example_text = "Harry Potter is a wizard. He goes to Hogwarts. He is in Gryffindor. He has a friend named Ron. Ron has a rat named Scabbers. Harry has a pet owl named Hedwig. Harry has a wand. He has a scar on his forehead."
root = Node("root", 0, {})
# Tokenize the text
tokenized_text = [sent.split() for sent in example_text.split(".")]

# Create the tree
for sent in tokenized_text:
    # set the current node to the root
    current_node = root
    for word in sent:
        if word in current_node.children:
            current_node = current_node.children[word]
            current_node.count += 1
        else:
            new_node = Node(word, 1, {})
            current_node.add_child(new_node)
            current_node = new_node

# Print the tree
def print_tree(node, level=0, prefix=""):
    indent = "  " * level
    print(f"{indent}{prefix}└── {node.value} ({node.count})")
    for i, child in enumerate(node.children.values()):
        new_prefix = "├── " if i < len(node.children) - 1 else "└── "
        print_tree(child, level + 1, new_prefix)

print_tree(root)
