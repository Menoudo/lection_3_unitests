TEST_FILES=$(wildcard test_*.py)

RUN_TESTS=python -m unittest

.PHONY: all test clean

all: test

test:
 @$(RUN_TESTS) $(TEST_FILES)

clean:
 @find . -name '*.pyc' -delete
 @find . -name 'pycache' -delete

