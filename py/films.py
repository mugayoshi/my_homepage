from yattag import Doc


class FilmsHtml:

    style_files = ['css/style_films.css']

    def write_films_content(self):
        films = {'episode I': 'img/phantom_menace.jpeg'}
        # modal-content
        doc_modal = Doc()
        with doc_modal.tag('div', id='modal-content'):
            with doc_modal.tag('div', klass='container'):
                with doc_modal.tag('div', klass='row'):
                    for film_title in films.keys():
                        with doc_modal.tag('div', klass="film"):
                            doc_modal.line('img','',  klass='slide_pic', src=films.get(film_title))
                            doc_modal.line('p', film_title)
        # modal-overlay
        doc_overlay = Doc()
        doc_overlay.line('div', '', id='modal-overlay')
        # container
        doc_cont = Doc()

        with doc_cont.tag('div', klass="container"):
            doc_cont.line('h1', 'My Favourite Films', klass='my-4 text-center text-lg-left')
            with doc_cont.tag('div', klass='row text-center text-lg-left'):
                film_id = 0
                for img_path in films.values():
                    with doc_cont.tag('div', klass='col-lg-3 col-md-4 col-xs-6'):
                        with doc_cont.tag('a', klass='d-block mb-4 h-100', href='#'):
                            doc_cont.line('img', '', klass='img-fluid img-thumbnail', id=film_id, src=img_path)
                    ++film_id

        return doc_modal.getvalue() + doc_overlay.getvalue() + doc_cont.getvalue()