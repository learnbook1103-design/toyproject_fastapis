```
{
  "project_name": "toyproject_fastapis",
  "task": "FastAPI 공지사항 CRUD 기능 구현 및 PostgreSQL 연동 파일 생성/수정 (기존 로직 유지)",
  "action": "CREATE_OR_MODIFY_FILES",
  "files": [
    {
      "file_path": "main.py",
      "action_type": "ADD_OR_APPEND_CONTENT",
      "purpose": "기존 main.py의 내용을 유지하며 PostgreSQL 연동을 위한 임포트, 템플릿 설정, 공지사항 CRUD 라우트를 추가합니다.",
      "modifications": [
        "**파일 상단 (임포트 영역):** 'from db import get_db_connection', 'from models import Notice, NoticeCreate', 'from fastapi.templating import Jinja2Templates' 등의 필요한 임포트를 추가.",
        "**FastAPI 앱 초기화 직후:** Jinja2Templates 설정 ('templates = Jinja2Templates(directory='templates')')을 추가.",
        "**파일 하단:** PostgreSQL 연동 기반의 다음 5가지 라우트 함수를 추가합니다:",
        "1. **CREATE (POST /notices/):** DB INSERT 쿼리 실행",
        "2. **READ All (GET /notices/):** DB SELECT 쿼리 실행 (API용)",
        "3. **READ One (GET /notices/{notice_id}):** DB SELECT 쿼리 실행 (API용)",
        "4. **UPDATE (PUT /notices/{notice_id}):** DB UPDATE 쿼리 실행",
        "5. **DELETE (DELETE /notices/{notice_id}):** DB DELETE 쿼리 실행",
        "6. **Web View (GET /notices_web/):** DB SELECT 쿼리 실행 후 'notices.html' 템플릿 렌더링"
      ],
      "required_imports": ["from db import get_db_connection", "from fastapi import HTTPException, status, Request", "from fastapi.templating import Jinja2Templates", "from typing import List", "from models import Notice, NoticeCreate"]
    },
    {
      "file_path": "db.py",
      "action_type": "CREATE",
      "purpose": "PostgreSQL 연결 함수 정의",
      "content_details": {
        "description": "psycopg2를 사용하여 DB 연결을 수행하며, 환경 변수 대신 지정된 하드코딩된 값 사용.",
        "requirements": [
          "psycopg2 임포트",
          "DB_HOST: 'db_postgresql', DB_PORT: '5432', POSTGRES_DB: 'main_db', POSTGRES_USER: 'admin', POSTGRES_PASSWORD: 'admin123' 사용",
          "get_db_connection() 함수 정의"
        ]
      }
    },
    {
      "file_path": "init.sql",
      "action_type": "CREATE",
      "purpose": "PostgreSQL 테이블 생성 스크립트",
      "content_details": {
        "description": "'notices' 테이블 생성 SQL 구문 포함",
        "requirements": [
          "CREATE TABLE notices",
          "컬럼: id (SERIAL PRIMARY KEY), title (VARCHAR), content (TEXT), created_at (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        ]
      }
    },
    {
      "file_path": "templates/notices.html",
      "action_type": "CREATE",
      "purpose": "공지 사항 목록을 표시하는 웹 페이지 템플릿",
      "content_details": {
        "description": "Jinja2 템플릿 구문을 사용하여 DB에서 전달받은 공지 사항 목록을 출력",
        "requirements": [
          "HTML5 구조",
          "공지 사항 목록(notices)을 순회하는 Jinja2 루프",
          "각 공지 사항의 title, content, id 표시"
        ]
      }
    },
    {
      "file_path": "requirements.txt",
      "action_type": "MODIFY",
      "purpose": "필요한 라이브러리 추가",
      "modifications": [
        "fastapi",
        "uvicorn[standard]",
        "jinja2",
        "psycopg2-binary" // PostgreSQL 연결 드라이버 추가
      ]
    }
  ],
  "next_step_cli": [
    "pip install -r requirements.txt",
    "// Docker 또는 PostgreSQL 클라이언트를 사용하여 DB에 연결 후 init.sql 실행",
    "uvicorn main:app --reload"
  ]
}
```