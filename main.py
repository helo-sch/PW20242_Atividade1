from os import name
from fastapi import FastAPI, Form, Request 
from fastapi.responses import RedirectResponse 
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates 
from models.produto_model import Produto 
from repositories import produto_repo 
from repositories.produto_repo import * 
import uvicorn 
 
criar_tabela() 
app = FastAPI() 
 
templates = Jinja2Templates(directory='templates') 
 
app.mount("/static", StaticFiles(directory="static"), name="static") 
 
@app.get("/") 
def get_root(request: Request): 
    return templates.TemplateResponse('index.html', {"request": request}) 
 
@app.get("/cadastro") 
def get_cadastro(request: Request): 
    return templates.TemplateResponse('cadastro.html', {"request": request}) 
 
@app.post("/post_cadastro") 
def post_cadastro( 
    request: Request, 
    nome: str = Form(...), 
    descricao: str = Form(...), 
    estoque: str = Form(...), 
    preco: str = Form(...), 
    categoria: str = Form(...)):  # Adicionando categoria 
    produto = Produto(0, nome, descricao, estoque, preco, categoria) 
    produto = produto_repo.inserir(produto) 
    if post_cadastro: 
        return RedirectResponse('/cadastro_recebido', 303) 
    else: 
        return RedirectResponse('/cadastro', 303) 
     
     
@app.get("/cadastro_recebido") 
def get_cadastro_recebido(request: Request): 
    return templates.TemplateResponse('index.html', {"request": request}) 
 
if name == "__main__": 
    uvicorn.run("main:app", port=8000, reload=True)