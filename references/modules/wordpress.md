# WordPress plugin checklist

Record checks under the `cms` module and link applicable identity, inputs, credits and operations evidence. Use this checklist for defensive review of the actual WordPress and PHP versions in scope.

- Inventory state-changing and sensitive read paths exposed through admin forms, REST, AJAX, shortcodes, scheduled jobs and command-line tools. For each path, trace the capability, target object or site, validation, and persisted or disclosed data. Check that REST permission callbacks and browser nonce checks preserve the intended authorization model.
- Trace request data into settings, options, metadata, custom tables, HTML and external requests. Check input constraints, context-sensitive output escaping, safe persistence, destination restrictions, upload handling and protection of credentials and private data.
- In multisite, distinguish site and network privileges, configuration and storage. Confirm the intended site context during activation, updates, jobs and teardown. Review migration and uninstall boundaries, including which data must remain.
- Prefer code and configuration evidence. In a disposable WordPress environment, use ordinary supported operations and synthetic users to confirm expected access for each applicable role and the rejection of unauthorized operations. Record scope, version, result and evidence gaps.

[WordPress Plugin Developer Handbook](https://developer.wordpress.org/plugins/) · [WordPress security APIs](https://developer.wordpress.org/apis/security/)
