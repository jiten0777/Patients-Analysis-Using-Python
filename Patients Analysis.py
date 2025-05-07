import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
data = pd.read_excel(r'C:\Users\Jitendra\PycharmProjects\Hospital project\.venv\Patients Data ( Used for Heart Disease Prediction ) (1).xlsx', engine='openpyxl')

# Check data
print(data.columns)
print(data.head())
print(data.isnull().sum())
print(data.duplicated().sum())

# Avg AgeCategory vs BMI - Bar Plot
Age_BMI_avg = data.groupby('AgeCategory')['BMI'].mean().sort_values(ascending=False).reset_index()
Age_BMI_avg['BMI'] = Age_BMI_avg['BMI'].round(2)  # Round BMI to 2 decimal places

fig1 = px.bar(Age_BMI_avg, x='AgeCategory', y='BMI', color='BMI',
              title='Average BMI by Age Category', text='BMI', color_continuous_scale='Reds')
fig1.update_layout(xaxis_title='Age Category', yaxis_title='Average BMI')
fig1.show()

# Gender Distribution
gender_count = data['Sex'].value_counts().reset_index()
gender_count.columns = ['Sex', 'Count']
fig2 = px.bar(gender_count, x='Sex', y='Count', color='Sex',
              title='Gender Distribution', text='Count', color_discrete_sequence=['red', 'blue'])
fig2.update_layout(xaxis_title='Sex', yaxis_title='Count')
fig2.show()

# BMI Histogram
fig3 = px.histogram(data, x='BMI', nbins=10, title='BMI Distribution', color_discrete_sequence=['green'])
fig3.update_layout(xaxis_title='BMI', yaxis_title='Frequency')
fig3.show()

# Health Condition by Age (Stacked Bar)
health_data = data.groupby('AgeCategory')[['HadDiabetes', 'HadHeartAttack']].sum().reset_index()
fig4 = go.Figure()
fig4.add_trace(go.Bar(x=health_data['AgeCategory'], y=health_data['HadDiabetes'], name='Diabetes', marker_color='orange'))
fig4.add_trace(go.Bar(x=health_data['AgeCategory'], y=health_data['HadHeartAttack'], name='Heart Attack', marker_color='red'))
fig4.update_layout(barmode='group', title='Health Conditions by Age Category',
                   xaxis_title='Age Category', yaxis_title='Number of Patients')
fig4.show()

# Patients Distribution by State (Pie Chart)
state_counts = data['State'].value_counts().reset_index()
state_counts.columns = ['State', 'Count']
fig5 = px.pie(state_counts, values='Count', names='State', title='Distribution of Patients by State',
              color_discrete_sequence=px.colors.qualitative.Pastel)
fig5.update_traces(textposition='inside', textinfo='percent+label')
fig5.show()

# Patients by State (Line Chart)
fig6 = px.line(state_counts.sort_values(by='Count', ascending=False), x='State', y='Count',
               markers=True, title='Number of Patients by State')
fig6.update_traces(marker=dict(color='red', size=8), line=dict(color='green'))
fig6.update_layout(xaxis_title='State', yaxis_title='Number of Patients', xaxis_tickangle=90)
fig6.show()

# BMI vs Weight (Scatter Plot by Sex)
fig7 = px.scatter(data, x='BMI', y='WeightInKilograms', color='Sex',
                  title='Scatter Plot of BMI vs Weight (Colored by Sex)',
                  color_discrete_map={'Male': 'black', 'Female': 'red'})
fig7.update_traces(marker=dict(size=10, line=dict(width=1, color='yellow')))
fig7.update_layout(xaxis_title='BMI', yaxis_title='Weight (kg)')
fig7.show()

# Smoking Status - Pie Chart
smoker_status_counts = data['SmokerStatus'].value_counts().reset_index()
smoker_status_counts.columns = ['SmokerStatus', 'Count']
fig8 = px.pie(smoker_status_counts, values='Count', names='SmokerStatus',
              title='Distribution of Patients by Smoking Status',
              color_discrete_sequence=['green','yellow','blue','red'])
fig8.update_traces(textposition='inside', textinfo='percent+label', pull=[0.05,0.03,0.03,0.02])
fig8.show()


