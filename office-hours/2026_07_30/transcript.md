[00:00] So, this is the office hours. If you
[00:02] have additional questions about Fabric
[00:05] IQ,
[00:07] then uh go ahead and ask them here. Um,
[00:12] all right. And let's see. And we
[00:16] hopefully have some folks. I see we've
[00:18] got Josh in the chat. So, Josh is one of
[00:21] our fabric data advocates
[00:25] and um that can help out. So, I was
[00:28] saying I am quite new to fabric. Um, I
[00:32] was like doing Oh, and we also have Sam
[00:34] in the chat. I'm just seeing who we
[00:35] have. Yay.
[00:38] Um, yeah. So, my colleagues
[00:42] feel free to say hi in the chat so
[00:45] people get to know. Friendly fabric data
[00:48] advocates.
[00:50] Here we go. All right. So, what
[00:52] questions do people have? Um, I think I
[00:54] saw I remember Bernard. Is Bernard here?
[00:57] Bernard was asking about GQL versus
[00:59] Cipher. That was also something I was
[01:02] wondering too. Um, not GQL. No, you have
[01:07] to get
[01:10] um Okay. So, oh, so GQL is actually the
[01:12] standard. Okay. All right. So,
[01:16] it looks like
[01:18] it looks like GQL is in fact the
[01:21] standard because this is ISO published.
[01:22] Okay. All right. though I I don't think
[01:24] I represented it correctly on the stream
[01:26] because I couldn't remember what which
[01:27] one was standard standardized. So yeah,
[01:30] so GQL is um is an ISO standard. So
[01:34] that's great. It's always lovely when
[01:36] we're using the standard. Um and I think
[01:40] cipher
[01:42] um you know cipher is you know was a
[01:46] kind of original version. Um so you
[01:49] might be using cipher. Cipher is very
[01:50] similar. We have cipher um on our Azure
[01:54] Postgress
[01:57] uh but it looks like they're really
[01:58] quite similar. Okay, so
[02:03] question is should we put all of our
[02:06] data in one lake and from there ingested
[02:08] to foundry knowledge bases and if so why
[02:11] are the other options available?
[02:15] Um okay so you could I mean it the
[02:20] question is right so you could have a
[02:21] foundry knowledge base that
[02:25] ingests from you know a lot of people do
[02:27] foundry knowledge bases that ingest from
[02:29] blob storage or ADOS2
[02:32] and um you know are not put in one lake.
[02:36] So I think the question is whether
[02:40] um if you have other re like you know
[02:42] the reason to put it in one link I I
[02:44] would say is if you want to be able to
[02:46] use the other fabric functionality on
[02:48] top of it right so if you do want to you
[02:51] know run all these other things on top
[02:53] of your data then it makes sense to
[02:56] bring it into one link um if your only
[02:59] goal is retrieval is search then you
[03:04] don't necessarily need to bring it into
[03:05] one link like you just set up a you know
[03:07] just standard blob storage and um you
[03:11] know set up an indexer there. So um yeah
[03:14] I mean I think it would depend on what
[03:16] are the what are the things that you
[03:18] want to do with that data. What kind of
[03:20] querying do you want to do with it? Is
[03:21] it is it data that's like um you know
[03:24] like hot data cold like is it data
[03:26] that's being updated all the time? Is it
[03:28] powering your website or is it just
[03:30] documents like and um do you do you need
[03:35] to run those other fabric things on top
[03:37] of it or not? Um
[03:39] and then like cost right you do want to
[03:41] look at costs for these things and uh
[03:43] fabric does have a you know a cost to
[03:45] it. Um so so yeah so you you could bring
[03:49] things into one lake and and query it
[03:51] that way um
[03:54] via the data agent um or you can even do
[03:57] ingestion
[03:59] um of it there. But if it's like PDF
[04:01] files like usually those are you would
[04:03] stick those in like blob storage or ADLS
[04:06] and then do a data ingestion pipeline
[04:09] from there. Let me just look at the
[04:11] indexers for
[04:14] Azure AI search. Oh,
[04:20] so generally at Microsoft we do have a
[04:22] lot of options overall.
[04:24] >> Um, so it it can be really overwhelming
[04:26] to figure out like, oh, well, what
[04:28] option should I use? You have so many.
[04:29] And it's just because all of our
[04:31] customers have just so many different
[04:33] needs. Um, and you know, we're always
[04:36] trying to offer everything for everyone.
[04:39] Um so you can like right so for like
[04:41] Azure AI search you can set up indexers
[04:44] even for like Microsoft one link you can
[04:46] set up an indexer right and let's see if
[04:48] this index okay index data from one lake
[04:50] files and shortcuts right and so you can
[04:53] even set up an indexer um so you you
[04:57] know you want to like check out all
[04:58] these things um but you don't have to
[05:00] because you could also use fabric data
[05:01] agent so it's really going to depend on
[05:03] the kind of the data that you have uh
[05:07] there and what what kind of things you
[05:09] want to do with it. Um,
[05:15] yeah, I see typing maybe followup.
[05:22] Um,
[05:28] it would be nice if one lake would be
[05:29] the one place for all data. And of
[05:31] course, it depends. Yeah.
[05:34] Um, yeah. I mean you could if you were
[05:36] definitely doing a lot of fabric heavy
[05:38] stuff on top of it you can um yeah you
[05:41] could you know start with one lake and
[05:43] you didn't even you know you wouldn't
[05:45] even have to necessarily do the indexer
[05:46] you could see if data agent would um you
[05:50] know would be enough for you to do the
[05:52] querying. Um, but then if you realize
[05:54] that you needed more customization of
[05:58] how things are being processed, that's
[06:00] when you would set up an indexer here.
[06:03] And um, and that would actually be so
[06:06] that would be doing a copy, right? So
[06:08] like, you know, as I always say, like if
[06:09] you for you know, if you if you don't
[06:11] have to copy it in uh, you know, it's
[06:14] better because then you don't have to
[06:15] worry about things getting out of date.
[06:17] Um, but luckily this does have like
[06:20] deletion detection, right? So it can
[06:21] delete when there it can detect when
[06:23] there's new data, updated files,
[06:25] deletion. Um
[06:29] so you know it can keep track of all
[06:31] that. That's why there is an indexer. Um
[06:34] so I would say like you start with a
[06:36] remote data source. You start with the
[06:38] remote option to see like hey is it good
[06:40] like can I get good enough results if
[06:42] I'm just using that fabric data agent
[06:44] knowledge source. Um but if not like if
[06:46] you need custom ingestion right like
[06:48] maybe if you have really uh messy data
[06:51] and you know maybe you know it's like
[06:52] unstructured documents then you could
[06:54] set up uh an indexer and then that way
[06:57] you can do custom ingestion skills and
[07:01] uh you can really customize it for the
[07:03] kind of data that you're storing in one
[07:04] lake.
[07:07] Um so if you have text fields
[07:10] that contain paragraphs um yeah so
[07:14] here's like the kind of these are the
[07:16] files that are supported for
[07:18] um the one leg indexer I didn't try so
[07:21] the thing is for my demos for this one I
[07:25] didn't try to
[07:27] really store something like you know
[07:30] like I'm not sure what kind of data
[07:31] you're thinking of storing like I didn't
[07:33] try to store this more like you know
[07:35] like docx like I didn't even attempt to
[07:37] store that in one lake to see what that
[07:39] experience would be like with a data
[07:40] agent. Um
[07:43] uh I think it would have to let's see
[07:44] for that sort of data it would have to
[07:47] do I guess it would do a direct query to
[07:51] because that's like unstructured data so
[07:53] it would need to do I guess a direct
[07:56] query [clears throat]
[07:58] to lakehouse or data warehouse
[08:02] and SQL and so then you wouldn't be
[08:05] getting like so if you're really trying
[08:06] to query you know like um these kind of
[08:09] documents you really do want to have
[08:12] that hybrid search on them so you can
[08:15] get vector search uh and combined with
[08:18] keyword search. So I I would say you
[08:20] know if you're dealing with these sort
[08:22] of documents here then you probably want
[08:24] to use the indexer.
[08:31] Okay. So comments on a website or
[08:32] descriptions of a product. Yeah. I think
[08:34] the question is whether you you know
[08:36] whether you think the questions are the
[08:38] kind that need to be answered with a um
[08:42] you know with the help of a vector
[08:43] search. Um and in that case I would be
[08:48] considering doing an indexing of them so
[08:50] that you can get that um get that vector
[08:53] search.
[08:56] Uh so Damian asks uh with fabric IQ we
[09:00] can get an agent of private questions
[09:01] about our PowerPoint by using a semantic
[09:03] model. Yeah. So, let me go back to that
[09:06] question uh that example
[09:09] data agent. Yeah.
[09:12] Um yeah. So, this question here, what
[09:14] are total website revenue and conversion
[09:16] rate, right? Um
[09:19] and that was quering a semantic model.
[09:23] Um I should let me think of a fancier
[09:25] question than that because that question
[09:27] was like really easy, right? But you can
[09:29] see it says analyze Ktoso web analytic
[09:31] semantic model for this right. So it is
[09:34] sending it's coming up with this DAX
[09:36] here and it is sending it to the
[09:38] semantic model.
[09:41] What would be a more interesting
[09:42] question I could ask it? Uh uh by for
[09:47] all social
[09:50] how many sessions
[09:53] how many conversions what were website
[09:56] conversions
[09:58] from
[10:00] social channels. Let's try that.
[10:10] Okay. So, Somali says it will answer
[10:13] questions about dating in your semantic
[10:14] model, but not necessarily the PowerBI
[10:16] report. So, it won't answer questions
[10:17] about what's on the report. Okay, that's
[10:19] a good that's a good distinction there,
[10:21] right? Um, so it has access to the
[10:24] semantic models. Um, but you wouldn't
[10:27] necessarily be like saying like, oh,
[10:29] tell me what's like in this chart or
[10:31] something, right? So, it has to be
[10:32] something that's answerable from the
[10:33] data itself, right? So, going back like
[10:36] these are the semantic models, right?
[10:38] Uh, it's cool. They've got like this
[10:39] best practice analyzer so we can like
[10:41] get um you know get feedback on whether
[10:45] we've done a good job on it.
[10:50] Oh, and then here's the DAX query view.
[10:52] So there's the DAX query view, right? Um
[10:54] so basically it' be things like if you
[10:56] can, you know, if you can run the DAX
[10:58] here and get the answer, then that's
[11:01] something that the data agent could do,
[11:03] right?
[11:06] Uh look, oh yeah, it got this answer. So
[11:08] let's see if it got a more complicated
[11:09] query for this one.
[11:16] Okay. So here we can see a much more
[11:18] complex stacks query that it came up
[11:20] with. So it created a filter.
[11:23] It summarized the columns by that filter
[11:27] and didn't order by right. Um so in
[11:30] theory, I haven't tried this before, but
[11:32] I could go and uh where was that DAX
[11:36] one?
[11:37] just go and like paste it in there. Get
[11:40] rid of those back ticks. Dax, run it.
[11:46] And there we go. It's the same result,
[11:47] right? So, if we can run the DAX here,
[11:50] then the data agent can come up with the
[11:52] DAX and get back the results.
[11:57] All right. So, Ken had a question for
[11:59] creating ontology, do we need admin
[12:01] permissions? And Josh said, "Antology is
[12:04] a preview feature. So as long as this
[12:06] enable tenant, you should be able to
[12:07] create intology in the same way you
[12:08] create items in fabric. Yeah, I will say
[12:11] I am not an this is I am borrowing my
[12:15] friend's fabric workspace [laughter]
[12:18] because I couldn't get access to fabric
[12:21] on my um on my main tenant. Um so I um
[12:25] I've been able to do all of this and I
[12:29] don't think I'm particularly an admin,
[12:31] right? like I'm just a like kind of like
[12:34] um hanging out uh in his workspace
[12:37] making lots of things. Um but yeah, as
[12:40] you saying there is there's a bunch of
[12:41] things you have to configure. So where's
[12:42] that? We have a doc about it. I don't
[12:44] know if you all remember where that doc
[12:46] is, but um there you do have to like
[12:50] really enable a lot of things. So the
[12:52] admin does have to enable a bunch of
[12:54] stuff, right? Um let's see. Is it this?
[12:57] Yeah. So when like whoever is your admin
[13:00] for the tenant does need to enable
[13:03] ontology item, right? So that was
[13:06] already enabled for this fabric tenant.
[13:08] Okay, thank you. Yeah. Um so that's
[13:11] that's the thing. If you don't see it,
[13:13] then that's going to be that's going to
[13:15] be the issue. Um
[13:18] now for the like this repo itself I do
[13:21] have um that the bicep knows how to
[13:25] provision a fabric capacity but I have
[13:28] that as an option that defaults to false
[13:31] um because that is something you you
[13:32] know you do need to uh have the ability
[13:35] to have fabric within your tenant and
[13:37] you know the permissions to actually
[13:38] create that. I tried doing that in a
[13:40] tenant where I only had like access to
[13:43] what was the um there was various like
[13:45] access issues, right? So being able to
[13:47] create a fabric capacity does require
[13:50] you know um the fabric availability in
[13:53] the tenant and some level of admin to be
[13:55] able to create that. Um to remember what
[13:57] the error was that I got. Uh but um but
[14:01] yeah, being able to actually do all this
[14:03] stuff once it's enabled like it you can
[14:05] you can do quite a lot.
[14:13] All right. I see
[14:17] folks typing there.
[14:24] Uh
[14:28] else?
[14:33] Okay. Colleen [clears throat] asked, "Do
[14:34] we get ontology data only on F64
[14:37] capacity and above or is it for all
[14:40] capacities?"
[14:44] It's a good question. I'll wait to see.
[14:46] [laughter]
[14:47] Um,
[14:49] let me look at the errors that I had.
[14:51] Yeah, I see Somal is was chatting. Um,
[14:54] let me see what errors I had when I was
[14:56] trying to do it on a non F2. So, the one
[14:59] I'm on right now, I think, is a fabric
[15:00] F2.
[15:02] Um,
[15:04] I think with the free trials, I did have
[15:08] options. Yeah. So, in order to
[15:14] um
[15:25] Okay. So, yeah, I Let's see. I I did
[15:28] want me to have an F2. See what you all
[15:30] said was the answer to that. Um F2 and
[15:34] above. Okay. All right. Well, do we have
[15:37] some disagreement here? Available in all
[15:38] paid. Oh, is F2 the first paid capacity?
[15:40] Is that why?
[15:43] Let's find the price.
[15:45] Okay.
[15:47] Um, I did occasionally get Yeah. So,
[15:50] here's Oh, let's look at the pricing.
[15:51] Okay. Oh, yeah. So, F2 is the the
[15:54] cheapest paid one.
[15:58] Oh, it's actually like reasonable.
[16:00] I remember when fabric first came out,
[16:02] it was like 15. It I think it was like
[16:04] this was like the minimum. This is
[16:07] actually pretty reasonable now. I am I
[16:08] did not realize that it was it was um
[16:11] that it went this low now. So, so there
[16:13] you go. So, you can start off with this
[16:15] F2. I mean, it's still certainly money,
[16:17] so you want to get your uh company to
[16:19] pay for this, but um but that's a very
[16:21] reasonable amount to start off with. Uh
[16:22] I did run into like a few capacity
[16:25] issues. Um and that was when I was doing
[16:29] like a lot of I think it was when I was
[16:31] doing like a lot of repetitive queries
[16:32] or something like that. Um it was like
[16:35] taking some time to to catch up. Um so
[16:37] if you're on F2 like you you'll like
[16:39] you'll just see like kind of a warning
[16:40] about it if it if you're running into
[16:42] the limits of the capacity. Um, but uh I
[16:46] think I've been able to do all of this
[16:47] on an F2.
[16:54] Let me link to this one too.
[17:01] And the question is, can we get this in
[17:05] the
[17:07] uh free trial?
[17:09] And let's find out.
[17:13] Um
[17:17] I think the answer is going to be no but
[17:19] we'll [laughter] let's confirm that. Um
[17:24] there's also
[17:27] okay let me look at these two
[17:31] capacity consumption
[17:33] capacity usage.
[17:37] Okay. So as as I suspected so data
[17:40] agents and any of the AI capabilities is
[17:43] not available in fabric free trial.
[17:52] Yeah. So yeah you will need to get um
[17:57] you know get your company to approve uh
[18:03] F2 capacity so that you can start
[18:05] playing around with it. Um but you know
[18:08] at at this level of pricing that's like
[18:11] compared to the amount we spend on
[18:12] tokens now
[18:14] that you know hopefully that's something
[18:16] that a company is willing to do so that
[18:19] you can start experimenting with this if
[18:23] you're working for a company right now
[18:29] if not there's also like yeah I think
[18:32] even the the I was going through like
[18:34] learn certifications
[18:36] Um there's various learn certifications
[18:38] but even those I think they
[18:42] you need to use I don't think they give
[18:45] you free access to try it. Where was the
[18:49] one I was doing? Um
[18:57] yeah this one I I had to use my own uh
[19:00] but this was helpful. This was like how
[19:02] I was uh doing some learning as well. So
[19:05] there's a bunch of like learn
[19:08] certifications. If you go to Microsoft
[19:09] learn
[19:11] uh certifications
[19:22] and then we can see we go browse search
[19:27] fabric.
[19:31] Which one was I trying to get? No, I
[19:34] think I was doing like
[19:36] uh where maybe I was doing the learning
[19:38] path
[19:40] reading.
[19:43] I was going through a fabric IQ learning
[19:45] path. Let's see if I can find it.
[19:48] Okay, we'll [clears throat] find it. Um
[19:51] all right, so there's a question about
[19:52] billing. Yeah, so I was just looking at
[19:54] the Ctology billing page. Um, so this
[19:57] one's like the
[19:59] that one's specific for ontology
[20:01] billing. But here you can see
[20:04] the um
[20:07] you know this one is the usage of
[20:10] ontology definitions.
[20:12] So each time the API is triggered by
[20:16] create update delete operations. So not
[20:18] read. Um so that's that's good. Uh so
[20:24] that it's a CU capacity units. Okay. And
[20:28] then uh ontology operations
[20:32] this is not currently in effect. Okay.
[20:34] Great. Um AI operations
[20:38] uh usage of AI for context reasoning
[20:41] query overtology.
[20:44] Um what would where would we be using
[20:47] that?
[20:50] So there must maybe with AI built into
[20:52] it. Um,
[20:55] yeah. So, if we're doing the
[20:58] ontology
[21:01] MCP, right? So, with the int MCP server,
[21:03] that's probably what we're referring to,
[21:04] right? So, we get the natural language
[21:06] query, natural language response. So,
[21:08] that is based off of tokens. So, yes, I
[21:12] would say this this here, I assume that
[21:15] that corresponding to this one here.
[21:21] Um and then we have
[21:24] graph cache storage. Okay, so the graph
[21:28] is when when we do the queries, you saw
[21:30] it use GQL. Um so presumably that's
[21:33] using this graph cache storage. Okay, so
[21:37] uh let's see a usage window and you get
[21:41] 30 minutes. All right, so you do want to
[21:43] kind of cluster things together if
[21:44] you're doing a bunch of editing. Sounds
[21:46] like you want to cluster that editing
[21:47] together because it goes in these 30
[21:49] minute increments.
[21:51] Um, and so you want to stuff it all into
[21:53] that same 30 minutes if you can. And
[21:56] then, um, operations
[22:00] and and that one has 20-minute windows.
[22:03] And then we have AI. Okay. So, um,
[22:07] do they talk about eachtology requests?
[22:11] Okay,
[22:14] interesting.
[22:16] It claims that's a background job.
[22:19] Little confused about that. Uh
[22:24] fabric capacity metrics app.
[22:29] See if I can open that.
[22:33] Okay.
[22:39] All right. How do we in Oh, I must be
[22:42] capacity admin. All right. So, I don't
[22:44] think I have access to that. Um, but if
[22:48] you're the admin, then you can add this
[22:50] app that will give you more information
[22:52] about what is going on.
[22:58] All right. And let me let me find the
[23:00] fabric IQ
[23:06] [clears throat]
[23:07] path
[23:12] here. Yeah, this is what I was doing.
[23:14] Okay.
[23:16] Um, you [clears throat] can see the ones
[23:17] that are purple is the ones I got
[23:19] through. Uh, but yeah, you could This is
[23:22] There's some good stuff there. Like cuz
[23:25] I was pretty brand new to to uh fabric.
[23:30] I think I did some of the earlier ones
[23:32] too, especially. Yeah. So, end to end
[23:34] analytics with fabric, getting started
[23:36] with lakehouses, right? So, there's a
[23:39] ton of ones here. Um, the UI, I will say
[23:41] like the UI is not exactly the same. So,
[23:44] I did kind of have to like poke around
[23:45] and figure out what the new UI was when
[23:48] I was following some of these because,
[23:49] you know, it's really hard with
[23:51] tutorials to keep them up to date when
[23:52] they refer to UI because when they have
[23:54] screenshots because UI is always
[23:56] changing. Uh, but there's a ton of
[24:00] training options here. Um, so what I
[24:03] did, like my tip was that, um, I think I
[24:05] was like going through like this one,
[24:07] right? You see I went through all this
[24:09] stuff and I opened up copilot on the
[24:12] side and like let me find um let's see
[24:16] uh yes all logged in okay data ware okay
[24:19] so I was like trying to understand it
[24:21] from my point of view yeah you can see I
[24:23] was asking a lot about like SQL I was
[24:26] like okay is it like cipher [laughter]
[24:29] so I was [clears throat] it's a similar
[24:30] questions as you know we were getting
[24:32] today like you know uh I asked like is
[24:34] GQL different from GraphQL so when
[24:36] you're going through these is like a
[24:38] learning path or documentation
[24:39] generally, it's super helpful to just
[24:41] pop open copilot um uh especially if
[24:46] you're just like feeling
[24:48] uh you know there's all this like custom
[24:49] terminology right um like what are
[24:52] trying to understand so I kept asking it
[24:54] to compare it to Postgress right because
[24:56] like I know Postgress well and I was
[24:57] like okay compare it to Postgress right
[25:00] uh you know or I'm struggling to
[25:01] understand data warehouses what are
[25:03] examples from other clouds or open
[25:05] source and so then it compared to at
[25:07] Google cloud and I've actually I've used
[25:08] BigQuery quite a lot right so that was
[25:10] actually quite helpful for me um because
[25:12] I my first job was at Google um so yeah
[25:15] so that's what I recommend just
[25:17] generally for learning is like you know
[25:19] you go through something but then um you
[25:22] know you can use LMS to help you make
[25:25] connections and to try and uh you know
[25:29] clarify things
[25:32] and related to you like that's the dream
[25:34] like you know there's a lot of people
[25:36] that are using LMS for learning right
[25:38] now in a bad way. Like because you can
[25:39] also use LLM to do your learning for you
[25:42] and you know that's bad and lots of us
[25:44] are doing that like to be fair like you
[25:46] know we do that I do that too where it's
[25:47] like oh I don't have time like I just
[25:49] need to get this done like figure out
[25:50] how to do this right but if you're truly
[25:52] trying to learn something then you can
[25:53] use LMS in this way that it it
[25:57] personalizes your learning journey and
[25:58] it helps connect to the things that are
[26:00] already in your head and deepens your
[26:02] understanding. Right? So that's what I
[26:04] would recommend like when you're when
[26:05] you are learning something you want to
[26:07] truly learn it is to you know when
[26:10] whenever you have like this question
[26:11] mark in your head like you know take
[26:13] that ask that question right like now
[26:15] you have somebody who you can um you
[26:17] know bounce your questions off of that
[26:19] like it's like the like the whole dream
[26:21] of learning is that ideally everybody
[26:24] would have a tutor and so if you can
[26:25] learn how to use um an LLM as your tutor
[26:29] then it can be really helpful as long as
[26:31] the LLM is is correct.
[26:33] and is grounded. Um, luckily like you
[26:36] know with most of our agents like with
[26:38] copilot these days is they can do web
[26:40] searches they they're back they can
[26:42] confirm their understanding. So that is
[26:45] what I would suggest there.
[26:48] Uh any other questions about fabric
[26:55] everything we covered? Let me bring open
[26:58] our slides again
[27:01] just as a reminder of what we talked
[27:03] about today.
[27:10] Otherwise, I'll just wait and see if
[27:13] there's any additional questions, but we
[27:15] can also close early today if we've
[27:18] answered everything.
[27:22] Let's see.
[27:25] Um, [clears throat]
[27:33] oh, let me also link to something else
[27:35] because let's see. Okay.
[27:39] IQ deep dive
[27:51] playing the agents. Okay, this one.
[27:53] Okay. So, yeah, I didn't unfortunately I
[27:56] didn't get to show doing a Foundry
[27:57] hosted agent with um with Fabric IQ. Um
[28:02] but there is
[28:04] information in this notebook here about
[28:08] how to do it. Um
[28:11] so if you are trying to make a foundry
[28:13] agent with with fabric um you know data
[28:17] agent uh the this is the what you can
[28:21] consult for how to add it to the
[28:22] toolbox. Um but you will need to have
[28:26] the fabric in order for this to work um
[28:30] and to be able to publish to teams. You
[28:31] would need the fabric to be on the same
[28:35] tenant as the foundry agent. Um so
[28:38] unfortunately I didn't have a tenant
[28:40] where I could both deploy agents and
[28:42] create fabric. I wasn't able to um show
[28:45] this but because that's the whole thing
[28:46] you have to remember is that with fabric
[28:48] we need to pass in a token for somebody
[28:50] who has permission to that workspace um
[28:55] and it's actually a user like it's a you
[28:58] it's like a user who's logged in right
[29:00] so if you were going to like make an
[29:02] agent and publish it from teams then the
[29:04] person using it in teams that logs into
[29:06] that agent would have to be a person
[29:08] that directly had access to fabric u so
[29:11] I don't know if that's really going
[29:12] going to be a use case that a lot of
[29:13] people do or if people are going to be
[29:15] putting uh you know basically like
[29:18] backends like proxies in front that um
[29:21] you know that are accessing fabric. So
[29:23] that'll be interesting to see.
[29:30] Uh okay so Kenne says looking at foundry
[29:33] tools you see fabric one lake and data
[29:35] agent where does the graph fall into
[29:37] there's no direct tool for graph right
[29:39] so we have um you can do ontology so
[29:42] basically you add the ontology um I
[29:45] think this example here yeah I think
[29:46] they tend to show data agent but you
[29:48] would add it the same way but just with
[29:50] the ontology MCP server instead um but
[29:54] graph yeah so you can't directly add
[29:56] graph so the the things you can directly
[29:58] add is fabric hq ontology or fabric IQ
[30:01] data agent. Um
[30:05] uh but graph if you want access to graph
[30:09] you either need to um you would either
[30:12] need to build like a custom tool somehow
[30:14] or you just add it as a data source to
[30:16] the data agent right um because there's
[30:19] no direct there's there's no yeah direct
[30:23] there's no MCP server for graph right
[30:25] the only MCP servers we have are um data
[30:29] agent and
[30:32] uh So here right this is fabric IQ and
[30:35] this example does show a data agent but
[30:39] I was told that we should be able to use
[30:41] ontology
[30:43] as well. Uh just you just specify the
[30:46] anttology URL
[30:50] for learning about ontology. Um there I
[30:54] think I did do antology
[30:57] training here
[31:00] Microsoft. Yeah, I think I did this one.
[31:02] Create an anttology. Um, so this was
[31:04] helpful. I like this one. Um, or you can
[31:06] do the, you know, you can go through the
[31:08] documentation obviously like the
[31:10] documentation's great, too. Um, here's
[31:12] the documentation, but um, yeah,
[31:14] sometimes the learning paths are a
[31:16] little more straightforward when you're
[31:17] brand new. Um, okay. So, Damian asks,
[31:23] uh, oh, and the anttogy playground.
[31:24] Thank you for plugging that. I had like
[31:27] I had that on my list to remember to
[31:28] plug and did not. But yeah, that's fun.
[31:31] Um, let's [clears throat] see. Can we So
[31:33] Damen asked, "Can we use a different
[31:34] agent framework like Linkchain or
[31:36] Pedantic AI with Fabric IQ and the rest
[31:38] of the Microsoft IQ catalog?" Um,
[31:42] you can. The question is whether you're
[31:44] trying to integrate with Foundry hosted
[31:45] agents. Um, or you know where what are
[31:48] those agents doing? Where are they
[31:50] getting their tokens from? Like like for
[31:52] a local agent, you know, it's easy to do
[31:54] any of this stuff. um it's just once you
[31:56] deploy them, you have to figure out
[31:58] where where it's going who's going to
[32:00] host it and where it's going to get its
[32:01] tokens from. How are you going to get a
[32:03] user token for it? Right? So that that's
[32:05] the big question, right? But um let me
[32:08] get like a pedantic AI demo for example.
[32:11] Um
[32:12] so if I was going to do um uh let's see
[32:17] like pedantic AI
[32:20] um oh wait, pant. See, I want this one.
[32:26] Okay.
[32:28] Examples. Pyantic AI.
[32:31] Right. So, I would do it as an MCP
[32:34] server. Yeah. So, we would we would add
[32:36] it as an MCP server. Um, so we'd say
[32:39] like, you know, uh, point this MCP
[32:42] server at at the URL and then we need to
[32:46] pass in that token, right? So, this is
[32:48] the tricky thing is just getting that
[32:49] token. So, as long as you have a way of
[32:51] getting that token, you're all good. You
[32:53] can do anything, right? because these
[32:54] are MCP servers. So, you know, you you
[32:57] just construct an agent that points at
[32:59] that server and you give it the token,
[33:01] right? Um, now getting that token can be
[33:04] easier can be is easier said than done.
[33:06] So, um, now um, so that's lang chain is
[33:11] similar, right? There's link chain MCP.
[33:14] Oh, link chain. Let me do MP
[33:17] HTTP. Uh, let's do the GitHub one
[33:20] because it has O in it. Okay. Um, so
[33:23] this is going to look really similar,
[33:24] right? We have this MCP server and we
[33:26] give it a token. Okay. Now the next
[33:29] question is where are you going to host
[33:31] it? If you're going to host it on
[33:32] Foundry hosted agents, you need a
[33:34] responses API adapter. So for lang
[33:37] chain, you're going to get that from the
[33:39] link chain Azure
[33:42] uh project. It has the responses adapter
[33:47] um in here. Let me find the the right
[33:50] example. Samples
[33:54] hosted lingraph hosted agents. Is it
[33:57] going to be this one?
[33:59] Uh
[34:00] yes. All right. So for that you you have
[34:03] to use this responses adapter if you
[34:05] want to be able to Yeah. So then I would
[34:08] right now I would go you know that
[34:10] route. Um
[34:13] and I think they even Yeah. They do also
[34:15] have a foundry toolbox um you know
[34:18] wrapper here. So your best bet if you're
[34:21] choosing you know I love pedantic AI but
[34:23] we don't have like a special package for
[34:25] pedantic and responses API um adaptation
[34:28] yet. So you're going to have more
[34:30] success using lang chain. If you're
[34:32] going to use responses API then uh with
[34:35] sorry if you're going to so if you use a
[34:36] link chain API just AI just use
[34:38] everything here. If you're going to do
[34:39] pidantic AI, you need a um either you
[34:43] need a responses adapter or you need to
[34:45] be happy with just using invocations
[34:48] API, which means um just basically
[34:52] having a URL to to hit up the agent. Uh
[35:00] um so you know generally there's two
[35:02] protocols responses protocol that one
[35:04] requires an adapter, right? So this is
[35:06] what I've been using for agent framework
[35:08] and I just showed you the link chain one
[35:09] that we um have in our link chain Azure
[35:13] repo or you can do invocations. So
[35:15] invocations just it's just HP request
[35:18] and response, right? So you could you
[35:20] could wrap up a padantic AI when it
[35:22] invocations. It means you're not going
[35:23] to have as like I don't know that like
[35:26] publish to teams would work at that
[35:28] point, right? Because a lot of the stuff
[35:30] in Foundry does assume that you're using
[35:32] responses protocol that is like our
[35:34] interoperability layer. So once you move
[35:37] to invocations then you may lose some of
[35:40] those features, right? Um I don't know
[35:42] exactly which features you're going to
[35:44] lose, but I think you're definitely
[35:46] going to lose some features. Um so yeah,
[35:49] that is it's a little
[35:52] little um bit of a decision framework.
[35:57] I open my
[35:59] boundary slides.
[36:04] Just looking back at the
[36:08] hosted agent.
[36:10] Okay.
[36:12] Right. So, here's the issue is that you
[36:14] know when we do these hosted agents is
[36:16] that it works best if we have this
[36:18] responses API adapter and the question
[36:20] is just where is that going to come
[36:22] from?
[36:25] Um Pablo asks is this repository
[36:27] recommended one for using with agents?
[36:30] Um
[36:32] that's a good question. Maybe if some or
[36:35] Josh
[36:37] um let's see are familiar with this one.
[36:40] Microsoft Fabric Skills.
[36:42] Uh, okay. So, these are skills you can
[36:44] install. You can install it as a plugin.
[36:47] Um,
[36:49] so try to make it easy. Uh, I didn't try
[36:53] this when I was using it. I just just,
[36:56] you know, when I work with Copilot, I
[36:58] just point it at documentation. Um, and,
[37:01] you know, it did fine there. But this is
[37:03] probably, you know, would be a more
[37:04] efficient efficient approach here. Um,
[37:10] so
[37:11] pro and probably it's probably it looks
[37:14] like it's probably from the fabric team.
[37:16] Um, you know, it's worth a shot. I mean,
[37:17] with skills, right? Like, um, I'll use
[37:22] them until they're getting like it's
[37:24] hard to know whether ski like sometimes
[37:26] skills actually can confuse things if
[37:29] they're not like up to date, but you can
[37:30] see this one is actually looks pretty up
[37:31] todate. So, that's good. Uh, so I think
[37:35] it's always worth a worth a shot. Um,
[37:37] and if it doesn't working, you can
[37:38] uninstall it. Like I actually
[37:40] uninstalled some skills yesterday, um,
[37:43] that I felt were getting in the way of
[37:45] something I was trying to do, like
[37:46] because they were getting because
[37:47] sometimes skills get called too much,
[37:49] right? But I think these ones are pretty
[37:51] specific. So, um, hopefully that
[37:53] wouldn't be the case. Oh, there's a lot
[37:55] of skills here. You can also just
[37:57] install specific skills. You don't have
[37:59] to install all of them at once. Like you
[38:00] can you could do a um a peacemail
[38:03] install if you're right. If you're just
[38:04] doing like, you know, you could just
[38:06] bring in those skills.
[38:11] I know. Let's see what instructions say.
[38:13] So, they have it as a plug-in, but you
[38:15] can do Yeah, you Oh, and they even have
[38:17] bundles. Wow. Fancy.
[38:30] Oh, okay. Okay, so Josh recommends
[38:31] install the fabric extension on VS Code
[38:34] and that will set up everything for you.
[38:36] Okay, I did not get the fabric
[38:38] extension.
[38:39] So you can search for
[38:43] fabric here,
[38:45] not the theme. So this one
[38:51] and so I assume this is the extension
[38:53] fabric.bscode fabric
[38:56] and then it's from Microsoft.
[39:00] Oh, and there's also an MCP server.
[39:03] That one is distinct.
[39:06] Uh,
[39:08] so this is this probably
[39:11] has the skills with it.
[39:16] So, this is like useful to just to have
[39:19] like, you know, it's going to be
[39:20] querying your data, right? This is not
[39:22] the MCP server you'd be using for like
[39:24] the agents you're building, but this is
[39:25] an MCP server that's helping you answer
[39:28] your questions as you're developing with
[39:30] fabric.
[39:32] Oh, so you're saying fabric extension
[39:33] includes MCP. Okay. All right. So, yes.
[39:38] Okay. All right. So, if you get this
[39:40] fabric extension, then that should get
[39:44] bundle everything together for you.
[39:50] Let's see if I can link to this in the
[39:52] There we go.
[39:58] There we go.
[40:17] I guess I could install it and see. All
[40:19] right. Pre-release.
[40:21] Okay. Fabric.
[40:24] Sign in.
[40:31] Oh, and then Okay. So, this pops up. So,
[40:34] it pops up. Enhance. As you see down
[40:36] here, enhance your fabric copa
[40:37] experience by installing the fabric MP
[40:39] server extension. Okay, so when you
[40:41] install the extension, it'll prompt you
[40:43] to install the fabric MCP server
[40:46] extension as well.
[40:52] It's still kind of loading. Yeah, it's
[40:54] still activating. You see down here it
[40:55] says it's activating. So, it's still
[40:56] activating. All right, it's getting
[40:58] activated.
[41:01] Let me see if I can Let's see if the
[41:04] extension
[41:06] uh is installed over here.
[41:10] Okay.
[41:13] Okay, that was my ontology one.
[41:17] Um, fabrictology.
[41:22] No, I've got maybe too many. Oh, here we
[41:25] go. Fabric MCP. Okay. All right. So,
[41:28] here you can see the fabric MCP server.
[41:30] Oh, wants to sign in. Very good. And I'm
[41:33] going to sign this one. Continue. Okay.
[41:37] Oh, good. All right. Now everything's
[41:38] signed in. Okay. So, you can see um
[41:43] my workspace, Pamela's test workspace.
[41:46] There we go. That was one I was doing in
[41:47] the training. Um
[41:52] yeah, so we got lots of workspaces
[41:53] there. Then
[41:57] um then we have the fabric MCP server.
[42:01] Uh and that one has a ton of tools in
[42:04] it. Um okay, let's just see where my
[42:09] fabric ando
[42:13] um lakehouse
[42:15] works. I wonder if I can find it.
[42:19] I've got so many MCP servers. I'm going
[42:21] to have to decide. Uh yeah, as Pablo
[42:23] pointed out, yeah, if you are using an
[42:25] agent besides VS Code and GitHub
[42:27] copilot, then uh you can, you know, use
[42:30] those you can install those skills for
[42:32] any agent. So that's a good point.
[42:36] Okay. All right. It wants
[42:39] Let's see this going to work. All right.
[42:43] So it is running.
[42:45] It's searching.
[42:47] Yay. It found it. All right.
[42:51] Sweet. Oh, good. Oh, yeah. This is where
[42:53] it is. Thank you. [laughter]
[42:57] That's great.
[42:59] That's super helpful.
[43:03] So, we can see that semantic model. Oh,
[43:05] yeah. Because Yeah. And Bernard was
[43:07] asking how I get those URLs inv. I just
[43:10] write out these URLs um after I'm done
[43:12] processing just for convenience, just to
[43:16] have these quick links. But you could
[43:17] also now of course use this extension
[43:20] and um
[43:23] and uh let's see can you open in fabric
[43:26] right so you can do like open in fabric
[43:28] and then go to it
[43:33] and that would have been
[43:36] uh a pretty slick way to to open
[43:39] everything actually. Here we go. All
[43:42] right we have another recommendation
[43:44] from Josh.
[43:46] Um, I think you should also point to if
[43:49] you have a link to your comic handy. I
[43:52] like the comic that Sam made. Um, I
[43:55] think it was some leaves. I don't know
[43:57] if I can find it. Okay, so Fabio Fabio.
[44:01] Okay. Uh, the agent native CLI for
[44:03] Microsoft Fabric.
[44:06] Okay, there we go.
[44:12] Why Fabio
[44:13] a sub a supererset of other CLI? Okay,
[44:19] so there's another great tool for you to
[44:21] use. Let's see if Somal is going to link
[44:23] to the the uh the cool comic that they
[44:27] made. [clears throat]
[44:48] always typing. Um, and so remember I
[44:50] didn't show everything in fabric IQ. So
[44:52] if you go to the overview, you'll see,
[44:55] you know, we I try to cover a lot, but
[44:57] we didn't talk about plan. So I haven't
[44:59] I have not even gone through that at
[45:01] all. I really don't know anything about
[45:02] it. Um, so you should check out that as
[45:05] well to see if that's useful for you.
[45:08] And then um didn't do operations agent
[45:11] that um uh but I think that like makes
[45:15] sense that you would want to have like
[45:16] we have like these sort of things also
[45:18] in like um app insights and Azure
[45:20] monitor right things that are like in
[45:22] your Azure portal like just monitoring
[45:25] things like I think this is a general
[45:27] best practice is to be running these
[45:29] kind of meta agents that are watching
[45:32] for issues.
[45:34] Oh. Oh, and there's a second episode.
[45:37] Yay. Okay. All right. This is what I
[45:39] wanted. Right. So,
[45:43] to confirm, this is a great way of
[45:45] confirming your understanding is if you
[45:46] can read this comic that they put
[45:48] together and if all everything makes
[45:51] sense to you. This is this is what I did
[45:53] was I went through and I was like, "Aha,
[45:56] I know. I know what he's talking about."
[45:58] I don't think I saw the new one.
[46:01] U did I see this one? What is ontology?
[46:07] Maybe I did read this one. I think
[46:09] they're great. Oh, look. Wait, this is
[46:11] all
[46:14] I did not see this.
[46:21] I love this so much.
[46:24] We read a lot of graphic novels in our
[46:26] house now, too, with my kids. So, I like
[46:29] the format.
[46:30] >> [snorts]
[46:30] >> All right. So, check those out and you
[46:33] know, make sure you know hopefully after
[46:36] today and your own experience with
[46:38] fabric all that make sense.
[46:42] Cool. All right.
[46:45] Okay. Uh well, thank you everyone.
[46:49] Uh I see Pablo's typing. See if any
[46:54] final questions.
[47:02] Okay, so the question was, is this a
[47:05] good source of information? This might
[47:06] just be the same docs that are on learn.
[47:09] Let's see. Fabric docs, IQ,
[47:12] is this just
[47:14] um
[47:17] this is probably the same docs you see
[47:19] on learn.oft.com. Like our docs are, you
[47:22] know, public based off markdown files.
[47:24] So if you go, let's see, let's try to
[47:27] match it up to um the learn learn doc.
[47:32] Uh yeah.
[47:34] Yeah. So I think this is just the the
[47:36] the repo that holds the docs for learn,
[47:41] right? You can see this is this doesn't
[47:43] get rendered. This is the YAML front
[47:45] matter. Um yeah, it looks exactly the
[47:49] same. Yes. Yeah. So if you ever find a
[47:53] bug in the docs, then you can send a PR
[47:56] um and uh and try to fix it.
[48:08] All right. Okay. Well, thank you
[48:10] everyone for joining today and watching
[48:13] the session and bring your questions.
[48:15] Thank you so much to Samaliz and Josh
[48:18] for joining in the chat and being the
[48:20] authorative source on the answers and
[48:23] for sharing all these additional
[48:24] resources as well uh so that we can all
[48:27] become fabric experts. Um I hope that
[48:29] you're all able to uh experiment with
[48:33] fabric. Um I know it's a little hard
[48:35] with fabric IQ because you do need to
[48:36] start at F2. Um but hopefully you can
[48:38] get access to an F2 and start playing
[48:42] around. Um, or maybe you can come to
[48:43] like one of our Microsoft conferences
[48:45] and come to labs where we often like,
[48:47] you know, have these things set up for
[48:49] you for you to try out.
[48:51] All right. Well, that is the end of our
[48:56] series. Um, when is the next time I'll
[48:58] see you? Uh, we are doing an MCP live
[49:01] stream on September 9th. Uh, so do join
[49:05] that if you're interested in MCP. We
[49:07] used a lot of MCP during this series as
[49:09] you've seen is very much a compatibility
[49:11] like layer that we're using like a
[49:13] protocol for across all of our services
[49:15] now. Uh and then we're also doing a live
[49:18] stream about sandboxes on container
[49:20] apps. So that um that should be a good
[49:24] one. Um oh and this co-pilot dev camp uh
[49:27] that we're going to be talking about
[49:28] Foundry IQ again. Um but also some other
[49:31] stuff there for the rest of the day. So
[49:34] uh yeah, lots of lots of things coming
[49:36] up.
[49:37] So hopefully we'll see you in the
[49:39] future. And then of course I have office
[49:40] hours every week uh Tuesdays at 11. So
[49:44] uh oh I'm going to have to cancel next
[49:47] week. I'm finally taking a vacation like
[49:48] a real vacation. So I think my flight
[49:52] leaves before that. So I think I'll have
[49:55] to cancel next week or move it to
[49:56] Monday. Um so we'll see. I'll I'll see
[49:59] what I can do for next week. All right,
[50:01] that's all. Thank you everyone. I'll
[50:04] publish the recording for this office
[50:06] hours to um to this to this uh wiki page
[50:12] here. So uh just check that in a day and
[50:16] you should see the write up for um the
[50:20] presentation and also the office hours
[50:22] recordings and writeups here as well.
[50:26] All right, bye everyone.
