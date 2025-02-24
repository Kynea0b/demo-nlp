# models

## ベースのモデル

CC-100: 74.3GB
Wikipedia: 4.9GB

tokenize tool:fugashi,mecab-ipadic-NEologd

参考;
[BERT base Japanese (unidic-lite with whole word masking, CC-100 and jawiki-20230102)](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3)

## 追加学習用のデータセット

テキストデータに対して、読んだ人の感想を8つの感情ごとに1~3点で評価済みのデータを教師ラベルとして追加学習に使用。

> Ver.1: 80人の筆者から収集した43,200件の投稿に感情強度をラベル付けしました。

- [ids-cv/wrime repository](https://github.com/ids-cv/wrime)
- [wrime-ver1.tsvの中身](https://raw.githubusercontent.com/ids-cv/wrime/refs/heads/master/wrime-ver1.tsv)

テキスト分類用のデータセット

### データセット詳細

各行が1つの文章（Sentence）に対応しており、その文章に対して書き手（Writer）および複数の読者（Reader1, Reader2, Reader3）が感情を評価しています。 

#### **各カラムの意味** 

1. **Sentence**: 評価対象の文章
2. **UserID**: 文章を書いたユーザーのID
3. **Datetime**: 文章が投稿された日時
4. **Train/Dev/Test**: データの分割（学習用(train)・開発用(dev)・テスト用(test)）
5. **Writer_*（例：Writer_Joy）**: - 文章を書いた人（Writer）が感じた感情 - それぞれの感情に対して数値が入っており、強さを表している（例: 0 = 無し, 1 = 弱い, 2 = 強い）
6. **ReaderN_*（例：Reader1_Joy, Reader2_Sadness）**: - 読者（Reader1, Reader2, Reader3）がその文章から感じた感情 - Writerと同じく、感情の強さを数値で表している
7. **Avg. Readers_*（例：Avg. Readers_Joy）**: - 3人の読者の評価の平均値 ---

#### **データの具体例** 

8項目について、１点から３点で評価。
- Joy
- Sadness
- Anticipation
- Surprise
- Anger
- Fear
- Disgust
- Trust

データ例。

| 項目 | 値 | 
|------|----| 
| Sentence | ぼけっとしてたらこんな時間｡チャリあるから食べにでたいのに… | 
| UserID | 1 | 
| Datetime | 2012/07/31 23:48 | 
| Train/Dev/Test | train | 
| Writer_Sadness | 1（書き手は少し悲しさを感じている） | 
| Writer_Anticipation | 2（書き手は強く期待感を持っている） | 
| Writer_Surprise | 1（少し驚いている） | 
| Writer_Anger | 1（少し怒りを感じている） | 
| Reader1_Sadness | 2（読者1は強く悲しみを感じた） | 
| Reader2_Sadness | 2（読者2も強く悲しみを感じた） | 
| Reader3_Sadness | 2（読者3も強く悲しみを感じた） | 
| Avg. Readers_Sadness | 2.0（読者全員が強い悲しみを感じた） | 

この例では、書き手自身は「期待感（Anticipation）」を強く持っているものの、読者たちは「悲しみ（Sadness）」を強く感じたという違いがあるのがわかります。 --- 

#### **データの活用方法** 
- **感情分類モデルの学習**:
  - `Sentence` を入力として、読者の感情ラベル（Avg. Readers_*）を教師ラベルとしてモデルを訓練できる
- **書き手と読者の感情の違いの分析**:
  - 書き手が意図した感情と読者が受け取った感情が異なる場合、どのような文章でギャップが生まれるのか分析できる
- **感情の可視化**:
  - `Avg. Readers_*` の値を棒グラフやヒートマップで可視化すると、文章ごとの感情の傾向がわかりやすくなる 


## 出来上がりモデル

Model repository
[model](https://huggingface.co/kynea0b/cl-tohoku-bert-base-japanese-v3-wrime-8-emotions)

### 入力例

Google Maps APIで試してみると快不快がはっきりしているので分類はちゃんとできてそう。

- [8-emotions.ipynb](https://github.com/Kynea0b/demo-nlp/blob/main/cl-tohoku-bert-base-japanese-wrime-8-emotions/8-emotions.ipynb)


「普通のデイリーヤマザキなのですが、ここ和歌山中之島店は、程近くに地蔵の辻と言う場所があります。辻。。つまり交差点にお地蔵様が見守っておられます(現在は道路拡張工事の為にお地蔵様は少し移設)。その地蔵の辻にちなんだお地蔵様あんぱんがここ中之島店限定で販売されております。つぶあんと、そしてホイップクリームをサンドしたオリジナルあんぱんは美味しさ満点！お地蔵様と言う事で縁起物としてプレゼントされる方も多いそうですよ( ´▽｀)普通のコンビニとは少し違う、このオリジナルあんぱんを是非食べて下さいね♪」
