![banner](assets/cgs.png)


![Python version](https://img.shields.io/badge/Python%20version-3.10%2B-lightgrey)
![GitHub last commit](https://img.shields.io/github/last-commit/aruryss/CodeGirlSummer2023Analytics)
![GitHub repo size](https://img.shields.io/github/repo-size/aruryss/CodeGirlSummer2023Analytics)

# Coding Camp Promo-campaign and Admission Analytics


## Authors

- [@aruryss](https://www.github.com/aruryss)

## Table of Contents

  - [Questions and Hypothesis](#questions--hypothesis)
  - [Approach and Analysis](#approach--analysis)
  - [Technical challenges](#technical-challenges)
  - [Tech Stack](#tech-stack)
  - [Quick glance at the results](#quick-glance-at-the-results)
  - [Assumptions and Limitations](#assumptions--limitations)
  - [Data Analysis](#q1-Educational-background-and-Acceptance-rate)
  - [Deeper analysis](#Deeper-analysis)
  - [Final results](#Final-results)
  - [Future Improvements](#Future-Improvements)
##
As Code Girl Summer 2023 free web development camp for girls of age 15 to 18, organized by NU ACM-Women Student Chapter came to an end, I conducted the analysis of our **promo campaign** and **educational biases** we might have during the admissions process to improve accessibility and popularity of our events.


## Questions & Hypothesis

**Q1:** Does educational background affect acceptance rate?

**H1:** _Yes, I believe that students of some institutions make up larger parts of the participants._
##

**Q2:** Which Instagram influencer drove the most traffic?

**H2:** _As some people mentioned Instagram influencer “same.ke” in their motivational letters, I believe it is “same.ke”._
##

**Q3:** Does the following of an Instagram influencer impact number of applications?

**H3:** _Yes, I think number of followers is directly proportional to the reached audience and potential applicants._
##

**Q4:** Does the engagement of an Instagram influencer impact number of applications?

**H4:** _Yes, I think engagement of the audience is directly proportional to the number of applicants_
## Approach & Analysis

1. Data was collected from applicants and participants of the camp via Google Forms.
2. Cleaned and formatted into 2 datasets of applicants and participants.
3. Columns of Education, Track-chosen, Track-final, Traffic and Timestamp were presumed to be necessary to answer the questions.
4. Instagram influencer data set with necessary data was collected and formatted by hand.
5. Graphical visualisation and statistic inference were incorporated.

## Technical challenges

- Datasets of applicants and participants were cleaned by removing duplicate values for education (Ex.:Nazarbayev University and Nazarbayev university) and removing column with motivational letters in Google Sheets
- Datasets of applicants and participants had missing value in the column Traffic, thus they were filled using Python3 Pandas library
## Tech Stack

- Python3
  - Libraries: Pandas, Seaborn, MatPlotLib, NumPy, and DateTime


## Quick glance at the results

Correlation between the features of applicants.

![heatmap](assets/applicants-heat-map.png)

Correlation between the features of participants.

![heatmap](assets/participants-heat-map.png)

Correlation between the features of influencers.

![heatmap](assets/influencers-heat-map.png)

Acceptance rate per Educational Institution.

![heatmap](assets/acceptance-rates.png)

Application amounts by day with Instagram Influencers' repost days highlighted.

![heatmap](assets/applications-timeline.png)


## Assumptions & Limitations

Several **assumptions** that I made for the analysis were:

1. Applications were driven by Instagram influencers **solely** within **5-day-window** of them posting about camp
2. Educational institution indicated by applicants is their primary source of learning
3. Engagement is defined as the number of likes under the **last 6 Instagram posts** prior to the date of camp advertisement divided by the number of followers
4. Number of following of and Instagram account was regarded as of **September 3rd 2023**

Thus, **limitations** of the analysis are the following:

1. All those who indicated their source of traffic to be Instagram, were counted towards the amount of influencers’ traffic, if within the 1-day-window (lifespan of Instagram Stories used to advertise camp), as I could not tell for sure whether they learned about camp through their Explore page, native post or video.
2. Girls could be studying in other institutions for way longer before the one they indicated, but I cannot track all educational history, thus I refer to the one they indicated as primary one.
3. Engagement in Instagram is calculated with many factors in mind, but it is private to each user, thus I took available to me interactions with influencers’ permanent content to be engagement.
4. Due to Instagram limitations, there is no publicly and privately available information on follower count at certain date, thus I regarded follower count on [DATE TAKEN] for analysis.

## Q1: Educational background and Acceptance rate
Firstly, let's take a look at the acceptance rate per educational institution.

![heatmap](assets/acceptance-rates.png)

As we can see Binom, NIS, and NU have the highest acceptance rates amongst all. As admissions was heavily dependent on the motivational letter, there is a possibility of those educational institutions providing more high-quality writing classes and access to such trainings that affect the quality of the letter. Thus, educational background did affect chance of acceptance into the camp.

Conclusion: To increase the acceptance rate of schoolgirls in ordinary schools, we will include a list of questions they should answer in their motivational letter rather than relying on their understanding of the format.

## Q2: Which Instagram influencer drove the most traffic?
From the applications timeline, it is evident that most applications were submitted after influencer 'same.ke' reposted our camp announcement and promo-video.

![heatmap](assets/applications-timeline.png)

He put a lot of effort into his repost as he recorded a video and included a link to registration for the camp. The analysis made it evident that his effort correlated with the traffic he brought.

Conclusion: Collaborate with influencers who make a talking video and include all the links to the event in future initiatives.

## Q3 & Q4: Does the following & engagement of an Instagram influencer impact the amount of applications?

![heatmap](assets/influencers-heat-map.png)

There is a correlation between follower count and engagement, both of which are the highest for 'same.ke', the influencer who drove the most amount of applications as discussed previously.

Conclusion: Collaborate with influencers with high engagement and follower count whose primary demographic are young women interested in IT.

## Deeper analysis

As applicants had an opportunity to choose their track of learning (Frontend & Backend), I wondered whether their preference affected their acceptance rate.

![heatmap](assets/track-rates.png)

As can be seen in the graph above, those who chose Frontend track had a 6.5% higher acceptance rate than those who chose Backend track, despite those tracks having the same capacity. This could be affected by multiple factors, such as: educational background of applicants, and quality of their motivational letter.

## Final results
***Q1:** Does educational background affect acceptance rate?

**Answer:** _In a sense, the highest acceptance rates were among the educational institutions for gifted children in Kazakhstan, but there was a factor of chosen track that also affected the acceptance rate._
##

**Q2:** Which Instagram influencer drove the most traffic?

**H2:** _Instagram Influencer 'same.ke' drove the highest traffic._
##

**Q3:** Does the following of an Instagram influencer impact number of applications?

**H3:** _Yes, the number of followers is directly proportional to the traffic driven._
##

**Q4:** Does the engagement of an Instagram influencer impact number of applications?

**H4:** _Yes, the audience engagement with the content is directly proportional to the traffic driven._

## Future Improvements
- Track the audience engagement of our own Instagram account, as it is the main platform of our promo-campaign and should be reffered as primary source of traffic
- Implement Natural Language Processing model for Russian Language to process quality of the motivational letters to better assess biases during admissions and factors affecting acceptance rates
- All the conclusions derived from the analysis above will be implemented into our upcoming events to increase the quality and accessibility of tech events for girls in Kazahstan.

## Repository structure


```

├── assets
│   ├── cgs.png                                   <- banner used in the README.
│   ├── acceptance-rates.png                      <- acceptance rate per educational institution plot used in the README.
│   ├── applications-timeline.png                 <- applications per day coming from Instagram plot used in the README.
│   ├── influencer-heat-map.png                   <- influencer metrics correlation heat map used in the README.
│   ├── track-rates.png                           <- acceptance rate per learning track plot used in the README.
│   ├── applicants-heat-map.png                   <- applicant attributes correlation heat map used in the README.
│   ├── participants-heat-map.png                 <- participant attributes correlation heat map used in the README.
│
├── datasets
│   ├── influencer.csv                    <- the dataset with Instagram Influencer profile information.
│   ├── participants.csv                  <- the dataset with participant information.
│   ├── registered.csv                    <- the dataset with applicant information.
│
│
├── README.md                                     <- this readme file.
```
