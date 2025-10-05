# AstroMaps

AstroMaps is an interactive web application that lets you explore the night sky, including stars, planets, and constellations. 
You can search for celestial objects, view them in a visual map, and learn detailed information about each one.

## Overview

AstroMaps allows users to:
- View textures of planets and stars.
- Explore constellations and celestial bodies in a visual interface.
- Search for planets, stars, or constellations by name.
- Learn facts and information about each object.
- Interact through an AI-powered assistant for astronomy-related questions.

## Features

- 3D celestial visualization with realistic planet textures.
- Search functionality for quick navigation.
- AI chat integration through `gemini_chat_api_cors.py`.
- Textures for all major planets and stars.
- Runs entirely in the browser.

## Project Structure

```
AstroMaps-main/
│
├── astromaps_FINAL.html        # Main front-end application
├── gemini_chat_api_cors.py     # Backend AI chat integration
├── Textures/                   # Planet and star images
│   ├── earth.jpg
│   ├── jupiter.jpg
│   ├── mars.jpg
│   ├── mercury.jpg
│   ├── neptune.jpg
│   ├── saturn.jpg
│   ├── stars.jpg
│   ├── sun.jpg
│   ├── uranus.jpg
│   └── venus.jpg
└── README.md                   # Project documentation
```

## How to Run

1. Clone or download this repository:
   ```bash
   git clone https://github.com/yourusername/AstroMaps.git
   cd AstroMaps-main
   ```

2. Run the front-end by opening `astromaps_FINAL.html` in your browser.

3. (Optional) To enable the AI assistant:
   - Run the backend script:
     ```bash
     python gemini_chat_api_cors.py
     ```
   - Make sure your API key and CORS configuration are correctly set up.

## Technologies Used

- HTML5 / CSS3 / JavaScript
- Python 3
- Google Gemini API (for AI integration)
- WebGL / Three.js (if implemented)
- Custom planetary textures

## Future Improvements

- Add constellations overlay and sky navigation.
- Integrate real-time astronomy data (e.g., NASA APIs).
- Improve mobile responsiveness.
- Expand AI astronomy knowledge base.

## License

This project is released under the MIT License. 
You may use, modify, and distribute it with attribution.

## Author

Developed with curiosity and passion for astronomy.
