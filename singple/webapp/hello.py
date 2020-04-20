from flask import Flask,render_template,request 
from vsearch import search4letters

app = Flask (__name__)


    
@app.route('/search4',methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']    #创建两个新变量“phrase”，“letters”
    letters = request.form['letters']  #并把HTML表单的数据赋至新创建的变量
    #创建一个python变量，名为title，并为title赋一个字符串
    title = '结果展示:'
    #创建一个python变量，名为results,将“search4letters”的调用结果赋给"results“
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)
                           
                           
@app.route('/') #entry_page函数现在有两个关联的URL
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='欢迎访问!')