from yattag import Doc


class IndexHtml():

    style_files = ['css/style_index.css']

    def write_films_content(self):
        doc_cont = Doc()
        content = []
        with open('txt/index.txt', 'r') as f:
            lines = f.readlines()
        with doc_cont.tag('div', id="main"):
            with doc_cont.tag('div', klass="container"):
                for l in lines:
                    doc_cont.line('p', l)
        return doc_cont.getvalue()