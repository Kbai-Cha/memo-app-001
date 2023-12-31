# memo-app-001
FastapiとFlutterでメモ帳アプリを作成

## 環境構築
### （初回）作成
miniconda（ターミナル上でのconda環境）
```
cd ~
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh
```

condaが使えるか確認
```
source ~/.bashrc
```

condaのchannel設定
```
conda config --add channels conda-forge
conda config --remove channels defaults
```
※ conda-forgeとはgithub上でコミュニティが主体になって管理しているパッケージコレクション。<br>
pipみたいなもの。

conda アップデート
```
conda update conda
conda update --all
```

作成済みの仮想環境を一覧表示. baseしかないのが生
```
conda info -e
```

仮想環境を作成
```
cd backend
conda env create -f env.yaml
```

### 環境切替
```
conda activate fastapi
```

### 環境終了
```
conda deactivate
```

### サーバー起動
main: メインファイル
app: ```app = FastAPI()```のようにFastAPI()で生成されたオブジェクト
--reload: コードが変更されるたびリロードされる
```
uvicorn main:app --reload
```

### FastAPIについて
## 特徴
Pythonに型定義の概念を取り入れたWebフレームワーク。Flask同様に非常に軽量かつ高速で動作することが特徴。<br>
特に非同期処理に対して高いパフォーマンスを出すことを目的として設計されている。<br>
API開発に特化していて、作成したAPIについて自動でドキュメントを作成する機能も存在する。<br>
```http://127.0.0.1:8000/docs```にアクセスすることで、アプリに実装されているAPIについて知ることができる。<br>
エンドポイントやリクエストメソッド（GETやPOSTなど）の確認の他、パラメータやリクエストボディを記載して動作のテストを行うこともできる。<br>
代替ドキュメントとして```http://127.0.0.1:8000/redoc```にアクセスしてもよい。開発者向けにはdocsを使い、エンドユーザー向けにはredocを提供するのが一般的。
