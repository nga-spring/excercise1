
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# ３．２に追加してキャラクターリスト(source)をCSVから読み込んで登録できるようにしてみましょう
# 検索ソース

PATH = "source.csv"

### 検索ツール
def read_source():
    with open(PATH,encoding='utf-8-sig') as f:
        # readlinesでファイルを読み込みリスト化し、リスト内包表記を使用し各要素でstrip()を使用し改行コードを削除する
        l =[s.strip() for s in f.readlines()]
        return l
       
def search():
    source = read_source()
    while True:
        word =input("鬼滅の登場人物の名前を入力してください >>> ")
        
        ### ここに検索ロジックを書く
        if word in source:
            print(f"{word}が見つかりました")
            
        else:
            print(f"{word}は存在しません")
            ans = input("終了しますか？yesかnoを記入してください。>>>")
            if ans =="yes":
                break
        
if __name__ == "__main__":
    search()