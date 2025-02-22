# models

## ベースのモデル

### About Dataset

CC-100: 74.3GB
Wikipedia: 4.9GB

tokenize tool:fugashi,mecab-ipadic-NEologd

参考;
[BERT base Japanese (unidic-lite with whole word masking, CC-100 and jawiki-20230102)](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3)

## 追加学習用のデータセット

> Ver.1: 80人の筆者から収集した43,200件の投稿に感情強度をラベル付けしました。
https://github.com/ids-cv/wrime

## 出来上がりモデル

Model repository
[model](https://huggingface.co/kynea0b/cl-tohoku-bert-base-japanese-v3-wrime-8-emotions)

### 入力例

「ピクミンのチョコエッグ売ってるコンビニ見つけた」
「普通のデイリーヤマザキなのですが、ここ和歌山中之島店は、程近くに地蔵の辻と言う場所があります。辻。。つまり交差点にお地蔵様が見守っておられます(現在は道路拡張工事の為にお地蔵様は少し移設)。その地蔵の辻にちなんだお地蔵様あんぱんがここ中之島店限定で販売されております。つぶあんと、そしてホイップクリームをサンドしたオリジナルあんぱんは美味しさ満点！お地蔵様と言う事で縁起物としてプレゼントされる方も多いそうですよ( ´▽｀)普通のコンビニとは少し違う、このオリジナルあんぱんを是非食べて下さいね♪」

## 追加実験

今後試したいデータセットたち or 追加学習したい
https://zenn.dev/panyoriokome/scraps/bb96bd0e512124
