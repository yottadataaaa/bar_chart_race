
特定フォーマットのcsvを入力すると、bar_chart_race形式の動画を出力するためのプログラムです。

## 実行方法

このレポジトリのホームディレクトリ配下で以下コマンドを実施してください。
以下に記載の前提準備も必須です。

```sh
$ python main.py \
    --csv_path {input/input.csv} \
    --value_column {"value"} \
    --id_column {"name"} \
    --time_column {"date"}
```

サポートしているpythonバージョンは `3.11.10` です。

実行時引数は以下です。

|#|引数名|型|必須|内容|
|:--:|:--:|:--:|:--:|:--:|
|1|`--csv_path`|str|◯|入力CSVファイルのパス|
|2|`--value_column`|str|◯|値として使う列名（バーの長さ）|
|3|`--id_column`|str|◯|各バーの名前・IDに使う列名|
|4|`--time_column`|str|◯|時系列のキー（日付や年）|
|5|`--image_map_path`|str|✕|各バーに対応する画像ファイルパスを指定したJSONファイル|
|6|`--color_map_path`|str|✕|各バーに対応する色を指定したJSONファイル|
|7|`--width`|str|✕|動画の幅（デフォルト：1920）|
|8|`--height`|str|✕|動画の高さ（デフォルト：1080）|
|9|`--fps`|str|✕|フレームレート（デフォルト：30）|
|10|`--duration`|str|✕|動画全体の秒数（デフォルト：無制限）|
|11|`--n_bars`|str|✕|表示する最大バー数（デフォルト：10）|
|12|`--interpolate`|str|✕|値が欠損しているときに線形補間するか（デフォルト：false）|
|13|`--output`|str|✕|書き出す動画ファイルパス（デフォルト：output.mp4）|
|14|`--font_path`|str|✕|カスタムフォントを指定したい場合（デフォルト：システムフォント）|


# 開発向け

## ディレクトリルール

- `scenes/`: 各種シーン（クラス）をまとめる
- `assets/`: 外部素材（画像・音声・フォントなど）を管理
- `styles/`: 色やフォント、テーマ設定を集中管理（`config.py`など）
- `utils/`: 共通描画処理やカスタムコンポーネント（例：ラベル、軸など）
- `output/`: Manim実行時に自動生成される動画フォルダ
- `manim.cfg`: 解像度、fps、背景色などプロジェクト設定。CLI指定も可能
- `main.py`: 実行エントリーポイント

