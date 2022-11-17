The code in what_is_year_now.py implements tests for the what_is_year_now function using to replace real cases to API. To run the code, enter in the console:
'''
python -m pytest -v what_is_year_now.py
'''
If you want to check test coverage, firstly, you shoul install the package:
'''
pip install -U pytest-cov
'''
After that write in console:
'''
python -m pytest -q what_is_year_now.py --cov
'''
You can save the coverage report to an html file by typing:
'''
python -m pytest -q what_is_year_now.py --cov . --cov-report html
'''
Veiw results in results.txt and coverage report in htmlcov