# Operating system

<u>Recommended:</u> OS certified by 4D

Important: Deploy 4D applications on operating systems certified by our
Quality Department. The software and system requirements are available
on our website: <https://us.4d.com/resources/>.

- **<u>On Windows:</u>**

    - To deploy the **4D** application on workstations: **Windows 10 (end
    of MS support in October 2025)** or **Windows 11**,

    - To deploy the 4D Server application on a server or the 4D
    application on an application server:

        - **Windows Server 2016 (end of MS extended support in January
      2027)**,

        - **Windows Server 2019**,

        - **Windows Server 2022**,

        - **Windows Server 2025 (20.6 LTS minimum or 20 R8 minimum)**;

    - Deploy the **4D Server** application on a dedicated machine (on
    Windows Server, disable all roles, including the file server role
    installed by default);

    - Deploy the 64-bit line:

        - **4D Server** is available in 64-bit version starting with v12,

        - **4D** is available in 64-bit version from version v16 R;

    - For performance reasons, we also invite you to disable the local
    security policy \"Microsoft network client: digitally signed
    communications (when accepted by the server)\" in the security
    options, which decreases performance by 15% when active;

    - The default settings for Windows and Windows Server computers are
    optimized to save power. This is the best setting for desktop use.
    However, a setting of \"high performance\" provides up to twice the
    performance of \"normal\" mode.

- **<u>On the Mac:</u>**

    - To deploy **4D** or **4D Server** applications:

        - macOS **Ventura** (**13**);

        - macOS **Sonoma** (**14**);

        - macOS **Sequoia** (**15**) ;

    - Deploying 64-bit line:

        - **4D Server** is available in 64-bit versions starting with v15,

        - **4D** is available in 64-bit version from version v16.

- **<u>Screen resolution:</u>**

    - Dialogs in 4D, such as the search editor, require a minimum screen
    resolution of **1280 x 1024 pixels** ;

    - Depending on the 4D application code used, applications may require
    smaller resolutions (e.g., for mobile devices) or larger resolutions
    (e.g., large screens and high-resolution displays).

The 64-bit versions allow single-user 4D applications as well as remote
4D applications to take full advantage of 64-bit operating systems. The
main advantage of the 64-bit architecture is that a larger memory size
can be addressed.

Although largely rewritten, 64-bit 4D applications are highly compatible
with current 4D databases. However, since they use the latest
technologies, we had to update some functions and stop others.

On the other hand, the implementation of the 64-bit architecture has
given us the opportunity to support powerful features such as preemptive
(multi-threaded) 4D processes, modernized printers, fast state and label
editors, and native object animations (4D 64-bit on OS X).
