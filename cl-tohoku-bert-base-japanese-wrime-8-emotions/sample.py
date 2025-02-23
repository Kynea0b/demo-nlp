import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib
import numpy as np
import pandas as pd


from transformers import AutoTokenizer, AutoModelForSequenceClassification


# sns.set_theme(font='IPAexGothic')
# 動作確認
plt.figure(figsize=(5,1))
plt.title('日本語を表示できるかテスト')



# https://www.delftstack.com/ja/howto/numpy/numpy-softmax/
def np_softmax(x):
    f_x = np.exp(x) / np.sum(np.exp(x))
    return f_x

def analyze_emotion(text, show_fig=False, ret_prob=False):
    # 推論モードを有効か
    model.eval()

    # 入力データ変換 + 推論
    tokens = tokenizer(text, truncation=True, return_tensors="pt")
    tokens.to(model.device)
    preds = model(**tokens)
    prob = np_softmax(preds.logits.cpu().detach().numpy()[0])
    out_dict = {n: p for n, p in zip(emotion_names_jp, prob)}

    # 棒グラフを描画
    if show_fig:
        plt.figure(figsize=(8, 3))
        df = pd.DataFrame(out_dict.items(), columns=['name', 'prob'])
        sns.barplot(x='name', y='prob', data=df)
        plt.title('入力文 : ' + text, fontsize=15)
        plt.savefig("{}.png".format(text))

    if ret_prob:
        return out_dict


# Plutchikの8つの基本感情
emotion_names = ['Joy', 'Sadness', 'Anticipation', 'Surprise', 'Anger', 'Fear', 'Disgust', 'Trust']
emotion_names_jp = ['喜び', '悲しみ', '期待', '驚き', '怒り', '恐れ', '嫌悪', '信頼']  # 日本語版
num_labels = len(emotion_names)


model_name = "kynea0b/cl-tohoku-bert-base-japanese-v3-wrime-8-emotions"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


# 動作確認
import json

with open('testdata/data.json', 'r', encoding='utf-8') as f:
    json_data = f.read()


data = json.loads(json_data)

# reviews配列の各要素からtextフィールドを抽出して配列にする
review_texts = [review["text"] for review in data["result"]["reviews"]]

for index, text in enumerate(review_texts):
    # print(f"Index: {index}, Item: {text}")
    analyze_emotion(text, show_fig=True)




