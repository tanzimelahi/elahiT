 document.getElementById("b").addEventListener("click",function(){
  var node = document.createElement("LI");
  var textnode = document.createTextNode("pika");
  node.appendChild(textnode);
  addEvent(node,"mouseover");
  addEvent2(node,"mouseout");
  disappear(node);
  document.getElementById("thelist").appendChild(node);
});
var list=document.getElementsByTagName("li");
var changeHeading=function(x){
  var heading=document.getElementById("h");
  heading.innerHTML=x;
}
var addEvent=function(obj,eventName){
  obj.addEventListener(eventName,function(x){
    changeHeading(obj.innerHTML);
  });
};
var addEvent2=function(obj,eventName){
  obj.addEventListener(eventName,function(x){
    changeHeading("helloWorld");
  });
};
var disappear=function(node){
  var obj=document.getElementById("thelist");
  node.addEventListener("click",function(){
    obj.removeChild(node);
  });
};
for (var i=0;i<list.length;i++){
  addEvent(list[i],"mouseover");
  addEvent2(list[i],"mouseout");
  disappear(list[i]);
};
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

});
