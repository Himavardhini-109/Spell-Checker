# Spell Checker Tool - AI NLP Project
A simple yet effective spell checking application built with Python using Tkinter for the GUI and TextBlob for natural language processing capabilities.

## 👨‍💻 Developer Information
- **Name**:O.Himavardhini
- **Roll No**:222T1A3140
- **Institution**:Ashoka Womens  Engineering College
  
## 🌟 Features

- **User-friendly GUI**: Clean and intuitive interface built with Tkinter
- **Real-time spell checking**: Instant correction suggestions using TextBlob's NLP capabilities
- **Error handling**: Validates user input and provides appropriate feedback
- **Lightweight**: Minimal dependencies and fast performance
- **Cross-platform**: Works on Windows, macOS, and Linux

## 🖼️ Screenshot

The application features a light pink background with a clean layout including:
- Title header with navy blue text on light blue background
- Input field for entering words
- Result display area showing corrections
- Check Spelling and Exit buttons

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed on your system. This project requires:

- Python 3.6 or higher
- tkinter (usually comes pre-installed with Python)
- textblob library

## 💻 How to Use

1. **Launch the application** by running the Python script
2. **Enter a word** in the input field (can include misspelled words)
3. **Click "Check Spelling"** to get the corrected version
4. **View the result** in the display area below
5. **Click "Exit"** to close the application

### Example Usage

- Input: `recieve` → Output: `The corrected word is: receive`
- Input: `occured` → Output: `The corrected word is: occurred`
- Input: `separate` → Output: `The corrected word is: separate` (already correct)

## 🏗️ Code Structure

```
spell-checker-tool/
│
├── spell_checker.py          # Main application file
├── README.md                 # Project documentation
└── requirements.txt          # Dependencies list
```

### Key Components

- **GUI Framework**: Tkinter for creating the user interface
- **NLP Engine**: TextBlob for spell checking and text correction
- **Event Handling**: Button clicks and input validation
- **Styling**: Custom colors and fonts for better user experience

## 🛠️ Technical Details

### Dependencies

- **tkinter**: Python's standard GUI toolkit
- **textblob**: Natural language processing library for spell checking

### Core Functions

- `checkSpelling()`: Main function that processes input and returns corrections
- Input validation to handle empty strings
- Error handling for edge cases

### GUI Elements

- **StringVar()**: For managing input and output text
- **Labels**: For titles, prompts, and result display
- **Entry**: For user input
- **Buttons**: For triggering spell check and exiting

## 🎨 Customization

You can easily customize the application by modifying:

- **Colors**: Change `bg` and `fg` parameters in the code
- **Fonts**: Modify font families and sizes
- **Window size**: Adjust the `geometry()` parameters
- **Additional features**: Add more TextBlob functionality like sentiment analysis
  ## 🙏 Acknowledgments

TextBlob: For providing excellent NLP capabilities
Python Tkinter: For the GUI framework
NLTK: Underlying natural language toolkit used by TextBlob



