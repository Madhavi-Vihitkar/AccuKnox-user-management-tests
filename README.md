# AccuKnox-user-management-tests
This is repo is for task given by AccuKnox-user-management-tests

# AccuKnox-user-management-tests
Playwright (Python) E2E tests for OrangeHRM User Management module.


## Requirements
- Python 3.8+
- Playwright (see requirements.txt)


## Setup
1. Clone repo
2. python -m venv .venv
3. source .venv/bin/activate # or .venv\Scripts\activate on Windows
4. pip install -r requirements.txt
5. python -m playwright install


## Run tests
- Run all tests (headed):
pytest
- Run single test file:
pytest tests/test_user_management.py -q


## Playwright version used
- Playwright for Python **1.55.0** (tested while authoring these files). See the Playwright docs.


## Notes
- Update selectors in `page_objects/user_page.py` to match your OrangeHRM DOM.
- Use a real `employee` value that exists in the HRM system.
