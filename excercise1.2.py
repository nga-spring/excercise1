
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# ２．１に追加して結果が存在しなかった場合に、キャラクターリスト(source)に追加できるようにしてみましょう
# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    while True:
        word =input("鬼滅の登場人物の名前を入力してください >>> ")
        
        ### ここに検索ロジックを書く
        if word in source:
            print(f"{word}が見つかりました")
            
        else:
            print(f"{word}は存在しません")
            source.append(word)
            print(source)
        
        ans = input("終了しますか？ yesかnoを記入して下さい。")
        
        if ans == "yes":
            break   
        
if __name__ == "__main__":
    search()
