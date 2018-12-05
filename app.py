from flask import Flask, render_template

app = Flask(__name__)
"""
書くこと
    /index にGETリクエスト が来たら
    index.html というテンプレートをレンダリングする
"""


# @ デコレート
@app.route("/search")
def search_volume():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
