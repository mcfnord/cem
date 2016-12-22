## Three writing samples

Samples, samples, samples! 

### One

- **SAMPLE:** [Get started with Azure Blob storage](https://docs.microsoft.com/en-us/azure/storage/storage-dotnet-how-to-use-blobs) 
- **MY ROLE:** This was a collaborative effort with non-writers. They knew what areas they wished to cover, what audience they had in mind, and how much time the tutorial would take. I tailored the code snippets, steps, and details to be clear and helpful. (Some sections have been added since the first publication of this document.)  
- **EDITED MYSELF?:** I may have informally involved my officemate, who also edits, but officially I played the writer and editor roles in this project.

### Two

- **SAMPLE:**
- **MY ROLE:**
- **EDITED MYSELF?:**

### Three

- **SAMPLE:**
- **MY ROLE:**
- **EDITED MYSELF?:**


## Answeraire in response to Questionaire



![](img/firstfive.png)

I've written for SaaS and Web applications. One system in particular gave non-technical 
users a powerful platform for learning marketing costs on inbound call enterprises, 
recording calls securely, routing calls based on the area code of the caller, and other 
clever, useful stuff. The browser-based UI for this tool was garbage. A team answered 
calls all day about the browser app's snafus and quirks. I was given very broad authority 
to upgrade the app's documentation. I designed a Markdown-based approach that let me 
publish easily to both PDF and a browse-able hierarchy of HTML. I made sure my design let 
anyone get a URL to a specific page and section in the content. The final publication 
might have been 300 pages, including newbie walkthroughs, nitty-gritty details, and 
developer APIs. I was voracious in studying app features and failings, using bug reports, 
historical design docs, source code, and logs of incoming email support incidents. When I 
was done, the team taking customer calls could send back a URL! They didn't have to hold 
the caller's hand, because my docs did that. And that customer, with a browseable 
hierarchy and PDF, might never need to call back. I couldn't fix the horrible UI. 
Instead, I used publishing tools and investigation to bridge the gap between what the 
user wants and how this kooky UI can do it.

Perhaps Web-based software can be more opaque than traditional software. If I know only 
that my user has a browser on the internet, then I can reach them there. Since I'm not 
shipping content, but only links to content, I can push more to readers, and get feedback 
more often. Web-based software does have some advantages for writers and publishers.

That telephone software had many CRM features. Businesses want to know who calls, and who 
calls once vs. twenty times. Some flavors of the tracking technology determined 
first-time caller demographics as the call rings, or told you exactly which search terms 
preceded the call. Tricky! Clever!

My typical process favors a finished product. ;) I've ingested (*burp*) specs, 
requirements, and prototypes by the tens of thousands of pages. I read them all with a 
highlighter. But those are mere suggestions of what the user might get some day. Sounds 
like fodder for a skeleton outline, but what is that? That's just scary! I want to talk 
about what works. Where can I get the daily dev build, and log of check-ins and diffs? 
How can I add documentation-specific flags to bugs? Specs, requirements, and prototypes 
are vaporware. While I'm often working with these clues to build out a skeleton of 
user-specific or developer-oriented task lists, I write about apps that run. Those 
pre-product sources suggest explanations of features, special cases, and caveats that 
might help a user use the software. I'll give them everything that could possibly help. 
Reading and repeating are large parts of this job.

Check out my answer to #1, where I published from markdown into both HTML and PDF, using 
pandoc. At a company called Qpass (now Amdocs) I single-sourced using AuthorIT, a 
professional publishing package. An unusual instance where I single-sourced involves 
Microsoft's Azure cloud platform. I worked in a small group to rewrite all the emails 
Azure sends to users about critical account events. This task was unique because the tool 
that emailed users was a Microsoft-wide tool, serving huge audiences with important 
billing, access, and other event details. Many of the paragraphs about credit cards and 
access control were used by multiple organizations and products! We had to modify the 
text enough to help our customers, without throwing other customers into confusion about, 
say, their Office subscription. We ended up mixing the shared paragraphs with some custom 
paragraphs of our own. I still remember this when I get these emails from Azure. And it's 
a good critique of single-sourcing: Trying to reach diverse audiences with chunks of 
tagged content can be a pain, especially when audiences differ significantly.

I was hired as part of a turnaround team to save a company from collapse. There were 
about 200 employees. The staff included hackers whose code was poor and opaque. The 
company collected price data without getting noticed. As I documented their systems, 23 
were laid off. I reviewed all returned company computers for critical information, and 
found some. The whole turnaround involved centralizing and surfacing every function of 
the enterprise. Eventually I filled a wall with maps of the stealth network, databases, 
scripts, and code repositories that drove the enterprise. The CEO sought bankruptcy 
protection, and the prospective buyers examined assets using large prints I prepared of 
the data flows. I video taped some technical talks and dramatically compressed them so 
the India teams could watch. I solicited tribal knowledge from the India teams, and 
translated very dense reports rich with vernacular into easy guidance. At one point the 
leadership worked with staff to evaluate the hiring priorities and needs. I asked them to 
use Post-its to add career details and hiring criteria for people we associated with 
company expansion tasks. I integrated meeting feedback into a clear hiring plan. I got to 
make timlines of product improvements, color-coded and easy to follow.
     
The company was saved, and my documentation skills, which I got to apply in a myriad of 
ways, played a pivotal role in the re-engineering and acquisition processes.

![](img/next2.png)

I documented the REST-level API of the Windows Azure storage system. I learned about it 
from existing documentation, plus clues about features that hadn't been documented yet. I 
learned about these features by using them. Sometimes that meant using an app like 
Fiddler, or using a framework like the .NET SDK for Azure storage, and tracking the HTTPS 
traffic using Fiddler again. Other times I had to know where Azure logs some events. I 
remember feeling really frustrated with a new Azure storage feature, a simple 
file-to-cloud API. I had the newest SDK, but my file never fully wrote to the cloud. Some 
small ones did, but larger ones didn't. The experts said I'd get an exception if it 
failed. They asked if I was ignoring exceptions from their code. I simplified my repro 
case, by switching to public storage buckets, and making a simple command line report of 
how many bytes were transferred. I put the .EXE on a server and went home. In the 
morning, I learned I wasn't failing, the .NET layer was. The dev released a blog 
explanation at 11pm, and new release of SDK bits the next day. With the feature finally 
working, I could write about it down to its nuances, by triggering all the features the 
interface claimed to provide. [Setting Timeouts for Blob Service 
Operations](https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/Setting-Timeouts-for-Blob-Service-Operations) 
is the comprehensive documentation I wrote next.

## TECHNOLOGIES AND ME

Let's dive in!

### XML authoring tools like Oxygen or Arbortext Editor

  - **Used daily?:** No.
  - **Self-rating:** 6
  - **Comments:** I don't use this stuff daily, but still rate myself a 7, because I 
speak XML, and because I've worked closely with DocStudio, the XML-based content 
management behind MSDN. I've also used AuthorIT, which tags chunks. I believe in technology that pulls its weight.  

### Image editing/creation software

  - **Used daily?:** Yes.
  - **Self-rating:** 7
  - **Comments:** Let's get something straight: I can create a miserable image using the 
coolest software. I can also provide great images using rather average tools. In this 
example, I used Visio:
      
    ![](http://i.msdn.microsoft.com/dynimg/IC588554.png)

I also create animated gifs as a hobby:

Yeah, I use ffmpeg. So. I'm kind of a big deal.
  
### HTML

  - **Used daily?:** Yes.
  - **Self-rating:** 8
  - **Comments:** Yeah, I use HTML daily. I learned HTML before there was CSS. Now HTML 
can include JavaScript libraries that navigate the DOM and round-trips asynchronously 
with servers. My knowledge of HTML gets a solid 7! I'm comfortable with it. I write 
tricks in PHP. I use HTML tricks to run projects on multiple domains.

### Source control software

  - **Used daily?:** Yes.
  - **Self-rating:** 7
  - **Comments:** I use git and GitHub daily. I've made branches, pushed and pulled with 
it. [John's GitHub](https://github.com/mcfnord/)


![](img/final.png)

I like writing, getting the scoop, and delivering the news.

My current "job" is cleaning the house, animating gifs, and messing around on AWS.
