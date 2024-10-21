function pizzaOven(crusType, sauceType, cheeses, toppings) {
  var pizza = {};
  pizza.crusType = crusType;
  pizza.sauceType = sauceType;
  pizza.cheeses = cheeses;
  pizza.toppings = toppings;
  return pizza;
}

var p1= pizzaOven("deep dish","traditional",["mozzarella"],["pepperoni","sausage"]);
console.log(p1);


var p2= pizzaOven("hand tossed","marinara",["mozzarella","feta"],["mushrooms","olives","onions"]);
console.log(p2);

var p3= pizzaOven("neapolitan","Margherita",["San Marzano tomatoes","mozzarella"],["olives","sausage"]);
console.log(p3)


var p4= pizzaOven("Stuffed","traditional",["feta","mozzarella"],["Onions","Pepperoni"]);
console.log(p4);