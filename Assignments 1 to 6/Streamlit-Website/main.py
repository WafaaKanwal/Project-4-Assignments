import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and Sidebar
st.set_page_config(page_title="Data Dashboard", layout="wide")
st.title("📊 Enhanced Data Dashboard")

# Set dark theme by default
plt.style.use('dark_background')
st.markdown("""
    <style>
        .stApp { background-color: #0E1117; }
        .css-18e3th9, .css-1d391kg { background-color: #0E1117; }
        .st-bb, .st-at, .st-ae, .st-af, .st-ag, .st-ah, .st-ai, .st-aj { color: white; }
        .stDataFrame { background-color: #0E1117 !important; }
        .stSelectbox, .stRadio, .stButton>button { background-color: #0E1117; color: white; }
    </style>
""", unsafe_allow_html=True)

# File Upload
uploaded_file = st.sidebar.file_uploader("📂 Upload a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.sidebar.success("File Uploaded Successfully!")
    except Exception as e:
        st.sidebar.error(f"Error loading file: {e}")
        st.stop()
else:
    st.info("Please upload a CSV file to begin")
    st.stop()

# Data Preview
st.subheader("🔍 Data Preview")
st.dataframe(df.head())

# Data Summary
with st.expander("📊 Show Data Summary"):
    st.write(df.describe(include='all'))

# Filter Data
st.subheader("🔎 Filter Data")
filter_column = st.selectbox("Select a column to filter", df.columns)
filter_values = st.multiselect(
    f"Select values from {filter_column}", 
    df[filter_column].unique()
)

filtered_df = df[df[filter_column].isin(filter_values)] if filter_values else df
st.write(filtered_df)

# Data Visualization
st.subheader("📈 Data Visualization")
col1, col2, col3 = st.columns(3)
with col1:
    x_column = st.selectbox("Select X-axis", df.columns, key="x")
with col2:
    y_column = st.selectbox("Select Y-axis", df.columns, key="y")
with col3:
    chart_type = st.radio("Select Chart Type", ["Line", "Bar", "Scatter"], key="chart")

if st.button("Generate Plot ✨"):
    # Data validation
    if len(filtered_df) == 0:
        st.warning("No data matches your filters!")
    elif not pd.api.types.is_numeric_dtype(filtered_df[y_column]):
        st.error(f"Cannot plot non-numeric column '{y_column}' on Y-axis!")
    else:
        fig, ax = plt.subplots(figsize=(10, 5))
        
        try:
            # Convert dates if needed
            if pd.api.types.is_datetime64_any_dtype(filtered_df[x_column]):
                filtered_df[x_column] = filtered_df[x_column].dt.to_pydatetime()
            
            # Plotting logic
            if chart_type == "Line":
                ax.plot(filtered_df[x_column], filtered_df[y_column], marker='o', linestyle='-', color='cyan')
            elif chart_type == "Bar":
                ax.bar(filtered_df[x_column], filtered_df[y_column], color='lime')
            else:  # Scatter
                ax.scatter(filtered_df[x_column], filtered_df[y_column], color='magenta')
            
            # Formatting
            ax.set_xlabel(x_column, color='white')
            ax.set_ylabel(y_column, color='white')
            ax.set_title(f"{chart_type} Plot: {x_column} vs {y_column}", color='white')
            ax.tick_params(colors='white')
            
            # Handle crowded x-axis
            if len(filtered_df) > 10:
                plt.xticks(rotation=45)
                fig.tight_layout()
            
            st.pyplot(fig)
            plt.close(fig)
            
        except Exception as e:
            st.error(f"Plotting failed: {str(e)}")
else:
    st.info("Select parameters and click 'Generate Plot' to visualize the data.")