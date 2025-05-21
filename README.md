NBA ChatBot 
This project is a  NBA chatbot that answers questions using your own game data and the OpenAI GPT model. It reads data from a CSV file and returns answers like game results or scores based on user questions.

📁 Project Files Overview

| File Name               | Description                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `main.py`               | The main runner. It loads the data, gets game info, and asks the chatbot.                   |
| `data_loader.py`        | Loads NBA game data from a CSV file into a DataFrame.                                       |
| `chatbot.py`            | Sends a question + context to OpenAI and gets the response.                                 |
| `.env`                  | Stores your OpenAI API key securely.                                                        |
| `Data/csv/nba_data.csv` | The CSV file with game results. Must include: `date`, `team1`, `team2`, `score1`, `score2`. |




