cd C:\Users\prate\PycharmProjects\nopcommerceApp
pytest -v -s -m "regression"  --html=./Reports/RegressionReportChrome.html  testCases/ --browser_name chrome
pytest -v -s -m "sanity"  --html=./Reports/SanityReportFirefox.html  testCases/ --browser_name firefox