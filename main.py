
import pandas as pd
import numpy as np
import streamlit as st
import pandas as pd
import numpy as np



df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=("col %d" % i for i in range(5)))

# Display a static table
st.table(df)

# Display an interactive table
st.dataframe(df)
