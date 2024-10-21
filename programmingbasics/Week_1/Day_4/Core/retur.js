function  howMuchLeftOverCake(numberOfPieces,numberOfPeople) {

if (numberOfPieces== 0)
  return "No leftovers for you!"
else if(numberOfPieces<= 2)
  return "You have some leftovers"
else if (numberOfPieces<=5)
  return "You have leftovers to share"
else if (numberOfPieces>=5)
  return "Hold another party!"
}
console.log(numberOfPieces-numberOfPeople)

var numberOfPieces= 12
var numberOfPeople= 5
