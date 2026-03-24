🔗 https://www.youtube.com/watch?v=ZBkRBs4O1VM&t=2227s

00:00:42
Hi there. Welcome to season two of AI Giants, a podcast where we dive very deep into the AI coding world with some of the most influential makers shaping the products we're using every day. I'm your host, Jeam George. Welcome to everyone watching on YouTube, X and LinkedIn. Also quick very quick announcement as we start. AI Giants is now available as a podcast. So make sure to follow um and um get on Spotify via the link below. Should appear anytime soon. Let's go. Um and very excited about the first episode

00:01:17
of 2026 with a unique um Jeffrey Huntley. Jeff is best described as a goat farmer. um he created Ralph a year ago and did a whole bunch of speaking before it was released. Jeff also did a lot of open source work, previously known as a maintainer of React extensions. Jeff is excellent to have you today. >> Thank you so much for having me here today. Um I'm looking at the run sheet that we're going to be going through. So strap yourself in, folks. It's going to be fun. It's going to be spicy. It's

00:01:47
going to be lively. Let's go. >> Okay. Before we start, reminder that you can post questions uh in the Q&A in our website, but also if you comment or make questions in YouTube X and LinkedIn, we have a number of folks that kind of just grabbing them and posting them here so we can try to answer them and we will address them at the end if we have the time. I don't promise to answer any single one of them, but we'll do our best. Let's get started. Jeff, what is Ralph? >> Yeah. So, there's uh it's taken a split

00:02:16
meaning. It's taken a split meaning. Um, Anthropic has published their implementation of my research that I published round about in uh, July last year and it is a implementation. Um, but you're not going to get as good as outcome unless you apply the general theory. So, we'll probably get into some of the general theory here. Um the way the anthropic implementation works it just completely continually runs until it gets a compaction event. Uh whereas the general theory is uh what you do is

00:02:54
you create a brand new context window every array and on every loop you tell it to only do one thing. So you don't get compaction you don't have uh you don't have any rot. So in this most simplest way, Ralph is really a very easy way to teach a concept. It's a pattern for an orchestrator. Now you you might be new to this term of an orchestrator. It's really simple. Imagine if you had a thousand of these Ralph loops going. This allows is a way of allocating memory or tasks or goals to a higher

00:03:33
level thing. So you can have thousand of these going like Steve's been talking about this for the last year and he's just released his with Gastown. I'm I've got my own that I'm building live u which is loom like I I want a thousand weavers going on. So in the most simplest way, it is a bash loop that deterministically allocates the memory, allows the LM to pick like one thing to do in the task list and uh you set it off to the races and uh it's just a bash loop. But then again, you might be

00:04:08
thinking, well, it's just a loop. Well, cursor is just a loop. Wind surf all these things using every day is just a loop. If you think really carefully about it from the right angle from GPT3ish days, we used to like make me a Python application and it would give you a Python application and it was pretty terrible back then. So you copy and paste it, you put it into uh your ID, you press run, you get compilation error, you copy and paste it back backwards forwards tool calling and cursor is just the automatic copy and

00:04:38
pasting. So you might be thinking oh it's just a bash loop nothing amazing. Well, cursor is just was or just essentially a loop of automatically copy and pasting. This is a loop for essentially which will allow a scalable supervisor on top to run thousands of these things. Okay. Um, what would you say that was the first test that you ran Ralph on and you thought, "Holy [ __ ] this actually worked." Um, and alternatively, what did it fail as particularly before that worked? >> Yeah, I I so

00:05:20
um I need to do a huge amount of shout outs to uh Kristoff. Kristoff um who is from the Finide team probably about four years ago joined GitHub next and they published a research um at GitHub next about specd driven development. Now it was too early. It was like most recent too early. That was in Gypit 3 days and it it didn't pop off but they they that research um at GitHub next proved that you could build an application in natural language. So I remembered that back in December. Um I had an ENG director come to me tap

00:06:05
me on the shoulder. It's like you need to pick up the tools. Everyone in the engine needs to pick up the tools here. And I remembered the researcher spec kit by Kristoff. He's in Poland. And I went with a specs or P based approach first now. And I just kept refining the approach from from Boxing Day. I guess it's two years ago now. Um and it the f I kept refining it by hand. You know, it was like I found myself like deterministically allocating things and then slowly changing my approach. I

00:06:44
used to high command like telling it the multi-stage thing what to do and I saw that the models are were pretty good at prioritizing things in implementation plan. So I started to learn to give away control but keep high oversight. That was really weird. Um I'm we got into computer programming because we I guess we we're high control. We like controlling the computers and I've learned in I guess in the last two years I'm still controlling the computers. I'm programming computers but what I'm doing

00:07:19
is I'm programming the new machine like the LLMs and the loop. I'm I'm I'm the orchestra the loops. Now to get to your question exactly, it was around about February. It was around about February last year and um I was playing been playing Factorio with my son extensively playing Factori with my son at this time like maybe maybe for six months and facing a Factori thing or a cursor on the side and I'm just doing that. Dad, can you help me get a rocket in space? And he's just watching me. He's like, "Dad,

00:07:56
you seem to be doing a lot of things by hand." Um, but it's the exact same way every time. Why don't you Why don't you just put it in a loop? And I'm like, okay, he's nine. I'm like, I'm going to just put it in a loop. Holy crap. Holy crap. And the models weren't great back then. So, I knew like where we're going. We're at like slope on slope improvements of these underlying models. It was only a matter of time before this would actually fundamentally change the

00:08:24
unit economics of software development. There is a difference between software development and software engineering. Software development is essentially uh like a jur ticket monkey. Um you could probably say that software development is over now because anyone can be a software developer. Uh the cost of software development now is $1042 an hour which is lower than the minimum wage and anyone can do it while they sleep. So if you identify as a software developer, it's some pretty tough times. But then

00:08:58
like typing the code or writing the code is it's been fun, but it was never really the real job. The real job is really engineering, breaking down requirements and like engineering loops and like how could it fail, security and all that stuff. So it's going to be really important for software engineering. So the first thing I did back in February, I did what I published something called the Z80. Uh Z80 was a essentially a research that was way too early which detailed how you could clone

00:09:27
a company, clone a SAS company or how you can drive an LLM like a crypto mixer over intellectual property. The reason that we have Intel CPU AMD CPUs today is because what someone did is AMD hired an engineer. They did some uh they did some very dirty reverse engineering to the Intel chip. They got a golden uh parachute when they did that, but that person is now burned. They legally can no longer work at AMD ever again. And what that person did was sat down with oscilloscope and like actually reverse hardcore reverse

00:10:07
engineer the CPU from Intel. and AMD can't use that that work directly any any notes whatever but if that person writes a book or a specification that's brand new IP that's original and that is legally clean so that's what happened that person gets a golden parachute out and then AMD hires a bunch of people to implement from his brand new IP that that describes a memoir of how the CPU works So that's what I did. I I took an application and I I went through the steps proving if I could clean room with

00:10:46
LLMs and I took >> You wrote a memoir. >> Yeah. And I or a technique. I was like, "Hey folks, wake up. Like things are about to change and I I took it like a sales tax calculator that I generated and I took it through all the steps up to a spec, threw away everything so there wouldn't be any pollution. And then I uh from specs I turned it I made it run on the Sinclair Z80 from the 1980s and like oh crap my toy example worked. And this was with a model that was I used to describe like Sonnet 35 I

00:11:21
used to describe as a hyperactive squirrel uh armed with kitchen knife like is easily distracted. Uh it's easily distracted. It's highly hyperactive. highly agentic and it just wants to do things and if you take your eye off it you you'll work you'll get stabbed. It's got a kitchen knife but if you learned how to like tame the squirrel you could probably get a salad. >> You used to get something like that out of it. And um the the the the the skill level to try and get something back then was like

00:12:02
that. With Opus, it's like this and it's just closing now. Like a year in, it is so much easier to do this technique. And now that my toy example had worked, I'm like, okay, could I clean room a company? So, I downloaded Hashi Corp uh Nomad source code and I ran Ralph in reverse. A lot of people right now are missing the point that Ralph goes forward, meaning you can use it to build software. No, run Ralph in reverse to create a clean room specification. And when you do that, you can run Ralph

00:12:43
in the reverse. And I was like, hey, study all this source code. completely don't care about the copyright whatever. I'm just doing proving that I could probably the toy example could I clone a product feature set of a of like a product with a they thought they were protected by their software license and they thought that they were protected by not releasing some of the uh some of the code the enterprise core. So I ran Ralph in reverse generate the specs. Cool. I got specs but they're missing 20%

00:13:14
because I didn't have the source code for the enterprise functionality and he's like okay I got a problem now. Like how like I'm I'm not interested in 80% of infrastructure orchestrator. No it's it's it's simple. You run Ralph over their product guides, their marketing material, all their customerf facing things that describe the product feature set and then that was enough to plug the gaps >> and at that point I was godamn spooked >> like it was spooky back in Feb because I

00:13:47
could see what's about to happen that for founders there is real no really no moat and I was just on the like just down the loop learning really to refine ing it. So I went out and did a lot a lot of like talks. I started writing a lot. Um it >> because you're concerned about the impact of this. >> Correct. Correct. Uh what does this mean now? Like what does this mean now to be a software developer? What does it mean to be a software engineer? What does it mean when like >> software development is cheaper than

00:14:19
like a burger flipper at Mackers? Um, and I'm getting emails from juniors saying, "Hey, look, I I've just completed uni. I feel absolutely screwed." Like, like, >> I I want to get into that junior question just in a in a second, >> but I I So, some some folks what they're doing essentially is like they're taking these screen uh captures of videos of products and now they're saying, "Hey, pick up all of this, build a spec, and then build a product." But you actually

00:14:48
use Ralph to go and read and understand from the source code, build the spec, and they'll grow from there just to prove the concept. >> Correct. Correct. That's what I did. So I I use source code to prove that any company out there that's raised a large amount of venture capital who has adopted like a BSL license or some bespoke license, none of that matters anymore. That's not a safety net yet. It's gone. >> Yeah, that's that's that's the quote of this podcast. Thank you. Um that's

00:15:19
that's scary stuff. Um so I want to again go back to a point here that you mentioned the cursor is is a loop and most of these tools are so question to you. Do you think that most of these modern AI agentic tools are just over complicated? >> Yep. I used to like I I professionally uh built these tools. Um >> take it from me. You're probably in corporate right now and you're swapping between like I'm going to cursive today. Oh, I'm going to wind surf next week. Oh, we got to do a evaluation of all

00:15:53
these different things. You're just chasing your tail. The harness really does nothing. It's the model that does all the work because there is really no moat in the harness business when you're reselling tokens. Uh the all you can do is project a brand. I'm Gucci. I'm I'm like like I'm Louis Vuitton, etc. We're different. Now, some have a higher degree of taste. Like there are like there are clothing and like bags and watches, etc. where uh they they're still just a watch, but

00:16:29
they they they've got a high degree of taste in how they take their approach. Um so like they're all really just the same. It's the model that does it all. So you just do a little bit as a coding tool to do this. Um so yeah we do complicate it but however said that whilst I've said that the anthropic is uh is not it they done a fantastic job of removing the need for me to teach a whole category of knowledge because they're making it very accessible that I I'm seeing videos on YouTube of like

00:17:06
>> like folks in folks in the Bronx launching their like crypto pro what else have you and they're like yo check Pat, Ralph, Luke, go. I I just woke up and and built my entire my entire thing when I was sleeping. That's only possible because of the work that Anthropic has done in Claude Co to make it super accessible. Um, one way that you describe Ralph, just to continue doubling down on how kind of a mental model of of of Ralph for people, especially folks that haven't heard about it since today or at the beginning

00:17:42
of the this podcast, you described it as deterministically bad in a nondeterministic world, which almost sounds like you're saying that failure is a feature of of of how Ralph and these loops operate. And so I'm hoping that you can explain to someone who's been trained their whole life um that code should work the first time or you want code to like failure is a bad thing. You know this this this this idea that failure is a feature. >> Yeah. Sure. Um I used to be so there there's a couple high level things. I

00:18:21
fully believe that software engineering should be a licensed profession with perhaps the if you work at a company uh that's contracted to build a bridge if that bridge collapses then that company should get liability like like the iron ring Canadian type topics. If uh before even AI you google can I be a software developer the top results say yeah anyone can be a software developer. so easy. But if you Google, can I be a veterinarian? It's like, no, you got to go study. And by the way, veterinarian

00:18:57
science is harder than being a doctor for humans. And this is like the stark difference of what we've been in. So that's always been really boggling for me. So that's that's the setup, right? I still believe in that. Still believe in that. But the way I used to approach it was very much I'm going to make a library and I'm gonna put all this effort that it works and I'm gonna higher control figure out how it all works and then I've got a Lego piece and then I got a Lego piece and I build it

00:19:24
mechanically piece by piece of known good components and if something's wrong I go look at what's wrong with that Lego piece. I update it and the tower doesn't topple or the bridge doesn't collapse. I now two years in see software development fundamentally different or software I still have the engineering principles. I now see the context window or the array kind of like clay on a pottery wheel, right? I turn the pottery wheel on. I sit down and say, "Hey, here is my specifications that have been built up

00:19:56
through this technique of a conversation with them." And I use that as a pin for this like to describe the describe that I am building a essentially autonomous weaving load. And every time I do this pro process it adds a little bit more context which frames the the future design. And when I want a new feature, I sit down. Hey, I want to add uh attribute based access management Aback study all my specifications. So you can specialize etc. And let's have a discussion about Aback. Interview me and

00:20:34
then it would go okay I'll learn about the existing specifications and how the application work. This has been going from zero like there was no specifications. I just did this process all the way up. And the more that I do it, the uh the better >> more context you're building, the more less iter guesses about the the domain that I'm in. I call this a model first company. >> Um corporate doesn't have this. So I go, hey, uh attribute based, how should we do this study, etc. And I was like, and

00:21:06
it comes back with five points. And I go, yes, I want that. Two, no, I want it like this. Is where I put my engineering in. I'm engineering the clay. I'm engineering the clay on the B wheel and then it goes for it gives me a thing like u do you want aback or arback and I'm like well I'm pretty sure I want attribute-based access control but I don't know. You can actually then have a conversation backwards and forwards deeper into the topic and it will explore and expand the topic until you

00:21:36
can make an informed engineering decision and you go yes I want that. I want option C. And you zoom back out of that. Zoom back out of that and you move on to the next one. And you just keep going that. And then at the end of this session, which is normally about 30 minutes, what you end up with is this pretty well-formed clay on the potty wheel. You just keep testing it. Does it understand what's going meant to happen? You try it a couple times. You're like, "Cool, it gets it. Write the specs.

00:22:02
Throw it to Ralph." And like I used to spend days thinking about the right architecture, the shape of my repositories and all this stuff like architecting XML like UML type stuff. I can now after that 30 minute session get a rough cut like I do a loop by hand like not even with Ralph allocating but I use the principles to try to even test it and if it if it doesn't seem right I go back I update the specs I try it again. prototypes are now free, they're now cheap, etc. And when I once I've got

00:22:36
a higher degree of understanding it's going to produce the right outcomes, then I just go back and I let it rip and I get a I get like something that is workable. Workable, not working within an hour. You get weeks worth of work of potentially multiple co-workers in a couple hours. And this is where it gets really interesting is I still believe in engineering. Still believe in engineering. And like if the bridge collapses, that's on you. But you know what? If it's wrong or it misses something, I can throw it back on

00:23:13
the pottery wheel and I can do a a crafted ra loop saying, "Hey, look, it looks like there's a like you're duplicating the like the SQL all over the place. You're not using the repository pattern." So that's a refactoring Ralph loop. Oh, you forgot uh you forgot to do internationalization. Well, that's I'm throwing it back on the wheel. That's a separate RA loop. Refactorings are now cheap and easy. And the interesting thing is you can actually generalize that into uh essentially a Roomba that

00:23:43
automatically vacuums your codebase and repairs and does all these things. >> That way you still have a forgetful Ralph that's doing its thing and building features. doesn't mean you when I talk about a thousand thousand uh Roombas or a thousand like Ralph loops going you can have an internationalization one you can have a security one that just checks for common things that the agent forgets etc you can automate these things this is a new class of engineering like we've got a new

00:24:15
computer here folks uh what we've had over the last 40 years we need to reimagine it for the new computer Um, as Ralph goes in each loop, um, and it starts fresh. Obviously, we have the spec files as kind of the foundation or that clay, right? But, um, what do you lose if you lose anything? Uh, what do you throw out? Like, is there institutional knowledge that dies in each loop? >> Yep. Yep. >> And that's okay. because that's okay because my institutional knowledge is in

00:24:51
the specifications file. So every loop I allocate the specifications which is a lookup table to other specifications and that's enough to pin and reframe each loop that like this is my domain knowledge. This is where you should look at certain modules. These are the patterns that you need to follow. And that's enough because once you've done that, you think about from that that point forward, you give it a task and goal implement logging. Well, how useless is the implement logging if the

00:25:21
logging is you got a logging spec and then four or five like features later that's in the context window. It's basically that that that array has two or three different competing goals. And if you think about context windows, there's an array, sliding window, etc. And we know that the more you use an array, the context window, the dumber it gets and then you get stuff like compaction. But what happens if compaction removes the pin, the specifications, and then it starts making stuff up? So,

00:25:52
it's really simple. Avoid compaction at all costs. Deterministically allocate the description of your application so we could use it as a lookup source and then pick one. >> Okay. So now I want to move on to more spicy um subjects and those are essentially how we look at the industry. So you've been very vocal about um essentially not hiring any junior or mid-level even software engineers which is terrifying right um as as just a statement. So you're saying essentially that entry level path into software

00:26:32
engineering is closing. Yep. It it closed for a while. It closed for a while. Uh um I was at CBER. The doors shut at Camber um about a year ago for juniors um until we figured it out how we're going to interview again. And then we opened it back up again once we figured out how we're going to interview again. Like I mean like how do we identify someone that's been curious? Um it is very important to raise the next generation of software engineers who think like software engineers. It is still really

00:27:08
an unsolved thing how we raise that next generation. You need to completely replenish that pool and we I believe firmly in apprenticeship. Having said that there is a hard line coming folks. There's a hard line coming. If you're only just picking up the tools today and after Opus because you finally discovered that it's great, understand that a lot of my writing and research it got syndicated with the prime gen like six, seven months ago to an article that was just, hey folks, hey juniors, pay attention, you're screwed

00:27:43
unless you pay attention here and invest in yourselves. And that kind of popped off and I started writing like how to build a coding age and and teaching the new compsai fundamentals of like inferencing loop etc. I think that's like 4.5 or 5ks on git github which is great right. So we now have essentially at least six or seven months, like half a cohort of juniors who will work at a quarter of the wage that a senior software engineers on because they're young, they're juniors. And it's not just they like it's not

00:28:22
that they're working with these particular tools. They they found discoveries. They found that like you can have you can drive loops that automatically copy and paste. Like for example, an example of a loop would be a workflow loop. Um I know that I can create uh I can drive the model to using T-Max. And then once you command it to use T-Max, it will automatically scrape the PES and copy and paste that into loop back. So I no longer need to be at the computer as much because it I've automated that that loop back. Another

00:28:58
classic loop back is like use the GitHub CLI to automatically resolve the CI failures for this pull request and it just does it. And it's that knowing of the techniques once you make that discovery that's your edge that's your advantage. So we got juniors now six months playing and making these discoveries of loop backs etc. If you're just starting now, you you you've you think you've got it. No, there is a lot of knowledge that you have to learn and techniques and this is becoming AI

00:29:28
native software engineering. >> Yeah. >> And if I may offer some resistance to that. One of the things that I see though is that where a junior could learn some of these ideas and explain how to code already with tools like cursor and now playing with Ralph and so forth, a senior from what we've seen at least and from what I've seen can can have so much more resistance to um offloading ownership and and and leaving kind of the old engineering practices behind. not even seeing a paper today that senior

00:30:08
engineer like to maintain ownership of of code and the practice and the agent right whereas what we're discussing now with Ralph is screw ownership here's the spec go build it do it in parallel and whatever you do just get there and so I my hope is that as we get you know farther into the future let's I can agree with you if anyone is learning how to code and does not take this into consideration Yeah. It's going to have a hard time. But if they are, it's they don't learn

00:30:39
the old vices, so to speak. Does that make sense? >> Yeah. Um, let's play let's play with this. Okay. So, these tools in the hands of a junior is uh dangerous. It's kind of like a woodworking shop. Like they they don't have the experience to know how a table saw can take your finger off. and they don't have the stories etc. So you need to supervise them. You need to mentor them like your your the workshop supervisor in your high school and you're supervising your class. You can't

00:31:12
use a lathe until you don't have a tie, no high hair, like it doesn't care about taking a finger off or strangling you, right? And a junior won't really have some of these domain knowledge of like how to be an engineer. I think that's our opportunity. But if you got an if you got a junior who's learning these concepts, they're so much more mentable mentorable and a shorefire bet than someone who doesn't have that. So that that's that's the difference. Now on for

00:31:40
the senior side of things, well, what happens uh what happens when a companies commit grafflers like that? Not that commits is is the the right measurement here, but like commit like grits like that for the high performers. And what happens when the high performers are basically the leadership team and they're discovering Ralph and they can run their organization just the three of them and the rest theorg commit velocity and product velocity is like that. The team's like that. That's like that. I my deepest

00:32:18
fear is people think they've got time. No, the unit economics of software development is forever changed. You need less humans. So the way I look at it is AI is a is an amplifier of operator skill. It amplifies the knowledge that you have. If you're really good at security, really good, you got that brain and thinking about like when I get hacked, what is the blast radius and like really thinking about these things and then thinking about gadgets and the widgets that is amazing. If they get curious and

00:32:54
they get really good at AI, they they turn into an absolute weapon with it. And this is the same with in any discipline, accounting, like legal, software engineering, etc. This is the new thing is like actually being curious, playing with it, and then automating your job function. Now, if an engineer is like, "Oh, no, whatever." Like I I I I see online and I I can't believe I read this last night. There are really respected software engineers that I respect in their craft taking a hardline stand. No, I will

00:33:32
never use AI because that is fascist. Fascism. that's installing fascism in your codebase. I can't believe that stuff from 2019. Someone is going to take such a hardline stance and not going to make it in that sense that like their commit velocities like that, a product velocity like that. Founders are learning. They're going hm why we pay the payroll of that person. We're we we're roughing now. And that's why really one of my concerns like you can send down ladders etc.

00:34:02
Um, but there's a hard line. There's a hard line coming. >> Yeah. Um, >> just because you don't feel it in your current company doesn't mean it's coming. >> It it's not real. I understand. Um, I want to explore that idea of skill of AI. So um that distinguish um that idea that separates between someone that is skilled using AI native flows or thinking with AI uh visa v someone that is unskilled. What do you think makes someone um skilled in AI assisted development? Um

00:34:39
>> it's the discoveries. It's the discovery. You can >> you can go to my YouTube channel. You can learn how to Ralph. You can learn how to do specs and P. You can go back to the GitHub next research about specs and P which kicked this entire thing off. I haven't actually seen them properly cited for this research to be honest. But it's the knowing of the tricks. If you pick up the guitar, you play it like this in the particular way that's C note. Like some of these things

00:35:09
don't actually have language or terms to them. We're inventing the terms for the new computer every day and we're trying to get consensus of this. So it makes it really even really hard to actually teach these things. But the main thing I can talk about is closing the loop and looking for opportunities to automatically copy and paste in the context window. It's it's I feels like I'm at my I'm I'm picking up my first computer again. I'm picking up my first computer again. This is a brand new

00:35:35
computer. And with this new computer, you can start think someone who's like far along the journey sees this is some of the most exciting times and we can reimagine what the new computer is and because the how the last 40 years until we get from here to there to where we are now. It was everything all the design decisions were for humans like why do we have a TTY? Well, so the human operator on the main frame could type. Why do we have environment variables? Well, the human need to configure an environment variable like

00:36:08
and then you start going wow Unix is based on 40 decision 40 years of decisions for humans. We got robots now. What's the bare minimum robot needs? And then you start thinking well what about uh what about programming languages? We never used to do breaking changes and we used to be very slow in our pace of language development because we would break humans and their mental model etc. Well, what happens if uh programming languages start raling by default and their velocity is like that I no

00:36:41
committees none of this garbage they just just go here it is you want high kind of types and rust there it is like a breaking change is now cheap and free because free compared to what it used to be because you just run a raph loop to auto migrate the codebase you can just publish an auto migration script and so you know the back compat and all that's really changed. Um all those concerns really changed. So this the skill level is really the discoveries of loop backs and there's a new mindset. Um

00:37:13
>> me people would be like if they're just using cursor to like ship their their things etc. They might be not picking on picking up why some of the biggest names in compsai have come out of retirement. Like why are they excited? Learn why they're excited is what I'm talking about. We've got a new computer. We can dream what the new computer is. We're we're building the new computer every day. >> And and and so in that example of guitar learning, when you're a teenager, you

00:37:43
have what feels like infinite time for you to, you know, play and explore, but what would you say to that um mid-career engineer with a mortgage and kids? Where do they find time for that deliberate practice? >> You just make it happen. I've got kids, right? Um, I like to describe this as we got this magic space us that allows you to teleport to the future and steal and rob your retirement plan from yourself. What are all the ideas you're going to do when you're retired? Do it

00:38:20
now. You can do it now. Like the idea of making a programming language or a Game Boy emulator or even a damn operating system. Like I started doing ralphing an operating system and I just stopped like okay I've done enough novelty stuff. I've done a programming language. I I definitely can do an operating system. I well actually one of the uh mono uh one of the the mono engineers behind Zamron they built an operating system over Christmas >> uh using these techniques. So uh you make the time and understand

00:38:55
it can build while you're away from the computer. So the amount of time the old this I've got to spend eight like ah I' got to spend 60 hours to learn this new thing and new new program I don't have time that doesn't make sense anymore that doesn't make sense anymore. You can just like pick it up for 30 minutes and try different things. You can discover new techniques. So just pick it up for 30 minutes, put it down. Pick it up, put it down. Don't watch some Netflix. Just

00:39:23
like pick up the guitar. You'll know. You'll know if you'll know when you truly get it. Why all the compsai people are out of retirement because if you have trouble sleeping because you you're so excited about what you can now build, you get it. you really truly get it because >> you can teleport to the future, build all the things you've always wanted to do but you never had time to. You can do it now. >> Right now. You haven't been be able to do it for the last year. So, you make

00:39:55
the time. Now, the interesting question if we split that is you're a midlevel software engineer and you're like, there's no way what Jeff is talking about is real because I don't see it around me. Everyone around me doesn't see it doesn't get it. No one else gets it. Well, I hate to hate to put it forward to you, but like there'll be a time when you you'll be an I like a like you'll be teleporting to the future and implementing all your things and you will get it so hard you won't be able to

00:40:23
tolerate people who don't get it. So, you'll seek to be around other like-minded people and you'll understand the rising tide here and the riff that's forming and you'll go seek to join a model first company of those who see it. Um, so if a if your company's outright banned AI, well, the only time you can get good at AI is at home. That sucks. The perfect place is that you play with it at home, you make a discovery, and you play it at work. at work, you play discovery, you play it at home, you got

00:40:57
this loop going on, etc. Um, for any for any other big corporate type thing, it could be like three, four years of a agile transformation program. They roll in essential coaches that teaches everyone this is how you do >> a engineering etc. It's already happening. But like >> seriously, what's the quality of those agile coaches AI? Like there's >> no they're outdated by definition by by the time they create a programs to wait a week and it's already outdated.

00:41:28
>> It's gone. It's gone. It's gone. Like I there's probably >> five to six people in the world that I write as brilliant. Like that's the pool is really small. >> And we're all sitting in WhatsApp groups like riffing each other's on >> um sharing ideas. Like you go do that. Like I' I've got folks who are just that like let's get rid of agent user space. What's a user what does agent space look like in Unix? They're exploring that.

00:42:02
These are low-level engineers thinking how much of the operating system can we cut >> and they want yeah they're heading that way. I'm I'm looking at can I have an automated software development automated weaving loom? What are the software engineering practices that no longer make sense? Why do we have CI? Why do we do code review? Like >> question everything. >> Questioning everything. Questioning everything. And they're doing the opposite for low-level computer

00:42:27
internals. >> Wow. >> Um so it's it's really strange. Um my biggest concern is in these corporate transformation programs is it's going to be three or four years where they do the transformation. You might feel that you're safe, right? But what happens if that corporate you're in is 5,000 employees? They've raised a large amount of capital and the unit economics has changed on that company. Like software development is now cheap. They've overhired software engineers or over

00:43:02
people before AI and you're working at the company doing the transformation. You might think it's going really well. What happens when there's a couple people uh that just in their 20s, they go to Bali and they run the Z80 and Ralph and instead of charging $100,000 a month for the enterprise >> SAS, they go after your product. Yeah. >> They go after your product and they charge $1,000 a month and they can turn things around faster than the bigger wall. We all know smaller teams

00:43:32
>> ship faster >> um because there's less hierarchy. So, I'm very concerned it's going to be kind of like a Titanic moment. Sorry, the boat is full. Get the next boat. >> Yeah. >> Um, >> so we're we're we're on time for questions, but I want to just get one final one in from from my side because the conversation has been so um entertaining and valuable. Um, what would have to happen for you to conclude that AIS development is overhyped? What's the what what would be

00:44:05
the thing that you'd say, "Yeah, I was wrong about the timeline." Oh, I was wrong about the magnitude of change. Or what would have to be true in order for you to make that statement? >> It's a fantastic question. Um, I originally was the person that was hardlining, but AI is hype and everyone that turned up uh, talking that AI was a pretty amazing. I just wrote him off as a shill. I just wrote them off as a shill. That used to be me. What was really happening is that person

00:44:43
was genuinely concerned that, yeah, it's getting good. And they were trying to communicate to me, yeah, it's getting good. Um, it took a conversation with a founder talking about like the unit dynamics of businesses changing and the bar and need to get back on the tools for me to go, oh [ __ ] right? And then I could see that it's a slope on slope improvement of the capability and the skill level needed to do things would I thought that would be like a safety net like opus. Every time the model gets

00:45:14
better, the skill level to drive these things is just getting easier and easier. So you got these random people on YouTube going, "Yo, check out Ralph Loop and Anthropic has taken the these concepts and made them super accessible." So I guess uh I was wrong about the time frame. I thought that like when I showed Ralph Loop about six months ago and published it, people would get it. Maybe I could have done better in teaching it etc. Um the people in San Fran I showed it to they got it immediately at the meetup

00:45:48
because they can they they're used to thinking in exponentials and then they're deep in the San Fran culture. Um I presented that and it was gez we spent like an hour after the presentation and we were just going [ __ ] what does it mean now? What does it mean to be a founder etc. That was six months ago and then then then they got showed in Y Combinator demoed internally in Y Combinator and there's like half a batch now or have been raphing for six months. So like this entire notion of couple people in

00:46:21
Bali going after the corporates that don't transform fast enough. It's it's real folks. It's real. >> They're going to get Ralph. >> They're going to get raled. Their actual business model is going to get Ralph by Ralph. Um, so I guess I was wrong. Uh, I would have expected it to happen kind of sooner. I still potentially see maybe AI as a as a bubble, right? Um, a lot of these labs are lighting money on fire. I do not deny that. But at the same time, I cannot it'll be it

00:46:56
would be a false equivalence to say that I for the last year I've been writing software while I sleep. Like yeah, like that's that's pretty crazy proof. And then when you got the social proof of like all these YouTube videos of non-software developers that would normally go to to lovable just installing clawed code in implementing their wildest dreams. So maybe it's how can you still say it's a bubble? There's actually economic utility coming now and founders are starting to go well let's

00:47:29
rethink about our business plan now. Maybe one of these front frontier labs explodes because they light too much money on fire. That's none of our concerns. We have open- source models that can run on local hardware. We'll probably have Opus level intelligence that can run on local hardware if you've got the hardware at home within the next six months. Right? If they if they go boom, so what? So what? We're not going back. I'm not c crafting code by hand. We got a CNC machine.

00:48:04
There's no way I'm going back. Like we've gone from essentially uh carrying carrying cargo by hand to we've now have a locomotive that just goes. It's our job now is to be locomotive engineers to keep the train on the tracks and to build the tracks etc. Um and to be engineers because there's no going back once you got a locomotive and that automates things for you. So, I guess I I could be wrong on many things. I think what I'd like really pass on is as certain as I am on these topics, I don't

00:48:39
bloody know. And I think anyone who says that they know is selling you horseshit. Like, I've sat for the last year figuring out where and how product will go in in all these scenarios after the discovery. Um, and Game Furied up where it goes. So, I've got a kind of idea what the shape of like the the tree and the structure of how it could go, but everyone says all these absolutes. Um, yeah, there's there is no knowing. Please understand there's a brand new computer. And if you aren't excited as I

00:49:17
am about a new computer and you're like, "Wow, what is this?" and like doing invention discovery. Uh it's it's time to it's time to start picking up the guitar and playing. And that's a great segue to to open up the questions to our audience. We have already have a number of them. Please do post. We'll have nine minutes, but we'll try to get as many as we can. So Andrew asks, "Does the current RAL loop within cloud code plugins ecosystem actually start with the free context window after

00:49:50
each task?" Uh my adviser said there was an additional script to get it to perform as such. >> Yeah. So have a look at the implementation. Have a look at the what I my video on YouTube which where I teach how I build my specifications and PS. I see a lot of people saying, "Oh, Ralph loop will never work because I got to spend all this time writing specifications." I codegen all my specifications. So, for the internals uh of uh for of that um watch my video, run an agent over that implementation, then compare

00:50:25
those notes together. This is the this is one of the things you can actually this is one of the techniques. um you can ask these questions and it's a very good question but this is now what I would normally use Ralph for like I get an academic paper and I instead of spending three or four days to read and find that information I run a Ralph loop to replicate the research I I do a prompt split this 100page PDF in compsai or in ML and uh convert that to markdown and give me a working prototype because

00:50:57
I feel I think and feel in code. I need to see it in code. Now I can do that. So the main thing is that it you could do the cord code plugin etc. and all the differences. We can focus on that. That's missing the bigger picture. This is orchestrator pattern that could orchestrate thousands of claude codes. That's where we're going. This is where Yagi has been telling welcome to Gas Town. Welcome to Gastown because the orchestrator can make intelligent decisions. This is you can maybe call

00:51:30
the orchestrator Lisa or Milhouse and it it tells it tells Ralph what to do and it can be hyperpersonalized. You need to anytime international isolation happens you need to do a RA loop to make sure all the things internationalized. If you're still thinking like I can just use claude code oneonone you're missing the bigger picture here. we have an automation primitive. You need to be thinking about how I can automate your your job function. Um, so you can do the plugin and if you do the

00:52:01
plugin, you're going to be doing so much more productivity and output than everyone else. Just understand there are people like me who are thinking about robots and robots and robots and loops and loops and loops. And there are other people since the publication they are building the Lisa building the millhouse and they're thinking about this as essentially a a a rooma and they want to be programming the rooms to automate their things. So it is important to have a brand new context window and people

00:52:31
are going playing either way. I'm very friendly with the ent anthropic team. Um I'm completely neutral to them like like they don't pay me any money or what else have you. Um, and I'm very thankful um, what for what they've done in making this more accessible. But if you're just using the Anthropic plugin, you're a consumer. You're a software engineer, aren't you? If you just got to consume the thing and understand how it works, you're just going to be consumer. Yeah,

00:53:02
sure, you'll make the cut. Um, but like the rewards go to the people who are the engineers who automate their job function with AI. Mhm. >> And to do that, you need to be thinking about orchestration. >> Orchestration. >> Um, a user in YouTube asks, "How do you get Ralph to rank order potential framework/platforms you're evaluating while building?" >> Well, this is going to be weird. So, yes, I own a farm. Goat farmer. Yes, I own a farm. I used to be one of the maintainers of

00:53:41
React extensions. I used to be very prolific in open source and I did an entire bend for multiple years about getting open- source financing and pleading companies to like donate to maintainers etc. Maybe we can change the world if we support the people who support the corporates. Um and like the the settlement of my land like the property conveyancing fees were all funded by Open Collective. That's the setup to this. I no longer use open source anymore. None. Because think about the problems of open

00:54:18
source. If there's a bug, you got to open a pull request. You got to go chase a human. You got to inject a human into the loop. Anytime you anytime you tool call a human, that's not AGI. That's not Ralph. So, it is much easier now to code generate everything. Um I got a blog post about this is what even is the point of open source now that you can code generate it. Now you wouldn't necessarily generate cryptography libraries like PKI I have but I wouldn't put it in production because that I

00:54:52
couldn't stand by my engineering bar. You know what there's got to be a PKI engineer who Ralphs and understands the domain and go that was amazing and that is safe right? So there's going to be these lines and you got to re-evaluate the lines of what you will generate and won't generate. So if you're thinking about frameworks, you missing the entire point unfortunately and I say that with absolute care. You actually need to rethink about things now like how do I not have humans in the

00:55:24
loop? Uh frameworks no longer matter. We made frameworks to make it easier to hire for humans. Like React, cool. we want two years React experience. Is that is that still true? Is that still true? Um and it gets really weird. So you can actually just make a framework like that. Or maybe you don't even need frameworks. Um I definitely there they're boundaries and lines like I'm not saying that we should go like ignore Ruby and Rails. It's in the training corpus and it does it really well. So

00:56:01
still use Ruby and Rails, right? I'm not saying that we should get rid of React. Use uh maybe you just stay with React or Next.js because it's in the training data. It does it really well and you're going to get better outcomes. However, what about the libraries in React or Ruby on Rails and all that instead installing those gems or the npm dependencies? Just codegenerate them. So you have like a stable base and heart of the framework and then everything else is codegenerated. Or you purchase some

00:56:27
first principles and go I just get to do the entire thing. I like rebuilding engines. It's now possible to rebuild an engine just from an idea. So, um, frameworks, I guess there there's something I've been thinking about programming languages. There are if you're like there is like a a tier list of programming languages. Um, I like to see uh unfortunately um F tier is Java and .NET to me. >> Okay. and and for reference uh there's 600 people on social media that the official Microsoft.NET account follows.

00:57:06
I'm one of them. I did a lot innet. I'm not saying this because I hate it because the way that these coding agents works, the search tool is uses the bash tool to execute rip grip or grap and that discovers a function signature or what else have you things like node modules. uh things like node modules. We used to joke about like it used to be the the weight of the black hole. Well, because it's sourcebased, not a DL new get and net is DL Ripket can run really well natively. But if you want to

00:57:40
get that type of stuff going innet, you have to do these crazy context engineering type things and all these other things that other programming languages get by default. So what makes something F tier? What make what makes something S tier? Uh, anything that's source-based uh with strong type systems that uh reject uh anything that's source-based uh that with strong type systems so it can run rip grip through it and the type systems reject invalid generations. So, TypeScript goes very hard.

00:58:17
>> Uh >> can you name one one S tier? What what would be one that you name? Rust is amazing. >> Rust is amazing. Uh pi python is so so but when you drive it with paidantic with that knowledge you should use pantic definitely s tier >> typescript is really good as well. Uh s tier if you do typescript with effect >> js. Wow. Okay. >> Because that's taking the idea of effect programming and making it very accessible which makes things very testable. >> Incredibly testable. Um but there is

00:58:51
there are trade-offs like rust the compilation speed on rust is very very very slow very very very slow >> yeah those are all trade-offs the trade-off if the compilation takes forever what happens if uh it does an invalid generation or hallucination >> and the compilation takes 30 minutes >> well you compare that against say like typescript in that time how many generations is it done because it will the generative function will be bad >> so you if you if you choose Rust or C++

00:59:21
or what else have you got to you got to be an engineer and make that back pressure fast. >> Yeah, we got to do a bullet round because we're already on time. So, we got to do very quick answers to some of these questions so we can address them. Very quick one. How do how will you implement Ralph on an existing codebase from Stallion? Um, it's really hard to give broadlevel guidance. Um, because Ralph is essentially unleashing an autonomous junior engineer with a kitchen knife. Like it's actually

01:00:01
can be quite dangerous. Um, an existing code base. Hopefully you got tests. Hopefully you got tests. Okay. Most enterprise stuff I've come across doesn't have tests. So maybe don't even think about it. Remember the Joel Spotsky thing, things you should never do, which is rewrite Netscape. I think that's now falsified. It might be easier to rebuild the application from scratch with specs with the techniques than it is to adapt the existing codebase. Um it's this is what like try it. Just

01:00:36
try it. So the first thing you do is you need to be creating the back pressure which is the uh doing the tests and making the maintainability. The next thing is you should be thinking about sandboxing. Can your application run in a sandbox a docker container and all the rest. If you can't do that then don't even bother rewrite it. Um um then you start uh then you start building uh the specification library. you can run Ralph in reverse on your existing codebase to generate the specs from like the Z80 and then you critique

01:01:10
that and maybe you can bootstrap your project. Um, just know that you're going to be going through a lot of pain to try to fit the old world in with the new world and you're going to be dealing with people problems like I want Hungarian. I want snake case. I want Pascal case. All that's just noise now folks like what they go oh AI doesn't create maintainable code for who? Why are humans the benchmark? If you can rip another agent through the codebase and you can like add the Aback things that

01:01:41
missed and identify all that stuff, why are humans the standard for maintainability? So I would try to generate the specs going in reverse, but it's it's hard to create >> it's hard to create broad guidance on this thing. >> Yeah, >> it's it's right. >> Do you agree with that the concept of shareware has returned? I don't know. I think we're in a Geio Cities moment. Like we're back to Commodore 64s. We're going to have everyone >> Geio Cities was such a cool moment in

01:02:13
the internet. >> Yeah, right. I think we're at the Geio Cities moment. Like we everyone is going to teleport to the future and in invent all they wanted to do and they're just going to give it away. Or maybe they keep it to themselves. Maybe they keep it themselves. I think we're going to see a whole bunch of like the same way in com 64. is like, "Hey mate, can you copy me that floppy?" Like someone does something, even if they don't share the source code or they do some

01:02:38
documentation, whatever, just that idea that it is possible, they're going to go open like Super Whisper or Whisper Flow and go, "Hey, that person over here, a really good idea. They describe the features, etc." >> And they got their own copy. >> So yeah, the topic of Moes is kind of going to disappear. I think it's going to be a beautiful time for a software engineer, >> but as software development, that that profession is now closed. >> Yeah. Yeah, >> because it's been replaced with a RA

01:03:02
loop. >> And I guess one final question just to end up from YouTube. Would it be fair to say that we are seeing in software engineering now will be true for most fields requiring creativity as well as a defined process such as finance, law or manufacturing? >> I don't know. Let's play let's play with it. I don't know. I think so. The reason why this is happening so much in our profession is we can be mechanically verified. So if if you think about I've talked about the the wheel of the notion

01:03:35
of a wheel. So you have a generative function and then you got the bottom half of the wheel which is the back pressure. The back pressure if it generates something wrong the test pushes back on the generative function to try again before the wheels allowed to turn around. Any discipline where you can do that is going to be automated and that's absolutely certain when you can mechanically verify it's going to be automated. Now I guess what is the failure rate for humans if it can't be

01:04:06
autom automated? Let's say you take a a lawyer um what happens if a parallegal makes mistakes. What if the LLM the LM definitely will make mistakes? What if the error rate on an LLM is less than the rate of a human? And and they're already used to the idea of failure and that's why they have three or four different people read a contract before it goes out. So like this is how I I would I've never worked in the legal profession, but this would be the approach I would take in a legal

01:04:35
profession. What I would do is I would build a whole bunch of like common red lines uh uh clauses in a contract like underlines things that you want to keep out an eye out for and I'll turn them into test cases and I'll keep those contracts around and I make sure when I change a model this is eval like it detects these type of test cases doesn't be 100% needs to be 90 80%. does you get used to the failure because like even in biology, humans, it's never been like 100%. It's been random chaos.

01:05:11
Um, and then when a new contract comes in, you have a look, did it detect it? Oh, wow. We've got to speed up. We got to speed up. And you can never outsource accountability to a machine that's always on the human. But what happens when a lawyer slash engineer, lawyer, engineer, they exist out there. They're both lawyers and engineers take these types of approaches and they start instead of having to look for this, they're actually building up a linting library >> for law. >> They're building up a static analyzer

01:05:41
library for law. This is this is the approach I would take. I would not be surprised if they take this approach as well. >> And so that their burden is a lot less. >> Yeah. >> Cool. Um folks, we're on time. Um, this has been a fascinating conversation. Truly worthy of a start of the year in season 2 of AI Giants. Jeff, I'm so thankful for you accepting the invitation. Thank you for your candid, honest uh very truthful um type of of dialogue that we have here today and for

01:06:14
answering these some some of these tough questions and answer also questions from the audience. Thanks for being here. >> No problem. Thanks for having me on. Um, as confident as I might be, I don't know. Um, but one thing's for sure, I'm not going to be stuck like a deer in the headlights while this goes on or wait for the next model to get good at this. I hope people who who watch this, go out there. I've got a a workshop that teaches you how to build an agent. This is now the baseline fluency. If we ever

01:06:47
cross paths and you and I'm interviewing, I want you to be able to explain that on a whiteboard. I'm making it very clear what the the new lines are and I hope uh people invest in themselves because I want to increase the pool and the mo of the people who can actually use the new computer. >> Wonderful. Um great. Well, folks, today we looked behind um the scenes at the origin story of Ralph with the great Jeffrey Huntley. Uh fascinating conversation. I hope you had as much fun as I had. As always, we

01:07:21
at Curtis have we are an inand solution for building products safely. Um next week, uh we are joined by the CTO of Versell, so please don't miss out. Um and with that, have a wonderful rest of your week and thank you for being here and for all your questions. See you guys. See you.

