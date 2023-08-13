import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain




def consultas_page():
    st.set_page_config(layout="wide", page_title="Talk Document")

    col_ask, col_pic3 = st.columns(2)

    with col_pic3:
        st.markdown("<h1 style='text-align: center'>QA Document Schema</h1>", unsafe_allow_html=True)

        st.image("docs\img\youarehere3.PNG")

    with col_ask:

        st.markdown("<h1 style='text-align: center'>Chat with the document</h1>", unsafe_allow_html=True)

        if not 'db' in st.session_state:
            st.markdown("<h3 style='text-align: center ; color: red;'>You must create a Data Base</h3>", unsafe_allow_html=True)
            rain(emoji="⚠️")

            m = st.markdown("""<style>
                                div.stButton > button:first-child {
                                    font-weight: bolder;
                                    background: rgb(222,181,151);
                                    background: linear-gradient(90deg, rgba(222,181,151,1) 0%, rgba(223,232,200,1) 94%););
                                }</style>""", unsafe_allow_html=True)

            go_back = st.button("Go to the previous step")
            if go_back:
                switch_page("1ª)create data base")

           
        else:
            db = st.session_state['db']
            print("RRR", db)

            if "generated" not in st.session_state:
                    st.session_state["generated"] = []
                
            if "past" not in st.session_state:
                st.session_state["past"] = []


            user_input = st.text_input(label=f"Question",
                                    value="Talk me about the document")

            # user_input = st.chat_input("Say something")


            if st.button("ASK"):
            # if user_input:
                    object_talkdocument = st.session_state["object_talkdocument"]
                    response = object_talkdocument.do_question(user_input, repo_id=st.session_state["settings"]["repo_id"])
                    st.session_state.past.append(user_input)
                    st.session_state.generated.append(response)

            if st.session_state["generated"]:
        
                    for i in range(len(st.session_state["generated"])-1, -1, -1):
                        # assistant = st.chat_message("assistant")
                        # user = st.chat_message("user")

                        question = st.session_state["past"][i]
                        # question_string = f"Question: {question}"
                        # response = st.session_state["generated"][i]["output_text"]
                        # chat_response = f"Anwser: {response}"

                        # assistant.write(chat_response)
                        # user.write(question_string)

                        st.markdown(f"<h3 style='text-align: center; color: black;'> ........................................................................</h3>", unsafe_allow_html=True)
                        
                        st.markdown(f"<h4 style='text-align: center; color: black;'> Question:</h4>", unsafe_allow_html=True)
                        st.markdown(f"<h4 style=' color: red;'>  {question}</h4>", unsafe_allow_html=True)
                        chat_message = st.session_state["generated"][i]["output_text"]
                        st.markdown(f"<h4 style='text-align: center; color: black;'> Anwser:</h4>", unsafe_allow_html=True)
                        st.markdown(f"<h4 style=' color: green;'>  {chat_message}</h4>", unsafe_allow_html=True)


                
                        
       

consultas_page()