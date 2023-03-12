# Find and Replace
The final touch for this program is to implement its actual functionality: finding and replacing. For this, we’ll use the regex crate, which compiles and executes regular expressions. It provides a struct called Regex, which represents a compiled regular expression. Regex has a method replace_all, which does exactly what it says: it searches a string for all matches of the regular expression and replaces each one with a given replacement string. We can pull this logic out into a function:


use regex::Regex;
fn replace(target: &str, replacement: &str, text: &str)
    -> Result<String, regex::Error>
{
    let regex = Regex::new(target)?;
    Ok(regex.replace_all(text, replacement).to_string())
}
The final touch for this program is to implement its actual functionality: finding and replacing. For this, we’ll use the regex crate, which compiles and executes regular expressions. It provides a struct called Regex, which represents a compiled regular expression. Regex has a method replace_all, which does exactly what it says: it searches a string for all matches of the regular expression and replaces each one with a given replacement string. We can pull this logic out into a function:


use regex::Regex;
fn replace(target: &str, replacement: &str, text: &str)
    -> Result<String, regex::Error>
{
    let regex = Regex::new(target)?;
    Ok(regex.replace_all(text, replacement).to_string())
}
Note the return type of this function. Just like the standard library functions we used earlier, replace returns a Result, this time with an error type provided by the regex crate.

Regex::new compiles the user-provided regex, and it can fail if given an invalid string. As in the Mandelbrot program, we use ? to short-circuit in case Regex::new fails, but in this case the function returns an error type specific to the regex crate. Once the regex is compiled, its replace_all method replaces any matches in text with the given replacement string.

If replace_all finds matches, it returns a new String with those matches replaced with the text we gave it. Otherwise, replace_all returns a pointer to the original text, avoiding unnecessary memory allocation and copying. In this case, however, we always want an independent copy, so we use the to_string method to get a String in either case and return that string wrapped in Result::Ok, as in the other functions.

