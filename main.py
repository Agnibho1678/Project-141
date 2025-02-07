from flask import Flask, jsonify, request
import csv

all_articles = []

with open('articles.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    }) 

@app.route("/liked-article", methods = ['POST'])
def liked_article():
    article = all_articles[0]
    allArticles = all_articles[1:]
    liked_article.append(article)
    
    return jsonify({
        "status": "success"
    
    }), 201 

@app.route("/unliked-article", methods = ['POST'])
def unliked_article():
    article = all_articles[0]
    allArticles = all_articles[1:]
    unliked_article.append(article)
    
    return jsonify({
        "status": "success"
    
    }), 201 


if __name__ == "__main__":
    app.run()