function clickbtn(element){
  var a=document.querySelector(element)
  a.innerText="Any name"
}

function delet(id) {
  var element = document.querySelector(id);
  element.remove();
}

function decrease(id){
  var request=document.querySelector(id)
  request.innerHTML--;
}

function increase(id) {
  var element = document.querySelector(id);
  element.innerHTML++;
}

