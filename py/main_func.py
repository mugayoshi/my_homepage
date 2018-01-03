from yattag import Doc
import sys
from films import FilmsHtml
from index import IndexHtml


def write_head_tag():
    doc, tag, text, line = Doc().ttl()
    bootstrap_url = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css'
    bootstrap_intgrty = 'sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb'
    stylesheet_public = ['css/normalize.css', 'css/font-awesome.min.css']
    my_stylesheets_common = ['css/style_common.css']
    my_stylesheets = []
    stylesheets_font = ['https://fonts.googleapis.com/css?family=Cherry+Swash:700'
                        , 'https://fonts.googleapis.com/css?family=Anton']

    if len(sys.argv) < 2:
        my_stylesheets = IndexHtml().style_files
    elif 'film' in sys.argv[1]:
        my_stylesheets = FilmsHtml().style_files
    else:
        my_stylesheets = ['css/style_index.css']

    with tag('head'):
        line('meta', '', charset='utf-8')
        line('meta', '', name='view-point', content='width=device-width, initial-scale=1')
        line('title', 'Muga Yoshikawa')

        for s in my_stylesheets_common:
            line('link', '', rel="stylesheet", href=s)
        for s in stylesheet_public:
            line('link', '', rel="stylesheet", href=s)
        for s in my_stylesheets:
            line('link', '', rel="stylesheet", href=s)

        line('link', '', rel="stylesheet", href=bootstrap_url, integrity=bootstrap_intgrty, crossorigin='anonymous')

        for s in stylesheets_font:
            line('link', '', rel="stylesheet", href=s)

    print doc.getvalue()


def write_body_tag():
    print '<body>'
    print write_nav_bar()
    print write_content()
    print write_footer()
    print write_source_scripts()
    print '</body>'

    return


def write_nav_bar():
    doc, tag, text, line = Doc().ttl()
    menu_links = {'Profile': 'profile.html', 'Albums': 'albums.html', 'Films': 'films.html'}

    with tag('div', id="header"):
        with tag('nav', klass='navbar navbar-expand-lg navbar-dark bg-dark'):
            line('a', 'Muga\'s Page', klass='navbar-brand', href='#')

            with tag(
                    'button', klass='navbar-toggler', type='button',
                    data_toggle='collapse', data_target='#navbarNavDropdown',
                    aria_controls='navbarNavDropdown', aria_expanded='false',
                    aria_label='Toggle navigation'):
                line('span', '', klass='navbar-toggler-icon')

            with tag('div', klass='collapse navbar-collapse', id='navbarNavDropdown'):
                with tag('ul', klass='navbar-nav'):
                    with tag('li', klass="nav-item active"):
                        with tag('a', klass='nav-link', href='#'):
                            text('HOME')
                            line('span', '(current)', klass='sr-only')
                    for k, l in menu_links.iteritems():
                        with tag('li', klass="nav-item"):
                            line('a', k, klass='nav-link', href=l)

    # return doc.getvalue().replace('_', '-')
    return doc.getvalue().replace('_', '-')


def write_footer():
    doc_f = Doc()
    doc_f.line('div', 'created by Muga Yoshikawa', id="footer")
    return doc_f.getvalue()


def write_content():
    if len(sys.argv) < 2:
        return IndexHtml().write_films_content()
    elif 'film' in sys.argv[1]:
        return FilmsHtml().write_films_content()
    else:
        print 'error'

    return


def write_source_scripts():
    jquery_link = dict(src='https://code.jquery.com/jquery-3.2.1.slim.min.js',
                       integrity='sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN',
                       crossorigin='anonymous')
    popper_link = dict(src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js',
                       integrity='sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh',
                       crossorigin='anonymous')
    bootstrap_link = dict(src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js',
                          integrity='sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ',
                          crossorigin='anonymous')
    js_src = ['js/footerFixed.js']

    if len(sys.argv) > 1 and 'film' in sys.argv[1]:
        js_src.append('js/films_controller.js')
        jquery_link = dict(src='https://code.jquery.com/jquery-3.2.1.js',
                           integrity='sha256-DZAnKJ/6XZ9si04Hgrsxu/8s717jcIzLy3oi35EouyE=',
                           crossorigin='anonymous')

    doc = Doc()

    doc.line('script', '', src=jquery_link['src'], integrity=jquery_link['integrity'], crossorigin=jquery_link['crossorigin'])
    doc.line('script', '', src=popper_link['src'], integrity=popper_link['integrity'], crossorigin=popper_link['crossorigin'])
    doc.line('script', '', src=bootstrap_link['src'], integrity=bootstrap_link['integrity'], crossorigin=bootstrap_link['crossorigin'])

    for j in js_src:
        doc.line('script', '', type='text/javascript', src=j)

    return doc.getvalue()


def main():
    print '<!DOCTYPE html><html lang="en">'
    write_head_tag()
    write_body_tag()
    print '</html>'


if __name__ == "__main__":
    main()