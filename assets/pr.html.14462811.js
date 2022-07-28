import{_ as o,a as i,b as n,c as l,d as h}from"./PR.7acaac3b.js";import{_ as c,r as d,o as p,c as u,a as e,b as s,F as _,e as t,d as a}from"./app.92764aa2.js";const b={},m=t('<p><img src="'+o+'" alt="Welcome"></p><p>PR\u5168\u79F0\u4E3APull Request\uFF0C\u5B83\u662F\u4E00\u79CD\u4EE3\u7801\u5E93\u7684\u534F\u4F5C\u65B9\u5F0F\u3002\u5F00\u53D1\u8005\u53EF\u4EE5\u901A\u8FC7PR\u5C06\u81EA\u5DF1\u5728\u4EE3\u7801\u5E93\u7684\u4FEE\u6539\u901A\u77E5\u5230\u4EE3\u7801\u5E93\u8D1F\u8D23\u4EBA\uFF0C\u7531\u539F\u4F5C\u8005\u8BC4\u5BA1\u4EE3\u7801\u5E76\u51B3\u5B9A\u662F\u5426\u80FD\u5408\u5165\u3002</p><div class="custom-container tip"><p class="custom-container-title">TIP</p><p>Pull requests let you tell others about changes you&#39;ve pushed to a branch in a repository on GitHub. Once a pull request is opened, you can discuss and review the potential changes with collaborators and add follow-up commits before your changes are merged into the base branch.</p></div><h1 id="pr\u64CD\u4F5C\u6D41\u7A0B" tabindex="-1"><a class="header-anchor" href="#pr\u64CD\u4F5C\u6D41\u7A0B" aria-hidden="true">#</a> PR\u64CD\u4F5C\u6D41\u7A0B</h1><h2 id="\u4E00\u3001fork\u76EE\u6807\u4EE3\u7801\u5E93" tabindex="-1"><a class="header-anchor" href="#\u4E00\u3001fork\u76EE\u6807\u4EE3\u7801\u5E93" aria-hidden="true">#</a> \u4E00\u3001Fork\u76EE\u6807\u4EE3\u7801\u5E93</h2><p><img src="'+i+'" alt="fork"></p>',6),g=a("\u70B9\u51FBFork\u540E\uFF0C\u4F1A\u5728\u81EA\u5DF1\u540D\u4E0B\u4EA7\u751F\u4E00\u4E2A\u76F8\u540C\u4EE3\u7801\u5E93\uFF0C\u6BD4\u5982\u6211Fork CodeAnalysis\u9879\u76EE\u540E\uFF0C\u4F1A\u5728\u6211\u540D\u4E0B\u591A\u51FA\u4E00\u4E2ACodeAnalysis\u4EE3\u7801\u5E93\uFF0C\u5730\u5740\u4E3A"),f={href:"https://github.com/Lingghh/CodeAnalysis",target:"_blank",rel:"noopener noreferrer"},k=a("https://github.com/Lingghh/CodeAnalysis"),q=t(`<h2 id="\u4E8C\u3001\u514B\u9686fork\u7684\u4EE3\u7801\u5E93\u5E76\u521B\u5EFA\u5206\u652F" tabindex="-1"><a class="header-anchor" href="#\u4E8C\u3001\u514B\u9686fork\u7684\u4EE3\u7801\u5E93\u5E76\u521B\u5EFA\u5206\u652F" aria-hidden="true">#</a> \u4E8C\u3001\u514B\u9686Fork\u7684\u4EE3\u7801\u5E93\u5E76\u521B\u5EFA\u5206\u652F</h2><p>\u5728\u672C\u5730\u514B\u9686Fork\u7684\u4EE3\u7801\u5E93\u5E76\u521B\u5EFA\u5206\u652F</p><div class="language-bash ext-sh line-numbers-mode"><pre class="language-bash"><code>git clone https://github.com/Lingghh/CodeAnalysis
git checkout -b dev/add_qa_20220301
</code></pre><div class="line-numbers" aria-hidden="true"><span class="line-number">1</span><br><span class="line-number">2</span><br></div></div><p>\u6CE8\uFF1A\u4E5F\u53EF\u4EE5\u5728\u81EA\u5DF1Fork\u7684\u4EE3\u7801\u5E93GitHub\u9875\u9762\u4E0A\u521B\u5EFA\u5206\u652F\u3002</p><p><img src="`+n+'" alt="fork1"></p><p>\u63A5\u4E0B\u6765\u5C31\u53EF\u4EE5\u5728\u672C\u5730\u4FEE\u6539\u4EE3\u7801\uFF0C\u4FEE\u6539\u5B8C\u6210\u540E\u5148push\u5230Fork\u7684\u4EE3\u7801\u5E93\u4E2D.</p><h2 id="\u4E09\u3001\u5728\u76EE\u6807\u9879\u76EE\u4E2D\u63D0\u4EA4pr" tabindex="-1"><a class="header-anchor" href="#\u4E09\u3001\u5728\u76EE\u6807\u9879\u76EE\u4E2D\u63D0\u4EA4pr" aria-hidden="true">#</a> \u4E09\u3001\u5728\u76EE\u6807\u9879\u76EE\u4E2D\u63D0\u4EA4PR</h2><h3 id="_1-\u8FDB\u5165\u5230\u76EE\u6807\u9879\u76EE\u4E2D-\u70B9\u51FBpull-requests-tab-\u518D\u70B9\u51FBnew-pull-request\u5C31\u4F1A\u8FDB\u5165\u5230\u521B\u5EFApr\u7684\u9875\u9762" tabindex="-1"><a class="header-anchor" href="#_1-\u8FDB\u5165\u5230\u76EE\u6807\u9879\u76EE\u4E2D-\u70B9\u51FBpull-requests-tab-\u518D\u70B9\u51FBnew-pull-request\u5C31\u4F1A\u8FDB\u5165\u5230\u521B\u5EFApr\u7684\u9875\u9762" aria-hidden="true">#</a> 1.\u8FDB\u5165\u5230\u76EE\u6807\u9879\u76EE\u4E2D\uFF0C\u70B9\u51FBPull requests Tab\uFF0C\u518D\u70B9\u51FBNew pull request\u5C31\u4F1A\u8FDB\u5165\u5230\u521B\u5EFAPR\u7684\u9875\u9762</h3><p><img src="'+l+'" alt="New pull request"></p><h3 id="_2-\u8FDB\u5165pr\u9875\u9762\u540E" tabindex="-1"><a class="header-anchor" href="#_2-\u8FDB\u5165pr\u9875\u9762\u540E" aria-hidden="true">#</a> 2.\u8FDB\u5165PR\u9875\u9762\u540E</h3><ul><li><p>\u70B9\u51FBcompare across forks \u3002</p></li><li><p>\u70B9\u51FBhead repository \u3002</p></li><li><p>\u9009\u62E9\u81EA\u5DF1Fork\u7684\u4EE3\u7801\u5E93\u548C\u6BD4\u8F83\u7684\u5206\u652F\uFF0C\u6BD4\u5982\u6211\u8FD9\u91CC\u9009\u62E9Lingghh/CodeAnalysis\u548C\u5F85\u5408\u5165\u7684\u5206\u652Fdev/add_arm64_file \u3002</p></li><li><p>\u6700\u540E\u786E\u8BA4commits\u548Cchanged files\u662F\u5426\u51C6\u786E\uFF0C\u5982\u679C\u6CA1\u6709\u95EE\u9898\u5C31\u53EF\u4EE5\u70B9\u51FBCreate pull request \u3002</p><p><img src="'+h+'" alt="PR"></p></li></ul><p>PR\u521B\u5EFA\u540E\uFF0C\u4EE3\u7801\u5E93\u7BA1\u7406\u5458\u4F1A\u8BC4\u5BA1\u4F60\u63D0\u4EA4\u7684\u4EE3\u7801\uFF0C\u5E76\u51B3\u5B9A\u662F\u5426\u63A5\u53D7\u8BE5PR\u3002</p>',12),x={id:"\u66F4\u591A\u4FE1\u606F\u8BF7\u53C2\u9605github-pullrequest\u5B98\u65B9\u6587\u6863",tabindex:"-1"},P=e("a",{class:"header-anchor",href:"#\u66F4\u591A\u4FE1\u606F\u8BF7\u53C2\u9605github-pullrequest\u5B98\u65B9\u6587\u6863","aria-hidden":"true"},"#",-1),v=a(" \u66F4\u591A\u4FE1\u606F\u8BF7\u53C2\u9605"),y={href:"https://docs.github.com/cn/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests/",target:"_blank",rel:"noopener noreferrer"},R=a("GitHub PullRequest\u5B98\u65B9\u6587\u6863"),w=e("h2",{id:"tca\u56E2\u961F\u8BDA\u9080\u60A8\u7684\u52A0\u5165",tabindex:"-1"},[e("a",{class:"header-anchor",href:"#tca\u56E2\u961F\u8BDA\u9080\u60A8\u7684\u52A0\u5165","aria-hidden":"true"},"#"),a(" TCA\u56E2\u961F\u8BDA\u9080\u60A8\u7684\u52A0\u5165")],-1);function F(C,A){const r=d("ExternalLinkIcon");return p(),u(_,null,[m,e("p",null,[g,e("a",f,[k,s(r)])]),q,e("h2",x,[P,v,e("a",y,[R,s(r)])]),w],64)}var T=c(b,[["render",F],["__file","pr.html.vue"]]);export{T as default};
