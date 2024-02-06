import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import altair as alt

df1 = pd.read_csv('https://raw.githubusercontent.com/dimsdika12/Analyzing-User-Behavior-Divvy-Bike-2023/main/data_dashboard/dashboard_p1.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/dimsdika12/Analyzing-User-Behavior-Divvy-Bike-2023/main/data_dashboard/dashboard_p2.csv')
df2_1 = pd.read_csv('https://raw.githubusercontent.com/dimsdika12/Analyzing-User-Behavior-Divvy-Bike-2023/main/data_dashboard/dashboard_p2_1.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/dimsdika12/Analyzing-User-Behavior-Divvy-Bike-2023/main/data_dashboard/dashboard_p3.csv')
df4 = pd.read_csv('https://raw.githubusercontent.com/dimsdika12/Analyzing-User-Behavior-Divvy-Bike-2023/main/data_dashboard/dashboard_p4.csv')
df5 = pd.read_csv('https://raw.githubusercontent.com/dimsdika12/Analyzing-User-Behavior-Divvy-Bike-2023/main/data_dashboard/dashboard_p5.csv')
df6 = pd.read_csv('https://raw.githubusercontent.com/dimsdika12/Analyzing-User-Behavior-Divvy-Bike-2023/main/data_dashboard/dashboard_p6.csv')
image1 = Image.open('aset/bike.jpg')

st.set_page_config(
    page_title = 'Divvy Bike Share Trip',
    layout='wide'
)

st.header("Divvy Bike Share Trip 2023" )
st.write("")


tab1, tab2, tab3 = st.tabs(["About Divvy:bike:", "Pricing:dollar:","Analyzing:chart_with_upwards_trend:"])
with tab1:
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.image(image1, width=450)
    with col2:
        st.markdown('<p style="font-size: 24px; color: #FF69B4; font-weight: bold;"><span>About</span> <span style="color: #0077b6;">Divvy</span></p>', unsafe_allow_html=True)
        st.markdown('''
        <div style="text-align: justify">
        Divvy Bikes is a bike-sharing system operating in Chicago and Evanston.
        Owned by the Chicago Department of Transportation and run by Lyft Bikes and Scooters, LLC, it offers affordable transportation for locals and tourists alike.
        With bikes available 24/7, users can explore the cities at any time of the day, any day of the year.
        </div>
        ''', unsafe_allow_html=True)

with tab2:
    image2 = Image.open("aset/price.png")
    st.image(image2, width=600, caption='Price as of January 2024.')
with tab3 :
    st.markdown('''
    **Analyzing User Behavior Divvy Bike in 2023**
                
    **Project objectives :** 
    
    The analysis of Divvy Bike Rentals user behavior aims to provide comprehensive understanding to stakeholders.
    By understanding what users prefer, trends they follow, and how they behave, stakeholders can make smarter choices and enhance the performance of Divvy Bike Rentals.            

                
    **Defining Questions**

    1. What's the proportion of yearly members (member) versus daily users (casual) in using the bike rental service?

    2. How is bike usage divided by type in terms of percentage?

    3. What's the typical length of bike rentals on average?

    4. How did bike rental numbers change (trend) throughout 2023?

    5. Do the number of bike rentals vary significantly across different days of the week?

    6. What are the busiest and quietest times for bike rentals?            
                            
    ''')

st.write("")

total_rent, member_rider, casual_rider = st.columns(3)


with total_rent:
    total = df1['total'].sum()
    st.metric("Number of Rent", value="{:,}".format(total))
with member_rider:
    member = df1[df1['member_type'] == 'member']['total'].sum()
    st.metric("Member Rider", value="{:,}".format(member))
with casual_rider:
    casual = df1[df1['member_type'] == 'casual']['total'].sum()
    st.metric("Casual Rider", value="{:,}".format(casual))

st.markdown('''
    <div style="text-align: justify">
During 2023, Divvy recorded a total of 5,719,877 bike rentals.
Approximately 64% of these rentals, equivalent to roughly 3.7 million users, were from members,
whereas the remaining 36%, totaling 2 million rentals, were made by casual users.
</div>
    ''', unsafe_allow_html=True)

st.write("")
st.write("")
p2_chart,description_p2 = st.columns([1.5,1])

with p2_chart:
    chart_type = st.selectbox("Select",['Bike Type','Bike Type Used By Member Type'])
    
    if chart_type == "Bike Type":

        colors = ['#45a70b','#026590','#ff9999']

        df2['explode'] = [0.1 if bt == 'docked_bike' else 0 for bt in df2['bike_type']]

        fig1 = px.pie(df2, values='total', names='bike_type', title='Percentage of Bike Type Used', 
                color_discrete_sequence=colors, 
                hover_data=['total'], 
                hole=0.3,
                )
        fig1.update_traces(pull=[0.1 if bt == 'docked_bike' else 0 for bt in df2['bike_type']], 
                    textinfo='percent+label', 
                    insidetextorientation='radial')
        st.plotly_chart(fig1)

    else :
    
        fig2 = px.bar(df2_1, x='member_type', y='percentage', color='bike_type', barmode='group',
                 title='Distribution of Bike_Type_Usage by Member Type',
                 labels={'percentage': 'Percentage', 'member_type': 'Member Type', 'bike_type': 'Bike Type'},
                 color_discrete_sequence=[ '#026590', '#ff9999','#45a70b'])

        st.plotly_chart(fig2)


           
with description_p2:
    st.write("")
    st.write("")
    st.markdown('''
    <div style="text-align: justify">
    Electric bikes lead in terms of usage, constituting the highest proportion at 51.5%, 
    followed by classic bikes at 47.1%, with docked bikes making up the remaining 3.8%.

                
    Further analysis reveals that among casual riders, 53.61% opt for electric bikes, 42.58% prefer classic bikes, and the remaining 3.80% select docked bikes.
    Conversely, among members, 50.31% favor electric bikes, and 49.69% prefer classic bikes.
                
    Note: Based on the available data, as of September 2023, there are no longer docked bike types available in Divvy's service.
    As of January 2024, Divvy offers three types of bikes: Classic, Scooter, and Ebike.
    </div>
    ''', unsafe_allow_html=True)

description_p3,chart_p3 = st.columns([1,1.5])

with description_p3:
    st.write("")
    st.write("")
    st.markdown('''
    <div style="text-align: justify">
    On average, casual riders typically spend 32 minutes riding electric bikes and 14 minutes riding classic bikes. 
    In contrast, member riders have an average duration of 14 minutes for classic bikes and 11 minutes for electric bikes.

    In general, casual riders invest more time in bike rentals compared to member riders, regardless of whether they're using classic bikes or electric bikes. 
    However, in the case of classic bikes, casual riders notably spend more time (32 minutes) compared to member riders (14 minutes).
    </div>
    ''', unsafe_allow_html=True)
with chart_p3:
    # Plot menggunakan Plotly Express
    fig3 = px.bar(df3, x='avg_duration', y='member_type', color='bike_type',barmode='group',
               title='Average Bike Rental Duration',
               labels={'avg_duration': 'Average Duration (menit)', 'member_type': 'Member Type', 'bike_type': 'Bike Type'},
               color_discrete_sequence=['#026590', '#45a70b'])

    # Menampilkan plot di Streamlit
    st.plotly_chart(fig3)


freq = st.selectbox("Freq", ['Daily','Monthly'])

timeUnit = {
    'Daily':'yearmonthdate',
    'Monthly':'yearmonth'
}
st.header("Bike Rental Trend")
if freq == 'Daily':
    sales_line = alt.Chart(df4).mark_line().encode(
        alt.X('date', title='Order Date', timeUnit=timeUnit[freq]),
        alt.Y('total', title='Number of Bike Rental', aggregate='sum')
    )

    st.altair_chart(sales_line,use_container_width=True)
else:
    sales_line = alt.Chart(df4).mark_bar().encode(
        alt.X('date', title='Order Date', timeUnit=timeUnit[freq]),
        alt.Y('total', title='Number of Bike Rental', aggregate='sum')
    )
    st.altair_chart(sales_line,use_container_width=True)

st.markdown('''
    <div style="text-align: justify">
    Divvy bike usage shows a noticeable pattern that changes with the seasons, greatly affected by the weather.
    More individuals choose to rent bikes during the spring and summer seasons, reaching its highest point in August with an impressive 771,693 Monthly Bike Rentals.
    Conversely, during autumn and winter, there's a considerable decrease in the number of users, hitting its lowest level in January with about 190,301 Monthly Bike Rentals.
    ''', unsafe_allow_html=True)


chart_p5,description_p5 = st.columns([1.5,1])
with chart_p5:
    fig5 = px.bar(df5,x='day_name', y='total', color='member_type',barmode='group',
              title='Daily Bike Rentals by Day of Week',
              labels={'day_name':'Day','total':'Number of Bike Rentals'},
              color_discrete_sequence=['#026590', '#45a70b'])

    st.plotly_chart(fig5)
st.write("")
with description_p5:
    st.write("")
    st.write("")
    st.markdown('''
    <div style="text-align: justify">
    Analyzing the daily bike rentals based on the day of the week shows clear differences in patterns between member and casual riders.

                            
    Members tend to be more active on weekdays, but their activity decreases notably during the weekend.
    In contrast, casual riders are more active during the weekend, especially on Fridays, which stands out as their busiest day.
                
    This emphasizes a distinct usage trend, where members prefer weekdays while casual riders lean towards weekends, especially Fridays.
    </div>
    ''', unsafe_allow_html=True)
       
fig6 = px.bar(df6,x='hour', y='total', color='member_type',barmode='group',
              title='Rush Hour Bike Rental',
              labels={'hour':'Hour','total':'Number of Bike Rentals'},
              color_discrete_sequence=['#026590', '#45a70b'])

fig6.update_xaxes(tickmode='linear', dtick=1)
fig6.update_layout(width=1200)
st.plotly_chart(fig6)

st.markdown('''
    <div style="text-align: justify">
Both casual and member riders are frequently renting bikes between 7 AM and 5 PM, with the highest activity recorded at 5 PM.
Following this, bike rentals steadily decrease post 5 PM, reaching their lowest point around 4 AM.
However, member riders experience two peaks in activity — the first peak happens at 8 AM, followed by another peak at 5 PM.
</div>
    ''', unsafe_allow_html=True)

st.write("")
st.write("")

st.subheader('Recommendation Action')
st.write("")
st.markdown('''
    <div style="text-align: justify">
    Based on the data obtained from Divvy bike rentals in 2023, here are some recommendations for stakeholders:

1. **Membership Promotion Strategies**: Given that a significant portion of bike rentals comes from members, there should be continued efforts to promote and incentivize membership subscriptions. This could include offering discounts for long-term memberships or introducing loyalty programs to encourage repeat usage.

2. **Electric Bike Investment**: Since electric bikes constitute the highest proportion of usage among both casual and member riders, investing in expanding the fleet of electric bikes could attract more users and enhance overall customer satisfaction.

3. **Optimizing Rental Duration**: Understanding that casual riders tend to spend more time on bike rentals compared to members, there could be strategies to encourage longer rental durations among members, such as offering bundled rental packages or discounts for extended usage periods.

4. **Seasonal Variations Management**: Acknowledging the seasonal fluctuations in bike rentals, Divvy can adjust its operational capacity and marketing efforts accordingly. During peak seasons like spring and summer, additional bikes and staff may be required to meet the increased demand, whereas promotional offers during off-peak seasons could help stimulate usage.

5. **Weekday vs. Weekend Strategies**: Divvy should tailor its marketing and operational strategies to accommodate the different usage patterns between weekdays and weekends. For example, focusing promotional campaigns targeted towards members on weekdays and offering special weekend deals to attract casual riders can help optimize usage throughout the week.

6. **Peak Hours Management**: Understanding the peak hours of bike rentals, especially the dual peaks experienced by member riders, Divvy can deploy resources effectively to ensure sufficient bike availability and streamline rental processes during these times. Additionally, targeted promotions or incentives during off-peak hours could help redistribute demand more evenly throughout the day.

By implementing these recommendations, Divvy can enhance user experience, increase ridership, and maximize the utilization of its bike rental service.        
    
</div>
    ''', unsafe_allow_html=True)


