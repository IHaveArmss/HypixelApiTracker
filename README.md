# 👾 HypixelApiTracker
A Python script designed to monitor specific **Hypixel API** endpoints for changes and automatically send formatted notifications to a **Discord webhook**.

---

## 🛠️ Setup

To run this tracker, you must configure your environment variables and install the required Python libraries.

---

## 📦 Prerequisites

Install all required Python packages using:

```bash
pip install requests deepdiff python-dotenv
```

The script uses:

- **requests** — for HTTP requests  
- **deepdiff** — for comparing old and new API data  
- **python-dotenv** — for loading environment variables from a `.env` file

---

## 🔑 Environment Variables (`.env`)

Create a `.env` file in the project root containing:

```
HYPIXEL_API_KEY=your_hypixel_api_key_here
WEBHOOK=your_discord_webhook_url_here
```

### Example

```
HYPIXEL_API_KEY=a0a0a0a0-b1b1-c2c2-d3d3-e4e4e4e4e4e4
WEBHOOK=https://discord.com/api/webhooks/123456789/abcdefghijklmnopqrstuvwxy
```

---

## 🚀 Running the Script

Make sure your `.env` variables are loaded, then run:

```bash
python fetchPush.py
```

---

## ⚙️ How It Works

1. The script retrieves the UUID of the hardcoded player **"IHaveArms"** using the Mojang API.  
2. It monitors selected Hypixel endpoints:
   - 📰 **Hypixel News**
   - 💰 **Bazaar Data**
3. Every hour it:
   - Fetches updated API data  
   - Compares it with the previously saved JSON files  
   - Detects differences using **DeepDiff**  
4. If changes are found:
   - The old JSON file is replaced  
   - A formatted change notification is sent to your **Discord webhook**  
5. If JSON files do not exist, they are generated on first run.

---

## 📁 Data Persistence

The tracker stores the last known API responses in local JSON files (e.g., `NewsData.json`) so it can compare differences between runs.

---

## 📨 Notifications

Detected changes are sent to your configured Discord webhook with a clean, human-readable summary of what changed.

---

## ⭐ Contributions

Feel free to open issues or submit pull requests to improve this project.
