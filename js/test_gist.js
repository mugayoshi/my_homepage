var token = '2c14581727e7ee3d9d06fafeee4cba4a390263b7';
var url = 'https://api.github.com/gists';
var content = window.getSelection().toString();
var filename = prompt('what is filename ?', 'index.js');

var json = {
  "description": 'this code was located in ' + location.href ,
  "public": true,
  "files": {}
};

json.files[filename] = {
  "content": content;
};

var request = new XMLHttpRequest();
request.open('POST', url, true);
request.setRequestHeader('Content-Type', 'application/json');
request.setRequestHeader('Authorization', 'token ' + token);

request.onload = function(){
  if (request.status >= 200 && request.status <= 400){
    var json = JSON.parse(request.responseText);
    if (confirm('Do you open thie URL ?')){
      window.open(json.html_url, '_blank');
    }
  }else {
    alert('Error occurs ' + request.responseText);
  }
};
request.send(JSON.stringify(json));
