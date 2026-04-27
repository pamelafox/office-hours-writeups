[00:00] So, welcome everyone to our weekly
[00:04] Python plus AI office hours. It is April
[00:08] 20th
[00:09] and
[00:11] uh yeah, I always start off with
[00:14] whatever the biggest news of the week is
[00:17] and uh anything I've been working on,
[00:20] upcoming events. Um but we usually talk
[00:23] about whatever people want to talk
[00:25] about.
[00:27] Uh so if you have anything
[00:30] uh any news you want to share, any
[00:32] questions uh that you have uh if there
[00:35] was any questions from last week still
[00:38] pending uh just go ahead and stick them
[00:40] in the chat.
[00:42] So yeah, the big news I think we have to
[00:45] start off with these news this news. Um
[00:48] so GitHub copilot has
[00:52] too much demand I think and um you know
[00:56] good thing bad thing um so you know it's
[00:59] good that lots of people are getting
[01:01] good use out of agentic coding and being
[01:04] productive with it um but because of
[01:06] that in order to come be more
[01:07] sustainable and support everyone fully
[01:11] uh new signups are actually paused for
[01:13] co-pilot pro plus and student. Uh you
[01:17] can do copilot free and that has you
[01:20] know uh rate limits. Uh and so you'll
[01:24] you'll only be able to use that for a
[01:25] certain amount of requests each each
[01:28] day. Um but yeah, you won't be able to
[01:30] sign up for pro or pro plus. Uh you can
[01:33] still do business or enterprise. So if
[01:35] you're using co-pilot within a company,
[01:37] then hopefully you can keep using
[01:40] co-pilot full speed ahead. Um but as an
[01:42] individual, you're more limited.
[01:46] Uh and then there's also some tighter
[01:51] tighter limit. Uh so Pro Plus has more
[01:54] limits. Uh so you're going to get
[01:55] warnings on the limits. What's really
[01:57] sad from from my perspective is that
[01:59] Opus models are removed from Pro.
[02:02] And uh so if you are on Pro, you do not
[02:04] get the Opus models at all. If you're on
[02:07] Pro Plus, you get Opus 4.7, but a lot of
[02:10] us prefer Opus 4.6 to 4.7. There's been
[02:13] a lot of discussion about 4.6. 7 versus
[02:15] 4.6. I know one person loved it, but I
[02:18] think many of us are not convinced that
[02:22] it's actually that much um better than
[02:24] 4.6 and that you know maybe some of the
[02:26] training on it was a little funky.
[02:30] Um so yeah, so there's yeah, so
[02:34] definitely um significant changes there.
[02:38] like hopefully this will change over
[02:41] time as we ramp up capacity to be able
[02:43] to support everyone. Um but uh yeah
[02:48] that's that is definitely big news
[02:52] there.
[02:54] So uh if that affects you go ahead and
[02:58] read the blog post about it.
[03:02] Um, but remember you can still do let's
[03:04] actually look at the pricing for GitHub
[03:06] business and enterprise. I assume those
[03:09] are both org level plans.
[03:12] Uh, GitHub copilot all so enterprise
[03:18] but is that only I actually don't really
[03:21] know compare plans um pro. Okay, so
[03:25] these are the ones that are
[03:28] paused now. Pro and pro plus.
[03:38] So you'd have to be part of a GitHub
[03:40] enterprise or business account.
[03:45] Yeah. So, I guess we knew the time would
[03:47] be coming when we'd have to start
[03:49] limiting, but I mean, everyone's talking
[03:51] about generally in the industry that,
[03:52] oh, we're, you know, not going to be
[03:54] able to have so many tokens forever. And
[03:56] so, now we're starting to see what it
[03:57] means to be more sustainable.
[04:00] Okay, so that's that news. I see a
[04:02] question from Honor. So, do I have a
[04:04] workflow for using agents for pulling
[04:07] data out of PDFs? Is market a good
[04:10] library for this? Um
[04:14] so uh yeah markdown is one of the
[04:17] potential libraries. I I do usually use
[04:20] document intelligence
[04:23] um or content understanding. I guess
[04:26] document intelligence is actually maybe
[04:28] being phased out. Uh let me see if I
[04:31] have the markdown demo. Did I do a demo
[04:35] with it yet?
[04:38] Do I have mark it down in here? Mark it
[04:40] down. I do have mark it down. Okay. All
[04:43] right. So, this one uses mark it down
[04:48] and just uh says okay convert it. But
[04:52] this one is actually this one is just
[04:54] converting it to markdown right. So mark
[04:55] it down has like a lot of functionality
[04:57] in it. So in this case I was just using
[04:58] it to convert a docx to markdown and
[05:01] then I was sending it to a model to
[05:04] actually do extraction. Um, sounds like
[05:08] you're talking about maybe using
[05:09] markdown
[05:11] for even more than that. So, let me go.
[05:13] I think I've got this
[05:17] sample running locally. Let's try it
[05:20] out.
[05:21] Uh,
[05:24] entity extraction.
[05:26] Okay.
[05:31] All right. Let's see if I can run this
[05:34] one. Here
[05:40] we have mark it down.
[05:43] We're converting and then we're sending
[05:46] to an LLM. So let's just try this one.
[05:48] Python extract word.x.
[06:02] So that's running.
[06:05] running right now. Um, so let's look at
[06:07] look at the documentation for market
[06:09] down.
[06:11] Uh,
[06:13] so you can right so this is just
[06:15] conversion conversion. Well, maybe
[06:17] that's all it does. Maybe it is all just
[06:19] about
[06:22] um Oh, but this one the markdown OCR
[06:24] plugin. So that's that's fun. So if you
[06:27] have
[06:28] that seems useful. So if you have images
[06:31] inside of the documents then you can
[06:35] also install this markdown OCR plugin
[06:40] and you would need to supply the LLM
[06:43] that it can use for doing that. Uh so LM
[06:46] client so we just have to give it a
[06:49] pointer to the opening eye client.
[06:52] Um
[06:53] so then if it finds any images in there
[06:56] then it will mark it down. I don't know
[06:57] if that's something you need. Oh, and it
[06:59] does also do document intelligence.
[07:00] Okay. So, um so that would be a good
[07:04] test. So, it does. Okay. So, here we
[07:05] have So, this is plain conversion. This
[07:07] is with document intelligence and then
[07:09] this is
[07:12] um con describing images with LLMs.
[07:17] Uh so, be kind of interesting to compare
[07:20] the document intelligence. So, you want
[07:22] to get the PDF to a point where you can
[07:23] pull out entities. Uh yeah, I mean I
[07:25] think generally converting to markdown
[07:27] is is easier. So this one um the example
[07:30] document that I gave, let me show this
[07:34] document.
[07:36] Uh what is this going to open in pages
[07:41] text edit? Okay. All right. So it was
[07:43] like a document like this, right? Like a
[07:45] word document. Um the kind of a mix of
[07:49] different text
[07:52] and then it we you know converted to
[07:55] markdown. Let's go ahead and look at
[07:56] what the markdown text
[07:59] looked like there because then I went
[08:02] and told it to, you know, to take that
[08:05] and extract out the the title, the
[08:08] author, and the headings, right? So,
[08:11] it's similar, I think, to what you're
[08:12] doing, right? Is that um
[08:16] you're converting it to a format first.
[08:19] Now, the thing that really, right, oh,
[08:21] so here you can see, so this is
[08:22] basically what it did. Um, so we, you
[08:25] know, it just went and turned everything
[08:27] into markdown and then we passed the lm
[08:29] and then it extracted it.
[08:33] So that worked
[08:36] pretty well. Um, but if you there are
[08:38] images then you probably want to try the
[08:41] OCR option uh so that it can see a
[08:45] description of those images. Uh, and you
[08:48] could potentially like if you have a
[08:50] really really complex document like let
[08:53] me see if I find
[08:55] um trying to remember. I have some like
[08:58] examples of very crazy documents that
[09:01] are a lot harder to
[09:04] parse. Um,
[09:08] this one.
[09:12] Okay. So you see like this one. If you
[09:14] have a document like this, like this is
[09:17] kind of crazy, right? Um now I don't
[09:19] know if your documents are this crazy.
[09:21] This is kind this is like an example
[09:22] document we use when testing
[09:25] uh you know data extraction
[09:28] because it's it really shows like how
[09:31] complex layout could be. So let me just
[09:33] try if we had that one what would
[09:36] happen. All right. So
[09:39] u just calltoso.pd PDF. Okay. And then I
[09:44] assume that we can convert. Can we
[09:47] convert a PDF
[09:50] hopefully?
[09:52] Let me just make a new file. Extract
[09:56] PDF.
[09:58] PY. Okay. All right. So, this one is
[10:02] going to be Ktoso.
[10:05] PDF.
[10:07] Um, and I think mark it down. It must
[10:11] support PDF, right? Yes, it does. Uh, so
[10:14] then we're going to markdown and then,
[10:17] uh, I'm not even going to do the next
[10:18] step. I just want to see what the
[10:20] markdown is like.
[10:22] Okay. So, let's try this. Extract PDF.
[10:32] Uh, let's see. PDF.
[10:35] Okay. So, for this one, we do have to
[10:37] install
[10:40] uh another I think we can just go like
[10:42] this. Yeah, let's try this. pip
[10:44] install-r requirements.ext. So, it's
[10:47] it's what's called an extra, right? So,
[10:48] right now we have docx extra. So, we're
[10:50] going to add on the PDF extra. Oh, okay.
[10:53] Apparently, that's not the valid way of
[10:54] doing it. Oh. Oh, I see you do commas.
[10:56] All right. You can see
[10:58] see how often I install multiple extras.
[11:00] Okay.
[11:04] So let's try.
[11:06] Okay. So now you can see it brought in
[11:08] PDF plumber, PDF minor, pillow, and pi
[11:12] PDFM. Uh that's I'm new to a lot of
[11:15] these pillow. I know we use that all the
[11:17] time, but the other ones are are a bit
[11:19] different because also in this repo we
[11:21] have pi mu PDF for LM and that's another
[11:23] one we can compare. Right. So now let's
[11:26] try running this and see what it comes
[11:28] up with um for for that crazy document.
[11:32] I might want to like
[11:34] Okay. So,
[11:37] yeah, it's a little rough. Uh,
[11:41] it's pretty rough. It's pretty rough.
[11:43] Okay. Uh, let's say save to a file.
[11:49] Uh, with Come on, Copilot.
[11:52] Write my code for me. Copilot. Thank
[11:53] you. Okay.
[11:57] All right. Uh, so we're going to say
[11:58] Ktoso. Mark it down. Okay,
[12:03] let's just run that. And then we also
[12:05] have in this one we have pi
[12:08] moo pdf. So let's try
[12:12] pyu pdf as well
[12:16] for comparison. Poo pdf.
[12:20] Okay. So we're going to say and then
[12:24] here not going to print it. Okay. And
[12:27] we're going to do pintoso.pdf. Ktoso
[12:31] slashpy new PDF.
[12:34] Uh we'll call this mark it down result
[12:40] and then
[12:43] uh py move pdf result
[12:47] and py move pdf. Okay.
[12:52] And write argument must be a string.
[12:54] Okay. Okay.
[12:57] Document converter result. Um,
[13:02] I'll just give that to Copilot.
[13:07] Um,
[13:09] so Honor says, "You're trying to avoid
[13:10] PDFs as much as you can, but sometimes
[13:13] you cannot." Yes, that's generally true
[13:16] with me in life as well. I tried to
[13:18] enjoy envoy PDFs for much of my life,
[13:20] but I seem to increasingly be surrounded
[13:22] by PDFs everywhere and PowerPoints. I'm
[13:26] gotten I've started I've now discovered
[13:28] you know PowerPoint PPDX is an XML
[13:30] format. So it's it is like something you
[13:33] can programmatically deal with but
[13:36] um yeah
[13:39] let me see. Oh maybe I already fixed it.
[13:41] Let's find out.
[13:47] Uh so you said you missed this AI system
[13:50] write codes when you're using Jupyter
[13:51] notebooks. You can use Copad in Jupyter
[13:53] notebooks. I find it's a lot more
[13:54] painful. It a lot of times struggles to
[13:58] correctly edit the the notebooks, but it
[14:01] is possible. Um, if you go to Sarah
[14:02] Kaiser's office hours, you can ask Sarah
[14:05] about it. All right, so now let's see.
[14:07] So, this was Ktoso from Mark It Down,
[14:10] and then this is Ktoso from Pyu PDF.
[14:15] And I don't know that we're going to see
[14:17] like
[14:18] um significant
[14:20] improvements across them. Let me open up
[14:23] this one. Okay. Trying to split it.
[14:25] Okay. All right. So, you can see, you
[14:29] know, there's
[14:31] It does look like maybe Pyu PDF did a
[14:35] slightly better job. I'm kind of seeing
[14:37] like less
[14:39] repetitive
[14:41] stuff. Um, but it's really going to
[14:43] depend on what, you know, how your stuff
[14:45] is laid out and what your end goal is.
[14:47] But it does just as like I'm just
[14:50] scrolling through this really quick, but
[14:52] it kind of looks to me like I'm seeing
[14:54] better results for PI new PDF. So um and
[14:57] that's specifically using their four
[14:58] LLM. Now you still have other options,
[15:01] right? You can try um you know using
[15:05] markdown with document intelligence. So
[15:07] that's just you can set up a document
[15:08] intelligence endpoint on Azure. That
[15:11] will cost money though. Um but it is
[15:15] it's another option. and then also the
[15:17] the the LLM option. So, um you know, I
[15:21] would try various things, but you want
[15:23] to you have an idea of what what results
[15:26] you're looking for and also try
[15:31] LLM doc intel. So, I usually use, you
[15:35] know, I usually use document
[15:36] intelligence. Um let's see, do I have um
[15:41] you print all your documents
[15:44] like a printer? Uh both of them skipped
[15:46] all the images. That's right. Yeah. So
[15:48] why don't we try adding we can go ahead
[15:49] and try adding this um this option here
[15:51] lm client. Um so it should be
[15:56] that we can pass down. Okay. So I'm
[15:58] going to do lm plugins. All right. So lm
[16:03] client. Let's see. Do I have my open eye
[16:05] client here? I do. Yeah. So I should
[16:07] just be able to pass that in. My model
[16:10] is this one. Model name. LM prompt. I'm
[16:15] not going to give it a prompt. It's
[16:16] optional. Okay.
[16:19] All right. Let's just see if that um
[16:24] let's see if that works. Uh
[16:29] I don't know if it's going to properly
[16:30] support the Well, hopefully it supports
[16:32] Azure OpenI because this is a Microsoft
[16:34] product.
[16:36] You never know, though.
[16:39] Okay, so it claimed to work. It didn't
[16:42] have any issues. So, let's look at look
[16:44] at it now. Do we see any descriptions
[16:50] article version of this poster?
[16:54] Um,
[16:56] I can't really tell
[16:58] if it changed something. So, we'd have
[17:00] to do let's do let's compare uh
[17:06] down normal.
[17:10] Okay. So I have this one
[17:13] and mark it down image
[17:17] normal enable
[17:20] plugins equals
[17:24] and then
[17:27] okay.
[17:29] All right. Let's try these two
[17:35] and then we could diff them.
[17:39] Okay. I see this one. This one. All
[17:40] right. So diff. Is there a diff? Is diff
[17:43] a command? Yes, it is a command. Okay,
[17:45] great.
[17:47] Ktoso mark it down image and Ktoso mark
[17:51] it down normal.
[17:53] I don't see a diff.
[17:56] So I feel like I don't know either like
[18:00] it didn't you know it didn't work for
[18:02] some reason. It's not giving any errors.
[18:04] Did I think we use MD convert?
[18:08] Um oh but we didn't install the plugin.
[18:10] So let's try you know we have to like
[18:12] explicitly
[18:13] install the plugin. So let's try that.
[18:18] Okay. Pip install
[18:23] requirements.ext. Okay.
[18:35] And then also while that's running what
[18:38] we can do is
[18:43] uh let me index it using
[18:49] uh using document intelligence. Uh so
[18:51] let me see.
[18:55] Okay. So now it's installing a bunch of
[18:57] things. It's getting uh got a bunch of
[19:00] PowerPoint and Excel stuff, too.
[19:02] Interesting. All right. So, now we're
[19:04] going to try
[19:07] running it again.
[19:12] Um yes. So, Shivam asks, "Are tables,
[19:14] images, and other information preserved
[19:16] while OCR?" So, it just depends on how
[19:18] they've implemented it. Right. So, the
[19:20] thing I was going to show is that let's
[19:22] see. Can I
[19:24] um go ahead? Let's see what checking
[19:27] which environments I have set up here.
[19:30] Do I have multimodal running right now?
[19:33] Um let me check
[19:37] as your tenant ID this one.
[19:42] This one. Okay, that looks promising. Is
[19:45] this running right now?
[19:49] I'm checking if I can use my rag
[19:52] application as a test. um because it
[19:55] uses document intelligence. So then we
[19:57] can do a comparison. We'll see if that
[19:59] runs. Okay, going back to this one.
[20:02] Okay, so it extracted and then let's do
[20:04] a diff.
[20:08] They're still the same.
[20:11] Um
[20:13] I don't maybe do we have to say no. I
[20:16] don't know. Um wait, what did it say in
[20:19] the docs exactly for this one? pip
[20:22] install enable plugins equals true
[20:28] if no ele
[20:30] is silently.
[20:32] So I think it might be silently failing
[20:34] and not telling us that it's failing.
[20:36] That's my
[20:38] that's my thought is that maybe that's
[20:40] what it's doing. Uh so let's also try
[20:44] I'm going to take this document and
[20:48] load it in over here.
[20:52] Okay.
[20:54] And and then I'm going to
[20:58] try
[21:00] to index it multimodal.
[21:04] All right. Let's try this.
[21:14] Um, so John says maybe it's under Oh,
[21:18] here. Let's look at this detailed
[21:19] readme.
[21:22] So, we installed that. We installed that
[21:25] D pass LLM client LM model just as you
[21:29] would exactly as you would for image
[21:32] descriptions.
[21:34] Um,
[21:37] works with any OpenAI client.
[21:42] Uhhuh.
[21:45] Embedded images are extracted by
[21:46] position.
[21:48] dox
[21:54] pptx.
[21:56] Oh, and it should say this image OCR.
[21:58] Ah, okay. The most likely cause is
[22:01] missing LM client or model. Uh oh, let's
[22:04] try this. Mark it down list plugins.
[22:07] Okay. Uh oh, here. But this is kind of
[22:10] fun. So, right now it's it's the rag app
[22:12] is ex is processing the file. So, first
[22:15] it extracted the test and then it did.
[22:18] So, document intelligence definitely
[22:19] does find a lot of figures. Look, it's
[22:22] probably going to find way too many
[22:23] figures. So, on page one, it found seven
[22:26] figures. On page two, it found two. Then
[22:28] we got two more. Three more. Two more.
[22:32] Five more. Three more. Three more. Two
[22:35] more. Three more. Okay. So, then you can
[22:37] see for each of them, it's taking each
[22:39] of them and it's uploading them.
[22:42] Um, and then it's also going to describe
[22:46] them. So, there's certainly, at least
[22:48] according to document intelligence,
[22:50] there's quite a few images in here.
[22:54] So, now the question is for mark it
[22:55] down.
[22:57] Uh, oh, sorry. Let me see. Does this
[22:59] work?
[23:03] Oh, we do see it. All right. Maybe the
[23:04] diff command. Sorry. I probably just
[23:06] suck at using the diff command. Okay.
[23:08] So, diff command wasn't showing us up.
[23:10] Look, if we look at this, we can see
[23:12] image OCR. So, it certainly did find.
[23:14] So, then if we compare that to
[23:17] um normal, then we should see the Ktoso.
[23:23] Okay, page one. Ktoso worldwide
[23:27] operation.
[23:32] Anyway, so here you can see see how this
[23:34] says image OCR. So, I think this is the
[23:36] point here. Maybe there is something
[23:40] crazy happening with this though. Look
[23:42] at this article version of this poster.
[23:48] Um, so I'm not sure exactly what's
[23:52] happening there. Um, something weird is
[23:55] happening. Uh, so here, but you can see
[23:58] that it did do an image OCR. So that
[24:01] image was if we look at that image
[24:04] um it is grabbing oh that's this one.
[24:09] It's got to be this one right because
[24:10] it's grabbing all those cities Irvine.
[24:13] Yep. And OCR
[24:16] and then we see oh I think it also
[24:19] extracted a text. So that's the
[24:20] interesting thing is that this one I
[24:23] think extracted both the text. Oh gosh.
[24:26] I don't know. There are a few issues
[24:28] here.
[24:32] Uh, every layer is repeated twice. Yeah,
[24:35] I mean PDFs are crazy. Like this is also
[24:37] because we're doing this as a PDF,
[24:38] right? Like maybe a DOCX would be
[24:40] cleaner. Like PDFs are probably the
[24:42] messiest thing you can deal with, right?
[24:43] So you definitely want to, you know, set
[24:46] up some evaluations there. Um, but it is
[24:49] do it is doing the OCR. Um, that's
[24:51] probably the cleanest part of that. But
[24:53] it's doing some sort of some like
[24:55] repeated stuff like yeah maybe every
[24:56] tech every letter is repeated as an No,
[24:58] but it's it's not that every letter is
[25:00] repeated as an image because we know
[25:01] that image OCR blocks are surrounded by
[25:03] image OCR, right? Um okay. So it did
[25:06] finish. All right. So you can see it
[25:08] uploaded everything to blob storage and
[25:10] then it it um described it using the LLM
[25:14] and then it embedded everything and
[25:16] uploaded it. Okay. So now that that is
[25:20] uh uploaded, I can go back to that uh
[25:24] thing here and then say tell me about
[25:28] Ktoso's cloud architecture.
[25:31] Let's try this. I've never I've never
[25:35] tried this as a sample doc here.
[25:38] It seems like a fun one though.
[25:41] Uh,
[25:44] so hopefully it's going to find the
[25:47] matching chunks. Okay, here we go.
[25:52] D. So what I'm going to do is check. So
[25:54] you can see it's referencing figures as
[25:56] well. So it's both referencing the text
[25:58] and figures on the in the text. So you
[26:00] can see figure 2.1
[26:03] yada yada yada. It's grabbing more
[26:06] things. I asked it kind of a big
[26:08] question. It grabbed another figure. So
[26:10] it's grabbing it's getting a mix of text
[26:11] results. So now what we can do is look
[26:13] at the um supporting content and we can
[26:16] see so this is this is what's nice here
[26:19] right. So um you know the way we do
[26:21] figure descriptions is we say okay this
[26:23] image is a network diagram blah blah
[26:25] blah like we're actually kind of
[26:26] describing it look more like alt text
[26:28] right uh this image is network diagram
[26:30] let me ask the question from the first
[26:32] page so we can compare the actual right
[26:34] so networking infrastructure okay what
[26:38] I guess we'll say what cities
[26:42] what cities
[26:46] host pentos
[26:48] networking gain architecture because I
[26:50] want to see the description of that map.
[26:55] So this is with um this this is with
[26:58] document intelligence extracting out the
[27:03] um this the uh the stuff and then
[27:06] sending it to an LLM for description. So
[27:08] now if we look at supporting content
[27:11] right so it's very different where it
[27:12] says this image is a world map showing
[27:14] an onress network with labeled office
[27:16] locations.
[27:17] So, I think that's I think that's
[27:19] better. Um, there's more information
[27:22] here than just an OCR, right? The OCR
[27:24] was just doing optical character
[27:26] recognition. So, it was only extracting
[27:27] the text versus this one where we're
[27:29] saying like, you know, hey, um, you
[27:32] know, we want to describe it. And, you
[27:34] know, part of this is because this is
[27:35] just what we've asked it to do. So, if
[27:36] we look at media describer, this is
[27:38] where I've implemented it. So, this
[27:39] code's all open source. You can take it.
[27:41] Um, so here I say, hey, you're a helpful
[27:43] assistant that describes images.
[27:45] Describe the image with no more than
[27:46] five sentences. Do not speculate about
[27:48] anything you don't know. Um, this is
[27:51] based off of my experimentations, right?
[27:54] So, this is literally what I'm sending
[27:55] to it. So, it, you know, you might have
[27:57] different desires for how you want your
[27:59] images described.
[28:01] Um, so I think that's the best result.
[28:05] You're welcome to, you know, copy this
[28:08] code into your own. You can see all the
[28:10] code we use here in order to use
[28:11] document intelligence and extract out
[28:14] the figures and we also extract out
[28:16] tables
[28:17] and so that we keep both the the figures
[28:22] and the tables.
[28:26] I I do think document intelligence I
[28:28] mean it's great that there's open source
[28:30] packages for things but um I like
[28:33] document intelligence. I think you're
[28:35] like the new thing is content
[28:36] understanding. So you can also try that.
[28:38] We do have content understanding in here
[28:40] as well. Um, where am I? I think it's
[28:46] here. That was using like the first
[28:48] version of the API. Maybe it's easier to
[28:50] use now. But that's basically wrapping a
[28:52] multimodal LLM as far as I understand
[28:55] it. Uh although I've heard it has gotten
[28:57] better. So it's also worth checking out
[28:58] the new content understanding analyzers
[29:02] um to see how they work. But generally
[29:04] document intelligence works well for me.
[29:05] So that is under you can grab that code
[29:10] over
[29:12] here. There's the what you want is the
[29:16] PDF parser that uses document
[29:17] intelligence.
[29:19] You know, just point your friendly local
[29:21] co-pilot at it if you got if you didn't
[29:24] get killed by the plan. Um let me get
[29:28] rid of those.
[29:30] Okay.
[29:34] All right. Um,
[29:36] so, so there we go. So, we saw a few
[29:38] different approaches and,
[29:42] um, you know, it definitely takes some
[29:45] tweaking. I spent a long time just
[29:47] tweaking tweaking this one um, both of
[29:50] these um, options here to try and figure
[29:53] out, you know, how I wanted the
[29:56] descriptions to work and then also just
[29:58] figuring out how I wanted them to like
[30:00] chunk up here. So here you can see in
[30:02] the chunks this is the markdown from the
[30:04] actual page and then I embed the figure
[30:08] descriptions and I never split figure
[30:11] descriptions. So I always keep the full
[30:13] description in a chunk.
[30:17] All right let's see um
[30:21] yeah so for document intelligence this
[30:22] is this is my this is the main repo and
[30:25] that's the code we shared. Uh I
[30:26] unfortunately I don't have standalone
[30:28] ones just because it's it is actually a
[30:30] fair amount of code and I didn't want to
[30:32] maintain it separately. Um I should make
[30:35] it like a skill like an agent skill that
[30:37] that would be the way to to make it more
[30:39] portable now. All right. The other
[30:43] question was uh okay going way back is
[30:47] son still here? Yes. So using the text
[30:49] embedding small modern you keep getting
[30:51] could not complete the vectorization
[30:53] action.
[30:54] Um, the vectorization endpoint returns
[30:58] status code 400. So presumably you are
[31:01] using Azure AI search or Foundry IQ.
[31:04] Correct. Because that error message
[31:06] sounds to me like an Azure AI search
[31:11] um error message. Yes, AI search. Yeah.
[31:15] So yeah, I definitely have seen it. It's
[31:17] when I haven't set up the um the
[31:21] permissions correctly. So, let me find I
[31:23] have actually worked a bunch with that
[31:24] when the last week. Uh, we do have that
[31:26] set up in this repo, but this repo is
[31:28] more complicated. So, let me find
[31:31] where I think I set it up more simply.
[31:35] Um, because you're going to need the
[31:36] right permissions setup. So, let me find
[31:39] it.
[31:42] Yeah. Uh, I think this is what you might
[31:45] be missing this one. Um, Cognos. Okay.
[31:49] So you can see how this one has
[31:53] so see how the search service has a
[31:55] principal ID.
[31:58] Um so this one we give it two things. We
[32:02] give it the cognitive services open AI
[32:04] user role. So we give it to the
[32:06] principal ID of the search service and
[32:10] um we also give it the Azure AI user
[32:12] role. I think that this one should be
[32:14] enough for the vectorzation endpoint. Um
[32:17] but I don't remember exactly. It should
[32:20] also be documented in the Azure AI
[32:23] search. Um
[32:25] this would be integrated vectorization
[32:29] openi user ro principal ID and find it.
[32:34] It works but fails randomly. Well that's
[32:36] bad.
[32:38] Um if it's working sometimes but failing
[32:40] other times then that's that's an issue.
[32:42] If you if you like message me with your
[32:45] um
[32:47] search service ID and like the time that
[32:49] it happens, then I can ask the search PM
[32:51] to look at the logs because sometimes he
[32:54] can actually
[32:56] see what's going on because it should
[32:58] work
[33:00] sometimes. I mean, it should work either
[33:02] all the time or no times. If it's only
[33:03] working sometimes, then um you know,
[33:07] that's that's not good. That's no bueno.
[33:09] Uh, so I was just looking for the
[33:11] cognitive services
[33:14] just to make sure. Yeah. So this one
[33:15] says
[33:18] um
[33:19] you're going to select the manage
[33:21] identity. So this one says cognitive
[33:22] service open eye user. So that that
[33:24] should be the main one that you need. Um
[33:27] and if you say if it's working if it is
[33:29] legitimately working sometimes. I mean
[33:31] double check your roles but if it's
[33:32] working sometimes.
[33:34] Okay. All right. So okay. So that's I
[33:38] wonder if it's
[33:40] So maybe then the 400 is not an off
[33:44] error. Maybe the 400 is a rate limit
[33:46] error and it's not surfacing that rate
[33:48] limit error to to us. Um
[33:53] yeah. So
[33:56] so that sounds like it might that's
[33:58] actual service issues. So, um if you if
[34:02] you like have like if you like have like
[34:04] a fancy like customer account
[34:06] representative already, I would give
[34:07] them the information. But if not, then
[34:09] you can just uh message me the
[34:12] information
[34:14] uh on LinkedIn
[34:18] uh or Twitter or wherever. Uh maybe I
[34:21] think LinkedIn's the easiest. I guess
[34:23] you can also DM on Discord. I don't
[34:24] really know which places I have open DMs
[34:26] cuz I don't really know how all there's
[34:28] too many social media platforms now.
[34:30] Anyway, I think what we need is your um
[34:32] give like the subscription information
[34:34] and the search service ID and the
[34:36] timestamp that it happened. That might
[34:39] be enough for the search team to check.
[34:42] I'm guessing
[34:44] that what is happening is a rate limit,
[34:49] but um not positive. Uh let me also just
[34:53] ping the search PM on that.
[34:58] Uh search customer is sporadically
[35:02] getting 400s from vectorization.
[35:06] Would that be a rate limit error or
[35:11] something else?
[35:14] Only sometimes.
[35:16] All right. Okay. Okay. Well, I just
[35:17] messaged the PM
[35:20] for search.
[35:23] Uh so, so we'll see if he has a reply in
[35:27] the next 15 minutes. Um otherwise,
[35:30] um we might ask for some information
[35:32] from you.
[35:35] Let's see what else. Um okay, so Honor
[35:39] asked, "Do I have a workflow for
[35:41] accessing PDFs in SharePoint? Do you
[35:43] have to use the graph API?" Well, if
[35:45] you're just accessing,
[35:48] you can kind of use work IQ maybe. Um,
[35:51] let me see. Is my work IQ working right
[35:53] now? But you can't get that much
[35:55] information, right? Like, um, right?
[35:57] Because you probably want to get the
[35:58] full document. I think if you want the
[36:00] full document, then you're going to have
[36:01] to use graph API. Um I think in the
[36:04] future work IQ is going to have more
[36:06] functionality like um to do to do more
[36:09] more of the graph commands but currently
[36:13] I think you'd have to use the graph API
[36:14] if your goal like if you're trying to
[36:16] ask questions about the document then
[36:18] you could should be able to ask
[36:19] questions versus work IQ but if you're
[36:20] trying to get the entire document then
[36:23] it's currently you'd have to use the
[36:25] graph API. Uh it's possible in the
[36:27] future that work IQ um would pass
[36:30] through and and let you do it but not
[36:32] currently.
[36:35] Let's see. Have I tried the Azure AI
[36:37] Foundry Atlassian MP server with OOTH
[36:39] paths through authentication seed tool
[36:42] calls fail?
[36:44] Is that a Foundry issue? Where are you
[36:47] calling it from? Are you calling it from
[36:48] your own agent code or from a Foundry
[36:52] agent? Um,
[36:55] what's the situation there?
[36:59] Uh,
[37:02] playground agent is that? So, if you say
[37:05] agent, you're saying it's a prompt
[37:06] agent.
[37:07] Um, it's like a prompt agent. Let me
[37:10] see. I have a prompt agent over here.
[37:15] A prompt agent. Okay. So, um, yeah,
[37:20] prompt agents can be really tricky to
[37:23] debug when they don't work. And we
[37:27] actually ran into one of the things I
[37:28] was doing this week was working on using
[37:30] Enthropic with prompt agents. And
[37:32] unfortunately,
[37:34] it's only working half the time and then
[37:36] it's having an error with MCP. So,
[37:39] there's something with the tool calls. I
[37:40] presume you're probably not. You're
[37:41] probably using OpenAI. Um, so I guess
[37:45] you added on the tool.
[37:50] Uh, is it Can you get it through here? I
[37:54] guess it's from the catalog.
[37:56] Atlassian.
[38:00] This one with the remote MCP. Yeah, I do
[38:02] know that we're having issues right now
[38:04] with the remote MCP server, like our
[38:06] custom remote MCP server, and we're just
[38:08] getting internal server error. So if you
[38:11] have once again if you have the request
[38:14] ID so for example like here um uh hi
[38:17] what cupcakes I'm not sure if this is
[38:19] still running but let me see
[38:24] catalog is still accessing okay yeah
[38:27] also the big thing we're working on this
[38:29] week is foundry hosted agents and the
[38:31] new version of that and so that would be
[38:33] a different instead of prompt agent
[38:34] because prompt agents are more limited
[38:36] and harder to debug foundry hosted
[38:38] agents um so far for me are easier to
[38:42] debug because the agentic loop is
[38:44] actually happening in a Docker container
[38:47] and you can like watch the container
[38:48] logs. So you might consider moving to
[38:51] Foundry hosted agents um once uh the new
[38:54] version's out hopefully this week, maybe
[38:58] next week. We'll see. Uh okay. Okay.
[39:00] Order the cloud special.
[39:04] All right. So this is you know
[39:05] interacting with a remote MCP server. Uh
[39:11] uh I haven't tried one at slash SSC.
[39:13] Okay. So here um so I just wanted to
[39:15] show the error so you can see is this
[39:17] the kind of error you're getting like
[39:19] this sort of internal server error.
[39:22] Let's see. Does hosted work in private
[39:24] networking yet? I don't know. Let me go
[39:26] and um add oh and also the search
[39:29] service PM if you can provide your
[39:31] search service ID and time stamp that it
[39:33] happens then he can check the logs. Uh
[39:36] so if you're not comfortable putting it
[39:37] here, let me just like can I like friend
[39:39] or something? Friend add friend, you are
[39:42] now well I just sent you a friend
[39:44] invite. So uh if you can ping me for
[39:48] search service, ping me with your search
[39:49] service ID and subscription and time
[39:53] stamp that you got the error then he can
[39:54] check the logs. Um and yeah, is this the
[39:58] is this the error that you're seeing for
[40:00] foundry prompt agents? And then let me
[40:03] check on will foundry hosted agent new
[40:08] version work with private networking.
[40:10] I'll just ask the team about that. Um I
[40:13] think in theory they it should but uh I
[40:16] haven't tested it myself.
[40:20] Um, so also yeah, if you do get an error
[40:23] like this, once again, if you have this
[40:25] request ID and if you can send the
[40:27] request ID to me, I can have that same
[40:32] PM check the logs to get more
[40:36] information. Um, but if it's a different
[40:37] sort of error, then I'm not sure. We
[40:40] have to kind of search around to see who
[40:42] can who can help debug it. Um, I haven't
[40:46] tried any of the MCPS with OOTH token
[40:49] pass through, so I don't know generally
[40:50] how well they're working.
[40:54] Um, okay.
[40:58] Let's see
[41:00] what else. So, Pablo pointed out
[41:04] that content understanding has an MCP
[41:06] server and it's under Azer samples. So,
[41:08] that must be an official one. Uh, great.
[41:11] So they already have
[41:13] a Is this a skill? No, it's MCP server,
[41:16] right? That's what it says. Oh, but it's
[41:17] withnet.
[41:23] I mean, if you're if you have net
[41:25] running on your machine, you can
[41:26] certainly try this one out. I my machine
[41:29] often struggles with net. You can see
[41:31] like Oh, this one's actually working
[41:32] today. And my other one
[41:36] uh oh, okay, net's working today.
[41:38] Usually in the bottom of VS Code, I have
[41:40] a little alert that says .NET didn't
[41:41] load. Okay, so yeah, there's a .NET
[41:44] server here. Um, for Azure content
[41:46] understanding, that could be a quick way
[41:48] to get started with, but either way,
[41:49] you're going to have to set up your
[41:50] endpoint, right? So, you'll have to go
[41:51] to Azure portal, create a content
[41:53] understanding. Also, this says
[41:55] understanding should be understanding.
[41:58] Interesting. Okay, we'll assume that's a
[42:00] typo. Um,
[42:03] yeah, so set that set that up.
[42:07] Uh, let's see.
[42:12] There we go. All right. Uh, what else?
[42:18] Let's see if I got any more replies. Uh,
[42:21] nope. Okay. All right. So, let's see
[42:23] what else is happening. Oh, yeah. A
[42:25] hackathon. Okay. Microsoft Vancouver
[42:28] hackathon.
[42:30] H.
[42:32] Vancouver web Summit pitch on May 13th.
[42:37] And then you get to go to Websoon Summit
[42:40] Vancouver
[42:42] and and that looks cool. Okay.
[42:48] Okay. Yeah, I haven't been involved with
[42:50] this one, but
[42:53] looks good. Yeah, good luck. Hope you
[42:56] win. Um,
[42:59] I know they did just announce the
[43:00] winners of the agent league hackathon.
[43:02] So, it might be interesting to look at
[43:03] the winners for that to get an idea for,
[43:06] you know, what the judges like. Um, let
[43:10] me see where the Agents League winners
[43:13] were because that just got announced
[43:17] this week.
[43:20] Agents league meet the winners. Was this
[43:22] from this week from? Yeah. Okay, here we
[43:25] go.
[43:28] So that might be kind of interesting.
[43:38] All right. And then what else is
[43:40] happening?
[43:42] Um let's see. We did the pricing. Opus
[43:45] 4.7. Talked briefly about that. Uh it
[43:48] has a huge multiplier in GitHub copilot.
[43:50] So I gave it a small amount of time to
[43:53] prove its worth and then gave up on it.
[43:55] Um,
[43:56] we the big thing that I'm working on is
[43:59] next week's live stream series about h
[44:02] foundry hosted agents. So, we're going
[44:04] to start off with how to host agent
[44:06] framework agents and workflows on
[44:09] Foundry, then link chain and langraph
[44:11] agents and workflows on Foundry and then
[44:13] talk about uh evaluation and safety. So,
[44:16] that'll be next week starting on Monday.
[44:19] Uh, we also have Cosmos DB comp
[44:22] happening on Tuesday next week. So,
[44:23] these are both virtual streams, so you
[44:25] can tune in from anywhere. Uh, there's
[44:27] Agent Con happening in person on May 4th
[44:30] in Mountain View, Pyon in person in Long
[44:33] Beach in midMay, and then of course
[44:34] Microsoft Build in June.
[44:37] Uh, there's also going to be a virtual
[44:39] Postgress conference, and I made the
[44:43] um I made the the slides for that
[44:46] already. Um, so you can
[44:50] check those out if you want to. And here
[44:53] we go. It's all here. So if you're
[44:54] building MSP servers on top of
[44:56] Postgress,
[44:58] uh you might be interested in that. Um
[45:00] but the actual talk reporting
[45:03] will
[45:05] go out for as part of the Poseette
[45:07] conference, but that's this is just like
[45:10] spoilers if you want to see.
[45:14] Um
[45:16] let's see. Yeah, enthropic. So reminder
[45:18] that you can use enthropic models on
[45:19] Foundry. So, we're going to do various
[45:21] workshops using Enthropic with Foundry.
[45:24] So, that's something fun you can play
[45:25] with is to use different enthropic
[45:27] models like Sonnet. I think we're using
[45:29] Sonnet for all of ours. Um, I also have
[45:32] the Python MCP tutorial. If you're
[45:35] running a MCP tutorial, that can be
[45:38] useful, too. Uh, so yeah, lots of lots
[45:41] of events coming up. Uh, the next two
[45:45] months are going to be packed, and of
[45:47] course, at Build, there'll be lots of
[45:49] announcements. So, that'll be more to
[45:53] talk about then.
[45:56] All right,
[46:00] let's see. Anything else? Um,
[46:05] yeah, just reminder to
[46:08] DM me with any account details if you
[46:12] need any bugs looked into.
[46:19] Oh, okay. Honorag will be at PyCon, but
[46:21] you'll miss my tutorial. Well, I found
[46:23] out I'm going to do another tutorial on
[46:25] Thursday for edu summit. So, if you're
[46:27] going to be there because I know, yeah,
[46:29] my tutorial is very early. It's on
[46:30] Wednesday, so I don't know how many
[46:32] people will be there for it. Um, but
[46:34] there's also going to be edu summit. I'm
[46:36] going to do a little tutorial there,
[46:39] which I have not made yet. That'll
[46:41] happen later. Um, and then we should
[46:44] also have a sponsored session on I think
[46:48] it's going to be
[46:51] Friday because we haven't even Have we
[46:54] announced it? Let's see if we've
[46:55] announced it.
[46:59] Uh,
[47:02] no. So, we'll have a sponsored session
[47:05] on either Thursday or Friday and then
[47:07] we'll be at the booth on Thursday
[47:09] evening, Friday and Saturday.
[47:15] Sylvester says we have a new
[47:18] certification.
[47:22] Oh, it's in Copet Studio.
[47:25] I mean, it's if you're using Copiot
[47:27] Studio. Yeah, I'm not I would fail this
[47:29] exam.
[47:31] I have not used Power Effects, Power
[47:34] Platform,
[47:35] Microsoft Dataverse. I haven't used any
[47:38] of these. Um, this is more of the stuff
[47:40] that I know. Um, but I feel like I'm
[47:43] gonna fail. I would fail the first part
[47:44] of this.
[47:50] Oh, and here's another one. Okay, maybe
[47:52] maybe this one will be more.
[47:55] Okay, so this one.
[47:59] All right. Oh, this looks great. Python
[48:01] and Azure AI services. This looks good.
[48:04] The first 300 people who take it before
[48:06] May 7th get 80% off. Done.
[48:10] Okay,
[48:12] this looks great. I think uh developer
[48:16] develop natural language extract
[48:17] insights from visual data. Is it going
[48:19] to be using content understanding? Yep,
[48:21] that's great. Yeah, you should totally
[48:23] take this one. You have 100 minutes to
[48:24] complete this assessment. I kind of want
[48:26] to just take it without studying and see
[48:27] what happens.
[48:30] What's the study guide? There we go.
[48:31] Study guide. Fun.
[48:36] Okay, great. Yeah, you should you should
[48:40] uh give those a go. Get certified. Oh,
[48:44] did a certification go away? AI 102.
[48:52] Did they say it went away? AI 102.
[48:56] Microsoft e-learning is super boring.
[49:00] Some people really like the
[49:01] certifications. Is that what you mean by
[49:03] the e-learning? I actually I haven't
[49:04] done one yet. Um, you know, there's lots
[49:08] of options. So, if you don't if you
[49:10] don't if you're not into the
[49:11] certifications, then you just come to
[49:15] our come to our live streams instead and
[49:18] we try to make those fun. All right,
[49:21] everyone. I have to go now because I
[49:23] actually have to record that Postgress
[49:25] talk um because it'll be a pre-recorded
[49:28] talk and uh yeah. Oh, Sylvestria has
[49:33] lots of fun links. AI skills navigator.
[49:36] This looks like it's learning related
[49:37] too. Standing still isn't an option.
[49:46] Fun. All right, everyone.
[49:49] Thank you so much for all the great
[49:51] questions. It's always fun to explore
[49:53] things together and I hope to see you
[49:56] next week on Monday for our foundry
[50:00] hosted agents series and I really hope
[50:04] that we release the foundry the new
[50:05] version of Foundry Hosted agents before
[50:08] that live stream so that we can show you
[50:11] all the new stuff happening in it. All
[50:14] right everyone, see you next time. See
[50:17] you Monday. Bye.
