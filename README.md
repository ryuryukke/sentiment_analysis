# sentiment_analysis
This is a simple implementation of sentiment analysis for Japanese sentences using Word2Vec.

For details of this implementation, check [sentiment_analysis_report.pdf](https://github.com/ryuryukke/sentiment_analysis/blob/master/sentiment_analysis_report.pdf)

It just takes the average of the cos similarity between the vectors of each words in a sentence and emotion words(嬉しい,悲しい,...), so it would be better to input the sentence(after tokenized, put into distributed representation,...) sequentially into LSTM or something.

## References
1.「Word2Vecの使い方」https://qiita.com/kenta1984/items/93b64768494f971edf86

2.「Wikipediaダンプデータ」https://dumps.wikimedia.org/jawiki/latest/

3.「A tool for extracting plain text from Wikipedia dumps」https://github.com/attardi/wikiextractor



