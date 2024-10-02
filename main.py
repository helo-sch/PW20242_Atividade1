from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()

templates = Jinja2Templates(directory='templates')

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

@app.post("/post_cadastro")
def post_cadastro(
    request: Request, 
    nome: str = Form(...), 
    descricao: str = Form(...), 
    estoque: str = Form(...), 
    preco: str = Form(...), 
    confirmacao_senha: str = Form(...)):
    salvar_cadastro(nome, descricao, estoque, preco)
        return RedirectResponse("/cadastro_recebido", 303)
    else:
        return RedirectResponse("/cadastro", 303)
    
@app.get("/cadastro_recebido")
def get_contato_recebido(request: Request):
    html = ler_html("cadastro_recebido")
    return HTMLResponse(html)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

