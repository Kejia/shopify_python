# Shopify Python Standards

This repository describes Python development standards at Shopify, and provides some utilities to assist other
Python repositories adhere to these standards.

## Development Principles
- Make sure your code is readable.
- Don't hesitate to refactor code where it improves the design.
- Don't take shortcuts; development is more like a marathon than a sprint.
- And leave the code cleaner than you found it.

## Python Style

Shopify follows the [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html) with the following
exceptions:
- Line Length: The maximum line length is 120 columns.
- Private Methods and Properties
  - Prefix class-private members and properties with double underscores. This invokes name-mangling, which provides some protection against violations of encapsulation.
  - Prefix module-private functions and variables with a single underscore.
- Multi-line docstrings: The first line of text (summary line) appears on the same line as the opening three double-quotes.

## Testing

All committed code requires quality tests that provide ample code coverage. Functionality that is not covered by tests
should be assumed to be broken (and probably will be).

## Code Review

Committing to `master` requires a code review, submitted in the form of a GitHub Pull Request. To be merged, a PR must
have an explicit approval from a core team member and no outstanding questions.


## Contributing

Please refer to our [Contribution Guidelines](CONTRIBUTING.md)