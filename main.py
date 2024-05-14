from jugaad_data.nse import stock_raw
from datetime import date, timedelta, datetime
import pandas as pd
import time
import os
import matplotlib.pyplot as plt

stock_select_headers = ["CH_TIMESTAMP",
                        "CH_OPENING_PRICE",
                        "CH_CLOSING_PRICE",
                        "CH_TRADE_HIGH_PRICE",
                        "CH_TRADE_LOW_PRICE",
                        "CH_LAST_TRADED_PRICE",
                        "CH_TOT_TRADED_QTY",
                        "CH_TOT_TRADED_VAL",
                        "CH_TOTAL_TRADES"
                        ]
stock_final_headers = ["DATE",
                       "OPEN",
                       "CLOSE",
                       "HIGH",
                       "LOW",
                       "LTP",
                       "VOLUME",
                       "VALUE",
                       "NO OF TRADES"
                       ]



def stock_df(symbol, from_date, to_date, series="EQ"):
    if not pd:
        raise ModuleNotFoundError("Please install pandas using \n pip install pandas")
    raw = stock_raw(symbol, from_date, to_date, series)
    df = pd.DataFrame(raw)[stock_select_headers]
    df.columns = stock_final_headers
    return df


# Function to get stock data
def get_stock_data(symbol, years):
    # Calculate the start date by subtracting the given number of years from today
    to_date = pd.to_datetime('today')
    start_date = to_date - timedelta(days=365 * years)

    # Fetch data using jugaad-data library
    data = stock_df(symbol, from_date=start_date, to_date=to_date, series="EQ")
    return data


# Function to write data to different file formats
def write_to_file(data, symbol, file_format):
    filename = f'{symbol}.{file_format}'
    if file_format == 'csv':
        data.to_csv(filename, index=False)
    elif file_format == 'txt':
        data.to_csv(filename, sep='\t', index=False)
    elif file_format == 'parquet':
        data.to_parquet(filename, index=False)
    elif file_format == 'binary':
        data.to_pickle(filename)


# Main function
def main(symbol, years):


    # Get stock data
    stock_data = get_stock_data(symbol, years)

    # Benchmarking variable
    benchmarks = {}

    # Write data to different file formats

    # Benchmark CSV
    start = time.time()
    write_to_file(stock_data, symbol, 'csv')
    end = time.time()
    elapsed_time = end - start
    file_size = os.path.getsize(f'{symbol}.csv') / 1024  # Size in KB
    benchmarks['CSV'] = {'Time': elapsed_time, 'Size': file_size}

    # Benchmark txt
    start = time.time()
    write_to_file(stock_data, symbol, 'txt')
    end = time.time()
    elapsed_time = end - start
    file_size = os.path.getsize(f'{symbol}.txt') / 1024  # Size in KB
    benchmarks['TXT'] = {'Time': elapsed_time, 'Size': file_size}

    # Benchmark Parquet
    start_time = time.time()
    write_to_file(stock_data, symbol, 'parquet')
    end_time = time.time()
    elapsed_time = end_time - start_time
    file_size = os.path.getsize(f'{symbol}.parquet') / 1024  # Size in KB
    benchmarks['Parquet'] = {'Time': elapsed_time, 'Size': file_size}

    # Benchmark Binary
    start_time = time.time()
    write_to_file(stock_data, symbol, 'binary')
    end_time = time.time()
    elapsed_time = end_time - start_time
    file_size = os.path.getsize(f'{symbol}.binary') / 1024  # Size in KB
    benchmarks['Binary'] = {'Time': elapsed_time, 'Size': file_size}

    # Display benchmarks
    print("Benchmark results:")
    for format, result in benchmarks.items():
        print(f"{format}: Time = {result['Time']:.6f} seconds, Size = {result['Size']:.6f} KB")

    # Generate a bar graph
    file_formats = list(benchmarks.keys())
    time_taken = [result['Time'] for result in benchmarks.values()]
    file_sizes = [result['Size'] for result in benchmarks.values()]

    plt.figure(figsize=(10, 5))

    # Bar graph for time taken
    plt.subplot(1, 2, 1)
    plt.bar(file_formats, time_taken, color='blue', alpha=0.7)
    plt.title('Time Taken to Write File')
    plt.xlabel('File Format')
    plt.ylabel('Time (seconds)')

    # Bar graph for file size
    plt.subplot(1, 2, 2)
    plt.bar(file_formats, file_sizes, color='orange', alpha=0.7)
    plt.title('File Size After Writing')
    plt.xlabel('File Format')
    plt.ylabel('Size (KB)')

    plt.tight_layout()
    plt.savefig(f'{symbol}.png')


if __name__ == '__main__':
    import sys

    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python your_script.py <symbol> <num_years>")
        sys.exit(1)

    # Get command line arguments
    symbol_arg = sys.argv[1]
    num_years_arg = int(sys.argv[2])

    # Call the main function with command line arguments
    main(symbol_arg, num_years_arg)
