import pandas as pd


def tag_objections():

    df = pd.read_parquet("output/data/transcripts_clustered.parquet")

    cluster_map = {
        0: "intro_pitch",
        1: "intro_smalltalk",
        2: "busy_callback",
        3: "pricing_concern",
        4: "gatekeeper_wrong_person",
        5: "payment_processing_objection",
        6: "not_interested_polite"
    }

    df["objection_tag"] = df["cluster"].map(cluster_map)

    df[["attempt_id", "objection_tag"]].to_parquet(
        "output/data/objection_tags.parquet",
        index=False
    )

    print("Objection tags saved.")
    print(df["objection_tag"].value_counts())


if __name__ == "__main__":
    tag_objections()