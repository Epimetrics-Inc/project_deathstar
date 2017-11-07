---
--- Drop api and basic_auth schemas
---
BEGIN;
DROP schema api CASCADE;
DROP schema basic_auth CASCADE;
COMMIT;

--
-- Revoke privileges and delete web_anon and authenticator;
--
BEGIN;

REVOKE select on table pg_authid from web_anon;
DROP USER web_anon;
DROP USER authenticator;

COMMIT;

