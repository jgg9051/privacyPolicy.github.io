import requests
import json

# --- Configuration ---
PAGE_ACCESS_TOKEN = "EAAjXGqWf478BO8L1ZCJTwzbZCcI4ri64YoI1Y4sYasqZBwBBZAgFQSW4aMcTZArrEma4Kf3dzFaigEn814BAN0zLREhJ61HZBLFC2RVDRZAhZCUSJMYWlP0ZAcMMOFC84o072Ta6sIGUw1NVwbslOKKU23cKd9578lMe8StELqvZC9MZAr5wNkFcN8sjFzTaU2fNiu63iaZCRdlIqxIZB1YvyokXJgm5TZAEJDF9h48foaCAqC"  # Replace with your Page Access Token
IG_USER_ID = "17841475316430493"  # Instagram Business Account ID
USERNAME = "sociableuta"           # IG username to inspect

# --- Function to Get Instagram Business Discovery Info ---
def get_business_insights(ig_user_id, username, access_token):
    fields = f"business_discovery.username({USERNAME}){{followers_count,media_count,profile_picture_url,name}}"
    url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}?fields={fields}&access_token={PAGE_ACCESS_TOKEN}"


    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        business_data = data.get("business_discovery")
        if business_data:
            return {
                "name": business_data.get("name"),
                "followers": business_data.get("followers_count"),
                "posts": business_data.get("media_count"),
                "profile_picture": business_data.get("profile_picture_url")
            }
        else:
            print("⚠️ 'business_discovery' not found in response.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# --- Run Script ---
if __name__ == "__main__":
    insights = get_business_insights(IG_USER_ID, USERNAME, PAGE_ACCESS_TOKEN)

    if insights:
        print("\n📊 Instagram Business Insights:")
        print(f"Name: {insights['name']}")
        print(f"Followers: {insights['followers']}")
        print(f"Posts: {insights['posts']}")
        print(f"Profile Pic: {insights['profile_picture']}")
