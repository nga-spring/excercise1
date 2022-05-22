
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# ４．３に追加してキャラクターリスト(source)をCSVに書き込めるようにしてみましょう
# 検索ソース

PATH = "source.csv"

### 検索ツール
def read_source():
    with open(PATH,encoding='utf-8-sig') as f:
        # readlinesでファイルを読み込みリスト化し、リスト内包表記を使用し各要素でstrip()を使用し改行コードを削除する
        l =[s.strip() for s in f.readlines()]
        return l
    
def write_source(word):
    # modeを'a'にして追記する。改行コード('\n')を加えて末尾に追加する
    with open(PATH, mode='a',encoding='utf-8-sig') as f:
        f.write('\n'+ word)
       
def search():
    source_list = read_source()
    while True:
        word =input("鬼滅の登場人物の名前を入力してください >>> ")
        
        ### ここに検索ロジックを書く
        if word in source_list:
            print(f"{word}が見つかりました")
            
        else:
            print(f"{word}は存在しません")
            write_source(word)
            ans = input("終了しますか？yesかnoを記入してください。>>>")
            if ans =="yes":
                break
        
if __name__ == "__main__":
    search()