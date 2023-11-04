import streamlit as st
import mysql.connector
import pandas as pd
import PIL
import plotly.express as px
import matplotlib.pyplot as plt
import requests
import geopandas as gdp
from PIL import Image
from streamlit_option_menu import option_menu
st.title('Phonepe pulse')


conn = mysql.connector.connect(user='root', password='1997', host='127.0.0.1', database="phonepy")

cursor = conn.cursor()

#with st.sidebar:
SELECT = option_menu(
    menu_title = None,
    options = ["About","Home","Basic insights","Contact"],
    icons =["bar-chart","house","toggles","at"],
    default_index=2,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "white","size":"cover", "width": "100%"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"}})


if SELECT == "Basic insights":
    st.title("BASIC INSIGHTS")
    st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--",
               "Top 10 states based on year and amount of transaction",
               "List 10 states based on type and amount of transaction",
               "Top 5 Transaction_Type based on Transaction_Amount",
               "Top 10 Registered-users based on States and District",
               "Top 10 Districts based on states and Count of transaction",
               "List 10 Districts based on states and amount of transaction",
               "List 10 Transaction_Count based on Districts and states",
               "Top 10 RegisteredUsers based on states and District"]

    
    select = st.selectbox("Select the option",options)
    if select=="Top 10 states based on year and amount of transaction":
        cursor.execute("SELECT DISTINCT States, Transaction_Year, SUM(Transaction_Amount) AS Total_Transaction_Amount FROM top_tran GROUP BY States, Transaction_Year ORDER BY Total_Transaction_Amount DESC LIMIT 10");
        
        df = pd.DataFrame(cursor.fetchall(), columns=['States','Transaction_Year', 'Transaction_Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 states and amount of transaction")
            st.bar_chart(data=df,x="Transaction_Amount",y="States")


    
    elif select=="List 10 states based on type and amount of transaction":
        cursor.execute("SELECT DISTINCT States, SUM(Transaction_Count) as Total FROM top_tran GROUP BY States ORDER BY Total ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','Total_Transaction'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 states based on type and amount of transaction")
            st.bar_chart(data=df,x="Total_Transaction",y="States")


    elif select == "Top 5 Transaction_Type based on Transaction_Amount":
        cursor.execute("SELECT DISTINCT Transaction_Type, SUM(Transaction_Amount) AS Amount FROM agg_user GROUP BY Transaction_Type ORDER BY Amount DESC LIMIT 5");
        df = pd.DataFrame(cursor.fetchall(), columns=['Transaction_Type', 'Transaction_Amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 5 Transaction_Type based on Transaction_Amount")
            st.bar_chart(data=df, y="Transaction_Type", x="Transaction_Amount")


    elif select == "Top 10 Registered-users based on States and District":
        cursor.execute("SELECT DISTINCT State, District, SUM(RegisteredUsers) AS Users FROM top_user GROUP BY State, District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','RegisteredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Registered-users based on States and District")
            st.bar_chart(data=df,y="State",x="RegisteredUsers")



    elif select=="Top 10 Districts based on states and Count of transaction":
        cursor.execute("SELECT DISTINCT States,District,SUM(Transaction_Count) AS Counts FROM map_tran GROUP BY States,District ORDER BY Counts DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','District','Transaction_Count'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts based on states and Count of transaction")
            st.bar_chart(data=df,y="States",x="Transaction_Count")


    elif select=="List 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT States,Transaction_year,SUM(Transaction_Amount) AS Amount FROM agg_trans GROUP BY States, Transaction_year ORDER BY Amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','Transaction_year','Transaction_Amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 Districts based on states and amount of transaction")
            st.bar_chart(data=df,y="States",x="Transaction_Amount")
            
            #7
            
    elif select=="List 10 Transaction_Count based on Districts and states":
        cursor.execute("SELECT DISTINCT States, District, SUM(Transaction_Count) AS Counts FROM map_tran GROUP BY States,District ORDER BY Counts ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['States','District','Transaction_Count'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 Transaction_Count based on Districts and states")
            st.bar_chart(data=df,y="States",x="Transaction_Count")
            
            #8
             
    elif select=="Top 10 RegisteredUsers based on states and District":
        cursor.execute("SELECT DISTINCT States,District, SUM(RegisteredUsers) AS Users FROM map_user GROUP BY States,District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns = ['States','District','RegisteredUsers'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 RegisteredUsers based on states and District")
            st.bar_chart(data=df,y="States",x="RegisteredUsers")



#...............HOME..........
cursor = conn.cursor()

# execute a SELECT statement
cursor.execute("SELECT * FROM agg_trans")

# fetch all rows
rows = cursor.fetchall()
from streamlit_extras.add_vertical_space import add_vertical_space

if SELECT == "Home":
    col1,col2, = st.columns(2)
    col1.image(Image.open(r"C:/Users/User/Downloads/phonepe.png"),width = 300)
    with col1:
        st.subheader("PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        st.video(r"E:/pulse/Phonepe pulse/pulse-video.mp4")
        
    st.subheader(':blue[Registered Users Hotspots - States]')     

    Data_Aggregated_Transaction_df= pd.read_csv(r"E:/pulse/Phonepe pulse/Data_Aggregated_Transaction_Table.csv")
    Data_Aggregated_User_Summary_df= pd.read_csv(r"E:/pulse/Phonepe pulse/Data_Aggregated_User_Summary_Table.csv")
    Data_Aggregated_User_df= pd.read_csv(r"E:/pulse/Phonepe pulse/Data_Aggregated_User_Table.csv")
    Scatter_Geo_Dataset =  pd.read_csv(r"E:/pulse/Phonepe pulse/Data_Map_Districts_Longitude_Latitude.csv")
    Coropleth_Dataset =  pd.read_csv(r"E:/pulse/Phonepe pulse/Data_Map_IndiaStates_TU.csv")
    Data_Map_Transaction_df = pd.read_csv(r"E:/pulse/Phonepe pulse/Data_Map_Transaction_Table.csv")
    Data_Map_User_Table= pd.read_csv(r"E:/pulse/Phonepe pulse/Data_Map_User_Table.csv")
    Indian_States= pd.read_csv(r"E:/pulse/Phonepe pulse/Longitude_Latitude_State_Table.csv")
    
    c1,c2=st.columns(2)
    with c1:
        Year = st.selectbox(
                'Please select the Year',
                ('2018', '2019', '2020','2021','2022'))
    with c2:
        Quarter = st.selectbox(
                'Please select the Quarter',
                ('1', '2', '3','4'))
    year=int(Year)
    quarter=int(Quarter)
    
    Transaction_scatter_districts=Data_Map_Transaction_df.loc[(Data_Map_Transaction_df['Year'] == year ) & (Data_Map_Transaction_df['Quarter']==quarter) ].copy()
    Transaction_Coropleth_States=Transaction_scatter_districts[Transaction_scatter_districts["State"] == "india"]
    Transaction_scatter_districts.drop(Transaction_scatter_districts.index[(Transaction_scatter_districts["State"] == "india")],axis=0,inplace=True)
    # Dynamic Scattergeo Data Generation
    
    Transaction_scatter_districts = Transaction_scatter_districts.sort_values(by=['Place_Name'], ascending=False)
    Scatter_Geo_Dataset = Scatter_Geo_Dataset.sort_values(by=['District'], ascending=False) 
    Total_Amount=[]
    for i in Transaction_scatter_districts['Total_Amount']:
        Total_Amount.append(i)
    Scatter_Geo_Dataset['Total_Amount']=Total_Amount
    Total_Transaction=[]
    for i in Transaction_scatter_districts['Total_Transactions_count']:
        Total_Transaction.append(i)
    Scatter_Geo_Dataset['Total_Transactions']=Total_Transaction
    Scatter_Geo_Dataset['Year_Quarter']=str(year)+'-Q'+str(quarter)
    # Dynamic Coropleth
    
    Coropleth_Dataset = Coropleth_Dataset.sort_values(by=['state'], ascending=False)
    Transaction_Coropleth_States = Transaction_Coropleth_States.sort_values(by=['Place_Name'], ascending=False)
    Total_Amount=[]
    for i in Transaction_Coropleth_States['Total_Amount']:
        Total_Amount.append(i)
    Coropleth_Dataset['Total_Amount']=Total_Amount
    Total_Transaction=[]
    for i in Transaction_Coropleth_States['Total_Transactions_count']:
        Total_Transaction.append(i)
    Coropleth_Dataset['Total_Transactions']=Total_Transaction 
    
    
    
    
    #scatter plotting the states codes 
    Indian_States = Indian_States.sort_values(by=['state'], ascending=False)
    Indian_States['Registered_Users']=Coropleth_Dataset['Registered_Users']
    Indian_States['Total_Amount']=Coropleth_Dataset['Total_Amount']
    Indian_States['Total_Transactions']=Coropleth_Dataset['Total_Transactions']
    Indian_States['Year_Quarter']=str(year)+'-Q'+str(quarter)
    fig=px.scatter_geo(Indian_States,
                        lon=Indian_States['Longitude'],
                        lat=Indian_States['Latitude'],                                
                        text = Indian_States['code'], #It will display district names on map
                        hover_name="state", 
                        hover_data=['Total_Amount',"Total_Transactions","Year_Quarter"],
                        )
    fig.update_traces(marker=dict(color="white" ,size=0.3))
    fig.update_geos(fitbounds="locations", visible=False,)
    # scatter plotting districts
    Scatter_Geo_Dataset['col']=Scatter_Geo_Dataset['Total_Transactions']
    fig1=px.scatter_geo(Scatter_Geo_Dataset,
                        lon=Scatter_Geo_Dataset['Longitude'],
                        lat=Scatter_Geo_Dataset['Latitude'],
                        color=Scatter_Geo_Dataset['col'],
                        size=Scatter_Geo_Dataset['Total_Transactions'],     
                    #text = Scatter_Geo_Dataset['District'], #It will display district names on map
                        hover_name="District", 
                        hover_data=["State", "Total_Amount","Total_Transactions","Year_Quarter"],
                        title='District',
                        size_max=22)
    
    fig1.update_traces(marker=dict(color="rebeccapurple" ,line_width=1))    #rebeccapurple
#coropleth mapping india
    fig_ch = px.choropleth(
                        Coropleth_Dataset,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',                
                        locations='state',
                        color="Total_Transactions",                                       
                        )
    fig_ch.update_geos(fitbounds="locations", visible=False,)
#combining districts states and coropleth
    fig_ch.add_trace( fig.data[0])
    fig_ch.add_trace(fig1.data[0])
    st.write("### **:blue[PhonePe India Map]**")
    colT1,colT2 = st.columns([6,4])
    with colT1:
        st.plotly_chart(fig_ch, use_container_width=True)
    with colT2:
        st.info(
        """
        Details of Map:
        - The darkness of the state color represents the total transactions
        - The Size of the Circles represents the total transactions dictrict wise
        - The bigger the Circle the higher the transactions
        - Hover data will show the details like Total transactions, Total amount
        """
        )
        st.info(
        """
        Important Observations:
        - User can observe Transactions of PhonePe in both statewide and Districtwide.
        - We can clearly see the states with highest transactions in the given year and quarter
        - We get basic idea about transactions district wide
        """
        )




#----------------About-----------------------#

if SELECT == "About":
    col1,col2 = st.columns(2)
    with col1:
        st.video(r"E:/pulse/Phonepe pulse/pulse-video.mp4")
    with col2:
        st.image(Image.open(r"E:/pulse/Phonepe pulse/top.jpeg"),width = 500)
        st.write("---")
        st.subheader("The Indian digital payments story has truly captured the world's imagination."
                 " From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and states-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government."
                 " Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. "
                 "PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
    st.write("---")
    col1,col2 = st.columns(2)
    with col1:
        st.title("THE BEAT OF PHONEPE")
        st.write("---")
        st.subheader("Phonepe became a leading digital payments company")
        with open(r"E:/pulse/Phonepe pulse/annual report.pdf","rb") as f:
            data = f.read()
        st.download_button("DOWNLOAD REPORT",data,file_name="annual report.pdf")
    with col2:
        st.image(Image.open(r"E:/pulse/Phonepe pulse/top.jpeg"),width = 300)
    
#..........................CONTACT.....................

if SELECT == "Contact":
    Name = "GOWRI SHANKAR M"
    Social_Media={
        "GITHUB":"https://github.com/MuYaLkuTty",
        "LINKEDIN":"https://www.linkedin.com/in/m-gowri-shankar-m-0544a8137/"}
    st.title('Phonepe Pulse data visualisation')
    st.write("The goal of this project is to extract data from the Phonepe pulse Github repository, transform and clean the data, insert it into a MySQL database, and create a live geo visualization dashboard using Streamlit and Plotly in Python. The dashboard will display the data in an interactive and visually appealing manner, with at least 10 different dropdown options for users to select different facts and figures to display. The solution must be secure, efficient, and user-friendly, providing valuable insights and information about the data in the Phonepe pulse Github repository.")
    st.write("---")
    st.write("#")
cols = st.columns(len(Social_Media))
for index, (platform, link) in enumerate(Social_Media.items()):
 cols[index].write(f"[{platform}]({link})")



        

