import eel
import desktop
import search

app_name = "web"
end_point = "index.html"
size = (500, 500)


@eel.expose
def search_character(csv_file_name, search_word):
    return search.search_character(csv_file_name, search_word)


desktop.start(app_name, end_point, size)
# desktop.start(size=size,appName=app_name,endPoint=end_point)
