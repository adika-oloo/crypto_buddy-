# CryptoBuddy Chatbot
print(" Hi, I'm CryptoBuddy! Your friendly crypto advisor bot.")
print("Ask me anything about sustainable or trending cryptocurrencies. (Type 'exit' to quit)\n")

# Sample crypto database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# Helper function to recommend based on sustainability
def get_most_sustainable():
    return max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])

# Helper function to recommend based on profitability
def get_best_for_growth():
    candidates = [
        name for name, data in crypto_db.items()
        if data["price_trend"] == "rising" and data["market_cap"] == "high"
    ]
    return candidates[0] if candidates else "No strong growth candidates right now."

# Start chatbot loop
while True:
    user_query = input("You: ").lower()

    if user_query in ["exit", "quit", "bye"]:
        print("CryptoBuddy: Goodbye! 🚀 Remember to do your own research!")
        break

    elif "sustainable" in user_query or "eco" in user_query or "green" in user_query:
        best = get_most_sustainable()
        print(f"CryptoBuddy: Go for {best}! 🌱 It’s eco-friendly with a strong sustainability score of {crypto_db[best]['sustainability_score']}/10.")

    elif "trending" in user_query or "growing" in user_query or "profit" in user_query or "long-term" in user_query:
        best = get_best_for_growth()
        if best != "No strong growth candidates right now.":
            print(f"CryptoBuddy: {best} is trending up 📈 and has a high market cap! Looks promising for long-term growth.")
        else:
            print("CryptoBuddy: Hmm, I don’t see any ideal growth options right now. Let’s check again later.")

    elif "cardano" in user_query:
        print("CryptoBuddy: Cardano (ADA) is known for sustainability and energy efficiency. 🔋")

    elif "bitcoin" in user_query:
        print("CryptoBuddy: Bitcoin is the most popular but uses a lot of energy ⚡ and has a lower sustainability score.")

    elif "ethereum" in user_query:
        print("CryptoBuddy: Ethereum is transitioning to more eco-friendly operations. It’s stable with high market cap.")

    else:
        print("CryptoBuddy: I’m still learning! Try asking about trending, sustainable, or specific coins like Bitcoin, Ethereum, or Cardano.")

# Disclaimer
print("\n Disclaimer: This chatbot is for educational purposes only. Crypto is risky—always do your own research before investing.")

