[00:01] All right. So, I think there were
[00:02] questions on um middleware. Yeah, I
[00:05] really glazed over because
[00:08] as usual try to do too much. Um okay, so
[00:13] with middleware
[00:15] um there's when we create the agent,
[00:20] right? So I passed in all this
[00:21] middleware, right? So um we had
[00:26] middleware that we defined with
[00:28] functions. So the example here was this
[00:30] one, right? So this is the simplest way
[00:31] is to do a function. And for the
[00:35] context, it depends on what kind of
[00:37] middleware you're setting up. Right? So
[00:40] this one because I'm passing in the
[00:41] agent context, that means it's going to
[00:43] operate on the um you know on the on the
[00:46] level of the agent. So this is going to
[00:48] run before the agent runs. And then this
[00:50] basically is equivalent to like when you
[00:52] do agent run, right? like uh you know
[00:55] it's this is like the pre-processing
[00:58] before agent run and this is the
[00:59] post-processing after agent run
[01:03] um and yeah and you can just get access
[01:05] to anything that's in the context in
[01:07] this case I didn't access the context
[01:08] but you can see in the agent context we
[01:10] get agent we get messages we get session
[01:13] so that if there was like a chat history
[01:15] you would see that here um any options
[01:18] whether it's streaming the result so
[01:20] that can be useful um if you want to
[01:23] override it, right? So you can So that
[01:25] would be something you would override
[01:26] afterwards, right? So you be like, you
[01:29] know, agent result equals, right? So you
[01:33] could you could overwrite it there if
[01:34] you wanted to. Um or sorry, it' be
[01:36] context, sorry, context.
[01:40] You know, equals block, right? Uh so all
[01:44] sorts of interesting things you can do
[01:45] there.
[01:49] Um so that's that's a functionbased
[01:52] middleware for the agent context and
[01:54] then we had the same this one's on the
[01:56] um uh this is a function a functionbased
[01:59] middleware for the function context
[02:02] and then this is a you know a function
[02:05] based middleware for the chat context.
[02:07] Uh so for each of them you can check to
[02:09] see what you have access to
[02:12] and uh in this one also you can override
[02:15] the result from the LLM like you know if
[02:17] you wanted to override what came back um
[02:19] or kind of filter it like if you were
[02:21] going to do PII reduction.
[02:24] Same thing with function result. So all
[02:25] of them let you mutate that result if
[02:28] you need to which is interesting.
[02:33] Uh so when to use it? Well, what I was
[02:36] suggesting for uh let me go back to the
[02:39] slide about when to use it, right? So,
[02:41] for function uh well, there's two okay
[02:44] when we say function middleware, there's
[02:45] you know defining a middleware using a
[02:47] function and then there's actually
[02:48] function middleware um which sits
[02:51] between the LLM calls and you know like
[02:53] the agent and the calls to the
[02:55] functions, right? So, here I think you'd
[02:57] want to use the function context
[02:59] middleware for lots of things having to
[03:01] do with security, right? So um uh you
[03:05] know checking permission like if you had
[03:08] a server that authorization that might
[03:10] be the way you wanted to implement
[03:12] permission checking um doing human in
[03:15] the loops uh stuff uh limiting the
[03:17] amount of tool calls. This is what I've
[03:19] actually used it for is if um you know
[03:21] if I'm trying to limit the amount of
[03:22] context and sometimes I'll just cut it
[03:24] off and be like hey listen you've
[03:26] already made 12 you know like sometimes
[03:29] deep researchers go too deep right
[03:30] you're making this deep researcher you
[03:32] give access to the web and it just like
[03:33] keeps on researching forever and every's
[03:35] like listen I'm cutting I'm cutting you
[03:37] off all right you are like doing too
[03:40] much
[03:42] um so uh
[03:45] you know so you're not allowed to do any
[03:46] more calls so that is Actually something
[03:48] I've I've done in the past is said like
[03:50] listen after you've done 12 tool calls
[03:52] you're just done right um tool retry. So
[03:56] there's some ideas there about what you
[03:57] might do with function context.
[04:01] Uh I see a question why do the tools
[04:03] have hard-coded recurrent returns?
[04:05] That's because we're just doing demos
[04:06] that are going to work for you without
[04:08] needing an API key for like a weather
[04:10] thing. So what you should do here like
[04:11] this should be like actually call a
[04:14] weather API. The problem is there's not
[04:16] many weather APIs that are completely
[04:18] free. Um, you know, most of them require
[04:21] a key. So, we're trying to make
[04:22] something that like works for the demos
[04:25] and doesn't require a key. Um, but, you
[04:28] know, that means it's not real. Um, so
[04:30] you'd want to actually call a real
[04:32] weather API here. So, then you'd be
[04:34] doing like, you know, request.get, you
[04:36] know, um, right? Like that, right? And
[04:39] then, and then you'd be returning,
[04:41] right? Like that. So this is what your
[04:44] actual you know like an actual get
[04:46] weather tool would look more like this
[04:48] right um but uh
[04:53] you know we get we get we you know we do
[04:56] this for the for the demo so that
[04:58] they'll work without additional keys.
[05:02] Let's see
[05:05] what other questions. Um
[05:11] uh so Patrick says okay so Patrick is
[05:13] relating things to NAN. I haven't
[05:15] actually used NAN myself although I I
[05:17] know it's quite popular. So things like
[05:19] context and options and stuff. Yeah
[05:22] context the word context is very very
[05:25] overloaded. That is the topic for
[05:26] tomorrow's session and I spend a long
[05:28] time researching what different people
[05:30] think of as context. But um in the agent
[05:33] framework context is actually distinct
[05:36] from tools like like context always gets
[05:39] passed into the agent where like it's
[05:41] like information that always gets passed
[05:43] in versus tools which is like you know
[05:45] you're passing the definitions but they
[05:47] may or may not get called. Um but I
[05:50] would say every framework probably uses
[05:52] the word context in a different ways.
[05:54] And also like the word context you can
[05:55] see also gets used here just as like the
[05:58] context for middleware which is like
[06:00] here's the context that this thing was
[06:02] this middleware was called in right so
[06:04] generally just generally that word
[06:07] context is way too overloaded
[06:10] um in you know just in industry at large
[06:14] right now and also in frameworks right
[06:17] so this so you do see there's this this
[06:19] context here um but there's also what
[06:21] we're going to see tomorrow is that
[06:23] there's something called um context
[06:26] providers, right? So that's a different
[06:28] this that's the kind of context we're
[06:30] going to talk to about tomorrow is um uh
[06:34] that you can provide additional context
[06:37] uh that's always available and which you
[06:40] might use in cases other than tools
[06:42] right like for um memory and such.
[06:46] So I can't say exactly what you know
[06:49] what context means for N8N.
[06:52] Um, all right. So, we see a lot of
[06:54] trouble starting at the code space. Um,
[06:58] and unavailable model. I did see people
[07:00] commenting on unavailable model. I
[07:02] wondered maybe I have access. It's
[07:04] possible that I don't know if Gwen
[07:05] figured out. I don't know if I like if
[07:08] we are the only ones that have access to
[07:11] GPD5 mini. That's why I showed people
[07:14] the tip of setting this. So, you know,
[07:16] if you don't have access to GD5 Mini, um
[07:18] I mean, first you can check here and
[07:19] just see like you should at least be
[07:21] able to use this this playground. Um
[07:24] um
[07:27] and but um if for some reason you can't
[07:28] access GBD5 mini in particular, that
[07:30] might be more limited for some reason,
[07:33] then you can I created a MV and just set
[07:36] GitHub model in there. And then um all
[07:39] of the examples they all start with the
[07:41] like this same um client setup at the
[07:44] top which checks to see um if there's a
[07:47] GitHub model environment variable and
[07:49] otherwise falls back to a default here.
[07:53] Okay. So I guess GB may work for some
[07:56] didn't work for others. So um you can
[07:58] you know do check out the marketplace
[08:00] and see if there's something that's
[08:01] blocking you from using it GitHub models
[08:03] at all with your account. um
[08:07] um because I don't know if it's a
[08:08] limitation on models all all the models
[08:10] or just g5 mini but you can change the
[08:13] models um you know either directly in
[08:16] the code where it says GBD5 mini or
[08:19] create av and set your GitHub model
[08:21] there
[08:22] or even just set it you can just do like
[08:24] this GitHub model equals you know GVO
[08:29] right you just need to set that
[08:30] environment variable somewhere
[08:34] Um, yeah. Yeah. So, if you're trying to
[08:37] use these from Azure, if you were
[08:39] actually deploying it, so we do have
[08:41] instructions, too. If you're trying to
[08:42] deploy to Azure, uh, you do sometimes
[08:45] need permission for some of the models.
[08:47] Um, but GB5 Mini, you shouldn't need
[08:51] permission anymore with Azure.
[08:54] Uh, not for the general deployment. Um,
[08:59] let me check.
[09:01] Blah blah blah. availability GBD5
[09:05] one we we're doing GBD5 MIDI yeah it
[09:08] says no access request so if you do like
[09:11] if you deploy with our infra in the repo
[09:14] um it should just be able to deploy GB5
[09:17] mini you can see it's there's no form
[09:19] required and it's available in quite a
[09:21] few regions right now
[09:27] um and we are we are recording this
[09:30] session there's There's a comment about
[09:32] rewinding. So, this this session is
[09:34] being recorded. Um, so I'll have a
[09:36] transcript of it and everything after.
[09:39] Okay. So, let me go back because there's
[09:41] a lot of questions. Um,
[09:46] let's see.
[09:52] Okay. So, a question from Perfect Storm.
[09:54] You're working with Debi and you can see
[09:56] the tool calls. Is it possible to see
[09:58] the full information sent to the LM?
[10:00] Ooh, that's a good question. We are
[10:02] going to see that on um
[10:06] we're going to see that in Thursday's
[10:09] session because we're going to look at
[10:10] open telemetry and open telemetry. I
[10:13] think we're going to end up seeing it
[10:16] with the open telemetry calls depending
[10:18] on where you're instrumented. But here,
[10:19] I'll show you my trick because I do this
[10:20] all the time. Let me see if this is
[10:22] going to work today. Um so here we have
[10:25] agent tools. I'm going to set the level
[10:28] of um logging to debug,
[10:32] right? Because sometimes you just really
[10:33] want to know get what's getting sent to
[10:35] the the LM, right? Um so
[10:39] I'm going to go ahead and run
[10:43] uh this one. And now we've got logging
[10:45] at debug. So we're going to see a lot of
[10:47] information to an overwhelming extent.
[10:50] Um, but uh what's fun here is you were
[10:54] just asking, oh, how do you see what's
[10:55] sent to the LM? Here you go. This is
[10:56] what's sent to the LM, right? So, it is
[10:59] literally sending a request to SLhatmp
[11:02] completions. Here is the JSON data. You
[11:04] can see there's the conversation, uh,
[11:06] the model stream, etc. And then here's
[11:08] the tools with the definitions, right?
[11:12] Um and so here so uh so yeah if you do
[11:16] want to see what is getting sent uh
[11:19] what's harder actually it's really hard
[11:21] to see the request body but I do have a
[11:23] trick for that too if you're trying to
[11:24] see uh the response body uh but you will
[11:27] because this is wrapping on um top of
[11:29] the OpenAI SDK I think it's you can
[11:33] always if you set your logging level to
[11:35] debug
[11:36] then you pretty much always will get to
[11:38] see what's sent to the LLM.
[11:43] Uh, and we can see it comes back. Um,
[11:45] but we don't you don't see the response
[11:48] body by default. If you do desperately
[11:51] need that, if you check the agents MD
[11:54] for this repo because I had to figure
[11:56] this out, there's in fact tips for how
[12:01] to see response um, bodies with various
[12:04] SDKs. This is actually with the Azure
[12:06] SDK because I was trying to um figure it
[12:10] out. Um but I think that this also works
[12:14] I think this trick might work with the
[12:16] with the
[12:18] LM request.
[12:20] Um
[12:22] this trick you need for Azure but let me
[12:24] try this trick.
[12:26] Uh
[12:30] okay let's see it depend like the thing
[12:32] is all these SDKs use different um you
[12:36] know different ways of making HP
[12:38] requests so the way to intercept them is
[12:41] is different. Um, so here we've got the
[12:43] request options.
[12:46] Just seeing if we're going to see the
[12:48] response body, request options,
[12:54] response post headers.
[13:05] I don't think I see the response body.
[13:06] So, that is actually the hardest thing
[13:08] to see the body, but you can certainly
[13:09] see what gets sent to the LLM.
[13:11] Um, and of course we were just talking
[13:14] about middleware, right? So if you if
[13:15] this is something you want to see a lot
[13:17] like then um you know I think let's see
[13:20] you could also we could look at the chat
[13:22] contest and here you know you can see
[13:24] the messages being sent. Um it's still
[13:27] not on the level of like HTTP like what
[13:30] I was showing. So I do like to just put
[13:32] on debug and just see what gets sent.
[13:36] Uh okay. All right. So let's see.
[13:39] What question are we on next?
[13:44] I like the comment. The the problem with
[13:46] what context means is that it is context
[13:49] dependent. That's right. Um okay.
[13:54] All right. Great question from Tea Leaf.
[13:56] Were these examples coded man manually
[13:59] vibe coded or a mix?
[14:03] Um
[14:04] I would say
[14:07] a mix. Um, a lot of these, the ones you
[14:09] saw today, actually, a lot of these were
[14:10] were handcoded. Um, but as you like,
[14:13] like as I start to, you know, like build
[14:15] more and more, um, you know, uh, I would
[14:18] actually say like the ones we'll see
[14:19] going forward were vibe. I I don't want
[14:23] to say vibe. They were I coded them in
[14:27] conjunction. So, what I do is that like
[14:28] I find all these examples, right? Like I
[14:31] I basically say, "Hey, here are the
[14:33] examples you're going to combine. You're
[14:34] going to combine this example and this
[14:35] example and this example, right?" So, um
[14:38] you know, I'll do that and then a lot of
[14:40] times I'll have like um you know, we'll
[14:42] come up with a plan first. Let me see if
[14:43] you can I don't know if you can. Yeah, I
[14:45] think you can see my um let me check out
[14:48] my branches. Um
[14:50] uh
[14:53] uh workflow builders.
[14:58] Um I'm just trying to show my okay plan.
[15:00] Right. So here I'm working on session
[15:03] five and um this was I used plan mode in
[15:06] GitHub copilot and I gave it like the
[15:10] full outline that I'd already written um
[15:13] you know based off of uh looking through
[15:15] the agent sample doc and then it wrote
[15:17] this plan right so basically like I work
[15:20] I work in conjunction with the agent on
[15:23] the plan and do a lot of back and forth
[15:25] and um adding to the plan and that way I
[15:29] can like you know be like okay now I
[15:31] think this looks good. You know, it's
[15:32] got examples that it's pulling from,
[15:34] right? And so I I kind of showed it
[15:35] where to find the most similar examples
[15:38] and uh you know, we we work it on
[15:40] together. It's uh it's collaborative.
[15:43] We're very collaborative.
[15:46] Uh let's see what other questions we
[15:49] have. Oh my gosh, so many questions. All
[15:50] right. Um do I recommend starting with a
[15:55] deployed model with Foundry for
[15:56] Learning? You want to do a multi- aent
[15:58] with MCPS integrations? I do think
[16:00] you're going to want to deploy as soon
[16:02] as you can because you you're going to
[16:04] rate you're going to reach the limits of
[16:06] GitHub models pretty quickly and you
[16:09] really cannot in my experience I at
[16:11] least cannot use small local models for
[16:13] tool calling. They're just not good
[16:15] enough. At least on my machine they're
[16:17] not good enough. They're not fast
[16:18] enough. If you have a really good
[16:19] machine maybe you can use an SLM um if
[16:21] you find one that's very good for tool
[16:23] calling that works on your machine but
[16:25] you must have a way better machine than
[16:26] I do. So generally to get really good
[16:29] responses from agents, you know, you
[16:31] want really good tool calling support,
[16:32] which means you do want like frontier
[16:34] models um and you they do agents do use
[16:38] up a lot of tokens. So um you know it
[16:41] does help to actually have a deployed
[16:43] model where you know you're able to use
[16:45] up that amount of tokens um because you
[16:47] might reach the limits with GitHub
[16:48] models. So if you can especially if you
[16:51] can like have your company pay for a few
[16:54] token credits because it doesn't take
[16:56] much like you can do a lot with like 20
[16:58] bucks right like you can do a lot even
[16:59] on openi.com right all these also work
[17:01] with openi.com so you know you can apply
[17:03] in Azure we've got the readme.md shows
[17:06] um has instructions for deploying to
[17:09] Azure you do a login and then um a
[17:13] provision and that'll that'll create the
[17:16] stuff in it'll create the that
[17:18] deployment there. Um,
[17:21] so I think it's nice if you can. Uh, it
[17:23] means you won't earn into the token
[17:25] limits. Um, but um, but yeah, also it's
[17:29] good to use free stuff as much as you
[17:31] can, too.
[17:34] All right. So,
[17:37] interesting. So, lot of people getting
[17:38] errors with GP5 mini. So, we probably
[17:40] we'll change it for tomorrow then. Um, I
[17:44] don't know why that is. There must be
[17:45] some limitations on GB5 Mini. It must be
[17:47] more restricted. Oh, and I see that
[17:49] honor just asked, can you use local
[17:51] llama models with agent framework? So,
[17:53] you definitely can technically use them.
[17:55] The question is whether they're going to
[17:57] work well. Um, I had like another
[18:01] Let's see where do I use I think in our
[18:03] other
[18:05] do we use it? I think we still have a
[18:07] llama set up in this other agent
[18:08] framework repo. Let me check.
[18:11] Um, and we were like trying to decide.
[18:14] Let's see. Does this one have a llama?
[18:15] Yeah, it does technically. So you you
[18:16] would do something like this. I haven't
[18:18] verified this with
[18:21] um the current thing. I guess I can even
[18:23] try it. Let me see. Did I let me see
[18:26] what models I have currently with a
[18:28] llama? So basically like Gwen and I
[18:30] both, you know, our machines aren't that
[18:32] powerful and we're like, "All right, are
[18:34] we going to have a llama support? Like
[18:36] do we even have machines that are
[18:38] powerful enough to check if a llama
[18:39] support works?" All right, we will do a
[18:41] quick check. It might work. And in which
[18:44] case, you know, I guess we add it back.
[18:46] We'll see. All right. So, let's see. Alf
[18:50] a host equals a llama. Okay. Let's try
[18:54] this. All right. Blah blah blah. Llama
[18:56] 3.1 latest. Okay. All right. I'm just
[19:00] going to set it to a llama.
[19:04] Okay.
[19:06] All right. Let's try this and see
[19:10] if we can get it working.
[19:15] Oh, it's doing it I because I changed
[19:17] forks. So, it's doing another
[19:21] setup. Got a merge main here.
[19:30] Yeah. So, Craig says, "For local models,
[19:32] make sure you pick a model that supports
[19:33] tooling. Not all modul." Yeah. So when
[19:35] you go to alama.com
[19:38] um you look at the models
[19:41] models there is they do specifically
[19:44] have a filter for tools like I have
[19:46] heard stuff good things about Quen
[19:49] um Quen
[19:51] I think I tried Neotron too Quen 3 I
[19:54] heard that one might be good um GPT a
[19:58] yeah GPD a I've used GP I my machine
[20:01] cannot run it I've only used it in the
[20:03] cloud on on Azure GPU serverless GPUs.
[20:07] Um, but it is if your machine can run
[20:08] it, it's quite good. Oh my gosh,
[20:12] we've got some package here that brings
[20:14] in like way too much. It's still it's
[20:17] still doing your rerun. Um,
[20:27] oh, so Teleaf that you're saying that
[20:30] the message that you need to create an
[20:32] Azure storage account. That is the
[20:33] expected response that if you just look
[20:35] at the example, it's it's just asking
[20:37] the question that's a response from the
[20:39] agent. Um, if you look at this, it's
[20:43] literally asking the agent, how do I
[20:44] create an Azure storage account? So, if
[20:46] you see an account, a response about how
[20:48] to create an Azure storage account, that
[20:49] means it's working. Uh, that's probably
[20:52] a little confusing. So, Craig says,
[20:55] "Gity and the GLM models are real nice
[20:57] to use if you have the VRAMm. Quinn
[20:59] models good for lower VRAMm." Yeah. So,
[21:01] I think I probably could try Quinn. I
[21:03] only recently cleared off a lot of space
[21:06] on my um on my machine. Um I gotta I
[21:11] gotta share the picture from this
[21:12] because this was crazy. Um because I had
[21:16] literally zero hard drive space left.
[21:18] So, I ran this tool called Grand
[21:20] Perspective and it makes this like tree
[21:21] map and so many of these squares are
[21:25] small language models. This one up here,
[21:26] this was like the hugging face. Yeah,
[21:28] these were the hugging face models. This
[21:29] was actually 53. So 53 was taking up
[21:32] like you know this fraction of my hard
[21:35] drive space right um this one over here
[21:37] was like foundry models over here are
[21:39] the Alama models and I I let them stay
[21:41] because um I do actively use a llama but
[21:43] just so much of my hard drive space was
[21:46] being taken up by cached models and they
[21:48] were like in cache files I didn't know
[21:50] where they are were so if you are
[21:51] playing with small models in different
[21:54] frameworks I do recommend checking your
[21:57] like hard drive to see if if Maybe
[22:00] they're like actually taking up half
[22:02] your hard drive space.
[22:04] Uh, all right. Let's see. Still
[22:06] installing.
[22:08] Why is it still installing? Okay.
[22:12] Um, okay. Uh, did I use
[22:18] this? Is this is an app called Grand
[22:20] Perspective. There's lots of apps like
[22:21] this that people were recommending. Um,
[22:24] all right. So, let's see
[22:27] what else
[22:29] people are asking.
[22:32] Um, okay. It definitely sounds like
[22:34] we're gonna have to change the model
[22:37] um to one that's not GB5 mini.
[22:41] All right, I'm just going to go back and
[22:43] see. All right, great. All right. Uh, it
[22:45] said connection error. Let me see a
[22:47] lama. Open a lama. Okay, so that's
[22:50] running. Oh, you know what the issue is?
[22:52] I'm inside a dev container. So that's
[22:54] fine. I'm just going to change this to
[22:56] what is it? Docker.in internal. Right. I
[23:00] think that's
[23:02] you have when you're inside a dev
[23:03] container, you have to like reach out
[23:05] the dev container in order to get at the
[23:07] um
[23:09] to get at the Docker that's running in
[23:11] your main machine. So I think
[23:16] I think it's docker. Oh, we still have
[23:18] like the huge amount of mapping on uh no
[23:21] add. No, I think I made that up. Okay,
[23:23] what is it? Um, docker
[23:27] inside container docker internal
[23:31] localhost. What is it? I should have
[23:33] asked the copilot too also. Um,
[23:36] host.docker.nal. That's what I wanted.
[23:39] host. Okay. Also, I'm going to take off
[23:42] the debug level.
[23:46] Uh, logging.
[23:49] Okay.
[23:54] Okay. All right. Let's see if it's going
[23:57] to go out.
[24:06] Yeah. Let me see if I can show you an
[24:07] example of a thread.
[24:10] Um
[24:23] Oh, it worked. It's working.
[24:26] All right. So, yeah, I guess we could we
[24:28] could add back the old llama.
[24:32] The nice thing that is like one of the
[24:34] big reasons I I like I do really like
[24:35] the coding agents is like if if I wanted
[24:38] to like I could just be like boom like
[24:39] add this to every single file and it
[24:41] would just do it, right? like re like
[24:44] like refactors like that um which are
[24:46] like not like typical refactors but are
[24:48] still basically like a trivial change
[24:50] across a bunch of files um you know I
[24:53] find they're you know much easier now so
[24:55] it's easier for us to maintain having
[24:57] like you know because by the time we're
[24:58] done with the series um there'll be like
[25:00] hundred examples in this folder right um
[25:03] so um yeah uh if people are actually
[25:07] using a llama we could add back the lama
[25:11] are all the models you're using free. Uh
[25:14] no uh only GitHub models are free. So if
[25:17] you're in code spaces, it defaults to
[25:19] GitHub models. You can see up here where
[25:21] I defaulted to GitHub models. Um
[25:23] otherwise locally I actually use Azure
[25:25] just to make sure um that I'm not going
[25:28] over limits. So you can see I use Azure.
[25:31] I've got a GB5 Mini. Um I've got some
[25:33] other stuff set up that we'll use uh
[25:36] later in the series. Um
[25:40] uh and then of course if you're using
[25:41] OpenAI, OpenAI is not free. Uh it costs
[25:44] money too. Olama is free. It's just your
[25:46] machine. It's however much you're paying
[25:48] for your machine. So here the one we
[25:50] just used was 3.1. Llama 3.1. That's
[25:53] actually quite an old model at this
[25:54] point. Um but it was able to handle that
[25:57] that um basic example there.
[26:02] Uh when I use a llama local, do I use
[26:04] local host? So typically I use local
[26:05] host. The thing is right now I'm inside
[26:07] a dev container um which means I'm like
[26:10] basically running a docker container for
[26:12] my VS code environment. So that's why I
[26:14] had to re like change this to
[26:16] host.docer.in internal. So if you're not
[26:19] running in the dev container and you're
[26:20] running locally then you're just going
[26:21] to do um you know the local host
[26:24] 11434v1.
[26:28] But if you are inside a container that's
[26:31] when you're going to do host dog
[26:33] internal. Um, so I'm running in a
[26:36] container because I was saying later in
[26:37] the week we're going to be using um
[26:40] stuff like uh Postgress and Reddus and
[26:44] Aspire like a bunch of stuff. So we've
[26:46] set this whole up with a dev container
[26:48] so that I'm always running inside a
[26:50] Docker container.
[26:55] Um, yeah, you're worried I was showing
[26:58] my keys. Uh, yeah, I I think that
[27:00] everything here is okay to be public. Um
[27:02] we generally use keyless
[27:05] uh connections. So you can see here this
[27:07] is using default Azure credentials. So
[27:10] um I'm logged in actually with both AZD
[27:12] and Azure for good measure. Um uh so
[27:16] yeah so there actually are no there's
[27:19] like an app insights key here but those
[27:22] ones are also not I think you know not
[27:24] considered to be very private um because
[27:27] I think people put them in their
[27:28] front-end code too. So I think we're
[27:31] good. Um, but also I don't want to like
[27:33] stare at it forever.
[27:38] Um, yeah, AZ and a are different um,
[27:42] login. So, there's a off login and then
[27:45] there's a login. Um, and normally you
[27:48] only have to do one of them, but because
[27:50] I am using a different tenant than my
[27:53] name main tenant, then I had to do both
[27:56] for reasons. Uh, okay. Let's see. Does
[28:00] the tracing in framework SDK also work
[28:03] with the opening eye tracing? Uh
[28:07] I don't think so. No. So um we'll talk
[28:10] about this on Thursday, but agent
[28:12] framework uses open telemetry for
[28:14] tracing. Um so anything like you know as
[28:17] long as you're outputting to open
[28:18] telemetry like you can take the agent
[28:21] framework open telemetry spans and put
[28:23] them there. Um but I don't think open AI
[28:25] tracing is actually like I don't think
[28:27] that open tracing is hotel. think it's
[28:29] like its own thing. Uh so there might I
[28:31] mean maybe there's a way to dig into the
[28:33] client like when you set up the OpenAI
[28:34] client like there might be a way to pass
[28:36] in your tracing information right
[28:39] because look you can even pass in your
[28:40] OpenAI client. So I would imagine like
[28:43] given we're basically like we are
[28:44] wrapping on top of OpenAI's client here.
[28:47] So I think if you wanted you like maybe
[28:51] it might work but I thought that they
[28:54] made their tracing specifically with
[28:56] OpenAI agents SDK. So, I would be
[28:59] surprised if it worked. You I think you
[29:01] got to dig into that a little bit, but I
[29:03] would be surprised if it worked.
[29:06] Um, let's see what else. How Oh, yeah.
[29:10] Yeah, you're right. I did supervisor too
[29:11] fast, too. Okay, so how does a
[29:14] supervisor work? All right, so we have
[29:17] this supervisor agent.
[29:20] Um, and you know, it has instructions.
[29:22] It says, "Okay, you're matching two
[29:24] specialist agents.
[29:26] um decide which specialists to call and
[29:29] it could actually call both. Um it would
[29:31] just uh you know had to figure out the
[29:33] sequence to call them in. Um
[29:37] and and then we say okay here's your
[29:38] tools. So we pass in the tools as if
[29:40] they are tools but then if we look at
[29:42] the tools plan meal is a tool that all
[29:46] it does is runs the meal agent with a
[29:49] query and returns back the response from
[29:52] that agent. So it is just wrapping on
[29:54] top of that agent. Right. So, same
[29:55] thing. And then, you know, and that
[29:57] agent is just a meal agent that has like
[29:59] find recipes and check fridge, which
[30:01] would be awesome if I had a check fridge
[30:02] tool. That would be really cool,
[30:04] wouldn't it? I wish. Um, and then the
[30:08] same thing here. Plan weekend just wraps
[30:10] on the weekend agent. And that's the
[30:11] same agent that we um, you know, used in
[30:14] our other examples. So, then,
[30:17] uh, let me actually do, you know, and
[30:20] okay, I need help. I need help. Let's
[30:24] let's do hard planning my kids dinner
[30:27] tonight and our we can plans. Okay. So,
[30:33] let's see if it's going to figure out
[30:35] that it has to do both of them here.
[30:37] Right.
[30:42] Okay. Here we go.
[30:50] Oh, I see another good question for
[30:52] after. Okay.
[30:57] Am I participating in Agents League?
[31:01] Uh, not as far as I know. Uh, I know my
[31:03] colleagues are Corey and who else is
[31:06] doing it? Um, it looks pretty Is that
[31:08] like the thing where they're doing like
[31:11] like esports or something?
[31:14] It looks It looked It looked pretty
[31:15] interesting. So, um I'm I'm not in it,
[31:18] but my colleagues are doing Agents
[31:19] League. Uh, you know, this series is
[31:21] going to keep me pretty busy the next
[31:22] two weeks. Uh, so here we can. So, it
[31:24] says, "I can handle both." Um, oh, oh,
[31:28] you know what's so funny? It asks for
[31:30] clarification.
[31:31] So, sometimes this happens, right? Like,
[31:33] you know, like normally when you build
[31:34] an agent, you're going to build it with
[31:36] some sort of user import input or
[31:38] something like this. But if your agent
[31:40] asks follow-up questions, then you know
[31:43] in this case it didn't answer the
[31:44] question because
[31:46] it um you know it has so many coming
[31:51] weekend in San Francisco. All right, for
[31:56] my fussy three-year-old and
[32:00] six-year-old. So I either need to use
[32:02] this in like a loop like I could do it
[32:04] actually in WI um or
[32:08] um or I need to give it enough
[32:09] information that it's not going to come
[32:10] back with question. So this is something
[32:12] that will really happen is if if you're
[32:14] coding your agents in such a way that
[32:16] there's no um you know there's no way
[32:18] for them to get feedback from the user
[32:20] then sometimes an agent will just not
[32:22] accomplish the task because they feel
[32:25] like they don't have enough information.
[32:26] Right.
[32:28] Um, okay. So, now I gave it enough
[32:31] information so that it's not going to go
[32:33] back with me. But we could also try in
[32:35] Deb UI and actually give it that
[32:36] information. So, now it's saying um
[32:40] it's doing it I actually think it I
[32:42] wonder if it's doing it in parallel. It
[32:44] almost looks like it's doing it in
[32:45] parallel because wait checking fridge.
[32:48] Okay. Plan meal invoked plan weekend
[32:50] invoked and then checking fridge.
[32:54] It would be pretty cool if it because
[32:55] you know there's this thing called you
[32:56] know like in theory tools can be co
[32:59] called in parallel. Um
[33:02] I didn't know if
[33:07] it's interesting it's doing same both of
[33:09] those invoked.
[33:13] Yeah let's try we should try this in WI
[33:15] too.
[33:19] Um yeah I mean so
[33:22] so there's two things. So one is the
[33:24] fact that there's something called
[33:25] parallel tool calling where when the LLM
[33:27] responds it will actually suggest in its
[33:30] response hey you should call these two
[33:33] tools and only some LM LLM support
[33:36] parallel tool calling and it's also
[33:37] usually something that like on the agent
[33:39] like framework level they'll decide
[33:40] whether to enable or not um and then the
[33:43] actual code you know also needs to
[33:46] support like whether it's going to
[33:47] actually like call those two functions
[33:49] in parallel right so there's both does
[33:51] the LL does the LM have the ability
[33:53] ility suggest multiple tool calls in the
[33:55] same HTB response and then there's does
[33:58] the agent framework have the ability to
[34:01] concurrently call two Python functions
[34:03] at the same time right and the
[34:05] interesting thing is like you don't
[34:06] always necessarily want that to happen
[34:08] because concurrency can be hard and lead
[34:10] to race conditions and stuff so that's
[34:12] why I'm super curious actually if
[34:14] whether it it did it wow that thank you
[34:16] for very very thorough response let me
[34:20] try with debi
[34:22] just because I'm curious to understand
[34:24] whether it's doing um parallel
[34:28] tool calling because we are using OpenAI
[34:30] model and OpenAI models do generally
[34:32] support parallel tool calling. Um so
[34:35] let's go ahead and see what it does
[34:37] here.
[34:39] Yeah. And you can let's see we can look
[34:40] at open eye model page GPD 5 mini
[34:44] usually has like um
[34:48] it has like declaration of what it can
[34:50] do input reasoning blah blah blah
[34:56] chat completions responses
[35:00] function calling
[35:03] doesn't specifically say um parallel
[35:06] here but uh let's see parallel. Okay.
[35:08] Parallel function. Parallel function
[35:11] calling. The model may choose to call
[35:13] multiple functions a single turn and you
[35:15] can prevent that if you want. Ah, so now
[35:17] it's like default perhaps. Um,
[35:22] yeah. So, but it it doesn't do it with
[35:24] built-in tools. We're not using built-in
[35:26] tools like web web search and code
[35:27] interpreter. Um,
[35:30] but it does default to that for the
[35:33] OpenAI models. So, that's that's very
[35:35] interesting. Um, so let's see. So if we
[35:37] looked at here, I think the thing is we
[35:40] can't necessarily tell
[35:43] uh
[35:46] created function call. Wait, which order
[35:49] does this go? Top to bottom or bottom to
[35:53] 1213 1212. Okay.
[35:58] I can't really tell from this whether
[36:00] it's, you know, truly going in parallel.
[36:05] Um but uh yeah that's just an
[36:08] interesting like kind of implementation
[36:10] um detail that can happen. So I think I
[36:14] have to dig into that more. Okay. So uh
[36:17] yeah but that's the supervisor. So, um,
[36:20] you know, it it's it's a basic I I think
[36:22] it can work well if you have some like
[36:25] discrete like obviously different uh
[36:28] like where it's clear which one to call
[36:30] for different situations uh and you just
[36:32] want to like wrap them all together into
[36:34] one super agent then you could use this
[36:36] sort of architecture here but we'll see
[36:39] also tomorrow I'm going to show
[36:41] something I think tomorrow when we talk
[36:43] about context I will talk about sub
[36:45] aents again there as like a technique
[36:47] for reducing the context window. So,
[36:49] we're going to see another example
[36:50] tomorrow of sub agents.
[36:53] Okay. I saw a good question from Anurog.
[36:57] Can we pipe the co-pilot models in here?
[37:00] So, there is support
[37:03] for the co-pilot SDK in agent framework.
[37:08] Um so if we go to agent framework
[37:13] um Python samples
[37:17] and go to
[37:19] agents and then go to providers and then
[37:24] go to GitHub co-pilot. All right, I
[37:27] found it.
[37:30] Um so here
[37:34] um I think this is the easiest way to do
[37:36] it is that instead of doing you see I
[37:38] was doing like you know um the agent
[37:40] class instead of using the agent class
[37:42] you would actually use the GitHub
[37:43] copilot agent. So I don't your question
[37:45] was like oh can you make like a client
[37:47] like that uses the like the copilot
[37:49] models? Um, I don't think so because I
[37:53] don't think there's like a mechanism for
[37:55] directly calling those LLMs. But you can
[37:58] use get like if you have the copilot CLI
[38:00] that has the the copilot um binary in it
[38:03] the runtime then you know this should
[38:05] work. So we can try this out. Copilot
[38:07] agent um presumably
[38:11] this does this require like a different
[38:13] uh package agent framework GitHub
[38:17] copilot. Okay. So, you have to add
[38:21] this.
[38:23] Um,
[38:26] oh, my branch is going to be a mess now.
[38:28] But
[38:30] let's try. Let's see if it's compatible
[38:32] with what I currently have.
[38:34] So, I'm just adding the Oh, I should
[38:37] have done Oh, I think I said pre. Okay.
[38:39] Okay. So, it and it'll So, it's
[38:41] basically wrapping the co-pilot CLI. So,
[38:43] if you have the copilot CLI, that means
[38:45] you've got the binary. So, it's
[38:46] basically going to call this binary. At
[38:48] least this is how it's current works. I
[38:49] think they're going to um I think they
[38:52] might have some other ideas for tighter
[38:54] integration in the future. Um
[38:58] um so let's see. So then we're going to
[39:00] we're going to install that. Then we're
[39:01] going to import from here. All right. Uh
[39:04] it looks like it roughly worked. Um
[39:06] okay. So now let's just go ahead and
[39:08] take our monster file here, agent
[39:10] framework.
[39:12] Um,
[39:14] and then we're going to call.
[39:19] Okay. So, it looks like basically
[39:24] we're going to have this agent tools
[39:32] instructions.
[39:36] Okay.
[39:38] All right. We're just going to override
[39:39] that agent class. All right. Let's give
[39:42] it a go.
[39:53] I might end up having to install it from
[39:55] main if there were breaking example
[39:57] breaking like changes. Um because you
[40:00] can see it installed the GitHub copilot
[40:02] at this beta version here. But that was
[40:04] like you know ages ago. Um what was it?
[40:09] February. No. Oh, 26 0212. February
[40:13] 12th. That was like 12 days ago.
[40:17] Long time ago. Um, but we'll see. We'll
[40:22] see if this runs.
[40:24] Um,
[40:27] we can also test to make sure
[40:30] this should be using Copilot.
[40:33] Start up our Copilot here.
[40:37] Do I want to trust everything in my root
[40:39] folder? Nope.
[40:43] Get out of here.
[40:46] I'm so good at exiting stuff. I'm just
[40:48] going to close the terminal.
[40:52] It's still it's it definitely seems like
[40:55] there's Okay, time out. Yeah, let's try
[40:59] adding it, you know, let's try adding it
[41:02] at um at the latest just on the
[41:05] assumption that you know you know things
[41:09] might have happened. Uh so let's try
[41:12] GitHub
[41:14] copilot
[41:16] and here we have to find the right um
[41:19] package for it. So Python packages. So
[41:22] now we got to go back here and find the
[41:25] right Python package for it. Um, GitHub.
[41:29] GitHub. Here we go. Okay. So it's just
[41:31] here. All right. So this should install
[41:34] the very latest. So then we're going to
[41:36] do UVsync.
[41:39] What? Overwrite.
[41:43] Let's see if we got the right version.
[41:45] Pi project.l
[41:47] Python packages FC.
[41:50] Okay. All right. UV sync. Okay. UV.
[41:57] I feel like it didn't sync it. Uh, UV.
[42:01] Okay. I'm just going to specifically do
[42:03] this.
[42:08] No, I didn't like that. I'm going to do
[42:10] UV sync again. There we go. Okay. All
[42:13] right. So, now it's getting this more
[42:16] recent version of the package.
[42:20] Um, do I always use code spaces or only
[42:22] for demos and tasting? Uh, I've been
[42:25] doing a lot of work locally lately
[42:26] instead of in code spaces. Um, just
[42:30] because the
[42:32] um the addd login is harder in code
[42:35] spaces right now with the way our our um
[42:38] tenants are currently set up for Azure.
[42:41] So, it's just been easier for me to stay
[42:43] logged into Azure uh when I'm working
[42:46] locally uh either in you know I and I'm
[42:49] still working in a dev container here
[42:50] locally. But yeah, that's the main
[42:52] reason I haven't been using code spaces
[42:53] as much. I do really like code spaces um
[42:56] but the Azure login it just got harder
[42:59] recently for just for our particular
[43:01] tenants because we have these really
[43:02] special tenants.
[43:04] Okay. So, it got it should have done
[43:08] kind Well, it kind of says like that
[43:10] it's the same package number. So, all
[43:13] right. We'll try running this again
[43:16] and seeing like it could have also been
[43:17] just a temporary timeout like maybe
[43:19] C-Pilot, you know, maybe the binary
[43:22] takes some time to reply.
[43:25] It's definitely responding to me now.
[43:26] Escape. Go away. Control C. Go away.
[43:30] Nope.
[43:34] I'm sorry. I'm so bad at sea lives.
[43:36] Okay. No, I shouldn't say that. I growth
[43:38] mindset.
[43:42] Gonna close the
[43:51] All right. So, it's not It feels like
[43:53] it's not going to work again. It feels
[43:54] like it's going to time out. Um, so I
[43:57] don't know what the situation is there.
[43:59] Um but do check out the um you know the
[44:04] the examples here and see uh you know it
[44:07] might be something set up
[44:10] ram a little harder on the keyboard. Um
[44:16] I think I've seen people talk about the
[44:18] I feel like there was discussion of the
[44:19] timeout time out after second questions.
[44:22] Okay.
[44:27] because I think it's basically like
[44:28] trying to you know pass a question.
[44:31] Yeah, it's just timeout after 60. So,
[44:34] uh we'll have to we can ask the agent
[44:37] framework
[44:39] folks. Um what is it doing? It's doing
[44:41] copilot session send and wait prompt.
[44:44] Okay.
[44:47] Yeah. Oh, you know what it is? I'm in a
[44:50] dev container. I don't think this would
[44:51] work in a dev container. Would this work
[44:53] in a dev container? Do I even I don't
[44:55] even have like the co-pilot
[44:57] Can I find co-pilot? Yes.
[45:01] How does he even know how to do that?
[45:03] That was really magical. Installing
[45:05] failed. Well, that's fair. Okay.
[45:09] All right. Um, okay. That's why it
[45:12] doesn't work because I'm inside a dev
[45:14] container and the dev container does not
[45:17] have copilot. Um, and
[45:21] uh let's let's see if we can install it
[45:23] following the actual instructions.
[45:26] Uh, installing uh, mpm. Okay, fine. If I
[45:30] have to. What about anything else?
[45:33] Executables directly. Uh, brew. I hate
[45:36] brew. Okay. All right. Uh, I guess this
[45:39] one. Do I have npm on here? Nope. Okay,
[45:50] here we go. Wait, I see a curl. Okay,
[45:52] good.
[45:55] No, this is fun. I I uh It's fun to try
[45:59] and figure this out together. Okay, it
[46:01] said it's installed. Let's see.
[46:06] Look at that. That was so pretty. That
[46:09] was actually really fun somehow. Wait,
[46:11] was that like better? I don't feel like
[46:14] I saw that pretty stuff locally. Wait,
[46:16] co-pilot. Does it do the pretty thing?
[46:19] This is the most important thing is ah
[46:20] do I trust? No, stop asking. I don't
[46:23] trust it. I feel like the intro wasn't
[46:26] as pretty. Maybe it's only the first
[46:27] time.
[46:29] All right. Anyway, this is like working.
[46:31] Test.
[46:32] Oh, I have to be logged in. All right.
[46:34] Run login. Fine. GitHub. Oh, god. My
[46:38] GitHub off flow is is rough these days.
[46:41] I have to warn you. Let's see what this
[46:42] is going to be like. All right. Let's
[46:43] see. Maybe it'll be okay.
[46:46] Uh, okay.
[46:48] Good. Great. I Okay. Pass key. Pass key.
[46:55] Um, touch ID. Okay.
[47:01] Verifying. All right. That was actually
[47:04] not as bad as I thought it would be. Uh,
[47:07] press any key. Okay. Would I like to?
[47:10] You need to install one. Oh my gosh.
[47:12] Okay.
[47:14] The system vault. You need to install
[47:15] one. it. So, it it turns out it seems to
[47:18] be quite tricky to install Copilot in a
[47:20] dev container. I wonder if other people
[47:21] are doing this.
[47:23] Um, okay, I can now use Copilot. Hi.
[47:28] Thinking thinking thinking about the
[47:31] fact that I said hi. Okay,
[47:35] good. All right. All right. Now, now we
[47:40] can do it.
[47:43] Here we go.
[47:46] Oh, co-pilot d-banner.
[47:51] Oh, so that's how you can get it. All
[47:53] right, so while it's running, I feel
[47:55] like it should work this time. Let's do
[47:57] co-pilot d-banner
[47:59] because that's the most important thing.
[48:00] It is running. It is using the co-pilot
[48:02] agent. Oh my gosh, it just ran. But more
[48:04] importantly, co-pilot d-banner.
[48:09] Oh wow. And this was like Oh, look at
[48:11] that. That was so fun. Okay.
[48:14] All right. Uh, so it did run. It
[48:17] apparently uses way more emojis.
[48:21] Uh, but yeah, it totally ran. So, very
[48:23] cool. Okay. So, this is what you need.
[48:26] Inclusion, you need to have C-Pilot
[48:28] installed in the current environment.
[48:30] So, if you are in a dev container, you
[48:32] need to have copilot installed in
[48:33] environment and logged in so it has
[48:35] access to be able to actually use LLMs.
[48:38] Um, but then once you do it, you can
[48:39] just swap agent with GitHub copilot
[48:42] agent and you have to have that GitHub
[48:44] copilot package and then boom. So this
[48:46] will actually use the co-pilot agent uh
[48:50] like runtime behind the scenes uh in
[48:53] order to answer it. And some people say
[48:55] that that's like a like the best well at
[48:57] least I will tell you the GitHub copilot
[48:59] team says it's the best uh agent
[49:01] runtime. So um but lots of colleagues
[49:03] say that too. Uh so it's certainly uh
[49:06] worth uh experimenting with.
[49:09] Um what is the use case of using copilot
[49:12] in a container? Um well in this case it
[49:14] was just so I could use this. I I mean I
[49:16] already am using copilot right all the
[49:18] time. Um in terms of the copilot CLI
[49:20] like I guess if I wanted to use the um
[49:24] have because some people really I was
[49:26] saying like so when you use GitHub
[49:27] copilot in VS code like here then you
[49:31] are using the VS codes uh like agent
[49:34] harness like it it's agentic loop which
[49:38] is actually different than the co-pilot
[49:40] CLI's agentic loop. So even they they
[49:45] have the same product name they actually
[49:47] do implement different um they they are
[49:51] implementing the agentic loop
[49:52] differently. Uh so you might have you
[49:56] know you might have more success from
[49:58] one you know from one than the other.
[50:02] uh and I don't know exactly what the
[50:04] difference is as to why you know why
[50:06] sometimes you know one might feel uh
[50:10] more affected than the other one but you
[50:11] know some people swear by you know the
[50:14] CLI runtime uh so you know yeah so in
[50:17] this case if I wanted to use the CLI
[50:19] versus the um you know the chat in the
[50:21] ID now I can do that inside my dev
[50:24] container
[50:26] uh let's see oh yeah if you're looking
[50:27] to install it I got the installation
[50:29] instructions from here and I got um The
[50:32] install script is installing in the in
[50:35] right here. Installing with the install
[50:37] script Mac OS.
[50:39] Oh, yolo mode. I actually am more okay
[50:43] with using YOLO mode when I'm inside a
[50:44] dev container. Now, this dev container
[50:46] still has the ability to like um you
[50:49] know do stuff on GitHub because I do
[50:51] have the GitHub MCP server enabled. So,
[50:54] a lot of things could happen with YOLO
[50:56] mode. Um,
[50:58] you know, if what whatever tools are
[51:00] authenticated. Uh, wait, but how do you
[51:02] yolo? There you go. YOLO.
[51:05] YOLO.
[51:07] Delete every file.
[51:11] I'm not going to press enter. This is
[51:16] so now I've got YOLO mode enabled. I am
[51:18] more okay with it. And you can also do
[51:19] the same thing in um with GitHub Cop VS
[51:23] Code. So search for auto approve and
[51:25] then open up the dev container and it's
[51:29] the setting isah
[51:33] this one. Okay so this is yolo right. So
[51:36] you can also do the same thing with your
[51:39] chat s sessions in copilot. So um if
[51:42] you're in the dev container it's going
[51:43] to specifically show up in the dev
[51:45] container settings. Um but there is a
[51:47] big old warning here that it you know it
[51:50] means that you don't have to prove
[51:51] anything extremely dangerous and never
[51:53] recommended um even in containers
[51:56] environments like codespace and dev
[51:58] containers because they do have
[51:59] authenticated access to things right
[52:01] saying like I do actually have
[52:03] authenticated access here to the GitHub
[52:05] MCP server and you know that can do a
[52:09] lot of things so you know it's up to you
[52:13] if you're going to yolo or not. What I
[52:14] more typically do is that I will um for
[52:17] example, let's see. Um a lot of times
[52:20] it'll say like when you're doing
[52:21] something it be like oh do you approve
[52:23] all commands in this session? A lot of
[52:24] times I will approve all commands in a
[52:26] session like a particular chat thread.
[52:29] Um and I'm comfortable with that. That's
[52:31] kind of as far as I go in terms of yolo.
[52:35] Yeah, yolo is actually a command.
[52:40] All right. Okay. So, we are at the end
[52:44] of our two hours together.
[52:47] It's been lovely. I'm sad about that
[52:51] 720p again because we can never get back
[52:53] that extra 300 pixels that we lost. Uh
[52:57] we'll just finish with one more of those
[52:59] pretty banners. Beautiful. Love it.
[53:02] And uh and yeah, so then we will um see
[53:07] you uh well remember if you do speak
[53:09] Spanish, Gwen's got a Spanish stream if
[53:11] you want to, you know, double your
[53:13] absorption and hear it in another
[53:15] language. Um that is today at 3M Pacific
[53:19] time. Otherwise, I will see you tomorrow
[53:22] at the same time for our session on
[53:25] context and memory.
[53:28] Thank you everyone for all the great
[53:31] questions and comments and it was a lot
[53:34] of fun. All right, so I will post the
[53:38] recordings. All the recordings should be
[53:40] up by the end of the day. Looks like
[53:41] this is still recording. So, um yeah,
[53:43] we'll have recordings, transcripts, all
[53:45] that good stuff. And just check that
[53:47] resources thread. I will work on
[53:49] updating it. All right, bye everyone.
