# utrustfa

青島又上企業服務有限公司官網專案，基於 Django 的企業形象網站。

## 技術棧

- **後端**: Django 5.x
- **資料庫**: SQLite（開發）/ PostgreSQL（可選，生產環境）
- **前端**: HTML、Tailwind CSS、Font Awesome
- **部署**: Gunicorn

## 環境需求

- Python 3.10+
- （可選）PostgreSQL，用於正式環境

## 安裝與設定

### 1. 建立虛擬環境並安裝依賴

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 環境變數

複製範例檔並依需求修改：

```bash
cp .env.example .env
```

| 變數 | 說明 | 預設 |
|------|------|------|
| `DJANGO_SECRET_KEY` | Django 密鑰 | 需自行設定（正式環境務必更換） |
| `DJANGO_DEBUG` | 除錯模式 | `True` |
| `ALLOWED_HOSTS` | 允許的主機 | `localhost,127.0.0.1` |
| `POSTGRES_DB` | PostgreSQL 資料庫名稱 | `utrustfa` |
| `POSTGRES_USER` | PostgreSQL 使用者 | `postgres` |
| `POSTGRES_PASSWORD` | PostgreSQL 密碼 | 不設則使用 SQLite |
| `POSTGRES_HOST` | PostgreSQL 主機 | `127.0.0.1` |
| `POSTGRES_PORT` | PostgreSQL 埠號 | `5432` |

- **未設定 `POSTGRES_PASSWORD`**：使用 SQLite（`db.sqlite3`），適合本地開發。
- **有設定 `POSTGRES_PASSWORD`**：使用 PostgreSQL，適合正式或團隊環境。

### 3. 資料庫遷移

```bash
python manage.py migrate
```

### 4. 收集靜態檔案（重要！）

**必須執行此步驟，否則後台管理介面會無法正常顯示樣式：**

```bash
python manage.py collectstatic --noinput
```

這會將所有靜態檔案（包括 Django 後台的 CSS/JS）收集到 `staticfiles/` 目錄。

### 5. 建立超級使用者（可選，用於後台）

```bash
python manage.py createsuperuser
```

## 執行方式

### 開發伺服器

```bash
python manage.py runserver
```

瀏覽 <http://127.0.0.1:8000/> 查看首頁，<http://127.0.0.1:8000/admin/> 進入後台。

### 正式環境（Gunicorn）

**部署前務必執行 `collectstatic`：**

```bash
python manage.py collectstatic --noinput
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

可依需求調整 `--workers`、`--bind` 等參數。

> **注意**：如果後台頁面樣式破版，通常是因為沒有執行 `collectstatic`。請確保已執行此命令。

## 專案結構（簡要）

```
utrustfa/
├── config/          # Django 專案設定（settings, urls, wsgi）
├── pages/            # 首頁等頁面 app
├── templates/        # 範本（含 pages/index.html）
├── static/           # 靜態檔（CSS、圖片等）
├── manage.py
├── requirements.txt
└── .env.example      # 環境變數範例
```

## 授權

依專案所屬單位規定使用。
