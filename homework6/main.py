import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create a directed graph
# G = nx.DiGraph()
# Create a undirected graph
G = nx.Graph()

# Add the null node (empty set)
G.add_node("∅", label="∅-F", level=0)

# Add nodes for Level 1 (1-itemsets)
G.add_node("a", label="a-F", level=1)
G.add_node("b", label="b-F", level=1)
G.add_node("c", label="c-F", level=1)
G.add_node("d", label="d-F", level=1)
G.add_node("e", label="e-F", level=1)

# Add nodes for Level 2 (2-itemsets)
G.add_node("ab", label="ab-F", level=2)
G.add_node("ac", label="ac-I", level=2)
G.add_node("ad", label="ad-F", level=2)
G.add_node("ae", label="ae-F", level=2)
G.add_node("bc", label="bc-F", level=2)
G.add_node("bd", label="bd-F", level=2)
G.add_node("be", label="be-F", level=2)
G.add_node("cd", label="cd-F", level=2)
G.add_node("ce", label="ce-I", level=2)
G.add_node("de", label="de-F", level=2)

# Add nodes for Level 3 (3-itemsets)
G.add_node("abc", label="abc-N", level=3)
G.add_node("abd", label="abd-I", level=3)
G.add_node("abe", label="abe-I", level=3)
G.add_node("acd", label="acd-N", level=3)
G.add_node("ace", label="ace-N", level=3)
G.add_node("ade", label="ade-F", level=3)
G.add_node("bcd", label="bcd-I", level=3)
G.add_node("bce", label="bce-N", level=3)
G.add_node("bde", label="bde-F", level=3)
G.add_node("cde", label="cde-N", level=3)

# Add nodes for Level 4 (4-itemsets)
G.add_node("abcd", label="abcd-N", level=4)
G.add_node("abce", label="abce-N", level=4)
G.add_node("abde", label="abde-N", level=4)
G.add_node("acde", label="acde-N", level=4)
G.add_node("bcde", label="bcde-N", level=4)

# Add nodes for Level 5 (5-itemset)
G.add_node("abcde", label="abcde-N", level=5)

# Add edges from the null node to Level 1
edges = [("∅", "a"), ("∅", "b"), ("∅", "c"), ("∅", "d"), ("∅", "e")]

# Add edges between levels
edges += [
    # Level 1 to Level 2
    ("a", "ab"), ("a", "ac"), ("a", "ad"), ("a", "ae"),
    ("b", "ab"), ("b", "bc"), ("b", "bd"), ("b", "be"),
    ("c", "ac"), ("c", "bc"), ("c", "cd"), ("c", "ce"),
    ("d", "ad"), ("d", "bd"), ("d", "cd"), ("d", "de"),
    ("e", "ae"), ("e", "be"), ("e", "ce"), ("e", "de"),
    
    # Level 2 to Level 3
    ("ab", "abc"), ("ab", "abd"), ("ab", "abe"),
    ("ac", "abc"), ("ac", "acd"), ("ac", "ace"),
    ("ad", "abd"), ("ad", "acd"), ("ad", "ade"),
    ("ae", "abe"), ("ae", "ace"), ("ae", "ade"),
    ("bc", "abc"), ("bc", "bcd"), ("bc", "bce"),
    ("bd", "abd"), ("bd", "bcd"), ("bd", "bde"),
    ("be", "abe"), ("be", "bce"), ("be", "bde"),
    ("cd", "acd"), ("cd", "bcd"), ("cd", "cde"),
    ("ce", "ace"), ("ce", "bce"), ("ce", "cde"),
    ("de", "ade"), ("de", "bde"), ("de", "cde"),
    
    # Level 3 to Level 4
    ("abc", "abcd"), ("abc", "abce"),
    ("abd", "abcd"), ("abd", "abde"),
    ("abe", "abce"), ("abe", "abde"),
    ("acd", "abcd"), ("acd", "acde"),
    ("ace", "abce"), ("ace", "acde"),
    ("ade", "abde"), ("ade", "acde"),
    ("bcd", "abcd"), ("bcd", "bcde"),
    ("bce", "abce"), ("bce", "bcde"),
    ("bde", "abde"), ("bde", "bcde"),
    ("cde", "acde"), ("cde", "bcde"),
    
    # Level 4 to Level 5
    ("abcd", "abcde"), ("abce", "abcde"),
    ("abde", "abcde"), ("acde", "abcde"),
    ("bcde", "abcde")
]

G.add_edges_from(edges)

# Define a hierarchical layout based on levels
pos = {}
y_offset = 0
for level in range(0, 6):  # Levels 0 to 5
    nodes_at_level = [node for node, data in G.nodes(data=True) if data["level"] == level]
    x_offset = -len(nodes_at_level) / 2  # Center nodes horizontally
    for i, node in enumerate(nodes_at_level):
        pos[node] = (x_offset + i, -y_offset)  # Position nodes
    y_offset += 1  # Move to the next level
    

# Extract labels for nodes
labels = nx.get_node_attributes(G, "label")


# Define a color mapping based on the label suffix
color_map = {
    "-F": "#4682b4",  # Blue for "Frequent"
    "-I": "#ffa500",  # Orange for "Infrequent"
    "-N": "#ff4500"   # Red for "Non-frequent"
}
# Create legend patches with marker borders
legend_patches = [
    mpatches.Patch(facecolor="#4682b4", label="Frequent (-F)", edgecolor="black"),
    mpatches.Patch(facecolor="#ffa500", label="Infrequent (-I)", edgecolor="black"),
    mpatches.Patch(facecolor="#ff4500", label="Non-candidate (-N)", edgecolor="black")  # Example with white border
]

# Assign colors to nodes based on their labels
node_colors = []
for node in G.nodes(data=True):
    label = node[1].get("label", "")
    suffix = label.split("-")[-1]  # Extract the suffix (e.g., "F", "I", "N")
    node_colors.append(color_map.get(f"-{suffix}", "#808080"))  # Default to gray if no match

# Draw the graph
fig = plt.figure(figsize=(20, 12))


# Add the legend with larger size
plt.legend(
    handles=legend_patches,
    loc="upper left",  # Position the legend
    bbox_to_anchor=(0, 1),  # Adjust the position of the legend
    fontsize=20,  # Explicitly set the font size
    markerscale=3,  # Scale up the size of the legend markers
    prop={'size': 20, 'family': 'STIXGeneral'}  # Explicitly set font size and family
)

nx.draw(G, pos, with_labels=False, node_size=3000, 
        # node_color='#4682b4',  
        edge_color='#FFFFFF',
        # labels=labels,
        node_color=node_colors,
        width=1.5, 
        alpha=1
        )
fig.set_facecolor("#00000F")

# Add custom labels with specific font settings
nx.draw_networkx_labels(
    G, pos, labels=labels, font_size=16, font_color="black",
    font_family="STIXGeneral"  # Use a modern math/statistics font
)


# nx.draw_networkx_labels(G, pos, labels=labels, font_size=8, font_color="black")
# Add the title with white font color
plt.title(
    "Exercise 8 Itemset Lattice", 
    fontsize=24,  # Set the font size for the title
    color="white",  # Set the font color to white
    fontdict={'family': 'STIXGeneral'}  # Use a modern math/statistics font
)
plt.savefig("lattice.png", format="png", dpi=300, bbox_inches="tight")
plt.show()