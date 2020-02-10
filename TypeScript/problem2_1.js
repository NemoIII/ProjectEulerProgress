// import {Memoize} from 'typescript-memoize'
function Fibonacci(n) {
    if (n === 0 || n === 1) {
        return n;
    }
    else {
        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }
}
console.log("Fibonacci", Fibonacci(9));
