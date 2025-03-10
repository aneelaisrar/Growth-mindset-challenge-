#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project" , page_icon="★")

st.title("Growth Mindset Challenge:Web App with Streamlit")

st.header(" 🚀 Welome to Your Growth Journey!")
st.write("Embrace Challange,learn from mistakes,and unlock your full potental. ThisAl-powered app helps you build a growth minset with reflection,challenges,and  achieveement!")


#quote section
st.header("Today `s Groeth Mindset Quote")
st. write("Success is nat final, failure is nat fatal:it is the courage to continue that counts._Winston churchill")

st.header("What's your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

#condition

if user_input:
    st.success(f"💪you're facing:{user_input}.Keep pushing forward towords your goll🚀")
else:
    st.warning("Tell us about your challange to get started!")

    #reflexing
    st.header("Reflect on your Learning")
    reflection = st.text_area("Write your reflections:")

    if reflection:
        st.success (f"✫Great Insught! your reflection: {reflection}")
    else:
        st.info("Reflecting on past experience help you grow! share your  difficulties")

        #acheivements

        st.header("Celebrate Your Wins!" )
        aceivement = st.text_input("Share something you've recently accomplished:")

        
        if aceivement:
            st.success(f"🌠 Amazing! You achieved: {aceivement}")
        else:
            st.info("Big or small , every acheivement counts! share one now 😍")


            #footer
            st.write("- - -")
            st.write("Keep believing in yourself.Growth is a journay,not a destination!🌟 ")
            st.write("''✍ Created by Aneela Israr''")