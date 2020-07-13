from flask import Flask, render_template, request
#from bs4 import NavigableString
#from bs4 import BeautifulSoup
#from easygui import *
#import requests
#import re
#import nltk
#import csv
#import sys
#import easygui as eg
from newspaper import Article
from googlesearch import search


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    msg = userText
    rec = 'site:receita.economia.gov.br intext:' + msg
    listag = []
    for urla in search(rec, tld='com.br', lang='pt-br', stop=3):
        listag.append(urla)
    else:
        print('Pesquisa não encontrada! Poderia ser mais específico, por favor!')

    g = int(len(listag))
    print(g)

    listago = []
    for z in range(0, g):
        ur = str(listag[z])
        listago.append(ur)
    else:
        print('Pesquisa não encontrada! Poderia ser mais específico, por favor!')

    print(listago)
    qo = int(len(listago))

    reports2 = []
    for r in range(0, qo):
        ia = str(listago[r])
        article = Article(ia, language="pt")
        article.download()
        article.parse()
        article.text
        article.nlp()
        article.summary
        reports2.append(str(article.text).replace('\n', ''))

    resposta_final = str(reports2).replace('\n', ' ')
    return str(resposta_final) or ("PESQUISA NÃO ENCONTRADA!")


if __name__ == "__main__":
    app.run()
