# Chatbot-sport
chatbot Ai for get answer for anything in sport

NBA ChatBot This project is a NBA chatbot that answers questions using your own game data and the OpenAI GPT model. It reads data from a CSV file and returns answers like game results or scores based on user questions.
| File Name               | Description                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------- |
| `main.py`               | The main script that loads the data, fetches game information, and interacts with the chatbot.                 |
| `data_loader.py`        | Loads NBA game data from a CSV file into a pandas DataFrame.                                                   |
| `chatbot.py`            | Sends the user question along with game context to OpenAI GPT and returns the response.                        |
| `.env`                  | Stores your OpenAI API key securely (not included in the repo).                                                |
| `Data/csv/nba_data.csv` | CSV file containing NBA game results with the following columns: `date`, `team1`, `team2`, `score1`, `score2`. |
