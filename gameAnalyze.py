from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests
#git test
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    game_info = None

    if request.method == "POST":
        game_name = request.form.get("game_name")
        game_info = get_game_info(game_name)
        return render_template("result.html", game_info=game_info)

    return render_template("index.html")

def test():
    return None

def get_game_info(game_name):
    # 게임명을 검색어로 위키피디아 페이지에 요청을 보냅니다.
    search_url = f"https://en.wikipedia.org/wiki/{game_name}"
    response = requests.get(search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 게임 정보가 있는 부분을 선택합니다.
        game_info_box = soup.find('table', {'class': 'infobox'})

        if game_info_box:
            # 게임 정보를 추출합니다.
            game_name = game_info_box.find('th').text.strip()
            developer = game_info_box.find('div', {'class': 'plainlist'}).text.strip()
            publisher = game_info_box.find_all('div', {'class': 'plainlist'})[1].text.strip()

            return {
                'name': game_name,
                'developer': developer,
                'publisher': publisher
            }
        else:
            return None
    else:
        return None

# 사용 예시
if __name__ == "__main__":
    app.run(debug=True, port=1234)
    game_name = "게임명"  # 검색할 게임명 입력
    game_info = get_game_info(game_name)
    if game_info:
        print("게임 정보:")
        print(f"게임명: {game_info['name']}")
        print(f"제작자: {game_info['developer']}")
        print(f"제작사: {game_info['publisher']}")
    else:
        print("게임 정보를 찾을 수 없습니다.")

