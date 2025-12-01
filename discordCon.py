import os
from requests import post
WEBHOOK = os.environ.get("WEBHOOK")
USER_ID = "706955959066689627"


def send_update(header,diff_data):
    if not WEBHOOK:
        print("Error: NO WEBHOOK how??")
        return

    if len(diff_data) >4000:
        diff_data = diff_data[:4000] + "\n"

    data = {

        "content" : f"<@{USER_ID}> Changes detected in ```{header}``` ",
        "embeds": [
            {
                "title": f"Update Found : {header}",
                "description": f"```{diff_data}\n``` ",
                "color" : 65280,
                "footer" : {
                    "text" : "Hypixel Api Tracker"
                }
            }
        ]
    }

    try:
        response = post(WEBHOOK, json=data)
        if response.status_code not in [200,204]:
            print(f"Failed to send webhook: {response.status_code}")
    except Exception as error:
        print(f"Error sending webhook: {error}")