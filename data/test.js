//recruitmsg
//gtx-body
//https://es.wikipedia.org/wiki/Desigualdad_matem%C3%A1tica

/*
Gráfica de la sucesión de Fibonacci hasta {\displaystyle f_{7}} {\displaystyle f_{7}}
En matemáticas, la sucesión de Fibonacci es la siguiente sucesión infinita de números naturales: 
0,1,1,2,3,5,8,13,21,34,55
La sucesión comienza con los números 0 y 1,2​ y a partir de estos, «cada término es la suma de los dos anteriores», es la relación de recurrencia que la define.
*/
/*
YES 
NO
*/

console.log(Math.pow(7, 3));    // 49

function exponente(val,mult){
    suma = val;
    if (mult>1){
        for (let index = 0; index < mult-1; index++) {
            suma = suma * val;
        }
    }
    
    return suma;
}
console.log(exponente(7,3));

function fibonacci(num) {
    if (num == 0 || num == 1){
        return num;
    }
    console.log("______");
    console.log("-1:" + fibonacci(num - 1));
    console.log("-2:" + fibonacci(num - 2));
    return fibonacci(num - 1) + fibonacci(num - 2);
}
for (let index = 0; index < 10; index++) {
    console.log("______________" + index);
    console.log(fibonacci(index));
}

function fibonacci(num){
    n1=1;
    n2=0;
    for (let index = 0; index < num; index++) {
        result = n1 + n2;
        n1=n2;
        n2 = result;
        console.log(result+" ");
        
    }
}
fibonacci(10);






/*
    El factorial de un entero positivo n, el factorial de n o n factorial se define en principio como el producto de todos los números enteros positivos desde 1 (es decir, los números naturales) hasta n. Por ejemplo:
    {\displaystyle 5!=1* 2* 3* 4* 5=120.\ } 5! = 1  *  2  *  3  *  4 *  5= 120.  \

*/
function factorial(n) {
    if (n <= 1) return 1;
    return (n * factorial(n - 1));
}
console.log(factorial(8));

function factorial(num)
{
    // If the number is less than 0, reject it.
    if (num < 0) {
        return -1;
    }
    // If the number is 0, its factorial is 1.
    else if (num == 0) {
        return 1;
    }
    // Otherwise, call this recursive procedure again.
    else {
        return (num * factorial(num - 1));
    }
}
console.log(factorial(8));