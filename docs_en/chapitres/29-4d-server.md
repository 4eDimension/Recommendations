# 4D Server

4D Server is an integrated client/server development system, optimized
to create robust enterprise applications with an integrated database
system. Although 4D can send data (with standards such as HTTP, SOAP,
ODBC or OCI) or can be accessed from the outside (with HTTP, SOAP,
ODBC/SQL), the primary use is based on the internal development language
\"4D\", using an internal and proprietary network protocol to
communicate between the client and the server.

The network communication supports TLS 1.3 encryption, either with a
predefined key (no SSL certificate required) or with a file containing a
key.

The close connection between the development language and the network
communication allows for a high-level construction in the protection
concept, avoiding typical attack scenarios such as SQL injection or
buffer overflow attacks.

The 4D language is a powerful and mature language, perfectly designed
for building enterprise application systems. It offers more than 1,500
commands, covering database operations (sorts, queries, creations,
transactions and so on), printing, communication with other devices or
computers, document management, a window or user interface, and much
more. Take a look at the 4D language manual for more details.

The language itself is segmented, even in interpreted mode (development
or prototyping), it is never run as a text evaluation. In production
mode, the language is compiled and includes automatic version range
control against buffer overflow attacks.
