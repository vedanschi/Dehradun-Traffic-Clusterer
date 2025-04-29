# Dehradun Traffic Hotspot Analysis Using DBSCAN Clustering

**Artificial Intelligence and Machine Learning Project**  
Submitted by: Vedanshi Samant
B.Tech CSE

---

## Abstract

This project analyzes Dehradun's traffic congestion using DBSCAN clustering and linear regression. With GPS and timestamp data, it identifies high-density hotspots and predicts vehicle speeds. The lightweight model provides city planners with actionable insights for improving traffic flow and sustainability, even with minimal infrastructure.

---

## 1. Introduction

### 1.1 Context

Dehradun has seen a 300% increase in vehicle registrations since 2010. Key issues include:
- Major congestion at Clock Tower, Rajpur Road
- Peak hour speeds dropping to 18 km/h
- PM2.5 levels exceeding WHO limits at ISBT

### 1.2 Project Aim

To develop a machine learning tool that:
- Detects traffic hotspots
- Predicts vehicle speeds
- Assists in city planning and emergency routing

---

## 2. Motivation

Dehradun faces major delays (~45 min in rush hours), slow emergency responses (~25% slower), and high pollution (vehicular emissions ~40%). This project offers a cost-effective, data-driven traffic management alternative.

---

## 3. Related Work

- **Delhi (2021)**: K-Means clustering — ignored temporal shifts.
- **Bangalore (2022)**: Random Forest — accurate but costly IoT setup.
- **Our Approach**: DBSCAN + Linear Regression for scalable, noise-resistant clustering and simple, interpretable prediction.

---

## 4. Problem Statement

Challenges:
- Noisy and sparse GPS data
- Lack of smart infrastructure
- Rapid temporal traffic changes

Solution:
- Use open-source tools and basic data (GPS, timestamps)
- Leverage DBSCAN for clustering
- Apply linear regression for speed prediction

---

## 5. Methodology

### 5.1 Data Acquisition

- 1,000 simulated records over 30 days
- Features: latitude, longitude, timestamp, speed, vehicle count
- Normalization and timestamp-to-hour conversion for preprocessing

### 5.2 Clustering (DBSCAN)

- Handles GPS noise well
- Parameters tuned: `epsilon`, `min_samples`
- Identifies high-density (congested) vs sparse zones

### 5.3 Speed Prediction (Linear Regression)

- Predicts speed based on hour and cluster ID
- Simple, low-overhead model with reasonable accuracy

### 5.4 Visualization

- Matplotlib used for:
  - Cluster plots (color-coded)
  - Speed vs. time line graphs

---

## 6. Results and Analysis

### 6.1 Cluster Analysis

- **Rajpur Road**: Avg. 162.7 vehicles, 18.1 km/h
- **Prem Nagar**: Avg. 149.5 vehicles, 20.5 km/h
- **ISBT**: Avg. 146.2 vehicles, 20.7 km/h

### 6.2 Regression Analysis

- **R² score**: 0.582 (moderate fit)
- **RMSE**: 5.2 km/h (good for noisy data)

---

## 7. Applications

- **Smart Traffic Control**: Dynamic signals based on cluster centroids
- **Emergency Services**: Predict fastest routes using time-of-day data
- **Infrastructure Planning**: E.g., flyover proposed near Prem Nagar (120% congestion rise)

---

## 8. Conclusion

This project demonstrates:
- DBSCAN's effectiveness in identifying congestion zones
- Linear Regression's adequacy for basic speed prediction
- Feasibility of lightweight, open-source traffic analytics in cities with limited resources

### Future Work

- Integrate live APIs (Google Maps, MapMyIndia)
- Include weather data (rainfall, visibility, etc.)

---

## 9. References

1. Uttarakhand Transport Dept. (2022). *Vehicle Registration Report*
2. Times of India (2023). *Dehradun’s Traffic Nightmare*
3. Ester et al. (1996). *A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise*
4. Pedregosa et al. (2011). *Scikit-learn: Machine Learning in Python*
5. Times of India (2025). *Traffic diversions lead to congestion in Dehradun*  
   [Link](https://timesofindia.indiatimes.com/city/dehradun/traffic-diversions-amid-budget-session-lead-to-congestion-in-dehradun/articleshow/118365127.cms)

---
