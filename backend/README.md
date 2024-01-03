## バックエンド環境構築（初回）
### miniconda インストール
[minicondaの公式サイト]([https://docs.conda.io/projects/miniconda/en/latest/#latest-miniconda-installer-links)から[minicondaインストーラーをダウンロード](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)<br>
ダウンロード完了後インストーラーを起動してインストールを進めていく.<br>
基本デフォルト設定のまま次へ進んでよい. 途中でインストール先を選択する場面が現れるがデフォルトのままか自分で設定するかはお好み.<br>
次の画面のAdvanced Installation Optionsでの各項目説明については以下.<br>
個人（Kbai）的には全部チェックでよいかも.
- Create start menu shortcuts: スタートメニューにAnacondaのアイコンを作成するか
- Add Miniconda3 to my PATH environment variable: Miniconda3のパスを環境変数に追加するか&nbsp;&nbsp;※公式では非推奨になっているが、初めてAnacondaをインストールするならばチェックしてもよい。
- Register Miniconda3 as my default Python 3.11: condaで環境を作成するときにデフォルトだとPython=3.11で作成するか
- Clear the package cache upon completion: インストール完了時にインストーラパッケージのキャッシュを削除するか
インストールが完了したらPower Shellを起動して```conda --version```でMinicondaがインストールされていることを確認.
```conda XX.YY.ZZ```のように出力されていればインストール成功.

### condaのchannel設定
```
conda config --add channels conda-forge
conda config --remove channels defaults
```

### conda アップデート
```
conda update conda
conda update --all
```

### VSCodeからAnaconda Promptを開けるようにする
(もし面倒だったらAnaconda PromptとVSCodeの2窓体制でもあり)
1. スタート画面から```Anaconda Prompt```を検索. Anaconda Promptが出るはずなので右クリックした後```ファイルの場所を開く```を選択
2. さらに```Anaconda Prompt (Miniconda3)```を右クリックして```ファイルの場所を開く```を選択
3. フォルダの中に```cmd.exe```があるはずなので右クリックして```パスのコピー```でファイルパスをコピーする.&nbsp;&nbsp;※この後使用するのでどこかでメモしておく
4. VSCodeから```Ctrl + ,(カンマ)```を押して設定画面を開いた後```terminal.integrated.profiles.windows```で検索する
5. 中に```settings.jsonで編集く```をクリックして```settings.json```を開く
6. ファイルの中に```terminal.integrated.profiles.windows```を以下の形に修正
```
{
    (既存の設定),
    ...,
    "terminal.integrated.profiles windows": {
        (既存の設定)
        ...,
        "Anaconda Prompt": {
            "path": <3.でコピーしたパス  ※ ダブルクォーテーション（""）で囲む>
        }
    }
}
```
7. ターミナルを起動（```Ctrl + Shift + @```）した後、ターミナル右上の＋の左にあるボタンから```Anaconda Prompt```を選択
8. ```conda activate memoapp```から仮想環境起動できることを確認する

### 新規環境の作成
env.yamlがある場合
```
conda env create -f environment_be.yml
```
env.yamlがない場合
```
conda create -n memoapp python=3.12.1
```

### VSCodeにインタープリターを設定
あらかじめ```conda info -e```で仮想環境のパスを確認すること.<br>
VSCodeで```Ctrl + Shift + P```でコマンドパレットを表示.<br>
```Python: Select Interpreter```を選択後```インタープリターパスを入力```を選択.<br>
```検索```を選択するとファイル選択ダイアログが開かれるので先ほど調べた仮想環境のパスで検索.<br>
フォルダの中に```pytyon.exe```があるので選択.<br>再度コマンドパレットからインタープリター選択画面を開き、先ほど追加したパスを選択

## パッケージのインストールとyaml出力
インストールの基本形. バージョンを指定しなければインストール可能な中で最新版がインストールされる.
```
conda install <package-name>[==version] -n <env_name>
```

envをyamlに出力. Power Shellからmemo-app-001/backend 配下で行う
```
conda env export -n memoapp | `
ForEach-Object { $_ -replace '^\s*prefix:.*', '' } | `
Select-Object -SkipLast 1 | `
Out-File -FilePath environment_be.yml -Encoding UTF8
```

## 普段使いするコマンド
### ローカルサーバー起動
```backend```に移動.<br>
```uvicorn backend.main:app --reload```

### モデルに変更をしたときの動き
1. モデルを変更
2. マイグレーションファイル作成
    - ```backend/migrations```に移動
    - ```alembic revision --autogenerate -m "comment"```
3. マイグレーションのアップグレードを反映
    - ```backend/migrations```に移動
    - ```alembic upgrade head```
    - もし未反映のマイグレーションファイルが複数あり、途中までしか反映させたくない場合<br>
    ```alembic upgrade +N```<br>
    N回分進める
4. マイグレーションのアップグレードを反映
    - ```backend/migrations```に移動
    - ```alembic downgrade head```
    - もし複数戻りたい場合<br>
    ```alembic downgrade -N```<br>
    N回分戻る

## ディレクトリ構成説明
■ models<br>
データベースに登録されるテーブルを定義するモジュール

■ src/crud<br>
実際にデータベースの操作を行うモジュール

■ src/routers<br>
各エンドポイントの処理を定義するモジュール

■ src/schemas<br>
APIのリクエストやレスポンスの型を定義するモジュール

■ src/services<br>
データの操作以外の処理を行うモジュール（単純な計算など）
