from src.node import Node

def load_corpus(filename):
    with open(filename, "r") as f:
        return f.read().replace("\n", "")

def print_tree(node, level=0):
  # thank u copilot for this code
  print("  " * level + f"{node.value} (count: {node.count})")
  for child in node.children.values():
      print_tree(child, level + 1)

if __name__ == "__main__":
    example_text = load_corpus("example_corpus.txt")
    root = Node("root", 0, {})
    # Tokenize the text
    tokenized_text = [sent.split() for sent in example_text.split(".")]
    print(tokenized_text)
    # Create the tree
    for sent in tokenized_text:
        if not sent:
            continue
        current_node = root
        for word in sent:
            word = word.strip()
            print(word  )
            if word in current_node.children:
                current_node = current_node.children[word]
                current_node.count += 1
            else:
                new_node = Node(word, 1, {})
                current_node.add_child(new_node)
                current_node = new_node

    print_tree(root)
