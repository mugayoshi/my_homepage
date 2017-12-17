import sys
from yattag import Doc
class IndexHtml():
  style_files = ['css/style_index.css']

  def write_films_content(self):
    doc_cont = Doc()
    with doc_cont.tag('div', id="main"):
      with doc_cont.tag('div', klass="container"):
        doc_cont.line('p', 'Hello, I\'m Muga.')
        doc_cont.line('p', 'Welcome to my page.')
        doc_cont.line('p', 'Take a look and I hope you\'d have fun !')
    return doc_cont.getvalue()