 How Not To Use Docker
######################
:date: 2016-06-06 17:11
:author: aidanharris
:category: Docker
:slug: how-not-to-use-docker
:status: published
:thumbnail: uploads/2016/06/20140516082706Docker_container_engine_logo.png
:headingTheme: dark
:headingIconFont: devicons devicons-docker

`Docker <https://aidanharr.is/glossary/docker/>`__ is an amazing tool
that's perfect for building Microservices. I'm still learning to use it
and if I'm being honest, I quite like it. I could see its power from the
onset. Docker is essentially a virtual machine (VM) without the overhead
of a VM (note: Docker isn't actually a VM I'm `generalising <https://blog.docker.com/2016/03/containers-are-not-vms/>`__
here) unless you (ab)use it like me. You might have noticed that I've
recently added a `"Portfolio" section <//aidanharr.is/portfolio/>`__ to
this website to better market myself. The problem I had, was taking a
local `Vagrant <https://vagrantup.com>`__ environment and deploying it
to an existing VPS. Docker solves this problem rather nicely. It's a
horrible way to use Docker but all I needed to do to get things up and
running was create a Dockerfile using the `ubuntu:trusty <https://hub.docker.com/_/ubuntu/>`__ image and add each
line of my shell provisioning script to the Dockerfile as RUN statements
and create a bootstrap file to handle starting the LAMP stack once a
container has started. The result works rather nicely, however, I'll
likely investigate alternative solutions since monolithic Docker
containers are unlikely to hold their own against large amounts of
traffic and may not scale very well.
