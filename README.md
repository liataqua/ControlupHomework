# Automation Project - Metric Conversions and Weather Comparison

## Overview
This project involves creating automation tests for two parts:
1. Part 1:**Metric Conversions** using Selenium in Python.
2. Part 2:**Weather Comparison** between data fetched using Selenium and an API.

The purpose of the project is to practice test automation with Selenium for web applications and to work with APIs for data comparison.

## Requirements

- Python 3.x
- Selenium WebDriver
- Pytest
- WebDriver for your browser (e.g., ChromeDriver)
- Requests library (for API requests)

## How to run
To run all the tests in the project:
pytest

To run only the tests for Part 1 (Metric Conversions):
pytest -m part1

To run only the tests for Part 2 (Weather Comparison):
pytest -m part2

To run a specific test, specify the path to the test file:
pytest path_to_your_test_file.py

Notes:
Ensure that you have the WebDriver for your browser installed (e.g., ChromeDriver).




