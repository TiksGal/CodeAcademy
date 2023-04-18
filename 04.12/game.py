import requests
from bs4 import BeautifulSoup
import random

def get_quotes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes_data = soup.find_all(class_="quote")
    quotes = []
    
    for quote in quotes_data:
        quote_text = quote.find(class_="text").get_text()
        author = quote.find(class_="author").get_text()
        author_bio_url = quote.find("a")["href"]
        
        quotes.append({"quote": quote_text, "author": author, "bio_url": author_bio_url})
    
    return quotes

def get_author_hint(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    birth_date = soup.find(class_="author-born-date").get_text()
    birth_place = soup.find(class_="author-born-location").get_text()
    
    return birth_date, birth_place

def play_game(quotes):
    quote = random.choice(quotes)
    print("\nHere's a quote:\n")
    print(quote["quote"])
    
    guesses = 3
    while guesses > 0:
        guess = input("\nWho said this? ")
        if guess.lower() == quote["author"].lower():
            print("\nCongratulations! You guessed it right!")
            break
        else:
            guesses -= 1
            if guesses == 2:
                hint_url = f'http://quotes.toscrape.com{quote["bio_url"]}'
                birth_date, birth_place = get_author_hint(hint_url)
                print(f"\nWrong guess! Here's a hint: The author was born on {birth_date} in {birth_place}.")
            elif guesses == 1:
                initials = " ".join([name[0] for name in quote["author"].split()])
                print(f"\nStill wrong! Here's another hint: The author's initials are {initials}.")
            else:
                print(f"\nSorry, you're out of guesses. The answer is: {quote['author']}")

    play_again = input("\nWould you like to play again? (y/n) ")
    if play_again.lower() == "y":
        play_game(quotes)

if __name__ == "__main__":
    quotes_url = "http://quotes.toscrape.com"
    quotes = get_quotes(quotes_url)
    play_game(quotes)
