from yattag import Doc

def writeHeadTag():
  doc, tag, text, line = Doc().ttl()
  bootstrap_url = 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css'
  bootstrap_intgrty='sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb'
  stylesheet_public = ['css/normalize.css', 'css/font-awesome.min.css']
  my_stylesheets_common = ['css/style_common.css']
  my_stylesheets = ['css/style_index.css']
  stylesheets_font = ['https://fonts.googleapis.com/css?family=Cherry+Swash:700']



  with tag('head'):
    line('meta','', charset='utf-8')
    line('meta','', name='view-point', content='width=device-width, initial-scale=1')
    line('title', 'Muga Yoshikawa')
    '''
    for s in stylesheet_public:
      line('link', '', rel="stylesheet", href=s)
    '''
    for s in my_stylesheets_common:
      line('link', '', rel="stylesheet", href=s)

    for s in my_stylesheets:
      line('link', '', rel="stylesheet", href=s)

    line('link', '', rel="stylesheet", href=bootstrap_url, integrity=bootstrap_intgrty, crossorigin='anonymous')

    for s in stylesheets_font:
      line('link', '', rel="stylesheet", href=s)

  return doc.getvalue()

def writeBodyTag():
  doc, tag, text, line = Doc().ttl()
  menu_links = {'Profile': '../profile.html', 'Albums': '../albums.html'}
  jquery_link = {'src': 'https://code.jquery.com/jquery-3.2.1.slim.min.js',
                 'integrity': 'sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN',
                 'crossorigin': 'anonymous'}
  popper_link = {'src': 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js',
                 'integrity': 'sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh',
                 'crossorigin': 'anonymous'}
  bootstrap_link = {'src': 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js',
                    'integrity': 'sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ',
                    'crossorigin': 'anonymous'}

  with tag('div', id="header"):
    with tag('nav', klass='navbar navbar-expand-lg navbar-dark bg-dark'):
      line('a','Muga\'s Page', klass='navbar-brand', href='#')

      with tag('button',
               klass='navbar-toggler', type='button',
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

  line('script', '', src=jquery_link['src'], integrity=jquery_link['integrity'], crossorigin=jquery_link['crossorigin'])
  line('script', '', src=popper_link['src'], integrity=popper_link['integrity'], crossorigin=popper_link['crossorigin'])
  line('script', '', src=bootstrap_link['src'], integrity=bootstrap_link['integrity'], crossorigin=bootstrap_link['crossorigin'])



  '''
    write content
  '''
  '''
    write footer
  '''


  print '<body>'
  print doc.getvalue().replace('_', '-')
  print '</body>'

def main():
  print '<!DOCTYPE html><html lang="en">'
  print writeHeadTag()
  writeBodyTag()
  print '</html>'

if __name__ == "__main__":
  main()