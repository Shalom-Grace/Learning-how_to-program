//Average of two teams
//John's team 89, 120, 103
//Mikes's team 123, 116, 94

var avg1 = (179 + 120 + 103)/3
var avg2 = (113 + 160 + 94)/3
var avg3 = (137 + 134 + 104)/3

if (avg1 > avg2 && avg1 > avg3)
{
    console.log('John\'s team wins! score = ' + avg1);
}
else if(avg2 > avg3)
{
    console.log('Mike\'s team wins! score = ' + avg2);
}
else if (avg1 === avg2 === avg3)
{
    console.log('The game was a draw!! ' + avg1);
}
else{
    console.log('Mary\'s team wins! score = ' + avg3);
}