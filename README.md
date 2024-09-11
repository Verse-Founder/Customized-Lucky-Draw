# Lucky Draw Software

A customizable and interactive lucky draw software designed for dynamic prize drawings. Easily configure window titles, text prompts, and background images. Supports Excel file imports for participant lists.

## Features

- **Customizable Titles and Texts:** Update the lucky draw window's title and text prompts.
- **Background Image Support:** Select and display custom background images.
- **Excel File Import:** Upload Excel files to manage participant lists.
- **Interactive Interface:** Start and stop the lucky draw with real-time updates.

## Requirements

- **Python 3.6+**
- **Pandas**
- **Pillow (PIL)**
- **Tkinter** (included with Python standard library)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Verse-Founder/Customized-Lucky-Draw.git
    cd Customized-Lucky-Draw
    ```

2. Install the required Python packages:
    ```sh
    pip install pandas pillow
    ```

## Usage

1. Run the application:
    ```sh
    python Lucky_Draw_IBSS.py
    ```

2. In the settings window, configure:
    - **Title for Lucky Draw Window**
    - **Text Prompts** ("Are You Ready?", "Will You Be the Lucky One?", "Congratulations!" etc.)
    - **Background Image** (select an image file)

3. Upload an Excel file containing participants and select the desired column.

4. Start the lucky draw and view the results in the new window.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request on GitHub.


## Acknowledgments

- Thanks to [Pandas](https://pandas.pydata.org/) for data manipulation.
- Thanks to [Pillow](https://pillow.readthedocs.io/en/stable/) for image processing.
- Thanks to [Tkinter](https://docs.python.org/3/library/tkinter.html) for creating the GUI.
