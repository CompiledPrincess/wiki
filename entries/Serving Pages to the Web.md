# Rust: Serving Pages to the Web
One of Rust’s strengths is the collection of freely available library packages published on the website crates.io. The cargo command makes it easy for your code to use a crates.io package: it will download the right version of the package, build it, and update it as requested. A Rust package, whether a library or an executable, is called a crate; Cargo and crates.io both derive their names from this term.

To show how this works, we’ll put together a simple web server using the actix-web web framework crate, the serde serialization crate, and various other crates on which they depend. 

$ cargo new actix-gcd
     Created binary (application) `actix-gcd` package
$ cd actix-gcd

[package]
name = "actix-gcd"
version = "0.1.0"
authors = ["You <you@example.com>"]
edition = "2018"

# See more keys and their definitions at
# https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
actix-web = "1.0.8"
serde = { version = "1.0", features = ["derive"] }
