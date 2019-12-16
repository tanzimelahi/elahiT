document.getElementById("b").addEventListener("click",function(){
  var node = document.createElement("LI");
  var textnode = document.createTextNode("pika");
  node.appendChild(textnode);
  document.getElementById("thelist").appendChild(node);
});
var list=document.getElementsByTagName("LI");
  console.log(list.length);
  for(var i=0; i<list.length;i++){
    list[i].addEventListener("mouseover",function(){
     document.getElementById("h").innerHTML=list[i].innerHTML;
     });
     list[i].addEventListener("mouseout",function(){
       document.getElementById("h").innerHTML="Hello World!" ;
     });
     list[i].addEventListener("click",function(){
       document.getElementById("thelist").removeChild(list[i]);
     });
  }
var fibonacchi=function(x){
  if(x==0){
    return 0;
  }
  else if(x==1){
    return 1;
  }
  else{
    return fibonacchi(x-1)+fibonacchi(x-2);
  }
}
var tracker=0;
document.getElementById("fb").addEventListener("click",function(){
  var node=document.createElement("LI");
  var text=document.createTextNode(fibonacchi(tracker));
  tracker++;
  node.appendChild(text);
  document.getElementById("fiblist").append(node);
  docu
})
