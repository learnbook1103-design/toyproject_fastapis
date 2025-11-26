import psycopg2
from fastapi import FastAPI, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List
from models import Notice, NoticeCreate
from db import get_db_connection

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# --- HTML Rendering Routes ---

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/notices_web/", response_class=HTMLResponse)
async def read_notices_web(request: Request):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, content, created_at FROM notices ORDER BY created_at DESC")
    notices_records = cur.fetchall()
    cur.close()
    conn.close()
    notices = [Notice(id=row[0], title=row[1], content=row[2], created_at=row[3]) for row in notices_records]
    return templates.TemplateResponse("notices.html", {"request": request, "notices": notices})

@app.get("/notices/create/", response_class=HTMLResponse)
async def create_notice_form(request: Request):
    return templates.TemplateResponse("notice_form.html", {"request": request, "notice": None})

@app.get("/notices/edit/{notice_id}", response_class=HTMLResponse)
async def edit_notice_form(request: Request, notice_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, content, created_at FROM notices WHERE id = %s", (notice_id,))
    notice_record = cur.fetchone()
    cur.close()
    conn.close()
    if not notice_record:
        raise HTTPException(status_code=404, detail="Notice not found")
    notice = Notice(id=notice_record[0], title=notice_record[1], content=notice_record[2], created_at=notice_record[3])
    return templates.TemplateResponse("notice_form.html", {"request": request, "notice": notice})

# --- Form Handling Routes ---

@app.post("/notices/create/", response_class=RedirectResponse)
async def handle_create_notice_form(title: str = Form(...), content: str = Form(...)):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO notices (title, content) VALUES (%s, %s)",
        (title, content)
    )
    conn.commit()
    cur.close()
    conn.close()
    return RedirectResponse(url="/notices_web/", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/notices/edit/{notice_id}", response_class=RedirectResponse)
async def handle_edit_notice_form(notice_id: int, title: str = Form(...), content: str = Form(...)):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE notices SET title = %s, content = %s WHERE id = %s",
        (title, content, notice_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return RedirectResponse(url="/notices_web/", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/notices/delete/{notice_id}", response_class=RedirectResponse)
async def handle_delete_notice(notice_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM notices WHERE id = %s", (notice_id,))
    conn.commit()
    cur.close()
    conn.close()
    return RedirectResponse(url="/notices_web/", status_code=status.HTTP_303_SEE_OTHER)


# --- API Routes (for programmatic access) ---

@app.post("/notices/", response_model=Notice, status_code=status.HTTP_201_CREATED)
def create_notice_api(notice: NoticeCreate):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(
        "INSERT INTO notices (title, content) VALUES (%s, %s) RETURNING id, title, content, created_at",
        (notice.title, notice.content)
    )
    new_notice_record = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if new_notice_record:
        return new_notice_record
    raise HTTPException(status_code=500, detail="Failed to create notice")

@app.get("/notices/", response_model=List[Notice])
def read_notices_api(skip: int = 0, limit: int = 10):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT id, title, content, created_at FROM notices ORDER BY created_at DESC LIMIT %s OFFSET %s", (limit, skip))
    notices_records = cur.fetchall()
    cur.close()
    conn.close()
    return notices_records

@app.get("/notices/{notice_id}", response_model=Notice)
def read_notice_api(notice_id: int):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT id, title, content, created_at FROM notices WHERE id = %s", (notice_id,))
    notice_record = cur.fetchone()
    cur.close()
    conn.close()
    if notice_record:
        return notice_record
    raise HTTPException(status_code=404, detail="Notice not found")

@app.put("/notices/{notice_id}", response_model=Notice)
def update_notice_api(notice_id: int, notice: NoticeCreate):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(
        "UPDATE notices SET title = %s, content = %s WHERE id = %s RETURNING id, title, content, created_at",
        (notice.title, notice.content, notice_id)
    )
    updated_notice_record = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if updated_notice_record:
        return updated_notice_record
    raise HTTPException(status_code=404, detail="Notice not found")

@app.delete("/notices/{notice_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_notice_api(notice_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM notices WHERE id = %s RETURNING id", (notice_id,))
    deleted_id = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if not deleted_id:
        raise HTTPException(status_code=404, detail="Notice not found")
