# Forms, APIs, and server inputs

Map each entry point to validation, authorization, storage, rendering, or outbound requests. Select checks for injection, contextual escaping, CSRF, upload execution, path traversal, SSRF, mail header injection, mass assignment, and abuse limits only where relevant.

For webhooks verify signature handling and replay constraints against provider documentation. For commerce inspect server-side payment state, not success-page redirects. Evidence should trace the source to the sensitive operation and identify upstream protections. Avoid real mail, payments, destructive payloads, or provider traffic outside authorization.
