var fibonacchi=function(n){
  if (n==1) {
    return 1;
  }
  else if(n==0) {
    return 0;
  }
  else{
    return fibonacchi(n-1)+fibonacchi(n-2);
  }
};
var min=function(a,b){
  if(a<=b){
    return a;
  }
  else{
    return b;
  }
}
var gcd=function(a,b){
 var x=min(a,b);
 while (!(a%x==0 && b%x==0)){
   x--;
 }
 return x;
};
var randomStudent=function(){
  internalList=["Tanzim","Vishwat","Raymond","Jesse","Justin","Srinath"];
  var num=Math.floor(Math.random()*internalList.length);
  return internalList[num];
};
