import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
st.set_page_config(page_title="Speed of Sound Experiment", layout="wide")
st.title("Determining Speed of Sound using Ultrasonic Sensor(HCSR04)")
data = pd.read_csv("./datasets/data_copy.csv")
st.header("Aim")
st.latex(r"""
\text{The aim of this experiment is to determine the speed of sound } 
\text{using data from the HC-SR04 Ultrasonic Sensor.}\\[8pt]
\text{Using statistical methods such as regression and correlation,} 
\text{we analyse the relationship between the dependent and independent variables.}\\[8pt]
\text{Regression also allows us to extrapolate the data and obtain an accurate slope } 
\text{compared to the raw measurements.}\\[8pt]
\text{(The temperature during the experiment was } 25^\circ\text{C--}26^\circ\text{C.)}
""")

st.header("Experiment Setup")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("./assets/apparatus-1.jpg")
with col2:
    st.image("./assets/apparatus-2.jpg")
with col3:
    st.image("./assets/apparatus-3.jpg")
with col4:
    st.image("./assets/schematic.png")
st.header("Experiment Data")
st.write(data)
data.describe()
st.header("Procedure")
st.latex(r"""
\textbf{Introduction}\\[6pt]
\text{First, an apparatus was constructed (temperature: }25^\circ\text{C--}26^\circ\text{C) that emits a sound wave } 
\text{and measures the time taken for the reflected wave to return.}\\[6pt]
\text{For this purpose, the HC-SR04 Ultrasonic Sensor was used in combination with a Raspberry Pi Pico } 
\text{to simplify the data collection process. The apparatus was set up as shown in the schematic above.}\\[12pt]

\textbf{Data Collection and Processing}\\[6pt]
\text{After collecting the data, it was converted from raw readings into a CSV file to enable easier manipulation. } 
\text{Python was used to convert the raw data to CSV format, and both Python and R were used for data analysis.}\\[6pt]

\textbf{Raw Data and Summary}\\[6pt]
\text{A data frame was created from the dataset. Out of the three available columns, the two used for analysis were } 
\text{the distance of the object from the sensor and the time taken for the echo to return.}\\[6pt]
\text{Since the measured time corresponds to a round-trip (sensor to object and back), the time values were divided } 
\text{by 2. The file \texttt{data\_copy.csv} contains this processed data.}\\[6pt]
\text{A correlation analysis was performed to verify whether the relationship between distance and time was linear.}\\[12pt]

\textbf{Correlation and Linearity}\\[6pt]
\text{Data was then plotted in R using a line plot, which clearly showed a linear relationship between the variables. } 
\text{Instead of directly computing the slope from raw data, a regression model was used to extrapolate the values } 
\text{to larger sample points.}\\[6pt]

\textbf{Result}\\[6pt]
\text{The regression model produced a slope of } 342.99\ \text{m/s, which successfully matches the } 
\text{theoretical speed of sound. The resulting plot also exhibited perfect linearity.}
""")

#data.select_dtypes(include=["float64"]).columns
plt.plot(data['Distance(m)'], data['Time(s)'], color='red')
plt.title('Distance(in meters) vs. Time(in seconds)')
plt.ylabel('Time(seconds)')
plt.xlabel('Distance(meters)')
st.header("Plotting Raw Data")
st.pyplot(plt)
data2 = pd.read_csv("./datasets/data1.csv")
plt.hist(data2['Temp(C)'], bins=20)
plt.xlabel('Temparature(in celcius)')
plt.ylabel('Count')
plt.show()
st.header("Frequency of Temparature")
st.pyplot(plt)
print("Median of Temparature - ", np.median(data2['Temp(C)']))
print("Mean of Temparature - ", np.mean(data2['Temp(C)']))
print("Mode of Temparature - ", data2['Temp(C)'].mode()[0])
from sklearn.linear_model import LinearRegression
distance = data[['Distance(m)']]
time = data['Time(s)']
sound_model = LinearRegression()
sound_model.fit(distance, time)
print(type(data[['Distance(m)']].values[0][0]))
st.subheader("📌 Temperature Summary")
colA, colB, colC = st.columns(3)
with colA:
    st.metric("Median", f"{np.median(data2['Temp(C)']):.2f} °C")
with colB:
    st.metric("Mean", f"{np.mean(data2['Temp(C)']):.2f} °C")
with colC:
    st.metric("Mode", f"{data2['Temp(C)'].mode()[0]:.2f} °C")
import random
test_arr = list()
# Distance is being randomly generated and 40 is the upper limit since 40 samples in the original dataset
for i in range(40):
    r_val = random.uniform(100, 10000)
    test_arr.append([r_val])
st.header("Random Values of Distance for Extrapolation")
st.code(test_arr)
y_pred = sound_model.predict(test_arr)
plt.plot(test_arr, y_pred, color='green')
plt.xlabel('Distance(m)')
plt.ylabel('Time(s)')
plt.title('Graph for the extrapolated values')
plt.show()
st.header("Plotting Extrapolated Data")
st.pyplot(plt)
st.header("Final Equation Obtained")
st.latex("Distance = 5.563 * 10^-8 + 342.99 * Time")
st.latex(r"""
\text{The equation has an intercept of the order } 10^{-8}, 
\text{ which represents the distance when } t = 0.\\
\text{Since it is negligible, we can ignore it and use } d = vt, \\
\text{where } v = 342.99\ \text{m/s} \approx 343\ \text{m/s.}
""")
st.success("Analysis completed successfully!")