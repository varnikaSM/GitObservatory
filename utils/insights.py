import pandas as pd


def generate_insights(df: pd.DataFrame):

    repo1 = df.iloc[0]
    repo2 = df.iloc[1]

    insights = []

    winner = (
        repo1 if repo1["overall_repository_score"] >= repo2["overall_repository_score"]
        else repo2
    )

    insights.append({
        "title": "Overall Recommendation",
        "message":
            f"{winner['repo_full_name']} achieved the highest overall repository score "
            f"({winner['overall_repository_score']:.2f})."
    })

    if repo1["merge_rate"] > repo2["merge_rate"]:
        better = repo1
        worse = repo2
    else:
        better = repo2
        worse = repo1

    insights.append({
        "title": "Merge Efficiency",
        "message":
            f"{better['repo_full_name']} merges "
            f"{better['merge_rate']-worse['merge_rate']:.1f}% more pull requests."
    })

    if repo1["workflow_success_rate"] > repo2["workflow_success_rate"]:
        better = repo1
        worse = repo2
    else:
        better = repo2
        worse = repo1

    insights.append({
        "title": "CI/CD Reliability",
        "message":
            f"{better['repo_full_name']} has the higher workflow success rate "
            f"({better['workflow_success_rate']:.1f}%)."
    })

    if repo1["avg_contributions"] > repo2["avg_contributions"]:
        better = repo1
    else:
        better = repo2

    insights.append({
        "title": "Community Activity",
        "message":
            f"{better['repo_full_name']} receives stronger contributor activity."
    })

    if repo1["issue_closure_rate"] > repo2["issue_closure_rate"]:
        better = repo1
    else:
        better = repo2

    insights.append({
        "title": "Issue Management",
        "message":
            f"{better['repo_full_name']} resolves issues more efficiently."
    })

    return insights