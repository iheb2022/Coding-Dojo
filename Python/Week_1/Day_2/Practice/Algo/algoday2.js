// the client give us the two strings
// we gonna compare the length of the strings if we have the same length we do the next step
// else we gonna return false
// first we need to make the strings with upper case and we gonna compare it
// if we have the same words : the result should be true 
// else : the result should be false
function compare(strA1,strA2){
  var Firstr = strA1.ToUpperCase()
  var Secondestr = strA2.ToUpperCase()
  if(
    Firstr == Secondestr
  )
  return true;
  else 
  return false;
}