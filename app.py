import streamlit as st
import numpy as np
from scipy.stats import t
from statistics import stdev
from scipy import stats

st.title("Two Sample t-Test Calculator")

st.write("Enter sample values separated by commas")

# Input boxes
sample1 = st.text_input("Sample 1")
sample2 = st.text_input("Sample 2")

alternative = st.selectbox(
    "Select Alternative Hypothesis",
    ["two-sided", "left", "right"]
)

if st.button("Calculate"):

    try:
        a = [float(x) for x in sample1.split(",")]
        b = [float(x) for x in sample2.split(",")]

        xbar1 = np.mean(a)
        xbar2 = np.mean(b)

        sd1 = stdev(a)
        sd2 = stdev(b)

        n1 = len(a)
        n2 = len(b)

        alpha = 0.05 / 2
        df = n1 + n2 - 2
        se = np.sqrt((sd1**2)/n1 + (sd2**2)/n2)

        tcal = ((xbar1 - xbar2) - 0) / se

        if alternative == "two-sided":
            p_value = 2 * (1 - t.cdf(abs(tcal), df))
        elif alternative == "left":
            p_value = t.cdf(tcal, df)
        else:
            p_value = 1 - t.cdf(tcal, df)

        st.subheader("Results")
        st.write(f"T-statistic: {tcal}")
        st.write(f"P-value: {p_value}")
        st.write("Scipy Result:")
        st.write(stats.ttest_ind(a, b, alternative=alternative, equal_var=False))

    except:
        st.error("Please enter valid numeric values separated by commas.")