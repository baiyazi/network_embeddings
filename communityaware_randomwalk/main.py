"""
@Time: 2020/11/17 10:51
@version: ,
@author: ,
@description: 
"""

if __name__ == '__main__':
    import CARandomWalk, learningEmbedding, SimCount
    import networkx as nx

    filename = "ca_randomwalk.txt"
    # 在图上进行随机游走，生成用于输入skip-gram的语料库
    def communityawarerw():
        G = nx.karate_club_graph()
        with open(filename, encoding="utf-8", mode="w") as f:
            for i in range(30):
                for node in G.node:
                    # 暂定随机游走的窗口长度为6，游走阈值为0.2，且所有节点在一个社区中
                    resu = CARandomWalk.RandomWalk(G, node, G.nodes, 6, 0.2).walk()
                    for node in resu:
                        f.write(str(node) + " ")
                    f.write("\n")

    communityawarerw()

    modelname = "ca_randomwalk.model"
    model = learningEmbedding.learn(filename, modelname)

    resu = SimCount.getSimilaryByMostKSimilary(model, k=6)
    print(resu)
