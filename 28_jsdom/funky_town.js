var factorial=function(n){
  if(n<2)
    return 1;
  else {
    return n*factorial(n-1);
  }
}
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
  console.log(var);
  return internalList[num];
};
var output = document.getElementById('output'); 

var factorialDOM = document.getElementById('factorial');
factorialDOM.addEventListener('click', function() {
  var num = factorial(5);
  console.log(num);
  output.innerHTML = '<h3>' + num + '</h3>';
});

var fibonacciDOM = document.getElementById('fibonacci');
fibonacciDOM.addEventListener('click', function() {
  var num = fibonacci(6);
  console.log(num);
  output.innerHTML = '<h3>' + num + '</h3>';
});

var gcdDOM = document.getElementById('gcd');
gcdDOM.addEventListener('click', function() {
  var num = gcd(12, 28);
  console.log(num);
  output.innerHTML = '<h3>' + num + '</h3>';
});

var randomStudentDOM = document.getElementById('randomStudent');
randomStudentDOM.addEventListener('click', function() {
  var student = randomStudent();
  console.log(student);
  output.innerHTML = '<h3>' + student + '</h3>';
});
