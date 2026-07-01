import pandas as pd


def comparison_table(df):

    repo1 = df.iloc[0]
    repo2 = df.iloc[1]

    rows = [

        ["Stars",
         f"{repo1['stars']:,}",
         f"{repo2['stars']:,}"],

        ["Forks",
         f"{repo1['forks']:,}",
         f"{repo2['forks']:,}"],

        ["Repository Health",
         f"{repo1['repository_health_score']:.2f}",
         f"{repo2['repository_health_score']:.2f}"],

        ["Repository Grade",
         repo1["repository_grade"],
         repo2["repository_grade"]],

        ["Merge Rate",
         f"{repo1['merge_rate']:.1f}%",
         f"{repo2['merge_rate']:.1f}%"],

        ["Issue Closure",
         f"{repo1['issue_closure_rate']:.1f}%",
         f"{repo2['issue_closure_rate']:.1f}%"],

        ["Workflow Success",
         f"{repo1['workflow_success_rate']:.1f}%",
         f"{repo2['workflow_success_rate']:.1f}%"],

        ["Approval Rate",
         f"{repo1['approval_rate']:.1f}%",
         f"{repo2['approval_rate']:.1f}%"],

        ["Average Contributions",
         f"{repo1['avg_contributions']:.1f}",
         f"{repo2['avg_contributions']:.1f}"]

    ]

    return pd.DataFrame(
        rows,
        columns=[
            "Metric",
            repo1["repo_full_name"],
            repo2["repo_full_name"]
        ]
    )