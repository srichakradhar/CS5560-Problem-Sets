import nltk
tokens = nltk.word_tokenize("Citing high fuel prices, United Airlines said Friday it has increased fares by $6 per round trip on flights to some cities also served by lower-cost carriers. American Airlines, a unit AMR, immediately matched the move, spokesman Tim Wagner said. United, a unit of UAL, said the increase took effect Thursday night and applies to most routes where it competes against discount carriers, such as Chicago to Dallas and Atlanta and Denver to San Francisco, Los Angeles and New York.")
grammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP
NP -> NN
V -> VB
""")
grammar = nltk.data.load("grammar_ps3.cfg")
parser = nltk.ChartParser(grammar)
trees = parser.parse_all(tokens)
for tree in trees:
    print(tree)

# from nltk.corpus import treebank
# tokens = treebank.
