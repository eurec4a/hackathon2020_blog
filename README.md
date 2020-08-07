# EUREC4A Hackathon 2020 blog

Welcome to the backend of the EUREC4A 2020 hackathon blog. If you want to see the blog, please go [this way](https://eurec4a.github.io/hackathon2020_blog/).
If you want to post anything, please add your article into the content subfolder.
Currently [markdown files](https://docs.getpelican.com/en/stable/quickstart.html#create-an-article) and [jupyter notebooks](https://github.com/danielfrg/pelican-jupyter) are supported.

When creating a blog article from an jupyter notebook, you have to add a `.nbdata` file including some additional metadata with otherwise the same name. Please have a look at the currently existing articles for examples.

Before pushing your updates, please have a look at your site locally, you can run a testing server using
```bash
pelican content -r -l
```
and access the Site at [http://localhost:8000/](http://localhost:8000/).

If you are happy with your new article, please file a pull request.

## requirements
In order to run the site generator locally, you'll have to install some dependencies:
```bash
pip install pelican[Markdown] pelican-jupyter
```
