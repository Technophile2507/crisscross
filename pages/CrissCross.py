import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Function to check if the file exists and create it if it doesn't
def initialize_files():
    if not os.path.exists("participants.xlsx"):
        df = pd.DataFrame(columns=["UID", "Name", "Mobile", "Answers", "Result", "Time Taken", "Verdict"])
        df.to_excel("participants.xlsx", index=False)

    
    if not os.path.exists("answers.xlsx"):
        df = pd.DataFrame({
            "Question": [
                "2] The workplace management digital gateway solution to search and find our colleagues.",
                "4] Search relevant courses and master new skills in business and technology, anytime.",
                "6] User-friendly ride tracking with self-rostering, privacy features, and safety measures.",
                "10] Update your skills and career path in a dynamic and evolving professional landscape.",
                "12] Your go-to spot for financial reports and declarations.",
                "16] Report concerns or violations confidentially and support value-based compliance.",
                "17] It’s fun to work with friends",
                "19] A first of its kind initiative by UST to encourage reusing from existing artefacts",
                "20] Recognize and celebrate the associates who drive our success and achievements.",
                "1] Locking in your hours? Don’t miss the cut-off—submit before EOD!",
                "3] Values are fundamental ‘beliefs’ or the principles which we abide by and which guide our decisions, actions and our culture.",
                "5] From talent to time off, it’s your all-in-one HR hub.",
                "7] Join a themed team that aligns with your passions and goals for impactful collaboration.",
                "8] Your gateway for employee links, requisitions, eprocurement, and expenses.",
                "9] Discover our community development efforts aligned with core values of humility, humanity, and integrity",
                "11] A tool to track, manage, and monitor visitor details for security compliance.",
                "13] Say hello to budget! Gain visibility into all spend managed in one place",
                "14] Need access, HR help, or something fixed? Log it here.",
                "15] A referral program that turns your network into a $5 billion opportunity.",
                "18] Manifests the company's commitment to integrate business and ethics into our everyday work"
            ],
            "Answer": [
                "PeopleFinder", "GAMA", "UStride", "Career Velocity", "MyPay",
                "EthicsPoint", "USTUSource", "CORA", "USTar", "GlobalTimesheet",
                "ValuesPortal", "Workday", "ColorsofUST", "OrionFinance", "CSR Portal", "VMT",
                "Concur", "isolve", "ColumbUS", "OVCPortal"
            ]
        })
        df.to_excel("answers.xlsx", index=False)

# Load participants and answers
def load_data():
    initialize_files()
    participants_df = pd.read_excel("participants.xlsx")
    answers_df = pd.read_excel("answers.xlsx")
    return participants_df, answers_df

# Save new participant data to excel file
def save_participant_data(participants_df):

    # Sort the DataFrame: 'Winner' at the top and sorted by 'Time Taken' in ascending order
    participants_df = participants_df.sort_values(by=["Verdict", "Time Taken"], ascending=[False, True])
    participants_df.to_excel("participants.xlsx", index=False)

# Check if the UID is unique
def is_unique_uid(uid, participants_df):
    # Strip any leading/trailing whitespace and convert to string for both input and DataFrame values
    uid = str(uid).strip()
    existing_uids = participants_df["UID"].astype(str).str.strip()
    
    return uid not in existing_uids.values

# Calculate the score and color the answers
def calculate_score_and_color(answers, correct_answers_df):
    score = 0
    answer_colors = []
    for i, answer in enumerate(answers):
        if ''.join(answer.split()).lower() == ''.join(correct_answers_df.iloc[i]["Answer"].split()).lower():
            score += 1
            answer_colors.append("green")
        else:
            answer_colors.append("red")
    return score, answer_colors

# Check if current participant is the winner
def check_winner(score, time_taken, participants_df):
    if score == 20:
        # Filter to get only rows where the verdict is 'Winner'
        winners_df = participants_df[participants_df["Verdict"] == "Winner"]
        
        # If there are no previous winners, the current participant is the first winner
        if winners_df.empty:
            return True
        
        # Get the minimum time among previous winners
        min_time = winners_df["Time Taken"].min()
        
        # Check if the current participant's time is less than or equal to the minimum time
        if time_taken <= min_time:
            return True
    
    return False

# Function to display colored text inputs
def colored_text_input(label, value, color, key):
    st.markdown(
        f'<div style="margin-bottom:10px;"><label>{label}</label>'
        f'<input type="text" value="{value}" style="color: white; background-color: {color}; border-radius: 4px; width: 100%;" disabled></div>',
        unsafe_allow_html=True
    )

# Initialize the app
st.markdown("<h1 style='text-align: center; '>UST CrissCross Puzzle</h1>", unsafe_allow_html=True)

# Load the data
participants_df, answers_df = load_data()

# User input fields
uid = st.text_input("UID")
name = st.text_input("Name")
mobile = st.text_input("Mobile number")

start_time = None

# Check UID uniqueness and validate all fields
if uid and name and mobile:
    if is_unique_uid(uid, participants_df):
        st.success("UID is unique, please proceed.")
        
        # Display the crossword image
        st.image("./Criss Cross Puzzle.jpg")
        start_time = datetime.now()

        # Create fields for answering the crossword questions
        answers = []
        
        placeholder = st.empty()
        with placeholder.container():
            with st.form("my_form"):
                for i, row in answers_df.iterrows():
                    answer = st.text_input(row["Question"], key=f"question_{i}")
                    answers.append(answer)

                submitted = st.form_submit_button("Submit")
        # Submit button
        if submitted:

            # Check if all fields are filled
            if all(answers):
                end_time = datetime.now()
                time_taken = (end_time - start_time).total_seconds()
                
                # Calculate score and color the answers
                score, answer_colors = calculate_score_and_color(answers, answers_df)
                
                placeholder.empty()

                # Display colored text boxes
                for i, row in answers_df.iterrows():
                    colored_text_input(row["Question"], answers[i], answer_colors[i], key=f"question_{i}")

                # Check if the participant is the winner
                is_winner = check_winner(score, time_taken, participants_df)
                verdict = "Winner" if is_winner else "Lost"

                # Save the data
                new_entry = {
                    "UID": uid,
                    "Name": name,
                    "Mobile": mobile,
                    "Answers": answers,
                    "Result": score,
                    "Time Taken": time_taken,
                    "Verdict": verdict
                }
                participants_df = pd.concat([participants_df, pd.DataFrame([new_entry])], ignore_index=True)
                save_participant_data(participants_df)

                # Display the score and time taken
                st.write(f"Your score: {score}/20")
                st.write(f"Time taken: {time_taken:} seconds")

                # Display winner or loser message
                if is_winner:
                    st.success("Congratulations! You are the winner!")
                else:
                    st.info("Good try! Better luck next time.")
            else:
                st.warning("Please fill in all the answers before submitting.")
    else:
        st.error("Sorry, you have already attended the game.")
else:
    st.warning("Please fill in all fields.")
