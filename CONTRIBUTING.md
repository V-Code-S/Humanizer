# Contributing to Humanizer

Thank you for your interest in contributing to the AI Text to Human Text Converter project!

## Code of Conduct

This project is committed to providing a welcoming and inspiring community. All contributors are expected to uphold this code of conduct.

## How to Contribute

### Reporting Bugs

Before creating bug reports, check the issue list to ensure the problem hasn't already been reported. When creating a bug report, include:

- **Clear description** of what the bug is
- **Steps to reproduce** the behavior
- **Expected behavior**
- **Screenshots** if applicable
- **Your environment** (OS, Python version, Node version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description** of the suggested enhancement
- **Why this enhancement would be useful**
- **Possible implementation** if you have ideas
- **Alternative solutions** you've considered

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

#### Pull Request Guidelines

- Update the README with any new features or changes
- Follow the existing code style
- Include appropriate test cases
- Update documentation as needed
- Ensure all tests pass

## Development Setup

### Backend Development

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

### Frontend Development

```bash
cd frontend
npm install
npm run dev
```

## Testing

### Backend Tests

```bash
cd backend
pip install pytest pytest-httpx
pytest
```

### Frontend Tests

```bash
cd frontend
npm run test
npm run lint
```

## Code Style

### Python (Backend)

- Follow PEP 8
- Use 4 spaces for indentation
- Use meaningful variable and function names
- Add docstrings to functions and classes

### JavaScript/React (Frontend)

- Follow the Airbnb JavaScript style guide
- Use 2 spaces for indentation
- Use meaningful component and variable names
- Add comments for complex logic

## Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Start with a capital letter
- Reference issues and pull requests liberally after the first line

Example:
```
Add humanization engine with sentence variation

- Implement sentence combining
- Add transition phrases
- Improve text burstiness
Fixes #123
```

## License

By contributing, you agree that your contributions will be licensed under its MIT License.

## Questions?

Feel free to open an issue with the `question` label or reach out to the maintainers.

---

Happy coding! 🚀
