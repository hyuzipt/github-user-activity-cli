import sys
import requests

def get_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        event = response.json()
        recent_activity = event
        print(f"Recent activity of {username}:")
        for event in recent_activity:
            if event["type"] == "CommitCommentEvent":
                print(f"- Commented on commit {event["repo"]["name"]}")
            elif event["type"] == "CreateEvent":
                print(f"- Created {event["payload"]["ref_type"]} {event["payload"]["ref"]}")
            elif event["type"] == "DeleteEvent":
                print(f"- Deleted {event["payload"]["ref_type"]} {event["payload"]["ref"]}")
            elif event["type"] == "ForkEvent":
                print(f"- Forked {event["repo"]["name"]} to {event["payload"]["forkee"]["full_name"]}")
            elif event["type"] == "GollumEvent":
                print(f"- {event["payload"]["pages"]["action"]} wiki page {event["payload"]["pages"]["title"]} in {event["repo"]["name"]}")
            elif event["type"] == "IssueCommentEvent":
                print(f"- Commented on issue {event["payload"]["issue"]["number"]} in {event["repo"]["name"]}")
            elif event["type"] == "IssuesEvent":
                print(f"- Created issue {event["payload"]["issue"]["number"]} in {event["repo"]["name"]}")
            elif event["type"] == "MemberEvent":
                print(f"- {event["payload"]["action"]} member {event["payload"]["member"]["login"]} to {event["repo"]["name"]}")
            elif event["type"] == "PublicEvent":
                print(f"- Made {event["repo"]["name"]} public")
            elif event["type"] == "PullRequestEvent":
                print(f"- Created pull request {event["payload"]["pull_request"]["number"]} in {event["repo"]["name"]}")
            elif event["type"] == "PullRequestReviewEvent":
                print(f"- Reviewed pull request {event["payload"]["pull_request"]["number"]} in {event["repo"]["name"]}")
            elif event["type"] == "PullRequestReviewCommentEvent":
                print(f"- Commented on pull request {event["payload"]["pull_request"]["number"]} in {event["repo"]["name"]}")
            elif event["type"] == "PullRequestReviewThreadEvent":
                print(f"- {event["payload"]["action"]} a review thread in pull request {event["payload"]["pull_request"]["number"]} in {event["repo"]["name"]}")
            elif event["type"] == "PushEvent":
                print(f"- Pushed to {event["repo"]["name"]}")
            elif event["type"] == "ReleaseEvent":
                print(f"- {event['payload']['action']} release {event["payload"]["release"]["tag_name"]} in {event["repo"]["name"]}")
            elif event["type"] == "SponsorshipEvent":
                print(f"- {event['payload']['action']} sponsorship with {event["payload"]["sponsorship"]["sponsor"]["login"]}")
            elif event['type'] == 'WatchEvent':
                print(f"- Starred {event["repo"]["name"]}")
            else:
                print(f"- {event["type"]}")
    else:
        print(f"Error fetching recent activity for {username}: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_user_activity(sys.argv[1])
    else:
        print("Usage: python github-activity.py <username>")