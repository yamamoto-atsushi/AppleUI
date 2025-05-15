# PyQt6 向け Apple 風 UI コンポーネント

このプロジェクトは、Apple のユーザーインターフェース要素のルックアンドフィールを模倣するように設計された、カスタム PyQt6 ウィジェットのセットを提供します。以下のコンポーネントが含まれています：

*   **`AppleStyleWindow`**: テーマサポート（ライト/ダーク）とスクロール可能なコンテンツエリアを備えたメインウィンドウ。
*   **`AppleStyleLabel`**: カスタマイズ可能なフォントサイズとスタイル（プライマリ/セカンダリ）を持つテキストラベル。
*   **`AppleStyleLineEdit`**: バリデーション状態（エラーハイライト）を持つ一行テキスト入力フィールド。
*   **`AppleStyleTextEdit`**: 複数行テキスト入力エリア。
*   **`AppleStyleButton`**: ホバーおよびプレスアニメーションと、テーマ対応のスタイリングが施されたプッシュボタン。
*   **`AppleStyleCheckBox`**: カスタムのチェックマーク描画を行うチェックボックス。
*   **`AppleStyleSwitch`**: スライドするハンドルアニメーション付きのトグルスイッチ。
*   **`AppleStyleSlider`**: 水平および垂直スライダー。
*   **`AppleStyleRadioButton`**: ラジオボタン。
*   **`AppleStyleComboBox`**: ドロップダウンメニュー（コンボボックス）。
*   **`AppleStyleDateEdit`**: カレンダーポップアップ付きの日付選択入力。
*   **`AppleStyleProgressBar`**: プログレスバー。

これらのコンポーネントは、Apple のデザイン言語との視覚的な一貫性を目指しており、あなたの PyQt6 アプリケーションで簡単に再利用できます。使用例については `comprehensive_sample_app.py` を参照してください。

## 使用方法

### 1. 準備

#### PyQt6 のインストール

まず、PyQt6 がインストールされている必要があります。インストールされていない場合は、ターミナルまたはコマンドプロンプトで以下のコマンドを実行してください。

```bash
pip install PyQt6
```

#### `apple_style_ui.py` の配置

`apple_style_ui.py` ファイルを、あなたの Python プロジェクトのディレクトリ（メインのスクリプトと同じ場所など、Python がインポートできる場所）に配置します。

### 2. コンポーネントのインポート

Python スクリプト内で、必要なコンポーネントを `apple_style_ui` モジュールからインポートします。

```python
import sys
from PyQt6.QtWidgets import QApplication # QApplication は常に必要
# apple_style_ui から必要なコンポーネントをインポート
from apple_style_ui import (
    AppleStyleWindow,
    AppleStyleLabel,
    AppleStyleLineEdit,
    AppleStyleTextEdit,
    AppleStyleButton,
    AppleStyleCheckBox,
    AppleStyleSwitch,
    AppleStyleSlider,
    AppleStyleRadioButton,
    AppleStyleComboBox,
    AppleStyleDateEdit,
    AppleStyleProgressBar,
    get_color # テーマカラーを取得する関数 (必要に応じて)
)
# その他の PyQt6 モジュール (必要に応じて)
from PyQt6.QtCore import Qt, QDate
```

### 3. 基本的なウィンドウの作成

`AppleStyleWindow` を使用して、アプリケーションのメインウィンドウを作成します。

```python
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # QSettings のために推奨される設定
    QApplication.setOrganizationName("YourCompanyName")
    QApplication.setApplicationName("YourAppName")

    main_window = AppleStyleWindow("My Apple-Style Application")
    
    # ここにウィジェットを追加していきます
    #例: main_window.addContentWidget(AppleStyleLabel("Hello World!"))

    main_window.show()
    sys.exit(app.exec())
```

### 4. 各コンポーネントの使用例

以下は、主要なコンポーネントの簡単な使用例です。これらのウィジェットを `AppleStyleWindow` の `addContentWidget()` メソッドを使って追加していきます。

#### `AppleStyleLabel`
テキストラベルを表示します。
```python
info_label = AppleStyleLabel("This is some information.")
main_window.addContentWidget(info_label)
```

#### `AppleStyleLineEdit`
一行のテキスト入力フィールドです。
```python
name_input = AppleStyleLineEdit()
name_input.setPlaceholderText("Enter your full name")
main_window.addContentWidget(name_input)
```

#### `AppleStyleButton`
クリック可能なボタンです。
```python
def my_button_action():
    print("Button clicked!")
action_button = AppleStyleButton("Perform Action")
action_button.clicked.connect(my_button_action)
main_window.addContentWidget(action_button)
```

*(その他のコンポーネントの使用例は `comprehensive_sample_app.py` を参照してください。)*

### 5. その他の機能

#### テーマの切り替え
`AppleStyleWindow` はライトモードとダークモードの切り替えをサポートしています。
```python
main_window.set_theme("dark") # ダークモードに設定
```
テーマ設定は `QSettings` を使って保存・読み込みされます。

#### メッセージ表示
ウィンドウ下部に一時的なメッセージを表示できます。
```python
main_window.show_message("Operation successful!", duration_ms=3000)
```

#### ツールチップ
各ウィジェットに `setToolTip("説明文")` でツールチップを設定できます。

#### キーボードショートカット
`QShortcut` を使ってアクションにショートカットを割り当てることができます。

### 6. レイアウト

ウィジェットは `AppleStyleWindow` の内部レイアウト (`QVBoxLayout`) に `addContentWidget()` で追加されます。最後に `main_window.addStretch()` を呼び出すと、コンテンツが上部に寄ります。
複雑なレイアウトのためには、`QWidget` と `QHBoxLayout` や `QVBoxLayout` などを組み合わせてコンテナウィジェットを作成し、それを `addContentWidget()` で追加します。

---

このガイドが `apple_style_ui.py` を使用する際の一助となれば幸いです。

---

**English version:** README.md