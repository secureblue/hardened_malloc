# hardened_malloc

[![hardened_malloc](https://img.shields.io/badge/dynamic/json?color=blue&label=hardened_malloc&query=builds.latest.source_package.version&url=https%3A%2F%2Fcopr.fedorainfracloud.org%2Fapi_3%2Fpackage%3Fownername%3Dsecureblue%26projectname%3Dhardened_malloc%26packagename%3Dhardened_malloc%26with_latest_build%3DTrue)](https://copr.fedorainfracloud.org/coprs/secureblue/hardened_malloc/package/hardened_malloc/)

RPM packaging for GrapheneOS's [hardened_malloc](https://github.com/GrapheneOS/hardened_malloc). Supports x86_64 and aarch64, including builds for x86_64 optimization levels.

> This is a security-focused general purpose memory allocator providing the
> malloc API along with various extensions. It provides substantial hardening
> against heapcorruption vulnerabilities. The security-focused design also leads
> to much less metadata overhead and memory waste from fragmentation than a more
> traditional allocator design. It aims to provide decent overall performance
> with a focus on long-term performance and memory usage rather than allocator
> micro-benchmarks. It offers scalability via a configurable number of entirely
> independently arenas, with the internal locking within arenas further divided
> up per size class.
