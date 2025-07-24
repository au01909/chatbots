import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import google.generativeai as genai
import toml
import io
import json

# Set Streamlit page config
st.set_page_config(page_title="Data Analysis Chatbot", layout="wide")

# Load Gemini API key
try:
    config = toml.load("config.toml")
    api_key = config["api_keys"]["gemini"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
except Exception as e:
    st.error(f"❌ Failed to load Gemini API key: {e}")
    st.stop()

def app():
    st.title("📊 Data Analysis Chatbot")
    st.markdown("Upload a CSV file and ask natural language questions about your data.")

    uploaded_file = st.file_uploader("Upload CSV", type="csv")

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("✅ File uploaded successfully.")
        except Exception as e:
            st.error(f"❌ Failed to read CSV: {e}")
            return

        st.subheader("🔍 Data Preview")
        st.dataframe(df.head(10), use_container_width=True)

        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        categorical_cols = df.select_dtypes(include="object").columns.tolist()
        low_cardinality = [col for col in categorical_cols if df[col].nunique() <= 20]
        all_cols = df.columns.tolist()

        st.subheader("📍 Gemini Chart Suggestion")
        suggest_chart = st.button("🔮 Suggest chart using Gemini")
        if suggest_chart:
            try:
                df_sample = df.head(15).to_csv(index=False)
                prompt = f"""You are a data visualization expert. Based on the dataset below, suggest the most appropriate chart type and which columns to use.

CSV (first 15 rows):
{df_sample}

Give the chart type, x-axis and y-axis (if applicable), and a short reason."""
                response = model.generate_content(prompt)
                st.success("🧠 Gemini Suggestion:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"❌ Gemini suggestion error: {e}")

        st.subheader("📈 Smart Chart Generator")
        chart_type = st.radio("Choose chart type", ["Histogram", "Bar Chart", "Pie Chart", "Line Plot", "Scatter Plot", "Box Plot"])
        x_axis = y_axis = None
        fig = None

        try:
            if chart_type == "Histogram":
                x_axis = st.selectbox("Select numeric column", options=numeric_cols)
                if pd.api.types.is_numeric_dtype(df[x_axis]):
                    fig = px.histogram(df, x=x_axis)
                else:
                    st.error("❌ Histogram needs numeric column.")

            elif chart_type == "Bar Chart":
                x_axis = st.selectbox("X-axis (Categorical)", options=low_cardinality)
                y_axis = st.selectbox("Y-axis (Numeric)", options=numeric_cols)
                if pd.api.types.is_numeric_dtype(df[y_axis]):
                    fig = px.bar(df, x=x_axis, y=y_axis)
                else:
                    st.error("❌ Bar chart needs numeric Y-axis.")

            elif chart_type == "Pie Chart":
                x_axis = st.selectbox("Column (Categorical)", options=low_cardinality)
                fig = px.pie(df, names=x_axis)

            elif chart_type == "Line Plot":
                x_axis = st.selectbox("X-axis (Numeric)", options=numeric_cols)
                y_axis = st.selectbox("Y-axis (Numeric)", options=numeric_cols)
                if pd.api.types.is_numeric_dtype(df[x_axis]) and pd.api.types.is_numeric_dtype(df[y_axis]):
                    fig = px.line(df, x=x_axis, y=y_axis)
                else:
                    st.error("❌ Line Plot requires numeric axes.")

            elif chart_type == "Scatter Plot":
                x_axis = st.selectbox("X-axis (Numeric)", options=numeric_cols)
                y_axis = st.selectbox("Y-axis (Numeric)", options=numeric_cols)
                if pd.api.types.is_numeric_dtype(df[x_axis]) and pd.api.types.is_numeric_dtype(df[y_axis]):
                    fig = px.scatter(df, x=x_axis, y=y_axis)
                else:
                    st.error("❌ Scatter Plot requires numeric axes.")

            elif chart_type == "Box Plot":
                x_axis = st.selectbox("X-axis (Categorical)", options=low_cardinality)
                y_axis = st.selectbox("Y-axis (Numeric)", options=numeric_cols)
                if pd.api.types.is_numeric_dtype(df[y_axis]):
                    fig = px.box(df, x=x_axis, y=y_axis)
                else:
                    st.error("❌ Box plot needs numeric Y-axis.")

            if fig:
                st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"❌ Error generating chart: {e}")

        st.subheader("🧠 Natural Language Chart Request (AI-Powered)")
        nl_chart_query = st.text_input("Describe the chart you want (e.g., 'scatter plot of age vs income'):")
        
        if st.button("📊 Generate Chart"):
            if not nl_chart_query.strip():
                st.warning("Please enter a chart description.")
            else:
                try:
                    df_sample = df.head(20).to_csv(index=False)
                    prompt = f"""
You are an intelligent data visualization agent. Based on the dataset below (first 20 rows), the user will describe a chart in natural language.

Your job:
1. Extract the chart type.
2. Extract the x-axis and y-axis column names.
3. Respond in JSON format like:
{{
  "chart_type": "scatter",
  "x_axis": "age",
  "y_axis": "income"
}}

Only respond with the JSON. Do not explain.

CSV dataset:
{df_sample}

User query:
{nl_chart_query}
"""
                    gem_response = model.generate_content(prompt)
                    parsed = json.loads(gem_response.text.strip())

                    chart_type = parsed["chart_type"].lower()
                    x_axis = parsed.get("x_axis")
                    y_axis = parsed.get("y_axis")

                    fig = None

                    if chart_type == "histogram" and x_axis:
                        fig = px.histogram(df, x=x_axis)
                    elif chart_type == "bar" and x_axis and y_axis:
                        fig = px.bar(df, x=x_axis, y=y_axis)
                    elif chart_type == "pie" and x_axis:
                        fig = px.pie(df, names=x_axis)
                    elif chart_type == "line" and x_axis and y_axis:
                        fig = px.line(df, x=x_axis, y=y_axis)
                    elif chart_type == "scatter" and x_axis and y_axis:
                        fig = px.scatter(df, x=x_axis, y=y_axis)
                    elif chart_type == "box" and x_axis and y_axis:
                        fig = px.box(df, x=x_axis, y=y_axis)
                    else:
                        st.error("❌ Could not understand the chart request or unsupported chart type.")

                    if fig:
                        st.success(f"✅ Showing {chart_type} of {x_axis} vs {y_axis}")
                        st.plotly_chart(fig, use_container_width=True)

                except json.JSONDecodeError:
                    st.error("❌ Gemini did not return valid chart info. Try again with a simpler prompt.")
                except Exception as e:
                    st.error(f"❌ Error generating chart from description: {e}")

        st.subheader("🧪 Correlation Heatmap")
        if len(numeric_cols) >= 2:
            corr = df[numeric_cols].corr()
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
            st.pyplot(fig)
        else:
            st.info("Not enough numeric columns for correlation heatmap.")

        st.subheader("📊 Summary Statistics")
        st.dataframe(df.describe(), use_container_width=True)

        st.subheader("💬 Ask Questions About the Data")
        user_query = st.text_input("Type your question here:")
        if st.button("Submit Query"):
            if not user_query.strip():
                st.warning("Please enter a question.")
            else:
                try:
                    df_sample = df.head(20).to_csv(index=False)
                    prompt = f"""You are a helpful data analyst. Answer the question about the dataset below.

CSV Dataset (first 20 rows):
{df_sample}

User's question:
{user_query}

Answer:"""
                    response = model.generate_content(prompt)
                    st.success("🤖 Gemini's Answer:")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"❌ Gemini API error: {e}")

if __name__ == "__main__":
    app()
