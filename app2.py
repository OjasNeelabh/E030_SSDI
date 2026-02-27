import streamlit as st
import numpy as np
from scipy import stats
from statistics import stdev

st.set_page_config(page_title="Two Sample t-Test", layout="centered")

st.title("Two Sample t-Test Calculator")

st.write("Enter sample values separated by commas (example: 12,15,14,10,13)")

# Input boxes
sample1 = st.text_input("Sample 1")
sample2 = st.text_input("Sample 2")

alternative = st.selectbox(
    "Select Alternative Hypothesis",
    ["two-sided", "less", "greater"]
)

if st.button("Calculate"):

    try:
        a = [float(x.strip()) for x in sample1.split(",")]
        b = [float(x.strip()) for x in sample2.split(",")]

        xbar1 = np.mean(a)
        xbar2 = np.mean(b)

        sd1 = stdev(a)
        sd2 = stdev(b)

        n1 = len(a)
        n2 = len(b)

        df = n1 + n2 - 2
        se = np.sqrt((sd1**2)/n1 + (sd2**2)/n2)

        tcal = (xbar1 - xbar2) / se

        if alternative == "two-sided":
            p_value = 2 * (1 - stats.t.cdf(abs(tcal), df))
        elif alternative == "less":
            p_value = stats.t.cdf(tcal, df)
        else:
            p_value = 1 - stats.t.cdf(tcal, df)

        st.subheader("Results")
        st.write(f"T-statistic: {round(tcal, 4)}")
        st.write(f"P-value (manual): {round(p_value, 6)}")

        st.write("SciPy Verification:")
        st.write(stats.ttest_ind(a, b, alternative=alternative, equal_var=False))

    except Exception as e:
        st.error("Please enter valid numeric values separated by commas.")
