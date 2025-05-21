from data_loader import load_all_nba_data
from chatbot import generate_response

def get_game_info(df, game_date):
    """
    Extracts game info from the dataframe based on the given date.
    :param df: The DataFrame containing NBA data.
    :param game_date: The date of the game.
    :return: A string with the game details.
    """
    game_info = df[df['date'] == game_date]

    if not game_info.empty:
        row = game_info.iloc[0]
        context = f"The game on {game_date} was between {row['team1']} and {row['team2']}. The score was {row['score1']} - {row['score2']}."
        return context
    else:
        return f"No game found on {game_date}."

def main():
    # Load the NBA data
    df = load_all_nba_data()

    if df is not None:
        print("Columns available:", df.columns)
        # Example question
        game_date = "2025-04-01"
        context = get_game_info(df, game_date)
        
        if "No game found" not in context:
            question = "What was the final score of the game?"
            chatbot_response = generate_response(question, context)
            print(chatbot_response)
        else:
            print(context)

if __name__ == "__main__":
    main()
