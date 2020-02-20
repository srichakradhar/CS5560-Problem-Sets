from openie import StanfordOpenIE

with StanfordOpenIE() as client:
    # text = 'Barack Obama was born in Hawaii. Richard Manning wrote this sentence.'
    corpus = "Citing high fuel prices, United Airlines said Friday it has increased fares by $6 per round trip on flights to some cities also served by lower-cost carriers. American Airlines, a unit AMR, immediately matched the move, spokesman Tim Wagner said. United, a unit of UAL, said the increase took effect Thursday night and applies to most routes where it competes against discount carriers, such as Chicago to Dallas and Atlanta and Denver to San Francisco, Los Angeles and New York."

    # with open('corpus/pg6130.txt', 'r', encoding='utf8') as r:
    #     corpus = r.read().replace('\n', ' ').replace('\r', '')

    triples_corpus = client.annotate(corpus)
    print('Corpus: %s [...].' % corpus[0:80])
    print('Found %s triples in the corpus.' % len(triples_corpus))
    for triple in triples_corpus[:3]:
        print('|-', triple)
    print('Text: %s.' % corpus)
    for triple in client.annotate(corpus):
        print('|-', triple)
    graph_image = 'graph.png'
    client.generate_graphviz_graph(corpus, graph_image)
    print('Graph generated: %s.' % graph_image)
