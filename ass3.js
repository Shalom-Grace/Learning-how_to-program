function calculateTip(bill) {
    var tip;
    if (bill < 50) {
        tip = (0.2 * bill);
           }
    else if (bill >= 50 && bill < 200){
        tip = (0.5 * bill);
        }
    else{
        tip = (0.1 * bill);
    }
    console.log('Your tip is ' + tip);
}

calculateTip(124);
calculateTip(48);
calculateTip(268);

var bills = [124, 48, 268];
var tips = [calculateTip(bills[0]), calculateTip(bills[1]), calculateTip(bills[2])];
var finalValues = [bills[0] + tips[0], bills[1] + tips[1], bills[2] + tips[2]];
console.log(tips, finalValues);