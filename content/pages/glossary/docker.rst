Docker
######
:date: 2016-09-03 16:15
:author: aidanharris
:slug: docker
:status: published

Docker is an open-source project that automates the deployment of Linux
applications inside software containers. Quote of features from Docker
web pages:

    Docker containers wrap up a piece of software in a complete
    filesystem that contains everything it needs to run: code, runtime,
    system tools, system libraries – anything you can install on a
    server. This guarantees that it will always run the same, regardless
    of the environment it is running in.

Docker provides an additional layer of abstraction and automation of
operating-system-level virtualization on Linux. Docker uses the resource
isolation features of the Linux kernel such as cgroups and kernel
namespaces, and a union-capable file system such as aufs and others to
allow independent "containers" to run within a single Linux instance,
avoiding the overhead of starting and maintaining virtual machines.

The Linux kernel's support for namespaces mostly isolates an
application's view of the operating environment, including process
trees, network, user IDs and mounted file systems, while the kernel's
cgroups provide resource limiting, including the CPU, memory, block I/O
and network. Since version 0.9, Docker includes the libcontainer library
as its own way to directly use virtualization facilities provided by the
Linux kernel, in addition to using abstracted virtualization interfaces
via libvirt, LXC (Linux Containers) and systemd-nspawn.

**Read More on
`Wikipedia <https://en.wikipedia.org/wiki/Docker_(software)>`__**
