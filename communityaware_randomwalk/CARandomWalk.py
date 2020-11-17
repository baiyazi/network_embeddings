"""
@Time: 2020/11/17 10:46
@version: ,
@author: ,
@description:  Community aware random walk for network embedding
"""


import random

class RandomWalk(object):
    def __init__(self, G, v, Com, l, alpha):
        """
        初始化参数
        :param G:  图数据，类型为 nx.Graph()
        :param v:  当前游走的起点
        :param Com: 节点v所在的社区列表  list
        :param l: 随机游走的长度
        :param alpha: 随机阈值变量
        """
        self.G = G
        self.v = v
        self.Com = Com
        self.l = l
        self.alpha = alpha

    def initialize(self):
        """
        初始随机游走的路径存储列表，并将当前节点存入该列表中
        initialize RW with v
        """
        self.RW = [self.v]

    def hasNeighbor(self, currentNode):
        """
        判断currentNode在图中是否有未访问过的邻居节点
        :param currentNode: 需要判断的节点
        :return: 未访问过的邻居列表
        """
        all_neighbors = list(self.G.neighbors(currentNode))
        not_visited_neighbors = []
        for node in all_neighbors:
            # 判断一下邻居节点是否已经在游走的路径上
            if(node not in self.RW):
                not_visited_neighbors.append(node)
        return not_visited_neighbors

    def randomSelectFromCom(self):
        # 从当前社区中随机选择一个节点
        available_nodes = []
        for node in self.Com:
            if (node not in self.RW):
                available_nodes.append(node)
        return available_nodes[int(random.random() * len(available_nodes))]

    def walk(self):
        self.initialize()
        dont_visited_node = []
        while len(self.RW) < self.l:
            currentNode = self.RW[len(self.RW) - 1]
            neighbors = self.hasNeighbor(currentNode)
            if len(neighbors) > 0:
                if(random.random() < self.alpha):
                    # select vj at random from vi's neighbors
                    node = neighbors[int(random.random() * len(neighbors))]
                else:
                    # select vj at random from members of vi's communities
                    node = self.randomSelectFromCom()

                if node not in dont_visited_node:
                    self.RW.append(node)
            else:
                # backtrack in the path and select the last node which has neighbors that are not in the path
                # 回溯到上一个节点，再进行判断
                if len(self.RW) > 1:
                    self.RW.remove(self.RW[len(self.RW) - 1])
                    dont_visited_node.append(self.RW[len(self.RW) - 1])

        # 返回路径
        return self.RW
