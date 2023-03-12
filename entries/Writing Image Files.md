# Writing Image Files
The image crate provides functions for reading and writing a wide variety of image formats, along with some basic image manipulation functions. In particular, it includes an encoder for the PNG image file format, which this program uses to save the final results of the calculation. In order to use image, add the following line to the [dependencies] section of Cargo.toml:


image = "0.13.0"
With that in place, we can write:


use image::ColorType;
use image::png::PNGEncoder;
use std::fs::File;

/// Write the buffer `pixels`, whose dimensions are given by `bounds`, to the
/// file named `filename`.
fn write_image(filename: &str, pixels: &[u8], bounds: (usize, usize))
    -> Result<(), std::io::Error>
{
    let output = File::create(filename)?;

    let encoder = PNGEncoder::new(output);
    encoder.encode(&pixels,
                   bounds.0 as u32, bounds.1 as u32,
                   ColorType::Gray(8))?;

    Ok(())
}
image, add the following line to the [dependencies] section of Cargo.toml:


image = "0.13.0"
With that in place, we can write:


use image::ColorType;
use image::png::PNGEncoder;
use std::fs::File;

/// Write the buffer `pixels`, whose dimensions are given by `bounds`, to the
/// file named `filename`.
fn write_image(filename: &str, pixels: &[u8], bounds: (usize, usize))
    -> Result<(), std::io::Error>
{
    let output = File::create(filename)?;

    let encoder = PNGEncoder::new(output);
    encoder.encode(&pixels,
                   bounds.0 as u32, bounds.1 as u32,
                   ColorType::Gray(8))?;

    Ok(())
}
The operation of this function is pretty straightforward: it opens a file and tries to write the image to it. We pass the encoder the actual pixel data from pixels, and its width and height from bounds, and then a final argument that says how to interpret the bytes in pixels: the value ColorType::Gray(8) indicates that each byte is an eight-bit grayscale value.

That’s all straightforward. What’s interesting about this function is how it copes when something goes wrong. If we encounter an error, we need to report that back to our caller. As we’ve mentioned before, fallible functions in Rust should return a Result value, which is either Ok(s) on success, where s is the successful value, or Err(e) on failure, where e is an error code. So what are write_image’s success and error types?

When all goes well, our write_image function has no useful value to return; it wrote everything interesting to the file. So its success type is the unit type (), so called because it has only one value, also written (). The unit type is akin to void in C and C++.

When an error occurs, it’s because either File::create wasn’t able to create the file or encoder.encode wasn’t able to write the image to it; the I/O operation returned an error code. The return type of File::create is Result<std::fs::File, std::io::Error>, while that of encoder.encode is Result<(), std::io::Error>, so both share the same error type, std::io::Error. It makes sense for our write_image function to do the same. In either case, failure should result in an immediate return, passing along the std::io::Error value describing what went wrong.

So to properly handle File::create’s result, we need to match on its return value, like this:


let output = match File::create(filename) {
    Ok(f) => f,
    Err(e) => {
        return Err(e);
    }
};
On success, let output be the File carried in the Ok value. On failure, pass along the error to our own caller.

This kind of match statement is such a common pattern in Rust that the language provides the ? operator as shorthand for the whole thing. So, rather than writing out this logic explicitly every time we attempt something that could fail, you can use the following equivalent and much more legible statement:
let output = File::create(filename)?;
If File::create fails, the ? operator returns from write_image, passing along the error. Otherwise, output holds the successfully opened File.


