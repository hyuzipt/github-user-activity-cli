# GitHub User Activity CLI

This app fetches the recent activity of a GitHub user and displays them in the terminal using a simple CLI. It provides a way to view recent activities such as pushes, pull requests, issues, comments, and more using the GitHub API.

## Features

- Fetches recent GitHub events for a specified user.
- Supports various event types like `PushEvent`, `IssuesEvent`, `PullRequestEvent`, `ReleaseEvent`, and more.

## Prerequisites

- Python 3.7 or higher

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/hyuzipt/github-user-activity-cli.git
    cd github-user-activity-cli
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To fetch and display the latest events for a specific GitHub user, use the following command:

```bash
python github-activity.py <username>
```

https://roadmap.sh/projects/github-user-activity
