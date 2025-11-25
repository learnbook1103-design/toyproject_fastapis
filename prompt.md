```
{
  "project_name": "toyproject_fastapis",
  "task": "FastAPI 프로젝트 초기 파일 구조 및 코드 생성",
  "files_to_create": [
    {
      "file_path": "main.py",
      "purpose": "FastAPI 애플리케이션 메인 엔트리 포인트 및 라우팅 정의",
      "content_details": {
        "description": "Jinja2 템플릿을 사용하여 HTML 파일을 렌더링하는 기본 라우트를 포함합니다. 템플릿 디렉토리는 'templates'입니다.",
        "requirements": [
          "FastAPI, Request, HTMLResponse, Jinja2Templates 임포트",
          "FastAPI 인스턴스 초기화",
          "Jinja2Templates 디렉토리 설정 (directory='templates')",
          "루트 경로 ('/')에 GET 메서드 라우트 함수 정의",
          "라우트 함수는 'index.html'을 렌더링하며 'title' 변수를 전달"
        ],
        "example_code_snippet": [
          "from fastapi import FastAPI, Request",
          "from fastapi.responses import HTMLResponse",
          "from fastapi.templating import Jinja2Templates",
          "...",
          "templates = Jinja2Templates(directory='templates')",
          "...",
          "return templates.TemplateResponse(name='index.html', context={'request': request, 'title': 'FastAPI Web App'})"
        ]
      }
    },
    {
      "file_path": "templates/index.html",
      "purpose": "FastAPI에서 렌더링할 기본 HTML 템플릿",
      "content_details": {
        "description": "기본 HTML5 구조와 Jinja2 변수(title)를 포함합니다.",
        "requirements": [
          "HTML5 기본 구조",
          "title 태그 안에 {{ title }} 변수 사용",
          "h1 태그 안에 'Welcome to FastAPI HTML' 텍스트 포함"
        ]
      }
    },
    {
      "file_path": ".vscode/launch.json",
      "purpose": "Visual Studio Code 디버깅 설정",
      "content_details": {
        "description": "VS Code에서 Uvicorn을 사용하여 'main.py'를 디버그 모드로 실행하는 구성을 정의합니다.",
        "requirements": [
          "구성 이름: 'Launch uvicorn'",
          "요청 유형: 'launch'",
          "모듈: 'uvicorn'",
          "인수: ['main:app', '--reload']"
        ]
      }
    },
    {
      "file_path": "requirements.txt",
      "purpose": "프로젝트 종속성 명시",
      "content_details": {
        "description": "프로젝트 실행에 필요한 라이브러리 목록입니다.",
        "requirements": [
          "fastapi",
          "uvicorn[standard]",
          "jinja2"
        ]
      }
    }
  ],
  "dependencies_check_command": "pip install -r requirements.txt",
  "run_command": "uvicorn main:app --reload"
}
```