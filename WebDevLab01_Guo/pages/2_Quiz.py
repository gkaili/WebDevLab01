import streamlit as st
import time
st.title("What is your spirit animal? 🤯")
st.write("Take this personality quiz to find out your definitive spirit animal, once and for all.")
swag = 0
violent = 0
graceful = 0
extraordinary = 0
wise = 0
q1= st.radio(
    "1. Pick a color? 🤔",
    ["Electric Blue⚡", "Blood Red🧛", "Dusty Rose🌹", "Periwinkle Purple🧚", "Smoked Gray💨"]
    )

q2= st.multiselect(
    "2. Which of these qualities describes you? 💪(select all that apply)",
    ["Infinite drip", "Always prepared", "Dancing through life", "Surprisingly insightful"]
    )

q3= st.slider(
    "3. How social are you from a scale from 0-10? 😚", 0, 10, 5)


q4= st.radio(
    "4. How would you wind down after a stresful day?",
    ["A cooling walk by the beach 🏄", "Destroying a rage room ⚾", "Brewing a nice cup of tea 🍵", "Reading your favorite book 📖", "No need 🤷‍♀"]
    )

q5= st.pills(
    "5. Choose your fashion necessities. 🤔(select all that apply)",
    ["Shoes", "Ribbon", "Hat", "Coat"], 
    selection_mode= "multi")

q6= st.selectbox(
    "6.Finally, pick your favorite animal! 🤗", 
    ["Cat", "Shark", "Dog", "Orangutan", "Swan"]
    )

st.write("How do you feel about the quiz right now?😊")
feeling = st.feedback("faces")
    

if q1 == "Electric Blue⚡":
    swag += 1.1
elif q1 == "Blood Red🧛":
    violent += 1.1
elif q1 == "Dusty Rose🌹":
    graceful += 1.1
elif q1 == "Periwinkle Purple🧚":
    extraordinary += 1.1
elif q1 == "Smoked Gray💨":
    wise += 1.1

if "Infinite drip" in q2:
    swag += 2
    graceful += 1
if "Always prepared" in q2:
    violent += 2
    wise += 1
if "Dancing through life" in q2:
    graceful += 2
    extraordinary += 1
if "Surprisingly insightful" in q2:
    extraordinary += 2
    wise += 1

if q3 <= 2:
    wise += 1
elif q3 <= 4:
    extraordinary += 1
elif q3 <= 6:
    swag += 1
elif q3 <= 8:
    graceful += 1
elif q3 <= 10:
    violent += 1

    
if q4 == "A cooling walk by the beach 🏄":
    swag += 1
elif q4 == "Destroying a rage room ⚾":
    violent += 1
elif q4 == "Brewing a nice cup of tea 🍵":
    graceful += 1
elif q4 == "No need 🤷‍♀":
    extraordinary += 1
elif q4 == "Reading your favorite book 📖":
    wise += 1

if "Shoes" in q5:
    swag += 1
if "Ribbon" in q5:
    graceful +=1
if "Hat" in q5:
    extraordinary += 1
if "Coat" in q5:
    wise += 1
if not q5:
    violent += 1

if q6 == "Cat":
    extraordinary += 1
elif q6 == "Shark":
    swag += 1
elif q6 == "Dog":
    violent += 1
elif q6 == "Orangutan":
    wise += 1
elif q6 == "Swan":
    graceful += 1

if swag > graceful and swag > extraordinary and swag > wise and swag > violent:
    trait = "swag"
elif graceful > extraordinary and graceful > wise and graceful > violent:
    trait = "graceful"
elif extraordinary > wise and extraordinary > violent:
    trait = "extraordinary"
elif wise > violent:
    trait = "wise"
else:
    trait = "violent"

if st.button("Click to see results 👀"):
    with st.spinner("Analyzing you aura, DNA, and depths of your soul...", show_time=True):
        time.sleep(2.222)
    st.toast("SYSTEM WARNING: Soul integrity compromised by excessive brainrot!", icon="🚨")
    time.sleep(2.222)
    if trait == "swag":
        st.title("Boi, you just got bamboozled🤯🫱")
        st.header("Your spirit animal is Tralalero Tralala!!! 🦈")
        st.image("Images/tralalero-tralala.jpg", width = 800)
        st.write("""
        Like those impossible designer sneakers on Tralalero Tralala's 3 feet, your natural aura demands absolute respect from every room you enter.
        Your effortless confidence is your most alluring quality, but that swaggy shell is hiding a terrifying amount of tomfoolery.
        """)
        st.balloons()
    if trait == "graceful":
        st.title("Boi, you just got bamboozled🤯🫱")
        st.header("Your spirit animal is Ballerina Cappuccina!!! 🧑‍🩰")
        st.image("Images/ballerina_cappuccina.jpg", width = 800)
        st.write("""
        Like a delicate espresso shot poured straight into a pirouette, you glide through life with terrifying poise.
        You never trip.
        You're just making your own impromptu choreography.
        """)
        st.balloons()
    if trait == "extraordinary":
        st.title("Boi, you just got bamboozled🤯🫱")
        st.header("Your spirit animal is Trippi Troppi!!! 🍤")
        st.image("Images/trippi_troppi.jpg", width = 800)
        st.write("""
        Reality simply cannot contain your dimensions.
        You exist simultaneously in five alternate timelines, operating on a frequency that defies both physics and common sense.
        The word eccentric doesn't do justice to your chaotic transcendence.
        """)
        st.balloons()
    if trait == "wise":
        st.title("Boi, you just got bamboozled🤯🫱")
        st.header("Your spirit animal is Brr Brr Patapim!!! 🦧")
        st.image("Images/brr_brr_patipim.webp", width = 800)
        st.write("""
        You hold the forbidden secrets of the universe... but you choose to communicate them strictly through auditory sound effects.
        Your brain is a library of profound epiphanies wrapped in absolute nonsense, making you an uncrackable riddle.
        """)
        st.balloons()
    if trait == "violent":
        st.title("Boi, you just got bamboozled🤯🫱")
        st.header("Your spirit animal is Tung Tung Tung Sahur!!! 🪵")
        st.image("Images/tung_tung_tung_sahur.avif", width = 800)
        st.write("""
        Peace was never an option.
        You don't negotiate with problems, you just beat them into submission.
        """)
        st.balloons()
##st.write(f"swag: {swag}, graceful: {graceful}, extraordinary: {extraordinary}, wise: {wise}, violent: {violent}")
##st.write(trait)
    
    
