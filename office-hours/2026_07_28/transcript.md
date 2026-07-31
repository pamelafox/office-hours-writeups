[00:00] Welcome everyone to our office hours for
[00:04] the Foundry IQ session from the
[00:07] Microsoft IQ deep dive. And uh yeah, I
[00:11] know there were lots of lots of good
[00:13] questions there. Um so hopefully you've
[00:17] come with your questions. Um if you just
[00:22] wandered into this and you don't know
[00:23] what we're talking about,
[00:26] um let me give you some links.
[00:31] Uh so you can see what we're talking
[00:32] about there. All right, great. So we
[00:36] have our first question from Nambdi. Um
[00:39] yeah, if you had a question uh yeah,
[00:43] just try to repeat it in the chat. Um
[00:46] uh since I haven't memorized the
[00:48] questions that were in the live chat.
[00:50] Okay, so uh yeah, can we talk briefly
[00:53] about data privacy? Yeah, that's a great
[00:55] question. And I didn't have time to
[00:56] really talk about that at all today, but
[00:58] that's actually a really big advantage
[01:01] of um Foundry IQ. Now remember, Foundry
[01:05] IQ is really secretly Azure AI search.
[01:07] So when you're looking for this, you're
[01:10] actually going to want to search for
[01:11] Azure AI search. Um
[01:14] um so first we can, you know, talk about
[01:17] um a few different ways, right? So um
[01:20] you know Azure AI search has this
[01:22] built-in idea of doing um document level
[01:28] access control and the way you do it is
[01:31] when you set up the search index you
[01:34] specify uh which of the fields oh
[01:37] there's a bunch of stuff here but the
[01:39] the way I've done it is that you specify
[01:40] like hey on this search index this is
[01:42] the oid field and this is the group
[01:44] field. Uh so this is for Entra, right?
[01:47] So you'd say like this is the Entra OID
[01:49] and this is the Entra groups. And so you
[01:51] would store that for each document chunk
[01:53] in the index. And then um and then you
[01:57] actually just pass the like the the user
[02:00] token when you do the search and that
[02:03] will make sure it only gets back chunks
[02:06] that uh you know pertain to that user,
[02:09] right? Um
[02:11] so that's that's one of the big uh big
[02:14] approaches. So that is like really
[02:16] helpful if you're you know you're
[02:18] indexing a bunch of documents from some
[02:20] arbitrary source and you need to make
[02:22] you know set you need to have like
[02:23] really full control uh over who can see
[02:27] it. Um now your other option is to
[02:29] basically you know like using um you
[02:32] know you can use a remote source right
[02:34] so if you're using work IQ work IQ
[02:36] requires the user's token so work IQ is
[02:38] only ever going to give back information
[02:39] from the user. So that would be the
[02:42] other approach is just using a remote
[02:43] source and you're passing in the user
[02:45] token that obeys it. Okay. But I can see
[02:46] Nambi said um if the client doesn't want
[02:49] PII or sensitive data going to the LLM.
[02:54] Um
[02:56] well that's a good question. So if you
[02:59] don't want data going to an LLM like one
[03:02] option is to try not to use an LLM at
[03:04] different stages right? So, you know, if
[03:05] we look at this, right, uh, if we're
[03:07] doing minimal, you're at least you're
[03:09] not configuring the,
[03:12] um, you don't configure the knowledge
[03:14] base with an LM. So, nothing's getting
[03:15] sent to an LM there. But um ultimately
[03:21] ultimately in order to answer a question
[03:24] you know if if depends what you're you
[03:25] know if you're just doing retrieval then
[03:27] probably you'd want to do minimal to to
[03:29] minimize the number of you know services
[03:31] that your data goes through then you'd
[03:33] want to you know do minimal here or even
[03:35] just a basic search call. Um, but if
[03:37] you're trying to build an agent that can
[03:40] answer questions or or, you know, take
[03:42] actions
[03:44] and they don't want PI going to the
[03:46] agent, then,
[03:49] you know, you have to figure out like,
[03:50] wait, can I still answer the questions
[03:52] if I don't send to the PII? So, you
[03:54] could use like I mean, there are like um
[03:56] I think we have like a PII
[03:59] detection service on Azure. Don't
[04:01] remember what it's currently called. So
[04:02] you could like do a little, you know,
[04:04] strip some stuff out, you know, before.
[04:08] Um, so, oh, this is what it's called
[04:09] now. Azure language and foundry tools,
[04:11] right? Um, so you could do redaction
[04:15] like there's um it sounds like there's a
[04:19] redaction policy. Um, so that would be
[04:23] that would be one approach if like if
[04:25] you really needed to. Um,
[04:29] uh, Bernard is saying, "Oh, we could use
[04:31] a local LLM." Sure. If you were doing
[04:34] the agent locally on your machine, then
[04:36] then yeah, then you know, you can do
[04:38] lots of things uh locally. Um,
[04:43] uh, I see and Lee is also recommending
[04:45] Foundry local, right? Um so so there you
[04:50] know there's a question of whether so
[04:52] you could have the foundry local um
[04:55] still reach out to the foundry IQ
[04:57] knowledge base you know and only use
[04:59] that in in minimal node mode and then
[05:01] you know you have less concern about how
[05:03] many services are seeing your data. Uh
[05:06] it's also worth pointing out that like
[05:07] as you're opening like we do do
[05:09] generally have a pretty good privacy
[05:11] policy. I'm sure your your um your
[05:13] people know that but I don't think
[05:14] everybody knows that. So I just want to
[05:16] point that out that um we do generally
[05:19] have a very good privacy policy right
[05:21] like your prompts are not available to
[05:22] other customers they're not available to
[05:24] open AI or other models they're not used
[05:26] to train any models without your
[05:28] permission right um so you know I I do
[05:31] think we have one of the best privacy
[05:32] policies uh across industry so it's just
[05:36] worth looking
[05:38] um you know that people know about that
[05:42] okay yeah and the other question was
[05:44] guards against indirect prompt
[05:46] injection, right? Um
[05:50] so you know with Foundry um there is the
[05:53] Foundry guard rails here, right? And we
[05:56] have got the default guard rails those
[05:58] are applied on the models themselves and
[06:01] those ones um contain you know they have
[06:05] like a you know this default
[06:08] um you know default things they allow
[06:09] but then we can make our own. So when we
[06:10] customize our own guard rails, we can
[06:12] say which type of risks um you know
[06:15] jailbreak is always detected but you
[06:17] also want to add on indirect prompt
[06:19] injection because that's the one that
[06:21] comes from um you know like websites
[06:24] right so if you're doing like web IQ um
[06:26] an indirect prompt injection is one
[06:28] that's in the data or the tool response
[06:30] right so uh you would want to turn that
[06:33] on and you decide you know what you're
[06:35] going to do with that information uh the
[06:37] content harms you can make custom block
[06:39] lists
[06:40] You can look at protected material. Oh,
[06:43] there is a PII now. Interesting. Okay.
[06:46] Um, so you could turn on that if you
[06:48] were concerned about that and didn't
[06:49] realize. Oh, look at this. There's a lot
[06:51] of stuff. Wow. Look at this. This is
[06:54] new. Look at Wow. All done. Okay, that's
[07:00] pretty cool. Um, these are kind of
[07:02] evaluation stuff. This is going to This
[07:04] one will I would say add probably add
[07:06] latency. um because these are actually
[07:08] running LM as a judge. So I wouldn't
[07:10] necessarily run those uh in line. And
[07:14] then network controls. Oh, so this
[07:17] applies to hosted agents. Interesting. I
[07:20] have not seen this one at all. Okay.
[07:22] Egress rules.
[07:24] Fancy. All right. There definitely some
[07:26] new stuff here that I haven't seen yet.
[07:28] Um
[07:30] uh so you know, I would look at that. Um
[07:34] uh but also that you should just like
[07:36] you know your agent can only do as much
[07:38] as you give it access to. So as general
[07:41] rule like if you don't want it to be
[07:42] able to send emails don't don't give it
[07:44] access to send emails right um or
[07:47] require approval for sending emails or
[07:50] send that through like another like LLM
[07:52] check to say like hey it's about to send
[07:54] an email like am I comfortable with that
[07:56] right? Um,
[08:00] so I think there's lots of different
[08:01] approaches you can use there, but
[08:03] definitely, you know, check out the
[08:04] guardrails first because this is going
[08:05] to apply at the at the model level. So,
[08:08] you know, as long as you you set up the
[08:10] guardrail, you assign it to the model,
[08:11] you use that model for your agent, then
[08:14] you know that you know the mo whenever
[08:17] the model is called, it's going to look
[08:18] for all these things.
[08:21] All right, let me make sure I can look
[08:23] at other people's questions as well
[08:25] because I know there's quite a few.
[08:28] Um,
[08:34] all right. So,
[08:39] so Pablo says
[08:41] um if for if for each knowledge source
[08:44] we create and all the services touch the
[08:45] data are they located in our tenant or
[08:47] can we ensure in which country region
[08:50] they are located? Web IQ is global. Um
[08:55] so if you're using web IQ right like the
[08:57] remote knowledge sources like that's
[08:59] going to depend on each of the sources.
[09:01] So I know web IQ is a a global service
[09:03] because people are at least last I
[09:06] checked um because people were asking
[09:07] about that. Um and I think it it is
[09:10] global and maybe architecturally has to
[09:12] stay global but you know um we'll see.
[09:15] Um
[09:17] uh and then otherwise like then that you
[09:19] know things should be um pretty
[09:22] region restricted um
[09:27] uh because I know that like reranking
[09:29] models those are per region because uh I
[09:32] know like when they're doing like
[09:33] rollouts of the new ranking models
[09:35] they're like oh it's in this region or
[09:36] not this other region. So I you know I
[09:39] we'd have to I guess double check all
[09:40] the um documentation but I believe for
[09:43] Azeri search
[09:46] um
[09:48] what would it call residency I think
[09:50] everything's going to be pretty like you
[09:53] know per region um but if if you've seen
[09:55] otherwise
[09:57] you know let me know um so region
[10:00] deploys
[10:02] right um so I think this is going to
[10:05] yeah and this shows you like which
[10:07] services are available in different
[10:09] regions, too.
[10:11] Um,
[10:12] as far as I understand, they should all
[10:14] be region specific as as long as they're
[10:17] not remote services.
[10:21] Okay, let's see.
[10:27] Okay. So, Max,
[10:29] so Max says they are using Azure AI
[10:33] search with Azure current content
[10:34] understanding to detect the document
[10:36] type, extract key fields and store them
[10:38] in a relational database. What would be
[10:40] the best approach to add a chat for the
[10:42] user to query their documents? Should
[10:45] you add the database, the relational
[10:47] database as a data source or the raw
[10:50] files as the data source? Well, I think
[10:52] it depends on their questions. You could
[10:54] add both, right? So I, you know, it
[10:56] really depends on what questions the
[10:57] user is going to ask. So you're going to
[10:58] want to send up some, you know, emails
[11:00] for that and some um example questions
[11:03] that people are asking. But in like one
[11:05] potential approach is that you could add
[11:07] both. You could have a tool that can
[11:08] query just the extracted data. Uh and
[11:11] you could have a tool that could query
[11:13] the original documents and you know and
[11:17] and or those could be a knowledge base,
[11:19] right? Where you have multiple knowledge
[11:20] sources. um uh because you might find
[11:24] that it's helpful to to have that
[11:26] extracted data, you know, because it's
[11:28] like, you know, you you extracted it,
[11:29] it's clean. Um your other approach is
[11:32] that you could take that extracted data
[11:34] and then you could add it as like
[11:35] basically metadata fields in the chunks
[11:37] in an Azure AI search index so that when
[11:39] it it comes back, it comes back with
[11:41] both uh you know like the text chunk and
[11:44] the um and the metadata. Um this is
[11:48] called like content stuffing or content
[11:50] expansion. has different names, but you
[11:52] know there you know you have both this
[11:54] like unstructured chunk of text, but
[11:55] also you have some metadata like this is
[11:58] from page number five, this is from this
[12:00] section heading, this is from this date,
[12:02] right? And it's just you're giving more
[12:04] information to the LLM um to help answer
[12:07] it. So I think there's a lot of ways you
[12:08] could go about it. I would just start
[12:10] experimenting. Set up some of eval, you
[12:13] know, like 50 different questions that
[12:15] show like would be a range of questions
[12:17] to see, you know, what results you get.
[12:20] um you don't really know until like once
[12:22] you set up evals with you know enough
[12:25] representative queries and really start
[12:28] running those evals then you start to
[12:30] see get a feel for what's really working
[12:32] right like don't test your solution with
[12:34] just like three sample questions because
[12:36] then it's going to work great for those
[12:38] three sample questions and then who
[12:39] knows how it's going to work beyond that
[12:41] right so you know set up a good
[12:43] representative data set for your emails
[12:48] um Okay, let's see.
[12:52] Does Foundry IQ handle ASPX based
[12:55] SharePoint content? Well,
[12:58] um, you run into the issue path with
[13:00] copilot failing to reliably retrieve.
[13:04] H, okay, let's look at the So, with
[13:07] SharePoint, I knew the SharePoint
[13:08] question would come up. Um, uh, it
[13:12] always it always comes up. Um, so let's
[13:14] see. So, with SharePoint, there are
[13:15] multiple options, right? So um you know
[13:20] we've got one of them is the index
[13:22] knowledge source right so Azure search
[13:25] does have an indexer particular for
[13:27] shareepoint where you can say like hey
[13:29] here's my shareepoint and you're going
[13:31] to index it right and when we're
[13:33] creating an index we are making a copy
[13:36] right um and you know the advantage of
[13:39] that is that we're going to get really
[13:41] you know we can if we're making copy we
[13:43] can you know we can make our own
[13:45] customize the injection right so if
[13:47] we're having an issue with with you know
[13:49] the the how the data is being ingested
[13:52] in theory we can build our own ingestion
[13:54] for it right um there is like a you know
[13:56] a built-in ingestion for it um so here
[13:59] you can see like how you can like set it
[14:00] up like we're making this SharePoint
[14:02] knowledge source D
[14:05] um
[14:07] and um you know we c we can also enforce
[14:10] those document level permissions we
[14:11] talked about before uh oh it looks like
[14:14] you can get images
[14:17] Um, what I wanted to see was the whether
[14:20] it talked about the file types.
[14:24] Uh,
[14:26] does it say here?
[14:32] Um,
[14:36] create a knowledge source. Check
[14:38] ingestion.
[14:40] Um,
[14:44] I don't know. It's not really mentioning
[14:47] the file format in particular here. So
[14:50] we have to check on that. Um so that's
[14:54] that's one option. There's also you'll
[14:56] also see this one SharePoint. This is a
[14:59] remote one. I don't I wouldn't
[15:03] necessarily recommend this one. Oh, this
[15:04] does talk OSBX. Okay. You can index
[15:06] modern starting and set.
[15:10] Okay. This one does have, but this was
[15:12] probably what you were just talking
[15:13] about with copilot because this is
[15:15] basically the co-pilot indexer. So, I
[15:18] wouldn't necessarily recommend this. I
[15:20] don't know. I don't know how what this
[15:23] is still in preview. I don't know
[15:24] whether it's like it's going to be
[15:27] longterm like has long-term sticking
[15:29] power because now we've got work IQ,
[15:31] right? So, I think these days the two
[15:33] options we'd recommend people checking
[15:35] out is like work IQ, which you know is
[15:38] going to talk about tomorrow. um or
[15:41] doing the indexer yourself. Um
[15:44] you you know you can look at this option
[15:47] here. I think you'll find that if
[15:48] co-pilot was having issues, this is the
[15:50] co-pilot indexer, so it's probably going
[15:52] to have the same issues. So then, you
[15:54] know, I would um I would I would say
[15:57] that um you don't necessarily want to
[15:59] use it. So yeah, so I would I would look
[16:02] at work IQ or index it yourself. Um, I
[16:08] think those are going to be your two,
[16:10] you know, your two best future
[16:14] future thinking options. Um, and yeah, I
[16:18] know generally co-pilot retriever, um,
[16:21] this one, uh, had some, you know, some
[16:24] has some quality issues. Uh, so I would
[16:28] guess that that's what you're running
[16:29] into.
[16:34] Uh, let's see. So Bernard asks about the
[16:37] document level access control. Um is the
[16:40] so you're saying the permissions to
[16:41] access the data is checked at query
[16:43] time. Is it cached? If somebody's
[16:44] removed from an on group, is there delay
[16:46] with the group update for rag queries?
[16:48] That's a good question. Let me give it.
[16:51] Did we talk about delay in here?
[16:54] Um is it cache?
[16:58] Um
[17:00] had query time. Yeah.
[17:04] I don't think we I don't think it's
[17:06] cash. Let me Okay, I'll go. I'm got to
[17:09] start asking double checking things with
[17:13] with um the Foundry IQ team. Make sure
[17:17] I'm representing it. Um
[17:21] for security
[17:25] our entropy cash
[17:28] or always refresh for eighth grade
[17:33] for region res.
[17:45] All right. Um, okay. Um, I'll check to
[17:49] make sure. Um, I think they they're
[17:51] doing the check on demand.
[17:54] Uh, Nambdi asked, "Can you apply the
[17:56] guardrails to LMS that are not hosted on
[17:58] Azure Foundry?" Yes. So, there is also a
[18:02] um a separate service. Yeah. And
[18:04] somebody already applied. Um, uh, oh
[18:07] well. Yeah. Well, Foundry models always
[18:08] come with Foundry guardrails applied,
[18:11] but um
[18:14] uh Foundry
[18:16] uh guard rails service. It used to be
[18:19] called the Azure OpenAI content service,
[18:22] but to remember what it's called now. Um
[18:25] we should be able to
[18:28] third party guided guard third party
[18:30] guard route. Guided guard route. What is
[18:32] this?
[18:33] Um, I'm looking for Okay, let's see if I
[18:36] As you're opening a content safety
[18:38] service, right? This is what it used to
[18:40] be called when I was standing alone. So,
[18:42] let's see if I can find it that way.
[18:45] Right. Um, prompt shields.
[18:49] Custom detection.
[18:52] Okay, maybe I don't know if I know Lee's
[18:55] in the chat. If Lee remembers what the
[18:56] current status of all this is. Um, so
[18:59] there is, you can see this is a
[19:01] standalone service here, this content
[19:02] safety service. What I'm not sure of is
[19:05] whether this is still
[19:08] up to date or if we would recommend um
[19:12] something else. But in yeah, in theory,
[19:14] we've had this available as a a
[19:16] standalone service. Uh the question is
[19:18] just whether is this is this the latest
[19:21] version of it or do we have
[19:23] a
[19:25] um something even more up to date
[19:28] because you know stuff changes a lot. I
[19:30] see Lee's typing so maybe Oh, Lee's
[19:32] getting the ASP. Um
[19:38] uh
[19:41] Oh yeah. Yeah. I you so le is recommend
[19:45] well I don't know that I'd recommend the
[19:47] SharePoint in 365 indexer um because
[19:51] for the impression I get is that it's
[19:54] perhaps not going to stick around
[19:56] forever um
[19:59] I'm just trying to say things gently and
[20:01] also the retrieval quality is generally
[20:04] lower because it's not using the um if
[20:07] it depends which one you're talking
[20:09] about if we're talking about right the
[20:10] question is are you
[20:12] um you know search and indexing from
[20:14] Azure AI search or using it from copilot
[20:16] right and so this one's using basically
[20:18] it's basically like a remote data source
[20:21] um in that case you're using the
[20:23] retrieval and the ingestion of co-pilot
[20:26] um versus the other one where um you
[20:29] know we were
[20:32] um doing ingestion and indexing and
[20:34] retrieval with Azure search itself. So
[20:36] there you have a lot of control and you
[20:38] get best-in-class retrieval.
[20:42] Um,
[20:45] okay.
[20:48] Um,
[20:52] okay. So if you add work IQ as a source
[20:55] is the cost charged on top of what it
[20:58] costs to process search inside work IQ.
[21:01] Um
[21:03] so Foundry IQ would cost um there'd be
[21:08] some cost for the agentic reasoning
[21:10] tokens.
[21:12] Um so you know if we look at like the
[21:16] right so for a remote knowledge source
[21:18] we look at like what is the work that
[21:20] you know that the
[21:23] uh let me find like shareepoint example.
[21:25] Okay.
[21:27] So, if you're doing like uh no, let's do
[21:31] medium. Okay. All right. So, you know,
[21:33] if you were doing query planning, then
[21:36] you know, there'd be the token cost um
[21:38] for the LLM. And so, that would actually
[21:40] be that'd be in your LLM budget. Then,
[21:44] um you know, the the actual call to work
[21:47] IQ. Uh I I don't think there's any cost
[21:50] for that itself. But then there is also
[21:53] there is the agentic reasoning. That's
[21:55] basically the reranking stage. So there
[21:57] is a cost for agentic reasoning. Um so
[22:00] there like there's I think the main cost
[22:04] there here is going to come from the
[22:05] agentic reasoning because that is a
[22:07] model that lives in the search service,
[22:09] right? So that I think is going to be
[22:11] the only cost that's going to come out
[22:13] of your search budget would be the
[22:17] basically the ranking, right? So if we
[22:19] look at this, you know, if you're doing
[22:21] a remote source, well, the search is
[22:23] handled by the remote source. Like this
[22:24] one's fabric IQ, right? You know, it
[22:27] does the, you know, remote source. Um,
[22:31] the LLM is doing the query planning. So
[22:33] that's the LM budget that's separate.
[22:35] Uh, but then the merge, the result
[22:37] merging that is coming from an Azure AI
[22:40] search model. So that is where your cost
[22:44] is going to be. Um, let me just, you
[22:46] know, confirm that pricing with their
[22:50] pricing guide. Uh, oh, and there is also
[22:53] a Foundry IQ serverless now, which is
[22:55] fun. So, they just announced the
[22:57] serverless at build. So, that makes
[22:59] Foundry IQ
[23:01] um more that's going to be uh you know,
[23:04] currently it's in preview mode, right?
[23:06] So, we can't really use it practically.
[23:08] Uh
[23:11] um but once serverless is properly out
[23:17] um serverless. Okay, that talks about
[23:19] it. Then that's going to really reduce
[23:21] search service prices. So that's cool.
[23:24] Um okay, anyway, we're looking at
[23:25] pricing, right? So we So there's a
[23:27] search service pricing for your index,
[23:29] right? Like whatever's in your index. Um
[23:32] and there's serverless that's going to
[23:34] be cheaper. Then features, right?
[23:36] Agentic retrieval
[23:38] um separate charges are incurred for
[23:40] remote knowledge sources like you know
[23:43] shareepoint and web now also fabric IQ
[23:48] um I'll tell them they should probably
[23:50] add fabric there um and MCP servers
[23:54] would be there right uh so anyway
[23:56] retrieval those are the you know those
[23:59] are the reranking
[24:01] tokens um and semantic ranker that but
[24:04] that's only per indexes So yeah, really
[24:06] you're looking at the reranking tokens
[24:08] that happens for the result merging. So
[24:11] you will spend some amount for result
[24:13] merging.
[24:19] Um okay so
[24:22] uh so uh MP Joner you said you've had an
[24:26] experience about knowledge graphs and
[24:28] can you repeat what the actual question
[24:29] is because I I didn't see what the full
[24:31] question was like um yeah I see you're
[24:36] typing okay great uh let's see do I have
[24:39] any experience with data versse and
[24:42] using fetch xml o data query to connect
[24:44] to models okay first we're going to look
[24:46] up what data versse is I think the
[24:48] answer is going to No. Oh, that's a
[24:50] Microsoft thing. All right. Didn't
[24:51] realize that was going to be Markoff
[24:52] thing. All right.
[24:54] Dang, I keep learning. There's more
[24:56] things. All right. My granddise. Oh
[24:59] gosh. Nope. Never heard of it. Okay. All
[25:03] right. Um, so no, I don't have
[25:06] experience with data verse, but I
[25:08] learned another Microsoft tool. That's
[25:10] cool. Um, O data query. Um
[25:14] uh I know Azure AI search uses O data
[25:16] queries uh quite a bit as their their um
[25:19] language for like filtering but I assume
[25:21] you're asking specific to data versse.
[25:23] So nope I have not used that. Anybody
[25:25] has
[25:27] um oh and it's got an MCP. Well if it's
[25:29] got an MCP
[25:31] uh then you know we can do things. Um
[25:35] okay it's cool to see. I I keep learning
[25:38] about new MCPS. All right. So this
[25:41] exposes the MCP. How do we do the
[25:43] authentication? Okay. Copi studio not
[25:47] learn how to connect. This is always the
[25:49] question whether you can do connect.
[25:51] Okay. Yeah, you have to bring your own
[25:53] probably client ID. Okay. List of tools.
[25:57] Search data.
[25:59] Uh uh
[26:03] interesting.
[26:05] Still don't quite know what data versse
[26:07] does.
[26:09] data versse.
[26:11] What is data versse?
[26:13] Okay, this kind of sounds like fabric.
[26:17] No, because fabric I guess I'm you know
[26:20] we're going to be showing PowerBI in the
[26:22] fabric session. Um I guess there's just
[26:25] you know Microsoft has so many customers
[26:26] that there's different ways of going
[26:28] about the same thing. This this is this
[26:29] whole Power Platform which at this point
[26:31] the only part of the Power Platform I've
[26:33] used is PowerBI. So I am going to show
[26:35] PowerBI on Thursday um with BI reports
[26:38] and semantic models because we can use
[26:40] those from fabric IQ um but I have not
[26:43] used the rest of the power platform.
[26:48] Oh okay so I see the question when we
[26:50] talk about knowledge as a function of
[26:52] Foundry IQ what role do knowledge graphs
[26:54] play in retrieving knowledge or
[26:55] reasoning? Yeah so that's a great
[26:58] question. Okay. Um so yeah, currently
[27:00] Foundry IQ does not have any particular
[27:04] knowledge graph um integration. Um there
[27:08] they've been looking they've been
[27:09] working with and looking at graph rag
[27:11] for
[27:12] um a long time. Um and you know there
[27:16] you'd be able to you know you know um
[27:20] answer you know answer more questions
[27:22] that um you know are better answered by
[27:25] a knowledge graph, right? like this one
[27:27] like what are the top five themes in the
[27:28] data that you're not going to be able to
[27:30] answer that question with a foundry IQ
[27:33] search because you know there's just you
[27:36] know the foundry IQ search is going to
[27:37] find chunks of data right like so you
[27:40] know assuming you just chunked up your
[27:41] data like how is it going to figure out
[27:42] the top five themes right um if you have
[27:44] something like graph rag graph rag you
[27:46] know does this kind of clustering right
[27:48] these semantic clusters and then is able
[27:51] to like search across the clusters um so
[27:53] they've been trying to figure out like
[27:54] you know is there a way they can
[27:55] production it. The hard thing with this
[27:57] is productionizing it, making it
[27:58] performant. Um, graph rag is very token
[28:02] hungry, very slow, expensive, right? So,
[28:05] you know, how can you make this be
[28:07] production ready and performant? And
[28:08] there's, you know, still trying to
[28:10] figure that out. Um, if you did want to
[28:13] try like if you wanted to try and like
[28:15] kind of make your own version of this,
[28:17] you could, you know, basically like in
[28:19] addition to having the chunks, the
[28:22] document chunks index, you could also
[28:25] have an index that was like summaries of
[28:27] your documents, right? And then you
[28:28] could have multiple like, you know, have
[28:30] it as a separate knowledge source of
[28:31] like, you know, search all the document
[28:32] summaries, right? Or you could have an
[28:34] index which was like um, you know,
[28:37] searching across themes, right? Because
[28:39] the basic idea here is that like uh I
[28:41] mean I think this one did it on demand
[28:42] which makes it particularly slow but you
[28:44] could you know basically kind of pre
[28:46] compute a graph and store it as separate
[28:49] indexes and then use a knowledge base
[28:51] with those separate indexes right so you
[28:52] have your indexes which is your like
[28:55] very zoomed in which is you know every
[28:58] everything in the index is a chunk from
[29:00] a document right and then you have your
[29:01] index which is like a summary of each
[29:03] document then you have your index which
[29:05] is a bunch of themes that it found you
[29:08] know across all the documents right so
[29:11] that I think would be an interesting way
[29:13] um or you could like even do like an
[29:15] entity analysis right like so in
[29:16] addition to themes you'd say like okay
[29:18] find all the people mentioned in this
[29:20] knowledge base and make a per people
[29:21] index and find all the objects find all
[29:24] the you know relationships right so um I
[29:27] think there's interesting ways that you
[29:28] could try and um you know create your
[29:31] own sort of um version of this that was
[29:37] um but that still stayed performant but
[29:39] could answer more of the highlevel
[29:42] zoomed out uh questions. Um I mean once
[29:46] again it does depend on like what are
[29:47] the questions you're getting and you
[29:49] know what's going to what kind of data
[29:51] layout is going to work for answering
[29:53] those questions. Um so yeah currently
[29:56] Foundry IQ does not particularly have um
[29:59] a knowledge graph approach. uh we will
[30:02] see that fabric IQ has something called
[30:05] graph um but that's more that's still
[30:08] more you know that doesn't work with
[30:10] like unstructured data that's just about
[30:12] like kind of connecting like that's like
[30:13] related relational data right um so you
[30:16] know I think this is still a work in
[30:18] progress but there are things you could
[30:20] experiment with on your own
[30:25] uh mcb 2.0 now. Yeah, we are going to
[30:28] have we have lots of stuff coming up.
[30:30] Yeah, sorry. We I know there were good
[30:31] questions about MCP2 about whether we've
[30:33] made any updates for MCP. So, definitely
[30:36] the GitHub MCP server has updates for
[30:38] the new version of MCP. But yeah, join
[30:40] us for we've got MSP live. Um that's
[30:44] coming up on September
[30:47] 8th. And then we're also doing inperson
[30:49] events in both San Francisco and
[30:50] Bengaloo. So, uh, and then also there's
[30:53] going to be a VS Code live stream,
[30:57] um, in mid August that's focused on MSP
[31:00] 2.0. Uh, because today is actually the
[31:03] release of MSP 2.0. I'm going to the
[31:04] release party later today. So, there's
[31:06] also release parties all over um all
[31:10] over the the world. So, you might find
[31:11] MSV release party um near you today.
[31:15] Let's see if there's a list of them.
[31:16] Right. So, this is the one I'm going to
[31:20] um
[31:21] and but there's a bunch just all over.
[31:24] So, you can check to see this is the MCV
[31:26] graduation party.
[31:28] Uh yeah, but yeah, if you're in the MCB
[31:31] space, it's an exciting day. Um and uh
[31:35] you know, go help MCP graduate.
[31:40] Yeah, lots of cool updates to it. All
[31:42] right, cool. So let me see what other
[31:46] Okay, so Keva says how do you add how do
[31:49] you filter documents index and AI search
[31:51] based on user role?
[31:53] Um so user role assuming do you mean
[31:55] like an entra user role that
[31:59] what you're asking?
[32:01] Um, let me don't
[32:08] let's see. Entra rolls
[32:13] like this sort of roll. Is that what
[32:15] we're talking about here?
[32:22] Okay. Oh, yeah. And I did get some um
[32:24] queries back. So for the security
[32:28] trimming um it is actually cached. Uh so
[32:31] where's the data access? So we were
[32:33] talking about the data access controls
[32:34] right when we check like group ids. So
[32:36] it is actually cached.
[32:39] Um
[32:41] let me see what the cache mean. Uh so
[32:45] that that is something to keep in mind
[32:47] right if somebody gets removed from a
[32:49] group um there is some caching that
[32:51] happens there. Uh let me see if I can
[32:53] find out the cache duration. Uh for
[32:56] region residency
[32:58] uh I asked like is everything always in
[33:00] the all in the region and um the they
[33:04] say it just it depends on the feature.
[33:06] Um so yeah I think you know if you're
[33:10] using particular features of AI search
[33:12] uh you'll just want to check on the docs
[33:14] and and see for that feature um what its
[33:18] region residency is. Um
[33:22] the you know when you're connecting
[33:23] models the models are in whatever region
[33:24] you put them in but there's lots of
[33:26] other things too. Uh custom user roles.
[33:29] Okay. So you're saying you're doing on
[33:31] but is that but is it within like like
[33:34] this? Is this what we're talking about
[33:37] custom role? Um like it's it's still
[33:41] within like it's like a formal role
[33:44] within the Entra um you know
[33:48] terminology. Is that what we're
[33:50] describing here? Let me link to this.
[33:55] Just want to make sure because because I
[33:57] could also see you talking just
[33:58] conceptually about like oh like you know
[34:00] the idea of a of somebody being an admin
[34:03] or something, right? Like versus natural
[34:05] entra role.
[34:14] Let's see what other questions.
[34:22] Um,
[34:26] oh, let me also ask about ASPX. Does the
[34:29] SharePoint indexer
[34:32] handle ASX?
[34:35] All right. Let me ask that. Okay. All
[34:38] right. Let's see.
[34:42] So, waiting there. All right. Someone
[34:46] typing
[34:52] Oh, now I have the I can also try like
[34:56] what I didn't show was
[35:00] um toolbox foundry IQ.
[35:06] I can show the publishing flow. All
[35:08] right, so publish, right? Oh, this one's
[35:10] even published. All right, we'll do
[35:12] publish, right? So, we're going to
[35:14] publish. say this is my agent that uses
[35:17] Foundry IQ in toolbox.
[35:21] I'll just repeat that. Okay. All right.
[35:24] And you can see it's going to make an
[35:25] Azure bot service. Publish options. I'll
[35:28] just say just me. I'm just testing it.
[35:31] And then I'm going to say publish.
[35:37] All right. And so now it's available. So
[35:39] in Teams I should be able to find it. So
[35:42] then I'm going to go
[35:45] and go over to my teams. Okay, I'm going
[35:48] to switch tenants. All right. So here in
[35:51] my teams now I can go to
[35:55] let me find this apps. Apps your agents
[35:59] and apps. No, you go down here, manage
[36:02] your apps.
[36:04] And then we're going to look for
[36:08] what did we call it? This one. Agent
[36:11] Toolbox Foundry IQ. I think it's that
[36:13] one.
[36:15] Let's make sure see what we called it.
[36:18] Agent channels.
[36:21] Okay. All right. It's probably this one.
[36:25] And
[36:26] your details.
[36:29] Open.
[36:31] Open.
[36:33] Say hi. See if this one's working.
[36:39] Okay. So, we get a sign-in link. So, I'm
[36:41] going to click on this
[36:47] and
[36:49] okay, it's signed in. Okay, foundry
[36:52] login complete and I'll just ask
[36:56] question
[37:01] and let's see. Oh, and it replied. Okay,
[37:05] we talked at the same time. I don't know
[37:07] if it's still going to see my question
[37:09] or not. Oh, here we go.
[37:12] Yep. Okay. So, that's just showing you
[37:15] the publishing flow. So, as you see, um
[37:18] you can publish your Foundry hosted
[37:21] agents and bring them into Teams. Uh in
[37:24] this case though, you know, um I did
[37:27] have to publish it to the same tenant
[37:30] that my teams is in. Right? So, if you
[37:32] have multiple tenants, it can get
[37:33] confusing, right? So, I'm in, you know,
[37:35] I'm in a particular tenant, right? this
[37:37] tenant here, Foundry Drive 2607.
[37:40] And if we look at my teams, like it's
[37:43] basically a test tenant for me. So you
[37:44] can see I switched into this tenant. Um,
[37:47] so it's only going to work inside the
[37:50] tenant where I published it, right?
[37:52] Because when we do the login, it's
[37:54] logging in uh it's logging in
[37:56] specifically to that tenant. That's
[37:57] that's the main tricky thing that I
[37:59] found um with this is that at Microsoft
[38:03] we have lots of different tenants and
[38:05] the our production like we don't deploy
[38:07] things into the production tenant unless
[38:08] it's really for production. Um so for
[38:10] protoing I made sure that you know I'm
[38:13] deploying the hosted agent to my test
[38:16] tenant and then I'm you know using teams
[38:19] from that test tenant as well.
[38:23] Okay. All right. So let me
[38:26] uh Okay, I see some questions now. Uh
[38:33] okay. Is there a decision tree? I see.
[38:36] All right.
[38:40] Okay.
[38:44] Is there a decision tree when to stay
[38:46] inside N365 and copy student and when to
[38:48] go for foundry? Uh let's see.
[38:53] For me, I've I never started inside M365
[38:57] and Copilot Studio, so um I can't really
[39:01] compare them. It I think tomorrow Acha
[39:04] might have a better feel for that
[39:06] because she's been in both places,
[39:08] right? Because she's from the M365 team,
[39:10] so I think she probably actually started
[39:12] off in Copiot Studio and then has moved
[39:15] to Foundry like because she um she ended
[39:18] up adding like turning hers into a
[39:20] Foundry hosted agent as well for
[39:21] tomorrow.
[39:23] Um, so I I think that she would be able
[39:25] to compare. So I've never I've just
[39:27] never been in Copi Studio because I
[39:28] tried it once like three years ago and I
[39:30] was like, "Oh, this is not like a happy
[39:31] place for me because I can't like write
[39:33] code for it." Um, so I'm always going to
[39:36] go where I can write the most amount of
[39:37] code and like have the most amount of
[39:39] control. Uh, so that's why, you know,
[39:42] for me it's uh, Foundry particularly
[39:45] with Foundry hosted agents. Um, and you
[39:47] can even go even like I mean there's
[39:49] different there's a whole spectrum,
[39:50] right? Right. So there's like copilot
[39:52] studio. It's probably like um I think
[39:56] there's even like SDKs for copilot
[39:58] studio. So I shouldn't necessarily say
[39:58] that's it's no code, but as far as I
[40:01] would say you get less control there, I
[40:03] would assume. And then we've got Foundry
[40:05] hosted agents. You got more control. Uh
[40:07] Foundry prompt agents, less control
[40:09] again. Um if you wanted uh even more
[40:12] control, you could just straight deploy
[40:14] on like container apps or container apps
[40:16] sandboxes now. So, I'm actually I do
[40:18] have a live stream coming up uh
[40:21] September about um ACA sandboxes and
[40:25] deploying
[40:27] agents on it. Um because you you know
[40:30] you don't even have to you know you know
[40:32] if you want like a full amount of
[40:34] control and then of course some people
[40:35] are going to go like Kubernetes right
[40:37] this is that's going real intense but um
[40:39] but yeah you can see here like you you
[40:41] could just deploy directly on a sandbox
[40:43] itself and and get the benefits of
[40:45] there. So you know with Microsoft like
[40:47] Microsoft gives you a lot of options um
[40:52] and uh you know a lot of times it's
[40:54] about control
[40:57] um integrations right so cop studio
[41:00] might might have a lot of you know well
[41:02] I'm sure has a lot of integrations the
[41:04] question is whether it has integrations
[41:07] that we don't now have in foundry
[41:09] because foundry does now have a lot of
[41:10] good integrations right you can see I've
[41:12] got connection to fabric IQ work IQ
[41:15] foundry IQ, right? Um, and we can like,
[41:17] you know, and we've got our tool boxes
[41:19] and we can add more tools. And if we
[41:20] look here, you know, we can see uh, you
[41:23] know, more more tools here. There's a
[41:26] whole catalog of other ones. Oh, look,
[41:28] there's data versse or like
[41:31] we're learning more about data versse
[41:32] all the time, right? So, you can connect
[41:34] data versse to the toolbox. So, um,
[41:38] yeah. So as you see like there's
[41:39] increasing
[41:41] uh support for integrations in Foundry
[41:45] itself. Um and then of course you can do
[41:48] custom tools here like opening API MCP
[41:51] or A2A.
[41:53] Uh so yeah so I would you know I tend to
[41:55] go where um I get a lot of control but
[41:59] also the features I need. Um so for me
[42:01] foundry hosted agents is nice because um
[42:05] you know I I get the deployment because
[42:07] you know I want easy deployment right so
[42:08] this we get the easy deployment I also
[42:11] get like the nice you know observability
[42:14] um I get good you know monitoring right
[42:17] all this is built in I could set up
[42:19] evaluations I haven't done it for this
[42:21] one yet but I could set up all these
[42:23] evaluations we can even use the
[42:25] optimizer so it's like a good balance
[42:29] between control and integration, you
[42:32] know, features.
[42:34] Um, but I think you need to have a list
[42:36] of like what features you need and how,
[42:40] you know, what flexibility and control
[42:42] you need, how you like to develop and
[42:43] see what's going to fit. Um, I I can't
[42:46] really compare Copilot Studio because I
[42:48] haven't used it in a long time.
[42:51] Uh, oh
[42:54] yeah. Um, let's see.
[42:58] So wait, let's let me look back in the
[43:01] questions. Um,
[43:05] if we need information located in the
[43:07] context of work IQ, are there
[43:08] differences in the retrieval methods
[43:10] compared with retrieving through Foundry
[43:12] IQ?
[43:14] Um,
[43:17] yeah, I mean, work IQ is a remote data
[43:19] source. So if you're comparing like
[43:21] index SharePoint versus remote work IQ,
[43:23] it's definitely going to be different.
[43:26] Um, so, uh, that's why that's like, you
[43:29] know, like you really want to compare
[43:31] those two and see if work IQ is good
[43:33] enough, great. Like if you can, if you
[43:35] can use a remote data source, like you
[43:37] should generally always use a remote
[43:38] data source because then you don't have
[43:39] to worry about keeping data, you know,
[43:41] up to date and fresh and all that stuff
[43:43] and data access control, right? Um, but
[43:47] you know, maybe you can't, maybe it it's
[43:49] not good enough for you. maybe it
[43:51] doesn't have everything you need and
[43:53] that's when you start you know doing
[43:55] indexing that data itself.
[44:00] Um
[44:03] I see we got some flowcharts here. Okay.
[44:07] Um,
[44:09] all right. So, can the built so Keva
[44:11] asked, "Can the built-in tool that the
[44:13] agents and founder uses connect to an
[44:15] index in search return custom fields
[44:17] from that same index?" Um, so if you're
[44:22] talking about the the knowledge base,
[44:25] then a knowledge base should be able to
[44:28] um you know return back all you know all
[44:31] of the fields. Uh let's look at how we
[44:33] configure configured our knowledge base.
[44:36] Uh let's see. So I actually configured
[44:40] where did I set it up?
[44:44] I set it up here. Okay. So create
[44:46] knowledge base. Um
[44:54] knowledge base. Knowledge sources.
[44:58] All right. So that would be actually in
[44:59] the knowledge source.
[45:01] So you would want to say what your
[45:03] source. Yeah. So here. Okay. Um, so when
[45:06] you create your knowledge base, you're
[45:07] going to connect your knowledge sources.
[45:09] So in the knowledge sources, I specified
[45:12] ex exactly what the source data fields
[45:14] were, right? Because I think mine, you
[45:18] know, I had some custom ones here. So I
[45:20] had like blob path, snippet, parent ID,
[45:22] right? Um, so you specify those in the
[45:24] source data fields and then you also
[45:26] tell it like which things it should
[45:28] actually search. So source data those
[45:30] should get returned
[45:32] and then search um you know is what is
[45:36] actually right. So yeah use request
[45:38] additional field for reference source
[45:39] data. So we should be able to get back
[45:41] everything we request in the source data
[45:42] fields right. So even with the MCP
[45:45] server let's see do I have it running
[45:47] right now? Yeah I actually had that one
[45:48] running. Um so let's just test it out
[45:51] because we should see that the
[45:53] references includes all of those fields
[45:56] that we see here.
[46:03] Uh, and this should pop. Yeah, it's
[46:05] going to pop it open. All right. Um,
[46:08] plus scuba diving. Okay.
[46:12] And then Oh, and we still had the
[46:13] question about c custom roles. So, let
[46:16] me see. Security. Okay. All right. Um.
[46:21] All right. Okay. And I got some other
[46:23] updates. So, the SharePoint indexer does
[46:25] not the like the the the SharePoint
[46:27] indexer, the one that's built into AI
[46:29] search, um does not the you know the
[46:32] built-in one does not support ASPX yet.
[46:34] So, with ASPX, you're kind of in a hard
[46:37] place. Um I would see if Work IQ is
[46:40] finding your ASPX pages. Um I don't
[46:43] know. also with work IQ. Um,
[46:49] uh,
[46:56] let me see if work I do.
[47:02] Okay. Uh, does okay. And then the
[47:05] question was, what's the security
[47:06] trimming support custom entra roles?
[47:11] All right. I'll just pass that. Okay.
[47:14] Um, let's see. Oh, yeah. We were going
[47:16] to check to see the custom fields. Okay.
[47:19] Um,
[47:21] all right. So, we're looking at the
[47:25] references that come back
[47:29] ref ID content.
[47:32] Content content.
[47:36] Interesting. So, I see the content.
[47:40] I think the MCP server. Oh, this is the
[47:43] issue. The MCP server does not
[47:48] have full references. Sorry, I had this
[47:51] as a con on this side. So, let's go back
[47:53] to this slide. You cannot access
[47:55] references. So, even Yeah. So, that's if
[47:58] you want access to those, you are going
[48:00] to want to use the um So, you know, I
[48:03] think that should change in the future
[48:04] because that's a definite drawback here,
[48:06] right? So when you're using currently
[48:07] when you're using MP server um you know
[48:10] there's no customization of the
[48:12] retrieval parameters and you cannot
[48:13] access the references. So even if you
[48:15] specified that right so if we went to
[48:18] our custom tool our custom tool we would
[48:20] see that in the references. So going
[48:22] back to this one that's going to show us
[48:24] all this but the MCP server just never
[48:27] shows the separate references like it'll
[48:29] show the inline references. So we see
[48:31] like oh ref ID one right? Um, so it will
[48:34] show like it's it's really minimal right
[48:38] now, right? So it's not going to it
[48:39] doesn't send back that. So let's try it
[48:42] with this print.
[48:45] That's a definite drawback of the MCP.
[48:47] So that would be like the built-in tool
[48:48] would be using um should be using the
[48:51] MCP server. So that has that that
[48:54] drawback there. Um so yeah, same so same
[48:57] thing with Foundry Toolbox with
[48:58] knowledgeb same drawbacks as MCP server.
[49:04] Okay. Uh so if we look at this one which
[49:08] gets back where we included everything
[49:10] there you can see source data fields you
[49:13] know there we've got the snippet blob
[49:16] path blah blah blah blah blah right like
[49:19] um
[49:21] it should
[49:24] does it actually show the fields get
[49:26] source data fields?
[49:28] Oh that's the activity log. Sorry, let
[49:30] me look at the actual reference. So
[49:33] that's the activity log response.
[49:38] Okay, what do we pass back? We passed
[49:39] back
[49:42] uh let's look at the code for this one.
[49:46] Okay, we passed back
[49:49] response references activity. Okay, it's
[49:52] a little hard to look at the JSON in
[49:54] line here. Okay. References type source
[49:58] data doc key.
[50:03] H
[50:05] source data null.
[50:08] I actually don't see it there. All
[50:09] right. I'm going to ping this too cuz
[50:12] um I feel like we shouldn't see this. We
[50:15] should see them there.
[50:17] Uh when we create a KB
[50:22] resource data,
[50:27] we be able to see them
[50:31] references
[50:33] this.
[50:43] All right. Okay. Let me um dig into that
[50:47] cuz I we should at least be able to see
[50:49] that there. But I'm seeing a um I'm
[50:52] seeing a null. So I'm not sure. Maybe
[50:56] we're just I'm not serializing it. Well,
[50:58] references.
[51:00] Okay, I'm going to dig into that. Um and
[51:05] yeah, I'm looking into the roles. So, um
[51:08] I don't think there's built-in spark for
[51:10] rolls. I'll find out. I'm finding out if
[51:12] there is. um you know if there's not
[51:14] what you can do is you can basically
[51:15] implement it yourself using a filter. Um
[51:19] let me find my
[51:21] because when so here's the thing like um
[51:23] the security trimming like wasn't built
[51:25] into uh Azure search originally but we
[51:28] implemented it ourselves in our open
[51:30] source
[51:31] uh you know rag solution. So you know
[51:34] many of you if you've seen me talk
[51:36] before you've seen me talk about this
[51:37] repo. This is our our you know open
[51:40] source rags repo and a lot of the um we
[51:43] get a lot of the ideas from developers
[51:45] here about what people want. So um you
[51:48] know we there's many things you can
[51:49] implement yourself and then when it we
[51:51] realize like everybody wants it then you
[51:53] know then Azure AI search team can like
[51:54] build it into the service. Um but let me
[51:57] see before we did
[52:00] um yes
[52:03] before it was built into the service
[52:06] we just implemented ourself and so this
[52:08] is basically the idea right so you know
[52:11] um we said like okay we're having
[52:15] um oids and groups you could imagine
[52:18] adding a roles here to the search index
[52:21] and then we would just send in a uh you
[52:23] know construct a filter um and say like
[52:26] okay like is the is the is user's oid in
[52:31] you know in in this group like to check
[52:34] to see is their oid in in there or is
[52:37] the groups in there so you could do the
[52:39] same thing with roles so you know you
[52:41] can always build your own filters um the
[52:45] AI search team decided just to to make
[52:48] it really straightforward to do entra
[52:51] oids in groups because so many people
[52:52] are doing them um but But if you wanted
[52:55] to add support for roles, then you know
[52:57] and if that's not a a built-in thing um
[53:00] then you can you know you can construct
[53:03] that filter yourself right and say like
[53:05] you know you would just add on an
[53:06] additional filter for roles and say
[53:08] which roles can see it and then you
[53:10] would construct the filter yourself on
[53:13] top of you know any other filters. Um,
[53:16] and then, uh, yeah, and then you just
[53:18] have to make sure you're keeping stuff
[53:20] up to date, right? And so you would have
[53:21] your roles on each of the documents,
[53:25] um, and you know, update that
[53:28] appropriately.
[53:39] All right, let's see what else.
[53:47] Okay, so Justin,
[53:50] how are teams thinking about the right
[53:52] boundary between foundry IQ for grounded
[53:54] knowledge
[53:56] and their own application for tenant
[53:57] isolated permissioning action through
[53:58] rules when deploying custom Azure
[54:01] environments?
[54:03] Good questions. Anyone want to share how
[54:05] they're thinking about it? Maybe Pablo.
[54:07] Um,
[54:15] yeah. I mean, you want to if you're if
[54:18] you're building like a whole agent that
[54:21] can take action, then you do also want
[54:23] to think about um where's my slide about
[54:26] that?
[54:28] Didn't put it in this one. Um,
[54:33] okay. here.
[54:37] Eventually there's a slide for
[54:38] everything.
[54:48] Uhuh. There. Okay.
[54:53] Right. So, if you're building something
[54:54] that has both founder IQ and can take
[54:57] actions, right? Then you yeah we and
[54:58] we've talked about this before so I
[55:00] think Justin's already seen this but um
[55:03] you know for other folks like you want
[55:05] to think about the the lethal trifecta
[55:08] which is having you know access to
[55:09] private data the ability to externally
[55:11] communicate and also exposure to
[55:13] untrusted content like web search
[55:15] results. This is where things get really
[55:16] bad. But of course even just access to
[55:19] data and the ability to take any action
[55:20] right. So even if it's just access to
[55:22] data and the ability to send an email
[55:24] then you know then that's really um you
[55:27] know then that's really risky. Um so you
[55:30] know that's where we usually recommend
[55:32] adding in a human approval step. The
[55:35] thing is like all of this is more that
[55:38] you have to build right because what
[55:39] where do you do the human approval? I've
[55:41] seen people that, you know, are have
[55:43] built on top of Foundry IQ um like for
[55:46] customer service help, right? And um you
[55:49] know, they have like a whole inbox of
[55:52] things that um that they need to process
[55:55] like and they'll like denote and say
[55:57] like, "Oh, we've detected that this one
[55:58] really really really needs human
[56:00] review." I kind of like rank it by um by
[56:03] priority there. So,
[56:06] um it just means that though you do need
[56:08] to like build build an additional
[56:10] interface, right? Cuz in order to add
[56:13] that human to loop um or you're adding
[56:15] just a lot more LMS that are evaluating
[56:19] along the way and saying like do we do
[56:21] we have the confidence to take this next
[56:23] move or or not, right? Um so yeah, I'm
[56:29] very curious about that too. What people
[56:30] are doing for action approvals, right?
[56:32] like what sort of interfaces are people
[56:34] using like or you know is it you know
[56:37] are you just sending someone a a chat or
[56:41] something and asking for approval there.
[56:43] Um, so yeah, I I would like to see all
[56:49] the different ways that people are doing
[56:51] approvals and human in the loop because
[56:53] that that is where things get really,
[56:55] you know, really interesting, right? Um,
[56:58] like I, you know, whenever I have an
[57:00] agent that can take action, I always
[57:02] give it the ability to not take action
[57:04] too, right? So say like, you know, give
[57:06] it the way to opt out and say like, you
[57:08] know, oh, I don't have the confidence to
[57:10] take this action right now, so I'm going
[57:11] to I'm going to um, you know, opt out of
[57:14] that. Uh,
[57:17] okay. All right. Well, we are at time
[57:20] now. Um, you know, I know there's still
[57:22] some questions that, um, you know, I
[57:26] need to dig into more. So um, as usual,
[57:29] what I'll do is let's see, we're still
[57:31] recording this, right? Yeah. So, you
[57:33] know what'll happen is that I'll have
[57:35] the recording. I'll put that on YouTube.
[57:39] I'll make a transcript of it. I'll post
[57:41] all the questions here. And if I have
[57:43] any updates to the questions, then I'll
[57:45] update the answers here too, right? So
[57:48] that you know, anything that comes in
[57:49] from the product teams afterwards that
[57:51] we learn um then um you know, I'll I'll
[57:55] have it updated here. So hopefully this
[57:57] becomes this this discussion strate
[57:59] should become a comprehensive QA.
[58:03] All right,
[58:06] thank you everyone. Uh hopefully we'll
[58:08] see you tomorrow for it session on work
[58:11] IQ
[58:13] and she's from the 365 team. So also
[58:16] just generally good um a good way to ask
[58:20] 365 questions um for her office hours.
[58:23] Actually Paulo will be doing them
[58:25] because Acha is in Dubai where their
[58:28] discord is voice is forbidden so she
[58:31] can't be on voice. So anyway we'll have
[58:33] Acha for the YouTube stream and then
[58:35] Paulo um will be doing the office hours
[58:38] after with Acha in the chat.
[58:42] All right. Thank you everyone. Have a
[58:45] good rest of your day. Bye.
