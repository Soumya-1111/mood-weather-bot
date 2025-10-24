# Mood-Based Weather Bot 🌦️

def mood_weather_bot():
    print("🌤️ Welcome to the Mood-Based Weather Bot!, I hope you're doing well!")
    print("Tell me how you're feeling today (happy, joyful, sad, depressed, angry, tired, excited, etc.)")
    print("Type 'exit' anytime to stop.\n")

    while True:
        mood = input("💭 Your mood: ").lower()

        if mood == "exit":
            print("☀️ Thanks for chatting! May your day stay bright!")
            break

        elif mood in ["happy", "joyful", "cheerful", "great"]:
            print("🌞 It's a bright, sunny day — just like your mood!\n")

        elif mood in ["sad", "upset", "down", "depressed"]:
            print("🌧️ Looks like a rainy day... but remember, rain brings new life!\n")

        elif mood in ["angry", "frustrated", "mad"]:
            print("🌩️ Thunderstorms ahead! Take a deep breath and let the clouds clear.\n")

        elif mood in ["tired", "sleepy", "lazy"]:
            print("🌙 It's a calm, starry night — perfect time to rest.\n")

        elif mood in ["excited", "energetic", "thrilled"]:
            print("🌈 A rainbow just appeared! The world’s full of possibilities today!\n")

        else:
            print("🌤️ Hmm… can’t find that mood in my forecast, but I hope your skies stay clear!\n")


# To run the bot
mood_weather_bot()
