[00:00] Welcome everyone to our weekly Python
[00:04] plus AI office hours. As usual, I've
[00:08] collected a lot of news from the last
[00:10] week and things that both Microsoft and
[00:14] industry and myself have been doing so
[00:17] that we can talk about them and explore
[00:20] whatever folks are the most interested
[00:22] in.
[00:24] Uh so
[00:26] let's see where to start.
[00:30] Um so Microsoft decision one. So let's
[00:34] start. We can start with decision
[00:36] decision models. Uh so we came out with
[00:39] this decision one. Oh, you've been using
[00:41] it. Okay. Justin says he's been using
[00:43] decision one. All right. Tell us Justin,
[00:46] what are you using it for? Um, I
[00:50] actually I just like set up my
[00:53] uh tenant today so that I could
[00:55] hopefully be able to try it out. Let's
[00:58] see. I have a new account this morning.
[01:00] Dang it.
[01:02] Yeah. Okay. [laughter]
[01:05] Let me [clears throat] see if I can
[01:06] access it another way. Um,
[01:09] we get new Azure tenants every three
[01:12] months, which makes everything very
[01:14] interesting. All right, let's see if I
[01:16] can make a foundry resource. Blah blah
[01:18] blah. Uh, create new BFI
[01:23] foundry. Okay.
[01:27] Uh, PF foundry resource.
[01:33] Okay, sure. Region East US is a bad one
[01:36] to do. Let's do
[01:38] West US3, I think. Okay, let's see.
[01:44] Maybe West US2
[01:46] and PFI
[01:48] [clears throat] Foundry project.
[01:53] Okay, let's see if it's going to let me
[01:55] make this. All right, so Justin says
[01:57] he's using it right now to help select
[01:59] reasoning before running the task, but
[02:01] you're going to use it for much more.
[02:03] All right, and were you Justin, were you
[02:05] using it? Like, have you compared it to
[02:07] something else we're using? We're using
[02:08] Jeb, we're using a smaller model, we're
[02:11] using structured outputs, or is this
[02:13] just a brand new uh workflow that you're
[02:16] using it with?
[02:18] Um, ah, so before you were all using
[02:21] always using extra high. Wow.
[02:24] Uh, that is
[02:26] that's really high. [laughter] I was
[02:28] told some people say you should never
[02:30] use extra high because that's just for
[02:31] the benchmarks and sometimes extra high
[02:34] like over things. I've definitely seen
[02:35] in some of my evaluations that XHI will
[02:37] overthink on some things. Um, but hey,
[02:40] if XHI was working for you. All right,
[02:42] so here you can see Ooh, interactive
[02:45] graphs. That's nice. I didn't know we
[02:46] could do that on this blog. Um, so they
[02:49] definitely worked on the latency.
[02:52] So the latency is quite good. Um, the
[02:57] accuracy is not as high as Jeb, it says.
[03:01] Uh, or at least Okay. Calibration. Wait.
[03:04] I don't quite understand calibration
[03:06] versus
[03:08] 100 equals perfect. Okay,
[03:12] interesting. All right, so there's
[03:14] calibration, which seems related to
[03:16] quality, but then there's accuracy,
[03:18] which is related to benchmarks. Um, now
[03:21] of course with benchmarks, you know, you
[03:24] always have to be worry about
[03:25] benchmaxing. Um, but they do tell you
[03:27] something, right? And so they did not
[03:30] compare it noticeably. They did not
[03:32] compare it to the OpenAI decisions API
[03:34] because that was the other piece of
[03:35] relevant news is that the OpenAI
[03:37] decisions API
[03:39] did come out on openai.com.
[03:42] Um so that's another thing to compare
[03:45] things to. And what this does, it uses a
[03:47] version of Luna that has constraint
[03:50] decoding enabled. Um, so that makes it
[03:54] be so it has reasoning turned off and
[03:56] then constraint to to decoding enabled
[03:58] on the inference and I'm not an ML
[04:00] expert but um I'm told that's how they
[04:02] did it in order so that they could get
[04:04] very fast uh results right
[04:08] uh so oh and it's multimodal that's what
[04:11] people really like about the openi
[04:12] decisions one I don't know what this one
[04:14] is decision one multimodal
[04:18] multimodal image okay I don't see
[04:20] anything that indicates that decision
[04:22] one is multimodal. So I think that means
[04:25] that if you want a no, Justin says no.
[04:28] Okay. So if you do want a multimodal
[04:33] uh option then decisions I API is one to
[04:37] go with. We do not have that on Azure
[04:41] yet. I have asked the team about that
[04:45] but I haven't heard back. Usually we do
[04:49] you know we do try to follow suit um
[04:52] with um you know what OpenAI makes but
[04:56] since this is a brand new API endpoint
[05:00] uh that does definitely take more effort
[05:02] to support right um okay so
[05:07] yeah so let's see did I manage to create
[05:09] a All right so let's see if I can
[05:12] actually
[05:14] test it out in the
[05:19] boundary portal here. Don't know if it's
[05:22] going to let me or not. Okay.
[05:26] All right. I have to figure out why we
[05:28] can't access it. Um
[05:32] uh that's what I get for getting a new
[05:33] tenant today. Okay. All right. So,
[05:36] anyway, Justin's been playing it with
[05:37] it. So, definitely check out decision
[05:40] one. It does have like a whole different
[05:41] endpoint. Um so, here's the
[05:44] documentation for it. Uh so you know
[05:47] currently
[05:49] you you'd have to use this you know you
[05:53] can't just swap it in it's with your LLM
[05:56] code because it uses a a different type
[05:58] of API right so here uh you can see that
[06:03] you send in the state you send in the
[06:05] questions you want to ask and each
[06:07] question has a type so null sorry null
[06:11] comes from I I listen to the podcast
[06:13] about Jev uh so it looks like we're
[06:16] using the same types as Jeb. N comes
[06:18] from Bernili probability. Um so you can
[06:21] also think of as a boolean with a
[06:24] probability. Uh so you use that when you
[06:26] want a boolean but you'll also get
[06:28] probability. So every time with these
[06:30] decisions APIs you'll get back
[06:31] probabilities. Uh and then you can like
[06:33] set thresholds.
[06:35] So new is our you can also think of as
[06:39] like p bull pro bullying with a
[06:41] probability. So you have the question
[06:43] and then you have the criteria for
[06:45] whether it should be true or false. Um
[06:48] and that's optional there. And then we
[06:50] have choice and you know that's multiple
[06:54] multiple choice basically. And then you
[06:56] have score and score is okay. So place
[07:02] an item on an ordered scale. Oh okay. So
[07:06] it's like labeled scoring. I didn't
[07:08] realize that. The return score is the
[07:09] probability weighted average of the
[07:11] level indexes
[07:13] and the result can fall between levels.
[07:15] Okay, so it'll do like zero, one, two,
[07:17] three and then you should validate
[07:20] scores on your own labeled examples.
[07:23] Very interesting. Okay.
[07:26] Um
[07:29] so okay and we have it available in
[07:33] global standard and then some of our
[07:35] regions. All right. So you deploy it and
[07:38] then
[07:39] you call it with this endpoint here. You
[07:42] send that information. Uh and it looks
[07:46] like we don't have
[07:48] an STK for it yet. So we're just using
[07:52] the URL lib package. Uh you can send
[07:55] multiple decisions at once. So this is
[07:56] what's you know what people love about
[07:58] Jev is the the latency really fast and
[08:01] the ability to do these multiple
[08:03] questions at once. So where we have the
[08:05] same thing here where we can send out a
[08:06] bunch of questions and all of them will
[08:08] come back with um their answers and
[08:11] their probabilities.
[08:14] Uh okay so Patrick says could someone
[08:17] explain when a decision model is being
[08:18] used? Like you're saying like when
[08:20] should you use it? Um so you know good
[08:24] use cases are oh here actually there's
[08:26] lots of examples here. um you know
[08:28] routing. Lots of people are using it for
[08:30] routing because a lot of times you you
[08:32] know you want like people want to put a
[08:33] router in front of a step but they don't
[08:35] want to right now because of the added
[08:37] latency but now you know because it's so
[08:39] fast you know now it's potentially easy
[08:41] to add a router in front. The thing to
[08:42] always keep in mind with routing is that
[08:44] your router should do a good job. If you
[08:46] have a bad router that's worse than
[08:47] having no router at all perhaps. Um oh
[08:50] and that leads oh sorry the next one
[08:52] also said you know model model model
[08:54] routing right? So, you know, people
[08:56] always debate about model routing and
[08:58] whether, you know, it's good or not. So,
[09:00] you really got to evaluate whether it's
[09:01] worth it to add, you know, a routing
[09:03] step in front of something. Um, you
[09:06] know, a lot of the PL so classification,
[09:08] you know, marking something as spam,
[09:10] right? Like Twitter right now should
[09:12] really be using some sort of better
[09:14] models to decide whether something is AI
[09:16] slop because man, Twitter's like all AI
[09:18] slop right now. So any sort of
[09:20] classification a lot of use cases were
[09:22] using structured outputs before if the
[09:24] outputs were all entirely you know
[09:27] boolean or choice or score then you
[09:29] could move to these decision models if
[09:31] your outputs also included free text
[09:33] then you couldn't use move to a decision
[09:35] model right um you know intent analysis
[09:39] that's like routing LM is a judge I've
[09:41] seen a lot of people using it for LM as
[09:43] a judge so if you're if you have an
[09:45] evaluation pipeline a lot of people are
[09:47] swapping in these models just to have
[09:49] much faster egos. And that's really
[09:51] helpful because when you're setting up
[09:52] evaluations, you potentially want to
[09:53] evaluate like hundreds of, you know,
[09:56] examples from your uh ground truth data
[09:59] set and it takes forever, right? So, I
[10:01] would be really excited about LLM as a
[10:03] judge. Um, you know, you want to
[10:05] calibrate that against human scores, but
[10:08] you know, potentially could really speed
[10:10] up evaluation pipelines.
[10:13] Uh, let's see, recommendation search
[10:16] relevance. So yeah, it reminds me quite
[10:18] a bit of a reranking model, right? So uh
[10:21] like our semantic reranking model for
[10:22] Azure AI search will look at each of the
[10:25] results and give them a score. So you
[10:27] could imagine you could implement a
[10:29] reranker model using this. Now reranker
[10:33] models are specifically trained to do
[10:35] reranking um you know versus this model
[10:38] which is a very you know a very generic
[10:40] one but it's worth like trying out
[10:42] right. So, um, you know, you could try
[10:45] re-implementing a reranker using that.
[10:47] Maybe we'll actually for one of our
[10:48] Ignite sessions, we're going to like
[10:50] reimplement Azure AI search from
[10:53] scratch. Maybe we'll maybe we'll use the
[10:55] decision model to compare it. Um, safety
[10:59] and security screening like in a coding
[11:01] agent might decide about risk levels.
[11:03] This was something that um, also the Jeb
[11:05] founder talked about in the podcast. Let
[11:07] me link to the podcast. Here we go. Um,
[11:12] so this is
[11:14] uh the founder.
[11:17] Um,
[11:20] he's super fun. He's very interesting.
[11:23] Uh, but he talked about a lot of
[11:24] interesting things. And one of the
[11:25] things he was talking about like safety
[11:26] and security screening, right? He was
[11:28] saying like, you know, you're, you know,
[11:29] all of your safety screening should be
[11:31] determined by um, you know, something
[11:35] more deterministic than like just a
[11:37] prompt, right? So you could be using
[11:39] these models for it. Uh robotics, I I
[11:43] did talk to OpenAI folks and they were
[11:46] about to do a robotics demo for their
[11:48] decisions API and they said it worked
[11:50] really well with the botic robotics the
[11:53] the micro duck. If you saw the micro
[11:54] duck from hugging base, right? So at the
[11:58] opening I dev day um they had this let
[12:02] me find the actual micro duck. Uh this
[12:05] one. Yeah, this is so cute. I feel like
[12:07] I might need to get it for Christmas.
[12:09] Uh, so they hooked this up to the
[12:12] opening eye decisions API and they said
[12:15] it was really good at, you know, really
[12:17] fast way of deciding what the robot
[12:19] should do next. So that would be another
[12:22] fun use case.
[12:25] Uh, so God, it's so cute. Um, okay.
[12:31] Yeah, so lots of lots of interesting
[12:34] scenarios to think about. Um, a lot of
[12:36] them are scenarios you're probably
[12:37] already, you know, thinking about using
[12:39] LMS for like smaller LMS or other
[12:42] models. Um, but this just makes them
[12:43] more practical
[12:45] because of just how fast and cheap it
[12:48] could be. Uh, so Justin says his next
[12:51] will it work is if it will classify
[12:52] tickets in your PSA. Yeah, so
[12:54] classifying tickets any sort of
[12:55] classification. In fact, a lot of people
[12:57] when the Jev model came out there, you
[12:59] know, everyone's like, oh, it's a new
[13:00] kind of model and people are like, no,
[13:02] it's a classifier model, right? So, you
[13:04] know, there's some people just basically
[13:05] calling it a classifier model.
[13:08] So, Pablo says, "How relevant would the
[13:12] 32K
[13:14] context be for those applications? And
[13:16] how does it compare with the compared
[13:18] models?" Oh, I didn't even notice that
[13:20] it's 32K. Is that Is that what it says?
[13:23] 32.
[13:25] Where did it say it was 32? Over here.
[13:27] 32.
[13:30] Where is the 32K context?
[13:36] Um,
[13:39] okay. Context of Microsoft decision one.
[13:42] I see you're typing. Okay. [gasps]
[13:45] Uh,
[13:47] context window
[13:49] in the Foundry link at the top. Okay.
[13:52] Yeah. Unfortunately, my Foundry is not
[13:54] working so good. Um,
[14:00] So, I can't even open my Foundry at the
[14:02] moment. Maybe I can. Let me try it with
[14:04] a different Foundry.
[14:06] Sign in. Let me try signing into this
[14:09] one. See if I can get into a tenant.
[14:17] Okay, maybe. Let's see. Come on. I've
[14:20] got to get access to something here.
[14:22] Yeah. Yeah. Yeah. Yeah. Yeah. Yeah.
[14:24] Yeah. Yeah. Yeah. Yeah. Just give me
[14:26] just give me something here. Just let me
[14:29] see something. All right. New foundry,
[14:31] all resources. Go me. Okay. I need to
[14:34] like quickly be able to click on
[14:36] discover. Okay. I'm trying to get to
[14:38] that discover link before it kicks me
[14:41] out. Discover. Ah.
[14:44] Okay.
[14:46] Uh, thank you. All right. Thank you,
[14:48] Pablo.
[14:50] All right. So, it said it is 32K. Okay.
[14:54] Um,
[14:56] I'm just going to try this sign in link
[14:58] just to see if I can use it here. All
[15:00] right. No. Okay. Dang it. All right. So,
[15:04] yeah. So, it is 32K. Uh, interesting.
[15:07] So, that's 32K. Um, let's compare that
[15:10] to
[15:12] uh the decisions API.
[15:16] And does it have a context
[15:21] window here?
[15:24] Uh,
[15:27] let's see. It's under the models page.
[15:28] Sometimes you'll see it. Astro, soul,
[15:32] lunar, specialized models, real time,
[15:34] speech generation. All right. Uh,
[15:39] I don't know if they're going to list.
[15:42] It's probably Yeah, they're not listing.
[15:44] So, what is the context window? Context
[15:48] window.
[15:50] Um,
[15:53] pricing availability blah blah blah blah
[15:55] blah.
[15:57] Uh, okay. So, Pablo says, "Jeb 1.13 has
[16:00] 64K."
[16:02] I don't see a context window because it
[16:06] might be that the context window
[16:08] for this one could be the same
[16:11] as Okay. Open the eye decisions API
[16:14] context window.
[16:25] It could be that it's the same as Luna,
[16:27] which you would think would be a higher.
[16:29] All right. The context.
[16:31] No.
[16:35] Um, so I'm not seeing a deter like a
[16:38] definitive source. Uh, here's the actual
[16:42] template. So, we can also try
[16:46] um putting in a huge amount [laughter]
[16:49] I don't know how much context it will
[16:50] let me paste in. Um,
[16:54] generate
[16:57] I need to generate how much? That would
[16:59] be like a lot. Okay. Generate
[17:02] 64k worth of tokens to test a model
[17:07] with.
[17:09] All right. Let me just
[17:13] try that out. Okay. All right. Uh, so
[17:17] yeah. So right now I don't know I don't
[17:20] know we don't know about decisions API.
[17:22] So we see decision one 32k jev 64k
[17:27] uh we're not sure about decisions API.
[17:31] Um so
[17:34] we'll have to see if we can figure that
[17:37] out.
[17:39] Umun
[17:42] oh Justin's typing. Maybe Justin knows.
[17:44] Uh all right. So, I got 64 test tokens.
[17:49] Open it local.
[17:56] All right.
[17:57] So, let's see if I can paste this into
[18:00] here.
[18:02] Okay. Well, it went through.
[18:05] [laughter]
[18:07] I don't know. It might have caught me
[18:09] off after a point. Comp. Is that the
[18:12] last [laughter]
[18:14] uh run decision prompt? No, it sent
[18:17] everything. Okay. Well, that works. Um,
[18:21] what if I did some more? Okay. Okay.
[18:23] Generate 120k and open it. All right. I
[18:28] don't know if it's like I don't know for
[18:30] sure if it's actually
[18:33] really sending everything here.
[18:36] Um,
[18:39] so that you know, uh, let's see. Is it
[18:41] going to give us our token usage?
[18:46] Um,
[18:48] it doesn't show your token usage here,
[18:50] right?
[18:53] Uh,
[18:57] yeah. Let me see. Does it do we have
[18:59] code templates choice docs code? Okay.
[19:04] So here's the code because if we do the
[19:06] code
[19:07] then we should
[19:12] okay
[19:14] all right so let's try this
[19:20] write code
[19:24] in
[19:29] all right I'm just writing the some code
[19:33] to test this out. Uh, let's see. I got
[19:36] to grab a key. I'm going to do that in a
[19:40] separate window.
[19:43] I'm going to move that over there.
[19:45] Create new secret key.
[19:49] Okay.
[19:51] D.
[19:54] All right. Create secret key. Copy.
[19:57] Okay. All right. Now, I've got a key.
[20:02] All right. How do I get
[20:09] where? All right. Uh, I've got my
[20:12] co-pilot writing that code right now.
[20:15] Um,
[20:20] yeah, right now what I'm trying to do is
[20:22] run a test script
[20:24] uh on the OpenAI decisions API.
[20:28] I unfortunately can't run the Azure
[20:30] decisions API at this point.
[20:32] um decisions [clears throat] or we have
[20:34] to get specific. I can't read the
[20:35] decision one model.
[20:38] Okay. So, I'm going to
[20:41] um export the key in my terminal
[20:46] open AI. Okay. Where which full?
[20:50] [clears throat]
[20:54] Okay. I'm just vibing it right now. All
[20:57] right.
[21:00] So,
[21:01] what we're going to do
[21:04] is go here. No, no, no. We're going to
[21:07] CD into this temporary location.
[21:12] This has the rundecision py. Let me make
[21:15] this bigger. Okay, so this will send in
[21:22] the input with the decisions,
[21:26] which makes no sense, but it's okay. And
[21:29] let me just set the key in this
[21:31] terminal. Offscript here. Uh,
[21:35] one sec. Export openi key equals.
[21:44] Okay. Where's my keys? Where's my keys?
[21:48] Here it is. All right.
[21:53] Okay. All right. So, now I've just set
[21:56] my key. Uh, and now I should be able to
[22:00] run
[22:02] this file. Rundecision. py.
[22:08] Run decision. py. Okay, let's see if
[22:11] it's got everything it needs in the
[22:12] environment. I don't know if it has the
[22:14] latest version. Yeah, it doesn't have
[22:17] the latest version of the package. I'm
[22:18] not surprised. So let's do the proper
[22:21] thing and make a oh uh make a Python
[22:26] environment.
[22:29] Uh oh module maybe oh MV sorry make a
[22:34] Python environment
[22:36] um oh yeah you still hear my child voice
[22:40] that my child voice only goes through to
[22:42] you. It doesn't get because I record via
[22:45] Streamyard. Streamyard doesn't hear it.
[22:46] It's just Discord that likes to pipe
[22:48] through, which I guess makes sense
[22:49] because people use Discord for video
[22:51] game streaming, right? So, I suppose it
[22:53] makes sense that by default it just
[22:55] pipes through the audio on a machine
[22:57] because that's like part of the video
[22:58] game stuff. Uh Streamyard doesn't do
[23:00] that. So, um and I don't hear I also
[23:04] don't hear because I mute mine. So,
[23:07] you're the only one that hears my child
[23:10] giggling. Uh enjoy. [laughter]
[23:13] I told the the GitHub copilot app team
[23:16] that they should have an easy way of
[23:18] pausing the hooks or disabling hooks,
[23:20] right? So that you know I could easily
[23:24] turn them off.
[23:26] All right. Uh let's pip install OpenI.
[23:28] That should bring in the latest.
[23:31] Okay,
[23:34] there we go.
[23:36] Brings in quite a lot of dependencies
[23:37] here.
[23:41] Okay, let's run the decision.
[23:46] All right, so we got back um we got back
[23:49] an answer. I want to see like we should
[23:51] be able to get back some sort of token
[23:52] usage, right? Oh, yeah. Let's let's
[23:54] print out like way more about the
[23:56] result. Okay, print decision.
[24:00] I want to see everything.
[24:05] Uh, I am trying the decisions API from
[24:09] OpenI. Here we go. We got it. Okay.
[24:11] Input tokens. Look at that. Input tokens
[24:14] is 95,000. So, we got all the way up to
[24:16] 95,000 at least, right? Um, okay. So,
[24:20] let me say we need higher. So, what is
[24:23] the GP6 Luna? Let's look at because I'm
[24:26] thinking it could just be based off of
[24:28] Luna's context, right? GB6 Luna. And
[24:32] that has a million context window. Um
[24:39] generate a larger file. All right. So
[24:41] let's see how high we can go. Um since
[24:44] that seemed like Yeah. So that would be
[24:46] another advantage. Can I test an image?
[24:48] Yeah. Yeah. Yeah. Let's do an image. Um
[24:51] so here check an image for visible
[24:54] damage.
[24:56] Um
[24:58] let's get the Python for this.
[25:01] That's nice. Okay. So, it's gonna
[25:05] um
[25:08] let's bring in this one.
[25:12] Okay. Uh [clears throat]
[25:15] BI check image. py. All right.
[25:19] [clears throat]
[25:21] And let me get uh the picture.
[25:24] Give me the picture. All right. We're
[25:26] just gonna
[25:28] ah
[25:30] All right, I'm gonna get this. There we
[25:33] go. I wanted that picture.
[25:36] Uh, see if we got the screenshot.
[25:40] Okay.
[25:42] Product.ping.
[25:44] And we're going to move desktop
[25:47] product.ping
[25:49] to here.
[25:52] Okay. So now let's run check image.p py.
[25:56] The cat has come to say hello. Oh. Oh
[26:00] gosh. Cat still has claws. All right.
[26:03] Um, it's Yeah. So, that worked. What was
[26:05] the thing you wanted to test in? I
[26:08] curious to see how it responds. See if
[26:09] it can see. Is it a dog or something? We
[26:11] should do that with my cat. [laughter]
[26:13] A lot of times my things will check if
[26:15] it's a Okay. Um, uh, so this one checks
[26:19] for probability. So, really I like a
[26:21] good test for it would be in my um,
[26:25] uh, the um, what's it called? vision. In
[26:29] my vision repo, I have all of these
[26:31] examples,
[26:33] right? And a lot of these examples could
[26:36] be
[26:38] rewritten using
[26:41] the um decisions
[26:44] API, right? Because a lot of these well
[26:46] like we have the damage one here. Um
[26:49] there's like um this one's like a
[26:52] choice. What's the cheapest plant,
[26:54] right? Oh man, these would be good
[26:56] tests. I'm going to tell it, okay, u
[26:58] port over this notebook to a bunch of
[27:04] Python files based on the new check
[27:09] image. py that I put in the folder. All
[27:12] right, let me sorry show you what I'm
[27:14] doing over here in the folder.
[27:20] uh
[27:23] and
[27:25] copy in the relevant images from that
[27:28] repo.
[27:32] All right. Uh so yeah, it so that's
[27:35] that's really compelling. All right,
[27:36] let's see. Also, did it do Okay, so it
[27:38] did give us a larger file to test on. Uh
[27:41] so let's also go ahead and run it with
[27:45] a larger token thing and see. We should
[27:47] in theory be able to get to a million
[27:49] contexts. Well, how much money is this
[27:51] costing me? All right, we got Yeah, it
[27:54] says input tokens 256. Very nice. All
[27:58] right. Okay. Um, can I do like is there
[28:01] like a BTW? No. Uh, aside. Isn't there
[28:06] something like fork for fork forks the
[28:08] current session? Okay. Oh, they already
[28:11] did it. Jesus, that was fast. Okay.
[28:13] [laughter]
[28:14] It's always [clears throat] like really
[28:15] impressive how fast things can be. Okay.
[28:19] Also generate 1 million token file to
[28:24] test that.
[28:26] All right. So now we've got a bunch of
[28:29] So let's just look at one of the ones
[28:31] that ported over. Inspect the animal in
[28:33] this image. Predicate. Is this a
[28:35] unicorn? Okay, it is not a unicorn for
[28:38] the record. So let's see. Check unicorn.
[28:42] PY is unicorn probability zero. All
[28:45] right, good. Oh, this is gonna be a
[28:48] tricky one. This is actually one that a
[28:50] lot of models will mess up. This is a
[28:51] good test. Um, identify the reptiles in
[28:54] this photo. Are the reptiles alligators
[28:56] or crocodiles? Are the reptiles
[28:58] crocodiles rather than alligators? Okay,
[29:01] let's see how it does. Oh, I should show
[29:03] you the image so you know what I'm
[29:04] talking mystery reptile.
[29:07] All right, let me show you this. It
[29:08] opened over here. Okay, so here is the
[29:10] mystery reptile. You can guess in the
[29:13] chat what it is. Um I know because I saw
[29:16] those reptiles in person and had several
[29:19] nightmares about them. Um okay, so now
[29:22] we're going to run check reptile
[29:26] and it says is alligator probability
[29:29] 0.91 is crocodile probability 0.67.
[29:34] Very interesting. Um, I think I would
[29:36] have intuitively assumed that the
[29:39] probabilities of those would have been
[29:41] adding up to 100, but as we see, they
[29:44] don't. So, that's actually a good way of
[29:46] checking to see like how um, you know,
[29:51] how confident it really is because if
[29:53] it's giving a greater than 50%
[29:55] probability for both of those, then it
[29:58] really isn't that sure, right? Uh, now
[30:01] let's see if any of you had guesses
[30:02] about what is the correct answer here.
[30:05] I'll just wait.
[30:10] I see a lot of folks taping.
[30:14] [clears throat]
[30:17] All right, Justin's going with the
[30:18] decision model.
[30:22] The funny thing, too, is if you do this
[30:24] check in Spanish, it often will do
[30:26] completely um completely different
[30:29] results.
[30:30] Um [clears throat]
[30:32] Oh, right. My Yeah.
[30:35] Can I run it multiple times? Yeah,
[30:36] that's the interesting thing is that
[30:37] these um Okay, these ones it looks like
[30:40] this is being very similar each time.
[30:42] The Jev model does not have a
[30:44] determinism because they're really
[30:46] optimizing for reliability. That's
[30:47] something else they uh or um speed
[30:51] performance and cost. Um they said
[30:54] they're open to adding like a seed
[30:55] parameter. Of course, the new OpenAI
[30:57] models also don't have a seed, but they
[30:59] are doing very predictable.
[31:02] Um,
[31:03] okay. So, by the way, these are
[31:05] crocodiles. So, the decision model is
[31:06] wrong in this case. Um,
[31:10] uh, so yeah, uh, that's interesting
[31:12] because I think if we tried it with
[31:14] usually actually the it usually in
[31:17] English it's correct. It's usually wrong
[31:19] once we go to Spanish because it gets
[31:21] particularly confused by um the fact
[31:24] that in Spanish kaiman is the way of
[31:28] saying alligator but kimon cayman in
[31:31] English is is not an alligator. So it
[31:33] gets like really confused. Um but yeah
[31:36] even in English it's getting this it's
[31:38] getting I would say you know it's
[31:39] getting it wrong. So that's a case um
[31:42] where it did not get that correct. All
[31:44] right let's see check menu vegan. So,
[31:47] this is a uh is there anything on this
[31:50] menu that is suitable for vegans? So,
[31:52] this is just going to be a true false.
[31:53] All right, that's not a very good test
[31:55] because I think it's just going to say
[31:56] yes because I think there's at least one
[31:59] thing on there. Probability 0.45. Yes,
[32:02] not a great test for it. Um,
[32:05] uh, insurance claim is probably a good
[32:07] one because that's the kind of thing you
[32:08] might actually be using it for. Claim
[32:10] states is this damage is due to hail.
[32:13] Um, is this is the damage in this photo
[32:17] consistent with hail making the claim
[32:19] valid? Okay. And uh the answer should be
[32:23] no because I'll show you the car. It is
[32:26] a very very dented car and that would
[32:29] have to be a massive piece of hail,
[32:31] right? Uh so the answer should be no.
[32:35] Dented car.
[32:40] Ooh, dented car. nonutf code. Weird. All
[32:46] right, I'll just send it to it. So,
[32:48] there's something up with that image.
[32:49] All right. Tree color cover loss. So,
[32:51] this would be a graph graph reading,
[32:53] right? Oh, don't look at the [laughter]
[32:56] uh let's [clears throat] look at the
[32:56] check. Tree cover loss. Um, analyze the
[33:00] graph of tree loss cover. Is the
[33:01] tropical zone the one losing the most
[33:02] trees? Oh, I was hoping it would use
[33:04] choice. Let's change that. Can we change
[33:08] Can we change
[33:10] tree cover?
[33:12] Oh, I ran the image as a script. Good
[33:14] point.
[33:16] [gasps]
[33:17] Lost to use choice instead of predicate.
[33:21] Oh, I think the example I gave it was
[33:23] using a predicate. So, it did everything
[33:25] with predicate, but sometimes you want
[33:27] to use choice, right? Um, all right. So,
[33:30] let's check that insurance claim.
[33:35] Uh, oh, invalid value system value must
[33:39] be user. All right. So what did we do
[33:43] here? So we said
[33:46] um so we had system and we had user are
[33:48] you not allowed to have
[33:50] system questions
[33:54] input equals
[33:56] okay input equals roll roll. So there's
[34:00] no system
[34:02] there's no system allowed. Okay
[34:05] interesting. Um, I guess all of these
[34:09] are
[34:10] Let's look at all the input examples.
[34:13] Input RO user
[34:15] input. Input input. All right. So,
[34:19] there's no system prompt allowed. Okay.
[34:22] Um,
[34:26] so let's just let that know
[34:31] on dented R.
[34:37] Here's the docs. Here's the docs. Let's
[34:40] just give it docs.
[34:44] All right. So now let's try it.
[34:52] All right. So, it says probability is
[34:54] zero. Great. Okay. So, that's what we
[34:56] wanted. So, now let's check out that
[34:58] tree cover one. So, now the tree cover
[35:00] one should be more interesting. So, now
[35:02] we're having uh which zone is losing the
[35:05] most trees and we gave it four choices,
[35:08] right? All right. So, let's check it out
[35:11] with four choices and see what we get.
[35:15] Tree cover loss. All right. Tropical
[35:18] 1.0. Yeah. So very good. So it gave
[35:22] tropical 1.0. So that would maybe be a
[35:24] better way of handling the alligator
[35:26] crocodile
[35:28] um
[35:30] and seen right. But it was really
[35:33] interesting to see that the
[35:33] probabilities did not add up to one. Um
[35:36] should we use choice or alligator
[35:40] crocodile too?
[35:47] Check. unicorn URL worked.
[35:53] Um, oh, it says you can add description
[35:56] fields to the choices. All right, so
[35:57] that would be another way of giving more
[35:59] data. So, if we wanted, you know, we
[36:01] could add descriptions. Um, all right.
[36:03] So, now let's try check uh reptile.
[36:08] Um,
[36:12] okay. So, now check reptile.
[36:19] Okay. Wait. Check reptile. Now it's one.
[36:23] Let's check that reptile. All right. So,
[36:26] this time it says Oh, it gave it hints.
[36:29] Cheating. All right.
[36:32] [laughter]
[36:33] Um, you know, it says, "Are the reptiles
[36:35] alligators or crocodiles? Identify the
[36:38] reptiles."
[36:40] Wait, that's weird. It did Did it do two
[36:42] things? Print answers. Okay, so this
[36:44] time Oh, it did both. Okay, so the first
[36:47] one it does is a choice. Are the
[36:49] reptiles, alligators, or crocodiles?
[36:51] It's good. It's always good to give
[36:53] something an out, right? If it gets
[36:54] something absolutely nonsense, right?
[36:56] Generally, anytime you're giving
[36:57] something choices, you should always
[36:59] give it an out. Um, because you have to
[37:02] presume like completely arbitrary input.
[37:04] All right, so we got so we saw both. So,
[37:08] Python,
[37:09] wait, so shouldn't we see the response
[37:11] from that one? Print
[37:15] print answers.
[37:17] Print answers. Print answers is just
[37:19] like floating in space there. What?
[37:23] I think this thing did not write good
[37:25] code. All right, let's actually print
[37:27] the answers.
[37:30] All right, so here we still really
[37:34] thinks it's an alligator even when it
[37:36] got like a good hint, right? So
[37:39] basically, you should not use the Luna
[37:41] model for animal identification.
[37:43] Uh, for some reason, it's not a good
[37:45] model. It's I'm kind of surprised
[37:46] because I've been doing that check with
[37:48] GVD40 Mini like way back. Um, but yeah,
[37:52] I guess maybe it's because of the
[37:54] constraint decoding. I'm not sure. So,
[37:56] you should definitely like check these
[37:58] things for your use case. Um, and see,
[38:01] let's check the plant table one. Okay.
[38:04] Is there any plant in the table priced
[38:06] under 10? Oh, yeah. So, this is one that
[38:09] it couldn't really port to the decisions
[38:12] API because this is one where um I'll
[38:15] show you where I asked what is the
[38:17] cheapest plant, right? So, I didn't I
[38:19] didn't have choices because for this to
[38:21] answer this question, you both have to
[38:23] read um read all the plants on the page
[38:27] and you then have to choose one of them,
[38:31] right? And so, you can't do that's the
[38:32] problem. You can't do free text
[38:34] analysis. So you'd have to if you want
[38:35] to do something like this, you'd have to
[38:37] first send it to an LLM for parsing the
[38:39] text or you'd send to an OCR model. That
[38:41] would be the other option is do an OCR
[38:43] model and then you'd have to then you
[38:46] could still send like you could still do
[38:48] this. So you could do the OCR and then
[38:50] you could send all the choices to the
[38:54] decision model and then ask one of
[38:56] those, right? Um, so you could set up
[38:58] these sort of multiworkflows, but this
[38:59] is an example of something that you
[39:00] can't just directly port this in whole
[39:04] flow to a decision model because it's,
[39:07] you know, it has this one would require
[39:09] free text output, right? And we can't we
[39:12] can't do just free text output.
[39:15] Um, but let's see how it does with this
[39:17] one. Anything I think this is
[39:18] [clears throat] going to be like too
[39:19] easy for it. Python check plant table
[39:26] probability 1.0. Okay, it's correct
[39:28] there. Still sucks at alligators and
[39:31] crocodiles. All right. Uh, well, that
[39:34] was super fun. Um, should check all that
[39:36] with Well, as we saw, there's definitely
[39:38] differences between the models. So, it
[39:40] does look like Oh, I never checked the
[39:41] really, really big. Where's that really
[39:44] huge one million? Okay, so this one,
[39:46] let's just check the context window to
[39:49] see. Nope. Uh, let me Oh, look at that.
[39:53] We finally got to exceed the token
[39:54] limit. So, that probably means we're
[39:56] slightly over one million tokens. Okay.
[39:59] So, what we determined is that the
[40:01] context window is somewhere between 256K
[40:05] and a million. Um, it's probably a
[40:08] million. Like probably this amount of
[40:09] tokens was slightly over um because it
[40:13] did a roughly a rough estimate. But we'd
[40:16] have to, you know, exactly analyze. So
[40:18] that's certainly a much bigger input
[40:20] window than the Microsoft decision one
[40:22] and the Jeb model. So if you have
[40:24] multimodal inputs
[40:27] and or you have long context then really
[40:30] you know of the three your only option
[40:32] is the decision API. Hopefully we'll
[40:34] have that coming to Azure soon so that
[40:36] you can use it from Azure with all the
[40:37] Azure goodness. Um
[40:40] uh but otherwise if you have what did we
[40:42] say 32k input and text only uh then you
[40:46] can try this decision one model. All
[40:49] right I actually have to oh we so many
[40:52] things to discuss here. Um okay I'll
[40:56] I'll like publish these um online
[40:59] because I I have to go now because I was
[41:02] called in for jury duty and I'm supposed
[41:03] to call right now the courtroom to find
[41:05] out if I have to like really really go
[41:07] in. I only have 10 minutes to call. Um
[41:11] Oh, so uh yeah, so lots of lots of good
[41:16] stuff this week. Um and uh thank you for
[41:23] playing around with the decision stuff.
[41:25] Yeah, we really only made it through the
[41:27] first uh point here. [laughter]
[41:30] Uh but I could I can like just publish
[41:32] these on these news links on GitHub
[41:34] pages. Hydrofusion. Yeah, Hydro Fusion
[41:37] is finally made it to the other GitHub
[41:39] copilot services. It was only in CLI
[41:41] first. Uh I have not turned it on yet.
[41:45] Um
[41:46] but that's you can you can try it out
[41:49] here.
[41:52] All right, I got to go call the court
[41:54] now. Um
[41:57] so thank you everyone for joining and I
[42:01] will see you next week.
[42:06] Bye everyone.
