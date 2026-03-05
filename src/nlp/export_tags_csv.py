import pandas as pd


def export_tags():

    df = pd.read_parquet("output/data/objection_tags.parquet")

    df.to_csv("output/data/objection_tags.csv", index=False)

    print("CSV exported to output/data/objection_tags.csv")


if __name__ == "__main__":
    export_tags()