// import {Memoize} from 'typescript-memoize'


function Fibonacci(n: number) {
    let memo = {}

    function f(x: number) {
        let value;
        if (x in memo) {
            value = memo[x];
        } else {
            if (n === 0 || n === 1) {
                return n;
            } else {
                return Fibonacci(n - 1) + Fibonacci(n - 2);
            }
        }
    }
}
console.log("Fibonacci", Fibonacci(9))
