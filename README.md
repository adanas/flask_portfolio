# Flask Portfolio

これは Flask, Chart.js を使用して作成された、インタラクティブなポートフォリオサイトです。

![スクリーンショット](https://via.placeholder.com/800x450.png?text=Portfolio+Screenshot)
*(ここにアプリケーションのスクリーンショットを挿入してください)*

## ✨ 主な機能

- **自己紹介**: プロフィール情報と画像を表示します。
- **プロジェクト一覧**: 携わったプロジェクトをアコーディオン形式で表示します。
- **技術スタックの可視化**: Chart.js を利用して、使用技術の割合を円グラフで表示します。
- **インタラクティブなフィルタリング**:
    - 円グラフのセクションをクリックすると、関連するプロジェクトがフィルタリングされます。
    - 各プロジェクトの技術タグをクリックしても同様にフィルタリングできます。
- **画像の拡大表示**: プロフィール画像をクリックするとモーダルウィンドウで拡大表示します。

## 🛠️ 使用技術

- **バックエンド**: Python, Flask
- **フロントエンド**: HTML, CSS, JavaScript
- **ライブラリ**: Chart.js, chartjs-plugin-datalabels

## 🚀 セットアップと実行方法

1.  **リポジトリをクローンします**
    ```bash
    git clone https://github.com/adanas/flask_portfolio.git
    cd flask_portfolio
    ```

2.  **Pythonの仮想環境を作成して有効化します (推奨)**
    ```bash
    # Mac / Linux
    python3 -m venv venv
    source venv/bin/activate

    # Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **必要なライブラリをインストールします**
    `requirements.txt` ファイルを作成していない場合は、まず以下のコマンドで作成してください。
    ```bash
    pip install Flask
    pip freeze > requirements.txt
    ```
    その後、ライブラリをインストールします。
    ```bash
    pip install -r requirements.txt
    ```

4.  **アプリケーションを実行します**
    ```bash
    python app.py
    ```

5.  ブラウザで **http://127.0.0.1:5001** にアクセスしてください。
