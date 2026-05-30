import requests

# -------------------------------------------------------------
# API Configuration (Replace with your actual API keys)
# -------------------------------------------------------------
# For live weather data, sign up for a free account at openweathermap.org
WEATHER_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY" 
# For Generative AI capabilities, insert your OpenAI API key here
AI_API_KEY = "YOUR_OPENAI_API_KEY"

def get_weather_data(city):
    """Fetches real-time weather information for the specified city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Extracting required data from the nested dictionary to showcase data structure skills
            weather_info = {
                "temp": data["main"]["temp"],
                "condition": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }
            return weather_info
        else:
            return None
    except Exception:
        # Graceful error handling prevents application crashes during network issues
        return None

def generate_ai_itinerary(city, days, budget, weather_info):
    """Generates a smart travel itinerary based on user input and weather conditions."""
    
    print("\n" + "="*40)
    print(f"🤖 AI TRAVEL BUDDY - {city.upper()} TRIP PLAN")
    print("="*40)
    
    if weather_info:
        print(f"🌤️ Current Weather: {weather_info['temp']}°C, {weather_info['condition'].title()}")
        print(f"💧 Humidity: {weather_info['humidity']}%")
    else:
        print("⚠️ Live weather data unavailable (Please check your API Key).")
    
    print(f"💰 Budget Category: {budget.title()}")
    print(f"📅 Trip Duration: {days} Days")
    print("-"*40)
    
    # Python dictionary holding distinct arrays for smart conditional logic mapping
    itinerary = {
        "low": [
            "Morning: Visit local free parks and historical landmarks.",
            "Afternoon: Try popular street food and explore the local markets.",
            "Evening: Watch the sunset from a public viewpoint or lakeside."
        ],
        "medium": [
            "Morning: Visit city museums or popular art galleries (ticketed).",
            "Afternoon: Enjoy lunch at a highly-rated traditional restaurant.",
            "Evening: Take a guided walking tour or a scenic river cruise."
        ],
        "luxury": [
            "Morning: Hire a private cab to visit premium resorts or exclusive spots.",
            "Afternoon: Fine dining experience at a Michelin-star or luxury restaurant.",
            "Evening: Relax at an exclusive rooftop lounge or attend a premium theater show."
        ]
    }
    
    # Dynamic AI recommendation logic adapting directly to real-time weather data
    if weather_info and "rain" in weather_info['condition'].lower():
        print("🌧️ AI Weather Advisory: Rain is predicted today! Opting for indoor activities (Museums, Cafes).\n")
    
    # Loop execution to dynamically map and print day-by-day activities
    activities = itinerary.get(budget.lower(), itinerary["medium"])
    for day in range(1, int(days) + 1):
        print(f"📌 Day {day}:")
        for activity in activities:
            print(f"   - {activity}")
        print()
    
    print("="*40)
    print("✨ Have a safe and wonderful journey! ✨")

def main():
    print("🌐 Welcome to AI-Powered Smart Travel Buddy! 🌐")
    print("------------------------------------------------")
    
    # Capturing user choices via mobile-friendly console inputs
    city = input("✈️ Enter the city you want to visit (e.g., London, Paris): ").strip()
    if not city:
        print("City name cannot be empty!")
        return
        
    days = input("📅 Enter duration of stay (1-5 days): ").strip()
    budget = input("💰 Select your budget preference (Low / Medium / Luxury): ").strip().lower()
    
    if budget not in ["low", "medium", "luxury"]:
        budget = "medium"  # Default fallback budget setting
        
    print("\n🔄 Analyzing real-time data and crafting your perfect itinerary...")
    
    # Executing external network request to pull active weather status
    weather = get_weather_data(city)
    
    # Rendering final tailored travel itinerary pipeline
    generate_ai_itinerary(city, days, budget, weather)

if __name__ == "__main__":
    main()
