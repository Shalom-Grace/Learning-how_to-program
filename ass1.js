/*****************
 * CODING CHALLENGE 1
 */
var Johnsmass = 54;
var Johnsheight = 1.69;
var Marksmass = 84;
var Marksheight = 1.32;

var JohnsBMI = Johnsmass/(Johnsheight*Johnsheight);
var MarksBMI = Marksmass/(Marksheight*Marksheight);

var pink = MarksBMI > JohnsBMI;
console.log(pink);
console.log("John's BMI is " + JohnsBMI);
console.log("Mark's BMI is " + MarksBMI);
console.log("Is Mark's BMI greater than John's " + pink);
