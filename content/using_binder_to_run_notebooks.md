Title: Using binder to run notebooks interactively
Date: 2020-08-07 14:00
Category: general
Author: Tobias Kölling
Summary: With binder, it is possible to prepare code examples such that readers can quickly start interacting with the code and data.
Tags: infrastructure

This post roughly describes the purpose binder and how binder is used within this blog.

## What is binder?

[Binder](https://mybinder.org) is a service for running notebooks hosted in git repositories interactively. At it's core, binder uses [repo2docker](https://repo2docker.readthedocs.io/) which transforms any git repository into a docker based operating system image, which contains all necessary software to run the code of the repository. mybinder.org is being run as a [federation of servers](https://binderhub.readthedocs.io/en/latest/federation/federation.html) by several companies and institutions. Binder is also open source, so it is possible to run binder on own premises or to join the binder federation by donating compute resources.

## What is needed to run data evaluation code in binder

To do useful data evaluation in binder, both the code and the data must be available publicly.

For the EUREC4A field campaign data is and will be hosted on [Aeris](https://eurec4a.aeris-data.fr/), from where all datasets are accessible via [OPeNDAP](https://www.opendap.org/). That way, it is easy to access datasets and subsets thereof from all over the world. Another option which we are currently investigating is to use [Zarr](https://zarr.readthedocs.io/), which started out as a Python library but actually defines a flexible data storage format which can naturally be served via HTTP. The netCDF developers are also currently working on [adding a Zarr variant](https://www.unidata.ucar.edu/blogs/developer/en/entry/overview-of-zarr-support-in) to netCDF, such that in future, Zarr archives will be available to everyone who is able to access netCDF.

Code can be shared via publicly available git repositories or package repositories. This blog is also a git repository and is used to share code examples, both as blog articles and as a code snippets to be run in binder.

## Configuring binder

In general, any github repository can directly be run within binder using [mybinder.org](https://mybinder.org/). This would run the repository in a default environment, which has only very few libraries installed. While it is possible to install further dependencies from within a running notebook, a better alternative is to configure binder by a series of [configuration files](https://repo2docker.readthedocs.io/en/latest/config_files.html), which can be stored in the users repository. These files are used to prepare a specialized docker image, which already contains all the mentioned dependencies. This approach has the great advantage that docker images are cached and thus the installation does not have to be performed again on every notebook start, but a cached version can directly be launched.

## Shorter startup delays

Binder recreates the whole docker image for every new commit of the repository which is loaded into binder. For a blog (and maybe other repositories as well) this may lead to many more required rebuilds than necessary, as most of the commits will only touch the articles but not the required library dependencies. To reduce the amount of unnecessary rebuilds, a [common method](https://discourse.jupyter.org/t/tip-speed-up-binder-launches-by-pulling-github-content-in-a-binder-link-with-nbgitpuller/922) is to use [nbgitpuller](https://github.com/jupyterhub/nbgitpuller). With nbgitpuller, it is possible to create a separate *environment repository* which is used to declare all dependencies but which likely will receive fewer commits. This repository will then be started by binder and immediately be instructed to pull in the actual code from the *data repository*. For this blog, we use [eurec4a/hackathon_env](https://github.com/eurec4a/hackathon_env) as an environment repository. Accordingly, if you want to add dependencies for new code examples, these additions must go into that repository. Using binder in this two-repository mode requires a slightly more complicated way of generating direct links to the notebooks. There is a [tool for it](http://nbgitpuller.link/?tab=binder) and a [function](https://github.com/eurec4a/hackathon2020_blog/blob/118571b75c2c743f056ba191d7330458ac61020b/pelicanconf.py#L60) which is used by this blog.
