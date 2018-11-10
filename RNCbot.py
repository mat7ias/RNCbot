#Load bot token
"bot_token": YOUR_BOT_TOKEN

#Flood filter
"previous_user_id": 0
"msg_count": 0

#Messages
pmme: >
   This response is too long for group chats. PM me @RaidenCommunityInfoBot

commands: >
   My commands:
   /resources
   /videos
   /pulse
   /events
   /rules
   /adminlist
   /previousevents
   /uraiden
   /adminpolicy

start: >
   Hi

heybot: >
   Hey

resources: >
   Raiden Network resources:
   [Website](https://raiden.network/)
   [FAQ](https://raiden.network/faq.html)
   [Github](https://github.com/raiden-network/raiden)
   [Raiden Explorer](https://explorer.raiden.network/)
   [Raiden Network Roadmap](https://raiden.network/roadmap.html)
   [Documentation](https://readthedocs.org/projects/raiden-network/)
   [Specification PDF](https://media.readthedocs.org/pdf/raiden-network-specification/latest/raiden-network-specification.pdf)
   [Medium Publications](https://medium.com/@raiden_network)
   [Weekly Github Update](https://reddit.com/user/bor4/posts/)

events: >
   Upcoming Events:
   TBD

previousevents: >
   Recent Events:
   9/11 - [Raiden Workshop: lightning payment solution for Ethereum with its creators](https://eventbrite.es/e/entradas-raiden-workshop-lightning-payment-solution-for-ethereum-with-its-creators-52005322319)
   8/11 - [Discover Raiden, a lightning payment solution for Ethereum](https://meetup.com/Devcentralised-Developing-DApps-Barcelona/events/255964749/)
   31/10-2/11 - [Devcon4](https://devcon4.ethereum.org/)
   29/10 - [The Future of LAYER 2: Prague Edition](https://www.eventbrite.com/e/the-future-of-layer-2-prague-edition-tickets-51535876193)
   1/10-31/10 - [Hacktoberfest](https://github.com/raiden-network/raiden/labels/hacktoberfest)
   5/9 - [Full Node: Mass adApption & use-cases](https://eventbrite.com/e/mass-adapption-use-cases-golem-raiden-status-tickets-49559434603)
   7/9-9/9 - [ETHBerlin Scaling & Interoperability Panel](https://ethberlin.com/)
   28/8 - [Copenhagen Ethereum Meetup](https://twitter.com/raiden_network/status/1030051960949551109)
   19/7-20/7 - [DappCon Lefteris and Augusto](https://dappcon.io/#speakers)
   30/6-1/7 - [Off The Chain Workshop in Berlin](https://binarydistrict.com/courses/master-workshop-off-the-chain/)
   18/5 - [State Channel Panel for Boston layer 2 scaling](https://workshopbostonblockchaincommunity.com/)

videos: >
   Raiden Network videos/presentations:
   [Raiden youtube channel](https://youtube.com/channel/UCoUP_hnjUddEvbxmtNCcApg)
   [Brainbot Technologies channel](https://youtube.com/channel/UCAfSoSy9FK5UqlSxqcsQElA/videos)
   [Devcon1](https://youtu.be/h791zjvf3uQ) - Heiko
   [Devcon2](https://youtu.be/4igFqFqQga4) - Heiko
   [Berlin Ethereum 2016](https://youtu.be/JuVP4iDVkoQ) - Lefteris
   [Oktahedron podcast](https://oktahedron.diskordia.org/?podcast=oh007-raiden#t=1:56.687) - Augusto
   [Devcon3](https://youtu.be/00RPE96LRVM) - Lefteris
   [Asseth](https://youtu.be/93qOwUSj4PQ) - Lefteris
   [Edcon 2018](https://youtu.be/VsZuDJMmVPY?t=7h45m51s) - Lefteris
   [L2 Summit State Channel Panel](https://youtu.be/jzoS0tPUAiQ?t=2h10m9s) - Lefteris
   [Off The Chain presentation](https://youtu.be/8Duil4pLzhI) - Lefteris
   [DAPPCON 2018](https://youtu.be/hSMIpl6e_Ow) - Lefteris
   [DAPPCON 2018 Panel Talking State Channels and Plasma](https://youtu.be/zmS0i3ZQZak) - Lefteris
   [Ethereum Asia Tour](https://youtu.be/MI5vgqq1hzA) - Jacob
   [Copenhagen Ethereum Meetup](https://youtu.be/arecj2vyjlE) - Jacob
   [Tackling Scalability Panel](https://youtu.be/AH2g-KpPk7w) - Lefteris
   [Mass Adoption and Use-Cases](https://youtu.be/GrWqRVDOC4M) - Lefteris
   [ETHBerlin](https://view.ly/v/MrLm3vSB1XEK) - Lefteris
   [Raiden Network Web Application Demo](https://youtu.be/ASWeFdHDK-E)

uraiden: >
   MicroRaiden:
   [uRaiden Github](https://micro.raiden.network/)
   [uRaiden Codebase](https://github.com/raiden-network/microraiden)
   [uRaiden Docs](https://microraiden.readthedocs.io/en/docs-develop/)
   [uRaiden Dev Chat](https://gitter.im/raiden-network/microraiden)
   [uRaiden Demo](https://demo.micro.raiden.network/)
   MicroRaiden videos:
   [Presentation Devcon3](https://youtu.be/yx0__aFvjzk?t=9m35s) - Loredana
   [Berlin Meetup drone demo](https://youtube.com/watch?v=E6CIgJPxgpQ) - Loredana
   [ScalingNOW!](https://youtu.be/81gK-5qLFeg) - Loredana

whenmoon: >
   The speed of light is 299.8km/s (or 299.792.458m/s). Average distance to the Moon is 384400km at the closest two points. 1.28 seconds on average for information traveling at the speed of light to reach the Moon.
   Although I think we can be more accurate about When Moon since the distance fluctuates between 363104-405704km. Which means that if we ignore computation/processing time the shortest time to the moon is 1.21 seconds ([time for light to reach the surface of the Moon from the Earth](https://i.imgur.com/nj8q3db.png)).
   For the longest time, we need to do a bit more and make some assumptions. First is that being the longest distance also implied that we have no direct line of sight and that we will need to send our Raiden Network transfer with the help of satellites. [OneWeb are setting up satellites with a low earth orbit of 1200km](https://en.wikipedia.org/wiki/OneWeb_satellite_constellation) so let's assume that's our satellite orbit for the Earth.
   For the Moon, we will also need to send the Raiden Network transfer to the furthest point and again need to use satellites. The lowest realistic lunar orbit is 15km (to avoid hitting lunar mountains, [which reach heights of 6.1km](https://en.wikipedia.org/wiki/Lunar_orbit).
   So now we need to find the distance [for this path](https://i.imgur.com/a8VxSnm.png). With some quick maths, we can figure this distance out as such [this](https://i.imgur.com/1zNeIMt.png) and our final maximum distance being a total of 431538km. Again if we ignore computation/processing time between the Payee and Payer then we have a maximum transfer time of 1.44 seconds.
   I am happy to officially announce that Raiden Network will Moon in 1.21-1.44 seconds once the milestone is reached in Q4 2018.Hope this helps!

rules: >
   Raiden Network Community telegram channel rules:
   1) This channel is about freedom of speech, but please keep in mind that it has its limits. Passionate debate is welcome, but unreasonable disrespect to any fellow members of the group (and especially the Raiden team) will not be tolerated. Doing so may result in your message being removed (this will be discussed with you in private messages).
   2) Not allowed: referral links unrelated to Raiden, telegram channel links, self promo media, pump and dump groups, NSFW content,  excessive swearing, spam in general, doxxing.
   3) Excessive trolling will result in removed messages.
   4) Please stay on topic, this channel is about the Raiden Network and scaling.

adminlist: >
   RNC Admin List:
   Boris - @BOR44
   Emil - @emiliorull
   Chomsky - @Chomsky12
   Ryan - @R2theD2
   Tim - @Kaleaso
   Hudazara - @Hudazara
   Mattias - @Mat7ias

ignorethat: >
   I'm not sure I want to ignore that...

devcon: >
   Devcon4 has finished but here's some past resources!
   [Agenda](https://docs.google.com/spreadsheets/d/e/2PACX-1vTmQ1maZLMDSo3r7wVCzwMadNUCGctmE5byRgv1za6R52wTUgZw-XB9P9dNO7-QBRka1AAwKrXO4kTP/pubhtml)
   [Livestream](https://devcon4.tv/)
   [Guidebook](https://guidebook.com/guide/117233/)
   [Handy Devcon Events summary by EthereumJesus](https://docs.google.com/spreadsheets/d/1gGlIdmx4AjtvRviAgL-PmqsO9y0-Lo2XXM5BHK_n188/edit#gid=0)
   [Guide to Layer 2 at Devcon](https://www.reddit.com/r/raidennetwork/comments/9sx9d0/con_a_guide_to_layer_2_and_scaling_at_devcon/)

pulse: >
   Raiden Pulse:
   [Raiden Pulse #1: News from July and August](https://medium.com/raiden-network/raiden-pulse-1-news-from-july-and-august-423fae4e9d3e)
   [Raiden Pulse #2: News from September and October](https://medium.com/raiden-network/raiden-pulse-2-news-from-september-and-october-6a6c6be8ad67)
