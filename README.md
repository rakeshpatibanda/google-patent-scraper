# Google Patents Scraper

## Overview

Google Patents Scraper is a Python-based tool with a user-friendly GUI that allows users to search and download patent documents from Google Patents. This tool is designed to simplify the process of patent research and data collection for researchers, inventors, and intellectual property professionals.

## Features

- **User-friendly GUI**: Easy-to-use interface built with PyQt5.
- **Flexible Search**: Enter custom search terms to find relevant patents.
- **Bulk Download**: Download multiple patent documents in one go.
- **Family Patents**: Option to include or exclude family patents in the download.
- **Proxy Support**: Set up proxies to avoid IP blocking by Google Patents.
- **Progress Tracking**: Visual progress bar for download status.
- **Logging**: Detailed logs of the scraping process.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/rakeshpatibanda/google-patent-scraper.git
   ```
2. Navigate to the project directory:
   ```
   cd google-patent-scraper
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. cd to the src folder and run the main script:
   ```
   python main.py
   ```
2. Use the GUI to:
   - Set the output directory for downloaded patents
   - Enter search terms
   - Choose download options (include family patents or not)
   - Start the search and download process

## Example

Here's a step-by-step example of how to use the Google Patents Scraper:

1. Launch the application by running `python main.py`.

2. In the GUI, set your desired output directory, e.g., `C:\Users\YourName\Documents\Patents`.

3. Enter your search terms in the search box. For example, to find patents related to artificial intelligence in healthcare, you might enter:
   ```
   artificial intelligence AND healthcare
   ```

4. Choose whether to include family patents by checking or unchecking the appropriate box.

5. Click the "Start Search" button to begin the process.

6. The tool will start searching for patents matching your criteria. You'll see the progress in the status bar.

7. Once complete, you'll find the downloaded patent documents in your specified output directory. Each patent will be saved as a separate PDF file, named with its patent number.

8. Check the log file in the output directory for details about the scraping process, including any errors or warnings.

Note: The number of patents downloaded and the time taken will depend on your search terms and the options selected. For broad searches, consider using more specific terms to narrow down the results.

## Technical Details

### Architecture

The Google Patents Scraper is built using a modular architecture:

1. **GUI Layer** (`gui.py`): Handles the user interface using PyQt5.
2. **Scraper Core** (`scraper.py`): Contains the main logic for searching and downloading patents.
3. **Proxy Handler** (`proxy_handler.py`): Manages proxy connections to avoid IP blocking.
4. **Utilities** (`utils.py`): Contains helper functions used across the application.

### Dependencies

The main dependencies for this project are:

- PyQt5: For the graphical user interface
- Requests: For making HTTP requests to Google Patents
- BeautifulSoup4: For parsing HTML content
- PyPDF2: For handling PDF operations

All dependencies are listed in the `requirements.txt` file.

### Configurable Parameters

Several parameters can be adjusted to modify the scraper's behavior:

1. **Search Result Limit**: 
   - File: `scraper.py`
   - Variable: `MAX_RESULTS`
   - Default: 200
   - To change: Modify the value of `MAX_RESULTS` to your desired limit.

2. **Request Timeout**:
   - File: `scraper.py`
   - Variable: `REQUEST_TIMEOUT`
   - Default: 30 seconds
   - To change: Adjust the value of `REQUEST_TIMEOUT` (in seconds).

3. **Proxy Rotation Interval**:
   - File: `proxy_handler.py`
   - Variable: `ROTATION_INTERVAL`
   - Default: 50 requests
   - To change: Modify the value of `ROTATION_INTERVAL` to rotate proxies more or less frequently.

4. **Log File Name**:
   - File: `utils.py`
   - Variable: `LOG_FILE_NAME`
   - Default: 'scraper_log.txt'
   - To change: Update the value of `LOG_FILE_NAME` to your preferred log file name.

### Extending the Scraper

To add new features or modify existing functionality:

1. GUI modifications: Update `gui.py` to add new interface elements or change existing ones.
2. Scraping logic changes: Modify `scraper.py` to adjust how patents are searched and downloaded.
3. Proxy handling: Update `proxy_handler.py` to change how proxies are managed and rotated.
4. Utility functions: Add or modify helper functions in `utils.py` as needed.

Remember to update the `requirements.txt` file if you add any new dependencies.

## Contributing

Contributions to improve Google Patents Scraper are welcome. Please feel free to submit a Pull Request.

## License

MIT

## Disclaimer

This tool is for research purposes only. Please ensure you comply with Google Patents' terms of service when using this scraper.