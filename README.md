---
layout: home
title: Just the Class
nav_exclude: true
permalink: index.html
seo:
  type: Course
  name: Just the Class
---

# Just the Class

Just the Class is a GitHub Pages template developed for the purpose of quickly deploying course websites. In addition to serving plain web pages and files, it provides a boilerplate for:

- [announcements](announcements.md),
- a [course calendar](calendar.md),
- a [staff](staff.md) page,
- and a weekly [schedule](schedule.md).

Just the Class is a template that extends the popular [Just the Docs](https://github.com/just-the-docs/just-the-docs) theme, which provides a robust and thoroughly-tested foundation for your website. Just the Docs include features such as:

- automatic [navigation structure](https://just-the-docs.github.io/just-the-docs/docs/navigation-structure/),
- instant, full-text [search](https://just-the-docs.github.io/just-the-docs/docs/search/) and page indexing,
- and a set of [UI components](https://just-the-docs.github.io/just-the-docs/docs/ui-components) and authoring [utilities](https://just-the-docs.github.io/just-the-docs/docs/utilities).

## Getting Started

Getting started with Just the Class is simple.

1. Create a [new repository based on Just the Class](https://github.com/kevinlin1/just-the-class/generate).
    - for CSW8, use the previous course repo to minimize the setup time: 
    - W22 ([github](https://github.com/ucsb-csw8/w22) / [web](https://ucsb-csw8.github.io/w22/)) 
    - S22 ([github](https://github.com/ucsb-csw8/s22) / [web](https://ucsb-csw8.github.io/s22/))
1. Update `_config.yml` and `index.md`/`README.md` with your course information. [Be sure to update the url and baseurl](https://mademistakes.com/mastering-jekyll/site-url-baseurl/).
1. Configure a [publishing source for GitHub Pages](https://help.github.com/en/articles/configuring-a-publishing-source-for-github-pages). Your course website is now live!
1. Edit and create `.md` [Markdown files](https://guides.github.com/features/mastering-markdown/) to add more content pages.
    - `_config.yml`- update first - its contents are not auto-refreshed like the .md pages do. To see the changes to its contents, stop/restart Jekyll
    - `about.md` - make sure to update the Syllabus and course policies
    - `announcements.md` - skip, if not using the website Announcements
    - `calendar.md` - the information from this file is displayed at the top of the page that lists weekly topics and due dates;
        - if not using reflections, make sure to comment-out that part of the instructions. 
        - The Calendar is populated using the files in the `_modules` folder. These are added semi-automatically, using a script `generate_due_dates.py` that hard-codes start and end dates, etc.
    - `faq.md` - make sure to update the QnA based on your course information. After you update the Syllabus and the Calendar, make sure you address the typical first-week questions and clarify the `#weekly-pattern-and-planning-your-work` section
        - can be omitted if you are short on time or you'd rather answer these repeated questions yourself
    - `index.md` - the front page of the course; some of the info there, like the course title, come from the `_config.yml` file 
    - `jekyll.sh` - no need to change: run it as a shortcut for the `bundle` command
    - `quiz.md` - make sure to update the instructions based on your course quiz structure and policies
        - can be omitted if you are short on time or you'd rather answer these repeated questions yourself
    - `schedule.md` - the information for it is pulled from the `_schedules/weekly.md` --> make sure to update the latter - usually done via a script
        - use the two scripts in `_modules` to automatically generate the weekly modules on the Calendar
        - read the script documentation and the TODOs that are included inside the `.py` files
    - `staff.md` - the information for it is pulled from the `_staffers` and images are in the `assets/images` --> make sure to update them (see the `_example.md` to help you get started with a template; there is a `404.png` for anyone who doesn't want their picture included) 
    - `success.md` - make sure to change the **Roadmap** to align with your course calendar
        - can be omitted if you are short on time 

* For the `ref/` folder, I recommend initially comitting the `goals.md`, since it's referenced in the Syllabus and `keyboard.md` (+ `debug`?); the `ide` shows them how to install Python and is part of the FAQ; the rest of them can be added later, when they become relevant.
    * `data-structures` - a comparison table for strings, lists, tuples and namedtuples, dictionaries
    * `debug` - a good one to release initially as well - contains common errors and troubleshooting tips
    * `goals` - a list of CSW8 learning goals/objectives
    * `ide` - how to set up IDLE + common issues/warnings; include when covering functions/IDE/Gradescope
    * `index` - auto-generated index page for this Category
    * `keyboard` - common keyboard symbols and their names
    * `labtocode` - how to convert lab instructions to code; include when covering functions
* Initial commit should include the following files (if using announcements): `README.md _announcements _config.yml _includes/ _layouts/ _modules/ _sass/  _schedules _staffers about.md announcements.md assets/ calendar.md faq.md index.md jekyll.sh ref/goals.md ref/keyboard.md schedule.md staff.md success.md `
    * include `debug.md`?

Just the Class has been used by instructors at Stanford University ([CS 161](https://stanford-cs161.github.io/winter2021/)), UC Berkeley ([Data 100](https://ds100.org/fa21/)), UC Santa Barbara ([CSW8](https://ucsb-csw8.github.io/s22/)), Northeastern University ([CS4530/5500](https://neu-se.github.io/CS4530-CS5500-Spring-2021/)), and Carnegie Mellon University ([17-450/17-950](https://cmu-crafting-software.github.io/)). Share your course website and find more examples in the [show and tell discussion](https://github.com/kevinlin1/just-the-class/discussions/categories/show-and-tell)!

### Local development environment

Just the Class requires no special Jekyll plugins and can run on GitHub Pages' standard Jekyll compiler. To setup a local development environment, clone your template repository and follow the GitHub Docs on [Testing your GitHub Pages site locally with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll).
