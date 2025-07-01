# GenAI Prompt Evaluation Tests

This repository is designed to evolve as a comprehensive suite for evaluating and comparing different Generative AI (GenAI) models and prompt engineering strategies. The goal is to provide a structured, repeatable framework for testing, benchmarking, and documenting which GenAI models perform best for specific use cases.

## Features
- **Prompt Evaluation**: Test and compare GenAI models using a variety of prompts and scenarios.
- **Automated Testing**: Uses `pytest` for automated test execution and reporting.
- **CI Integration**: GitHub Actions workflow runs tests on every push and pull request to the `master` branch.
- **Extensible**: Easily add new test cases, models, and evaluation metrics as the field evolves.

## Directory Structure
```
prompt_tests/
    prompt_eval.ipynb         # Jupyter notebook for interactive prompt evaluation
    prompt_eval.py           # Core evaluation logic
    test_prompt_eval.py      # Pytest-based test cases
    requirements.txt         # Python dependencies
```

## Getting Started
1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install -r prompt_tests/requirements.txt
   ```
3. **Run tests**:
   ```bash
   pytest prompt_tests/
   ```

## Continuous Integration
- The repository uses GitHub Actions (`python-app.yml`) to automatically run all tests on every push and pull request to the `master` branch.

## Contributing
- Add new test scenarios to `test_prompt_eval.py`.
- Update or add new evaluation logic in `prompt_eval.py`.
- Document new use cases and findings in the README as the project evolves.

## Vision
This project aims to become a living benchmark and knowledge base for GenAI prompt engineering, helping practitioners choose the best model and approach for their specific needs.

---
Feel free to open issues or submit pull requests with new test scenarios, models, or evaluation ideas!
