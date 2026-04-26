# Network

<u>Recommended:</u>

- Use the old network layer up to version v15 R5

- Use the new network layer from version 16.2 public

*Please note: The old network layer is not available in the 64-bit
versions of 4D Developer (Windows and Mac) and in the 64-bit version of
4D Server (Mac only).*

It is very important for 4D Server to always have enough bandwidth to
communicate with its remote computers. If you share the bandwidth, you
will have to reserve part of it for 4D Server.

Indeed, when the bandwidth runs out, some packets are lost and this
inevitably causes errors on the Server side. If too many network errors
occur at the same time or too frequently, you will destabilize 4D
Server.

Also be aware that if you are using 4D Web Server and you want to
separate traffic for security and/or performance reasons, it is possible
to dedicate one network card to 4D Distant users and another to Web,
SOAP or REST requests.
