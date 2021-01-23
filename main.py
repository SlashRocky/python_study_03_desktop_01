import csv
import eel


def main():
    eel.init("web")
    eel.start("index.html")


@eel.expose
def search_character(csv_file_name, search_word):

    # 入力されたCSVファイル名と存在するCSVファイル名が一致する場合
    if csv_file_name == 'member.csv':
        with open('member.csv', 'r') as rewrite_csv:
            existing_members = csv.DictReader(rewrite_csv)

            existing_member_list = []
            for existing_member in existing_members:
                existing_member_list.append(existing_member['NAME'])

        # 「検索ワード欄」に入力されたキャラクターがCSVファイルに存在する場合
        if search_word in existing_member_list:
            return f'『{search_word}』はいますよ！\n'

        # 「検索ワード欄」に入力されたキャラクターがCSVファイルに存在しない場合
        else:
            print(search_word)
            with open('member.csv', 'a') as add_to_csv:
                writer = csv.DictWriter(add_to_csv, fieldnames=['NAME'])
                writer.writerow({'NAME': search_word})

            return f'『{search_word}』はいませんよ！\nなのでリストに追加しておきますね！\n'

    # 入力されたCSVファイル名と存在するCSVファイル名が一致しない場合
    else:
        return "そのCSVファイルはありません。\n別のCSVファイル名を入力してください。"


if __name__ == '__main__':
    main()