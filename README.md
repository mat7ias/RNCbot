# Awesome Raiden

### Resource Contents

- [Raiden Network](#raiden-network)
  - [Specifications](#specifications)
- [Developer Resources](#developer-resources)
  - [Tools](#tools)
  - [RNapps](#rapps)
  - [Hackathon](#hackathon) (BEYOND BLOCKCHAIN June 24th, 2019 - July 10th, 2019)
  - [Ether Faucets](#ether-faucets)
  - [dApp Testing](#dapp-testing)
- [Explorers](#explorers)
- [Learning Resources](#learning-resources)
  - [Talks](#talks)
  - [Research Calls](#research-calls)
  - [Pulse](#pulse)
- [Other Resources](#other-resources)
- [Community](#community)
  - [Community Channels](#community-channels)
- [Raiden Trust](#raiden-trust)
- [MicroRaiden](#microraiden)
  - [MicroTalks](#microtalks)
- [Misc. Bot Functions](#misc-bot-functions)

# Raiden Network

- [Website](https://raiden.network/)
- [Github](https://github.com/raiden-network/)
- [Dev Chat](https://gitter.im/raiden-network/raiden)
- [Reddit](https://www.reddit.com/r/raidennetwork)
- [Twitter](https://twitter.com/raiden_network)

### Specifications

- [Raiden Network Documentation (stable)](https://raiden-network.readthedocs.io/en/stable/)
- [Raiden Network Specification (latest)](https://media.readthedocs.org/pdf/raiden-network-specification/latest/raiden-network-specification.pdf)
- [Raiden Services Documentation (latest)](https://raiden-services.readthedocs.io/en/latest/)
  - [Monitoring Service](https://raiden-network-specification.readthedocs.io/en/latest/monitoring_service.html)
  - [Pathfinding Service](https://raiden-network-specification.readthedocs.io/en/latest/pathfinding_service.html)
  - [Smart contracts for Raiden Services](https://raiden-network-specification.readthedocs.io/en/latest/service_contracts.html)

## Developer Resources

- [Workshop](https://workshop.raiden.network)
- [Raiden Workshop Configurator](https://workshops.raiden.network/) - host a Raiden workshop or meetup
- [Releases List](https://github.com/raiden-network/raiden/releases) (+[nightly releases](https://raiden-nightlies.ams3.digitaloceanspaces.com/index.html))

<sub><sup>Note: The following sections include WIP and demo projects.</sup></sub>
### Tools

- [Docker Hub](https://hub.docker.com/r/raidennetwork/raiden) and Use Docker, Infura.io to [Build Raiden Network on Ubuntu 18.04](https://medium.com/@szhao_31738/use-docker-infura-io-to-build-raiden-network-on-ubuntu-18-04-a5eae7357f61) tutorial
- PyPI for [Raiden](https://pypi.org/project/raiden/) and [Raiden Services](https://pypi.org/project/raiden-services/)
- [DAppNode](https://github.com/dappnode/DAppNodePackage-raiden) (+[DAppNode docs](https://dappnode.github.io/DAppNodeDocs/install/) +[testnet version](https://github.com/vdo/DAppnodePackage-raiden-testnet)) - DAppNode package for the Raiden network
- [Raiden Scenario Player](https://github.com/raiden-network/scenario-player) - integration testing tool
- [Homebrew Tap](https://github.com/raiden-network/homebrew-raiden) for Raiden
- [WebUI](https://github.com/raiden-network/webui) - Raiden Web User Interface
- [Test environment scripts](https://github.com/kelsos/test-environment-scripts) - a collection of scripts used to bootstrap a test raiden environment
- [Raiden Express Server](https://github.com/TarCode/raiden-express-server) and [Raiden React Client](https://github.com/TarCode/raiden-react-client) - an Express Server that connects to a Raiden Client
- [Parity Docker Raiden dev env](https://github.com/calinchiper/parity-docker-raiden-dev-env) - Dockerized POA Parity blockchain + Raiden network contracts deployment scripts & config generator
- [Token Network's Channels](https://github.com/manuelwedler/token-network-channels) - Small dApp displaying Token Network's Channels (part of the Raiden network)
- [Raiden Invoice](https://github.com/ChaeByunghoon/raiden-invoice) and [Invoice Server](https://github.com/ChaeByunghoon/raiden-invoice-server) - A library for encoding and decoding Raiden network payment requests
- [Go Raiden Client](https://github.com/cpurta/go-raiden-client) - A Raiden node client written in Go


### Rapps

- [Grid Ethereum Plugin](https://github.com/PhilippLgh/ethereum-grid-tutorials/blob/cfb3b205374a34550e43cdbdbb4ec7e90a2d4bf4/Raiden.md) - the functionality with a plugin and a Web UI
- [Fairspot](https://github.com/ilinzweilin/ethCapeTown) - WiFi internet access on the go (in 100kb chunks) using Raiden
- [NUtube](https://nutube.network/#/), [Github](https://github.com/CryptoManiacsZone/nuTube.network), [demo](https://www.youtube.com/watch?v=Tx-j0TubY7k) - decentralized P2P live streaming w/ micropayments
- [DTok](https://github.com/ethcapetown/burner-wallet/tree/dtok-raiden), [demo](https://www.youtube.com/watch?v=2CFAJCfKs-8) - decentralized streaming and tipping platform w/ Raiden, BurnerWallet ([link](https://github.com/austintgriffith/burner-wallet)) and ENS domains
- [Raiden Light Client](https://github.com/raiden-network/light-client) - Raiden Light Client SDK and dApp
- [The Raiden dApp](http://lightclient.raiden.network) - a reference implementation of the Raiden Light Client SDK
- [XUD](https://github.com/ExchangeUnion/xud/) - a decentralized exchange built on the Lightning and Raiden networks to enable instant and trustless cryptocurrency swaps
- [Storj](https://github.com/stefanbenten/raiden-on-storj), [Medium post](https://storj.io/blog/2018/12/taking-payments-to-the-next-level-with-raiden/) - decentralized cloud storage
- [CryptoBotWars](https://cryptoplayer.one), [GitHub](https://github.com/cryptoplayerone/cryptobotwars), Medium posts [Part 1](https://medium.com/@loredana.cirstea/cryptobotwars-or-how-to-build-shitty-demos-and-why-19b5ecf60c76) and [Part 2](https://medium.com/@loredana.cirstea/cryptobotwars-part-2-conclusions-ebde6fa716f6) - Tic Tac Toe w/ micropayments and a Game Guardian
- [Team SCG](https://github.com/StupidCatGentlemen/Ether) - buying and supplying electricity on an open marketplace using Raiden for payments.
- [Cryptogrannies](https://github.com/swops-io/ETHSingapore-project) - pushing crypto to be simple enough to be used by the oldies
- [Raidenooh](https://github.com/pisuthd/raiden-dooh) - decentralized digital signage platform

### Hackathon

The [BEYOND BLOCKCHAIN](https://gitcoin.co/hackathon/beyondblocks) hackathon. June 24th, 2019 - July 10th, 2019.
A three-week virtual hackathon where global developers and entrepreneurs will collaborate to push blockchain applications to new frontiers of business + technology + social change.
- [Join the BEYOND BLOCKCHAIN discord channel](https://discord.gg/eVxbav)
- [Gitcoin](https://github.com/gitcoinco/beyondblockchainteams) issue board to discuss hackathon ideas and find teams!
- [Raiden specific hackathon repo](https://github.com/raiden-network/hackathons/issues)
- Video: ["Beyond Blockchain Hackathon: Raiden"](https://youtu.be/wdz8M3RXJQs)

### Ether Faucets

- [Ropsten](https://faucet.ropsten.be/)
- [Rinkeby](https://faucet.rinkeby.io/)
- [Kovan](https://faucet.kovan.network/)
- [Goerli](https://faucet.goerli.mudit.blog/)

Or use the [MetaMask faucets](https://faucet.metamask.io). It should detect which testnet you're on if you have MetaMask installed.

### dApp Testing

Resources for trying the WIP Raiden dApp in your browser. The Light Client works on Ropsten/Rinkeby/Goerli/Kovan, here we'll use Ropsten.
1. Make sure you have MetaMask installed and connected to Ropsten Test Network
![ropsten](assets/ropsten.png).
2. Get testnet Ether on [Ropsten](https://faucet.ropsten.be/) (going off-chain with Raiden requires on-chain interactions, i.e. Gas).
3. Wrap Ether using the [0x Portal](https://0x.org/portal/weth). MetaMask might not show the correct wrapped Ether on testnet after you've wrapped it. If so, click on MetaMask and add Custom Token 0xc778417e063141139fce010982780140aa0cd5ab
![addweth](assets/addweth.png)
4. Start the Raiden dApp [here](http://lightclient.raiden.network). You can now use the dApp to open, close and settle channels.

note: The dApp user interface is very early WIP<sup>[explained more here](https://t.me/RaidenNetworkCommunity/28310)</sup>, the first milestone will enable sending tokens and not receiving them. If you're interested in trying Raiden you will want to run a full Raiden node and use the WebUI to get a good experience. To try this quickly, follow the [workshop](https://github.com/raiden-network/workshop/tree/tu-berlin-blockchain-labs). You can start it on Goerli with "--eth-rpc-endpoint https://rpc.slock.it/goerli" to skip signing up for Infura. Another option is to use Raiden with [DAppNode](https://medium.com/raiden-network/run-raiden-on-dappnode-a45a1f63609b)!

## Explorers

- [Mainnet](https://explorer.raiden.network)
- [Kovan](https://kovan.explorer.raiden.network)
- [Ropsten](https://ropsten.explorer.raiden.network)
- [Goerli](https://goerli.explorer.raiden.network)
- [Rinkeby](https://rinkeby.explorer.raiden.network)
- [Raiden Maps](https://medium.com/raiden-map/raiden-map-mockups-5586082693bf), [Github](https://github.com/raiden-map)

## Learning Resources

- [Raiden FAQ](https://raiden.network/faq.html)
- [Medium Publications](https://medium.com/@raiden_network) / [Blog](https://medium.com/raiden-network)
- [Reddit Weekly Update](https://www.reddit.com/r/raidennetwork/search?q=GIT&restrict_sr=1&sort=new)
- [Raiden Network WebUI Demo](https://youtu.be/ASWeFdHDK-E)
- [Raiden: Ethereum's Payment Channel Network](https://medium.com/@surferfc/raiden-ethereums-payment-channel-network-acc6e5c709b0)
- [How to install a Raiden node on the Ethereum Mainnet](https://youtu.be/fy2ctCQHfD4)

### Talks

List of presentations, podcasts, channels, etc. related to Raiden Network
- [brainbot Technologies channel](https://youtube.com/channel/UCAfSoSy9FK5UqlSxqcsQElA/videos)
- [Raiden youtube channel](https://youtube.com/channel/UCoUP_hnjUddEvbxmtNCcApg)
- [Beyond Blockchain Hackathon: Raiden](https://youtu.be/wdz8M3RXJQs)
- [Asseth 2019 - Paris](https://youtu.be/pN2jEgH1Nbs)
- [Red Eyes on Mainnet and 2019 Outlook](https://youtu.be/g7hgGWl8vb0)
- [Nugget's News Interview](https://youtu.be/Cp8hprIjJHc)
- [Stanford Blockchain Conference](https://youtu.be/_irp4Jx0qjM)
- [CryptoMonday 2nd Layer Scaling on Ethereum](https://youtu.be/piT0GeE7Rw4)(Deutsch)
- [Rock-Paper-Scissors on Raiden Network](https://youtu.be/Mv6Ukdu0Xso)
- [Devcon4 2018](https://youtu.be/v9UQlE2We50)
- [The Future of Layer 2 - Prague Edition](https://youtu.be/htyJrK9VuCc)
- [ETHBerlin](https://view.ly/v/MrLm3vSB1XEK)
- [Mass Adoption and Use-Cases](https://youtu.be/GrWqRVDOC4M)
- [Tackling Scalability Panel](https://youtu.be/AH2g-KpPk7w)
- [Copenhagen Ethereum Meetup](https://youtu.be/arecj2vyjlE)
- [Ethereum Asia Tour](https://youtu.be/MI5vgqq1hzA)
- [DAPPCON 2018 Panel Talking State Channels and Plasma](https://youtu.be/zmS0i3ZQZak)
- [DAPPCON 2018](https://youtu.be/hSMIpl6e_Ow)
- [Off The Chain presentation](https://youtu.be/8Duil4pLzhI)
- [L2 Summit State Channel Panel](https://youtu.be/jzoS0tPUAiQ?t=2h10m9s)
- [Edcon 2018](https://youtu.be/VsZuDJMmVPY?t=7h45m51s)
- [Asseth 2018](https://youtu.be/93qOwUSj4PQ)
- [Devcon3](https://youtu.be/00RPE96LRVM)
- [Oktahedron podcast](https://oktahedron.diskordia.org/?podcast=oh007-raiden#t=1:56.687)
- [Berlin Ethereum 2016](https://youtu.be/JuVP4iDVkoQ)
- [Devcon2](https://youtu.be/4igFqFqQga4)
- [Devcon1](https://youtu.be/h791zjvf3uQ)

### Research Calls

- [Layer 2 Community Call #1: Routing in state channel networks](https://youtu.be/SUxe_WJw5Yw)
- [State Channel Researchers Call #6](https://youtu.be/YzomDzpLW_o)

### Pulse

- [Raiden Pulse #6:](https://medium.com/raiden-network/raiden-pulse-6-news-from-may-and-june-f519818e7650) News from May and June
- [Raiden Pulse #5:](https://medium.com/raiden-network/raiden-pulse-5-news-from-march-and-april-56e781aea7c) News from March and April
- [Raiden Pulse #4:](https://medium.com/raiden-network/raiden-pulse-4-news-from-january-and-february-a25dbee298de) News from January and February
- [Raiden Pulse #3:](https://medium.com/raiden-network/raiden-pulse-3-news-from-november-and-december-dd0da04961d3) News from November and December
- [Raiden Pulse #2:](https://medium.com/raiden-network/raiden-pulse-2-news-from-september-and-october-6a6c6be8ad67) News from September and October
- [Raiden Pulse #1:](https://medium.com/raiden-network/raiden-pulse-1-news-from-july-and-august-423fae4e9d3e) News from July and August

## Other Resources

Resources indirectly related to Raiden Network
- [dxDAO Vote Staking Interface](https://dxdao.daostack.io) - lock RDN tokens to earn voting power for the [@dxDAO](https://twitter.com/_dx_dao). Staking period is ongoing. Newly staking tokens has finished.

## Community

- [Meeting Raiden @ Web3Summit](http://reddit.com/r/raidennetwork/comments/9red2i/meeting_raiden_web3summit/) and [Raiden: Ethereum's Payment Channel Network](https://medium.com/@surferfc/raiden-ethereums-payment-channel-network-acc6e5c709b0)
- [Non-profit 3D printed Raiden model](https://www.shapeways.com/shops/raiden)
- [Red Eyes on testnet](https://youtu.be/RpaAS64dI6k)
- [Github Visualization](https://youtu.be/xqxTGF--Bhk)
- Watchtower scaling: Lightning VS Raiden [#1](https://medium.com/crypto-punks/lightning-vs-raiden-watchtowers-monitoring-services-differences-c8eb0f724e68), [#2](https://medium.com/crypto-punks/lightning-vs-raiden-watchtowers-monitoring-services-solutions-e243f7793d19) and [#3](https://medium.com/crypto-punks/lightning-vs-raiden-watchtowers-accountability-business-models-celer-pisa-833384f01ad0)
- [Messari Raiden Network profile report](https://messari.io/asset/raiden-network#profile)
- [Community built FAQ on Reddit](https://www.reddit.com/r/raidennetwork/comments/7hhkv5/work_in_progress_raiden_network_and_token_faq/)

### Community Channels

- [RNC Telegram](https://t.me/RaidenNetworkCommunity) - where this bot lives
- [Discord](https://discord.gg/zZjYJ6e) - bridge and feeds (most maintained)
- [Slack](https://join.slack.com/t/raidencommunity/shared_invite/enQtNTQwMTM5MjY4MTQ4LTBlOTQzMjUyOGFkMTgwOGQyMmMyNTE0MmI0YmI4OTQ5MjY3N2FkYTVlNWRkODdkNmIwMWQzZDBjODAyZGFhOWI) - bridge and feeds
- [Matrix/Riot](https://riot.im/app/#/room/#raidencommunity:matrix.org) - bridge

<sub><sup>note: community channels are run by the community</sup></sub>

## Raiden Trust
- [Raiden Trust Website](https://www.raidentrust.li/)
- [Twitter](https://twitter.com/raiden_trust)
- Announcement [Introducing Raiden Trust](https://medium.com/raiden-network/introducing-the-raiden-trust-cd47db60146)
- [Apply now](https://medium.com/raiden-network/apply-now-for-a-raiden-trust-grant-aca7d3e1e908) for the first wave of Raiden Trust grants

## MicroRaiden

- [MicroRaiden Website](https://micro.raiden.network/)
- [MicroRaiden Github repo](https://github.com/raiden-network/microraiden)
- [MicroRaiden Docs](https://microraiden.readthedocs.io/en/docs-develop/)
- [MicroRaiden Dev Chat](https://gitter.im/raiden-network/microraiden)

### MicroTalks

- [Devcon3](https://youtu.be/yx0__aFvjzk?t=9m35s)
- [Berlin Meetup drone demo](https://youtube.com/watch?v=E6CIgJPxgpQ)
- [ScalingNOW!](https://youtu.be/81gK-5qLFeg)

### MRapps

- [AppStoreFoundation](https://hackernoon.com/anu-2-app-store-foundation-and-dev-status-a3de6d144e5f), [Github](https://github.com/AppStoreFoundation/asf-sdk) - sell in-app items for AppCoins
- [SmartMesh/SmartRaiden](https://smartmesh.io/) - internet-free digital payments and transactions
- [RightMesh](https://www.rightmesh.io/) - ad hoc mobile mesh networking platform and protocol

# RaidenInfoBot
A [Telegram bot](https://t.me/RaidenInfoBot) with a collection of resources about Raiden Network (and some misc. features). Currently running in https://t.me/RaidenNetworkCommunity (unofficial)

## Misc. Bot Functions

- Spam filtering
  - Removes joining message and sets some basic permissions (more strict against users with no profile picture or tag)
  - Welcome user with a tag joining the group, as long as they have a tag
  - Removes messages with blacklisted words, also checks edited messages for blacklisted words
  - Removes forwarded photos if user has no profile picture
- Updated dates and details for events/conferences/hackathons/meetups related to Raiden
- Basic bot points system
- Memes
- Warnings to watch out for scams anytime airdrops or giveaways are mentioned
- Fortune cookies
- Get telegram ID
- A few functions specific to the RNC telegram group
  - Upcoming Raiden related events, updated regularly (called using /events)
  - Can't be spammed (i.e. deletes previous command+response in favour of the new command+response)
  - A community FAQ
  - A message self destruct function if /secret is called after a message
