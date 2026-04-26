# Physical or virtual machine

<u>Recommended:</u> dedicated physical machine per 4D application

We recommend deploying one 4D application per virtual or physical
machine.

Even if 4D runs in a virtual environment (on-premise or in the Cloud)
and is therefore eligible in terms of operability, our experience shows
that a physical machine offers better performance over time with
equivalent resources.

If you are not required to virtualize the 4D server in production, we
recommend that you first deploy it on a physical machine. Then, in a
second step, program extensive tests in a virtual environment. This will
give you the advantage of being able to compare the 2 solutions.

However, if there is an advantage to virtualization, it is the
flexibility of resource allocation (CPU, memory in particular). It is
possible to allocate additional resources later, or even to allocate
resources in real time, depending on the activity of the machine. We
have a number of customers who work with virtualized environments, and
more and more of them. We even have customers deploying virtualized TSE
servers on blade servers.

However, we do not have any official documents certifying the operation
of 4D in a virtualized environment or favoring one solution over
another.

We only recommend to make sure that the performance of the machine is
sufficient in terms of resources (memory, processor, etc.) or that the
virtualized operating system is certified with the version of 4D
installed.

In general, CPU and RAM resources should be a little higher in a
virtualized environment than in a non-virtualized solution.

Moreover, the performance observed depends greatly on the virtual
machine's parameters (CPU, memory, etc.) but also on the hard disk and
the network card (characteristics, is it shared, dedicated, correctly
configured, etc.), the solution used, the version of the solution and
the system on which the solution is installed. For this part, I invite
you to consult the websites and forums of virtualized solution editors
as well as comparative studies.
