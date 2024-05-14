# Variables
PYTHON = python3
SCRIPT = main.py
SYMBOL?=SBIN
num_years?=2

# Default target
all:run

# Target to run the Python script
run:
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) $(SCRIPT) $(SYMBOL) $(num_years)

# Target to clean generated files
clean:
	find . \( -name '*.csv' -o -name '*.txt' -o -name '*.parquet' -o -name '*.binary' -o -name '*.png' \) ! -name 'requirements.txt' -exec rm {} +
	
.PHONY: run clean

