[00:00] Okay. All right. So, now we are
[00:03] recording for today's office hours. Um,
[00:06] so for context, since I just raided
[00:08] Sarah's office hours, thank you, Sarah.
[00:11] Um, we just had a live stream in this
[00:15] Python plus agents live stream series,
[00:17] you can see all the resources here. Um,
[00:22] so if you are interested in that, you
[00:24] can uh catch up with uh you know with
[00:27] the with the series and and join us in
[00:29] it. It's uh it's actually a lot of fun
[00:31] learning lots as I give it and uh and
[00:34] yeah so this office hours is for
[00:38] uh follow-up questions after today's
[00:40] session which was about adding context
[00:42] and memory to agents where we covered
[00:46] quite a lot probably too much
[00:50] so I I imagine there's some follow-up
[00:52] questions
[00:54] okay so I see the first question was how
[00:57] to configure the GitHub workspace to
[00:58] call paid authenticated LMS to avoid the
[01:01] issues. Yeah. So that's all um we did
[01:04] put in the if you look at the
[01:09] repo
[01:10] in the readme um
[01:14] we have instructions on deploying you
[01:18] know configuring it right so configuring
[01:19] the model providers um generally you if
[01:22] you're not using GitHub models and
[01:24] you're not in a code space then you need
[01:25] to do the deenb so there's instructions
[01:27] for how to do github models locally and
[01:29] setting up the token there's
[01:31] instructions for foundry models and
[01:34] we've also got the bicep in here so you
[01:36] can actually you know provision them and
[01:39] in that case I actually if you do that
[01:41] route I actually write the MV for you um
[01:44] using a script um but if you want to
[01:47] just manually configure it if you've
[01:49] already got a a deployment that uh that
[01:52] works then you're just going to have a
[01:55] so if you look atsample
[01:57] right you can see you need to set up
[01:58] your endpoint and your chat deployment
[02:00] and they need to be set up with keyless
[02:01] keyless authentication because we are
[02:03] using keyless we're not passing in an I
[02:05] key. If you want to pass in a key, you
[02:06] have to change the code itself. Uh,
[02:09] which you can certainly do that. Um, but
[02:10] by default, we avoid keys because keys
[02:13] uh are bad like with OpenAI. Um, so you
[02:16] can see mine here, right? I've got this
[02:18] deployed here. And uh let's see, we
[02:21] don't need that anymore. Um, you know,
[02:24] and and it's got the the right
[02:25] variables. If you if you run the ACD up
[02:29] that I suggest in the readme, then it
[02:31] will write this file for you.
[02:35] I guess we do need that version now.
[02:36] Okay. All right. So, it'll write it'll
[02:38] write the value for you. Uh write the
[02:40] for you. So, you can run a up. It'll do
[02:42] it all for you. Or if you already have a
[02:46] um as your uh model set up, then you
[02:49] know just manually make your MV file.
[02:54] All right. Um,
[02:56] yes, you can do something similar if you
[02:58] want to do OpenAI or O Lama.
[03:01] Yeah, right. Or TFM.
[03:04] Um, okay.
[03:07] Uh, good questions.
[03:10] Uh, what other questions uh do you have
[03:14] following up from the session? I know
[03:15] there were quite a few in the in the
[03:18] chat uh that we didn't get to. Um so
[03:22] just as a reminder of you know what we
[03:25] showed is we had the chat history.
[03:29] Um we had the dynamic memory with me
[03:33] zero. We had uh knowledge as a context
[03:37] provider using Postgress and AI search
[03:41] and then we had context management with
[03:43] summarization and sub aents.
[03:57] All right, I'll just wait to see because
[03:59] I see lots of people are typing
[04:05] and see what questions folks have.
[04:09] Okay.
[04:11] Oh, great question from Rose. Will this
[04:13] series cover hosting agents in Azure
[04:16] such as options and best practices?
[04:19] Um, so our original thought was to
[04:21] actually do a follow-up series
[04:23] specifically about hosting agents on
[04:26] Azure and um and uh really like
[04:31] separating that from this series um
[04:33] because we wanted to to emphasize code
[04:36] that people could you know mostly run
[04:38] locally like almost all the examples
[04:40] today you could run with with GitHub
[04:41] models for free. Um so we thought we
[04:44] would do a a separate series about
[04:46] deployment but we are and we are getting
[04:47] a lot of questions about deployment. Um
[04:50] so uh we're I I think there's definitely
[04:53] definitely desire for it. Um for now
[04:55] what I would direct you to I will I will
[04:58] show one deployed example in the
[04:59] workflow um week next week on Monday. Uh
[05:03] I am going to show one deployment
[05:04] example which is on container apps. Uh
[05:07] but really there's a lot more that you
[05:10] know we could talk about because there's
[05:11] many deployment options right there's
[05:13] container apps there's Azure functions
[05:15] there container app jobs um there's um
[05:19] you know actually like using foundry uh
[05:22] foundry hosted agents uh there's
[05:24] something called hosted agents there's
[05:25] like there's quite a lot of options now
[05:27] but for now what I'm going to point to
[05:29] is there is the official documentation
[05:33] does talk about hosting options here and
[05:36] this actually doesn't mention container
[05:38] apps at all, which is the one I'm going
[05:40] to going to show. Um, but it probably
[05:43] doesn't mention it because a container
[05:44] app is just a Docker container, right?
[05:46] So, these are all Python scripts, right?
[05:48] So, if you've got a Python script, you
[05:49] can set up a Docker container to run a
[05:51] Python script. So you don't necessarily
[05:52] have to do anything special, but there
[05:54] are maybe some thoughts about oh should
[05:56] you use a job because you're um you know
[05:59] because you're going to be having a
[06:01] longunning workflow or are you going to
[06:04] use a normal container app for like a
[06:06] userfacing application? Um uh so yeah
[06:10] and actually I just asked the container
[06:13] apps PM uh because somebody in the
[06:16] Spanish session yesterday asked about um
[06:19] deploying an agent using the playright
[06:22] MCP and so the AC the container apps PM
[06:25] actually wrote a docker file for me. So
[06:28] the thing if you're using container apps
[06:30] it's just a question of can you write
[06:32] can you write the docker file right? So
[06:34] this one is a docker file that sets up
[06:36] Python and also installs installs npm
[06:38] and installs a playright right. So when
[06:40] it comes to container apps it's really
[06:41] about um you know how how you set up
[06:45] your docker file and that's something
[06:47] that you know it's is somewhat um
[06:52] standard across clouds. Uh but yeah, so
[06:55] I think we do want to do like a
[06:56] follow-up
[06:58] a follow-up series about deployment, but
[07:00] I will try to touch on it briefly
[07:04] because we are getting asked a lot about
[07:05] it.
[07:09] Um all right, let's see. Okay. Um so
[07:13] there was a qu uh so we say Espon says
[07:16] there was a question about how to have
[07:18] multi-tier
[07:21] um memory
[07:23] choices to store lots of stuff if more
[07:25] details are needed but keeping the local
[07:27] storage manageable. Is it helpful to
[07:30] toss the details when it summarizing or
[07:32] useful to keep them as part of a re
[07:34] summary with the full
[07:37] original context?
[07:40] Okay. I'm trying to track what we're
[07:41] like when we're saying here like um are
[07:44] talking about like combining the user
[07:46] memories with the conversation memory.
[07:50] Uh I think that would normally be done
[07:51] separately, right? Typically user
[07:53] memories you're going to stuff into the
[07:55] um system prompt. Um whereas like the
[07:58] conversation history is going to be like
[07:59] a message in the in the thread. Um but I
[08:03] think you might be talking about more
[08:05] stuff as well. And it's also worth
[08:07] pointing out that like mem zero we use
[08:08] the mem zero basic option. If you look
[08:11] at the documentation for um mem you'll
[08:15] find that uh they have
[08:18] uh you know more options than that. They
[08:21] have something called graph memory as
[08:23] well. And this is kind of remembering
[08:24] like entities, relationships, that sort
[08:26] of thing. Um so you know we use the most
[08:29] basic you know their basic one which is
[08:32] still quite um quite good but they do
[08:34] have some other options as well.
[08:38] Um, so I'm not sure exactly what kind of
[08:40] details we're talking about there, but
[08:42] um it sounds like it's a good question
[08:43] and uh you
[08:47] a good question like a good thing to do
[08:49] is look at existing memory systems and
[08:51] see how they're implemented like with
[08:52] you know with copilot memory you can
[08:54] actually inspect and see what memories
[08:56] are getting sent and and see how they're
[08:58] doing summarization.
[09:01] Um Patrick says, "What would you suggest
[09:04] about how to learn all of this?"
[09:08] Yeah. So, good question. So, first I'd
[09:09] make sure like that you're like running
[09:11] through all these examples and
[09:13] understanding them and if you have any
[09:14] questions you know you can al you you
[09:16] can always ask like co-pilot to you know
[09:18] explain something and it usually does a
[09:20] pretty good job um you know digging
[09:22] through the code and explaining
[09:23] something because if you're using
[09:24] copilot and VS code like it can actually
[09:27] um you know in look at the um agent
[09:30] framework stuff right like here I was
[09:32] trying to understand um Reddus like does
[09:34] reddis have a max size of values and
[09:36] then I asked like oh why does agent
[09:38] framework have this and it dug into
[09:39] agent framework code. So, you know, I
[09:41] recommend being, you know, running all
[09:42] the examples, asking any questions um to
[09:46] copilot about things you don't
[09:47] understand and then pick one of the
[09:49] examples and build on it, right? So,
[09:51] general best practice is if I'm learning
[09:53] something, I do the basic I do the basic
[09:55] tutorial and then I build on that
[09:57] tutorial or build on something that
[09:58] already works. So, first, you know, you
[10:00] want to make sure you're building on
[10:02] something that already works. And if it
[10:03] does, great. Then extend that for your
[10:06] scenario, right? Think about something
[10:07] you can actually use it for, right?
[10:09] Maybe for your home life or for your
[10:12] developer life, right? I think those are
[10:13] my two most common scenarios is like
[10:15] something that helps me with parenting,
[10:18] like planning summer camps. I did that
[10:20] the other day with an LLM. Um or
[10:22] something that helps me with, you know,
[10:24] codebased maintenance, right? So, um I
[10:26] often will, you know, write like
[10:28] triagers to to help me maintain my
[10:30] issues, for example. So, you know, pick
[10:32] a use case that is actually relevant for
[10:34] you. uh because then you're going to be
[10:36] able to evaluate whether it is doing a
[10:38] good job. It is very important that
[10:39] you're picking a scenario that you have
[10:42] domain expertise in so that um then you
[10:46] can um you know look at the answers and
[10:49] know if they were good. Uh this is very
[10:51] important withever whenever you're with
[10:53] using LMS because remember LMS can be
[10:56] convincingly wrong. Uh so you want to
[10:59] pick something where you do have domain
[11:00] expertise, right? Uh let's see. We got
[11:03] recommendations for boot.dev. dev. Um,
[11:07] let's see. Okay, cool. I like the font.
[11:11] Uh, so you can check out that course as
[11:14] well. All right. Um, so Bernard says,
[11:18] "Scode often forgets you have a VM in
[11:21] your project. Does it swap that
[11:22] knowledge out of its memory from time to
[11:24] time?" Oo. Um, that's a good question.
[11:28] And so you know if what we can do here
[11:31] here like when you're in VS Code and
[11:33] you're wondering what information does
[11:35] it have? I always go to you see this
[11:37] little dot dot here. Click the dot dot
[11:40] and you say show chat debug view and
[11:42] that will show you everything that is
[11:45] sent um you know over uh to the LM right
[11:50] um
[11:52] so let's see uh clear my reddus okay all
[11:56] right so here we can see this is the
[11:57] full conversation so we can see all the
[11:59] tools that got sent to it we can see the
[12:02] full system prompt from GitHub copilot
[12:06] um you know there's it's a lot
[12:09] Ha. This is all all stuff from GitHub
[12:12] Copilot. And then we can see there's
[12:14] actually um memory guidelines because I
[12:16] am using the memory tool. We should see
[12:19] the actual memories at some point. Let's
[12:20] see if it I don't Oh, and this is from
[12:22] me where I tell it my username. Uh this
[12:25] is the agents.md. So we do have an
[12:27] agent. MD in this repo. So it gets sent
[12:31] um you know. So if it if it did
[12:33] understand anything about the
[12:34] environment, like the fact that there's
[12:36] avm, we would expect it to be, you know,
[12:41] somewhere somewhere in here. Um, oh,
[12:45] here we go. Environment info. The user's
[12:46] current OS info is Linux. Uh, so this is
[12:49] an example of context, right?
[12:50] Environment info. I'm on Linux because
[12:52] I'm on a dev container. I'm working on a
[12:54] workspace with these folders, right? And
[12:56] you can see the folders here. Um, it
[12:59] actually doesn't mention the VM here. uh
[13:02] even though I have avm so it it that
[13:04] might be because it's in the getit
[13:06] ignore and it might decide I don't know
[13:08] why it doesn't mention the VM here
[13:10] that's actually a really good question
[13:12] um because it did show py cache
[13:15] interesting uh let's see um user memory
[13:18] so if there were any memories it would
[13:20] pull it from here repository memories oh
[13:23] this is fun um so we can see these are
[13:27] all memories that it decided to store uh
[13:30] Spanish translations use informal latm
[13:33] right so these are all memories that
[13:35] decided to store so if I went to my
[13:36] GitHub repo I would see them all
[13:40] uh let's see and then we have
[13:41] information about the current repository
[13:44] current date remember I told you good to
[13:46] have your current date uh terminal
[13:48] information last command run and exit
[13:50] code and some reminders okay so this all
[13:55] of this is the context before we get to
[13:59] the user request Right. Finally, we get
[14:02] to the user request. So, it's really,
[14:03] really interesting to see everything
[14:06] that gets sent to GitHub Copilot. And I
[14:09] think it's helpful if you're developing
[14:10] your own agents because you really see
[14:12] how much environment information the
[14:15] coding agent is sending. Um, and and
[14:18] yeah, it's interesting to see there that
[14:19] it didn't actually list a VM. The other
[14:21] thing, of course, to look at is the
[14:22] tools, right? Sometimes it's going to be
[14:24] using tools to decide. So in this case
[14:26] there is like a Python
[14:29] um this Python tool that has get Python
[14:31] environment info and you know maybe
[14:34] maybe that's not returning correctly
[14:36] right
[14:38] um so so yeah so I don't know exactly
[14:40] why um you could poke into that and see
[14:43] if you see differences in you know in
[14:45] that chat debug you can you can file um
[14:48] issues about it I think it's for me it's
[14:50] gotten better at understanding my Python
[14:52] environment but I also think it's not
[14:54] Perfect.
[14:56] >> All right. Uh, okay. Let me catch up.
[14:59] Um,
[15:01] uh, okay. So, from PK, two questions.
[15:04] Uh, why would use agent framework and
[15:06] not the Foundry SDK and why consider
[15:08] non-foundry hosting options? Okay. So,
[15:12] um, the Foundry SDK is, let me find the
[15:14] docs for Microsoft Foundry agent SDK.
[15:17] So, Microsoft Foundry has a hosted agent
[15:21] service. Um so if you use that you are
[15:24] running the agent um in like the agent
[15:27] loop entirely in the cloud and the big
[15:31] advantage to me is that then if there's
[15:33] built-in tools that Foundry agent
[15:35] builtin tools like Bing search code
[15:37] interpreter it's really easy for the
[15:39] foundry agent to call those tools
[15:40] because it's already running in the
[15:41] Azure cloud and they're just right there
[15:43] and it's very easy to set them up. Um,
[15:45] and also in this case, if you do found
[15:47] your Agent, it does have its own like
[15:49] built-in session management, right?
[15:50] It'll it'll set that up for you. Um, so
[15:53] it's it's like less setup, right? Like
[15:55] you get some built-in tools out the bat
[15:57] and you get built-in session management,
[16:00] right, with um with like threads and
[16:02] stuff. So it'll build it'll create that
[16:04] thread database for you. Uh, so that's a
[16:07] benefit. The drawback is that it is, you
[16:09] know, a a very hosted service. So if you
[16:12] run into um limitations of the way it's
[16:16] you know storing threads or the way it's
[16:18] using tools the way it's running things
[16:20] in a loop like you know the the amount
[16:22] of flexibility you have might be limited
[16:24] in terms of like middleware right we saw
[16:25] an agent framework we can add middleware
[16:27] at many many different points it's very
[16:29] likely that you can't add middleware to
[16:31] as many parts of a foundry agent because
[16:34] a lot of it is running in the cloud and
[16:36] you just can't intercept it at the same
[16:38] places so that's what I would say
[16:40] generally the drawback is going to be
[16:41] with any sort of hosted agent is that if
[16:43] the agentic loop is running in the
[16:45] cloud, it's going to be harder for you
[16:47] to insert yourself into that agentic
[16:49] loop and customize it further, right?
[16:51] Um, but that being said, if it works for
[16:54] you, great. Like if it has everything
[16:55] you need and you don't find yourself
[16:57] needing more than that, then then
[16:59] awesome. You're good to go, right? So
[17:01] that that's that's always going to be
[17:03] the, you know, the consideration when
[17:06] you're deciding whether to use a hosted
[17:07] service is does it do everything I need?
[17:10] Is it flexible enough for me? Um or do I
[17:13] need to be able to customize further?
[17:14] Right?
[17:16] Um so if you decide not to use the
[17:18] Foundry SDK uh and instead do agent
[17:21] framework, then that's when you would um
[17:24] consider options for where you want to
[17:26] host it because now you have additional
[17:28] options. Uh that being said, if you do
[17:29] use agent framework, you can also
[17:31] basically host it on Foundry as like
[17:33] what's called a hosted agent. Um
[17:36] um and then you get a little bit of the
[17:38] foundry management.
[17:42] All right, good questions. Um
[17:45] so Manny says, "From your two
[17:47] presentations thus far, it appears that
[17:49] designing your overall project cannot be
[17:51] LLM agnostic. Um you know, the way we
[17:54] design build tools, manage memories are
[17:56] designed based on LM. Can you confirm?"
[17:58] Uh that's a good question. So you know
[18:00] you saw in our examples we in each of
[18:03] them we um you know set up our our uh
[18:09] connection and we used the the um open
[18:14] AI chat client. So this means it is it
[18:18] is um you know using the chat
[18:21] completions API.
[18:24] Okay. So stepping back there are every
[18:28] LLM like there's different APIs out
[18:30] there right like HTTP um you know APIs
[18:34] for interacting with LMS OpenAI when it
[18:37] uh you know for the last few years um
[18:39] okay OpenAI first when it first came out
[18:41] it had this completions API uh which we
[18:45] basically don't use anymore then it came
[18:46] out with the chat completions API where
[18:48] you pass in a conversation and you get
[18:50] back a new response and that's like that
[18:52] really become very very popular very
[18:54] fast and that's what the majority of
[18:55] people are still using is the chat
[18:57] completions API. Then about a year ago
[18:59] they came up with the responses API
[19:02] which is very similar to chat
[19:03] completions but also has support for
[19:05] built-in tools. So it's it's actually a
[19:07] bit more convenient. It's a little more
[19:09] agentic in that it does have built-in
[19:10] tools. If you're using like Azure you
[19:12] would get access to the code interpreter
[19:13] and web search um just built in and it
[19:16] has more of a notion of state like it
[19:18] can be stateful or stateless. So that's
[19:21] a responses API. So when you're using
[19:23] OpenAI models on Azure, you can use chat
[19:25] completions or responses. And in fact,
[19:28] Azure is standardizing on responses now.
[19:32] Um so even though we're not using it
[19:33] today, um increasingly uh you're going
[19:36] to see more uses of responses. Um and
[19:39] because responses can be a generic layer
[19:43] on top of all of the Foundry models
[19:46] because Foundry has more than just
[19:47] OpenI, right? Foundry has DeepSeek, it
[19:50] has Mistral,
[19:52] um tons, tons and tons of models, right?
[19:54] Deepseek, llama, etc., right? So,
[19:57] Foundry has this generic support for
[19:59] responses across all of them. Uh this is
[20:01] a repo that my colleague just
[20:06] um just made. So if you want to get
[20:07] started with responses API um you know
[20:11] across all these um so that means if you
[20:13] standardize on responses API then um you
[20:17] know you can theoretically you know
[20:20] point at uh any of the foundry models.
[20:22] So that's that's very cool. Um the
[20:26] reason we didn't use it today is because
[20:28] GitHub models does not support it and we
[20:31] wanted you to be able to run things in
[20:33] GitHub models. So that's a little
[20:34] awkward. If we weren't relying on GitHub
[20:36] models, GitHub models only supports chat
[20:38] completions right now. If we weren't
[20:40] trying to make stuff work in GitHub
[20:41] models, we actually would have used
[20:42] responses for everything. Um, so yeah,
[20:45] so you know, right now this is somewhat
[20:49] specific to OpenAI models or at least
[20:51] specifically just to things that support
[20:53] chat completions, which is still a lot.
[20:54] Like you can like OAMA supports chat
[20:56] completions, right? Like lots of models
[20:58] do support chat completions. Um, but in
[21:01] production when I if I wasn't having to
[21:03] worry about GitHub models these days, I
[21:05] would switch everything over to
[21:07] responses API because that's going to be
[21:09] the most agnostic option if your models
[21:11] are on Foundry, right? Because then if
[21:14] you're using responses API, in theory,
[21:16] you can point at any of those Foundry
[21:19] models and your code is is going to work
[21:23] and you get access to those built-in
[21:25] tools.
[21:27] Um so so that's what I would say is that
[21:29] and and then you can have a fair amount
[21:31] of um agnosticism. So as long as
[21:34] something as long as you know something
[21:36] supports a responses API then you know
[21:39] then you you can work with it.
[21:42] Um okay. All right. So that was a very
[21:47] good questions. Um
[21:52] uh okay. Okay, so Esbonds follows up on
[21:55] the the question about summaries. Should
[21:57] the original be saved for a later
[21:59] summary?
[22:00] Uh, that's a very good question. I think
[22:03] yeah, you definitely could store the
[22:05] original in memory as as long as you
[22:07] weren't worried about going over memory
[22:10] like you're in memory constraints, which
[22:11] you probably wouldn't because it's just
[22:12] text. Um, so you could store that
[22:15] original in memory. Uh, I yeah, it's a
[22:17] good question. I don't know in
[22:19] practically whether people do actually.
[22:22] um store it in memory. Like the other
[22:25] thing you could look at is so to be fair
[22:27] I was inspired by lang chain for um for
[22:30] the middleware example. So if you look
[22:32] at uh their um GitHub
[22:37] uh they they have a lot of built-in
[22:39] middleware. So they actually build their
[22:42] summarization middleware into
[22:45] uh into their into their package. Um, so
[22:48] I looked quite a bit at this um to
[22:51] decide how to do it for agent framework.
[22:54] Um, but I simplified it a lot. Uh, but I
[22:56] definitely looked at their at their
[22:57] prompt. So, you know, take a look at how
[23:00] lang chain does it. You might get some
[23:02] inspiration also generally looking at
[23:03] their middleware like because people
[23:05] were asking like what are good uses of
[23:06] middleware like lang chain has all this
[23:08] middleware built in. It' be cool if
[23:09] Asian framework did more of it built in
[23:11] but also just because it's just nice to
[23:13] from a discoverability point of view,
[23:15] right? So this gives you a nice idea for
[23:18] um the kinds of uses for middleware.
[23:21] Some of this middleware uses LLMs. A lot
[23:22] of it doesn't. A lot of it is just like
[23:24] logging, counting, um that sort of
[23:26] thing.
[23:28] Uh so but yeah, so you know I think
[23:31] summarization is an art in a science and
[23:33] uh you can you know look for inspiration
[23:35] to see what other people are doing.
[23:39] All right. Uh um
[23:44] yeah, I think the point is that if you
[23:45] keep the full, you know, if you
[23:48] summarize, you could lose things. I did
[23:49] have like a really negative experience
[23:51] with summarization and copilot the other
[23:53] day. So I will share that because um uh
[23:57] let me actually just find find it so I
[23:59] can specifically
[24:00] uh
[24:02] um
[24:06] uh share
[24:08] share what that um was like. Um so this
[24:12] is kind of like a what not to do. Um
[24:16] uh so here what happened is that I told
[24:19] GB co-pilot like okay it says I you know
[24:21] I can give you a shorter slide friendly
[24:23] oneline caption version and so here I
[24:26] said yes please to wanting a caption
[24:28] right this should have been a single
[24:29] sentence response but notice how it
[24:31] compacted the conversation at that point
[24:34] and it decided my yes please was
[24:37] actually in response to wanting to
[24:38] implement the entire plan and I was
[24:41] still in planning mode and I was like
[24:43] hold up we are not implementing right
[24:45] now. You better like hold these horses.
[24:47] We're not implementing. Stop it. Um, but
[24:50] it it lost the fact that the most recent
[24:53] request was this and that the yes,
[24:55] please was this request. So, I think you
[24:56] do want to be really careful with
[24:58] summarization that you really retain
[25:01] that last message. like potentially
[25:03] maybe you should only summarize
[25:05] everything before this last message or
[25:07] in your prompt to the summarizer like
[25:09] really say like if the user you know
[25:11] like you if there like if there was any
[25:13] like follow-up thing I don't know like
[25:16] this is something I would test your
[25:17] summarization on is this sort of
[25:19] scenario where um you know user says yes
[25:21] please what is that yes to right because
[25:25] you really don't want to accidentally
[25:26] say yes to something that you don't want
[25:29] it to happen right so this was really
[25:31] interesting so This makes me think like,
[25:33] you know, this isn't your actual
[25:34] question about original messages, but I
[25:36] do think you have to be really careful
[25:37] with um retaining the most recent
[25:41] context. Like generally like a lot of
[25:43] the Yeah, you're going to have
[25:45] information that's really relevant in
[25:47] the most recent context, especially here
[25:49] where I'm answering. Um, and a lot of
[25:50] times there's also a lot of relevant
[25:52] conversation at the beginning. Um, but
[25:54] just just don't lose this, right? Don't
[25:56] don't let this happen.
[25:59] Um, let's see. Uh D. Okay.
[26:07] Yeah. See lots of situation um about
[26:11] summarization. Yeah. And if you're not
[26:12] sure, you just got to evaluate, right?
[26:14] And and come up with, you know, like
[26:16] interesting edge casations like this,
[26:18] scenarios like this, and see how does it
[26:20] do with this, right? Um and then put
[26:22] that in your evaluation. And of course,
[26:24] tomorrow we're going to talk about
[26:26] evaluation. But you know, generally the
[26:27] idea is that you would um you know,
[26:29] collect edge cases like this and see how
[26:31] it does.
[26:35] Um so Rose says they're running a PC in
[26:38] Foundry agent and started running into
[26:39] its limitations. Uh doesn't offer ways
[26:42] to change them in the portal. You have
[26:44] to dig deeper in the SDK to to see.
[26:46] Yeah, that can be tricky as well like
[26:47] because the Foundry agent experience is
[26:49] kind of like a very portal centric
[26:52] experience, but it also has an SDK. Um
[26:54] but you kind of have to figure out what
[26:55] you can do in the portal versus the SDK.
[26:57] Um I tend to prefer very code first
[26:59] experiences.
[27:01] Um and then the question is like have
[27:03] you run into broking breaking changes. I
[27:05] believe they are iterating quite a bit
[27:06] on Foundry agents like um there's like a
[27:08] V2 or whatever, right? So um I think you
[27:11] are going to have to um you know keep up
[27:14] with them. Um code interpreters not
[27:18] working. Oh that's sad. Um that might
[27:21] might just be a fluke.
[27:24] Yeah, I see. That's a great this is a
[27:26] great summary of the the issue with
[27:28] compacting conversation, right? So, it'd
[27:30] be great to like just set up these like
[27:32] example uh conversations to test
[27:34] summarization with to see, you know, see
[27:36] how it does.
[27:38] Um
[27:41] I don't know if the question does copa
[27:43] expect me to use the thumbs up.
[27:44] Actually, I don't know. I think that
[27:46] this thumbs up and thumbs down are
[27:47] primarily used for um you know uh pure
[27:51] QA for seeing um you know monitoring so
[27:54] that the co-pilot team can see generally
[27:55] are they getting more thumbs and thumbs
[27:57] down. I don't really use them anymore.
[27:59] Um I only use the thumbs down if I want
[28:01] to report an issue because you can just
[28:03] say thumbs down report an issue and it's
[28:04] just the fastest way to get to the issue
[28:06] reporter. So, if you do have an actual
[28:07] bug like with Bernard with like theVBM,
[28:10] um you can, you know, pop this open and
[28:12] because that way it's going to include
[28:14] um all your VS Code info and it's going
[28:16] to put it in the right repo. So, that's
[28:18] the only time I use that thumbs down. Um
[28:21] of course, you could use it for all this
[28:22] too. It's just going to send data to the
[28:23] team. Um I don't think any of that is
[28:26] sent to the LLM. That's my guess. I'd
[28:28] have to check the chat debug view to see
[28:29] but I think this is more about sending
[28:32] uh analytics to the copilot to see to
[28:34] see how users are perceiving the quality
[28:36] right
[28:39] um
[28:44] uh so Bernard says they have a rail
[28:46] guard for prompts have a minimal length
[28:48] for agents um so that's when you're like
[28:51] building agents for your in your
[28:53] organization
[28:55] um yeah That's a That's a good idea as
[28:58] well.
[29:00] Okay, let's see.
[29:03] Uhuh. Let's see if there's any Foundry
[29:07] uh yes, we're we haven't really we're
[29:08] not talking about Foundry agents in this
[29:10] series. That also might be something
[29:11] we'd cover in a in a a follow-up series,
[29:15] but there's also the difference between
[29:17] Foundry Classic and Foundry New. And
[29:18] some things work in Foundry Classic
[29:20] Portal, some things work in Foundry New.
[29:23] And um you know I think there's some
[29:25] growing pains uh with all the changes on
[29:28] Foundry. So I tend to stay in my happy
[29:31] land um of just writing code in in VS
[29:35] Code agent.iq. Well there is the three
[29:39] IQ IQ times three. Um we've got Foundry
[29:42] IQ, Fabric IQ, and Work IQ. Um I don't
[29:46] know if that's what you're talking about
[29:47] with agent.IQ, IQ. But uh but Microsoft
[29:50] now has three services branded IQ. Um
[29:54] Foundry IQ is basically AI search which
[29:56] I talked about today. Fabric IQ is on
[29:59] top of Microsoft Fabric and it's um
[30:01] built on top of Fabric ontologies. Um I
[30:04] haven't used it but I just heard about
[30:06] it. And then work IQ is built on top of
[30:08] Microsoft Graph and is like an MCP
[30:10] server.
[30:15] All right. What other um questions do we
[30:20] have?
[30:27] Let's see. Um okay, we have a question.
[30:31] Um what are the issues with Foundry? Um
[30:35] well, as you see, there's maybe some
[30:37] breaking changes as things change. Um
[30:41] uh but you know, just yeah, generally,
[30:43] you know, things are changing. Um
[30:44] there's different kinds of there's now
[30:46] like basically there's there's two kinds
[30:48] of Foundry projects. There's hub-based
[30:49] projects and then there's the new
[30:51] Foundry kind of projects. So there's
[30:52] that that's different. But then also
[30:54] there's two UIs for Foundry now. There's
[30:56] Foundry Classic and Foundry New. And
[30:58] like some things work in Foundry
[31:00] Classic, some things work in Foundry
[31:01] New. So you kind of have to keep track
[31:03] of that as well. And then for Foundry
[31:05] agents, I think there's an agents v2
[31:07] service and an agents v1 service. And so
[31:10] you have to keep track of that. So
[31:11] there's there's just a lot changing
[31:13] there and I personally have not quite
[31:16] kept track of it. Um but you need to
[31:18] keep in mind all those changes and just
[31:21] keep track of like okay what kind of
[31:22] foundry project are you in? Which
[31:24] Foundry UI are you using? Are you using
[31:26] agent service v1 or agent service v2?
[31:30] Um so yeah.
[31:34] Um okay. Is IQ using graph frag with
[31:37] knowledge graphs? Well, when you say IQ,
[31:39] we've got the three different IQs. I'm
[31:40] going to assume you're using found
[31:42] you're talking about Foundry IQ. So if
[31:43] you are talking about Foundry IQ then it
[31:46] is using um the new knowledgebased
[31:49] feature
[31:51] um and um and you can just you basically
[31:54] you point it at a um you know add a a
[31:58] knowledge you set up the knowledge base
[31:59] with whatever knowledge sources you want
[32:01] and then um you can set like the mode
[32:04] for the knowledge base and you know and
[32:06] it uses that. But Foundry IQ is
[32:08] basically as your AI search
[32:10] knowledgebased feature, right? Uh so it
[32:12] does not use graph rag at this point. Um
[32:15] the team is always looking into stuff
[32:17] like graph rag. In the past it hasn't
[32:19] they haven't found a good way of like
[32:21] productionizing it and being able to run
[32:22] those graph rag queries efficiently in a
[32:25] way that really got good results. Um but
[32:27] they are always looking into uh things
[32:31] like graph rag. Um, so you know, you
[32:33] know, maybe it'll add something like
[32:34] that if it finds good results, but it's
[32:36] also looking into other stuff like, um,
[32:38] you may have heard of, uh, Copali, which
[32:41] is a different kind. Uh, so Cali
[32:44] Yeah. Um, Colbert Copali. Uh, it's just
[32:49] a different um, sorry, Colbert. Um, it's
[32:52] a different approach to uh, vector
[32:54] search. Colbert Steven Colbert.
[33:00] Oh, got it. multi vector embeddings.
[33:02] Yeah. Um so yeah, generally the AI
[33:04] search team is always looking into how
[33:06] they can improve retrieval. Um but you
[33:09] know there's a lot of things that work
[33:10] well in research or in local databases
[33:13] but then when you try to put them into
[33:16] production uh then you know you run into
[33:18] more issues. Uh and that's always a
[33:20] question of how how they can make things
[33:22] production level that's going to work
[33:24] for everyone.
[33:29] Uh
[33:30] D
[33:32] um you know with with Okay, so question
[33:35] from Pixels and Bits with the Microsoft
[33:37] agent framework. Is there any middleware
[33:39] context caching that can be that can cut
[33:41] down on token usage?
[33:44] Um
[33:45] yeah, you could do some some um you
[33:49] could do some more caching, right? Like
[33:52] especially if you were doing, you know,
[33:54] um you know, we talked about different
[33:56] context providers today. So you could
[33:57] imagine that in those context providers
[33:59] you could do a um you know do a do a
[34:05] search but here when you're saying
[34:07] cutting down on token usage that means
[34:08] you want to like send less tokens to the
[34:11] LLM.
[34:13] Um there's also a question that LLMs
[34:16] have themselves like I how does this
[34:19] work? I think if we like if you send the
[34:22] same system prompt to the LM, it may be
[34:25] able to use its own caching feature,
[34:27] right? So there's there's different
[34:28] kinds of like caching we're talking
[34:30] about here. Um like the enthropic
[34:33] models, they have this this caching
[34:35] feature with their long context, right?
[34:37] So yeah, the issue of of caching is
[34:40] really interesting one. So there's
[34:41] there's there's a side of the fact that
[34:43] like if you keep certain things
[34:45] constant, then they will get cached.
[34:48] Like for example, when you're using
[34:49] structured outputs uh and with open AI
[34:52] models, it will in fact cache like the
[34:54] JSON schema setup for them. So that's
[34:57] like the first call is slow but then the
[34:58] subsequent calls are faster. Um but then
[35:01] I think there's also that a lot of LMS
[35:02] will implement um system prompt based
[35:05] caching. So if you keep the first you
[35:08] know uh end tokens of the system prompt
[35:10] the same then you know then it'll um you
[35:13] know it'll cache those. Um but I would I
[35:15] actually haven't dug into them a lot. If
[35:17] anyone um has and has some links to
[35:21] remind us of what LLM caching we could
[35:24] take advantage of, that's um that's good
[35:26] to know because that just affects like
[35:28] maybe where you put stuff in your um in
[35:31] your system prompt, right? To take
[35:32] advantage of LM caching. Like maybe you
[35:34] always keep the the prefix of your
[35:36] system prompt the same. Um but for
[35:38] middleware to reduce token usage um
[35:43] h I'm trying to think how you can reduce
[35:44] token usage without doing some you can
[35:47] do like just truncation right I used to
[35:49] do that where I would just truncate but
[35:51] of course there's a danger to truncation
[35:53] where you're you're missing context
[35:55] right um but if you have if you you like
[35:59] the question is do you have a heristic
[36:01] that does not use an LM whereby you can
[36:03] remove stuff you're from your context if
[36:05] you have that heruristic then great You
[36:07] can build the middleware that can do it,
[36:09] but you do need to have that heristic,
[36:12] right? And so you may have a heristic.
[36:13] In the past, I just did like, you know,
[36:15] remove the oldest messages. Um, but you
[36:18] definitely risk losing information
[36:21] there. I wonder what their context
[36:23] editing middleware do. Oh, clearing
[36:26] older tour results. Right. So that's
[36:27] interesting. So this one probably
[36:28] doesn't use an LM. This probably just
[36:30] uses a heristic, right? Right? So that
[36:32] would be an example of one that they say
[36:34] like well once you've gone past a burnt
[36:36] number two tour results um you know you
[36:38] may want to truncate right so you just
[36:40] you would have to have a heristic for
[36:42] what you're going to remove and um
[36:45] consider whether it's going to still you
[36:47] know have good results right so you want
[36:49] to evaluate there
[36:54] um let's see do we have examples with
[36:57] app service and UV on Azure uh is Gwen
[37:01] around. Gwen is the one. I'm trying to
[37:04] see if Gwen's in our chat still. Um
[37:09] Gwen is the one that that was playing
[37:10] with that and and working with the app
[37:12] service team. Okay, let's see. App
[37:14] service UV because I thought we Yeah, we
[37:18] did get it. Okay, what's new? November.
[37:20] Um support for UV.
[37:24] Um so I haven't messed with it. I think
[37:27] Gwen did mess with it. Um, check out you
[37:30] weren't able to make it work. Okay.
[37:31] Okay, great. All right, Gwen and John,
[37:34] if you can work together and figure that
[37:36] out. Maybe there's some bugs we need to
[37:38] report to the app service team. So, um,
[37:40] so Gwen was working with the app service
[37:42] team on that. So, if there are some
[37:43] issues, we should get that reported to
[37:44] the app service team.
[37:48] Uh,
[37:51] uh, so,
[37:53] um, Rose wants to Rose wants to move to
[37:56] code first. Agents do it. I love it. Um,
[38:00] Bernard uh says, "Model router also can
[38:03] save tokens."
[38:04] Let's see. How does the model browser
[38:06] How, wait, how does a model browser save
[38:08] tokens? You mean like you can go to like
[38:10] a cheaper model, but isn't it still
[38:12] using the same number of tokens? Can you
[38:14] clarify on that? Um, let's see. Honor
[38:17] says, "Oh, this is a good question. Is
[38:20] it possible to use skills like GitHub
[38:22] Copilot?" This question just came up in
[38:25] our internal agent framework chat. So,
[38:26] let me find the answer to it. Um, let's
[38:29] see.
[38:31] Um, okay. Uh,
[38:37] um, okay. So, they added support for.net
[38:41] for skills. Um, because apparently this
[38:43] is something other frameworks are um
[38:45] supporting is the ability to just point
[38:47] at local skills. Um, so they did add
[38:51] support for it in.NET net and they said
[38:54] they were going to follow up with Python
[38:56] support. Oh, here we go. Python support
[38:58] agent skills. Okay. And it was merged.
[39:01] Great. Uh oh, and look, it did it as a
[39:04] context provider. So, this is a perfect
[39:07] uh followup for this section is that um
[39:10] and now if you do have skills in the
[39:13] file system, um you could advertise
[39:15] those skills to the agent. So, very
[39:17] cool. Um good great question there. And
[39:22] yeah, test it out. You'll need to point
[39:24] at latest main, but that's how we roll
[39:25] here. You just update the Git hash and
[39:27] UV sync and try it out and report any
[39:31] issues uh to the team. Awesome.
[39:35] Super cool to see that. Um so many
[39:37] different ways we can uh build our
[39:40] agents. Okay. Uh
[39:45] okay. Oh yeah. So model so Bernard says
[39:48] model routing helps only for simple
[39:50] questions
[39:55] when you have a um okay so I think it
[39:58] sounds like basically like you're you're
[39:59] saving because you're using a cheaper
[40:00] LLM. So um and maybe also you can I
[40:03] guess one way that you reduce token
[40:05] theft is that some LLMs are more verbose
[40:07] than other LLMs, right? So, for example,
[40:09] going back to AI search, um you can pick
[40:11] which LLM is used for the query planning
[40:14] and some LLMs will like generate like 10
[40:16] different queries and other LLMs will
[40:19] generate like two different queries. Um
[40:21] and it's just because some LLMs like
[40:23] they're just they're just different,
[40:25] right? So, it is true that like yeah,
[40:27] depending on what you're doing, some LM
[40:28] will just like decide to call lots of
[40:30] tools like will decide to be more
[40:32] verbose in their responses, right? And
[40:35] you know, you can you can switch your
[40:37] LMS, you can put in your system prompt
[40:39] like, hey, limit yourself to this. You
[40:40] can just cut it off and say like,
[40:42] listen, like you've done too many tool
[40:43] calls. Um,
[40:46] so uh so yeah, you can there there is
[40:48] certainly a lot of um you know um LM
[40:52] dependency. Actually, let me find this
[40:53] great blog post from my colleague
[40:57] Anthony where he did some comparisons.
[41:02] Uh
[41:04] D
[41:09] performance benchmarking LM models. So
[41:11] here he does talk about the fact like
[41:13] you can run these um you know run
[41:16] uh you know run these evaluations he was
[41:19] looking at time and but really the
[41:21] reason that time varied so much a lot of
[41:23] times was based off of the L some LLM
[41:26] just being way more verbose. Right. So,
[41:28] so that's an interesting um
[41:32] observation is is that um you know LMS
[41:35] can really vary in their veracity and
[41:36] when regard to tools is how many tools
[41:39] they decide to call and what they call
[41:40] it with
[41:44] uh okay tune notations can I share some
[41:49] comments about the tune notation
[41:52] project? Yeah, you know, I saw I saw um
[41:57] let me see if Okay, so I do recommend as
[41:59] it comes to context, I really like um
[42:02] Drew Brunig. He's actually even writing
[42:05] a book um which is really cool. So he is
[42:08] like a context expert and I believe he
[42:12] tweeted about tune. So I would I would
[42:15] defer to him. I don't know if he I don't
[42:17] know if he posted about it, but I do
[42:19] recommend um
[42:22] uh checking out his blogs and and
[42:25] following him um on uh on on social
[42:30] media. He really should post his put his
[42:35] social media here. Um because I do think
[42:38] he
[42:40] I think he um did promote some research
[42:45] about it.
[42:48] Oh, cool. I didn't even know he was in
[42:50] San Francisco. I should go
[42:53] go to that meetup. Um okay, let's see.
[42:55] Tune tune. Can we get Tune? Uh I I think
[42:59] he posted about it because basically I'm
[43:01] trying the research said something like
[43:04] you know that um
[43:07] the research said something like you the
[43:11] LLMs end up being less efficient with
[43:13] tune because they don't know it as well.
[43:15] Right? So there's like people try to do
[43:17] like new coding, you know, new shell
[43:19] commands and new coding, you know, not
[43:21] notation formats and all that stuff, but
[43:23] when the LLM doesn't know that format,
[43:27] then um it just doesn't do, you know, it
[43:31] doesn't it doesn't it doesn't do as
[43:32] well. There we go. I got it. Yes. Okay.
[43:36] So here's the research.
[43:39] um
[43:41] saving a handful of tokens in the data
[43:42] format is wasted if models are not
[43:45] trained on the format. Right? So our
[43:47] beloved YAML versus tune. Um so tune
[43:51] consumed more tokens just because the
[43:55] models didn't understand the two syntax
[43:57] and you know weren't able to use it
[43:59] well. Right? So you know I would you
[44:02] know anytime there's a new format like
[44:04] this I would take it with a grain of
[44:05] salt. um and you know actually you know
[44:09] do your own evaluations or um you know
[44:13] wait for research on it like we benefit
[44:15] so much from the fact that LLMs know you
[44:19] know know these formats and um know how
[44:23] to like interact with them in many
[44:25] different ways right if you're using
[44:26] YAML like it knows YAML syntax it knows
[44:28] PyAML the Python package for parsing it
[44:30] right it knows so much about YAML so
[44:32] even if like we all silently hate YAML
[44:35] at this point at this point like it's
[44:39] it's uh we're going to stick with it. Uh
[44:42] yes, these officers are recorded. Um
[44:45] looks like they're recording. Yep. So
[44:46] it'll be up uh later. All resources will
[44:49] be linked from um from the resources
[44:53] thread here.
[44:59] Okay, let's see. We got a few more
[45:04] minutes here. Any
[45:10] last um
[45:13] questions?
[45:18] Wait and see. Why do I have 13
[45:20] notifications?
[45:24] Yay. Sebastian.
[45:27] Uh all right.
[45:32] Thank Oh, thank you everyone.
[45:41] All right, if we don't have any more
[45:44] questions, we can call it since we've
[45:46] been going for a couple hours.
[45:50] And u remember tomorrow's session is
[45:53] about monitoring and evaluating. So,
[45:55] we're going to look at Open Telemetry,
[45:57] Aspire, App Insights, and then um
[45:59] evaluation with the Azure AI evaluation
[46:02] SDK to see how our agents are doing.
[46:08] All right, great. Thank you everyone.
[46:10] And if you do speak Spanish, you can
[46:11] tune in to Gwen's uh later today and get
[46:15] it in both languages. I'll be there in
[46:17] the chat as well. It's a super fun
[46:19] session.
[46:20] All right, bye everyone.
