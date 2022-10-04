//Objects and methods
//********************************************** */
var Mark = {
    fullName: 'Mark Alexander',
    mass: 79,
    height: 1.34,
    calcBMI: function(){
        this.BMI = this.mass / (this.height * this.height);
        return this.BMI;
    }
};

var John = new Object();
John.fullName = 'John Akpos';
John.mass = 86;
John.height = 1.18;
John.calcBMI = function () {
   this.BMI = this.mass / (this.height * this.height);
   return this.BMI;
};

console.log(John);
console.log(Mark);
calcBMI();
calcBMI1();