import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns






# Load Titanic dataset
titanic = pd.read_csv('train.csv')

# Load the trained model
model = joblib.load('titanic_model.pkl')

# Streamlit App
page = st.sidebar.selectbox("Select a page", ["Prediction Model", "Graphs"])

# Home Page
if page == "Prediction Model":
    
    st.title('Titanic Survival Prediction App')
    st.write("Would you have survived the disaster? Type in your details and find out!")
    st.markdown("<br>", unsafe_allow_html=True)  # Adds a line break
    st.markdown("<br>", unsafe_allow_html=True)  # Adds a line break


    sex = st.selectbox("Sex", ("Male", "Female"))
    # Ticket class input
    ticket_class = st.selectbox("Ticket class", options=["First", "Second", "Third"])  # Radio for Ticket Class

    age = st.slider("Age", 1, 100, 25)

    # Define fare ranges based on the class
    fare_ranges = {
        "First": (150, 512),
        "Second": (60, 150),
        "Third": (10, 60)
    }

    # Set the fare slider based on selected class
    fare_min, fare_max = fare_ranges[ticket_class]
    fare = st.slider("Ticket fare", fare_min, fare_max, fare_min)

    # Input field for Parch
    parch = st.slider("Number of relatives aboard", 0, 6, 0)

    # Convert user input to model format
    sex = 1 if sex == "Male" else 0
    ticket_class = {"First": 0, "Second": 1, "Third": 2}[ticket_class]

    # Predict button
    if st.button("Predict"):
        input_data = np.array([[sex, age, fare, ticket_class, parch]])
        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)
        survival_chance = probability[0][1] * 100

        if survival_chance >= 50:
            st.success(f"You would have survived with a {survival_chance:.2f}% chance!")
        else:
            st.error(f"You would have survived with a {survival_chance:.2f}% chance!")


elif page == "Graphs":
    st.title("Data Visualizations")
    st.markdown("<br>", unsafe_allow_html=True)  # Adds a line break
    st.markdown("<br>", unsafe_allow_html=True)  # Adds a line break
    # 1. Survival Rates by Gender
    survival_counts = titanic.groupby('Sex')['Survived'].value_counts().unstack(fill_value=0)
    survival_rates = survival_counts.div(survival_counts.sum(axis=1), axis=0)

    fig, ax = plt.subplots()
    survival_rates.plot(kind='bar', stacked=True, color=['red', 'green'], ax=ax)
    ax.set_xlabel('Gender')
    ax.set_ylabel('Proportion')
    ax.set_title('Survival Rates by Gender')
    ax.legend(['Did Not Survive', 'Survived'], title="Legend")

    col1, col2 = st.columns(2)  # Create two columns for side-by-side layout

    with col1:
        st.pyplot(fig)

    # 2. Survival Rate by Class
    survival_rate_by_class = titanic.groupby('Pclass')['Survived'].mean()

    fig1, ax1 = plt.subplots()
    ax1.bar(survival_rate_by_class.index, survival_rate_by_class.values, color=['darkblue', 'darkblue', 'darkblue'])
    ax1.set_xticks([1, 2, 3])
    ax1.set_xticklabels(['First', 'Second', 'Third'])
    ax1.set_title('Survival Rate by Class')
    ax1.set_xlabel('Class')
    ax1.set_ylabel('Survival Rate')

    with col2:
        st.pyplot(fig1)

    # Create new columns for the next pair of graphs
    col3, col4 = st.columns(2)

    # 3. Distribution of Survivors Based on Ticket Fare
    with col3:
        fig3, ax3 = plt.subplots()
        sns.boxplot(x='Survived', y='Fare', data=titanic, ax=ax3)
        ax3.set_xticklabels(['Did Not Survive', 'Survived'])
        ax3.set_title('Ticket Fare Distribution')
        ax3.set_xlabel('Survival Status')
        ax3.set_ylabel('Fare')
        st.pyplot(fig3)

    # 4. Age Distribution of Survivors vs Non-Survivors
    with col4:
        survivors = titanic[titanic['Survived'] == 1]['Age']
        non_survivors = titanic[titanic['Survived'] == 0]['Age']

        fig4, ax4 = plt.subplots()
        sns.kdeplot(survivors, label='Survivors', color='green', ax=ax4)
        sns.kdeplot(non_survivors, label='Non-Survivors', color='red', ax=ax4)

        ax4.set_xlabel('Age')
        ax4.set_ylabel('Density')
        ax4.set_title('Age Distribution of Survivors vs. Non-Survivors')
        ax4.legend()
        st.pyplot(fig4)
