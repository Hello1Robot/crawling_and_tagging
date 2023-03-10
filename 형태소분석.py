# --------------------- 형태소 분석파트 시작 ---------------------- #
import sys
sys.path.insert(0, '../')
from soynlp.noun import LRNounExtractor
from soynlp.utils import DoublespaceLineCorpus

noun_extractor = LRNounExtractor(
    max_left_length=10, 
    max_right_length=7,
    predictor_fnames=None,
    verbose=True
)

corpus_fname = 'processed_wiki_ko.txt'
sentences = DoublespaceLineCorpus(corpus_fname, iter_sent=True)
print(len(sentences)) # 311237
print('success')
nouns = noun_extractor.train_extract(
    sentences,
    min_noun_score=0.3,
    min_noun_frequency=20
)

print("## 뉴스 단어 분석 ##")
print(nouns['뉴스'])

top100 = sorted(nouns.items(), 
    key=lambda x:-x[1].frequency)[:100]

for i, (word, score) in enumerate(top100):
    if i % 5 == 0:
        print()
    print('%6s (%.2f)' % (word, score.score), end='')

top100 = sorted(nouns.items(), 
    key=lambda x:-x[1].frequency * x[1].score)[:100]

for i, (word, score) in enumerate(top100):
    if i % 5 == 0:
        print()
    print('%6s (%.2f)' % (word, score.score), end='')


# # NewsNounExtractor 버전
# print('# NewsNounExtractor 버전 테스트 시작')
# from soynlp.noun import NewsNounExtractor

# noun_extractor = NewsNounExtractor(
#     max_left_length=10, 
#     max_right_length=7,
#     predictor_fnames=None,
#     verbose=True
# )

# nouns = noun_extractor.train_extract(sentences)

# top100 = sorted(nouns.items(), 
#     key=lambda x:-x[1].frequency)[:100]

# for i, (word, score) in enumerate(top100):
#     if i % 5 == 0:
#         print()
#     print('%6s (%.2f)' % (word, score.score), end='')

# top100 = sorted(nouns.items(), 
#     key=lambda x:-x[1].frequency * x[1].score)[:100]

# for i, (word, score) in enumerate(top100):
#     if i % 5 == 0:
#         print()
#     print('%6s (%.2f)' % (word, score.score), end='')

# v2 테스트
print('v2 test start -------------------')
from soynlp.noun import LRNounExtractor_v2
corpus_path = 'processed_wiki_ko'
sents = DoublespaceLineCorpus(corpus_path, iter_sent=True)

noun_extractor = LRNounExtractor_v2(verbose=True)
nouns = noun_extractor.train_extract(sents)
# 추출된 단어 확인
print("추출된 단어 중 5가지 : "+list(noun_extractor._compounds_components.items())[:5])

