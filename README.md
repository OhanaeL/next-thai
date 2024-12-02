# Next Thai - AI-Powered Travel Planner

## Overview
Next Thai is an AI-powered travel planning application that helps users create personalized itineraries for their trips across Thailand. By simply inputting a starting point, desired destinations, trip type, and budget, users can receive customized travel plans generated by an AI model. The application leverages Google's generative AI to create detailed itineraries while considering the user's time and budget constraints.

### Key Features:
- **Customizable Travel Plans**: Select your starting point, destination(s), and trip type, and set your budget and travel dates.
- **AI-Powered Itinerary Generation**: Get personalized travel plans with recommendations on activities, transportation, and accommodations.
- **Budget Constraints**: The AI ensures the travel plan stays within your budget and time range.
- **Multi-Destination Planning**: Visit multiple destinations within Thailand in a single trip.
- **Downloadable Itinerary**: Once the plan is generated, download it for future reference.
- **Dark and Light Themes**: Customize the app’s visual appearance with the theme of your choice.

## Technologies Used
- **Streamlit**: For creating the web application interface.
- **Google Gemini AI**: For generating the travel itineraries based on the user's input.
- **Datetime**: For handling date inputs and calculating the duration of the trip.
- **Python**: The main programming language used for the application logic.

## Installation

### 1. **Clone the repository**:
   ```bash
   git clone https://github.com/OhanaeL/next-thai.git
   cd next-thai
```

### 2. Interact with the app:
- **Starting Point**: Choose your starting location in Thailand.
- **Destinations**: Select one or more destinations you want to visit.
- **Duration**: Specify your trip’s duration by selecting start and end dates.
- **People**: Define how many people will be traveling.
- **Total Cost**: Set your budget per person.
- **Trip Type**: Select the types of experiences you’re interested in (e.g., adventure, beach vacation, cultural tour, etc.).

### 3. Generate the Itinerary:
- After filling out the details, click the "Generate" button.
- The AI will process the information and provide a detailed itinerary.
- You can download the plan by clicking the "Download Plan" button once the itinerary is ready.

### 4. Change Theme:
- Toggle between dark and light themes for a personalized experience.

## Project Structure

- `app.py`: Main script that powers the Streamlit app.
- `images/`: Folder containing the images used in the app (e.g., logo or icons).
- `requirements.txt`: List of required Python libraries for the project.
- `README.md`: This file.

## Contributions

Feel free to fork the repository, make changes, and submit pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
