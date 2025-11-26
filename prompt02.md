```
{
  "project_name": "toyproject_fastapis",
  "task": "FastAPI 공지사항 CRUD 구현 (PostgreSQL 연동) 및 모든 파일 초기 생성",
  "action": "CREATE_ALL_FILES",
  "files": [
    {
      "file_path": "main.py",
      "action_type": "CREATE",
      "purpose": "FastAPI 애플리케이션 메인 엔트리 포인트, 라우팅 정의 및 DB 연동 CRUD 로직 포함",
      "content_details": {
        "description": "PostgreSQL 연동 기반 CRUD API 엔드포인트와 HTML 폼 및 목록 렌더링 라우트 포함.",
        "requirements": [
          "FastAPI, Jinja2Templates, db, models 임포트",
          "PostgreSQL 기반의 5가지 CRUD API 라우트 (`/notices/` POST, GET, PUT, DELETE) 구현",
          "공지사항 목록 웹 뷰 라우트 (`/notices_web/`) 구현 (notices.html 렌더링)",
          "공지사항 등록 폼 제공 라우트 (`/notices/create`) 구현 (notice_form.html 렌더링)",
          "공지사항 수정 폼 제공 라우트 (`/notices/edit/{id}`) 구현 (notice_form.html 렌더링)",
          "기존 `/` 경로 라우트 유지 (index.html 렌더링)"
        ]
      }
    },
    {
      "file_path": "db.py",
      "action_type": "CREATE",
      "purpose": "PostgreSQL 연결 함수 정의",
      "content_details": {
        "description": "psycopg2를 사용하여 DB 연결을 수행하며, 하드코딩된 값 사용.",
        "requirements": [
          "psycopg2 임포트",
          "DB_HOST: 'db_postgresql', DB_PORT: '5432', POSTGRES_DB: 'main_db', POSTGRES_USER: 'admin', POSTGRES_PASSWORD: 'admin123' 사용",
          "get_db_connection() 함수 정의"
        ]
      }
    },
    {
      "file_path": "models.py",
      "action_type": "CREATE",
      "purpose": "Pydantic 데이터 모델 (스키마) 정의",
      "content_details": {
        "description": "공지 사항 데이터의 구조를 정의합니다.",
        "requirements": [
          "NoticeBase (title, content)",
          "NoticeCreate (NoticeBase 상속)",
          "Notice (id, created_at, NoticeBase 상속)"
        ]
      }
    },
    {
      "file_path": "init.sql",
      "action_type": "CREATE",
      "purpose": "PostgreSQL 테이블 생성 스크립트",
      "content_details": {
        "description": "'notices' 테이블 생성 SQL 구문 및 테스트 데이터 삽입 포함",
        "requirements": [
          "CREATE TABLE notices",
          "컬럼: id (SERIAL PRIMARY KEY), title (VARCHAR), content (TEXT), created_at (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)",
          "테스트 데이터 INSERT 구문 포함"
        ]
      }
    },
    {
      "file_path": "templates/index.html",
      "action_type": "CREATE",
      "purpose": "기본 시작 페이지 템플릿",
      "content_details": {
        "description": "프로젝트의 시작점을 알리는 간단한 HTML 페이지",
        "requirements": [
          "HTML5 구조",
          "루트 경로 (`/`)에서 렌더링",
          "공지 사항 목록(`/notices_web/`)으로 이동하는 링크 포함"
        ]
      }
    },
    {
      "file_path": "templates/notices.html",
      "action_type": "CREATE",
      "purpose": "공지 사항 목록 표시 및 CRUD 버튼 포함 템플릿",
      "content_details": {
        "description": "DB에서 가져온 notices 리스트를 순회하며 출력하고 등록, 수정, 삭제 링크 포함",
        "requirements": [
          "Jinja2 루프 사용",
          "'/notices/create' 링크 포함",
          "각 항목에 '/notices/edit/{id}' 및 '/notices/delete/{id}' 링크 포함"
        ]
      }
    },
    {
      "file_path": "templates/notice_form.html",
      "action_type": "CREATE",
      "purpose": "공지 사항 등록 및 수정에 사용되는 HTML 폼 템플릿",
      "content_details": {
        "description": "제목과 내용 입력 필드, POST/PUT 액션 처리를 위한 폼 포함",
        "requirements": [
          "제목(title) 및 내용(content) 입력 필드",
          "POST 메서드를 사용하여 데이터 전송",
          "수정 시 기존 데이터를 표시하는 Jinja2 구문 포함"
        ]
      }
    },
    {
      "file_path": "requirements.txt",
      "action_type": "CREATE",
      "purpose": "프로젝트 종속성 명시",
      "content_details": {
        "description": "프로젝트 실행에 필요한 라이브러리 목록입니다.",
        "requirements": [
          "fastapi",
          "uvicorn[standard]",
          "jinja2",
          "psycopg2-binary" 
        ]
      }
    }
  ],
  "next_step_cli": [
    "pip install -r requirements.txt",
    "// Docker 또는 PostgreSQL 클라이언트를 사용하여 DB에 연결 후 init.sql 실행",
    "uvicorn main:app --reload"
  ]
}
```