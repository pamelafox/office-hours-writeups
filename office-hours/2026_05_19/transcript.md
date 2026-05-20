[00:00] All right, welcome to our weekly Python
[00:05] plus AI office hours.
[00:08] Welcome everyone. I see we have more
[00:10] folks flowing in. I'm Pamela from Python
[00:14] Abby.
[00:15] Uh I did spend the last week at Pyon
[00:18] where I did a lot of talking and uh my
[00:23] voice is pretty dead. Um so that's why I
[00:28] sound a bit funny. I do have a massive
[00:30] amount of lozenes,
[00:33] but I'm making really good progress
[00:34] through them. Uh, so we're gonna we're
[00:38] gonna do what we can. Uh, so in this
[00:42] office hours, what we usually do is, you
[00:45] know, talk about
[00:47] news over the last week, new things
[00:49] happening, new things, uh, we've been
[00:51] working on. And then
[00:54] when you have any questions either about
[00:57] these new things or about just something
[00:59] you've seen, uh, just go ahead and stick
[01:02] it in the chat. Um, so yeah, so as I was
[01:07] saying, I was just at Pyonus and I had
[01:11] several
[01:13] talks and tutorials there. So let me go
[01:15] ahead and share those with you. Uh so I
[01:20] did an MCP tutorial. Uh this was similar
[01:23] to the MCP series that we did in
[01:26] December except for this one I did add
[01:30] on
[01:32] um I added on some new
[01:34] parts of MCP. So specifically
[01:38] elicitations and MCP apps. Those are
[01:41] newer parts of MCP protocol. And also
[01:44] for this one uh I had
[01:49] uh
[01:51] um I also this one has exercises. So if
[01:54] you're looking to really get familiar
[01:56] with MCP and you want a structured way
[02:01] to go through it uh then you could uh
[02:04] look through my slides and basically the
[02:07] slides link to the exercises so you
[02:10] could do a little self-paced tutorial to
[02:14] uh to learn how to build MCP servers in
[02:18] Python.
[02:20] So that was the tutorial that I ran at
[02:23] Pyon. Uh the other thing uh that I did
[02:27] at Pyon
[02:29] was a
[02:32] uh this talk here about making slides
[02:35] using reveal.js
[02:37] and GitHub copilot.
[02:41] And you know that's helpful for any of
[02:43] you that ever give presentations. You
[02:45] can do it for conferences, for internal
[02:49] presentations, um, whatever you do. Um,
[02:52] but you know, basically had my tips and
[02:55] examples for how I use GitHub Copilot to
[02:59] make my to make my presentations. Here's
[03:02] a little video here um, where it makes
[03:05] it and and also link to my skills. So,
[03:08] as part of that, I also made a
[03:11] a little tutorial for that as well. So,
[03:13] if you wanted to, you could you could
[03:15] actually do a little structured
[03:19] uh a little structured tutorial there to
[03:22] see what it's like to make things with
[03:24] reveal.js.
[03:26] Uh, as you can see, like first you
[03:28] generate the basic deck and then you can
[03:30] ask the co-pilot to make it fancier. And
[03:34] what's really fun is that if you use VS
[03:35] Code, it has this integrated browser
[03:37] that's shared with the agent. You can
[03:39] see here it says sharing with agent and
[03:41] so co-pilot can very easily iterate on
[03:44] frontends. So if any of you do anything
[03:46] with frontends um like frontends for a
[03:49] full stack web applications in this case
[03:52] it's a front end for slides but if you
[03:54] ever do that definitely use the VS code
[03:56] integrated browser because then your
[03:59] agent can get rapid feedback on whatever
[04:02] it's building. So that's really really
[04:04] key and I really love it. Um, and some
[04:08] tips here like mocking up asy diagrams
[04:10] of different slide options. Once again,
[04:12] you can use this same technique if
[04:14] you're doing anything for front end. You
[04:15] say, "Hey, mock mock up an ASKI diagram
[04:17] of what this front end could look like,
[04:19] right?" So, it's nice to start off with
[04:21] the ASKI diagrams first before uh, you
[04:25] know, having it write all of that code.
[04:27] uh it's much faster to think through
[04:28] asky diagrams
[04:31] and then do some auditing and then
[04:33] afterwards turning the presentation into
[04:36] writeups and stuff like that. Um so
[04:39] that's all you know a lot of that is
[04:41] based off of skills that I have in uh in
[04:45] this repo here presentation skills.
[04:49] Um, okay. So, I did that at Pyon.
[04:55] Um,
[04:57] the uh let's see the other thing. So, at
[05:02] Pyon, we also had a booth and at the
[05:04] booth I was demonstrating our new GitHub
[05:07] co-pilot app. Uh this is a this is like
[05:11] brand new as of the next la last week
[05:14] and it is available
[05:16] for
[05:19] um for let me see yeah this one it's
[05:22] available for co-pilot enterprise and
[05:25] business subscribers.
[05:28] So if you have either of those you
[05:30] should be able to use the app already.
[05:33] And this is basically a desktop app that
[05:36] wraps the CLI and makes it particularly
[05:39] easy to go between sessions and
[05:41] different repos. So I actually really
[05:42] like it. I don't think I'll use the CLI
[05:44] anymore. Um because it's basically like
[05:48] for me it's a it's a better UI than the
[05:51] CLI because I'm not I don't really like
[05:53] CLI that much. Not especially not for
[05:55] this where there's like a lot of rich
[05:57] information I want to see. So this is
[05:59] the same kind of thing that previously I
[06:01] would do with the CLI, but now I've got
[06:04] like a much better way of viewing it. Uh
[06:06] so this is actually this is what I ran
[06:07] like 10 uh you see 19 minutes ago. So I
[06:10] wanted it to make this this PowerPoint,
[06:13] right? So uh so it used the skill and
[06:17] the skill used MCP servers, right? So
[06:19] this you know you can this this will by
[06:21] default it's a wrapper for the copilot
[06:23] CLI. So if you have MCB servers that are
[06:25] hooked up to the copilot CLI, then it's
[06:27] already hooked up. So if you go here, we
[06:29] can see here's the MCP servers, here are
[06:32] the skills, right? So it's got all the
[06:35] same hookup as the CLI.
[06:38] Um,
[06:40] so yeah, and I I like I like doing this
[06:43] here because then it's like I can really
[06:45] easily expand it and see, okay, this is
[06:48] um I would decide to do a web search.
[06:49] Uh, that's cool. Actually, I didn't even
[06:52] know it had a web search tool.
[06:55] So it has a web search tool. Very good.
[06:57] Um, right. So, you know, went through
[07:00] all of that and then and then finished.
[07:03] Uh, now more commonly, you're going to
[07:05] probably use this for interacting with
[07:07] your GitHub repositories. So, for
[07:09] example, um, I asked it to upgrade this
[07:13] repository to use the new HPX2 package,
[07:17] right? So, it went through, it looked
[07:19] through all the code and um, you know,
[07:23] looked looked at code files. We can see,
[07:25] you know, we can see what code it was
[07:27] looking at, which that's really nice.
[07:30] Um, it did some file editing, so we can
[07:32] also see what files it edited. We can
[07:35] see the inline diff. Like, yeah, it's
[07:37] just so it's so nice. I love it. Uh, and
[07:40] then it makes a PR, right? And then we
[07:43] can open the PR just right here in, you
[07:47] know, in the app. So, we can see here's
[07:49] the PR and then, um, we can decide
[07:51] whether to merge it. You can also uh use
[07:54] the agent merge where the agent just
[07:57] will do the merging for you and fix the
[08:00] CI and all that stuff. I didn't enable
[08:02] the agent merge because I do like to
[08:04] look at my PRs first, but I have some
[08:07] colleagues that really like the agent
[08:08] merge. So there we have the whole end
[08:11] workflow. Now the other thing that's
[08:13] exciting here is the uh uh workflows. So
[08:18] workflows is a feature inside this app
[08:22] where you know if there's a kind of
[08:24] thing you just want to be run on uh you
[08:27] know on a on a standard basis. So you
[08:28] can see this one issue triage. This is
[08:30] treating issues from our most popular
[08:33] repo. So this is set to run every day at
[08:36] 9:00 a.m. And this is really nice
[08:39] actually. Um,
[08:42] so it it uh it added on um
[08:48] it so I you know so basically you give
[08:50] it a prompt and it's going to run that
[08:53] prompt when you know whenever you tell
[08:55] it. So here I said to run it daily, you
[08:57] could run weekly. You could also run
[08:59] based off a trigger. So it runs the
[09:02] prompt, it does you know whatever it
[09:04] does. It can use MCP servers. It can use
[09:06] you know it can use anything that you
[09:07] could use in any prompt. Uh, and then it
[09:10] triumphs the issues and um, you know,
[09:14] said what I should fix right now, next
[09:16] sprint, black backlog, low priority, and
[09:18] then it even has this nice this cool
[09:21] widget here. I actually didn't even I
[09:22] don't know if this is new, but um, it
[09:25] looks like this is an inline
[09:28] uh, like an inline widget that
[09:30] specifically
[09:31] is helpful for looking at issues. So you
[09:33] can see this has got really nice
[09:36] integration
[09:38] uh with GitHub specifically um because
[09:41] you know it's from GitHub so they know
[09:42] you're going to be looking through
[09:43] issues.
[09:44] Uh so yeah so you can set up like these
[09:46] are personal workflows so you just set
[09:48] up whatever workflow makes sense for
[09:50] you. Uh they've got a whole
[09:53] uh they've got like a whole gallery of
[09:55] examples of workflows you might want to
[09:57] run. Uh like a change log, a re repo
[10:00] audit, accessibility audit. That's nice.
[10:03] Uh performance improvements, right? So,
[10:05] common things you might want to build,
[10:07] but also it lists all of your skills and
[10:10] because a lot of times skills might be
[10:11] something you want to do every week. For
[10:12] example, I have this recap my week
[10:15] skill, which I use before my weekly
[10:18] one-on-one with my manager. And right
[10:20] now, I have to remember to do it. But
[10:22] what I can do instead is say, let's do
[10:24] it weekly. And I'm going to do it um
[10:28] let's see. Normally I talk with her
[10:30] Monday at 3 p.m. So I could set it to
[10:33] run, you know, Monday at 100 p.m. You
[10:37] know, that'd be reasonable. Um, recap my
[10:40] week for my meeting with my manager.
[10:46] Uh, okay. Okay. So then
[10:49] here we go. It doesn't really need to be
[10:53] on any particular repo. So now that's
[10:55] set to run weekly Mondays at 3 p.m. So
[10:58] that's super handy. Uh and then you can
[11:00] also just have chats that aren't
[11:02] specific to a repo. So you just say
[11:03] like, hey, how do I use HBX2? Right? Uh
[11:08] HBX2 is a new version of HBX. Uh there's
[11:12] if you are using HBX, which is a common
[11:14] way of making requests, there are now
[11:16] multiple community forks of HBX due to
[11:19] maintainability issues with the original
[11:21] HBX. So, you know, you might want to use
[11:23] HBX2 or maybe HBXYZ.
[11:27] Anyway, that's a question you might send
[11:29] off to the, you know, to your co-pilot
[11:32] agent.
[11:33] Uh, so that's pretty exciting. Uh,
[11:35] definitely check that out if you do have
[11:38] an eligible eligible license. Uh, I I
[11:41] really like it.
[11:44] Um,
[11:46] what else? Oh, yeah. I wanted to show
[11:49] this. Okay.
[11:51] Uh so in foundry
[11:54] uh I've been playing more with you know
[11:56] other models you can deploy in foundry.
[11:58] So for example
[11:59] uh in foundry you can deploy the
[12:01] enthropic models right and we talked
[12:04] about this in the past but here I've got
[12:06] a claude sonnet model and you know this
[12:10] is deployed here and then um what I can
[12:13] do let me get um
[12:19] then you can actually let's see if I
[12:21] have this one running locally
[12:27] cupcakes workshop. Okay.
[12:31] Okay. Uh so
[12:35] here we go. Then you can actually write
[12:38] code
[12:40] um you know against this model
[12:44] and say hey here's my model deployment.
[12:46] This is my key. This is my URL. Uh and
[12:49] in this case we are um we are pointing
[12:52] this agent. So this is an agent built
[12:55] with agent framework but that's using a
[12:57] foundry model.
[12:59] We're pointing that at an MCP server
[13:01] that's deployed on container apps. And
[13:04] then um this this agent
[13:07] can order cupcakes
[13:10] uh from
[13:13] uh from the MCP server.
[13:16] So let's try running it. See if my
[13:19] enthropic is up right now. I think so.
[13:23] And this is a this is for a workshop
[13:26] that we just ran in San Francisco two
[13:28] weeks ago and then in London today.
[13:31] Um and what's very cool is that the
[13:34] creator of Cloud Code was in the London
[13:37] workshop and so he actually did the
[13:40] workshop and ordered a cupcake.
[13:44] Um but it looks like it's still
[13:45] connecting there. Okay, there we go. So,
[13:48] it's connected to the MCP server and
[13:50] then says, "Do I have a customer ID?"
[13:53] No, let's create a new one.
[13:56] Uh,
[13:58] wants my name,
[14:01] last name. So, it's just getting
[14:03] information that it needs in order to
[14:06] make the the MCP tool call from the
[14:09] cupcake server so that I can order it.
[14:11] Uh, let me find
[14:14] the cupcake store dashboard.
[14:17] One sec.
[14:20] Uh, D. There's the dashboard. Okay. So,
[14:24] here's the dashboard. You can see all
[14:26] the orders are currently um there's no
[14:30] current orders because the workshop was
[14:32] a few hours ago. All right. Which one do
[14:34] I want? I want chocolate.
[14:38] Looks like these are the flavors they
[14:40] had in London today.
[14:43] Uh, and it says, "Look at the big
[14:44] dashboard screen." Okay, this is how we
[14:47] make sure you can only order these
[14:48] cupcakes if you're in person. And then
[14:51] I'll say it's a test order. Okay, so now
[14:55] it should go through and it's being
[14:57] slightly slow right now because it just
[14:59] made that order. So, if I go back to the
[15:01] dashboard, you can see that indeed the
[15:04] MCB tool call went through and there is
[15:08] now an order for chocolate cupcake on my
[15:11] dashboard.
[15:13] Okay, so that's one example of a cool
[15:16] model you can use. But now I also want
[15:18] to show a model that I finally got
[15:20] deployed a couple days ago that I've
[15:23] been really excited about being able to
[15:26] use from here. Uh let's see. It is here.
[15:31] So, let me find
[15:33] that model.
[15:36] Uh, actually, is it this one? I think it
[15:38] might be. Let's check. Uh,
[15:42] deployments. I think it's a different
[15:44] one. Oh. Oh, this is why I deployed
[15:46] Kimmy. Kimmy is a model that a lot of
[15:48] people talk about as being quite a good
[15:50] model. So, I also want to start playing
[15:52] around with Kimmy. I don't know if any
[15:53] of you have used Kimmy, but I was
[15:55] actually trying to set up my GitHub
[15:56] co-pilot to use this Kimmy. Uh, but I
[15:59] didn't quite get that working yet. So,
[16:01] have to get that working uh on a
[16:03] different week. But let me
[16:06] uh let me switch projects.
[16:08] I think it's
[16:13] this one. Let me try this one.
[16:20] This one. Yep. Okay. So, this one I also
[16:22] have Kimmy. I guess I've been doing
[16:24] Kimmy everywhere. Um but then the one I
[16:26] really wanted to show was MI image 2E.
[16:30] Uh this is um an image generation model
[16:35] and it's really quite good. Um, so in
[16:39] this playground, we can, you know, give
[16:40] it a prompt and have it generate an
[16:43] image and like generate a photo of
[16:48] developers in an office hours about
[16:53] Python plus AI.
[16:56] All right. So, we can send that off and
[16:58] it'll spend a few seconds generating. It
[17:01] does take some time to generate. It's
[17:02] not instant. Um, and it'll generate a
[17:06] nice image. Uh the thing I like to do is
[17:08] actually to give it source images. Uh
[17:10] the this playground doesn't support
[17:12] that, but if you build your own
[17:14] application on top of it, it does. Uh so
[17:17] here we can see our our office hours.
[17:23] Um let's see if I can zoom in to see
[17:25] what these people are talking about.
[17:28] Let's see. It's always a test of what
[17:29] the audio looks like, right? What the
[17:32] sorry what the characters look like. I
[17:33] cannot read those words. I guess that's
[17:36] one way to to do it is just to make it
[17:38] so you can't read the words. So, it's
[17:40] not perfect, but I think it's pretty
[17:42] good. And uh especially if you give it
[17:45] if you give it some uh some input image,
[17:49] uh then it's it's really good at
[17:51] transforming it. Let me show uh the
[17:54] alternative application. So, this is an
[17:56] application that somebody else built on
[17:57] top of it. And so, when people were
[18:00] coming up to the booth at Pyon, I was
[18:02] taking their images and turning them
[18:03] into new images. So this is Simon
[18:05] Willis. He has a fantastic blog about
[18:08] LMS and he always is generating images
[18:10] of pelicans. So of course I generated
[18:12] him as a Jedi with a pelican. Now you'll
[18:14] notice there is one flaw here in that he
[18:16] seems to have a lightsaber coming out of
[18:18] his knuckle.
[18:20] So not perfect. That's actually the
[18:22] first time I've seen it really make an
[18:24] artifact like that, which is quite
[18:26] interesting. Um but the the facial
[18:29] likeness is quite good. And that's what
[18:31] really impresses me about this model is
[18:32] that if you wanted to generate a picture
[18:35] of an existing person, it's quite good
[18:36] at capturing that. Um, this is another
[18:38] Python programmer called Trey and it
[18:40] looks a lot like him and he's teaching
[18:43] iterators. Uh, and then this is another
[18:45] one of Simon because somebody wanted him
[18:47] with a puffin instead. Uh, this is one
[18:50] of a um a type of poppy I have in my
[18:53] garden and it looks perfect. I cannot
[18:56] find any flaws with it. So just uh you
[19:00] know I'm really impressed with this
[19:00] model. I usually do not use image
[19:03] generation models because of my you know
[19:05] fear of replacing artists but I do think
[19:08] that for something like photoshopping
[19:11] uh you know basically like a better
[19:12] version of Photoshop uh then you know
[19:14] then it can be quite quite good.
[19:19] Uh so yeah check that out. You can
[19:21] deploy that from from foundry. Uh so
[19:25] yeah generally we want to encourage
[19:27] developers to try the other models on
[19:29] Foundry and give feedback right so try
[19:31] the anthropic models try Kimmy Mistl
[19:35] coher whatever like try all those models
[19:36] and then um you know tell us whether we
[19:41] need to make it easier to work with them
[19:43] uh because a lot of times I do when I do
[19:45] try it out I find out oh STK doesn't
[19:48] quite work with it or something right
[19:51] uh so
[19:53] yeah and Then as part of in addition to
[19:55] that model, there's also some other MIA
[19:58] models that my colleagues say are quite
[20:01] good. Um I didn't try these ones yet,
[20:04] but I do hear really good things about
[20:06] them. So MAI transcribe one and MAI
[20:10] voice one
[20:12] uh for transcription and then voice
[20:15] generation.
[20:17] Uh, so I'm excited that we have some wow
[20:20] that we have some high quality models
[20:22] coming out here
[20:24] and that they are governed by safe and
[20:27] responsible AI. That's I like that. Oh,
[20:29] and they have model cards. Yay. Oh, I
[20:31] haven't read the model card. I love
[20:32] reading model cards.
[20:35] Okay. Oh, so it says this is so cool.
[20:38] Okay, so it says how they did
[20:40] evaluation, right? So they this is like
[20:42] kind of the category that they rate
[20:44] stuff on. So photo realalistic
[20:47] um product brand and commercial 3D
[20:49] imaging cartoon anime fantasy text
[20:52] rendering uh then they did red teaming
[20:55] that's good that they did red teaming uh
[20:57] to make sure it can't generate uh you
[20:59] know violent gory contextual content or
[21:01] nudity
[21:03] um and yeah and how did they do the
[21:07] training okay they did be uh broad
[21:09] general purpose domain every objects
[21:11] natural scenes
[21:13] I'm trying to figure wide is so good at
[21:18] retaining the facial likeness. Okay, so
[21:20] here's a data summary.
[21:23] I Yeah, I I love model cards. I I think
[21:26] you can like really understand more
[21:28] about the LLM well model training
[21:30] process when they have a model card. So
[21:33] they describe the training corpus. Um
[21:36] they don't go in a ton of detail here.
[21:39] Uh but we can see the text, the image.
[21:43] Uh so that's it just text and image. Um
[21:48] people focus data. Ah okay.
[21:51] Um so
[21:54] they special attention is given to
[21:57] images of people including portraits and
[21:59] full body shots. So that might be why
[22:03] they're so good at peoples. And then
[22:04] also they try to have a range of
[22:07] everyday objects, natural environments
[22:09] and human activities.
[22:11] complex lighting.
[22:14] Okay.
[22:16] Really cool. All right. Um so yeah,
[22:20] check check that out. I think that's
[22:21] really exciting. Um what else? We
[22:24] haven't had any questions yet. No one
[22:25] has questions. Okay, let's see.
[22:29] Um what else
[22:32] have I been showing? Okay, which which
[22:36] text to speech model do you recommend
[22:37] using locally offline?
[22:41] haven't used them. I think most people
[22:42] are going to tell you whisper or like
[22:44] using whisper inside
[22:47] um some sort of some sort of harness. U
[22:52] but that might be something that other
[22:54] folks in the chat
[22:56] um can can uh reveal their what they're
[22:59] using offline. Um I only just got a
[23:03] computer that can like really run more
[23:04] models because now I've got 64 gigs of
[23:06] RAM. So I am hoping to
[23:10] start experimenting more with uh with
[23:13] local models and seeing how far we can
[23:16] push them with the additional RAM. So if
[23:19] there are recommendations for things to
[23:20] try
[23:22] uh let me know. Let me see if any of
[23:24] them are any of the TTS models are on
[23:27] here. This is can I run.ai. No, I don't
[23:30] think they do the TTS models.
[23:33] Um, uh, so Zoro asks, "Was the first UI
[23:37] just the regular MS copilot UI?" No, I
[23:40] was showing the new GitHub Copilot app.
[23:42] So, um, this is brand new as of last
[23:45] week, and it's it's you can use it if
[23:48] you have GitHub Enterprise or or Pro.
[23:50] Uh, there's a link to it if you look way
[23:52] up in the chat. It's just GitHubgitub.
[23:57] And yeah, it's it's a really clean UI. I
[24:00] actually I know some of the people
[24:01] working on the UI and they're really
[24:02] good. UI developers. So, I think they've
[24:05] done a really nice job.
[24:08] Kev says, "I want to experiment with
[24:10] generative UI. Is A2 UI integrated with
[24:14] map and is it a good starting point?"
[24:15] Oh, that's a good question. So, I know
[24:17] that um for fast MCP, I know that they
[24:21] have generative UI because that was one
[24:23] of the things we talked about um here is
[24:27] that if you're making an MCP app, your
[24:29] MCP server could actually respond to the
[24:33] request with um I should say generative
[24:35] UI really um and and that will you know
[24:42] output uh UI components on the fly. Um,
[24:45] so that that would be one way of doing
[24:47] gender UI, but that's if you're, you
[24:48] know, actually building an MCPS server
[24:50] that you want to output an app. Uh,
[24:53] presumably you're you're not. Um, so
[24:56] let's go ahead and look into agent
[24:58] framework and see what it has for Oh,
[25:02] look at this. We got AG UI. I think what
[25:06] we're looking for is AGUI
[25:09] seam with a web interface. Okay. Um, is
[25:14] this doing generative AI or I think AGUI
[25:19] is
[25:22] basically showing you what the front end
[25:24] and back end should work on. I don't
[25:25] know if it's actually
[25:28] Let's see what HUI is and see if that's
[25:30] what we're looking for. If we're looking
[25:31] for something else.
[25:34] Um, so I think this is like how the
[25:36] front end back end works. I don't know
[25:38] that this is actually
[25:40] Oh, here we go. AGUI has Okay, so
[25:43] understanding AGUI's relationship with
[25:46] generative UI specifications.
[25:49] Um, so it says A2 UI, MCP UI, and
[25:52] OpenJUI are all generations.
[25:55] Um, so we have A2 UI. Ah, and that's
[25:58] what you just asked about. So that's
[25:59] from Google. Declarative LM friendly
[26:02] generative UI spec. Okay. Open JSON UI
[26:07] and then MCP UI. I would think that MCUI
[26:10] is basically replaced by MCV apps at
[26:12] this point. I think that they probably
[26:14] haven't updated this yet. Um because MCV
[26:17] apps are based off MCUI.
[26:20] So AGUI is not gener. Okay, so we're
[26:22] looking for A2 UI. All right. Okay,
[26:26] good. Um let's see
[26:29] if we have any sort of A2 UI
[26:32] in this repo here.
[26:35] Um, Sylvestri
[26:38] has
[26:40] a link here. So, we didn't get any hits
[26:43] when we searched for it, but let me look
[26:45] at discussions. Oh, wait. We did get
[26:47] once. We did get a hit. Okay. Um, I've
[26:50] been looking to ATI Google announcement
[26:53] any progress. This is in prog. Okay. So
[26:56] this is Evban Evans
[26:59] software engineer on math and it says it
[27:01] is in progress for math Python
[27:04] and now of course someone wants forn net
[27:07] but hey we're Python here. Uh let me
[27:09] just sub to this issue. So uh yeah I
[27:12] would say subscribe to this issue
[27:15] probably um you'll see a pull request
[27:18] come through. I don't know if there's a
[27:19] pull request yet. I think I would have
[27:21] found that when I searched. So,
[27:25] um I'm
[27:27] guessing that
[27:30] he hasn't pushed it yet.
[27:33] Um
[27:36] so
[27:38] yeah, uh
[27:41] so yeah, so that's in that's in progress
[27:43] for agent framework.
[27:47] Um but you might if you just want to
[27:49] start you could it depends if you're
[27:51] building servers. So, I know that fast
[27:53] MCB already already um implements that
[27:56] that so that could be kind of fun if
[27:58] that makes sense for you to experiment
[28:00] with the fastm approach. Let me get you
[28:02] a link to that one. Um
[28:06] apps apps apps apps
[28:09] apps. Here we go.
[28:14] And this one will send down you know a
[28:17] constrain apps constrained to the prefab
[28:20] components uh which you know would be
[28:22] safer uh than passing down just any
[28:25] arbitrary HTML. Uh so that' be fun to
[28:29] experiment with. And then this is the
[28:32] link that Sylvester shared from deep
[28:34] learning.ai.
[28:36] Uh so this is with co-pilot kit. That's
[28:38] an even though that sounds like a
[28:39] Microsoft thing, that is a open-source I
[28:42] believe an open source tool. Um,
[28:47] oh, and they're the team behind the AGUI
[28:49] protocol.
[28:51] Okay. Well, this sounds Yeah, this
[28:53] sounds really useful, too. Uh, so
[28:55] co-pilot kit, right? So, if you
[28:59] Okay, but we do I thought I think we do
[29:02] I think math does integrate with
[29:07] Okay. Well, I think we do integrate with
[29:09] AGUI,
[29:11] but I so I imagine maybe the um a A2 UI
[29:17] integration might build on this or maybe
[29:19] it'll be separate. So, we'll have to see
[29:21] what that you know what that ends up
[29:22] looking like.
[29:25] Uh it sounds pretty fun, huh? Uh
[29:30] so I think in this case you would like
[29:32] build the front end using copilot kit
[29:34] and then the back end would come from
[29:37] math uh generating the UI.
[29:42] Good questions. Um so
[29:46] let's see another thing that came up was
[29:50] um there was a talk at Pyon
[29:54] about about Monty which is the
[29:58] uh let me find it uh Monty Monty Monty
[30:02] Monty is a
[30:05] basically um you can run Python from
[30:09] Python but inside but it like it's
[30:12] completely safe and sandbox. Uh, it's
[30:14] only a sub a sub subset of Python. Um,
[30:17] but I I put together a quick example of
[30:21] using that from a math agent. So, let me
[30:25] find that.
[30:27] I think this one
[30:31] agent tools. Yeah. All right. So, let me
[30:34] just run
[30:36] run this one.
[30:42] Okay. So, Python examples, agent tools,
[30:51] Monty, right? Well, that's a good point.
[30:53] So, Monty, there's kind of two main use
[30:55] cases for Monty. So, one of them is for
[31:00] code mode. And code mode is the idea
[31:01] that in when you're doing tool calling
[31:03] from agents, you have this like back and
[31:05] forth where you have lots and lots of
[31:07] tool calls and where you might want to
[31:09] run some tools in parallel, you might
[31:11] want to run them in in in in sequence
[31:14] and that adds a lot to your
[31:17] communication with LM. So if you use
[31:19] code mode, you're going to just have the
[31:21] LM write the code that calls those tools
[31:24] as if they were Python functions. And
[31:25] that way that code can do a sequence, it
[31:28] can do a for loop, it could do a gather,
[31:30] like it could do a lot of stuff inside
[31:32] that code. And the idea is that that's a
[31:34] more efficient approach to
[31:37] um to tool calling that reduces the
[31:40] overall tokens used and just the back
[31:43] and forth um um of the yeah of the tool
[31:47] calling. So that's that is one of the
[31:50] really big uses for Monty and um and
[31:54] actually the uh agent framework team is
[31:58] working on a PR for agent framework that
[32:02] adds Monty as a code mode option. Uh
[32:06] it's just here
[32:08] uh
[32:10] so this is like the goal of this is
[32:12] about more efficient
[32:15] tool calling, right? Yeah, exactly. It
[32:18] does the glue code. You can't
[32:19] anticipate. So, um,
[32:22] so yes, if you did want to use this
[32:24] from, it's really easy to use from
[32:25] Vidantic AI because of course they they
[32:27] created Monty. Um, but, uh, yeah, if you
[32:31] wanted to use it in agent framework,
[32:34] then uh, you can see it is in rapid
[32:37] review right now. Just got reviewed
[32:38] yesterday. Um, and yeah, that was that's
[32:43] the talk. Thank you, Sylvester. And he
[32:45] also he did an extended version of that
[32:47] talk at Pyon. Um I don't think the Pyon
[32:51] I don't think the PON videos are up yet.
[32:54] Um but it was
[32:58] uh let me see it was was it on the
[33:00] second day?
[33:04] Uh
[33:06] where did Monty
[33:09] say? No.
[33:13] Where did he do it? Samuel,
[33:16] why can't I find it?
[33:20] I don't know. I don't know why I can't
[33:22] find it. Um Oh, was there was Paulo and
[33:26] then right after that would have been
[33:29] Huh.
[33:32] I don't know why I can't find it. Maybe
[33:33] it's considered a Oh, it's probably
[33:35] considered like a a sponsored talk.
[33:38] Maybe it was a sponsored presentation.
[33:42] There we go. Okay. Okay. So, yeah. So,
[33:45] also look out for this talk from him
[33:47] because that one was interesting because
[33:48] he basically built on top of the agent
[33:50] con talk, but then he actually explained
[33:52] how Monty works. So, he was going into
[33:54] the details of uh basically how they
[33:57] re-implemented Python in Rust. Uh so,
[34:00] got it a bit a bit more nerdy, but I
[34:02] thought it was quite interesting.
[34:05] Um
[34:07] so,
[34:10] yeah. So, and he did um so there's a
[34:13] hack monty competition and they like the
[34:15] hack monty competition did find one um
[34:19] issue. So, they fix that and then
[34:22] they're going to do a new version of it
[34:24] that for $10,000. So, um, you know,
[34:28] hopefully after I think they they say
[34:31] like after they do the 10,000 one, you
[34:33] know, $10,000 one, they they they're
[34:36] going to feel pretty confident about
[34:37] saying like it's it's pretty safe.
[34:40] Um, so yeah. So yeah, so there's two
[34:43] reasons for it. One of them is code mode
[34:45] in order to reduce tokens and LLM back
[34:48] and forth when doing tool calling. Um,
[34:51] and if you're using PDFI, it's very
[34:53] easy. That's like one line of code to
[34:54] add it in with Monty and then if you're
[34:57] doing agent framework just you know let
[34:59] me subscribe actually subscribe to this
[35:01] PR and you'll find out when that's
[35:02] available in agent framework. Um
[35:06] but I also wanted to see well just the
[35:10] idea of using Monty for um for code for
[35:15] code execution.
[35:16] Uh so here I added on a tool that does
[35:20] code execution
[35:22] and it just takes the code runs it and
[35:26] then gets a result and I put in the
[35:28] system prompt use the code execution
[35:31] tool if you need to do some date or math
[35:33] manipulation. So example like what can I
[35:36] do three weekends from now in SF right
[35:40] so I'm giving it a harder a harder date
[35:43] time and you know the hope would be that
[35:46] it decides to use that code execution
[35:49] tool to do that basic datetime in
[35:51] ablation um because if you've ever done
[35:53] datetime stuff with LLMs you know
[35:56] they're they kind of suck at it I mean
[35:59] it's surprising like sometimes they
[36:00] actually do figure it out if you're just
[36:01] saying you know this Monday next Monday
[36:03] as long as they know today's date, they
[36:04] can usually figure it out. Um, but uh
[36:08] yeah, if you give them just a Monty
[36:10] tool, then they can work out anything,
[36:12] right? They just say, "Oh, here's
[36:13] today." Actually, in this case, because
[36:15] I used to have this get current date
[36:16] function, but in I can just remove it
[36:19] now, right? Because it be like it could
[36:20] always just because it's very fast. So,
[36:23] I can just have it do everything with
[36:27] with Monty. Um, oh, let me get
[36:31] right. So basically I'm deferring all
[36:35] um you know all calculations updates I'm
[36:39] deferring it to the Monty tool.
[36:42] Um, so you can see in this case it
[36:44] immediately decides to call the Monty
[36:47] tool in order to find out today's date
[36:50] and then it tries to find the upcoming
[36:52] Saturday and then the next Saturday and
[36:55] then it gets back the results and then
[36:56] it sends those results
[36:59] um to the LM and now the LLM is you know
[37:03] is able to you know do the right um
[37:06] right calculations. So
[37:08] um so yeah so I think that's
[37:10] interesting. You can imagine also having
[37:13] a like a like a fast code execution
[37:16] tool, right? Call this the fast one. And
[37:18] then if you're, you know, using the
[37:20] OpenAI models on Foundry, then you also
[37:23] get access to like the the um the code
[37:26] interpreter, the built-in code
[37:27] interpreter. So you could have two code
[37:29] execution tools. You could have one
[37:30] that's for very fast stuff like with
[37:32] that does like, you know, access to
[37:34] datetime and math. And then you could
[37:36] have another one. We could say like hey
[37:38] if you need access to pillow or pandas
[37:40] or numpy then use the slow code
[37:44] execution tool right but that's more
[37:45] powerful. So one of them is obviously
[37:47] much cheaper and faster because it's
[37:48] running the python directly you know on
[37:50] on the machine. Uh the other one has to
[37:53] call out to our hosted code interpreter
[37:55] tool but it's more powerful because it
[37:57] can do that code generation. Uh so uh I
[38:02] think that's a interesting
[38:06] uh interesting idea. Um
[38:10] so we'll see just keep all that in mind
[38:13] as you're developing your agents as to
[38:15] what kind of tools your agents needs and
[38:18] if you want to try something like code
[38:19] mode. All right. So I see question from
[38:22] Keva. Can I use GitHub copilot with a
[38:25] model deployed in Foundry? Yes, there is
[38:26] a doc about it. Um, I didn't succeed in
[38:29] doing it yet, but let's see if I got
[38:33] um Okay, so I was trying to do it with
[38:35] that Kimmy the Kimmy model. Um, but I
[38:40] was trying to do it with
[38:43] um
[38:44] with keyless. Um, so let me show you my
[38:49] configuration
[38:51] for it. Uh, let's see.
[38:55] Manage. Okay. So if you go to manage
[38:57] language models. So under here we have
[38:59] all the copilot models and we have a
[39:01] lama models. I added those two. And then
[39:03] you can see I have a an Azure model. So
[39:06] what you can do basically go to add
[39:08] models and then you would pick Azure
[39:10] here. Maybe we should rename that to
[39:13] Foundry. But you know naming is hard.
[39:15] And then we go to the little gear icon.
[39:17] We say configure
[39:20] and oh no. Okay. I want to configure
[39:22] this one actually. How do we um Okay.
[39:25] Yeah. No, I just want to go to my
[39:28] configuration. Uh,
[39:31] okay. You can see I'm new to this. Uh,
[39:32] let's see.
[39:34] It's probably in I'm just going to go to
[39:36] my settings.json. I'm uh user settings
[39:39] JSON. Okay.
[39:41] Um,
[39:45] no, it's not in there.
[39:52] Where is it? Okay. I know what the JSON
[39:55] looks like.
[39:58] Where did I put it?
[40:01] Where did it go?
[40:04] All right, let's see.
[40:07] If I go here, other models, Kimmy,
[40:13] and then it's not going to work. I just
[40:15] trying to get a link to Okay.
[40:18] unrecognized account
[40:22] and where. All right, let's try and find
[40:24] the doc so I can remember how I did
[40:26] this. Voice code manage language models
[40:29] Azure.
[40:42] Okay, bring your own language model key
[40:45] so you can customize.
[40:50] Install language arts and
[40:52] considerations. add a model from the
[40:53] built-in provider
[40:57] and then you can manually own add your
[40:59] own.
[41:01] Okay, so this is the setting. So there's
[41:05] a setting for it here. So let's try
[41:07] adding a different one since um let's
[41:09] try adding since I have this one and
[41:12] this one has a key. Let's try adding
[41:13] this one and I need to change this key
[41:15] afterwards. Um so let's just try adding
[41:18] a new one
[41:20] actually.
[41:23] Oh, yeah. This one has a key. Okay. All
[41:25] right. Let's try doing this. So, we'll
[41:26] go to manage language models
[41:30] and then I'm going to add a new one
[41:33] here. Add models Azure.
[41:35] And
[41:37] no, that looks We'll just Well, yeah,
[41:40] I'm trying to add Okay, sorry. How do I
[41:42] add another model?
[41:46] Uh, why is this so hard?
[41:50] Fine. We're going to do a new group.
[41:52] Okay. Enter value for the API key. So
[41:55] I'm gonna enter Oh, okay. So you have to
[41:57] do Okay. All right. Sure. All right.
[42:00] Here it is. This is what I was looking
[42:01] for.
[42:03] So this Okay. So this is a separate All
[42:06] right. So it is a separate settings
[42:08] file. It's chat language models.json
[42:10] inside your user settings. This is what
[42:13] I was confused about. So here I've got a
[42:14] llama. I've got Azure. I've got Azure 2.
[42:18] Um, and here I'm going to say, you know,
[42:20] quad deployed.
[42:23] And the name is probably the deployment
[42:26] name. So we'll call it this. And then
[42:29] the URL
[42:30] should be,
[42:32] let's see, I think it should end with
[42:34] V1.
[42:37] And then tool calling true vision true.
[42:43] And
[42:44] I think I already pasted in the secret
[42:47] hopefully. Okay. And then we're going to
[42:48] go and select this from here and then
[42:53] see if we can get it to work.
[42:55] Unrecognize.
[42:58] And it's still doing this.
[43:01] So I can't I have not gotten that. This
[43:02] is the same error I got before.
[43:09] Okay. I'm just going to message the team
[43:11] about it.
[43:13] Um
[43:15] because it shouldn't be this hard,
[43:16] right?
[43:18] Uh let me
[43:20] let me message our documentation person.
[43:23] I am I am still failing to get by y key
[43:27] working and I got another
[43:31] question about it. A and oh
[43:35] tried it with a key model
[43:39] as well.
[43:42] Um,
[43:46] and let me get here's I got this error.
[43:53] Any idea what's wrong? All right.
[43:58] I haven't gotten work yet. You got it to
[44:00] work. I am an insider. So, what is your
[44:02] does your what does your URL look like?
[44:04] Am I using the wrong URL? Check debug
[44:07] logs. Okay, we can check the debug logs.
[44:09] We can let's work this out. So we have
[44:11] output or which debug logs are we
[44:14] talking about here? Tasks
[44:16] um copilot
[44:18] uh
[44:20] yeah so it just says unrecognized Azure
[44:24] deployment URL agent debug. Oh you want
[44:27] to go to agent debug. So agent debug is
[44:30] over here. Agent debug logs. Um
[44:36] yeah, this one doesn't haven't found
[44:39] this to be so useful yet. Uh it just
[44:42] says so here we can see that co-pilot
[44:46] errors
[44:48] uh with this unrecognized as your
[44:50] deployment URL.
[44:53] You just gave the key no URL. How would
[44:56] it then know um what the what the URL
[45:01] was? Because it's going to be different
[45:02] based on everything. All right. So,
[45:04] okay. Let's see. Thanks for
[45:07] They had the same problem.
[45:10] Um, the coil it only supports open AI
[45:13] models. That shouldn't be true. Um,
[45:17] okay. Loosening.asure.
[45:22] All right. So, they say it should be
[45:25] what do they say? It should be.ai.
[45:29] So, there I think I'm using.ai.
[45:31] Let me double check.
[45:33] Um, yeah, I am using.ai.
[45:36] Oh, you're using anthropic directly.
[45:38] Okay. Yeah, in this case, I'm trying to
[45:42] um
[45:44] use it um via So, let's try what if
[45:49] Yeah, I uh I don't see
[45:53] it only. It says Okay, it says it only
[45:55] throws I see the actual code. Oh, here
[45:59] we go. Okay. So, it says if URLs
[46:02] includes
[46:04] All right. So, this is what we're going
[46:05] to do. We're going to check the actual
[46:06] VS Code source code. Um, is it is it in
[46:11] here last month?
[46:17] I think that they like didn't they move
[46:19] it back into this repo?
[46:21] First, we got to figure out
[46:24] where the code's coming from. Okay, here
[46:26] we go.
[46:28] Uh that's the test for it.
[46:32] So as your provider.
[46:34] Okay. Great. All right. So this is the
[46:36] actual code that VS code is running.
[46:40] So it says
[46:42] if the URL includes models.ai.asure.com
[46:48] or Okay. So in this case it No, it's
[46:51] services.
[46:53] Oh.
[46:55] Oh. Oh, that's why we don't have a
[46:57] models.
[46:59] Okay.
[47:02] Uh, so let me see if we can get a
[47:05] models.
[47:08] Models.ai.asure.com.
[47:10] I'm not sure if we can get that URL for
[47:14] let's see some we often do have multiple
[47:18] URLs available for our things. This
[47:21] one's services.
[47:24] Hm.
[47:27] Okay.
[47:29] Um,
[47:33] it assumes
[47:41] not services. All right. So, it might be
[47:43] that we can only
[47:46] maybe it's not going to work with the
[47:48] foundry models. Uh, I can try
[47:53] uh Yeah. Oh, yeah. That's good point.
[47:54] The URL on the foundry homepage. Thank
[47:56] you. I knew we I knew we had another
[47:58] URL. Thank you. Okay. Project endpoint.
[48:01] This one is Oh, and we have the Azure
[48:03] opening import. I don't Is that one
[48:05] going to work with Enthropic? I don't
[48:07] think so. Let's look at this endpoint to
[48:09] see what it is. Um
[48:13] no, that one is services. The one on the
[48:15] endpoint is this one. We can try the
[48:17] Azure OpenI endpoint. I believe that's
[48:21] only going to work. But here, let's
[48:23] let's at least just Okay, why don't we
[48:25] just deploy a OpenAI endpoint as well.
[48:29] Um, just at least to get that working.
[48:33] Uh, so let's see.
[48:35] Thank you everyone for debugging this
[48:37] with us. Uh, so GPT whatever. I don't
[48:41] care. We'll just do 40. Actually, that's
[48:43] a really old model. We shouldn't do 40.
[48:45] Remember, if you hear GBD40, you say
[48:48] GBD4. No. Okay.
[48:52] We could do V 5.2 codeex.
[48:55] Um, let's go expensive. This is my
[48:59] personal account for the record
[49:02] because I can only deploy Foundry uh
[49:04] Enthropic for my personal account. So,
[49:06] I'm not going to do the super expensive
[49:08] one uh because I'm actually paying for
[49:11] this one.
[49:13] Uh yeah, the the issue is I can't deploy
[49:16] Enthropic from my Microsoft account
[49:18] because Microsoft in particular is
[49:20] restricted. Um you should be a you
[49:23] should be able to deploy Enthropic from
[49:26] um your own accounts. It's just
[49:28] Microsoft in particular has a
[49:29] restriction because we are partners and
[49:31] like it's just like how revenue share
[49:33] whatever works. I don't know. Okay. So
[49:36] then now I've got GBD 5.2 codeex. So,
[49:40] I'm going to go back to my home and grab
[49:42] the OpenAI URL for it. And that would be
[49:47] um so let me just add in
[49:50] uh I guess we'll just change it to this
[49:53] one. And that should match. Let's look
[49:55] at the code again. So, openi.asure.com.
[49:59] Oh, then it uses the old version of it.
[50:02] Then it does URL/openi
[50:04] deployment. So, then I feel like it only
[50:06] wants
[50:08] this.
[50:09] So, we'll just give it we'll just give
[50:11] it this. Okay. I think feel like it only
[50:13] wants this. And then let's go and check
[50:16] out what that deployment was.
[50:19] Uh, so that's just GBD 5.2 codeex is the
[50:23] name of the deployment.
[50:26] And we just give it an ID.
[50:30] Okay.
[50:32] All right. Let's try again. And we're
[50:35] going to change the model
[50:37] to this. say hi.
[50:42] Okay. So, you said you have to be at a
[50:44] certain tier. So, our docs say that, but
[50:47] I don't think that my personal account
[50:49] is at a particular tier.
[50:52] All right. So, now we got a different
[50:54] error. So, we're making progress. Um,
[50:58] it says the requested operation is
[51:01] unsupported.
[51:05] I don't Okay. Um, this looks like a
[51:07] server error. Uh the requested operation
[51:09] is unsupported
[51:12] with GBD 5.2 codeex. Oh, let me look at
[51:15] here.
[51:17] Um the requested. So this we're getting
[51:20] a 400 error for this one.
[51:25] Um is 5.2 codecs not let's see is that
[51:29] one of the models that we would have if
[51:31] we were doing normal? I see 5.3 codecs.
[51:34] Did 5.2 codecs like not support? All
[51:36] right, let's just try sporting like
[51:38] deploying one more model.
[51:41] Um, all right, we'll just do 5.4
[51:45] because that I have used that in,
[51:48] you know, in VS Code proper. Uh, so that
[51:52] should support everything in agent
[51:53] needs.
[51:55] Oh, open AI compatible section. Okay.
[51:57] Yeah, we can try that, too. Um, all
[52:00] right. Let's just try. Okay, I've got
[52:02] 5.4 now. Let's try 5.4 four and then
[52:05] after that we'll try the other screen.
[52:09] Uh
[52:11] okay. And we're going to change this
[52:13] other models
[52:16] and
[52:20] other models.
[52:25] Oh, let me give it like mine. Okay. Just
[52:29] make sure it'll show up. Maybe the idea
[52:32] was the same. Okay, great. All right.
[52:35] And then we're gonna say, "Hi,
[52:38] uh, the API deployment for this resource
[52:41] does not exist." All right. Let me
[52:43] double check that the name of the
[52:45] deployment is the same. GVD 5.4
[52:49] details.
[52:51] GBD 5.4
[52:54] name.
[52:56] I think that the ID
[52:59] I guess the question is is the ID
[53:02] is the ID the deployment or the which
[53:06] one is the deployment name? I I feel
[53:08] like it would be this one. Um
[53:11] TV 5.5 worked.
[53:14] I can't tell like if it's trying to use
[53:17] this as the deployment ID or the other
[53:19] one is the appointment ID. Try again.
[53:22] Try again. Okay.
[53:24] Can I just do this employee
[53:29] other? I don't know. I I the problem is
[53:32] I'm kind of guessing at what these
[53:34] things are supposed to be. No, it
[53:36] doesn't like that I think because it's
[53:37] like overlapping.
[53:40] Okay. Hi. Hi again.
[53:45] Oh, now it's doing now it's doing auto
[53:49] other models. Hi.
[53:53] Okay. All right. Okay, that one didn't
[53:55] work. Um,
[53:57] all right. Now, you wanted, you said
[53:59] we're going to try the other. Okay,
[54:00] let's try manage language models. We're
[54:02] going to do openi compatible even though
[54:04] that's deprecated. Is that the one you
[54:06] wanted to do? Okay, open compatible.
[54:08] Deprecated. Great.
[54:10] And we'll give the API key uh over here.
[54:14] Uh, API key. All right. And we're going
[54:18] to give it the URL. So, OpenAI
[54:19] compatible.
[54:21] Um, we should be able to give it uh
[54:25] that. Um, I think it would want a
[54:29] responses URL.
[54:31] E1 responses ID open GPDI
[54:37] 5
[54:40] foundry and then the name. I'm going to
[54:43] assume that's the deployment name. It
[54:44] should be like passing the model.
[54:48] Okay, let's try that one.
[54:52] Other models
[54:54] open compatible. Hi.
[54:58] Let's see. Okay, that one. Okay, look at
[55:00] all the exciting errors we get. Um,
[55:04] so it said invalid supported values are.
[55:10] All right, this looks like a tool call
[55:12] error.
[55:14] What if we do openi
[55:17] um check the ID
[55:20] uh
[55:24] let's remove all the tools. Okay.
[55:34] All the tools. Okay.
[55:37] Hi.
[55:39] Nope. Um, let's let's just try
[55:44] the V1
[55:46] URL. I think it would be Nope. Hi.
[55:56] H. Let's go and use the
[56:01] endpoint on the front page as your
[56:03] opening eye endpoint. This just this
[56:05] one.
[56:07] Okay.
[56:09] and then say, "Hi,
[56:13] API deployment does not exist." I don't
[56:16] know.
[56:18] Yeah, I don't have AI toolkit installed.
[56:20] I mean, maybe I do. I think it's one of
[56:22] these. Uh, no, this is new. This is a
[56:25] new one, but I want to know how to do it
[56:28] this way.
[56:32] Um, because you shouldn't have to use
[56:33] like a whole extension. We should be
[56:35] able to do it with VS Code properly.
[56:37] proper proper
[56:42] um
[56:44] because why should we have to use a
[56:46] whole extension just do it because also
[56:48] this
[56:50] um I'm using two different accounts
[56:52] here.
[56:54] I I want to get this working with just
[56:56] this. I'm I'm talking with the
[56:58] documentation person right now. So,
[57:03] I'm going to figure out how to get this
[57:04] working and then I'll like post on
[57:07] LinkedIn or something when it's working.
[57:10] Um, because in theory we we should be
[57:13] able to do this, right? This this should
[57:16] work. So, that'll be my homework
[57:20] and because this was something I wanted
[57:21] to get working anyway so that I could
[57:23] try that Kimmy model.
[57:26] So, yeah. Um, if anyone does get it
[57:29] working via this chat language
[57:31] models.json, please
[57:34] share with me what your like URL was and
[57:37] deployment ID and name and stuff like
[57:39] what that mapped to. And I think we need
[57:43] better documentation
[57:46] um for how to do it for Azure.
[57:51] Yep. All right. Uh, we are over
[57:55] time now. Um, thank you everyone for
[57:58] joining today, for bringing all the
[58:01] great questions.
[58:02] I've got some homework. Maybe you do
[58:05] too. I shall see you next week. Yeah,
[58:10] we'll have it next week. And, uh, yeah,
[58:14] I'll and I'll upload the recording of
[58:18] this uh, later today.
[58:21] All right. Thank you everyone. Bye.
