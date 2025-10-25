from flask import Flask, render_template
app = Flask(__name__)

# ポートフォリオに表示するプロジェクトのサンプルデータ
projects = [
    {
        'id': 1,
        'title': '官公庁向けシステム開発',
        'description': '官公庁向けシステム開発。ビッグデータを処理してExcel帳票を作成する機能',
        'technologies': ['Java', 'Springboot'],
        'role': 'PL'
    },
    {
        'id': 2,
        'title': '官公庁向けシステム開発',
        'description': '官公庁向けシステム開発。情報基盤から取得したデータを表示する閲覧システム',
        'technologies': ['Vue', 'Java', 'Springboot', 'Groovy', 'JUnit', 'Python', 'AWS'],
        'role': 'PL'
    },
    {
        'id': 3,
        'title': 'ディスプレイオーディオ開発',
        'description': 'メーカー向けディスプレイオーディオ開発。Bluetooth、WifiSetting、CICDを担当',
        'technologies': ['Android', 'Java', 'JUnit', 'Jenkins'],
        'role': 'L'
    },
    {
        'id': 4,
        'title': '車両メーカー向けCICD環境構築',
        'description': '車両メーカー向けCICD環境構築',
        'technologies': ['JavaScript', 'Jenkins', 'JUnit'],
        'role': 'L'
    },
    {
        'id': 5,
        'title': '市販向けカーナビゲーション機能開発',
        'description': 'プローブ、Carplay/Androidautoを担当',
        'technologies': ['C++', 'CppUnit'],
        'role': 'SL'
    },
]

@app.route('/')
def index():
    # 自己紹介やプロジェクトデータをテンプレートに渡す
    # 技術名と色のマッピング
    tech_colors = {
        'java': '#F57C00',      # Deep Orange 700
        'springboot': '#388E3C',  # Green 700
        'python': '#3F51B5',    # Indigo 700
        'vue': '#00796B',       # Teal 700
        'aws': '#FFB300',       # Amber 700
        'android': '#64DD17',   # Light Green A700
        'junit': '#AFB42B',     # Lime 700
        'jenkins': '#D32F2F',   # Red 700
        'groovy': '#0288D1',    # Light Blue 700
        'javascript': '#FBC02D',# Yellow 700
        'c++': '#004D40',       # Teal 900
        'cppunit': '#4A148C',   # Purple 900
        'default': '#BDBDBD'    # Grey 400
    }

    profile = {
        'name': 'sanada_a',
        'bio': 'SE。バスケとスノーボード、キャンプが好きです。たまにロードバイク。',
        'github_url': 'https://github.com/adanas/flask_portfolio'
    }
    return render_template('index.html', profile=profile, projects=projects, tech_colors=tech_colors)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
