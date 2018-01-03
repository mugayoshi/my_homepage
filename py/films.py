from yattag import Doc


class FilmsHtml:

    style_files = ['css/style_films.css']

    def write_films_content(self):
        films = {'The Empire Strikes Back': 'img/empire.jpg',
                 'Return of the Jedi': 'img/jedi.jpg',
                 'Mad Max Fury Road': 'img/fury_road.jpg'}
        # modal-content
        doc_modal = Doc()
        with doc_modal.tag('div', id='modal-content'):
            with doc_modal.tag('div', klass='container'):
                with doc_modal.tag('a', klass='button-link', id='modal-close'):
                    doc_modal.line('i', '', klass='fa fa-times', aria_hidden='true')
                with doc_modal.tag('div', klass='row'):
                    for film_title in films.keys():
                        with doc_modal.tag('div', klass='film'):
                            doc_modal.line('img','',  klass='slide_pic', src=films.get(film_title))
                            doc_modal.line('p', film_title)
                with doc_modal.tag('div', klass='row'):
                    with doc_modal.tag('div', klass='btn', id='btn_prev'):
                        doc_modal.line('i', '', klass='fa fa-arrow-circle-o-left', aria_hidden='true')
                    with doc_modal.tag('div', klass='btn', id='btn_next'):
                        doc_modal.line('i', '', klass='fa fa-arrow-circle-o-right', aria_hidden='true')
        
        str_to_be_replaced = dict()
        str_to_be_replaced['aria_hidden'] = 'aria-hidden'
        
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
                    film_id += 1

        films_content = doc_modal.getvalue() + doc_overlay.getvalue() + doc_cont.getvalue()
        for str_key in str_to_be_replaced.iterkeys():
            films_content.replace(str_key, str_to_be_replaced.get(str_key))

        return films_content
