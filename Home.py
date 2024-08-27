import streamlit as st

# Set the page configuration
st.set_page_config(page_title="CrissCross Puzzle", layout="wide")

# Page title
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎉 Welcome to UST CrissCross Puzzle! 🎉</h1>", unsafe_allow_html=True)

# Game introduction
st.markdown("""
    ## 🤔 What is the CrissCross Puzzle?
    The **CrissCross Puzzle** is an exciting game designed specifically for the **BestofUS** competition! 
    This puzzle challenges you to connect your knowledge of the various service portals available at UST. 
    It’s a fun way to test how well you know the tools and platforms that keep our workplace running smoothly! 💻🔗
    
    The puzzle is a grid-based game where clues are given to help you find the correct portal names that fit into the puzzle.
    Each answer relates to a service or tool we use in our day-to-day activities at UST.
    
    Do you think you have what it takes to solve it all? Let’s find out! 🚀
""")

# Instructions
st.markdown("""
    ## 📝 How to Play:
    1. **Click on the > icon on the Top left of the page & Select CrissCross to Start the Game.**
    2. **Unique ID**: Start by entering your **UID** (Unique ID). This ensures you can participate in the game only once. 🚪
    3. **Name & Mobile**: Fill in your name and mobile number to track your progress. 📱
    4. **Clues**: Read the clues carefully and enter the corresponding portal or service name in the text fields provided. 🕵️‍♂️
    5. **Submit**: Once you've filled in all the answers, hit the **Submit** button! 📤
    6. **Score**: Your score will be calculated based on the accuracy of your answers. 🏅
    7. **Winner**: The fastest person with all correct answers will be crowned the **winner**! 🏆

    ## 🚨 Important Notes:
    - Make sure all fields are filled before submitting.
    - You only get one chance to play, so give it your best shot! 🔥
    - If you win, your name will be displayed on the **Winners Dashboard**. 🥇

    ## 💡 Tips:
    - Think about the portals and services you use daily. 
    - Don't rush, accuracy is key!
    - Remember to enjoy the game—it's all in good fun!

    ## 📅 Timeline:
    The puzzle is open until the end of the **BestofUS** competition. Make sure to submit your answers before the deadline to be eligible for the winner's spot.

    ### Good luck and have fun! 🎯
""")

# Footer
st.markdown("""
    ---
    🛠 **Created for the BestofUS Competition**  
    🌟 **Empowering Associates through Fun and Learning**
""")
