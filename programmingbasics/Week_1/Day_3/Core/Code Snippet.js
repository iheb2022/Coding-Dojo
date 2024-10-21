function hello() {
  console.log('hello'); //this print hello
}
hello(); //this calls the function
console.log('Dojo'); //this print Dojo




function hello() {
  console.log('hello'); //this print hello
  return 15; //return the value 15
}
var result = hello(); //this call the function result = hello 
console.log('result is', result); //thi print the result is + 15



function numPlus(num) { 
  console.log('num is', num); //this print num is + num
  return num+15; //this return the value num+15
}
var result = numPlus(3); //this calls result =numPlus(3)
console.log('result is', result); //this print result is 3



var num = 15;  //this call the num = 15 
console.log(num); //this print 15
function logAndReturn(num){
   console.log(num);   //this print 15  
   return num; // this return the value 15
}
var result = logAndReturn(10); //this call thee result=LogAndReturn(10)
console.log(result); //this print 10  
console.log(num); //this print 15


var num = 15; //this call the num = 15
console.log(num); //this print 15
function timesTwo(num){
   console.log(num);   //this print 15
   return num*2; //this return the value 15*2 = 30
}
var result = timesTwo(10); //this call result = timesTwo(10)
console.log(result); //this print 20
console.log(num); //this print 30


function timesTwoAgain(num) {
  console.log('num is', num); //this print num is + num
  var y = num*2; //this call y = num*2
  return y; //this return y*2
}
var result = timesTwoAgain(3) + timesTwoAgain(5); //this call the result = timesTwoAgain(3) + timesTwoAgain(5)
console.log('result is', result); //this print result is 16



function sumNums(num1, num2) {  
  return num1+num2; //this return the value num1+num2
}
console.log(sumNums(2,3)) //this print 5
console.log(sumNums(3,5)) //this print 8


function printSumNums(num1, num2) {
  console.log(num1);   //this print only num1
  return num1+num2; //this return the value num1+num2
}
console.log(printSumNums(2,3)) //this print 5
console.log(printSumNums(3,5)) //this print 8


function sumNums(num1, num2) {
  var sum = num1 + num2; //this call sum = num1+num2
  console.log('sum is', sum); //this print sum is sum
  return sum; //this return the value sum
}
var result = sumNums(2,3) + sumNums(3,5); //this calls result = sumNums(2,3) + sumNums(3,5) = 5+8
console.log('result is', result); //this print 13


function sumNums(num1, num2) {
  var sum = num1 + num2; //this call sum = num1 + num2
  console.log('sum is', sum); //this print sum is sum
  return sum; //this return the value sum
}
var result = sumNums(2,3) + sumNums(3,sumNums(2,1)) + sumNums(sumNums(2,1),sumNums(2,3)); //this call 5+6+8
console.log('result is', result); //this print the result is 19

