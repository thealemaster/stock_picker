# stock_picker
Coding exercise for work

type "make test" to run the tests and see the output.

I decided to try to learn a few things about Python by doing a code exercise with some people
at work. It's also my intent to do some TDD along with it to learn more about Python's testing
capabilities. You'll need Python and Make installed in your command line environment (I used
MacOS and installed everything with homebrew).

My understanding of the user stories for this exercise are:
- As a stock trader, I want to buy a stock at it's lowest price low and sell a stock at it's highest
  price so that I can maximize profit.
- As a stock trader, I want to see an error returned if there is no solution to making a profit.

Do I really need a Makefile? No, I don't. I just wanted a convenient way (personal preference) to
run tests from the command line.

You can see from the commit history that I originally went down the path of using min and max
from Python's library. That was working great, until it wasn't :) Refactored to use a loop instead
and all tests continued to pass. I left in the simple case of min and max to save some CPU cycles
iterating through a loop. That code could just as easily be removed. I also threw in a test for the
edge case of all the values in the list being equal just for fun.

And why did I use command line editors instead of using an IDE like Visual Studio Code?
Because IDEs are for kids :)
