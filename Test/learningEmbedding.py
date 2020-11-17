"""
@Time: 2020/11/13 15:44
@version: ,
@author: ,
@description: 
"""

from gensim.models import word2vec

def learn():
    filename = "test.txt"
    sentences = word2vec.LineSentence(filename)
    model = word2vec.Word2Vec(sentences, size=128, window=10, min_count=0, sg=1, workers=8, iter=2)
    model.save('text.model')  # 模型可保存
    return model