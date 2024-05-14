# Fetching-stock-data
Fetching stock data from jugaad-data library and writing it into different file formats

# Introduction

The objective of this report is to provide insights into different file formats and the benchmarking methods employed to assess their performance. The code provided utilizes the jugaad-data library to fetch stock data and writes it to various file formats, including CSV, TXT, Parquet, and Binary. The benchmarking process aims to measure the time taken for writing each file format and the resulting file sizes.

## Code Overview

The Python script consists of the following components:

### 1. Data Retrieval

The script retrieves stock data using the `jugaad_data.nse` library, focusing on the equity series.

### 2. File Format Writing

The script writes the acquired stock data to different file formats using the `write_to_file` function. Supported formats include CSV, TXT (tab-separated), Parquet, and Binary (using pickle). 

- **Pandas Library**: Pandas is a powerful data manipulation and analysis library for Python. It provides data structures for efficiently storing and manipulating large datasets.

### 3. Benchmarking

For each file format, the script measures the time taken to write the data and the resulting file size. The benchmarks are stored in a dictionary for further analysis.

### 4. Graphical Representation

The script generates two bar graphs illustrating the time taken to write each file format and the corresponding file sizes by utilizing Matplotlib library.

- **Matplotlib Library**: Matplotlib is a 2D plotting library for Python that produces high-quality charts and graphs. It is widely used for data visualization in scientific computing and data analysis.

## Benchmarking Process

### Data Preparation

1. **Data Retrieval:**
    
    - The script fetches stock data using the `jugaad_data.nse` library, focusing on the equity series.
    - The relevant data columns are selected using the `stock_select_headers` list.
2. **File Format Writing:**
    
    - The script uses the `pandas` library to create a DataFrame from the fetched stock data.
    - The `write_to_file` function writes the DataFrame to various file formats: CSV, TXT, Parquet, and Binary (Pickle).

### Benchmarking

1. **Time Measurement:**
    
    - For each file format, the script measures the time taken to write the data using the `time` module.
    - A start time is recorded before writing the data, and an end time is recorded after the write operation is completed.
2. **File Size Measurement:**
    
    - The size of each generated file is calculated using the `os.path.getsize` method.
    - File sizes are reported in kilobytes (KB) for standardization.
3. **Benchmark Storage:**
    
    - Benchmark results are stored in a dictionary named `benchmarks`.
    - The dictionary structure is as follows: `{'Format': {'Time': elapsed_time, 'Size': file_size}}`

### Benchmark Results

The benchmark results include metrics for each file format:

- **Time:** Elapsed time in seconds for writing the data file.
- **Size:** Size of the generated data file in kilobytes (KB).


### Graphical Representation

1. **Bar Graphs:**
    
    - The script uses the `Matplotlib` library to create two bar graphs.
    - One graph illustrates the time taken to write each file format.
    - The other graph shows the resulting file sizes for each file format.
    
2. **Graph Saving:**
    
    - The generated bar graphs are saved as an image file (PNG) using `plt.savefig`.

3. **Graphical Representation:**
    
    - The bar graphs visually compare the performance of different file formats.

Example: 
`make SYMBOL=SBIN num_years=2`




## Makefile Integration

The project includes a Makefile to streamline the execution of tasks and manage dependencies. The Makefile contains the following targets:
### `all`

The default target (`all`) is used to run the `run` target by default. This ensures that executing `make` without specifying a target will trigger the execution of the Python script.
### `run`

The `run` target installs the required Python packages specified in `requirements.txt` using `pip`. After installing dependencies, it runs the main Python script (`main.py`) with the specified symbol (`SYMBOL`) and number of years (`num_years`) as command-line arguments. The default values are set to `SBIN` and `2`, respectively.

`make run`

To execute the code, use the command:

`make SYMBOL={$SYMBOL} num_years={$years}`
Example: `make SYMBOL=SBIN num_years=2`

### `clean`

The `clean` target is responsible for removing generated files, including CSV, TXT, Parquet, Binary, and PNG files. It helps in maintaining a clean project structure.

`make clean`



## Conclusion

In conclusion, the benchmarking process provides valuable insights into the performance characteristics of various file formats. The choice of file format depends on factors such as speed, file size, and compatibility with downstream applications. This report serves as a guide for making informed decisions when selecting a file format for storing financial data.
