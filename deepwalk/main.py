"""
@Time: 2020/11/13 15:50
@version: ,
@author: ,
@description: 
"""

import getCropu
import networkx as nx

if __name__ == '__main__':
    g = nx.karate_club_graph()
    path_length = 12
    alpha = 0.2
    # 生成路径
    walks = []
    for node in g.nodes:
        path = getCropu.getPath(node, g, path_length, alpha)
        walks.append(path)
    # 保存路径
    import savePath

    savePath.save_path(walks)
    # 学习嵌入
    import learningEmbedding as learn

    model = learn.learn()
    # 统计
    import SimCount

    resu = SimCount.getSimilaryByMostKSimilary(model, k=10)
    print(resu)