import MeCab
from gensim.models import word2vec
import numpy as np

mecab = MeCab.Tagger("")
mecab.parse("")
model = word2vec.Word2Vec.load("./wiki.model")

def text_senti(text):
    senti = []
    node = mecab.parseToNode(text)
    while node:
        hinshi = node.feature.split(",")[0]
        if hinshi == '名詞' or hinshi == '動詞' or hinshi == '形容詞':
            res = list(map(model.wv.similarity, [node.surface]*6, ["嬉しい", "怒り", "悲しみ", "興奮", "恐怖", "安心"]))
            senti.append(res)
        node = node.next
    return senti

def main():
    print("文章を入れてください")
    sentence = input()
    senti_map = text_senti(sentence)
    senti_map = np.array(senti_map)
    mean_senti = np.mean(senti_map, axis=0)
    print(f"喜び:{mean_senti[0]}")
    print(f"怒り:{mean_senti[1]}")
    print(f"悲しみ:{mean_senti[2]}")
    print(f"興奮:{mean_senti[3]}")
    print(f"恐怖:{mean_senti[4]}")
    print(f"安心:{mean_senti[5]}")

if __name__ == "__main__":
    main()
