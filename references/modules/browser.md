# Browser and frontend

Inventory templates, DOM sinks, embedded content, analytics, third-party scripts, storage, and sensitive responses. Select checks for DOM XSS, script trust, CORS, framing, cookie attributes, CSP, cache isolation, and actual secret exposure.

Distinguish public frontend configuration from credentials with privileged access. Judge browser controls against observed responses and deployment context; do not prescribe headers without their purpose. TLS termination at a proxy needs deployment evidence. Record the browser-to-service boundaries and data shared with integrations; unknown provider settings remain unverified.
