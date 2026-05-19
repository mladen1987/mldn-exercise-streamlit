import pandas as pd
import altair as alt
import streamlit as st

from config import DATE_COLUMN

def render_contribution_heatmap(exercise_data_df):

    if exercise_data_df.empty:
        st.info("No exercise data available")
        return

    # ===== PREPARE DATES =====
    df = exercise_data_df.copy()

    df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN])

    # One row per date
    daily_sessions = (
        df.groupby(DATE_COLUMN)
        .size()
        .reset_index(name="session_count")
    )


    # ===== DATE RANGE =====
    end_date = pd.Timestamp.today().normalize()

    start_date = end_date - pd.Timedelta(days=365)

    # align to Monday
    start_date = start_date - pd.Timedelta(days=start_date.weekday())

    all_dates = pd.DataFrame({
        DATE_COLUMN: pd.date_range(start=start_date, end=end_date)
    })

    heatmap_df = all_dates.merge(
        daily_sessions,
        on=DATE_COLUMN,
        how="left"
    )

    heatmap_df["session_count"] = (
        heatmap_df["session_count"]
        .fillna(0)
    )

    heatmap_df["has_session"] = (
        heatmap_df["session_count"] > 0
    ).astype(int)

    heatmap_df["weekday"] = heatmap_df[DATE_COLUMN].dt.weekday

    heatmap_df["week"] = (
        (heatmap_df[DATE_COLUMN] - start_date).dt.days // 7
    )

    heatmap_df["date_str"] = heatmap_df[DATE_COLUMN].dt.strftime("%Y-%m-%d")
    heatmap_df["has_session_str"] = heatmap_df["has_session"].apply(lambda x: "Y" if x > 0 else "N")

    # ===== MONTH LABELS =====
    month_labels = (
        heatmap_df[[DATE_COLUMN, "week"]]
        .drop_duplicates(subset=["week"])
        .copy()
    )

    month_labels["month"] = month_labels[DATE_COLUMN].dt.strftime("%b")

    month_labels = (
        month_labels
        .groupby("month", as_index=False)
        .first()
    )
    
    heatmap_df[[DATE_COLUMN, "week"]].drop_duplicates(subset=["week"])
    
    text = (
        alt.Chart(month_labels)
        .mark_text(
            align="left",
            baseline="bottom",
            dy=-2,
            color="#9aa0a6"
        )
        .encode(
            x=alt.X("week:O"),
            y=alt.value(-0.5),  # 👈 pushes labels above grid
            text="month:N"
        )
    )
    
    # ===== TEXT SUMMARY =====
    sessions_this_year = int(
        heatmap_df["has_session"].sum()
    )

    st.markdown(
        f"### {sessions_this_year} sessions this year"
    )    

    # ===== CHART =====
    alt.theme.enable("dark")

    chart = (
        alt.Chart(heatmap_df)
        .mark_rect(cornerRadius=5)
        .encode(
            x=alt.X(
                "week:O",
                title=None,
                axis=None
            ),
            
            y=alt.Y(
                "weekday:O",
                title=None,
                sort=[0, 1, 2, 3, 4, 5, 6],
                axis=alt.Axis(
                    labelExpr="['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][datum.value]"
                )
            ),
            color=alt.Color(
                "has_session:O",
                scale=alt.Scale(
                    domain=[0, 1],
                    range=[
                        "#191a1b",  # no session
                        "#40c463"   # session exists
                    ]
                ),
                legend=None
            ),
            tooltip=[
                alt.Tooltip("date_str:N", title="Date"),
                alt.Tooltip("has_session_str:N", title="Session")
            ]
        )
        .properties(
            width=900,
            height=180
        )
    )

    st.altair_chart(
        chart + text,
        use_container_width=True
    )
