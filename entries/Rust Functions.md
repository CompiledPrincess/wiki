# Rust Functions
Rust’s syntax is deliberately unoriginal. If you are familiar with C, C++, Java, or JavaScript, you can probably find your way through the general structure of a Rust program. Here is a function that computes the greatest common divisor of two integers, using Euclid’s algorithm. You can add this code to the end of src/main.rs:

    assert!(n != 0 && m != 0);
    while m != 0 {
        if m < n {
            let t = m;
            m = n;
            n = t;
        }
        m = m % n;
      }
      n
      }

The fn keyword (pronounced “fun”) introduces a function. Here, we’re defining a function named gcd, which takes two parameters n and m, each of which is of type u64, an unsigned 64-bit integer. The -> token precedes the return type: our function returns a u64 value. Four-space indentation is standard Rust style.

Rust’s machine integer type names reflect their size and signedness: i32 is a signed 32-bit integer; u8 is an unsigned 8-bit integer (used for “byte” values), and so on. The isize and usize types hold pointer-sized signed and unsigned integers, 32 bits long on 32-bit platforms, and 64 bits long on 64-bit platforms. Rust also has two floating-point types, f32 and f64, which are the IEEE single- and double-precision floating-point types, like float and double in C and C++.

By default, once a variable is initialized, its value can’t be changed, but placing the mut keyword (pronounced “mute,” short for mutable) before the parameters n and m allows our function body to assign to them. In practice, most variables don’t get assigned to; the mut keyword on those that do can be a helpful hint when reading code.

The function’s body starts with a call to the assert! macro, verifying that neither argument is zero. The ! character marks this as a macro invocation, not a function call. Like the assert macro in C and C++, Rust’s assert! checks that its argument is true, and if it is not, terminates the program with a helpful message including the source location of the failing check; this kind of abrupt termination is called a panic. Unlike C and C++, in which assertions can be skipped, Rust always checks assertions regardless of how the program was compiled. There is also a debug_assert! macro, whose assertions are skipped when the program is compiled for speed.

The heart of our function is a while loop containing an if statement and an assignment. Unlike C and C++, Rust does not require parentheses around the conditional expressions, but it does require curly braces around the statements they control.

A let statement declares a local variable, like t in our function. We don’t need to write out t’s type, as long as Rust can infer it from how the variable is used. In our function, the only type that works for t is u64, matching m and n. Rust only infers types within function bodies: you must write out the types of function parameters and return values, as we did before. If we wanted to spell out t’s type, we could write:

let t: u64 = m;
Rust has a return statement, but the gcd function doesn’t need one. If a function body ends with an expression that is not followed by a semicolon, that’s the function’s return value. In fact, any block surrounded by curly braces can function as an expression. For example, this is an expression that prints a message and then yields x.cos() as its value:


{
    println!("evaluating cos x");
    x.cos()
}
It’s typical in Rust to use this form to establish the function’s value when control “falls off the end” of the function, and use return statements only for explicit early returns from the midst of a function.

