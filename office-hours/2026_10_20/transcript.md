[00:00] Welcome everyone to this week's Python
[00:02] plus AI office hours. As usual, I have a
[00:06] weekly news roundup for some of the
[00:10] interesting things that have been going
[00:11] on across Microsoft and GitHub and the
[00:14] industry and also things that I've been
[00:17] working on. So, you know, I'll hop
[00:19] around uh some of these news items here
[00:22] and, you know, we'll see where the
[00:26] questions and comments take us. So uh
[00:29] yeah, feel free to post any questions or
[00:31] comments in the chat and also you know
[00:34] share any news that I missed uh here.
[00:37] All right. So what do I want to start
[00:39] with? Um Microsoft web IQ actually. Uh
[00:44] so web IQ this is something that we
[00:46] announced at build and when we announced
[00:50] it at build it was only you had to do a
[00:52] sign up form to get access to it. So it
[00:54] was only for select customers. It is now
[00:57] available for all customers. We actually
[00:59] haven't like made a big splash about it
[01:01] because they're waiting for Ignite to
[01:03] make the big splash, but now it just
[01:05] means you can just get started. Now, the
[01:08] getting started process is like a little
[01:11] weird right now because it goes across
[01:13] two different portals. So, there's both
[01:16] an Azure resource that you make in the
[01:18] Azure portal and then you go back to the
[01:20] WebQ portal and then finish it, which is
[01:23] weird. Um, so hopefully that's going to
[01:25] get better. But here you can see I've
[01:27] made if you go to the Azure portal, you
[01:29] can make the Microsoft web IQ resource.
[01:32] And once you've made that, then you go
[01:34] to the web IQ portal and then you know
[01:37] sign into the web IQ portal. And here
[01:40] I'll sign in with my Azure account.
[01:44] And um and then we can see that I have
[01:47] access to web IQ here. So, we've got um
[01:51] web search, video search, browse. I
[01:54] think browse requires special access.
[01:56] So, sometimes some things do require
[01:58] special access. Um
[02:01] news search, image search, places
[02:03] search. Oo, exciting. Auto. Auto. I
[02:06] assumed that was for automobiles, but
[02:08] it's actually um
[02:12] not the case. Multi-answer. So, I think
[02:15] that goes across all of those. Um, and
[02:18] we've got like a little playground here,
[02:20] right? So, you can uh search. So, this
[02:24] one lets me search web videos and images
[02:27] and be like, okay, um,
[02:31] Jev
[02:33] uh, multimodal. Okay. And you can see we
[02:37] don't have access to news. So, a news is
[02:39] also something that requires more
[02:42] access. And then we can see the
[02:43] parameters here. So, how many results
[02:45] you want back, the language of the
[02:46] results, the region, latitude,
[02:49] longitude. That's interesting. So, you
[02:50] can kind of customize and say where
[02:51] you're coming from, uh, and safe search
[02:54] whether that's on or off. Uh, so then we
[02:56] can run this request here
[02:59] and then see the results. So, you can
[03:01] see for each of the results, uh, what we
[03:04] get back is a title, a URL, and the
[03:08] content. Now the content is this is a
[03:11] what's a passage is the kind of content
[03:13] here. So this is actually like basically
[03:15] like a chunk. So you know they've taken
[03:17] the web page they've chunked it up and
[03:19] this is the chunk of the web page the
[03:22] passage that best uh answer this query
[03:25] right. So you won't in in this new
[03:28] version by default you get back passages
[03:31] and not like the entire web page. Um
[03:34] there is an option to get back the
[03:36] entire web page, but that one does
[03:37] require special access, right? So by
[03:39] default with the public version, you'll
[03:41] get back passages. We can see when it
[03:43] was last updated, so that tells us
[03:44] freshness when it was crawled. Um
[03:47] whether it's adult web page, uh the
[03:50] click URL, so that's if you want to have
[03:52] people click through, uh which is good
[03:54] practice, best practice, maybe also
[03:57] required by um the terms. And then I
[04:01] don't know actually what instrumentation
[04:02] suffix is. I haven't looked into that.
[04:04] Uh, right. And so you can see code and
[04:07] it just gives you examples. There's no
[04:08] SDK for this because it's just a really
[04:10] simple HTTP API. Um, there is an MCP
[04:14] server. So I actually have the MCP
[04:16] server configured
[04:18] uh in my I've got it in my C-pilot here,
[04:22] the web IQ server. So that's something
[04:25] that you could add um you know once you
[04:28] have it. Um, I've added it to to my
[04:31] co-pilots. Now, GitHub copilot does have
[04:33] its own default web search. Um, so you
[04:37] know, sometimes, uh, let's see where,
[04:40] you know, you'll have to you might have
[04:42] to say like use web IQ to search for,
[04:46] uh, Jev multimodal support, right?
[04:53] Um, so you know here, oh, sorry. You can
[04:57] hear my my kid giggling. I was like,
[04:59] "Oh, I should turn it off." I was like,
[05:00] "I'm not going to use co-pilot that much
[05:02] today." Um, so you can see it did search
[05:06] the web IQMCP server. And we can see
[05:11] we can see the query that it sent in.
[05:14] Um, the content format is passage. And
[05:17] then the max resulted in one for eight,
[05:19] right? Uh so yeah so the web IQMP server
[05:24] definitely um you know or just generally
[05:26] web IQ uh consider that as an option for
[05:30] your agents if you need to ground your
[05:32] agents in real time results. Uh it's
[05:36] very it's very good. It's very fast,
[05:38] right? Um just incredibly fast, kind of
[05:41] shockingly fast because I'm used to
[05:42] things these days being kind of slower.
[05:44] Um but because you know they've really
[05:47] optimized this for speed it it is really
[05:51] fast.
[05:53] Uh what kind of limitations does web IQ
[05:55] have? Yeah, let's look at the um
[06:00] uh see error handling. So presuming
[06:03] there's like a 429 too many requests but
[06:06] then question what is the time window?
[06:08] Let's see best practices.
[06:12] Um, implement retry logic. Yeah, but
[06:15] what's the actual? Okay, we got
[06:17] languages and regions, MCP server.
[06:21] Um,
[06:26] see,
[06:28] oh, usage. There's usage here. Okay.
[06:31] Daily average. Whoop. Uhoh.
[06:35] Come on. Oh, don't use that part of the
[06:38] thing. All right, let's go back and uh
[06:42] Okay, get started.
[06:46] Okay. All right. So, we have
[06:50] usage. Oh, wait. No, let's not go there.
[06:52] Let's go to account settings, profiles.
[06:54] Okay. Here we go. This is what I was
[06:55] looking for. All right. So, I have a
[06:57] quota limit of 900 queries per minute.
[07:01] So, that is looks like that's what the
[07:04] default is. Let me see if that was
[07:05] something I configured.
[07:08] Um, is that something configurable?
[07:12] Uh,
[07:14] I don't remember ever setting that. So
[07:16] maybe
[07:18] that might be the
[07:21] um maybe that's the default right now.
[07:24] Uh, so I have to look and see if that's
[07:26] something we can um let's see how can I
[07:32] Uh
[07:38] uh they they still need to update this
[07:41] to remove some of the stuff the FAQs
[07:44] about invites.
[07:46] Um all right. So right now it's 900
[07:48] queries per minute. I'll need to ask
[07:50] them what is the strategy for increasing
[07:52] that because I don't I don't see a way
[07:56] of increasing that. Oh, and then also we
[07:58] see 15 queries per second. Okay. Okay,
[08:01] so right now we're seeing 15 queries per
[08:02] second, 900 queries per minute. So
[08:06] that's actually a pretty low quota. So I
[08:08] assume that um
[08:12] you know there's a way Oh, there's a
[08:14] really long FAQ. All right, let's see if
[08:16] this one has it in there. Quota
[08:20] um per app ID quota enforcement quota
[08:24] quota.
[08:26] Uh okay. All right. So, I don't see
[08:29] anything here about how you increase
[08:32] your um your quota. Uh let's see. Also,
[08:37] pricing. Where does pricing go? Oh, the
[08:40] pricing. Oh, I should mention the
[08:41] pricing got cheaper. Um it was I think
[08:45] $12
[08:46] and now it is $7 per thousand calls. So,
[08:49] that is the other
[08:52] uh exciting thing about it is that it
[08:54] has gotten cheaper.
[08:57] Um, oh, and so you were also having
[08:59] getting you were also going to ask about
[09:00] getting throttled by web scraping
[09:02] preventions and captures. You shouldn't
[09:04] get throttled by anything like that
[09:05] because this is already indexed data,
[09:07] right? Um, so there should be there
[09:11] should be no sort of throttling there.
[09:13] Um,
[09:16] it's already in the index. Uh, and then
[09:18] there's the terms of use. So,
[09:21] um, I see also Hutaf said, okay, using
[09:24] Gina. right now to get fresh web data.
[09:29] Um, is there another advantage compared
[09:31] to Gina.ai?
[09:33] Well, I guess let's take a look at the
[09:35] pricing for Gina AI.
[09:41] Um, what is the So, we got reader
[09:44] embedding
[09:46] models your search foundation
[09:49] supercharge rate limit uh reader API.
[09:53] Okay, so this converts URL to LLM
[09:54] friendly text. Okay, so I would argue
[09:56] this is basically just a not the same
[09:58] thing there. The equivalent of this is
[10:00] the um
[10:02] the the browse um but that one does
[10:05] require more access, right? So I think
[10:07] this is the you know the equivalent of
[10:10] GNA.I if you're like literally want the
[10:13] entire
[10:15] uh contents of the page, right? So the
[10:17] URL of the web page, the max length um
[10:19] live crawl, right? it's whether it's
[10:22] actually I guess going to do um you know
[10:25] whether you're going to return index
[10:27] content you're going to crawl it's not
[10:29] there you're going to force it to always
[10:31] crawl uh render dynamic pages yeah so
[10:34] this looks like this is the equivalent
[10:35] of ginai
[10:39] um
[10:41] but uh I believe this requires
[10:45] uh special access right now we should
[10:48] probably make it here.
[10:51] Um,
[10:55] which of these require special access?
[10:58] Uh, that this form is closed. Okay.
[11:01] Yeah. All right. We need to do a little
[11:03] clean up around there. Um,
[11:06] and then yeah, so I think if you're
[11:09] using Git AI that, you know, this would
[11:11] only be a swap in if you were going to
[11:16] change over to using the browse,
[11:20] uh, the browse
[11:23] tool here. Um,
[11:26] but for that, uh, some additional access
[11:29] is needed. It's weird. we should have
[11:31] like a form to request the additional
[11:32] access. So, I'll have to ask about that
[11:34] as well.
[11:37] Um, okay. So, yeah, good questions on
[11:42] web IKEA. I good things for me to follow
[11:45] up on. Uh, there and there's no
[11:48] automatic summary. There is the
[11:49] automatic like chunking, right? That's
[11:51] so you know, it's like a retrieval. Let
[11:53] me find the blog post. Uh, here we go.
[11:56] This is a good blog post about the whole
[11:58] system that they've built.
[12:00] um you know it you know basically it's a
[12:03] search index that is optimized for
[12:05] really fast retrieval to use by agents
[12:09] right and so the what they're giving
[12:11] access to now is the passages you can
[12:13] see here um
[12:16] so passages right so we have the
[12:18] documents they can be a little too long
[12:20] so most of the times you actually don't
[12:21] want to necessarily give the whole
[12:23] document to an agent right uh so instead
[12:26] they bring out use packages and then
[12:30] that becomes, you know, what gets sent
[12:33] to the agent, right? Um, and they've got
[12:38] it really fast latency. Um,
[12:42] and
[12:44] yeah, and you know, it's based off of
[12:46] Bing, but optimized for your agents.
[12:52] All right, so that is uh, web IQ. Oh,
[12:57] let me actually link to it. I didn't
[12:59] link to it, silly. Okay, here we go.
[13:04] All right.
[13:05] Now, um the other thing I wanted to
[13:07] mention is that last week we were
[13:09] talking about the decisions API and I
[13:11] didn't have access to sorry, decision
[13:12] one. Um we did end up using the openi
[13:16] decisions API, but we also talked about
[13:17] Microsoft decision one. I did deploy
[13:19] that in foundry. It is actually quite
[13:21] easy to deploy and then you get like a
[13:23] little playground for it. So you can see
[13:25] here, here's my model. Here's like you
[13:28] pass in the state, you pass in the
[13:30] decisions JSON. And so here you can see
[13:32] I have a a NUL which is like a boolean
[13:35] with probability a choice and a score.
[13:38] And so then we can see the results. Um
[13:41] and it's quite interesting like the new
[13:42] is the easiest one, right? So you know
[13:44] it just says it's 99.7%
[13:48] true, right? So that's like a really
[13:50] high probability that it's true. Uh and
[13:53] then we have let's see choice. So with
[13:56] choice we can see um that it selects one
[14:00] of the choices and it shows the
[14:03] confidence in that choice and then it
[14:04] also shows
[14:07] uh interestingly like I'm a little
[14:09] confused why we see two different kinds
[14:10] of confidence because it shows his
[14:12] confidence in that choice. Oh I guess
[14:13] this would be relevant if there was like
[14:15] even more choices. You would actually
[14:17] see confidence in each of those. So um
[14:22] yeah, so you'll get a breakdown
[14:25] uh for each each option there. Uh and
[14:28] then priority is what's called a score.
[14:30] So here it says how high is priority. So
[14:32] this can do like in between, right? So
[14:36] you're making like this score from here
[14:38] it's like 0 to two. And so it gave it a
[14:40] weighted score of 1.53 and then a
[14:42] confidence for that score. Here the
[14:44] confidence is like really low. It says
[14:46] only like 30% confidence. But that makes
[14:48] sense because prioritization, you know,
[14:50] we know as software engineers,
[14:52] prioritization is like the hardest thing
[14:53] you can ever decide is how how high
[14:56] priority is something. I usually don't
[14:57] even know, right? Even on my own to-do
[14:59] list. Um, now I'm thinking of some high
[15:01] priority to-dos I should do. But, uh,
[15:04] yeah. So, you can see it kind of gave
[15:05] like equal weightage to one and equal to
[15:08] two. And so, it gave this weighted score
[15:10] of 1.53. Yeah. Yeah. And good
[15:12] observation from uh Sam is that uh you
[15:17] know this criteria was not very
[15:19] specific, right? So you'd really you
[15:21] know want to give some more examples
[15:23] here, right? And presumably you could
[15:25] get quite long with this and give a lot
[15:27] more examples
[15:28] um and help it become more confident,
[15:31] right? U but you also don't want to
[15:34] overfit it, right? So that's always the
[15:36] debate is like you know with prompt
[15:38] engineering
[15:39] uh you know the more examples you put
[15:42] into something the better it'll do on
[15:43] your examples but it might not it might
[15:47] get confused then when it sees novel
[15:49] inputs right so you know do be careful
[15:52] that if you're you know making your
[15:54] descriptions your prompts everything
[15:56] more specific that you are evaluating
[15:59] them for a very wide range of um you
[16:03] know of inputs.
[16:05] so that you can see
[16:07] uh that it's not over you're not like
[16:09] overfitting your examples to just what
[16:11] you happen to be testing on, right?
[16:15] Uh so yeah, so that's the decision one
[16:18] model from Microsoft. Uh so definitely
[16:22] uh check that out. Um related to that,
[16:25] there was just an article
[16:28] came out just before office hours about
[16:30] using decision models for evals. Uh this
[16:33] is from Hamal Huain. Um and the other
[16:38] exciting thing I wanted to mention,
[16:40] Hamal Hussein, I bring him up all the
[16:41] time because he's in valuations expert
[16:44] and he just joined uh OpenAI. So he just
[16:48] announced that yesterday. So that should
[16:50] mean that OpenAI evals will get better.
[16:55] Um because they brought in like the
[16:56] expert on eval. So that will be really
[16:58] interesting. Um, but yeah, so he just
[17:01] did this blog post about using decision
[17:03] models for evals. I haven't even read it
[17:05] yet because it just it just came off.
[17:08] Let me see what they compared. Oh, they
[17:11] didn't put didn't put decision one ML.
[17:15] Uh, but you can So here, so what did it
[17:19] decide? Um,
[17:24] all right. So I'd have to actually read
[17:25] it to understand. Um, so wow. Okay. Open
[17:29] eye decisions is doing really really
[17:32] well on everything. Maybe that's why he
[17:34] joined OpenAI.
[17:37] Jeb did not Jeb did not meet his
[17:39] requirements here. Okay. Uh, and then
[17:42] you have to So there's this decision
[17:44] threshold you can set. Um, so he did a
[17:48] little tuning here on the decision
[17:50] threshold. Uh, okay. So I guess OpenAI
[17:54] decisions is a lot more expensive.
[17:57] But the performance is, you know, really
[18:01] good.
[18:02] Um,
[18:05] but it's four times the cost. Okay.
[18:08] Okay. So, yeah, lots of interesting
[18:09] things here. I think this would also be
[18:10] a good blog post to look at just if
[18:12] you're considering switching to decision
[18:14] models for anything, just to see um, you
[18:16] know, just his evaluation approach. I
[18:18] see Adam said, you know, any
[18:20] recommendations for which decision model
[18:21] would be good to use for health and
[18:23] medications data. Um, so yeah, so I
[18:26] don't know because that probably would
[18:28] depend also on what was in their
[18:30] training data. So maybe you want to look
[18:32] at all these also add in Microsoft
[18:34] decision one. Um, decision one was
[18:37] trained based off of Quen a Quinn model
[18:40] I believe. So I don't know how much how
[18:42] good generally Quen. So you know OpenAI
[18:45] decisions is based off Luma, Microsoft
[18:47] decision one's based off Quen. Um, so
[18:49] you could also look at the benchmarks
[18:51] for those generally to see like, oh, how
[18:53] well does Luna do with, you know, health
[18:54] and medications data. Um, you could also
[18:57] try fine-tuning your own. Um, let me
[18:59] see. My colleague was just messaging me
[19:02] about what he was fine-tuning. Um, you
[19:06] know, it is an option then. Um,
[19:10] let's see.
[19:12] What was he doing?
[19:15] Uh, 400.
[19:18] Oh, let's see.
[19:21] Um,
[19:23] lia, let me see. Lia model, is that
[19:26] public
[19:28] non? Oh, here we go. Yeah. So, this is
[19:30] what my colleague was fine-tuning.
[19:34] U, it says you can fine-tune it in less
[19:36] than 24 hours on your laptop.
[19:40] Wow. I guess it depends how good your
[19:42] laptop is.
[19:44] Um but um you know that would be another
[19:46] thing to consider because a decision
[19:48] model is a lot smaller than
[19:51] an LLM. Um so if you're doing it for a
[19:55] really specific
[19:57] scenario
[19:59] then you know this might be something
[20:01] where it would make sense to do some
[20:04] fine-tuning.
[20:06] So you could check that out as well. Uh
[20:10] that's pretty cool.
[20:13] Uh let's see what else. Okay,
[20:17] related to decision models, we we last
[20:21] week we played around with the openi
[20:22] decisions API and of course this week I
[20:26] got to go to light mode. Uh this week um
[20:29] they added multimodal support. Um oh and
[20:33] even something specifically called box.
[20:35] Okay, there's both images and box. Oh,
[20:38] they call them dreamer ready. They're so
[20:40] fun. I gotta say, I just love like the
[20:43] Jev kind of um their style to things. Uh
[20:48] so they call this dreamer ready. So
[20:50] they're not production ready, they're
[20:51] dreamer ready. And you have to send in
[20:54] this header here. Type safe danger zone
[20:56] images. True. Um so I guess first we
[20:59] should look at images. Okay. So with
[21:02] Jeb, you can now send in images and um
[21:06] you know it can be
[21:08] you can judge judge things against an
[21:12] image. Um so you can send in looks like
[21:15] multiple images
[21:19] and then you can oh and you can give
[21:22] them kind of you you can name them
[21:24] right. So you could give them names and
[21:26] so that then your questions can
[21:29] reference the assets.
[21:33] Um
[21:35] so that's good. Okay D uploading images
[21:40] yada yada. We got some Python here etc.
[21:44] Okay. So yeah, so they added image
[21:46] support and then they also added this
[21:50] box because everybody kept on trying to
[21:53] use these models to do um you know like
[21:56] image detection, object detection in an
[21:58] image and uh so I guess they decided to
[22:03] make that a formal thing. Um so you
[22:06] could you know extract extract things
[22:08] out of an image, right? So like we used
[22:11] to run machine learning on our webcam
[22:14] images uh on our front door and there we
[22:16] use like OpenCV to do that. Um but you
[22:20] could use a decisions API and be like
[22:21] okay
[22:23] is my cat at the front door? If so let
[22:26] my cat in. Whatever. Um so yeah that's
[22:30] interesting. Uh I didn't actually know
[22:32] they added this. So um that is something
[22:36] that Jeff has now added. So this
[22:38] decisions the decision space is heating
[22:41] up right now. You got lots of options
[22:45] and people are turnurning new things out
[22:48] all the time. Uh it's funny that this is
[22:51] like you never like it's good. I'm glad
[22:53] that you know things are shaking up a
[22:55] bit. Um I think generally you're going
[22:57] to see more custom models. I know at
[23:00] Microsoft we're you know building a few
[23:02] more uh custom models for Ignite. um cuz
[23:06] you know sometimes an LLM is too big and
[23:09] you don't have to go that big. So I
[23:11] think you'll see more of this uh related
[23:14] to that Microsoft models.
[23:17] Uh this was a blog post from the MAI
[23:21] team about how their training works for
[23:26] our MAI models. and uh they've worked on
[23:29] a new
[23:32] uh they you know they're they just
[23:34] completed pre-training a new base model.
[23:36] So that's a foundation model that then
[23:39] you know they're building other models
[23:40] on top of. So once again this is
[23:42] something you might expect to see more
[23:44] models at Ignite. Hint hint hint. Um
[23:48] so yeah but this is the base model. Um,
[23:52] and
[23:54] I also have not read this blog post, but
[23:56] I was told by, you know, people in the
[23:57] ML space is that there's some
[24:00] interesting um,
[24:03] reflections here. Gosh, this looks very,
[24:06] it's looks very uh, very ML.
[24:10] Um, so I don't know if I'll necessarily
[24:13] follow everything in this blog post. Um
[24:16] but if you are into LLM training then
[24:21] uh this one might be uh interesting for
[24:24] you.
[24:26] Yeah, I don't really follow any of this.
[24:28] Okay.
[24:29] Scaling data. Uh they've improved our
[24:32] quality classation topinning web parsing
[24:34] deation evaluation decination. All
[24:36] right.
[24:37] Um
[24:39] this is cool that I understand. All
[24:40] right. So they're getting more web
[24:42] content. Um but they're prioritizing
[24:45] novel data and reducing duplicate
[24:47] content in order to improve model
[24:49] performance.
[24:50] Uh they invested heavily in growing
[24:52] their BLM corpus cross image text pairs.
[24:55] So image captioning, spatial reasoning,
[24:57] medical understanding. Oh, for the
[24:58] question about medical there, sheet
[25:00] music reading, oddly specific.
[25:04] Um,
[25:06] uh, yeah. So they're be using this as
[25:09] the basis for,
[25:12] uh, more MAI models to come out.
[25:17] So look forward for more of that. Uh,
[25:20] just related to this because this blog
[25:21] post is from MAI. Mai is
[25:25] uh from U led by Mustafa
[25:30] Selimon and I am currently reading this
[25:33] is just a book recommendation but I am
[25:35] currently reading
[25:37] um this book here the infinity machine
[25:40] about Demis Hasabis but it also talks a
[25:43] lot about MU Mustafa because Mustafa
[25:46] started off at Deep Mind so I think this
[25:49] is a great book um so you know just if
[25:51] you're looking for a book to
[25:55] Uh, you might want to check that book.
[26:01] Uh, okay Justin. Okay. Microsoft copilot
[26:03] manage runtime.
[26:06] Is this the harness? Uh, or is this
[26:08] different? This is different.
[26:11] Go in the wraps.
[26:16] Build apps and co-work create apps in
[26:18] Microsoft Co. Build apps and co-pilot
[26:20] code. Okay. All right. I do not actually
[26:24] use any of these products here because I
[26:27] just I only use GitHub copilot, but I'm
[26:28] trying to figure out whether this is
[26:31] using the co-pilot harness behind the
[26:33] scenes or it might be uh because I think
[26:37] if you're doing any of these, I think
[26:39] these all use the co-pilot harness. So,
[26:41] I'm assuming
[26:44] that
[26:48] Huh.
[26:50] It's the first time I'm seeing it. Let
[26:52] me ask my M365 colleagues. You can
[26:56] publish apps in Power Platform. Yeah,
[26:57] anything that makes it easier to do
[26:59] stuff. Um
[27:02] uh
[27:04] and let me see.
[27:13] I just asked my colleague if she has any
[27:15] opinions. Um,
[27:19] yeah. Uh, so it does it. Okay. So, it
[27:23] makes it easier
[27:25] to
[27:28] So, it adds stuff to the admin center.
[27:30] So, that also sounds a lot like the
[27:32] agent 365
[27:36] as well. Oh, look. This article is
[27:38] pre-release documentation. Okay.
[27:41] Nice little
[27:44] nice little note up there. Um,
[27:48] create apps.
[27:50] Find it. Requires enrollments in the
[27:53] Frontier program. Okay.
[28:02] Let's see. Pre-release.
[28:05] Internal line of business apps.
[28:08] Conserely connect
[28:12] Microsoft Entra access to connectors. I
[28:14] seen that's connectors.asure.com.
[28:18] Um,
[28:21] and it looks like it integrates with the
[28:23] 365
[28:25] uh agent 365. Bring your own GitHub
[28:28] repository.
[28:31] All right. Yeah, I haven't messed with
[28:33] this at all. Uh, you're saying Lovable
[28:35] is using it to publish their apps, Power
[28:37] Apps. Oh, cool.
[28:39] Nice. Okay. So, that's good. So
[28:43] hopefully it makes it easier because one
[28:44] thing we don't have at Copilot, you
[28:46] know, like with Claude and OpenAI, like
[28:48] OpenAI has what do they call them?
[28:50] Spaces and sites and then Claude has
[28:54] I what do they call them apps or
[28:57] something? Cloud pages. Cloud has
[28:59] something too. And then um basically
[29:01] like all these different, you know, AI
[29:04] platforms have really easy ways of
[29:08] vibing an app and then sharing it. And
[29:12] um
[29:14] yeah, I didn't think we had that yet,
[29:17] but maybe we do if you're in one of
[29:19] these places, right?
[29:22] Um what I don't see here is how to do it
[29:25] from GitHub copilot since that's what I
[29:27] would be doing. But I suppose you you'd
[29:28] then use this. Uh so yeah, I think that
[29:31] it's good. This should make it easy. Oh,
[29:33] I see. Publish level app. Okay,
[29:36] interesting.
[29:39] All right. Well, hopefully it becomes
[29:40] easier because if copilot code, copilot
[29:43] code is basically GitHub copilot as far
[29:46] as I understand it. Um,
[29:49] so if you can do it in co-pilot code,
[29:55] then I would assume you'd be able to do
[29:57] it, you know, very easily in GitHub
[30:00] copilot too. So you say bring in your
[30:01] file, preview and interact with your
[30:03] canvas.
[30:05] The canvas blah blah blah build and
[30:07] publish. Okay. So, how do we do it now?
[30:09] Publish.
[30:11] Build an app.
[30:14] I assume we need to Okay, there's got to
[30:16] be like an agent plugin or something for
[30:18] it. Is there an agent plugin? No.
[30:22] Manage runtime.
[30:24] I'm trying to see how we can use this in
[30:26] Git Copilot. Normally, you would have
[30:28] like a
[30:30] um
[30:33] No. Normally, you'd have like a uh it'd
[30:36] be like a plugin that knew how to do it,
[30:38] right? Yeah. So, I don't know. I don't
[30:40] know anything,
[30:43] but thank you. I will uh I will ask my
[30:46] colleagues if if they've played with
[30:49] that. Um
[30:52] and see if there's a story
[30:55] for GitHub Copilot
[30:58] as well to be more developer friendly.
[31:02] All right. What else? What have I What
[31:04] do I know about? Um,
[31:07] let's see. On co-pilot note, there's
[31:09] Gemini 4 argan. I hear that model is
[31:12] actually decent. Uh, I'm still using
[31:14] Opus 5.5.
[31:16] That's my fave. Um,
[31:21] let's see if there's anything exciting
[31:23] in the news here.
[31:25] Uh, yeah, I've been working.
[31:29] We we have agent con and MCPcon is
[31:32] coming up. Uh so we're doing Oh, I can
[31:36] just share the my friends
[31:40] uh the workshop we're doing. So this is
[31:42] a little workshop where you um where you
[31:47] create this whole agent using um
[31:50] containers
[31:52] and uh you know this all works locally
[31:55] with docker compose and so it just goes
[31:57] through the process of
[32:00] you know making um making the the
[32:03] architecture more robust with open
[32:06] telemetry and uh you know using an Llama
[32:10] container and all this stuff. So, uh it
[32:13] might be interesting if you like
[32:15] containers and Kubernetes. Uh there's
[32:17] also
[32:19] a K8 folder here. Uh let's see. The
[32:22] other thing
[32:24] is
[32:26] my
[32:30] workshop. This is just a talk I gave at
[32:32] AI engineer. It finally got published.
[32:36] So, uh you might be interested in that.
[32:38] the the repo for that is here. Um, at
[32:42] this point the models are old because
[32:44] that was in June and what are we now?
[32:46] October.
[32:48] Um, but you know, you can swap in swap
[32:51] in new models and uh, you know, it's the
[32:55] point
[32:57] uh is to try stuff out. Uh, okay. What
[33:02] else is going on here? Sorry, I'm a
[33:04] little out of it because of the cold. Uh
[33:06] do
[33:08] um
[33:10] what else was I doing? I got to say like
[33:13] Opus 55 is so good. This is what I was
[33:15] really impressed. Right. I I told Opus
[33:17] 55 that I needed to, you know, I was
[33:20] testing this OCR ingestion pipeline and
[33:23] I wanted some good sample data. This is
[33:25] for Ignite and it invented its own way
[33:30] of doing synthetic handwriting
[33:31] generation, right? which I just thought
[33:34] was just incredible. So like synthetic
[33:37] data generation, this is something I
[33:39] probably need more than other people,
[33:40] but wow, like the ability of these
[33:43] models to just, you know, be like, oh,
[33:46] I'm just going to make up my own
[33:47] synthetic handwriting generation
[33:48] algorithm, right? Just incredible.
[33:51] Um,
[33:54] okay,
[33:57] what else? What else?
[34:01] Yeah, we've mostly been doing lots of
[34:02] prep for Ignite.
[34:04] Um, so you know, lots of I'm doing lots
[34:08] of IQ stuff for that. So, Foundry IQ,
[34:10] Fabric IQ, Work IQ, Web IQ, all the IQs.
[34:16] Let's look at this Hydrofusion. So,
[34:17] Hydra Fusion is now available in VS
[34:19] Code. Uh, I haven't swapped to it yet.
[34:24] Uh, let's see how we can check. Has
[34:26] anybody here tried Hydrofusion?
[34:28] Uh, you like the idea of hydrofusion. I
[34:30] like the idea of hydrofusion.
[34:33] I just don't in practice want to leave
[34:35] my Opus 55.
[34:38] Okay, so this is how you do it. Um, you
[34:40] search for your settings. Oh, it's your
[34:43] daily driver. Oh, it's Nick from
[34:45] Microsoft. Hi, Nick. Okay.
[34:47] Uh, okay. So, let's say to so to switch
[34:51] it over, we're going to go to user
[34:52] settings. Hydra Fusion. Okay. Uh, Uh, so
[34:58] you can say hydrofusion enabled.
[35:03] Oh, we've got two different options
[35:04] here.
[35:08] Hydrofusion enabled.
[35:10] V2 multi-root
[35:14] and ask the service to keep reading.
[35:16] Gosh, I don't know which which setting
[35:18] are you using, Nick? There's a lot of
[35:20] settings here. when I enable together
[35:21] with China.
[35:24] Okay, maybe I'll just change everything
[35:26] to the max.
[35:31] Uh, research with GB6 Luna. Okay, give
[35:36] me a prompt I should try here. Let's
[35:38] see. Uh,
[35:42] oh, Nick. Hi, Nick. Nick, are you gonna
[35:44] share it?
[35:51] Yeah, there's a little background stuff
[35:52] behind you, but
[35:57] Oh, yeah.
[36:00] Nice.
[36:05] I don't know what Discord has for
[36:08] stuff, but uh it's fine. We can we can
[36:10] hear. All right. You want to screen
[36:11] share and show off Hydro Fusion?
[36:16] Nice.
[36:31] Oh, okay. Let me see. Um,
[36:37] do
[36:38] invite
[36:42] options.
[36:44] More options. Ignore
[36:48] Maybe I just have or Okay, I stopped
[36:51] sharing doing it now. You can do it.
[36:53] Okay, that was just it. Okay,
[37:01] it's fine. The only issue is that this
[37:03] won't work on the recording, but that's
[37:05] okay.
[37:10] Actually, let me just bring those
[39:24] So you're only using it in copilot app.
[39:46] Oh
[39:49] yeah.
[40:04] H
[40:30] Yeah, that's something I should Yeah, I
[40:32] don't know why they didn't make it in my
[40:33] news this week. Yeah, VS Code does
[40:34] support Canvas now. So, that makes me
[40:36] more inclined to use Canvas because I
[40:38] still go between VS Code and Copilot.
[40:42] Um, yeah, because I like to edit code
[40:45] still and stuff. Um and uh yeah, so
[40:50] that's good. So generally VS Code and
[40:52] the Copilot app are converging more now
[40:55] because they now
[40:57] um as of this week are like using the
[40:59] same harness. Uh and and now we've got
[41:03] support for canvas. So you should be
[41:06] able to just um you know have you know
[41:09] VS Code or GitHub Copilot just make a
[41:12] make a canvas though I haven't made any
[41:14] in VS Code yet. See which of my I don't
[41:17] even think I've Yeah. Do you have a
[41:18] canvas handy?
[41:22] There we go.
[42:43] Yeah.
[42:56] Yeah.
[43:02] So, they're wondering, can it I think it
[43:04] can pick local models now, right? That
[43:06] was the announcement last week. Um I
[43:08] thought that Kayla did a did a demo of
[43:12] that.
[45:09] So the blog post says that hydroofusion
[45:11] was going to start tapping into local
[45:13] models in October in experimental
[45:16] preview. So do you have that
[45:17] experimental preview on?
[46:00] Yeah, I think the question is how do how
[46:02] when is hydrofusion how is hydrofusion
[46:05] going to start picking the local models
[46:06] because according to that blog post it's
[46:08] you know it's it's it should be able to
[46:11] start using local models but when and
[46:14] Now
[46:34] yeah. Yeah. Uh, you should yeah, put
[46:37] together a demo of that and maybe I'll
[46:40] try one try it one day if I can bring
[46:43] myself away from Opus 55. I deserve like
[46:45] as long as I can use Opus 55 for
[46:47] everything. Why not? I guess your point
[46:49] is like sub agents but sub agents h
[46:53] could already potentially I could
[46:55] already instructed to use sub agents to
[46:56] do research if I really wanted to speed
[46:58] up research, right?
[47:14] Oh, okay.
[47:42] And we can't yet we can't customize the
[47:45] models yet though, right? Like to say
[47:47] exactly like this is my expensive model,
[47:50] this is my cheap model.
[48:18] Okay.
[48:29] Nice.
[48:37] All right. Okay. Awesome. Well, we are
[48:41] Yeah. Well, we're at time now. Uh thank
[48:44] you, Nick. Um that's good since I'm a
[48:47] little out of it today still. Um, so
[48:50] yeah, everyone go play with stuff. Um,
[48:53] try out the try out canvases too now
[48:56] that they're everywhere.
[48:58] Uh, you basically you can just tell like
[49:01] there's built-in skills for it. So you
[49:03] can just be like make a canvas for this,
[49:04] right? And it'll just, you know, it'll
[49:07] just spin up a little mini web page,
[49:09] right? So the idea here is that with
[49:10] canvas is you know you um you don't
[49:14] necessarily you know want to use chat
[49:17] for all the ways you're interacting
[49:20] uh with your agent. Sometimes you want
[49:21] to interact a different way some sort of
[49:24] visual uh so a canvas can be your
[49:28] visual.
[49:30] All right there you go. That's right.
[49:32] Yeah. So you can explicitly invoke the
[49:34] skill by doing slashcreate canvas. Let
[49:36] me actually see if that works in create.
[49:40] Yeah. So, looks like that
[49:44] even though it says VS Code supports it
[49:46] now. Um Oh, we have to turn it on. Uh
[49:49] preview canvas is enabled. Okay. Wait.
[49:52] So, all right. Let me just quickly
[49:55] screen.
[49:57] Um
[50:00] just to show this. All right. Let's just
[50:02] get let's just get a canvas working in
[50:06] here. All right. So, you have to it says
[50:08] you have to do user settings canvas
[50:13] enabled. Okay. So, you go here. Chat
[50:15] canvas is enabled. Now, it's enabled.
[50:18] So, now we should be able to create
[50:21] canvas. Now, you can do it. So, yeah.
[50:22] So, you can use create canvas for all of
[50:24] them. So, I'm going to create canvas to
[50:27] visualize my AI search
[50:30] index stats, whatever.
[50:34] Um,
[50:36] and it's going to
[50:39] create a canvas. Uh, hopefully, uh, I
[50:44] don't know how fast, but normally these
[50:46] things could be like pretty fast. Um,
[50:50] library snapshots. What are we? It keeps
[50:53] defaulting to 61 soul. I have to fix up
[50:56] my defaults because I want Opus 55.
[51:00] All right, we'll just do
[51:03] that one. I just want a pretty canvas.
[51:06] Okay, so you can see it like read a
[51:08] skill, right? So that's the
[51:10] um
[51:13] mandatory claw pilot theme. What
[51:18] is this from? Is this from this? Wait.
[51:22] Copilot skills. Where did this web
[51:24] artifacts builder come from? Is this
[51:27] from I don't know. Yeah. And also, for
[51:31] some reason, my thing I always like to
[51:32] default to YOLO now, but my YOLO default
[51:34] is also not working. So, uh, this is
[51:37] just because of the change over to the
[51:38] new harness that some of my defaults
[51:40] aren't there. What is this claw pilot
[51:42] thing? I have so many questions. I don't
[51:44] know if this is something that is just
[51:46] private, some internal thing that I
[51:48] accidentally got, but apparently we are
[51:51] going to get a claw pilot theme for some
[51:54] reason. Um,
[51:58] I don't know why.
[52:01] Okay, this is correct. Yeah,
[52:02] extension.mgs. So, you know it's a
[52:04] canvas if it's an extension.mgs. It's
[52:07] also called like a canvas extension. Um,
[52:10] because sometimes I'll actually like
[52:11] look at it. So here you can we can
[52:13] actually like well it's not going to let
[52:15] me look at it right now. Um
[52:19] let's see here we go. Uh oh yeah so it's
[52:21] looking at one of my previous extensions
[52:23] canvas extensions. So this is one that
[52:25] I've made before um for writing posts
[52:29] across different social media networks
[52:31] and I just wanted to be able to draft it
[52:33] in like a text editor and see how short
[52:36] it would have to get. So you can see
[52:38] it's just a big old JavaScript file and
[52:41] the JavaScript file can you know has
[52:43] this create canvas function in it and it
[52:47] can take actions um and the actions can
[52:51] interact with the agent the main agent.
[52:55] Uh so uh now normally you shouldn't have
[52:59] to look at the MGS. I'm just a nerd so I
[53:01] like to look at the MGS and see what's
[53:03] up. Um,
[53:06] but you know, usually you it's just a
[53:09] something you're making to help you out.
[53:11] Um, because you, you know, want uh some
[53:15] other way of interacting. So, normally
[53:16] you would add some sort of interaction
[53:18] to be like, okay. And then you're going
[53:19] to add buttons to the canvas so that
[53:21] when I click on the button, it'll like
[53:23] insert all the details from that search
[53:25] index into my chat. Right. And right. So
[53:28] it's you know you really like the place
[53:31] where canvases shine is as a way of
[53:33] interacting with your chat. So is
[53:36] something like okay when I click this in
[53:38] the canvas it's going to send such and
[53:40] such message to my chat right you can
[53:44] also just use them as like a quick web
[53:45] page um that's just not as you know it's
[53:49] not taking a full advantage of of
[53:51] everything.
[53:53] All right. So, but
[53:55] all right. The dashboard is implemented.
[53:58] It is loading,
[54:00] loading, loading, loading here. Um,
[54:05] listing canvas capabilities.
[54:08] There we go. All right. So, we got it.
[54:10] So, it only took a few minutes. Um,
[54:13] oh, so refresh. Yeah. So, here, uh, we,
[54:18] you know, this is just a bunch of stuff.
[54:20] Oh, that's fun. I like this actually. I
[54:23] didn't I didn't know what I was going to
[54:24] get here.
[54:27] You know what? At this point,
[54:28] visualizations are so Oh, that was a big
[54:31] giggle. But visualizations are so easy
[54:34] to make that you should just like always
[54:36] be making visualizations
[54:38] because you never know like which of
[54:39] them might be actually just really good.
[54:41] You're like, "Wow, like I really am
[54:43] happy um that uh you know, I visualized
[54:47] it that way, right?"
[54:49] Um, and now this would work in both
[54:51] copied app and VS code. Uh, so filter.
[54:55] Wow, it even added a filter. Fancy,
[54:58] fancy, fancy, fancy.
[55:01] Uh, yeah. But it say add a button to the
[55:07] canvas so that when I click on
[55:11] an index
[55:14] it puts the index info
[55:18] in the chat. I don't know something like
[55:20] that.
[55:29] Whoa. Oh, I got some long got some long
[55:32] chunks. Got some chunky chunks.
[55:38] Uh, now I'm going to have to like
[55:41] actually check this this canvas in. Now
[55:44] remember this is not I also in the same
[55:46] web p uh repo I do have a full web app,
[55:49] right? So, you know, sometimes you
[55:51] actually do want a full web app that
[55:53] you're like running locally. A canvas
[55:55] should be an alternate form of, you
[55:58] know, interacting with data and an agent
[56:00] together.
[56:02] Um, that's how I would think of it.
[56:06] Let's see if it's going to figure this
[56:09] out. Yeah. And then of course there's So
[56:12] I asked whether we could use MC apps
[56:14] instead because you could also be making
[56:17] an MCP app. Um, so if you have an MCP
[56:20] server,
[56:22] uh, then you know your MC server can
[56:24] hand out an app. So I would I would vote
[56:27] for that. Like if you're, um,
[56:30] you know, if you're trying to make
[56:31] something more generic that's going to
[56:32] work across any coding agents, because
[56:34] these canvases are still only specific
[56:36] to VS Code and GitHub Copilot. So if
[56:38] you're trying to make something that can
[56:39] work across any coding agent, then uh
[56:43] you know then you can make an MCP server
[56:45] and have that MCP server uh return back
[56:48] an app. Um and the MC server could just
[56:51] be like you know you can you know make
[56:53] an agent plugin that bundles together
[56:55] skills and MCP server and it could just
[56:56] be a local MCB server like a standard
[56:59] input output server and even a local uh
[57:02] standard input output server can send
[57:04] back an MP app, right? So, um, you know,
[57:08] you do have that options. Canvases, how
[57:12] would how do canvases work in the coat
[57:14] CLI? It's a CLI. How is that even
[57:17] possible? What does it do? Open up like
[57:20] a web page. That's so weird. My gosh.
[57:24] Like, you have to really I'm sorry. I
[57:26] don't use a copot any CLI anymore
[57:28] because why would I? Because the app is
[57:30] so much, you know, better. Like, you
[57:32] have to really like CLIs to be uh using
[57:35] it. Okay, here we go. Send a chat.
[57:36] That's what I wanted to show. It opens
[57:38] up another window. I guess at that
[57:42] point, I really think you should just
[57:44] move to the Copilot app.
[57:47] Um,
[57:49] all right. So, it it did it. Uh, it's
[57:51] just it's just doing it. Oh, it's just
[57:53] testing it right now. It's testing it.
[57:56] It's running some playright code, making
[57:58] sure it works.
[58:00] I actually don't know what's going to
[58:01] happen when I click send to chat. It's
[58:03] very exciting.
[58:06] CLI is trying too hard these days. I
[58:09] mean, it's good. It's good we have CLI
[58:11] because some people want a CLI.
[58:13] I just personally
[58:16] uh I have there's no reason for me to
[58:19] ever use CLI. The CLI does have a lot
[58:21] more options in the app because they're
[58:23] able to just add more args all the time.
[58:25] So, I have noticed there's a lot more
[58:26] flexibility. Like for example, plug-in
[58:28] installation. I'm trying to test this
[58:29] new plugin that we're building for
[58:30] Ignite. And the Copilot app only let me
[58:34] install plugin from like a marketplace
[58:35] URL, but we don't have a marketplace
[58:37] URL.
[58:39] Uh we only have a you know, we only have
[58:41] a private um folder.
[58:45] Giggle, giggle, giggle. Uh all right,
[58:48] send to chat. There we go. Look at that.
[58:52] See,
[58:54] Nick's new here, so he doesn't know
[58:55] about the giggles. Uh that's my child
[58:58] giggling. All right. So here, so this is
[59:00] us all what I wanted to show, right? Is
[59:01] that we can click it and it can interact
[59:05] with the agent, right?
[59:08] Um
[59:10] so yeah, so you know, get some ideas for
[59:13] canvases as long as I think canvases
[59:15] work if you are a fully a GitHub copilot
[59:17] shop or if it's just for your own
[59:19] personal use. Um I just wouldn't use
[59:22] canvases if you're looking for support
[59:24] across multiple coding agents because
[59:26] they're only you know supported by the
[59:28] GitHub co-pilot surfaces right so great
[59:30] option now if you're full full co-pilot
[59:33] shop but if you need more compatibility
[59:35] portability
[59:37] uh then uh you know uh look into other
[59:41] options well Nick you have to start
[59:43] recording the giggles and then and then
[59:45] you can make an agent hook that uh if
[59:48] they're one they're probably giggling so
[59:50] Then you can just make a little agent
[59:51] hook. Let me show you the code for that.
[59:54] Where is it? Um,
[59:56] give each agent notifications.
[01:00:00] Where is it? Uh,
[01:00:03] this one.
[01:00:06] Here you go. So, you record your kid and
[01:00:09] then you make the hook and then boom,
[01:00:13] you get non-stop giggles.
[01:00:19] All right, I'm way over now and I think
[01:00:21] I should give my voice a break, but I
[01:00:24] just wanted to play with canvases. Um,
[01:00:27] all right. Thank you everyone. I will um
[01:00:31] publish the recording and put all the
[01:00:34] the transcript and everything in our
[01:00:37] usual spot. Uh so you can check check
[01:00:42] here later.
[01:00:44] And next week is a little awkward
[01:00:47] because it's GitHub Universe. So I might
[01:00:49] be able to move the office hours to
[01:00:51] Monday. On Tuesday, I'll be doing uh on
[01:00:54] CA on at GitHub Universe to do the tech
[01:00:56] check. Um so I'll either have to cancel
[01:01:00] or move it to Monday. So I'll just check
[01:01:02] my schedule for next week.
[01:01:06] All right. Oh, what do I use for slides?
[01:01:08] Yeah, this comes up all the time. So my
[01:01:10] slides are all revealjs or they are when
[01:01:13] I when I get the choice. So here is and
[01:01:16] here is my slides. I have two slides
[01:01:18] about my slides.
[01:01:21] Um
[01:01:24] and then I also have um
[01:01:29] oh let me see HML five slides. Here we
[01:01:32] go. Sorry this is the other one. This is
[01:01:35] from a few years ago.
[01:01:37] And then I also have a repo with
[01:01:40] presentation skills in it here.
[01:01:45] So there you go. Uh yeah, slide dev. I
[01:01:48] think they use reveal. Yeah. Uh right.
[01:01:51] Maybe maybe more. Okay.
[01:01:55] Uh uh. Oh, I see someone's using their
[01:01:56] cloud code. Remember, you can use opus
[01:01:58] 55 with co-pilot and it's great. It's
[01:02:01] really really great. As long as you the
[01:02:03] most important thing in life is to have
[01:02:05] access to opus 55. That's all that
[01:02:07] matters. Obviously, I really like it.
[01:02:10] All right, bye everyone.
[01:02:13] Thanks for hanging out.
