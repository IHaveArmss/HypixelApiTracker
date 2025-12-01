👾 HypixelApiTrackerA Python script designed to monitor specific Hypixel API endpoints for changes and notify users via a Discord webhook.
🛠️ SetupTo run this tracker, you need to set up your environment variables and install the necessary Python libraries.
📦 Prerequisites (Python Libraries)You can install the required libraries using 
pip:Bashpip install requests deepdiff
The script relies on the following packages:
requests: For making HTTP requests to the Mojang and Hypixel APIs.
deepdiff: For performing detailed comparisons between the previous and current API data.
🔑 Environment Variables (.env file)The script uses two crucial environment variables, which should be stored in a .env file in the project root (or otherwise loaded into your environment, depending on how you run the script):Variable NameDescriptionExample Value
HYPIXEL_API_KEYYour personal Hypixel API key.a0a0a0a0-b1b1-c2c2-d3d3-e4e4e4e4e4e4
WEBHOOK Your Discord webhook URL for sending change notifications.https://discord.com/api/webhooks/123456789/abcdefghijklmnopqrstuvwxy
🚀 ExecutionEnsure your .env variables are loaded into the environment where you run the script.
Run the main script:Bashpython fetchPush.py
⚙️ How It Works (At a Glance)The script retrieves the UUID for the hardcoded player "IHaveArms".
It continuously monitors the configured Hypixel endpoints .Every hour, it fetches the latest data and compares it against the previously saved JSON files (e.g., NewsData.json).If differences are detected, it overwrites the old file with the new data and sends a formatted notification message (including the changes) to the Discord webhook.If the files don't exist, it creates them for the first time.
