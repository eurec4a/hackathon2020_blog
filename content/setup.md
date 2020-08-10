Title: Organizational Setup
Date: 2020-08-04 12:00
Category: general
Author: Heike Konow
Summary: This is an overview of the organization and setup for the first virtual EUREC4A Hackathon.
Tags: infrastructure

# The organizational setup for the EUREC4A Hackathon 2020

Aside from the scientific collaboration, we also wanted to use the the EUREC4A Hackathon to test online collaboration for the EUREC4A community. We thought of this hackathon as a test bed to explore virtual collaboration. Not only due to the current pandemic, but also because we are a very distributed community in general.

This article describes our setup for this online collaborative workshop, what we have learned and what we would do differently in the future.

## Workshop phases
The workshop was structured into two different phases: a preparation phase and a collaboration phase. During the **preparation phase**, the participants explored different topics that they would like to work on during the workshop. During workshop registration, a couple of possible topics were collected and then discussed and refined in different groups during preparation phase. Most of the participants knew ahead of the actual workshop what project they would like to work on. The **collaboration phase** took place over the course of three half days in the last week of July 2020.

## IT setup
In the beginning of the preparation phase, we started a channel on **Mattermost** ([mattermost.com](https://mattermost.com)) with all participants. This was our main way of communication to reach everyone involved. All information about the workshop was share through this channel.

While planning the workshop, we identified the need to have a place for everyone to share information, links, data, anything. We debated setting up a Wiki for this, but then landed on a **shared folder**. This folder was hosted on an OwnCloud instance and was accessible and editable for every participant. We used this from the organizational side to distribute participant lists, schedules, links, or introduction slides. From participant side, this was used to share Jupyter Notebooks, data sets, or links.

The center of our virtual collaborative workshop was the **video conference system**. By connecting via video, we could still try to emulate a sense of togetherness even when being distributed over several countries and continents. After a bit of testing and getting feedback from different participants which systems they could use and which not, we landed on [BigBlueButton](https://bigbluebutton.org). We used an instance hosted by CEN IT at Hamburg University.

## Agenda
The three half days of the workshop were split into discussions in plenum and _group work_. This was the general structure:

| Day 1                    | Day 2          | Day 3            |
| :----                    | :----          | :----            |
| Welcome and introduction | Open questions | Open questions   |
| _Group work_             | _Group work_   | _Group work_     |
| Daily roundup            | Daily roundup  | Workshop roundup |

We began and ended with plenum discussions to share the state of the work, communicate about different aspects of the workshop, and discuss open questions. In-between, participants dispersed into smaller working groups. Additionally, we agreed on times to have a common coffee break for everyone interested to build a sense of community.

Participants were located in Europe and the US. To accomodate the different time zones, the workshop took place from 12 to 17 UTC each day.

## Tips and tricks

We came up with a couple of tips and tricks as rules of communication for the virtual workshop.

* _Video on if possible:_ Video helps with nonverbal communication in an online setup. You can see if someone has left their computer, if they are distracted or if they want to say somenthing.
* _Audio off when in plenum:_ This helps reducing audio disruptions and echos. But it also reduces spontaneity in discussions. We found during the workshop that it could be helpful to leave audio on in smaller groups to have a more natural discussion.
* _Exclamation mark in chat:_ As a way to raise your hand, it is a good practise to post an exclamation mark. Not all video conference systems have the option for raising hands and the chat can be monitored by everyone and not only the moderator.
* _Stand up and walk away from the computer from time to time:_ Even though it is nice to be connected to the others during a workshop, it is important and sometimes also helpful to get up and walk away from time to time to clear your head and to stretch out. Videoconferencing for five hours straight would be a very long time and very hard.
* _Mattermost as main way of communication with everyone:_ We needed to identify one way of communication as a fallback option if everything else failed. We were especially unsure about the stability of the video conference system and needed a way to reach everyone in case we needed to switch platforms. Fortunately, this wasn't necessary. But it was still helpful to identify this as main communication channel, so that everyone knew how to reach all other participants.

## Video conference setup
As mentioned above, we decided to use BigBlueButton as our video conference platform.

### BigBlueButton
We used BigBlueButton that was hosted by CEN IT at Hamburg University. We tested the setup ahead of the workshop with a couple of people to see how the system would work on different platforms and with different browsers. We found that the video streams would increase the CPU load on the computers but in a range where working would hopefully still be possible.

### Meeting rooms
One way to facilitate a collaborative workshop atmosphere was to create opportunities to meet and discuss. This is why we came up with different virtual rooms. BigBlueButton offers running multiple meeting rooms in parallel and we created 10 rooms ahead of the workshop. One central meeting room was identified for everyone to meet in plenum or during coffee breaks and the others could be used for group discussions.

In an in-person workshop, people can walk around and go into different rooms and join different discussions. This is something we wanted to also have in our virtual workshop. We therefore collected a list of links to all meeting rooms and shared those with all participants. Since the experiment EUREC4A was centered on or close to Barbados, all rooms had names of places on Barbados. This made communication about the different rooms much easier. You didn't have to talk about URLs but simply name the room you were meeting in.

In the meeting rooms, every participant had moderator status to easily share screens or use whiteboard functionalities. This way, meetings could also be started by anyone.

## Ways of working
We did not define the way of collaborative work but we proposed different options. Code was often shared via GitHub or via the shared OwnCloud folder. We arranged for guest accesses to the supercomputer of the DKRZ ([Deutsches Klimarechenzentrum](https://www.dkrz.de)) and the associated file structure. Especially the JupyterHub running on the supercomputer was used for collaborative programming work during the hackathon.

## Lessons learned
Overall, we were very happy with how things went and how many productive discussions took place. If we would organize something similar again, this is what we would also think about:
* A list with important links is very helpful. This was created during the workshop and we collected links to different meeting rooms, the shared folder, access to the supercomputer, etc.
* To have a lively discussion with most people having their audio on, head sets are very important to reduce echo and other audio disruption.
* The initial discussions on the first day were sometimes a bit slow. People needed to get used to the format and get to know some people first. We would try to initiate these discussions already in the preparation phase of the workshop by having a short video meeting ahead of the actual workshop.
