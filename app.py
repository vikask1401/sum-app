import streamlit as st

st.header("Addition of Two Numbers")

def sum():
  a=st.number_input("FIRST NUMBER")
  b=st.number_input("SECOND NUMBER")
  return a+b

ans=sum()

st.header("Answer: "+str(ans))

