function Fibonacci(n) {
    if (n <= 1) {
        return n;
    }
    else {
        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }
}
console.log("Fibonacci", Fibonacci(10));
