---
title: "Exploring team and service boundaries with User Needs Mapping — Team Topologies - Organizing for fast flow of value"
source: "https://teamtopologies.com/key-concepts-content/exploring-team-and-service-boundaries-with-user-needs-mapping"
author:
  - "[[Team Topologies]]"
published: 2022-08-31
created: 2026-08-29
description: "User Needs Mapping refers to the first four steps of the Wardley Mapping process that can provide significant value when helping understand users/customers, their needs and the dependencies required to deliver those needs within an organization. By mapping out the dependency tree/value chain we can begin to explore, visualize and identify potential team boundaries by simply re-organizing the dependency tree and overlaying the Team Topologies team shapes. Using these visualizations we can then discuss whether those team boundaries seem appropriate and adjust where necessary. This can then form the basis of a Team Interaction Modeling process using the   Team Topologies team shape templates  ."
tags:
  - "clippings"
---
In many organizations, team and service boundaries were historically defined by things like technology, process, or architecture tier (for N-tier systems). However, in the context of a fast flow of value for user-centric systems, it can be important to let user needs shape and influence team and service boundaries. This is where User Needs Mapping can help.

User Needs Mapping is a term coined by [Rich Allen, a TTVP](https://teamtopologies.com/all-ttvp/rich-allen-ttvp), during the preparation of some of the Team Topologies official Guided Workshops, and is based on one of the early stages of the [Wardley Mapping](https://learnwardleymapping.com/) process. Wardley Mapping builds upon ancient principles taken from Sun Tzu’s *The Art of War* and provides a great way for business leaders to map out a strategy by taking into account a number of factors including purpose, landscape, climate, doctrine and leadership in a continuous cycle of observing, orienting, deciding and acting (the OODA loop from John Boyd).

## Quick overview of Wardley Mapping

One of the core principles (and potentially most intimidating part) of Wardley Mapping is the use of an evolutionary axis that runs from Genesis on the left through Custom Built, Product and finally Commodity on the right of the map. When plotting an item on the map it is done so with respect to how “evolved” the item is, so something that is new to the world would be added to the Genesis column whereas something that was widely available would be plotted in the Commodity column. This allows the mapper and colleagues taking part in the mapping session to begin strategic conversations about the current state of items on the map and also discuss how they may evolve in the future (based upon market trends etc). This then means they can make more informed, strategic decisions about how to plan for the future.

![](https://images.squarespace-cdn.com/content/v1/5b3296b78ab7229ecafcf4ed/1661957240540-R2QPG80W8UW0L3LG69AT/Wardley+map+example.jpeg?format=2500w)

A completed Wardley Map showing the evolutionary axis

The power of Wardley Mapping lies within this unique ability to capture “movement” or evolution over time i.e. changing the position of an item changes its meaning on the map and puts the focus of the conversation onto the map. However, it is also this concept that means people can find the practice intimidating in the first instance since there is so much to take in. The Wardley Mapping process consists of 5 steps (see [learnwardleymapping.com](https://learnwardleymapping.com/) for more details):

1. **Define Your “True North”** (ie Your Customer/User).
2. **User’s Needs** – Needs to be met.
3. **Capabilities** – How you’re going to meet your user’s needs.
4. **Value Chain** – A list of users, needs, and capabilities becomes a value chain when you add dependency relationships.
5. **Wardley Map –** A value chain becomes a Wardley Map when you determine how evolved everything is and position it accordingly (left-to-right) on the evolutionary axis.

The term User Needs Mapping attempts to capture the first 4 steps of the Wardley Mapping process as we believe it can provide initial value for identifying potential team boundary issues without progressing into step 5 and the evolutionary world of Wardley Maps.

[Get time with our experts](https://teamtopologies.com/contact-us)

## Mapping User Needs to explore team boundaries

User Needs Mapping begins by simply asking the question “Who are your users/customers?”. It is still surprising how many people are unable to concisely answer that seemingly simple question. Many people might know who their users are but haven’t actually documented it or shared it with anyone, User Needs Mapping provides a simple canvas to begin the process and starts by capturing the user and their needs.

![](https://images.squarespace-cdn.com/content/v1/5b3296b78ab7229ecafcf4ed/1661957355334-GPM814EFAWZBFFWE24NU/P812+-+Footprints+-+Team+Topologies+Accelerator+Programme+-+Align+to+business+flow++-+User+Needs.jpg?format=2500w)

Capturing users and user needs in a simple visual way

After capturing some user needs, the next phase is mapping the dependency. This phase essentially uses the vertical “value chain” axis of a Wardley Map without the evolutionary horizontal axis. The map is “anchored” by the user at the top of the canvas and the user's needs are linked to each user. Focusing on one need at a time we plot what service, dependency or business capability is used in order to meet that particular need. The vertical axis represents how visible the capability is to the user.

![A collection of users and their needs connected to dependencies within the value chain](https://images.squarespace-cdn.com/content/v1/5b3296b78ab7229ecafcf4ed/1661957482879-ZW8PQ1AH5AFAQSJOXY4J/P812+-+Footprints+-+Team+Topologies+Accelerator+Programme+-+Align+to+business+flow+-+User+Needs+Mapping+-+session+1.jpg?format=2500w)

An example early stage User Needs Map highlighting potential team boundaries

[Check the user needs mapping workshop](https://teamtopologies.com/all-guided-workshops/workshop-find-good-boundaries-for-flow-using-user-needs-mapping-p828)

## A User Needs Mapping example

Imagine a company called *Footprints Tours* which offers ‘alternative’ walking tours of cities exploring their social and cultural history. They provide both guided and self-guided tours and have implemented a monolith website and mobile application to serve all of their customer needs. The flow of development has slowed down significantly as the code base has grown over time. Using User Needs Mapping they are looking to understand how they might re-organize the teams, and therefore the applications/services, to improve flow and alignment with the needs of their customer.

We could begin the exploration with a user journey such as “Finding a self-guided tour”. In this scenario we can imagine what would be required when a user needed to find a good self guided tour. The first service they might use is a search engine such as Google or Bing (an external service). In order for our “Find a tour” service to appear in the search engine results, we would need some search engine optimization (SEO) and this would lead the user to that page on our website. Once the user has landed on the “Find a tour” page, they might be encouraged to use the Tour Search Service (an internal service dependency) to find a tour that looks good for them. The Tour Search Service might require a database which contains the data about the tours. The database is provided as a platform as a service offering from a cloud provider which then becomes a further external dependency that can be mapped on the canvas. As each dependency becomes less visible to the end user, it is plotted further down the vertical axis.

After performing an initial mapping process we can explore overlaying the Team Topologies team types to highlight where we think some possible team boundaries might exist.

![A user needs map with team topologies team shapes overlaid](https://images.squarespace-cdn.com/content/v1/5b3296b78ab7229ecafcf4ed/1661957634230-EI20676SP7MC1ZRLPCE9/P812+-+Footprints+-+Team+Topologies+Accelerator+Programme+-+Align+to+business+flow+-+User+Needs+Mapping+-+session+4.jpg?format=2500w)

A User Needs Map after overlaying some initial Team Topologies team shapes

After this initial session and seeking feedback we might decide to “drill in” to some areas such as the website to identify which parts of that system might be owned by specific teams and therefore be a good candidate for stream-alignment.

![An evolved User Needs Map identifying opportunities for stream-aligned and platform teams](https://images.squarespace-cdn.com/content/v1/5b3296b78ab7229ecafcf4ed/1661957720705-1JN1H17EBX5Y91DBRBTA/P812+-+Footprints+-+Team+Topologies+Accelerator+Programme+-+Align+to+business+flow+-+User+Needs+Mapping+-+session+2.jpg?format=2500w)

The User Needs Map has evolved after identifying potential opportunities for stream-aligned and platform teams

As we can see the database is potentially a shared dependency between the two stream-aligned teams. This raises questions such as whether data should be stored in a single database? Should the data be owned by a database platform team? Is there data that is only relevant to the individual streams? Could this database be split into two databases provided by a platform but owned by the streams?

After we have drilled down the dependency chain as far as we want to go, we then look at the next user need and repeat the process. As we do this, we begin to uncover and visualize the dependencies between the services and capabilities within our organization. The more we do this, the more we might spot patterns or opportunities to decouple services to provide faster flows of change or introduce other types of team to help reduce the cognitive load of stream-aligned teams.

### The User Needs Mapping Process

In summary, the [User Needs Mapping](https://userneedsmapping.com/) Process is as follows:

1. Create a list of customers/users
2. Identify user needs
3. Identify what capability/component/service is required to meet the user need
4. Overlay potential team boundaries using the Team Topologies shapes
5. Annotate the map with questions about suspect dependencies
6. Discuss how the dependencies might be broken and capture your thoughts of other ways to organize the dependencies
7. Repeat steps 1 to 5 as necessary until you identify potential team boundaries that “feel” right

### Delving Deeper

After you have completed the User Needs Mapping process, the next logical step may be to introduce the horizontal evolutionary axis of Wardley Mapping. It can often be an interesting thought experiment to consider whether products or services you are currently “custom building” with specific teams should actually be purchased as a “product” or even used as a “commodity”. Or maybe the products and services you are building now will evolve within the next couple of years? This might prompt the question whether you should start preparing for the inevitable evolution now? If you would like to learn more about Wardley Mapping take a look at [https://learnwardleymapping.com/](https://learnwardleymapping.com/) for some great resources.

[engage with us to accelerate value](https://teamtopologies.com/contact-us)

## Summary

User Needs Mapping refers to the first four steps of the Wardley Mapping process that can provide significant value when helping understand users/customers, their needs and the dependencies required to deliver those needs within an organization. By mapping out the dependency tree/value chain we can begin to explore, visualize and identify potential team boundaries by simply re-organizing the dependency tree and overlaying the Team Topologies team shapes. Using these visualizations we can then discuss whether those team boundaries seem appropriate and adjust where necessary. This can then form the basis of a Team Interaction Modeling process using the [Team Topologies team shape templates](http://shapes.teamtopologies.com/).

If you are interested in learning how to apply User Needs Mapping to find boundaries in your organization, take a look at our [*P828 - Find good boundaries for flow using User Needs Mapping*](https://teamtopologies.com/all-guided-workshops/workshop-find-good-boundaries-for-flow-using-user-needs-mapping-p828) workshop.

[all adoption content](https://teamtopologies.com/resources)