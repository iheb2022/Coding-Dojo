function here(){
  alert("Loading weather report...")
}

function ab(){
  var del = document.querySelector(".cookies");
  del.remove();
}
var arr=["red","blue","red1","blue1","red2","blue2","red3","blue3"]

function changing(){
  arr=["red","blue","red1","blue1","red2","blue2","red3","blue3"]
  for (var i=0;i<arr.length;i++){
    changeweather(arr[i])
  }
}

function changeweather(element){
  var hello=document.getElementById(element);
  hello.innerText= Math.floor((hello.innerText)*9/5+32);
}