# Reddit Crawler ![](https://img.shields.io/apm/l/vim-mode.svg)
This is a python code based on Scrapy package to crawl top 1000 posts of all time of a sub reddit.
Be aware that this code is published on Agust 8, 2022, and if Reddit will be updated in the future this code may not work properly.
## Prerequisites
Scrapy python package.
If you don't have scrapy do `pip install scrapy`

## How to use it?
##### 1- set the reddit sub:
at */reddit/reddit/spiders* there is a **\__init__.py** and there is a variable named **sub_reddit** that is initialize like this:
```python
sub_reddit = "shortstories"
```
you can change this  to crawl the sub that you want.
##### 2- run:
go to the file */reddit/reddit/spiders* and run this in the terminal

    scrapy crawl reddit -o [name of file to write into].jl
    

and the data will be stored in  [name of file to write into].jl at */reddit/reddit/spiders*

## How is the output?
The output is a JSON Lines file format. It contains the title, upvotes and post text content.
for example, this is one sample:
```json
{
  "upvotes": "3",
  "title": "[MT] Some questions since I’m new",
  "flair": "Meta Post",
  "text": [
    "Will breaking grammar rules and norms about punctuation or how paragraphs are get a pass if I am aware of what I am doing and doing it for a reason? I’ve had a short story I’ve been really excited to post for a while now, but I notice those rules and realize I would get struck down by them.",
    "The specific concept is a way to show mental disorganization in a character that is mentally unwell in ways that are inspired by myself."
  ],
  "url": "https://old.reddit.com/r/shortstories/new/?count=300&after=t3_vohy2z"
}
```
## Author

* **Peyman Mohseni kiasari**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
