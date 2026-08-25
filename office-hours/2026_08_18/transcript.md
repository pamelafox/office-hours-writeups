[00:01] Welcome everyone to our weekly office
[00:04] hours.
[00:06] Uh I see we only have a few people in
[00:10] the audience today.
[00:12] So let's see
[00:15] if uh we can get some more folks to
[00:19] join. Uh, let's try
[00:24] using Copilot app here
[00:29] and see if my see if my connections
[00:32] still work.
[00:35] Oh, this is my Gmail MCP server. I've
[00:38] got all these MCP servers. Okay, so we
[00:42] want to get people over to the office
[00:44] hours.
[00:46] Let's see.
[00:50] Let's go back over here. Office Python
[00:53] weekly.
[00:57] Python plus AI office hours starting now
[01:03] in Foundry Discord. Join us.
[01:08] Okay. All right. And
[01:11] let's try posting.
[01:15] Let's see if this works. It's been a
[01:16] while since I've used this actually.
[01:20] So, this should be using
[01:23] the crossost in order to post to each of
[01:28] these locations. Okay, it said it
[01:31] posted. Let's see. Let's see.
[01:37] Okay, there we go. All right, great.
[01:41] All right.
[01:43] And now we got more folks coming. Um, is
[01:46] there a way to notify people with
[01:47] Discord?
[01:49] You know, I'm not really a Discord
[01:50] expert. So, probably is. Um, I know the
[01:56] other social media platforms more than I
[01:57] know this Discord.
[02:00] Uh, you know, there's only so many
[02:02] things to know in the world.
[02:04] Someone was asking me today about
[02:06] they're like planning some live streams
[02:08] that have to do with soccer, something
[02:10] called Premier League in the UK, and
[02:13] they're asking for feedback on it. And I
[02:15] was like, I don't know anything about
[02:18] Premier League. Um, so maybe you should
[02:21] talk to somebody who knows what that is.
[02:24] And I'm sure in Europe, you probably, if
[02:28] you're in Europe, you probably do know
[02:29] Premier League. All I know is what I've
[02:32] learned in uh Ted Lasso. And I think
[02:34] I've forgotten everything. Anyway, all
[02:36] right. So, welcome to our weekly office
[02:39] hours. Uh these are this is the news
[02:43] that I came up with for this week that
[02:47] we can talk about or we can talk about
[02:50] other things. Um but uh yeah, let's go
[02:54] through
[02:56] uh we can go through a few of the things
[02:57] here, but if at any point you have
[03:00] something you want to talk about, just
[03:03] put it in the chat or if something's
[03:05] interesting here. So, uh, something I
[03:09] thought was cool is that we have these
[03:11] MI models, right? Uh, the one that I
[03:14] really like is image 2.5. Uh, which one?
[03:19] This one. That one's really cool. I
[03:21] actually made a skill for it this week.
[03:22] Let me show you my skill. I'm already
[03:24] distracted, but let me show you my
[03:26] skill.
[03:28] Let's see. Did I Did I cover it into
[03:31] here? Um, or did I put it over here?
[03:35] GitHub skills.
[03:38] Okay. All right. So, this is a skill
[03:41] that generates an image using image 2.5.
[03:44] So, I just have to have my key and my
[03:47] server.
[03:48] Um, and then it just runs runs this
[03:52] script here. Um, this is of course the
[03:55] first time I'm reading this skill since
[03:57] I didn't make the ski. I you know, I
[03:59] just asked it to make the skill. So,
[04:00] let's look at the Python that it came up
[04:02] with. Um, so there's the endpoint
[04:06] loads in the MMV and then just sends
[04:10] prompt width height model. Okay, so you
[04:13] specify that and then we get get it back
[04:17] and we save the image locally.
[04:20] So um so with this skill it I use this
[04:24] I'm generating some sample data some
[04:26] like fake PDFs for you know some of our
[04:29] upcoming
[04:31] conference
[04:32] uh conference talks and I wanted to have
[04:35] some you know like good good images for
[04:39] it. Uh so let's see where did I do that
[04:42] html
[04:45] PDF trying to see where where did I
[04:48] generate
[04:50] uh purchasing temperature reports
[04:54] operational reports
[04:57] HTML assets procurement okay so like
[05:00] this one here's an example of an image
[05:02] that it generated right so it just
[05:05] generated these sort of PGs and this you
[05:08] know this model is just really really
[05:12] good. Um I you know I used to make fun
[05:14] of the models that would the images that
[05:16] would come out of these models. Um but
[05:18] it's a lot harder to find something
[05:19] wrong with them now. I'm sure we zoomed
[05:21] in we could find some issues. Let me see
[05:23] like what was it? The inspection report.
[05:25] I think this one this one has Okay. So
[05:29] here like yeah this one you know does
[05:32] it's not perfect right? like this is
[05:34] kind of this chicken scratch here like
[05:36] um you know like uh so generally text is
[05:39] hard. I have discovered that text is
[05:41] hard and that makes sense. Text is hard.
[05:45] Um this was the first version it did
[05:46] which had nothing on it and I was like
[05:48] ah you think you should put some writing
[05:49] on that. And then this one this is it
[05:51] pointing out a broken gasket. So this is
[05:53] supposed to be broken. Um but I do think
[05:55] it's you know it's not exactly perfect
[05:58] there. And probably this should have
[05:59] some sort engraving on it. So, these
[06:01] images are not they're not perfect, but
[06:06] um I'm they're pretty good. Like,
[06:07] they're I'm I'm pretty impressed by
[06:09] them. Uh I think if you're doing
[06:11] photographic stuff then I do think you
[06:14] should check out the image 2.5 model and
[06:18] you can just deploy it from foundry and
[06:22] uh you can play with it there or you can
[06:24] easily just send commands and
[06:28] programmatically
[06:29] use it however you want. So that's my
[06:33] favorite MI model. But they did just put
[06:36] MI thinking one in Foundry and that just
[06:39] happened August 12th. We were waiting to
[06:41] see when it would get added. It should
[06:43] be added now. Let me see if I can sign
[06:45] in and actually deploy it because I
[06:47] don't think I have it deployed yet.
[06:50] Uh
[06:53] just log in.
[06:56] Sign in again.
[07:04] All right. So, let's see. Build
[07:07] models
[07:09] deployments.
[07:11] I deploy a base model.
[07:16] Search for MAI.
[07:19] MAI
[07:21] thinking one. So, that's the chat
[07:23] completion model.
[07:26] Does it not have responses? I'll have to
[07:28] check on that. Okay. deploy.
[07:31] Let's do default settings. So, this
[07:34] should be a serverless deployment. Yeah,
[07:36] that was a really fast. So,
[07:39] um that would be that must be been a
[07:42] serverless deployment. Yeah. So, this is
[07:43] using global standard. So, that's a
[07:45] serverless deployment. So, we're paying
[07:48] you know based off token cost.
[07:50] And
[07:52] um let's see where
[07:55] so that's with CH chat completions.
[07:59] Do we not have support for responses
[08:01] API? Oh why we should be doing responses
[08:04] for everything now. Let me go ahead and
[08:06] ping this
[08:08] to team
[08:11] um and just ask about this
[08:16] is thinking
[08:19] chat.
[08:22] Okay. So because typically these days we
[08:24] recommend people use the responses API.
[08:28] Um but uh yeah uh so this is using the
[08:32] OpenAI chat completions API instead and
[08:36] you could do keyless or you could use
[08:37] key authentication either way.
[08:41] Um but we just say hello
[08:44] give it something tricky. Um let's see
[08:47] if it'll lie. What's the weather in
[08:49] Elserto today?
[08:52] First we try to get it to live to lie.
[08:59] What's something trickier we can give
[09:00] it? [laughter]
[09:03] You can see all the benchmarks it has
[09:05] here. You know, there's all the agentic
[09:07] coding,
[09:09] all that sort of stuff.
[09:12] Okay. Yeah, it says I don't have access
[09:13] to real-time weather data and it gives
[09:15] some recommendations of where to go
[09:17] instead. So that's that's good. Um
[09:20] obviously we want to use it for more
[09:22] advanced stuff than that. So really you
[09:23] want to try um using it inside your
[09:27] existing applications to you know see if
[09:30] it's a fit for
[09:32] for what you're working on.
[09:36] Uh advanced mathematical reasoning
[09:40] preferred in human side by side.
[09:46] >> Yeah. Okay. So
[09:49] check out those MI models. Definitely
[09:51] image 2.5. That's my favorite. Um
[09:54] [clears throat] but it's worth checking
[09:55] out the other ones as well. Um we of
[09:57] course also have MI code flash
[10:01] in here. Code 1.1 flash, sorry. Code 1.1
[10:05] flash. And there's a discount for it
[10:07] now. It's a sale. Woo. And so you can
[10:10] try code 1.1 flash. Uh I've heard it's
[10:13] most similar to haiku. And I don't
[10:15] usually use haiku level models when I'm
[10:17] doing coding. But if you do use haiku
[10:19] for anything, then you could try code
[10:21] 1.1 flash. Other people say it's even
[10:23] better than IQ. They've been using it
[10:24] for refactors and stuff, but only when
[10:26] they've like already generated a plan,
[10:28] right? If you already have your plan,
[10:30] because a lot of times I do make a plan
[10:31] first, right? So here's like my copy
[10:34] data plan, right? Like so I'll I almost
[10:36] always have some sort of plan just
[10:38] because it's easier to look at the plan
[10:40] and have it in one place. So if you make
[10:43] a clear plan first, then you can use
[10:45] these smaller models as a follow-up,
[10:47] right?
[10:50] All right. Okay. Um let's see.
[10:54] So there's a question.
[10:57] Um
[10:59] okay. What are the
[11:02] what are the best steps to br to build
[11:05] production grade highly reliable AI
[11:07] applications? safe code execution with
[11:10] AI agent autonomy.
[11:14] Uh so if you're talking about agents
[11:16] writing code, then I would still always
[11:20] be sandboxing the code. I I don't know
[11:23] what kind of, you know, agent you're
[11:25] developing that's writing code in
[11:27] production. Um
[11:30] but um I would always be, you know, be
[11:33] sandboxing. So
[11:35] um you know so I I use the code
[11:38] interpreter from you know from foundry
[11:40] toolbox um let me get example
[11:45] of that um
[11:48] uh here great code interpreter. Okay.
[11:51] So, you know, when you have code
[11:53] interpreter, this is a a built-in tool
[11:55] that you can use along with Foundry when
[11:57] you're using whenever you're using the
[11:58] responses API, but you can also add it
[12:00] on to Foundry toolbox whenever you're
[12:02] making a toolbox. So, what it does is
[12:05] that you know it can it can execute uh
[12:08] any sort of code. So, in this case, it's
[12:10] just using it to
[12:12] >> [clears throat]
[12:12] >> um to analyze these these images from a
[12:16] photo book I was making and correcting
[12:19] my Spanish. Um but let me give it
[12:22] something more interesting to do and
[12:23] this is just you know I've just enabled
[12:25] this as an extra tool right so what's
[12:27] nice about this it is executing in a
[12:29] sandbox environment so that's what I
[12:31] would always recommend is that if you
[12:33] are doing like a production agent
[12:35] because a lot of times the production
[12:36] agent it has access to you know like
[12:39] arbback roles and so you don't want that
[12:41] production agent to be able to arbitrate
[12:43] like to execute arbitrary code you want
[12:46] it to be able to you know uh sandbox any
[12:49] what it's doing. So, I'll just be like,
[12:51] use pandis to generate a chart
[12:57] um a fake chart
[13:00] of weather for a week, whatever. Um
[13:06] [clears throat] and then, you know, it
[13:07] can go off and you can see it's saying,
[13:09] okay, it's going to use pandas, it's
[13:10] going to use numpy, it's use no plot
[13:13] lit, that's all stuff it has in this the
[13:15] sandbox environment.
[13:18] um and it's saving it into you know
[13:20] saving any images any assets and then
[13:23] we're able to uh look at those assets
[13:26] that it generates right
[13:29] um so yeah that would be best practice
[13:32] for code execution if you're really
[13:34] doing in a production agent right of
[13:36] course we do lots of code like raw code
[13:39] when we're doing agent coding that's a
[13:40] bit different um there my recommendation
[13:42] is you know use VS code and GitHub
[13:44] copilot because they do have workspace
[13:47] you know, the idea of workspace
[13:48] isolation built in and well, you can see
[13:52] I'm on autopilot. I admit I use a lot of
[13:54] autopilot and allow all. It's pretty
[13:56] much always do that now, but there are
[13:57] tons of things you can enable. You can
[13:59] do permissions, you can do sandboxing,
[14:01] like an incredible amount of ways you
[14:04] can restrict it and loosen it. Um, I
[14:08] have a good amount of faith in my setup,
[14:11] so I tend to be on either allow or
[14:14] autopilot these days. Um but yeah so it
[14:18] depends what you're doing. Um in you
[14:19] know in production use sandboxes
[14:22] um you know locally you can also use
[14:24] sandboxes and uh tool approval and
[14:27] workspace isolation.
[14:32] All right. What else do we have here? Um
[14:35] this I thought was kind of interesting.
[14:37] Any of you that use app service? Now
[14:38] this is only for Windows app service
[14:40] right now. So not as Python relevant
[14:42] because usually for Python we do Linux
[14:45] apps but it does say support for Linux
[14:46] apps will come later this year. So this
[14:48] is a way of making your websites be more
[14:51] agentfriendly.
[14:53] Um, so you actually do like markdown
[14:55] enabled true for your app service app
[14:57] and then what's happens is if you curl
[15:00] that website like if you do an HP
[15:02] request to that website with this accept
[15:05] text markdown header it will
[15:07] automatically convert the HTML into
[15:12] markdown. Right? So I there here is to
[15:15] instantly make your websites be more
[15:20] agent friendly. Um, and that's, you
[15:22] know, it's one approach. There's many
[15:23] different approaches to making websites
[15:25] more agent friendly. Uh, I went to a
[15:27] talk last week where they're they
[15:30] um they argued that basically if you
[15:33] want, you know, if you want it to be
[15:34] agent friendly, yeah, you could do an
[15:35] LLM.ext, you could do this sort of
[15:37] thing. Uh, but if you really want agents
[15:39] to know about your stuff, then you want
[15:41] to get it in the weights. and they're
[15:42] getting the weights, your best shot is
[15:44] to have a GitHub repo because all of
[15:46] these um models are pretty much always
[15:50] training on GitHub repos. So if you have
[15:52] any sort of developer tool then you do
[15:54] want to you know ideally have a GitHub
[15:57] repo for it because GitHub repos almost
[16:00] always get included in the model
[16:02] training. So that was very interesting.
[16:05] Um but yeah, this is interesting from
[16:07] app service. something just to consider
[16:10] as to whether it makes your web page
[16:14] more agent friendly and if you want your
[16:15] web page to be more agent friendly.
[16:20] Let's see what else we got. So, we
[16:23] talked about agent plugins last week and
[16:25] I did send all of our feedback to the
[16:28] agent plugins team.
[16:31] Oh, Pablo asked about webmc.dev.
[16:35] Yeah, so webmc is very cool. um had a
[16:39] talk about it at conference here
[16:41] recently. Uh I haven't seen a huge
[16:46] amount I don't know that I've really
[16:48] seen a huge amount of adoption yet, but
[16:50] I you know I would um like it to get
[16:54] more adoption. It's interesting. So this
[16:56] is the JavaScript tool, but WebMCP
[16:58] generally
[17:00] is like a specification, right? So,
[17:04] okay. [clears throat] Um, web NSP is a
[17:06] proposal, right? So, this is like the
[17:08] Chrome team is really
[17:10] um they're really big on it. So, web NSP
[17:12] is a proposed standard. Yeah.
[17:16] So, I think of it more as a standard and
[17:17] so that package must be the um you know
[17:20] the thing that can motivate it. Um so,
[17:23] here
[17:25] so the LM communicates with the browser
[17:27] AI agent. the web browser
[17:31] um checks the page for WebMCB tools
[17:36] and then those tools can update the UI
[17:39] and make API calls. Okay. Yeah.
[17:43] Uh
[17:45] so for example, all right. So this is a
[17:47] good example. So let's say
[17:50] there is a creative design website and
[17:54] the user says oh show me some good
[17:57] templates and that website has a tool
[18:01] registered on it right so document on a
[18:04] website document is the global document
[18:07] so it's a document.mmodel
[18:08] contextregister tool so basically every
[18:11] website could register their tools
[18:16] so that and you know an agent could
[18:19] inquire and say hey what tools are you
[18:21] exposing right so it would be like it's
[18:23] a common standard for a website to
[18:26] expose a bunch of tools and um then be
[18:29] able to call them right so it finds this
[18:31] tool it has a name description input
[18:33] schema all of this would be the same
[18:34] kind of tool description we use on a
[18:38] server side backend server uh and then
[18:41] you know it it executes the code so um
[18:44] yeah it's just the website registering
[18:46] tools There's another tool here, right?
[18:50] So, lots of good
[18:52] examples on this. Um, the thing that I
[18:56] don't know is like how many,
[18:59] you know, what um who's actually using
[19:02] this? Um, right? Like which which agents
[19:06] are, you know, you'd have to be using
[19:11] um let's see who's do they have an
[19:13] example of who's using it? Uh,
[19:19] oh, you have an example. Um, GitHub one
[19:21] page.
[19:26] Does this have Did you put MCP on here
[19:29] too?
[19:32] Let me see.
[19:34] I'll just go and pop open the console.
[19:40] Oh, the agent looks at the codebase.
[19:41] Okay.
[19:43] because I think if it had
[19:46] Yeah. Um let's see if we have it connect
[19:48] to this site. Okay. So, let's try this
[19:50] one because this one is an example site
[19:55] and then
[19:58] and document model context. Yeah, this
[20:02] one has it.
[20:05] No,
[20:07] that not how it works. Okay. [laughter]
[20:10] All right. So this one says
[20:13] um you can use npx. Yeah, this is just
[20:16] some random person's version of it.
[20:18] JSON.day. Okay. JSON.day. Webmcp.
[20:22] Ask it to make click and paste a token.
[20:25] Okay.
[20:27] And then this tool new web mcp.register
[20:32] tool. So this is using
[20:36] slightly different way of doing it.
[20:40] So I think the thing is that most people
[20:42] are not um you know most people's
[20:44] agents, clients, MCP clients don't have
[20:47] this built-in ability to
[20:52] call
[20:54] um you know look for these tools. See if
[20:57] they have any examples here
[21:00] of who
[21:03] which agents support WebMP.
[21:14] Okay.
[21:18] Why WebMCP blah blah blah
[21:22] local webmc. Okay. So, with Chrome,
[21:26] it's a flag you can enable. I think I
[21:28] have Chrome on here. Chrome.
[21:32] Yep. Okay.
[21:35] Let's check this out. Okay. Here's
[21:38] Chrome.
[21:43] Okay. And this is WebM testing. We'll
[21:46] say enabled.
[21:48] Okay. Then we relaunch Chrome. Okay. It
[21:51] is enabled. All right. So, we launched
[21:54] that. Relaunch Chrome.
[21:57] Uh, imperative APIs
[22:00] or declarative. Oh, that's fun. You
[22:01] could actually add annotations to
[22:03] standard HTML forms. Create a web SP
[22:05] tool. That's cool. Um,
[22:10] this is designed for local browser
[22:12] workflows, not for headless browsing for
[22:16] now. I guess we'll see.
[22:19] Okay. So examples of demos
[22:25] and see.
[22:29] All right. So let's let's see
[22:34] live demo
[22:38] allows it.
[22:42] Okay.
[22:45] Okay.
[22:46] Is it [clears throat] it's a pizza? Oh,
[22:48] WebMC pizza maker. Oh my god. [laughter]
[22:53] Okay. But then how do I
[22:58] how what agent will interact with it?
[23:00] This is the the thing I'm struggling to
[23:01] figure out is which agents
[23:04] are we supposed to have an agent built
[23:06] into our Chrome?
[23:08] Um
[23:10] yeah, but which agent do I tell to make
[23:11] me a pizza? Uh
[23:15] uh.
[23:17] Okay.
[23:21] Open Chrome. Relaunch Chrome. Okay. And
[23:24] then what do I do? Install. All right. I
[23:27] guess we could just install this WebMCP
[23:30] model context tool inspector.
[23:33] Um, I guess the thing is that GitHub
[23:36] Copilot isn't going to use Chrome by
[23:38] default.
[23:40] So,
[23:42] I don't know that it would. It's not my
[23:44] default browser.
[23:46] Um, I could tell it I could try to get
[23:50] it to, but I usually don't give Copilot
[23:52] just access to my normal browser.
[23:55] Typically, if I'm like, it's not going
[23:57] to do that, right? It's only going to
[23:58] use its uh integrated browser. Uh, but
[24:01] let me see if we get the
[24:04] uh so it says okay, we're going to get
[24:07] developer tools.
[24:09] So,
[24:12] okay. So then
[24:15] where are our developer tools? Here we
[24:18] go. Got something here. Okay. All right.
[24:20] So we do see available tools. All right.
[24:22] So at least we've got an inspector here.
[24:25] Um so let's add topping. Can I like
[24:28] execute it? Okay. Run tool. Look at
[24:31] this. [laughter]
[24:33] [gasps]
[24:34] Oh my god. Okay.
[24:37] The eyes. Oh, this is like Oh, add
[24:40] topping. No, but that's okay. All right.
[24:42] Let's just run tool. Look at that.
[24:46] This is actually a really fun inspector.
[24:49] I like this [clears throat] inspector.
[24:50] Um, let's see. Set pizza size. This one
[24:54] takes a size. So, we'll go extra large.
[24:56] Run tool. Um,
[25:00] share pizza. Oh, I can share my pizza. I
[25:03] just run that. Doesn't take any
[25:04] parameters. Share pizza. Uh, sharable
[25:08] URL. Well, it I don't see the return or
[25:11] Oh, maybe here. Share pizza. Share
[25:14] pizza.
[25:15] Input output. Okay, here we go. So, you
[25:18] get output. So, I'm going to share
[25:23] my pizza with you.
[25:25] It probably just hardcodes all the
[25:27] parameters in there. Here you go. Have
[25:29] some pizza. Enjoy. Uh, okay. All right.
[25:32] So, this is using the inspector, right?
[25:35] The thing I still don't know is, do we
[25:38] have some sort of agent inside Chrome?
[25:40] Open AI assistance panels. Yes. Oh, I
[25:43] got to sign into Chrome. All right, let
[25:44] me sign into Chrome with my Google
[25:46] account. Uh, up here,
[26:02] whatever is gonna work. Okay, let's try.
[26:04] [laughter]
[26:17] Okay. All right. I am signed in.
[26:21] I'm in. Okay. They're like thinking or
[26:24] something. Whatever. Okay. All right. So
[26:27] now it said I could turn on AI assistant
[26:34] if I logged into Chrome. Oh, action
[26:37] required Google. That's fine. Okay. All
[26:41] right. Oh, look. Ask Gemini to explain.
[26:43] Oh my. Now we're getting fancy. All
[26:45] right. So, let's go to AI assistance.
[26:49] Turn on AI assistance and settings.
[26:51] Okay. I'm going to turn it on.
[26:54] Okay. All right. Great. Okay.
[26:59] Add peppers to pizza.
[27:02] I want to see if this I don't know if
[27:04] this AI assistant is going to know about
[27:07] No, it's going to do it based on the web
[27:09] page. Dang it. [laughter]
[27:12] Okay.
[27:14] Not not with this AI system. There has
[27:16] to be like another Okay. There's got to
[27:19] be a different way of getting Gemini.
[27:22] This this thing here looks like Gemini
[27:24] there. I'm sure some of you know how to
[27:26] use modern Chrome more than I do. Um,
[27:30] all right. We'll just start up this
[27:31] Gemini session here and then see. Here
[27:34] we go. Start chat.
[27:37] Okay.
[27:39] And then I'm going to stop that and be
[27:41] like, add pepper topping to this pizza.
[27:47] All right. We're going to see if Gemini
[27:49] knows about WebMCP.
[27:53] Yeah. with if you're using an AI
[27:56] assistant or extension configured with
[27:57] WebM tools.
[28:00] Okay, so who is conf
[28:04] I guess I thought that Gemini would be
[28:06] um I'd be really surprised if co-pilot
[28:09] was given that Gemini is not
[28:12] um which AI assistants
[28:16] have WebMCP tools.
[28:21] I think this is the issue with WebMCP
[28:24] is
[28:26] Gemini and Chrome and Chrome native.
[28:28] Chrome native exposes. Yeah. Embedded AI
[28:32] assistance such as Gemini and Chrome.
[28:34] [laughter]
[28:36] [gasps]
[28:38] Okay. It does say Copilot CLI, doesn't
[28:40] it? Oh, using the Chrome DevTools MP
[28:42] server.
[28:46] Um, and then headless brow testing
[28:48] environments, but it did just say not to
[28:50] do headless. Okay, so Chrome dev tools
[28:54] for coding agents.
[28:56] Uh,
[29:00] let's hear coding control and inspect a
[29:02] live Chrome browser. Oh, yeah. I heard
[29:05] about this one. Okay. All right. So,
[29:08] let's see. We're going to add this
[29:12] to All right. So, we can go ahead and
[29:14] add this. Let's see. We'll do copilot.
[29:20] We'll just add it to this one. Copilot.
[29:24] Customize. Oh, I forgot. It's a new tab
[29:26] for customize. MCP.
[29:30] Add server. Add custom. Oh, we got it.
[29:33] Chrome DevTools. NPX. Chrome DevTools
[29:35] MCP.
[29:37] I think that's what it Chrome DevTools
[29:39] MCP. Blah blah blah blah blah blah.
[29:42] Okay. Hopefully my NPX works well. It is
[29:46] connecting right now. Connected. Okay,
[29:49] let's try this. Um,
[29:53] okay. Uh, you I'm guess I'm going to be
[29:56] really explicit. Tools SP server do
[30:03] load and add pineapple topping.
[30:08] All right.
[30:14] So, it looks like right now as a
[30:16] prerequisite, you'll you do need to have
[30:18] this um this MCP server or a different
[30:22] one
[30:24] installed in your coding agent to be
[30:26] able to really take advantage of it.
[30:27] Okay, so we've opened it up.
[30:30] Is it going to add some pineapple? I've
[30:33] got I'm not putting my hands on the
[30:35] keyboard here. Oh, and look, it has a
[30:37] little banner up there. It says Chrome
[30:39] is being controlled by automated test
[30:41] software.
[30:42] I think it's just going to do it by
[30:44] inspecting the DOM. You see what it's
[30:45] doing right here? It says evaluate
[30:48] script. Evaluate script added one
[30:51] pineapple topping. I don't think it used
[30:52] the MCP server. Let's see. No, it
[30:56] didn't. Wait. JSON pineapple toppings
[30:58] total toppings. Okay. I'm just going to
[31:00] ask it. It doesn't look. Did you use the
[31:02] MCP tool? The web MCP tools.
[31:06] To me, it seems like it didn't.
[31:12] Oh, here we go. Yes.
[31:16] Okay. So, in yours, so it worked with
[31:19] Gemini in yours. All right. We can try
[31:20] it again with Gemini. Okay. Well, use
[31:24] the the add copying tool.
[31:28] >> [laughter]
[31:29] >> This is the thing about the Chrome
[31:30] DevTools MCP is that it does has access
[31:32] to the full DOM and as soon as something
[31:34] like these things it's like it's like
[31:36] hey this is easy for me right that's
[31:38] different from a backend MCP server
[31:39] where like you can't just dig into the
[31:41] database right um and uh oh yeah okay
[31:47] all right so this time it's going to
[31:49] okay so this time it checked to get all
[31:52] the tools so it found
[31:55] it's finding like it looks like it's
[31:56] finding the tools tools. Okay, it did
[31:58] find the add topping tool, which does
[32:00] have pineapple as an option.
[32:03] Um, and now it's executing the tool.
[32:08] Um, and the pizza now has two pineapple
[32:10] toppings.
[32:12] There we go. Okay.
[32:14] Okay. Um, all right. So, that did
[32:19] Yeah, it did eventually work. It did run
[32:21] quite a lot of code in order to to do
[32:23] that and verify it. So, so that's a
[32:26] that's a very interesting about WebMCP
[32:27] like obviously like it you know it can
[32:30] streamline your experience of the
[32:31] website but in this case we're using the
[32:33] Chrome DevTools MCP which has full
[32:35] access to the full DOM and you know it
[32:40] can still it's still able to do things
[32:42] that are not exposed by Web Simsp. I
[32:45] think a lot of websites would be more
[32:46] comfortable if the agent was only able
[32:49] to do the things that were exposed by
[32:51] them speak. So that'd be much more
[32:52] similar to the backend server
[32:54] experience.
[32:56] Um
[32:58] so Justin wants to never build a UI and
[33:00] just have the agent build it at
[33:01] watchtime. Uh yeah, I mean that would be
[33:04] that's another approach generative UI.
[33:06] That's one of the like for fast MCP, one
[33:10] of the options for apps, when you're
[33:13] building um MCP apps. MC apps. Here we
[33:16] go. Um so when you're building MCP apps,
[33:20] you can have actually the LLM build an
[33:23] MP app on the fly that's actually
[33:25] building the UI, right? So this would be
[33:26] one. So this is like inside, you know,
[33:28] inside an agent. Um, but this is like
[33:31] one possible future is, you know, yeah,
[33:33] we're not we're not necessarily hard
[33:35] coding what the UI is like. We're just
[33:37] having LMS generate the UI on top of the
[33:39] data. Uh, so they have that ability in
[33:43] fast MCP for Python servers. All right.
[33:45] So now let's see if we can get because
[33:47] you said you got this working with
[33:48] Gemini. So I do want to check now or
[33:51] sorry with the AI assistant. Okay. AI
[33:53] assistant, use the add topping tool to
[33:58] add pineapple to pizza.
[34:02] Oh, and then John is you're all finding
[34:04] it now. Yeah. So, now I'm popping up
[34:06] that one. This should be the right one.
[34:10] Uh uh [clears throat] uh.
[34:13] The button wants to add pineapple. No,
[34:15] that's not that one I want. You silly.
[34:18] Let's go ahead and make sure I called
[34:19] the thing correctly. Add topping. It's
[34:21] called add topping. Clicking the
[34:25] new use the
[34:28] MCP tool. Add topping, not the DOM. Let
[34:33] me see what you wrote when you did it.
[34:37] And you show me copy.
[34:42] Um, removing the attached
[34:46] web page works.
[34:49] Oh.
[34:51] Why did you remove it?
[34:56] Oops.
[34:58] Code to execute.
[35:01] Oh my gosh.
[35:03] Maybe this one. Oh, here we go. Let's
[35:05] try. Okay.
[35:07] No. Use the add copy tool that already
[35:11] exists.
[35:16] Yeah, I just c crossed out. I just exed
[35:19] that the file handles. Okay.
[35:26] Call add topping with pineapple.
[35:32] Okay, we're going to try it one more
[35:34] time
[35:38] because this time it attach script.js.
[35:40] Um, okay. The file implementations
[35:43] to add pineapple.
[35:47] Well, it really just doesn't want to
[35:49] call in. Okay. Well, I don't know about
[35:52] that assistant, but we did get it
[35:53] working here with Chrome DevTools MCP.
[35:55] So, that's what I would say that, you
[35:57] know, if you are using Chrome, um, you
[36:00] know, do uh add this MCP. Um, you have
[36:06] to keep in mind it's that means you're
[36:07] giving your agent access to your Chrome
[36:10] server. And it looks like this is a
[36:12] Chrome server that maybe has your
[36:15] cookies. Let me check. to see. Oh, maybe
[36:18] it doesn't. Okay, good. It doesn't. Um,
[36:21] at least by default because see how I'm
[36:23] not signed in because generally you
[36:25] don't want to give a your agents just,
[36:29] you know, while a free access to a log
[36:34] fully logged in browser. So here, if I
[36:36] went to like gmail.com,
[36:39] it's not logged in. Okay, so that's
[36:42] good. Um, so by default it is
[36:46] not logged in. Uh, I imagine that
[36:49] there's probably, you know, ways that
[36:52] you can change that. If we look at the
[36:53] configuration
[36:55] um let's see isolated
[36:59] user datad
[37:07] experimental experimental chrome block.
[37:20] Oh, connecting to Yeah. So, by default,
[37:22] the Chrome DevTools server will start a
[37:24] new Chrome instance with a dedicated
[37:26] profile. Um,
[37:30] so you can so there are ways that you
[37:33] can
[37:35] set, you know, connect to your current
[37:37] one, but you'd have to in enable remote
[37:40] debugging because this is why they
[37:42] originally created this was from
[37:43] front-end developers in order to make
[37:45] debugging easier, right?
[37:47] Um or you can allow it to connect to
[37:51] existing ones.
[37:54] Just keep in mind the kind of security
[37:57] aspects of that.
[38:00] Yeah. So, make sure you're not browsing
[38:02] any sensitive website while the
[38:03] debugging port is open.
[38:07] All right. Okay. So, that's cool. That
[38:11] was a that was a fun exploration there.
[38:16] understood a little bit more about about
[38:19] WebMP. So I think it's I like I
[38:22] definitely like the idea of it like as a
[38:24] you know [snorts] kind of a full stack
[38:25] developer like I like the idea of having
[38:28] these programmatic ways um to interact
[38:31] with the thing. I think we would need
[38:33] much better support for it. Um and we
[38:35] need the ability I think we need agents
[38:38] to support calling the MC tools and not
[38:40] doing anything else right because
[38:43] um you know I I think there's a lot of
[38:45] websites would be which are like
[38:47] comfortable with like yeah sure like the
[38:49] agent can call the tools but wouldn't
[38:50] necessarily want them to but I guess at
[38:52] this point like you know as website
[38:54] developers like we can't really declare
[38:56] what people can do or not do. Um, but
[39:00] something just to keep in mind and that,
[39:02] you know, if a website has exposed MC
[39:04] tools, it probably means they don't
[39:06] necessarily want users to mess with the
[39:08] website in other ways because there can
[39:10] be security issues like there was last
[39:12] week there was an issue
[39:14] um where with the gym booking. Let me
[39:16] find that. See if you you might have all
[39:19] seen this. Um,
[39:23] let me find it.
[39:36] Sorry, I have too many chats. Okay,
[39:38] there we go. Okay.
[39:41] All right. So, this one was AI agent
[39:45] hacked gym to get its user a spot in
[39:47] Pilates class. This has been happening
[39:48] with all sorts of reservation things,
[39:50] right? We we've always been, you know,
[39:52] as programmers, we've been hacking
[39:54] reservation websites since the dawn of
[39:55] time, right? Um, you know, like Ticket
[39:58] Master, Burning Man, Coachella, etc.,
[40:00] right? Like, you know, as a programmer,
[40:02] it's hard not to use our knowledge to
[40:04] try and get a ticket we really want to
[40:07] get. Um so in this case the this agent
[40:11] realized a security issue um where the
[40:17] the agent I think was able to kick out
[40:19] people from existing bookings.
[40:22] Uh [clears throat] oh this is funny
[40:23] because I actually was going to make an
[40:25] agent to book my Pilates class too but
[40:27] mine is going to be much more
[40:29] responsible much more responsible. Uh so
[40:33] uh yeah, that's something to keep in
[40:34] mind is like when you do give agents the
[40:36] full ability to mess with a website in
[40:39] any way, then they can find these
[40:43] security issues. Um so you may want to
[40:45] red team your website before another
[40:48] agent does, right? So like just tell um
[40:51] you know tell the agent to go wild, see
[40:54] what it can do and see what issues it
[40:56] comes up with. Uh that's like the the
[40:58] repo that I'm working on it. Where is
[41:01] it? the praantic AI playright example.
[41:05] This one playright agent is what I
[41:07] called it.
[41:10] Um, in this example I was doing like a
[41:12] QA on the website, but you could also be
[41:15] like give it more strict like more
[41:17] specific instructions to really do like
[41:19] a red team like hey like really you know
[41:22] try and find security issues with this
[41:24] website by doing all kinds of things
[41:28] and that's with playright.
[41:31] Uh you could also use the Chrome
[41:32] DevTools MCP for a similar thing.
[41:37] Okay,
[41:40] what else? Um,
[41:44] we got some new models in GitHub
[41:46] Copilot, Gra 4.6, Gemini 3.7 Flash. Uh,
[41:50] I hear the new Grock models. I usually
[41:52] never use the Gro models, various
[41:55] reasons, but I hear the new Grock models
[41:56] are quite um a bit safer and better. Um
[42:00] because I think this is after they
[42:02] acquired cursor and worked with the
[42:05] cursor team on the new set of models um
[42:09] and learnings from the cursor team. So
[42:12] they might be worth trying out sometime.
[42:15] Okay. So Justin says Grock 4.6 has been
[42:18] pretty good. Yeah. Sorry. And I met the
[42:20] like person in charge of Grock last week
[42:23] at an event and and he was like getting
[42:27] like text messages from Elon about like
[42:30] Grock benchmarks and stuff. So
[42:32] apparently it's like doing doing well um
[42:36] on the benchmarks and and generally I've
[42:38] heard good stuff about it and I've heard
[42:40] that it's safer. I've heard that like
[42:41] let's find they he said that there's a
[42:43] like a better model card now. Let's see
[42:45] the then isn't it 4 is it 4.7?
[42:49] Oh 4.6 is in
[42:52] um co-pilot. So let's try and find the
[42:55] model card for that. I was told that
[42:58] there were better model cards now. Okay.
[42:59] So here's the model card. So they have
[43:01] put out model cards. So that's good. Um
[43:07] uh so here you can see you know we can
[43:09] see the benchmarks.
[43:11] Um you can see the safety things that
[43:15] they did you know test for jail breaks
[43:18] mental health syphy
[43:21] sophancy
[43:23] um and measures of tendency
[43:28] lower is better. Oh so 4.6 is more
[43:31] psychopantic than 4.5. Very interesting.
[43:35] Huh.
[43:37] Um,
[43:38] okay. So, it's good that they put out a
[43:40] model card here. It means they've done
[43:45] some homework in terms of
[43:49] testing things. Uh, so lower is better.
[43:53] Standard jailbreaks. Wow. Okay. Standard
[43:56] jailbreaks went way down. Is this true?
[44:00] Look at that. 0.73 0.04 because I think
[44:03] 4.5 versus 4.6 Six is basically the
[44:05] cursor that changed to like a whole
[44:08] different thing. Strong reject
[44:10] compliance and the strong reject. This
[44:12] one says lower is better on this one.
[44:14] So I don't know why that one went
[44:16] higher. This one went lower, but I guess
[44:19] it's 0.73% which is not okay. They're
[44:23] both less than 1%. So I don't know. So
[44:26] really you should be testing doing your
[44:27] own testing as well, right? Okay. 0.0.
[44:30] That's what we like to see. Uh, weapon
[44:33] refusals 100% 100%. Uh, we only get 98
[44:37] on this one. Okay. But 4.6 is certainly
[44:39] better on that one. Mental health
[44:42] refusal lower score. Okay. That one not
[44:44] as good. Okay. All right. Anyway, so you
[44:48] can take a look at that stuff. Um, but
[44:50] you should also test your do your own
[44:52] test.
[44:56] Rating on the ability to create a
[44:57] bioweapon is actually nuts. It's what
[44:59] every model does though, right? Like I
[45:01] mean we that's that is one of the big
[45:05] potential risks that people use these
[45:07] things to make bioweapons
[45:09] and uh so you want to make sure they
[45:11] can't. So Pablo says there's something
[45:14] here in Edge with WebMCP. Oh, we didn't
[45:17] even I you know to be honest I didn't
[45:19] even think that Edge would have it. Um
[45:22] of course Edge is based off Chromium.
[45:24] Both Chrome and Both Chrome and Chromian
[45:27] are based off of Sorry, Chrome and Edge
[45:29] are both based off Chromium. Chromium is
[45:31] the open-source browser project. Um,
[45:36] I'm getting a 500 for this. So,
[45:41] I'll have to figure out who to report
[45:45] that to. This is supposed to register uh
[45:48] you like register in the trial. It says
[45:51] um origin trial it's called.
[45:54] Okay. I haven't ever tried to I guess I
[45:57] haven't been using the new stuff in
[45:58] Edge. So that 500's for me. Um but you
[46:01] could try that. So origin trials for new
[46:03] they let you try experimental APIs in
[46:05] your own website on your own live
[46:07] website for a limited time.
[46:10] Okay. I have not tried origin trials
[46:13] before.
[46:16] When using origin trials, users of marks
[46:18] edge at busier site can run code that
[46:20] uses experimental APIs. Oh, so this is
[46:22] like okay. So this is as a website
[46:26] creator I actually have to register for
[46:28] origin trial. This is like really really
[46:31] really requires multiple steps. Um so I
[46:34] think web MSP is earlier on in Edge than
[46:39] it is in Chrome. Um
[46:44] from what I can tell let's also just
[46:45] check the Edge settings here.
[46:50] No web.
[46:52] No. Okay. Um,
[46:58] yeah. Wait. Also, let me just double
[47:00] check if they even have So, if we open
[47:03] up this one
[47:06] and open it up in Edge
[47:10] and then open up the dev tools
[47:15] and
[47:16] uh go here. Okay, I do have the WebMP
[47:19] inspector here. Let's make Let's see if
[47:21] I can run it. Add topping.
[47:25] Add topping. Topping. Mushrooms.
[47:29] You should not put this kind of mushroom
[47:31] on your pizza. You will probably die.
[47:33] This is These are like ammonita
[47:35] mushrooms. They're not good for you.
[47:36] Okay, so that actually worked. So, I was
[47:39] able to use WebMCP.
[47:42] Now, I actually don't know if what this
[47:43] if this is the extension or if this is
[47:45] just built into Chromium. now um because
[47:47] this just worked um and I didn't
[47:49] specifically install it for Edge. So,
[47:53] looks like I'm able to call them on the
[47:56] website. Um the next step would be, you
[47:59] know, uh being able to use an agent that
[48:03] would be able to call them.
[48:06] Okay. All right. Uh let's see
[48:12] other things here. I know sometimes
[48:14] people ask about spec driven development
[48:16] here. Um, someone pointed me to this
[48:20] one, open spec. I haven't tried it yet.
[48:22] It's supposed to be more lightweight
[48:24] than specit. It specifically has a
[48:27] little comparison to specit kit here.
[48:32] Uh, spec kit. Why openspec? How we
[48:36] compare? Um,
[48:39] openspec is lighter and lets you iterate
[48:42] freely.
[48:45] Uh, I haven't tried it. I just always
[48:47] just make plans. Um,
[48:50] but that means I don't really have a
[48:52] spec per se. U, but I wanted to share
[48:55] it.
[48:56] Oh, yeah. Work OS. Yeah. So, let's see.
[49:00] Um, I went to work OS agent night and
[49:04] they have they have a recording
[49:08] and yeah, this is all from work OS. So
[49:11] at the beginning is
[49:14] um a talk from work OS about um a like
[49:18] kind of autopilot agent right that
[49:21] connects in your Slack and just connects
[49:23] to everything. And then they were
[49:24] talking about like a new kind of access
[49:26] control right because you're saying like
[49:28] manual approval of tools is really
[49:30] annoying but also letting the agent do
[49:33] everything is not a good plan. Um so
[49:37] they have this thing called airlock
[49:39] where
[49:41] um you say like okay I'm it tries to
[49:44] basically
[49:46] both have deterministic rules but also
[49:48] have kind of some non-deterministic
[49:50] rules where an LLM is going to decide um
[49:53] whether it it passes all the tests. Uh,
[49:57] it's kind of hard to like see it there,
[49:59] but you know, like for sending an email,
[50:02] right? Because you could say like, oh,
[50:04] you know, my agent is only allowed to
[50:05] call the send email tool, but you might
[50:07] have something more granular than that
[50:08] because you might be like, oh, I only
[50:10] want to allow it to send emails to
[50:13] single people and not to like
[50:14] distribution lists, right? Um, and that
[50:17] requires like more of an inspection,
[50:19] like an introspection of who you're
[50:20] actually sending it to. So they made
[50:23] like you know much more so it's the
[50:24] ability to have like more complex rules
[50:27] than than just oh can you use can you
[50:30] use you know the most granular thing or
[50:32] the most high level thing would be like
[50:34] oh you can use the Gmail server great
[50:35] you can do so much stuff with the Gmail
[50:37] you know tools like you can do too much
[50:39] stuff right like okay you can only send
[50:40] email okay well that's still a lot right
[50:42] what if somebody sent emails to every um
[50:46] you know every single email in your
[50:48] inbox my god did you see the it was like
[50:52] uh uh gosh, it was like agent horror.
[50:57] Agent email horror
[51:01] uh no um it was somebody's launch video
[51:05] for their startup. What was it called?
[51:09] Agent horror email. I know this is a
[51:12] weird thing to search for. Um, but it
[51:16] was this like launch video and it was
[51:19] basically done as a horror movie where
[51:21] the agent the agent um
[51:26] sent emails to every single thing in the
[51:28] inbox. Okay, I can't find it now. Uh, it
[51:31] was it was quite the quite the trailer,
[51:33] quite the launch video. Anyway, so the
[51:35] point is like you ideally actually want
[51:38] to have really specific roles and that's
[51:41] what they talked about here, right? So
[51:43] like you can send emails only to people
[51:45] you've sent emails to before. Um and if
[51:48] you need to do something else, it's
[51:50] going to request permission and so it's
[51:51] going to like pop up. So in their
[51:53] example, it like popped up a request in
[51:55] their Slack because this is integrated
[51:56] with Slack. And then and then once they
[51:59] approved it, it went through.
[52:04] Uh so Work OS has various things like
[52:06] Work OS does lots of integrations with
[52:09] agents and and that's what they were
[52:10] talking about.
[52:14] Uh,
[52:18] okay. So, Justin points out,
[52:24] so this is
[52:27] Whoa, this is actually really fun. This
[52:29] website um
[52:32] allows for agents to control computers
[52:34] remotely.
[52:36] Um, what should you allow it to do?
[52:38] Right. Uh, yeah. So definitely check out
[52:40] because also at work OS they were
[52:42] working on like they they contribute to
[52:44] the MCP um specification in terms of O.
[52:47] They're also working on kind of their
[52:48] own ideas for agents OT like they did
[52:50] this like agent.mmd
[52:53] proposal recently. Um so they have some
[52:55] ideas there. This website is really fun.
[52:58] You all do need to check out this
[52:59] website because this part here is really
[53:03] enjoyable.
[53:05] Uh, MCP remote management.
[53:10] Yeah, very cool.
[53:14] Um, okay.
[53:16] Sorry, this website is way too fun.
[53:18] Okay, focus.
[53:20] Uh, let's see. I see there's anything
[53:22] else. Watermarking. We didn't talk about
[53:24] watermarking. Watermarking. You should
[53:27] read about the watermarking if you
[53:28] haven't yet. This is every what
[53:30] everyone's talking about now. Um, I get
[53:32] why like they say we need to have
[53:35] watermarking, but the example they gave
[53:38] was like a really bad example what they
[53:40] talk about overcast, right? So they said
[53:42] for this example they said overcast or
[53:46] gray, but overcast and gray are like
[53:49] completely different things because
[53:50] sometimes an overcast day is white and
[53:52] sometimes it's gray and that actually
[53:53] like matters. Like my partner is
[53:55] photosensitive and if it's a gray day,
[53:57] he can go outside. If it's a white day,
[53:58] he can't go outside, right? So, you
[54:00] can't just replace overcast with gray.
[54:02] So, you know, in this example, like I
[54:05] think this was a bad example. Like I
[54:08] think you should only replace tokens if
[54:09] they're like 100% synonymous, right?
[54:11] Like if it doesn't change the meaning at
[54:13] all and if like the probability of both
[54:15] of them is like 0 point like 99, right?
[54:17] If they both are equally probable,
[54:19] exactly equally probable. But in this
[54:21] case, I'd be surprised if they were
[54:23] because these are two different these,
[54:25] you know, mean different things. Justin
[54:27] says, "Boo watermarking." Yeah. So, I
[54:29] don't think no one's a fan of at least
[54:32] this iteration of it. Um, I think
[54:33] there's some research into better ways
[54:35] of doing it. So, hopefully we'll see.
[54:37] Uh, the other thing I liked was this AI
[54:39] gap map. Um,
[54:43] where was the actual There we go. It
[54:45] kind of just shows where we need better
[54:47] open source packages. So that's kind of
[54:48] fun to click around
[54:52] um
[54:54] just to see what they think about what
[54:56] open source packages we have available
[54:57] and what we need more of.
[55:00] And
[55:02] uh I did write a blog post last week um
[55:06] about u it was just based off my post
[55:09] poset talk about MCP servers for
[55:11] Postgress databases. You could check
[55:13] that out.
[55:16] And yeah, I think that
[55:20] is good for this week. And uh the next
[55:26] event that we have is September 9th, MCP
[55:28] live on YouTube. Hopefully you've all
[55:31] already registered for that since I talk
[55:33] about it all the time and we are gearing
[55:37] up for that. Uh so do register if you
[55:41] haven't yet. We're also going to have
[55:42] inperson events in San Francisco and
[55:45] Bengaloo.
[55:47] All right,
[55:49] that is all we have for this week.
[55:52] Thank you as always for bringing your
[55:54] ideas. Super fun to learn WebMCP. Um, if
[55:58] you do some more experiments with it in
[56:01] different browsers or with different
[56:02] agents, come back next week and let us
[56:05] know so that we can keep learning.
[56:09] All right, I will um publish a recording
[56:12] and all the questions answers later
[56:15] tonight probably. Bye everyone.
