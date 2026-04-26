# Web server

4D has its own HTTP server, a powerful multithreaded server for static
and dynamic content. The tight integration has a considerable impact on
increased security.

Besides better code security (see below), this concept removes the
typical forgotten update problem. Since everything is integrated, there
is only one piece of software to update. The usual solutions require a
huge amount of software to keep up to date: PHP, OpenSSL, Apache,
NodeJS, etc. All of them need regular updates and it is common that some
parts remain unpatched for a long time, especially if they are used as a
service solution, without a dedicated IT team.

Web requests trigger 4D code, which responds to the request at the
application level, not just the database level. Tight integration allows
control of all requests, using custom authorization and implementation
building, of course TLS encrypted.

The integrated HTTP server also allows fine-grained control
justifications, for example for a REST server.

Since version 4D v16 R6, 4D now supports Perfect Forward Secrecy (PFS).
This gives you the highest level of security for your communications, by
default! Beyond the protection it provides, PFS support also increases
SSL verification test results, which is great for our customers.
Especially those who work with sensitive information.

The default security level of 4D Web Server has been increased to comply
with certain network security features (App Transport Security (ATS) on
iOS, for example), and allows for better results in web security
verification tests (e.g. SSL Labs).

To achieve this, we have:

enabled \"Perfect Forward Secrecy\", and

disabled the RC4 algorithm from the encryption list.

As a result, the 4D Web server gets an \"A\" in the SSL Labs rating,
with no action required!

Perfect Forward Secrecy (PFS) is a key exchange algorithm. It uses
Diffie-Hellman (DH) algorithms to generate session keys in such a way
that only the two parties involved in the communication can obtain them.

4D automatically activates PFS when TLS is enabled on the server. To do
this, 4D generates a \"dhparams.pem\" file - if it doesn't already
exist - that contains the private key of your DH server. If you use the
standard 4D cipher list, PFS is ready to use. If you prefer to use a
custom cipher list, check that it contains entries with ECDH or DH
algorithms.

To find out if PFS is enabled on your web server, run the \"WEB Read
Server Info\" command with the new \"perfectForwardSecrecy\" attribute.
This will check if all the necessary conditions to use PFS are met:

TLS is enabled

The cipher list contains at least one ECDH or DH algorithm

The file \"Dhparams.pem\" is present and valid

All SSL / TLS certificates are present

The RC4 algorithm has experienced security problems and is now
deprecated in the 4D web server. All RC4 ciphers have been removed from
the default cipher list and the \"RC4\" pattern has been added to the
cipher list to explicitly prohibit it.
