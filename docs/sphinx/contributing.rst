Contributing
============

Contributions are welcome! This document provides guidelines for contributing to CaPybara.

Getting Started
---------------

1. Fork the repository
2. Clone your fork: ``git clone https://github.com/yourusername/capybara.git``
3. Create a branch: ``git checkout -b feature/your-feature-name``
4. Install development dependencies: ``pip install -e ".[dev]"``

Development Setup
-----------------

.. code-block:: bash

   # Install in development mode
   pip install -e ".[dev]"

   # Run tests
   pytest

   # Run linting
   ruff check src/
   black --check src/

   # Type checking
   mypy src/

Code Style
----------

* Follow PEP 8 style guidelines
* Use type hints for all function signatures
* Write docstrings in Google style
* Keep line length to 100 characters
* Use black for code formatting

Testing
-------

* Write tests for all new features
* Aim for high test coverage
* Use pytest for testing
* Place tests in the ``tests/`` directory

Documentation
-------------

* Update documentation for all new features
* Add examples where appropriate
* Keep docstrings up to date
* Follow the existing documentation style

Pull Request Process
--------------------

1. Ensure all tests pass
2. Ensure code passes linting and type checking
3. Update documentation as needed
4. Submit a pull request with a clear description
5. Respond to review feedback

License
-------

By contributing, you agree that your contributions will be licensed under the MIT License.
