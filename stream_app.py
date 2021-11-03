import streamlit as st
import joblib

#Load Model
model1 = joblib.load('lr_model.pkl')

# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:silver;padding:10px"> 
    <h3 style ="color:black;text-align:center;">Streamlit Petrol Consumption Prediction App</h3> 
    </div> 
    """
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 


    # following lines create boxes in which user can enter data required to make prediction 
    pet_tax = st.number_input("Petrol tax")
    avg_inc = st.number_input("Average_income")
    p_hgh = st.text_input("Paved_Highways")
    pdl = st.number_input("Population_Driver_licence")
    


    if st.button("Predict"):    
        result = model1.predict([[float(pet_tax),float(avg_inc),float(p_hgh),float(pdl)]]) 
        html_temp = """ <h3 style ="color:black;text-align:left;">Output : </h3> """
        st.markdown(html_temp, unsafe_allow_html = True)
        st.success('Petrol Consumption         :       {}'.format( round(result[0],3)))
        
        
     
if __name__=='__main__': 
    main()


    

    
