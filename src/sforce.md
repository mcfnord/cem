## Three writing samples

I've chosen these three examples of my work. See more by visiting [my online 
resume'](http://tucc.us/resume).

### Sample One: Cloud Storage Paloosa

- **SAMPLE:** [Get started with Azure Blob storage](https://docs.microsoft.com/en-us/azure/storage/storage-dotnet-how-to-use-blobs) 
- **MY ROLE:** This was a collaborative effort with two non-writers. They knew what areas 
they wished to cover, what audience they had in mind, and how much time the tutorial 
should take. I tailored the code snippets, steps, and details to be clear and helpful (and accurate).
I remember actual fighting-like-dogs events 
around this document, as it was a symbolic part of a re-invention of documentation for the Microsoft cloud initiated by a VP. I mediated some disagreements and engaged in a few.
We shipped a document and new doc framework that has stood up over some time!

(Do note there's new writing in this document that 
wasn't in my original.)
- **EDITED MYSELF?:** Yes.

### Sample Two: What Humans Want From Machines

- **SAMPLE:** [Human Interface Guide](http://tucc.us/docs/hig.pdf)
- **MY ROLE:** Constructed publication from diverse source materials and interviews.
- **EDITED MYSELF?:** Yes.

### Sample Three: Company Vision

- **SAMPLE:** [Engineering Roadmap](http://tucc.us/docs/roadmap_blur.png) 
- **MY ROLE:** 
(This is blurry at owner's request.)
Worked with 
technical staff to plan engineering roadmap. 
This marketing information features the assets of a ten million dollar company during its successful, solvent 
bankruptcy. 
- **EDITED MYSELF?:** Yes.

### Bonus sample: Tedium is Troublesome

- **SAMPLE:** [Walkthrough: Manually Deploying a ClickOnce Application](https://msdn.microsoft.com/en-us/library/xc3tc5xx%28VS.100%29.aspx) 
- **MY ROLE:** (I felt bad about showing you that blurry sample.) This is 100% my work. I'm 
including it because it's a very tricky topic. Nobody could use it. Then I wrote this and 
people were more successful with this technology. It's still a very tricky technology to 
use. I wrote this by using the heck out of the Mage.exe tool. 
- **EDITED MYSELF?:** I had the help of a skilled editor.


## Answeraire in response to Questionaire

I've organized my answers to your questions into something like an essay.

I've written for SaaS and Web applications. 

Perhaps Web-based software can be more opaque than traditional software. If I know that my user has a 
browser on the internet, then I can reach them there! Since I'm not shipping content, but only links to 
content, I can push more to readers, get feedback more often, and fix errors in a snap. So Web-based 
software does have some advantages for writers and publishers.

Any pre-product source suggest explanations of features, special cases, and caveats that might help 
anyone use the finished product. As the writer, I'll pass along everything written in source documents that could 
possibly help. Sometimes I'll erase old documents because they're fully reflected (more accurately and clearly) in new ones.
Reading and repeating are large parts of the job. Culling can be, too. 

Whenever possible, I want to build 
guidance using running code. I certainly have to *finish* it using running code.

### Telephone Tricks

You've asked about CRM experiences. One project I worked with in Seattle had clever techniques for 
learning more about customers and prospective customers.

The web-based software provided a powerful 
platform for learning marketing costs of inbound call enterprises, recording calls securely, 
routing calls based on the area code of the caller, and other clever, useful stuff. 
That telephone software had many CRM features. Businesses want to know who calls, and who calls once vs. 
twenty times. Some flavors of the tracking technology determined first-time caller demographics as the 
call rang, or told you exactly which search terms preceded the call. Tricky! Clever! Valuable!

The browser-based UI 
for this tool was garbage, unfortunately. A team answered calls all day about the browser app's snafus and quirks. I 
was given broad authority to upgrade the app's documentation. I designed a Markdown-based platform that 
let me publish easily to both PDF and a browse-able hierarchy of HTML. I made sure my design let anyone 
get a URL to a specific page and section in the content. The final publication might have been 300+ 
pages, including newbie walkthroughs, nitty-gritty details, magic tricks, and developer APIs. I 
methodically studied app features and failings, using bug reports, design docs, source code, and logs of 
incoming email support incidents. When I was done, the team taking customer calls could send back a URL! 
They didn't have to hold the caller's hand, because my docs did that. And that customer, with a 
browseable hierarchy and PDF, might never need to call back. Or when they do, they'll have a much more complicated set of objectives for the software.
Looking good in print can help users and developers, and can also help make external partners more comfortable about the maturity of your platform.

I documented [the REST-level API of the Windows Azure storage system](https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/lease-container). 
I learned about it from existing 
documentation, plus clues about features that hadn't been documented yet. External and internal blogs 
offered some clues. I learned about these features by using them. Sometimes that meant using an app like 
Fiddler, or using a framework like the .NET SDK for Azure storage, and tracking the HTTPS traffic using 
Fiddler again. Other times I had to know where Azure logs some events. When something just didn't make 
sense, I had experts I could ask. Or experts who could ask other experts.

I remember feeling really frustrated with a new Azure storage feature, a simple copy-file-to-cloud API. 
I had the newest SDK, but my file never fully wrote to the cloud. Some small ones did, but larger ones 
didn't. The experts said I'd get an exception if it failed. They asked if I was ignoring exceptions from 
their code. I simplified my repro case, by switching to public storage buckets, and making a simple 
command line report of how many bytes were transferred. I put the .EXE on a server and went home. In the 
morning, I learned I wasn't failing, the .NET layer was. The dev [released an explanation blog post at 
11pm](https://blogs.msdn.microsoft.com/windowsazurestorage/2011/09/27/blob-download-bug-in-windows-azure-sdk-1-5/), 
and the SDK bits were revised the next day.

With the feature finally working, I could write about it down to its nuances, by triggering all the 
features the interface claimed to provide. Here's what I wrote next:

[Setting Timeouts for Blob Service Operations](https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/Setting-Timeouts-for-Blob-Service-Operations)

### Heroics in Technical Writing

I was hired as part of a turnaround team to save a company from collapse. There were about 200 
employees. The company collected price data without getting noticed. 
The staff included hackers whose 
code was poor and opaque. As I documented their systems, 23 were laid off. I reviewed all returned 
company computers for critical information, and found some. The whole turnaround involved centralizing 
and surfacing every function of the enterprise. Eventually I filled a wall with maps of the stealth 
network, databases, scripts, and code repositories that drove the enterprise. Engineers scrutinized my 
wall of systems and plans. Prospective buyers examined the enterprise using large-format technical 
diagrams and roadmaps I developed. 
I video taped some technical talks and dramatically compressed 
them so the India teams could watch. One day on the wiki, I found detailed tribal knowledge collected in 
India, but thick with vernacular. I turned it into easy guidance. I re-wrote their entire technical 
wiki, structuring it into browsable information for the first time.

After the layoffs, the company entered bankrupcy! Apparently the founder had misappropriated seed 
capital from his first start-up, and the aggrieved party had gained access to our payroll account! 
This is an unusual level of uncertainty for a 9-5 job. But... the only people left were those whose 
hearts were in it. Once the heat stopped working in our Pioneer Square brick office, at a 
particularly cold time of year. Having a scrum in our winter coats was a fun diversion to me. It just 
enthused me, as the whole job did, precisely because the chaos was obvious, but so was our grit. I 
liked using capturing, writing, publishing tools and techniques to have such an obvious impact, 
during nothing short of a crisis.

At one point the leadership worked with staff to evaluate the hiring priorities and needs. I asked 
them to use Post-its to add career details and hiring criteria for people we associated with company 
expansion tasks. I integrated meeting feedback into a clear hiring plan. I got to make timlines of 
product improvements, color-coded and easy to follow. The company was saved by a buyer, at ten million 
dollars. My documentation skills, which I got to apply in a myriad of ways, played a pivotal role in the 
re-engineering and acquisition processes.


### More Stuff I believe

My typical process favors a finished product. ;) I've ingested (*burp*) specs, requirements, and 
prototypes by the tens of thousands of pages. I read them all with a highlighter uncapped. But those are 
mere suggestions of what the user might get some day. I want to talk about what works. Where can I get 
the daily dev build, and log of check-ins and diffs? How can I add documentation-specific flags to bugs? 
How can I log details of what I want to confirm in the finished product? Specs, requirements, and 
prototypes are vaporware. I often work with these clues to build a skeleton of topic titles.
A good title can evoke details and clues from everyone. Sometimes I wish I wrote titles 
for a living. Alas, details matter. Accuracy matters. 

At a company called Qpass (now Amdocs) I single-sourced using AuthorIT, a professional publishing 
package. A more unusual instance where I single-sourced involves Microsoft's Azure cloud platform. I 
worked in a small group to rewrite all the emails Azure sends to users about critical account events. 
This task was unique because the tool that emailed users was a Microsoft-wide tool, serving huge 
audiences with important billing, access, and other event details. Many of the paragraphs about credit 
cards and access control were used by multiple organizations and products! We had to modify the text 
enough to help our customers, without throwing other customers into confusion about, say, their Office 
subscription. We ended up mixing the shared paragraphs with some custom paragraphs of our own. I still 
remember this when I get these emails from Azure. And it's a good critique of single-sourcing: Trying to 
reach diverse audiences with chunks of tagged content can be a pain, especially when audiences differ 
significantly.

## What does John Know, Really?

What do I know? Let's dive in!

### XML authoring tools like Oxygen or Arbortext Editor

  - **Used daily?:** No.
  - **Self-rating:** 6
  - **Comments:** I don't use this stuff daily, but still 
rate myself competently, because I speak XML, and because 
I've worked closely with DocStudio, the XML-based content 
management behind MSDN. I've also used AuthorIT, which tags 
chunks.  I've done a lot of non-documentation XML, and a lot 
of documentation. And I've implemented chunk insertion in this platform, where I'm writing to you now.
You can learn more about this platform by following the links at the end of this page.

### Image editing/creation software

  - **Used daily?:** Yes.
  - **Self-rating:** 7
  - **Comments:** There are many high-end image tools, but I rarely use them.
I can create 
a miserable image using the coolest software. I can also 
create great images using rather average tools. In this 
example, I used Visio:
      
![](http://i.msdn.microsoft.com/dynimg/IC588554.png)

That diagram is part of 
[this reference topic](https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/lease-blob), 
which I significantly re-wrote and amended.

I also [create animated gifs](http://ec2-35-165-168-112.us-west-2.compute.amazonaws.com/an_color.html) 
as a hobby.

And I use [ffmpeg](https://ffmpeg.org/). So. I'm kind of a big deal.
  
### HTML

  - **Used daily?:** Yes.
  - **Self-rating:** 8
  - **Comments:** Yeah, I use HTML daily. I learned HTML before there was CSS. Now HTML can include 
JavaScript libraries that navigate the DOM and round-trips asynchronously with servers. HTML5 goes in 
directions I can't really list. 
[This code, in PHP, implements a link forwarding tool](https://github.com/mcfnord/cem/blob/master/em-is-us/makelink.php) 
using many tricky features of 
HTML.

### Source control software

  - **Used daily?:** Yes.
  - **Self-rating:** 7
  - **Comments:** I use git and GitHub daily. I've made 
branches, pushed and pulled with it. [John's GitHub](https://github.com/mcfnord/)


## Bring it on home

I like writing, getting the scoop, and delivering the news. In this case the 
news might be the full description of what a user must know and do to make your offering 
valuable to them. A technical writer is the user's last line of defense. Maybe the UI is 
only halfway to where we want it. Telling the user now what they can do now is fun for 
me. Showing everyone what it *really* takes to use a software product can help drive the 
designs for improvements. I like how writing can clarify just how successful we are at 
simplifying user tasks. 
Writing can separate the substance from the vapors, let the chips fall where they may. 


## Markdown publishing tool

I wrote all this on [my own publication 
platform](https://github.com/mcfnord/cem/blob/master/pub.sh). 
You can see [the Markdown source for the file you've just 
read](https://github.com/mcfnord/cem/blob/master/src/sforce.md). 
Single-sourcing your cup of tea? I've added [a feature to single-source from DIV tag attributes in my
markdown source](https://github.com/mcfnord/cem/blob/master/add-insertions.py)
 with this syntax:

> insert: sourcefile classname
 
